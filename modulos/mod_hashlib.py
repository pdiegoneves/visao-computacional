import hashlib

# verificar os algoritimos
print(hashlib.algorithms_available)

# verificar os algoritomos do SO
print(hashlib.algorithms_guaranteed)

algorithm = hashlib.sha256()
print(algorithm.digest())
message = "A melhor forma de prever o futuro é criá-lo".encode()
algorithm.update(message)
print(algorithm.hexdigest())

