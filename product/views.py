from django.shortcuts import render

def category_view(request):
    return render(request, 'category.html')