import secrets
charLib= ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","9"]
seed = []
secondSeedPermutation = []
tertiarySeedPermutation = []
finalSeed = ""

for i in range(0,secrets.randbelow(10240)):
    for i in range(0,secrets.randbelow(1024)):
        seed.append(secrets.choice(charLib))
    charLib = seed

while len(finalSeed) < 81:
    finalSeed = finalSeed + seed[secrets.randbelow(1024)]
print(finalSeed)
