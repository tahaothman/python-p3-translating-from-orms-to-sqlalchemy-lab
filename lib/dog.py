import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Base, Dog


def create_table(Base, engine):
    engine = create_engine('sqlite:///./lib/dogs.db')
    Base.metadata.create_all(engine)
    
def save(session, dog):
    session.add(dog)
    session.commit()


def get_all(session):
    return session.query(Dog).all()


def find_by_name(session, name):
    return session.query(Dog).filter_by(name=name).first()


def find_by_id(session, id):
    return session.query(Dog).filter_by(id=id).first()


def find_by_name_and_breed(session, name, breed):
    return session.query(Dog).filter_by(name=name, breed=breed).first()


def update_breed(session, dog, new_breed):
    dog.breed = new_breed
    session.commit()


def main():
    engine = create_engine(SQLITE_URL)
    Session = sessionmaker(engine)
    session = Session()
    
  
    create_table()

    joey = Dog(name="joey", breed="cocker spaniel")
    save(session, joey)

    all_dogs = get_all(session)

    conan = find_by_name(session, 'conan')
    dog_1 = find_by_id(session, joey.id)
    fanny = find_by_name_and_breed(session, 'fanny', 'cockapoo')
    update_breed(session, joey, 'bulldog')

    session.close()
    os.remove('dogs.db')

if __name__ == "__main__":
    main()
