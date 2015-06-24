from tajo.client import TajoClient

client = TajoClient("http://127.0.0.1:26880/rest", username='charsyam')
print(client.create_database("test123"))
print(client.delete_database("test123"))
databases = client.databases()
for database_name in databases:
    ret = client.database_info(databases[0])
    print(ret)
