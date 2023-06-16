from django.shortcuts import render

developers = [
    {
        "name": "Mayte Ozoria",
        "username": "Ozmayte",
        "email": "ozoria@gmail.com",
        "links": "insert Link",
    }
]

posts = [
    {"title": "This is a title", "text": "This is some text", "imagesource": ""},
    {
        "title": "This is another title",
        "text": "This is some more text",
        "imagesource": "",
    },
]


# Define the home view
def home(request):
    # Include an .html file extension - unlike when rendering EJS templates
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def developers_index(request):
    return render(request, "developers/index.html", {"developers": developers})
