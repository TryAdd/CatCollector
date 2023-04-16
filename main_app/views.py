from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Cat, Toy
from django.views.generic.edit import CreateView, UpdateView , DeleteView
from django.views.generic import ListView, DetailView
from .forms import FeedingForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

#? ds 3shan ys2l aluser for login mo bkefh ydsh bdon login
#! de 3shan al def
from django.contrib.auth.decorators import login_required
#! de 3shan al class
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
# class Cat:
#     def __init__(self, name, bread, description, age):
#         self.name = name
#         self.bread = bread
#         self.description = description
#         self.age = age

# cats = [
#     Cat('Esraa','Annoying','So annoying',24 ),
#     Cat('ahlam','Cute','Secret Keeper',20 ),
#     Cat('Haya','Kind','So kind',12 )
# ]

@login_required
def home(request):
    #? res.send in express
    # return HttpResponse('<a href="http://127.0.0.1:8000/about/"> About </a> <h1>Cat Collector </h1>')
    return render(request, 'home.html')

@login_required
def about(request):
    # return HttpResponse('<h1>About the Cats Collector</h1> <a href="http://127.0.0.1:8000/"> Go back </a>')
    return render(request, 'about.html')

@login_required
def cats_index(request):
    # select * from main_app_cat;
    # cats = Cat.objects.all() #? django's ORM Function 
    cats = Cat.objects.filter(user=request.user) #? de t5le kl cats l kl wa7d bro7h (every cat have 1 user leha)
    return render(request, 'cats/index.html', {'cats': cats})

@login_required
def cats_detail(request, cat_id):
    # select * from main_app where id = cat_id
    cat = Cat.objects.get(id = cat_id)
    feeding_form = FeedingForm()
    toys_cat_doesnt_have = Toy.objects.exclude(id__in = cat.toy.all().values_list('id'))
    return render(request,'cats/detail.html', {
        'cat': cat,
        'feeding_form': feeding_form,
        'toys' : toys_cat_doesnt_have
        })

class CatCreate(LoginRequiredMixin , CreateView):
    model = Cat
    fields = ['name', 'breed', 'description', 'age' , 'image']# ele mktob hne same t7t
    # fields = '__all__'
    # success_url = '/cats'

    def form_valid(self, form):
        #? self.request.user is the logged user 
        form.instance.user = self.request.user

        #? allows Createview form_valid method to do it normal work 
        return super().form_valid(form)

class CatUpdate(LoginRequiredMixin, UpdateView):
    model = Cat
    fields = ['breed', 'description', 'age']

class CatDelete(LoginRequiredMixin, DeleteView):
    model = Cat
    success_url = '/cats'

@login_required
def add_feeding(request, cat_id):
    # pass
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.cat_id = cat_id
        new_feeding.save()
    return redirect('detail',cat_id=cat_id)


class ToyList(LoginRequiredMixin, ListView):
    model = Toy


class ToyDetail(LoginRequiredMixin, DetailView):
    model = Toy

class ToyCreate(LoginRequiredMixin, CreateView):
    model = Toy
    fields = '__all__'

class ToyUpdate(LoginRequiredMixin, UpdateView):
    model = Toy
    fields = ['name' , 'color']
    
class ToyDelete(LoginRequiredMixin, DeleteView):
    model = Toy
    success_url = '/toys'

@login_required
def assoc_toy(request, cat_id, toy_id):
    Cat.objects.get(id=cat_id).toy.add(toy_id)
    return redirect('detail',cat_id=cat_id)

@login_required
def unassoc_toy(request, cat_id, toy_id):
    Cat.objects.get(id=cat_id).toys.remove(toy_id)
    return redirect('detail',cat_id=cat_id)

def signup(request):
    error_massage = ''
    
    if request.method == 'POST':
        #? make a "user" form object with the data from the browser
        form = UserCreationForm(request.POST) 

        if form.is_valid():
            #? save user to db
            user = form.save()
            #? log in the user auto once they signup 
            login(request, user)
            return redirect('index') 
        else:
            error_massage = 'please Try Again!'
    # if it was bad post or req
    form = UserCreationForm()
    context = {
        'form': form,
          "error_massage": error_massage
          }
    return render(request, 'registration/signup.html',context)


