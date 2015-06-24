from tajo.client import TajoClient

client = TajoClient("http://127.0.0.1:26880/rest", username='charsyam')
tables = client.tables("default")
for table in tables:
    t = client.table("default", table.name)
