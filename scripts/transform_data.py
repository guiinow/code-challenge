from pandas import DataFrame as pd
from pandas import read_csv


def transform_data(csv_file_path, output_file_path):
    df = read_csv(csv_file_path)

    # aqui é pra ter certeza que os nomes estão consistentes
    df.rename(columns={
        'OrderID': 'order_id',
        'CustomerID': 'customer_id',
        'OrderDate': 'order_date',
        'TotalAmount': 'total_amount'
    }, inplace=True)

    # certifica que os tipos de dados tão consistentes
    df['order_date'] = pd.to_datetime(df['order_date'])
    df['total_amount'] = df['total_amount'].astype(float)

    df.to_csv(output_file_path, index=False)

if __name__ == "__main__":
    transform_data('data/extracted_data.csv', 'data/transformed_data.csv')