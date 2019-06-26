
primus_members = ['Les Claypool', 'Larry LaLonde', 'Herb']
print("FRIZZLE FRY - 1990")
print(*primus_members, sep="\n")

primus_members.append('Jay Lane')
print("\nSAILING THE SEAS OF CHEESE - 1991")
print(*primus_members, sep="\n")

del primus_members[-1]
print("\nPORK SODA - 1993")
print(*primus_members, sep="\n")

print("\nTALES FROM THE PUNCHBOWL - 1995")
print(*primus_members, sep="\n")


del primus_members[-1]
primus_members.append('Bryan Mantia')
print("\nBROWN ALBUM - 1997")
print(*primus_members, sep="\n")

print("\nANTIPOP - 1999")
print(*primus_members, sep="\n")

del primus_members[-1]
primus_members.append('Jay lane')
print("\nGREEN NAUGAHYDE - 2011")
print(*primus_members, sep="\n")

del primus_members[-1]
primus_members.append('Herb')
primus_members.append('Mike Dillon')
primus_members.append('Sam Bass')
print("\nPRIMUS AND THE CHOCOLATE FACTORY WITH THE FUNGI ENSEMBLE - 2014")
print(*primus_members, sep="\n")

del primus_members[3:]
primus_members.append('Justin Chancellor')
print("\nTHE DESATURATING SEVEN - 2017")
print(*primus_members, sep="\n")
