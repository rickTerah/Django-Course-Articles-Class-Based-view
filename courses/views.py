from django.shortcuts import render
from django.http import HttpResponse
from .models import Course
from django.views import View
from .forms import CourseForm
from django.urls import reverse

# Create your views here.
class CourseListView(View):
    template_name = 'course_list.html'
    def get(self,request):
        queryset = Course.objects.all()
        context = {
            "object_list": queryset
        }
        return render(request, self.template_name , context)

class CourseDetailView(View):
    template_name = 'course_detail.html'
    def get(self, request, id):
        obj = Course.objects.get(id=id)
        context = {
            "object": obj
        }
        return render(request, self.template_name, context)

class CourseCreateView(View):
    template_name = 'course_create.html'
    def get(self, request):
        form = CourseForm()
        context = {
            "form": form
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = CourseForm(request.POST or None)
        if form.is_valid():
            form.save()
            form = CourseForm()
        context = {
            "form": form
        }
        return render(request, self.template_name, context)

class CourseDeleteView(View):
    template_name = 'course_delete.html'
    def get(self, request, id):
        obj = Course.objects.get(id=id)
        # if request.method == 'POST':
        #     obj.delete()
        context = {
            "object": obj
        }
        return render(request, self.template_name, context)

    def post(self, request, id):
        obj = Course.objects.get(id=id)
        if request.method == 'POST':
            obj.delete()
        context = {
            "object": obj
        }
        return render(request, self.template_name, context)

    def get_success_url(self):
        return reverse("courses:course_list")

class CourseUpdateView(View):
    template_name = 'course_create.html'
    def get(self, request, id):
        form = CourseForm()
        obj = Course.objects.get(id=id)
        context = {
            "form": form,
            "object": obj
        }
        return render(request, self.template_name, context)

    def post(self, request, id):
        form = CourseForm(request.POST or None)
        obj = Course.objects.get(id=id)
        if form.is_valid():
            form.save()
            form = CourseForm()
        context = {
            "form": form,
            "object": obj
        }
        return render(request, self.template_name, context)