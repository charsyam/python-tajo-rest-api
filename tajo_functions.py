from tajo.client import TajoClient

client = TajoClient("http://127.0.0.1:26880/rest", username='charsyam')
functions = client.functions()
for f in functions:
    print(f)
