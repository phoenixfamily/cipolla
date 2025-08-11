from django.shortcuts import render

def category_view(request):
    return render(request, 'category.html')


def product_view(request):
    return render(request, 'product.html')