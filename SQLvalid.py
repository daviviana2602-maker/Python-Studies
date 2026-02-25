from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "postgresql+psycopg2://postgres:cttdavi2602@localhost:5432/postgres"
# postgresql+psycopg2://usuario:senha@localhost:5432/your_database

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

Base = declarative_base()


#start code

class PythonTable(Base): # class is mandatory with database
    __tablename__ = 'python' # reference or create table name

    id = Column(Integer, primary_key=True) # create column (id)
    name = Column(String) # create column (name)
    age = Column(Integer) # create column (age)

Base.metadata.create_all(engine)


def main():
    while True:
        name = input('Enter the name here: ').strip().title() # name validation
        if name.replace(' ','').isalpha():
            break
        else:
            print('enter a valid name')
            continue
        
    while True:
        try:
            age = int(input(f'enter {name} age here: ')) # age validation
            if age < 1 or age > 130:
                 print('please, enter a valid age')
                 continue
            else:
                break
        except ValueError:
            print('please, enter a valid age')
                    
            
    session = Session()

    try:
        new_record = PythonTable(name=name, age=age) 
        session.add(new_record)
        session.commit() # enter in PostgreSQL
        print('register inserted with sucess!')
        
    except Exception as error:
        session.rollback()
        print(f'register wrong: {error}')
        
    finally:
        session.close()

if __name__ == "__main__":
    main()