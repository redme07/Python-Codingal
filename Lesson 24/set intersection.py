setx = {"green", "blue", "red", "orange", "purple"}
sety = {"black", "white", "red", "orange", "yellow"}
print(setx)
print(sety)

setz = setx.intersection(sety)
seta = setx.union(sety)
setb = setx.difference(sety)

print(setz)
print(seta)
print(setb)