# vars for cyper suite
N = 23 # shared prime
g = 5 # shared base

a = 6  # alice secret
b = 15 # bobs secret

print("Shared Prime: " , N)
print("Shared Base: " , g)

# Alice sends Bob A=g^a mod N
A = (g**a) % N
print("Alice sends: " , A)

# Bob Sends Alice B = g^b mod N
B = (g**b) % N
print("Bob sends: " , B)

print("\n--------------------\n")
print("Calculated shared secrets: " )

# alice s = B^a mod N
sA = (B ** a) % N
# bob s = A^b mod N
sB = (A ** b) % N

print("     Alice Shared Secret: ", sA)
print("     Bob Shared Secret:   ", sB)
