import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///darbuotojai.db')
Base = declarative_base()


class Project(Base):
    __tablename__ = "Darbuotojai"
    id = Column(Integer, primary_key=True)
    name = Column("Vardas", String)
    surname = Column("Pavardė", String)
    date_of_birth = Column("Gimimo data", DateTime)
    responsibilities = Column("Pareigos", String)
    salary = Column("Atlyginimas", Float)
    works_from = Column("Dirba nuo:", DateTime, default=datetime.datetime.now)

   
    def __init__(self, name, surname, date_of_birth, responsibilities, salary):
        self.name = name
        self.surname = surname
        self.date_of_birth = date_of_birth
        self.responsibilities = responsibilities
        self.salary = salary

    def __repr__(self):
        return f"({self.id}, {self.name}, {self.surname}, {self.date_of_birth}, {self.responsibilities}, {self.salary}, {self.works_from})"


if __name__ == "__main__":
    Base.metadata.create_all(engine)