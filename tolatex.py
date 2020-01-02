import os, jinja2
from jinja2 import Template
import templates
import yaml

from subprocess import Popen
import os
import tempfile
import shutil


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
template = latex_jinja_env.get_template('new.tex')

# populate a dictionary with the variables of interest
import yaml

with open(r'camposdeldoc.yaml') as file:
    template_vars = yaml.full_load(file)

#doc.generate_pdf("complex_report",clean_tex=False,compiler='pdflatex')
# create a file and save the latex
output_file = open('./Latex/subiendo.tex', 'w')

# pass the dictionary with variable names to the renderer
output_file.write( template.render( template_vars  ) )
output_file.close()