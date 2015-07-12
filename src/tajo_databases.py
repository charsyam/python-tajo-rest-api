from tajo.client import TajoClient

client = TajoClient("http://127.0.0.1:26880/rest", username='charsyam')
client.create_database("test123")
databases = client.databases()

for database_name in databases:
    try:
        ret = client.database_info(database_name)
        print(ret)
    except:
        pass

client.delete_database("test123")
