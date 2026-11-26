from sqlalchemy.orm import sessionmaker
from crear_base_entidades import motor, HistoriaClinica

Sesion = sessionmaker(bind=motor)
sesion = Sesion()

# orden de las historias por fecha, de la mas reciente a la mas antigua
historias = sesion.query(HistoriaClinica).order_by(
    HistoriaClinica.fecha_atencion.desc()
).all()

print("\nHISTORIAS CLINICAS ORDENADAS POR FECHA")
print("------------------------------------")

for historia in historias:
    print("Mascota:", historia.nombre_mascota)
    print("Fecha:", historia.fecha_atencion)
    print("Diagnostico:", historia.diagnostico)
    print("------------------------------------")

sesion.close()