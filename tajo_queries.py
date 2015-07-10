from tajo.client import TajoClient

client = TajoClient("http://127.0.0.1:26880/rest", username='charsyam')
queries = client.queries()
for query in queries:
    print query
