import time
import krpc
import math
conn = krpc.connect(name='Sub-orbital flight')

turn_start_altitude = 250
turn_end_altitude = 50000
target_apoapsis = 150000
turn_angle = 0
vessel = conn.space_center.active_vessel
accent = True
drag_max = 80
circurlarize = False
stage_2 = True
stage_3 = True
stage_1_resources = vessel.resources_in_decouple_stage(stage=1, cumulative=False)
stage_0_resources = vessel.resources_in_decouple_stage(stage=0, cumulative=False)
srb_fuel = conn.add_stream(stage_1_resources.amount, 'SolidFuel')
booster_fuel = conn.add_stream(stage_0_resources.amount, 'LiquidFuel')
ut = conn.add_stream(getattr, conn.space_center, 'ut')
altitude = conn.add_stream(getattr, vessel.flight(), 'mean_altitude')
apoapsis = conn.add_stream(getattr, vessel.orbit, 'apoapsis_altitude')
vessel.auto_pilot.target_pitch_and_heading(90, 90)
vessel.auto_pilot.engage()
vessel.control.throttle = 1
time.sleep(1)

print('Launch!')
vessel.control.activate_next_stage()


print('Gravity turn')
while  vessel.flight(vessel.orbit.body.reference_frame).vertical_speed > -0.1 and accent == True:
    drag = vessel.flight(vessel.orbit.body.reference_frame).drag[2]
    #print(apoapsis())

    vessel.control.throttle = (1 - ( drag/drag_max))

    # Gravity turn
    if altitude() > turn_start_altitude and altitude() < turn_end_altitude:
        frac = ((altitude() - turn_start_altitude) /
                (turn_end_altitude - turn_start_altitude))
        new_turn_angle = frac * 90
        if abs(new_turn_angle - turn_angle) > 0.5:
            turn_angle = new_turn_angle
            vessel.auto_pilot.target_pitch_and_heading(90-turn_angle, 90)
    if altitude() > turn_end_altitude:
        accent = False
        insertion = True
    if srb_fuel() == 0 and stage_3 == True:
        vessel.control.activate_next_stage()
        stage_3 = False

if booster_fuel() == 0 and stage_2 == True:
    vessel.control.activate_next_stage()
    stage_2 = False

print('insertion')
while accent == False and insertion == True:
    if booster_fuel() == 0 and stage_2 == True:
        vessel.control.activate_next_stage()
        stage_2 = False
    vessel.auto_pilot.target_pitch_and_heading(0, 90)
    vessel.control.throttle = 5 * (1 - (apoapsis()/target_apoapsis))
    if altitude() >= 70000 and target_apoapsis <= 0.999 * apoapsis():
        insertion = False
        circurlarize = True
        vessel.control.throttle  = 0

if circurlarize == True:
    print('Planning circularization burn')
    mu = vessel.orbit.body.gravitational_parameter
    r = vessel.orbit.apoapsis
    a1 = vessel.orbit.semi_major_axis
    a2 = r
    v1 = math.sqrt(mu*((2./r)-(1./a1)))
    v2 = math.sqrt(mu*((2./r)-(1./a2)))
    delta_v = v2 - v1
    node = vessel.control.add_node(
        ut() + vessel.orbit.time_to_apoapsis, prograde=delta_v)

    # Calculate burn time (using rocket equation)
    F = vessel.available_thrust
    Isp = vessel.specific_impulse * 9.82
    m0 = vessel.mass
    m1 = m0 / math.exp(delta_v/Isp)
    flow_rate = F / Isp
    burn_time = (m0 - m1) / flow_rate
    print('Orientating ship for circularization burn')
    vessel.auto_pilot.reference_frame = node.reference_frame
    vessel.auto_pilot.target_direction = (0, 1, 0)
    vessel.auto_pilot.wait()

    # Wait until burn
    print('Waiting until circularization burn')
    burn_ut = ut() + vessel.orbit.time_to_apoapsis - (burn_time/2.)
    lead_time = 5
    conn.space_center.warp_to(burn_ut - lead_time)

    # Execute burn
    print('Ready to execute burn')
    time_to_apoapsis = conn.add_stream(getattr, vessel.orbit, 'time_to_apoapsis')
    while time_to_apoapsis() - (burn_time/2.) > 0:
        pass
    print('Executing burn')
    vessel.control.throttle = 1.0
    time.sleep(burn_time - 0.1)
    print('Fine tuning')
    vessel.control.throttle = 0.05
    remaining_burn = conn.add_stream(node.remaining_burn_vector, node.reference_frame)
    while remaining_burn()[1] > 0:
        pass
    vessel.control.throttle = 0.0
    node.remove()

    print('Launch complete')
    circurlarize = False


#    if apoapsis() < target_apoapsis:
#        vessel.control.throttle = (1 - (apoapsis()/(target_apoapsis + 2000)))
#    if apoapsis() >= target_apoapsis:
#
