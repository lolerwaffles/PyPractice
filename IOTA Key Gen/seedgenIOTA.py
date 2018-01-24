import secrets
charLib= ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","9"]
initSeed = []
secondSeedPermutation = []
tertiarySeedPermutation = []
finalSeed = ""
for i in range(0,1048576):
    initSeed.append(secrets.choice(charLib))
for i in range(0,1048576):
    secondSeedPermutation.append(secrets.choice(initSeed))
for i in range(0,1048576):
    tertiarySeedPermutation.append(secrets.choice(secondSeedPermutation))

while len(finalSeed) < 81:
    finalSeed = finalSeed + tertiarySeedPermutation[secrets.randbelow(1048576)]
print(finalSeed)
