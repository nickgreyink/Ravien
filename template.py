from pathlib import Path

template_directory = "/template/"

template_html = "ariel"

location = Path().absolute()

keywords = ["css", "js", "title"]

import_page = str(location) + str(template_directory) + str(template_html) + '.html'
css_import_page = str(location) + str(template_directory) + str(template_html) + "_css" + '.css'
js_import_page = str(location) + str(template_directory) + str(template_html) + "_js" + '.js'

title = "raviwen"

css = open(css_import_page, 'r').read()

js = open(js_import_page, 'r').read()

data = open(import_page, 'r').read()

def replace_keywords(page, keyword):
    return page.replace("$" + keyword + "$", globals()[keyword])

def get_page():
    edit_page = data
    for keyword in keywords:
        edit_page = replace_keywords(edit_page, keyword)
    final_page = edit_page
    return final_page