# In your views.py file, import the following modules
from django.shortcuts import render
from django.http import HttpResponseRedirect

# Define a list of districts and their Wikipedia URLs
districts = [
    ("Alappuzha", "https://en.wikipedia.org/wiki/Alappuzha_district"),
    ("Ernakulam", "https://en.wikipedia.org/wiki/Ernakulam_district"),
    ("Idukki", "https://en.wikipedia.org/wiki/Idukki_district"),
    ("Kannur", "https://en.wikipedia.org/wiki/Kannur_district"),
    ("Kasargod", "https://en.wikipedia.org/wiki/Kasaragod_district")
]

# Define a view function that renders the navbar template
def navbar(request):
    # Pass the districts list as a context variable
    context = {"districts": districts}
    return render(request, "nav.html", context)

# Define a view function that redirects to the selected district's Wikipedia page
def district(request, name):
    # Find the URL that matches the district name
    url = ""
    for d in districts:
        if d[0] == name:
            url = d[1]
            break
    # Redirect to the URL or return an error message if not found
    if url:
        return HttpResponseRedirect(url)
    else:
        return HttpResponse("Invalid district name")
