from sqlalchemy import create_engine
import pandas as pd
import os

def load_data_to_postgres():
    db_user = 'northwind_user'
    db_password = 'thewindisblowing'
    db_host = 'localhost'
    db_port = '5432'
    db_name = 'northwind'
    
    engine = create_engine(f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')
    
    # carrega dados do arquivo CSV extraído
    csv_file_path = os.path.join('data', 'extracted_data.csv')
    data = pd.read_csv(csv_file_path)
    
    # carrega os dados na tabela orders do PostgreSQL
    data.to_sql('orders', engine, if_exists='append', index=False)

if __name__ == "__main__":
    load_data_to_postgres()