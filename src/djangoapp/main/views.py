from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, 'main/home.html')


# def create(request):
#     if respond.method == "POST":
#         form = CreateNewlist(request.POST)

#         if form.is_valid():
#             n = form.cleaned_data["name"]
#             t = ToDoList(name=n)
#             t.save()
#         return HT