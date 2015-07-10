from tajo.client import TajoClient

client = TajoClient("http://127.0.0.1:26880/rest", username='charsyam')

client.execute_query_wait_result('create table Test1 (col1 int)')
client.execute_query_wait_result('create table Test2 (col1 int)')
client.execute_query_wait_result('create table Test3 (col1 int)')
client.execute_query_wait_result('create table Test4 (col1 int)')

tables = client.tables("default")
print(tables)
for table in tables:
    t = client.table("default", table.name)
    print(t)

client.execute_query_wait_result('drop table Test1 purge')
client.execute_query_wait_result('drop table Test2 purge')
client.execute_query_wait_result('drop table Test3 purge')
client.execute_query_wait_result('drop table Test4 purge')
