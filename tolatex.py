import os, jinja2
from jinja2 import Template
import templates
import yaml
import io
from subprocess import Popen
import os
import tempfile
import shutil

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
template = latex_jinja_env.get_template('nuevaplantilla.tex')

#genera un dictionario con las variables de interés
with open(r'Analisis_Visual_Datos.yaml') as file:
    template_vars = yaml.full_load(file)

#doc.generate_pdf("complex_report",clean_tex=False,compiler='pdflatex')

#crea un archivo y guarda el latex
output_file = open('./Latex/Analisis_Visual_Datos2.tex', 'w')
#io.open('./Latex/cambiarcar.tex', encoding='latin-1')

#pasa el diccionario con los nombres de las variables al render
output_file.write( template.render( template_vars  ) )
output_file.close()