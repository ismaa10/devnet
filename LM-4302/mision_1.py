from myspark import spark_get_room_id, spark_send_message, _headers
import requests

token = 'ZTI0MDlhZDktODYwMi00ZDU3LTg2YmQtZDk1YTU4YWZlYWExZWU1YTBjMGItNDNj'
token_bot = 'ODE5MGJmNDMtODQwYS00YjFkLTk1OTMtMDEyZGE1NThjMWY4MzA4ZWQyZTEtNzM0'
sala_grupo = 'DevNet Express - Buenos Aires'
sala_prueba = 'salaDePrueba'
room_id = spark_get_room_id(token_bot, sala_prueba)
#print('El room id es: ' + room_id)
#spark_send_message(token_bot, room_id, 'Prueba de bot')
my_query = {'email': 'gmonne@conatel.com.uy'}
my_request = requests.get('https://api.ciscospark.com/v1/people', params=my_query, headers=_headers(token))
print(my_request.json())
