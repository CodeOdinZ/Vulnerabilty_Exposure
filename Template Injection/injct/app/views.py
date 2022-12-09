from django.shortcuts import render
from django.http import HttpResponse
from django.template import engines
import jinja2
import os
import sys
from jinja2 import Environment, PackageLoader, FileSystemLoader

# Create your views here.

def inject(request, *args, **kwargs):
    
    # vari = request.GET.get("fname")
    # return render(request, 'index.html.j2', {'tmplt':varip} )

    engine = engines["jinja2"] 
    use = request.GET.get("inputz")

    if use is None:
        use = ''
    #use = request.args.get("inputz")
    
    filez = open("./app/templates/abc.html", 'r')
    textz = filez.read()
    #print(os.getcwd())
    #print(textz)
    #print(use)

    

    template = engine.from_string(
    textz   + str(use)
    
        + "</body></html>"
    )
    
    return HttpResponse(template.render({}, request))

    # templateLoader = jinja2.FileSystemLoader(searchpath="./templates")
    # templateEnv = jinja2.Environment(loader=templateLoader)
    # TEMPLATE_FILE = "index.html"
    # template = templateEnv.get_template(TEMPLATE_FILE)
    # outputText = template.render()  


    # environment = Environment(loader=FileSystemLoader("templates"))
    # template = environment.get_template("index.html")

