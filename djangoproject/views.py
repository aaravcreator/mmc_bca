from django.shortcuts import HttpResponse,render
from random import randint
def index_view(request):
    random_data = randint(1,100)

    data = {
        "name":"RAM SHARMA",
        "age":22,
        "gender":"Male",
        "hobbies":["Singing","Dancing","Swimming"],
        "random":random_data
            }
    # return HttpResponse("<h1>THis is index page</h1>")
    return render(request,"index.html",data)





