from sqlalchemy import or_
from sqlalchemy.orm import sessionmaker
from crear_base_entidades import motor, HistoriaClinica

Sesion = sessionmaker(bind=motor)
sesion = Sesion()

# busqueda de las historias clinicas con diagnostico de dermatitis u otitis
historias = sesion.query(HistoriaClinica).filter(
    or_(
        HistoriaClinica.diagnostico == "Dermatitis",
        HistoriaClinica.diagnostico == "Otitis"
    )
).all()

print("\nATENCIONES POR DERMATITIS U OTITIS")
print("--------------------------------")

for historia in historias:
    print("Mascota:", historia.nombre_mascota)
    print("Diagnostico:", historia.diagnostico)
    print("Veterinario:", historia.veterinario.nombres,
          historia.veterinario.apellidos)
    print("--------------------------------")

sesion.close()