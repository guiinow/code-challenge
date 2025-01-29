import pandas as pd

def extract_csv(file_path, output_path):
    data = pd.read_csv(file_path)
    
    # escreve os dados extraídos no disco
    data.to_csv(output_path, index=False)

if __name__ == "__main__":
    extract_csv('./data/order_details.csv', 'data/extracted_data.csv')