import os, jinja2,pypandoc
from jinja2 import Template
import templates
import yaml
import io
from subprocess import Popen
import os
import tempfile
import shutil

def decodeData(values):
    variables={}
    for elemento in values:
        for regis in elemento[1]:
            tuples=regis.items() 
            for (k,v) in tuples: 
                variables[k]=v
    return variables              

# crea el ambiente para pasar a Latex mediante el motor jinja2
latex_jinja_env = jinja2.Environment(
    block_start_string    = '\BLOCK{',
    block_end_string      = '}',
    variable_start_string = '\VAR{',
    variable_end_string   = '}',
    comment_start_string  = '\#{',
    comment_end_string    = '}',
    line_statement_prefix = '%%',
    line_comment_prefix   = '%#',
    trim_blocks           = True,
    autoescape            = False,
    loader                = jinja2.FileSystemLoader(os.path.abspath('./'))
)

def generateLatex(yamlfile,textemplate,textogenerate):
    template = latex_jinja_env.get_template(textemplate)

    #genera un dictionario yaml_vars con las variables de interés
    with open(r'../files/yamls/'+yamlfile) as file:
        yaml_vars = yaml.full_load(file)

    #decodifica el diccionario
    template_vars=decodeData(yaml_vars)

    #crea un archivo latex
    output_file = open('../files/texs_pdfs/'+textogenerate, 'w')

    #io.open('./Latex/cambiarcar.tex', encoding='latin-1')

    #envía el diccionario con los nombres de las variables al render
    output_file.write( template.render( template_vars ))
    #pypandoc.convert_file('../files/texs/Analisis_Visual_Datos_.tex', 'pdf',  outputfile="../files/texs/Analisis_Visual_Datos_.pdf",extra_args=['--output=../files/texs/Analisis_Visual_Datos_.pdf'])
    output_file.close()

generateLatex('Analisis_visual_de_datos.yaml','templates/nuevaplantilla.tex','pruebaestructura7.tex')


