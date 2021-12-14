from datetime import datetime
import requests

url = 'https://api.stackexchange.com/2.2/search?order=desc&sort=activity&intitle=perl&site=stackoverflow'
datos = requests.get(url) 
data = datos.json()
items = data["items"]

#Obtener el número de respuestas contestadas y no contestadas
n_respuestas_contestadas = 0
n_respuestas_no_contestadas = 0
for i in items:
    if(i["is_answered"]):
        n_respuestas_contestadas+=1
    else:
        n_respuestas_no_contestadas+=1
print("Número de respuestas contestadas: {:d}".format(n_respuestas_contestadas))  
print("Número de respuestas no contestadas: {:d}".format(n_respuestas_no_contestadas))            

#Obtener la respuesta con menor número de vistas
min_visitas = items[0]["view_count"]
respuesta = {}
for i in items:
    n_vistas = i["view_count"]
    if(n_vistas<min_visitas):
        min_visitas = n_vistas
        respuesta = i
print("\nRespuesta con menor número de vistas:\n {0}\nNúmero de vistas: {1}".format(respuesta,min_visitas))         

#Obtener la respuesta más vieja y más actual
res_mas_vieja = items[0]["creation_date"]
res_mas_actual = items[0]["creation_date"]
respuesta_vie = items[0]
respuesta_act = items[0]
for i in items:
    aux = i["creation_date"]
    if(aux<res_mas_vieja):
        res_mas_vieja = aux
        respuesta_vie = i
    if(aux>res_mas_actual):
        res_mas_actual = aux
        respuesta_act = i
print("\nRespuesta mas vieja: \n{0}\nFecha: {1}".format(respuesta_vie,datetime.fromtimestamp(res_mas_vieja))) 
print("Respuesta mas actual: \n{0}\nFecha: {1}".format(respuesta_act,datetime.fromtimestamp(res_mas_actual))) 

#Obtener la respuesta del owner que tenga una mayor reputación
max_reputacion = items[0]["owner"]["reputation"]
respuesta = {}
for i in items:
    rep_owner = i["owner"]["reputation"]
    if(rep_owner>max_reputacion):
        max_reputacion = rep_owner
        respuesta = i
print("\nRespuesta con mayor reputacion: \n{0}\nPuntuación: {1}".format(respuesta,max_reputacion))         