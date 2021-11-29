from django.http import response
from django.shortcuts import render, redirect
import requests
from django.views.generic import DetailView
from .models import *

def Home(request):
    

    context = {
       'aboutme':AboutMe.objects.first(),
       'skills':Skills.objects.all(),
       'socials':Socials.objects.all(),
       'category':CategoryOfPortfolio.objects.all(),
       'portfolio':Portfolios.objects.all(),
       'blog':Blog.objects.all().order_by('-id'),
       'blogofcategory':CategoryOfBlog.objects.all(),
       'icon':Icon.objects.all(),
       'icons':Icons.objects.all(),
       'resume':Resume.objects.all().order_by('-id'),
        'logo':Logo.objects.all()
    }

    return render(request, 'index-10.html', context)


class PortfolioDetail(DetailView):
   model = Portfolios
   template_name = 'portfolio-detail-dark.html'
   context_object_name = 'portfolio'

class BlogDetail(DetailView):
   model = Blog
   template_name = 'blog.html'
   context_object_name = 'blog'

   def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['categories'] = CategoryOfBlog.objects.all()
       context['prev'] = Blog.objects.filter(category=self.object.category, id__lt=self.object.id).first()
       context['next'] = Blog.objects.filter(category=self.object.category, id__gt=self.object.id).first()
       
       return context





def SendMsg(request):
     
    name =  request.POST['name']
    email =  request.POST['email']
    message =  request.POST['message']
    subject =  request.POST['subject']


    
    bot_token = '1936856188:AAGPWusgP-KQkAamGAn3Rat-WJgjJnXq08M'
    text = 'Saytdan xabar: \n\nIsmi : ' + name + '\nemail : ' + email + '\nxabar : ' + message + '\nsubject : ' + subject
    url = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id='
    requests.get(url + '1942414515' + '&text=' + text)

    return redirect('/')

def Page404(request):
   return render(request, '404.html')

def customhandler404(request, exception, template_name='404.html'):
   response = render(request, template_name)
   response.status_code = 404
   return response