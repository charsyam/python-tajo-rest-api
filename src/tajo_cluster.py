from tajo.client import TajoClient

client = TajoClient("http://127.0.0.1:26880/rest", username='charsyam')
cluster_info = client.cluster_info()
print(cluster_info)
