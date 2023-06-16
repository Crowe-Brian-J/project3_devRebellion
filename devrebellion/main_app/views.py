from django.shortcuts import render

developers = [
    {'name': 'Mayte Ozoria', 'username':'Ozmayte','email':'ozoria@gmail.com','links':'insert Link'}
]

# Define the home view
def home(request):
    # Include an .html file extension - unlike when rendering EJS templates
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")

def developers_index(request):
    return render(request, 'developers/index.html', {
        'developers': developers
    })