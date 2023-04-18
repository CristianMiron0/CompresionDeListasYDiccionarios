asistencias = {"Ana": (1, 2, 3, 5, 6), "Luis": (2, 3, 4, 6, 7)}
# 1.
cSesiones1 = 0

for nombre, sesiones in asistencias.items():
    print(nombre,len(sesiones))
    cSesiones1 += len(sesiones)

print("1.", cSesiones1)

# 2.
cSesiones2 = 0
cList2 = []
for x in asistencias["Ana"]:
    if x in asistencias["Luis"]:
        cSesiones2 += 1
        cList2.append(x)

print("2.", cList2)

# 2.1
cList2 = [x for x in asistencias["Ana"] if x in asistencias ["Luis"]]

print("2.", cList2)

# 3.
cSesiones3 = 0
cList3 = []
for x in asistencias["Ana"]:
    if x not in asistencias["Luis"]:
        cSesiones3 += 1
        cList3.append(x)
for x in asistencias["Luis"]:
    if x not in asistencias["Ana"]:
        cSesiones3 += 1
        cList3.append(x)

print("3.", cList3)

# 3.1
anaSet = set(asistencias["Ana"])
luisSet = set(asistencias["Luis"])

cList3 = [x for x in anaSet if x not in luisSet] + [x for x in luisSet if x not in anaSet]
cSesiones3 = len(cList3)

print("3.", cList3)

# 4.
cSesiones4 = 0
cList4 = []
for x in asistencias["Ana"]:
    if x not in asistencias["Luis"]:
        cSesiones4 = 0
        cList4.append(x)

print("4.", cList4)

# 4.1
cList4 = [x for x in asistencias["Ana"] if x not in asistencias["Luis"]]
print("4.", cList4)

# 5.
cSesiones5 = 0
cList5 = []
for x in asistencias["Luis"]:
    if x not in asistencias["Ana"]:
        cSesiones5 = 0
        cList5.append(x)

print("5.", cList5)

# 5.1
cList5 = [x for x in asistencias["Luis"] if x not in asistencias["Ana"]]
print("5.", cList5)
