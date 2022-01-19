from sqlalchemy import create_engine
from sqlalchemy import text
from faker import Faker

import pandas as pd

def insert_a_record():
    engine = create_engine('postgresql://postgres:1234@localhost:5432/dataengineering')
    fake = Faker()
    with engine.connect() as conn:
        query = f"INSERT INTO person (name, city, zip) VALUES ('{fake.name()}', '{fake.city()}', '{fake.zipcode()}')"
        result = conn.execute(query)
        conn.commit()

def gen_record():

    fake = Faker()
    record = {
        'name' : fake.name(),
        'city' : fake.city(),
        'zip' : fake.zipcode()
    }

    return record

def insert_thousand_records():

    engine = create_engine('postgresql://postgres:1234@localhost:5432/dataengineering')

    records = [gen_record() for _ in range(1000)]

    with engine.connect() as conn:
        conn.execute(
            text("INSERT INTO person (name, city, zip) VALUES (:name, :city, :zip)"),
            records
        )

def get_as_dataframe():

    engine = create_engine('postgresql://postgres:1234@localhost:5432/dataengineering')

    with engine.connect() as conn:
        df = pd.read_sql('SELECT * FROM person', conn)
        df.to_csv('person.csv')
        return df