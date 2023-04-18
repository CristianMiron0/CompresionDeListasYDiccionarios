asistencias = {"Ana": (1, 2, 3, 5, 6), "Luis": (2, 3, 4, 6, 7)}

# 1. 
cSesiones = 0

for nombre, sesiones in asistencias.items():
    print(nombre,len(sesiones))
    cSesiones += len(sesiones)

print(cSesiones)

# 2. 
ana = set(asistencias["Ana"])
luis = set(asistencias["Luis"])
sesionesDosAlumnos = ana.intersection(luis)
print(sesionesDosAlumnos)

# 3. 
def sesionesDiferente(alumno1, alumno2):
    asistenciasAlumno1 = set(asistencias[alumno1])
    asistenciasAlumno2 = set(asistencias[alumno2])
    sesionesAlumno1 = asistenciasAlumno1.difference(asistenciasAlumno2)
    sesionesAlumno2 = asistenciasAlumno2.difference(asistenciasAlumno1)
    return sesionesAlumno1.union(sesionesAlumno2)

alumno1 = "Ana"
alumno2 = "Luis"
sesiones = sesionesDiferente(alumno1, alumno2)
print(f"Sesiones diferente: {sesiones}")

# 4.
ana = set(asistencias["Ana"])
luis = set(asistencias["Luis"])

soloAna = ana - luis
print(f"Solo Ana:{soloAna}")
# 5.
ana = set(asistencias["Ana"])
luis = set(asistencias["Luis"])

soloLuis = luis - ana
print(f"Solo Luis:{soloLuis}")