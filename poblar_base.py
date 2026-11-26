from datetime import date
from sqlalchemy.orm import sessionmaker
from crear_base_entidades import motor, Clinica, Consultorio, Veterinario, HistoriaClinica

Sesion = sessionmaker(bind=motor)
sesion = Sesion()

# Evitamos ingresar los mismos datos dos veces
if sesion.query(Clinica).first() is None:

    # clinicas vets
    clinica1 = Clinica(
        nombre_comercial="Huella Sana",
        direccion="Av. Francisco de Orellana, Guayaquil",
        veterinario_responsable="Lucia Cedeño"
    )

    clinica2 = Clinica(
        nombre_comercial="Patitas del Rio",
        direccion="Av. Leon Febres Cordero, Daule",
        veterinario_responsable="Carlos Mendoza"
    )

    clinica3 = Clinica(
        nombre_comercial="Amigos Peludos",
        direccion="Centro de Milagro, Guayas",
        veterinario_responsable="Andrea Zambrano"
    )

    # Consultorios
    consultorio1 = Consultorio(
        nombre="Consultorio 1",
        especialidad="Medicina general",
        clinica=clinica1
    )

    consultorio2 = Consultorio(
        nombre="Consultorio 2",
        especialidad="Dermatologia",
        clinica=clinica1
    )

    consultorio3 = Consultorio(
        nombre="Consultorio 1",
        especialidad="Cirugia",
        clinica=clinica2
    )

    consultorio4 = Consultorio(
        nombre="Consultorio 1",
        especialidad="Medicina general",
        clinica=clinica3
    )

    # Vets
    vet1 = Veterinario(
        nombres="Lucia", apellidos="Cedeño",
        correo="lucia@huellasana.com",
        licencia_profesional="VET-001",
        consultorio=consultorio1
    )

    vet2 = Veterinario(
        nombres="Mario", apellidos="Vera",
        correo="mario@huellasana.com",
        licencia_profesional="VET-002",
        consultorio=consultorio2
    )

    vet3 = Veterinario(
        nombres="Carlos", apellidos="Mendoza",
        correo="carlos@patitasrio.com",
        licencia_profesional="VET-003",
        consultorio=consultorio3
    )

    vet4 = Veterinario(
        nombres="Andrea", apellidos="Zambrano",
        correo="andrea@amigospeludos.com",
        licencia_profesional="VET-004",
        consultorio=consultorio4
    )

    # historias clinicas de las mascotas
    historia1 = HistoriaClinica(
        fecha_atencion=date(2026, 11, 5),
        diagnostico="Gastritis",
        tratamiento="Dieta blanda y medicacion",
        nombre_mascota="Max",
        veterinario=vet1
    )

    historia2 = HistoriaClinica(
        fecha_atencion=date(2026, 11, 8),
        diagnostico="Infeccion respiratoria",
        tratamiento="Antibioticos segun indicacion",
        nombre_mascota="Luna",
        veterinario=vet1
    )

    historia3 = HistoriaClinica(
        fecha_atencion=date(2026, 11, 12),
        diagnostico="Dermatitis",
        tratamiento="Champu medicado y control",
        nombre_mascota="Bruno",
        veterinario=vet2
    )

    historia4 = HistoriaClinica(
        fecha_atencion=date(2026, 11, 15),
        diagnostico="Herida superficial",
        tratamiento="Limpieza y curaciones",
        nombre_mascota="Nina",
        veterinario=vet3
    )

    historia5 = HistoriaClinica(
        fecha_atencion=date(2026, 11, 18),
        diagnostico="Otitis",
        tratamiento="Limpieza y gotas oticas",
        nombre_mascota="Toby",
        veterinario=vet3
    )

    sesion.add_all([
        clinica1, clinica2, clinica3,
        consultorio1, consultorio2, consultorio3, consultorio4,
        vet1, vet2, vet3, vet4,
        historia1, historia2, historia3, historia4, historia5
    ])

    sesion.commit()
    print("Datos de las clinicas registrados correctamente")

else:
    print("Ya existen datos registrados en la base")

sesion.close()