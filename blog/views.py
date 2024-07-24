from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View

from rest_framework.views import APIView

from blog.forms import CreateMessageForm
from blog.models import ModelBlog


# class for Registration new users
class RegisterUser(View):
    template_name = "registration/register.html"

    def get(self, request):
        context = {
            'form': UserCreationForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)


class CreateMessageView(View):
    template_name = "create_message.html"

    def get(self, request):
        context = {
            'form': CreateMessageForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = CreateMessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)


# class for displaying the main page
class IndexPageView(APIView):
    def get(self, request, *args, **kwargs):
        content = ModelBlog.objects.all()
        data = {
            'content': content.order_by('-pub_date')
        }
        return render(request, 'index.html', data)


# about view
def about_view(request):
    return render(request, 'about.html')

