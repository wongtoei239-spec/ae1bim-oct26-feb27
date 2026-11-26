
from datetime import date
from sqlalchemy import and_
from sqlalchemy.orm import sessionmaker
from crear_base_entidades import motor, HistoriaClinica

Sesion = sessionmaker(bind=motor)
sesion = Sesion()

# Buscar atenciones de gastritis despues del 1 de noviembre
historias = sesion.query(HistoriaClinica).filter(
    and_(
        HistoriaClinica.diagnostico == "Gastritis",
        HistoriaClinica.fecha_atencion > date(2026, 11, 1)
    )
).all()

print("\nATENCIONES DE GASTRITIS EN NOVIEMBRE")
print("------------------------------------")

for historia in historias:
    print("Mascota:", historia.nombre_mascota)
    print("Fecha:", historia.fecha_atencion)
    print("Diagnostico:", historia.diagnostico)
    print("Tratamiento:", historia.tratamiento)
    print("------------------------------------")

sesion.close()