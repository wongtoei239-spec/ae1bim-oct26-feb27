from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from configuracion import cadena_base_datos

motor = create_engine(cadena_base_datos)
Base = declarative_base()


# los datos de las clinicas veterinarias
class Clinica(Base):
    __tablename__ = "clinicas"

    id = Column(Integer, primary_key=True)
    nombre_comercial = Column(String(100), nullable=False)
    direccion = Column(String(150), nullable=False)
    veterinario_responsable = Column(String(120), nullable=False)

    consultorios = relationship("Consultorio", back_populates="clinica")


# Consultorios que pertenecientes a cada clinica
class Consultorio(Base):
    __tablename__ = "consultorios"

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    especialidad = Column(String(100), nullable=False)
    clinica_id = Column(Integer, ForeignKey("clinicas.id"), nullable=False)

    clinica = relationship("Clinica", back_populates="consultorios")
    veterinarios = relationship("Veterinario", back_populates="consultorio")


# los veterinarios que trabajan en los consultorios
class Veterinario(Base):
    __tablename__ = "veterinarios"

    id = Column(Integer, primary_key=True)
    nombres = Column(String(100), nullable=False)
    apellidos = Column(String(100), nullable=False)
    correo = Column(String(120), nullable=False)
    licencia_profesional = Column(String(50), nullable=False)
    consultorio_id = Column(Integer, ForeignKey("consultorios.id"), nullable=False)

    consultorio = relationship("Consultorio", back_populates="veterinarios")
    historias_clinicas = relationship("HistoriaClinica", back_populates="veterinario")


# las atenciones realizadas a las mascotas
class HistoriaClinica(Base):
    __tablename__ = "historias_clinicas"

    id = Column(Integer, primary_key=True)
    fecha_atencion = Column(Date, nullable=False)
    diagnostico = Column(String(200), nullable=False)
    tratamiento = Column(String(200), nullable=False)
    nombre_mascota = Column(String(100), nullable=False)
    veterinario_id = Column(Integer, ForeignKey("veterinarios.id"), nullable=False)

    veterinario = relationship("Veterinario", back_populates="historias_clinicas")


# Crear las tablas en SQLite
if __name__ == "__main__":
    Base.metadata.create_all(motor)
    print("Base de datos creada correctamente")