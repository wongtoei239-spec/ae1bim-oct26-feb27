from sqlalchemy.orm import sessionmaker
from crear_base_entidades import motor, Clinica

Sesion = sessionmaker(bind=motor)
sesion = Sesion()

# se obtiene todas las clinicas
clinicas = sesion.query(Clinica).all()

print("\nHISTORIAS CLINICAS POR CLINICA")
print("--------------------------------")

for clinica in clinicas:
    total_historias = 0

    for consultorio in clinica.consultorios:
        for veterinario in consultorio.veterinarios:
            total_historias += len(veterinario.historias_clinicas)

    print("Clinica:", clinica.nombre_comercial)
    print("Total de historias clinicas:", total_historias)
    print("--------------------------------")

sesion.close()