from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import Contact

# Create your views here.


def index(request):
    if request.method == 'POST':
        name = request.POST['name']
        mail = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        inbox = Contact(name=name, subject=subject, message=message)
        inbox.save()

    return render(request, 'webapp/index.html', {})


#def add_form(request):
 #   submitted = False
  #  if request.method == "POST":
   #     form = ContactForm(request.POST)
    #    if form.is_valid():
     #       form.save()
      #      return HttpResponseRedirect('/index?submitted=True')
       # else:
        #    form = ContactForm
         #   if 'submitted' in request.GET:
          #      submitted = True

   # return render(request, 'webapp/index.html', {'form': form, 'submitted': submitted})
