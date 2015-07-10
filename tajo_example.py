from tajo.client import TajoClient

client = TajoClient("http://127.0.0.1:26880/rest", username='charsyam')
client.execute_query_wait_result('create table "Test2" (col1 int)')
client.execute_query_wait_result('insert into "Test2" select 1')
client.execute_query_wait_result('insert into "Test2" select 2')
client.execute_query_wait_result('insert into "Test2" select 3')

resultset = client.execute_query_wait_result('select * from "Test2"')
while True:
    t = resultset.next_tuple()
    if t is None:
        break

    print(t)

client.execute_query_wait_result('drop table "Test2" purge')
