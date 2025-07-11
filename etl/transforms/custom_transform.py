import etl_qbiz

def main(data_query_executor: etl_qbiz.DataQueryExecutor):
    err = data_query_executor.execute_create_table_query(create_table_query=etl_qbiz.DataQueryCreateTable(
        table_name="hoge",
        attributes=[
            etl_qbiz.Column(name="id", type="STRING", nullable=False, comment="ID"),
            etl_qbiz.Column(name="name", type="STRING", nullable=True, comment="Name"),
        ],
        partitions=["id"]
    ))
    if err is not None:
        print(f"Error creating table: {err}")
    else:
        print("Table created successfully.")
