import pandas as pd
from sqlalchemy import create_engine


def extract_postgres():
    db_url = 'postgresql://northwind_user:thewindisblowing@localhost:5432/northwind'
    table_name = 'orders'
    
    engine = create_engine(db_url)
    
    query = f'SELECT * FROM {table_name}'
    df = pd.read_sql(query, engine)
    
    output_file = 'data/extracted_data.csv'
    df.to_csv(output_file, index=False)
    print(f'Data extracted and written to {output_file}')