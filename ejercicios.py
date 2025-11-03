import json


data = {
          "elemendozao" : {
                "nombres" : "Elymileth de Jesús",
                "apellidos" : "Mendoza Ortega",
                "edad" : 17,
                "colombiano" : True,
                "deportes" : ["ajedréz","Natación","Fútbol"]
           } ,
           "orjuan" : {
                "nombres" : "Juan Sebastián",
                "apellidos" : "Ortíz Valencia",
                "edad" : 20,
                "colombiano" : False,
                "deportes" : ["Fútbol","Ajedréz","Baloncesto"]
            },
           "jadiazcoronado" : {
                "nombres": "Juan Antonio",
                "apellidos": "Díaz Coronado",
                "edad":24,
                "colombiano":True,
                "deportes":["Fúitbol","Ajedréz","Gimnasia"]
            },
         
            "dmlunasol" : {
                "nombres": "Dorotea Maritza",
                "apellidos": "Luna Sol",
                "edad":30,
                "colombiano":False,
                "deportes":["Baloncesto","Ajedréz","Gimnasia"]
            },
            "roserosof" : {
                "nombres" : "Sofía María",
                "apellidos" : "Rosero Yela",
                "edad" : 35,
                "Colombiano" :True,
                "deportes" : ["Natación","Voleibol","Boxeo"]
            },
            "mordayana" : {
               "nombres" : "Andrea Dayana",
               "apellidos" : "Mora Fernández",
                "edad" : 38,
                "colombiano" : False,
                "deportes" : ["Boxeo","Natación","Baloncesto"]
            },

            "rodpaula" : {
                "nombres" : "María Paula",
                "apellidos" : "Rodiguez Ayala",
                "edad" : 14,
                "colombiano" : True,
                "deportes" : ["Gimnasia","Boxeo","Voleibol"]
           },
           "zamalejandro" : {
                "nombres" : "Alejandro Santiago",
                "apellidos" : "Ruíz Zambrano",
                "edad" : 44,
                "colombiano": True,
                "deportes" : ["Voleibol","Fútbol","Ajedréz"]
           },
}



with open("Programación de computadores", "w",encoding = "utf-8") as write_file:
  json.dump(data, write_file, ensure_ascii=False, indent = 4, )

sports_json = {}
for usuario,persona in data.items():
   for deporte in persona["deportes"]:
       if deporte not in sports_json:
         sports_json[deporte] = []   
       sports_json[deporte].append(usuario)
   

with open("Proyecto_arcunal", "w",encoding = "utf-8") as write_file:
  json.dump(sports_json, write_file, ensure_ascii=False, indent = 4, )



with open("Programación de computadores", "r",encoding = "utf-8") as read_file:
  data = json.load(read_file)
nombres = [info["nombres"] for info in data.values()]
apellidos = [info["apellidos"] for info in data.values()]
deportes = [info["deportes"] for info in data.values()]
edad = [info["edad"] for info in data.values()]


deportes1 = input("Ingrese un deporte: ")

for persona in data.values():
  if deportes1 in persona["deportes"]:
    print(persona["nombres"], persona["apellidos"])

edad1 =int( input("ingrese una edad inicial : "))
edad2 =int( input("ingrese otra edad final: "))

for persona in data.values():
  if edad1 <= persona["edad"] <= edad2:
    print(persona["nombres"], persona["apellidos"])

    