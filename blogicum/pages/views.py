from django.shortcuts import render


def about(request):
    """Показывает страницу «О проекте»."""
    return render(request, 'pages/about.html')


def rules(request):
    """Показывает страницу «Наши правила»."""
    return render(request, 'pages/rules.html')
