from sqlalchemy import create_engine

engine = create_engine('postgresql://postgres:1234@localhost:5432/dataengineering')
print(engine)