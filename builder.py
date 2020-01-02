import yaml
import io
import re
import docx2txt
import re
from docx import Document

def ConvertirEnYaml():
  
    document = Document ("Analisis_visual_de_datos.docx")
    tables = document.tables
    datos={}

     #armando el diccioario
    datos['Carrera']=tables[0].cell(1,3).text
    datos['PlanEstudios']=tables[0].cell(2,3).text
    datos['NombreEspañol']=tables[0].cell(3,3).text
    datos['NombreInglés']=tables[0].cell(4,3).text
    datos['Docente']=tables[0].cell(5,3).text
    datos['Año']=tables[0].cell(6,3).text
    datos['Semestre']=tables[0].cell(7,3).text
    datos['Previas']=tables[0].cell(9,3).text
    datos['Duracion']=tables[0].cell(11,3).text
    datos['Creditos']=tables[0].cell(11,4).text
    datos['TipoCurso']=tables[0].cell(13,3).text
    
    #Datos de Categoria del Curso --Colocar una Cruz
    datos['T1row1Col1']=tables[0].cell(15,3).text
    datos['T1row2-Col1']=tables[0].cell(16,3).text
    datos['T1row3-Col1']=tables[0].cell(17,3).text
    datos['T1row4-Col1']=tables[0].cell(18,3).text
    datos['T1row5-Col1']=tables[0].cell(19,3).text
    datos['T1row6-Col1']=tables[0].cell(20,3).text

    #Datos de Categoria del Curso --Comentarios
    datos['T1row1-Col2']=tables[0].cell(15,4).text
    datos['T1row2-Col2']=tables[0].cell(16,4).text
    datos['T1row3-Col2']=tables[0].cell(17,4).text
    datos['T1row4-Col2']=tables[0].cell(18,4).text
    datos['T1row5-Col2']=tables[0].cell(19,4).text
    datos['T1row6-Col2']=tables[0].cell(20,4).text


    datos['Resumen']=tables[0].cell(22,1).text
    datos['Objetivos']=tables[0].cell(24,1).text
    datos['Resultados']=tables[0].cell(26,1).text
    datos['Contenido']=tables[0].cell(28,1).text

    #Datos de Tabla 15.Métodos Didácticos 
    datos['T2row1-Col1']=tables[0].cell(31,1).text
    datos['T2row2-Col1']=tables[0].cell(32,1).text

    #Datos de Categoria del Curso --Comentarios
    datos['T2row1-Col2']=tables[0].cell(31,3).text
    datos['T2row2-Col2']=tables[0].cell(32,3).text

    datos['T3row1-Col1']=tables[0].cell(35,3).text

    datos['Biblobasica']=tables[0].cell(37,1).text
    datos['BibloAmpliatoria']=tables[0].cell(39,1).text
    print(datos)
   
    #se crea el archivo yaml con el diccionario  
    with io.open('camposdeldoc.yaml', 'w', encoding='utf8') as outfile:
        #print(sorted(datos))
        yaml.dump(datos, outfile, default_flow_style=False, allow_unicode=True)
    return datos

    def cargarYaml(archivo):
        with open(archivo, 'r') as stream:
            data_loaded = yaml.safe_load(stream)
        return  data_loaded

    # with io.open('data2.yaml', 'w', encoding='utf8') as outfile:
    #     yaml.dump(datos, outfile, default_flow_style=False, allow_unicode=True)

ConvertirEnYaml()