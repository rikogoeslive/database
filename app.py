from module import Project, engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime, date
session = sessionmaker(bind=engine)()


def input_worker():
    print_workers()
    try:
        worker_id = int(input("Įveskite darbuotojo ID: "))
    except ValueError:
        print("Klaida: ID turi būti skaičius.")
        return None
    else:
        return worker_id


def new_worker():
    print("[::: Naujas darbuotojas :::]")
    try:
        name = input("Vardas: ")
        surrname = input("Pavardė: ")
        date_of_birth = datetime.strptime(input("Įveskite gimimo datą (YYYY-MM-DD) formatu: "), "%Y-%m-%d")
        responsibilities = input("Pareigos: ")
        salary = float(input("Atlyginimas per mėnesį: "))
    except ValueError:
        print("-" * 50)
        print("KLAIDA: Atlyginimas turi būti skaičius.")
        print("-" * 50)
        return
    else:
        worker = Project(name, surrname, date_of_birth, responsibilities, salary)
        session.add(worker)
        session.commit()
        print("-" * 60)
        print(f"Darbuotojas {name} {surrname} sėkmingai pridėtas į sąrašą.")
        print("-" * 60)


def update_worker ():
    worker_id = input_worker()
    if worker_id:
        worker = session.query(Project).get(worker_id)
        if worker:
            try:
                name = input(f"Vardas ({worker.name}): ")
                surname = input(f"Pavardė ({worker.surname}): ")
                date_of_birth = datetime.strptime(input(f"Gimimo data ({worker.date_of_birth}): "), "%Y-%m-%d")
                responsibilities = input(f"Pareigos ({worker.responsibilities}): ")
                salary = float(input(f"Atlyginimas ({worker.salary}): ") or 0)
            except ValueError:
                print("")
                print("KLAIDA: atlyginimas turi būti skaičius")
                print("")
                return
            else:
                if len(name) > 0:
                    worker.name = name
                if len(surname) > 0:
                    worker.surname = surname
                if date_of_birth == datetime:
                    worker.date_of_birth = date_of_birth
                if len(responsibilities) > 0:
                    worker.responsibilities = responsibilities
                if salary > 0 :
                    worker.salary = salary
                session.commit()
                print("-" * 45)
                print(f"Darbuotojas {name} {surname} atnaujintas sėkmingai.")
                print("-" * 45)

        else:
            print("-" * 45)
            print(f"KLAIDA: darbuotojas su ID: {worker_id} neegzistuoja.")
            print("-" * 45)


def delete_worker():
    print("")
    print("Jūs pasirinkote pašalinti darbuotoją :)")
    print("")
    worker_id = input_worker()
    if worker_id:
        delete = session.query(Project).get(worker_id)
        if delete:
            session.delete(delete)
            session.commit()
            print("-" * 45)
            print(f"Darbuotojas {delete} sėkmingai ištrintas.")
            print("-" * 45)
        else:
            print("")
            print(f"KLAIDA: darbuotojas su ID: {worker_id} neegzistuoja!")


def print_workers():
    print("---- > Darbuotojai <----")
    print("(#, Vardas, Pavardė, Gimimo data, Pareigos, Atlyginimas, nuo kada dirba)")
    workers = session.query(Project).all()
    for worker in workers:
        print(worker)


while True:
    print("")
    print(" |---| Darbuotojų dirbančių įmonėje duomenų bazė  |---| ")
    print("")
    print("Jūsų pasirinkimas: ")
    print("[---> Q <---]: Išeiti")
    print("[---> R <---]: Rodyti visus darbuotojus.")
    print("[---> N <---]: Naujas darbuotojas.")
    print("[---> P <---]: Pakeisti darbuotojo duomenis.")
    print("[---> T <---]: Trinti darbuotoją.")
    choice = input("Pasirinkite: ").casefold()
    if choice =="q":
        print("")
        print("Jūs pasirinkote išeiti iš programos!")
        print("")
        print("Viso gero! ( ͡~ ͜ʖ ͡° )")
        break
    elif choice == "r":
        print("")
        print("Jūsų pasirinkimas: Peržiūrėti darbuotojų sąrašą: ")
        print("")
        print_workers()
    elif choice == "n":
        print("")
        print("Jūs pasirinkote pridėti naują darbuotoją.\nUžpildykite informacinius laukus!")
        print("")
        new_worker()
    elif choice == "p":
        print("")
        print("Jūs pasirinkote pakeisti darbuotojo duomenis: ")
        print("")
        update_worker()
    elif choice == "t":
        delete_worker()
    else:
        print("KLAIDA: Blogas pasirinkimas, rinkitės iš naujo!")

