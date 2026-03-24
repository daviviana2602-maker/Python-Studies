from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = # postgresql+psycopg2://usuario:senha@localhost:5432/seu_banco

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

Base = declarative_base()


#start code

class PythonTable(Base): # class is mandatory with database
    __tablename__ = 'python' # reference or create table name

    id = Column(Integer, primary_key=True) # create column (id)
    name = Column(String) # create column (name)
    age = Column(String) # create column (age)

Base.metadata.create_all(engine)


def main():
    name = input("Digite o nome: ").strip().title()
    age = input("Digite a idade: ").strip()

    session = Session()

    try:
        new_record = PythonTable(name=name, age=age) 
        session.add(new_record)
        session.commit() # enter in PostgreSQL
        print("register inserted with sucess!")
        
    except Exception as error:
        session.rollback()
        print(f"register went wrong: {error}")
        
    finally:
        session.close()

if __name__ == "__main__":
    main()
