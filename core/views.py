from django.shortcuts import render


def index(request):
    text = [
        'Architecto at eligendi ipsum laborum maiores nostrum vel.',
        'Atque aut dolor fuga harum illum maiores nostrum officia, qui quia\
rerum vel, voluptatibus.',
        'Lorem ipsum dolor sit amet, consectetur adipisicing elit.',
    ]
    context = {
        'title': 'django e-commerce',
        'text': text,
    }
    return render(request, 'index.html', context)


def contact(request):
    return render(request, 'contact.html')


def product(request):
    return render(request, 'product.html')


def products(request):
    return render(request, 'products.html')
