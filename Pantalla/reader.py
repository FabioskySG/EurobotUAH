import json                                # Agrego biblioteca

f = open("entities.json", "r")             # Abro fichero (modo lectura)
content = f.read()                         # Leo fichero sobre variable content
jsondecoded = json.loads(content)          # Decodificamos el fichero y cargamos su contenido (sobre variable especificada anteriormente)

'''for entity in jsondecoded["Classes"]:
    entityName = entity["Name"]
    print(entityName)'''

for entity in jsondecoded["Classes"]:
    print("Entidad " + entity["Name"] + ". Sus propiedades son: ")
    for entityProperty in entity["Properties"]:
        print("Propiedad " + entityProperty["Name"] + " de tipo " + entityProperty["Type"]) 
