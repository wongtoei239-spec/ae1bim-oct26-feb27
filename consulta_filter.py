from sqlalchemy.orm import sessionmaker
from crear_base_entidades import motor, Consultorio

Sesion = sessionmaker(bind=motor)
sesion = Sesion()

# para buscar consultorios de medicina general
consultorios = sesion.query(Consultorio).filter(
    Consultorio.especialidad == "Medicina general"
).all()

print("\nCONSULTORIOS DE MEDICINA GENERAL")
print("--------------------------------")

for consultorio in consultorios:
    print("Consultorio:", consultorio.nombre)
    print("Especialidad:", consultorio.especialidad)
    print("Clinica:", consultorio.clinica.nombre_comercial)
    print("--------------------------------")

sesion.close()