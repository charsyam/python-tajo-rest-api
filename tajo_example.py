from tajo.client import TajoClient

client = TajoClient("http://127.0.0.1:26880/rest", username='charsyam')
resultset = client.execute_query_wait_result('select * from test')
while True:
    t = resultset.next_tuple()
    if t is None:
        break

    print(t)

