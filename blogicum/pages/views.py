from django.shortcuts import render

def about(request):
    # Определяем шаблон для страницы about
    template = 'pages/about.html'
    return render(request, template)


def rules(request):
    # Определяем шаблон для страницы rules
    template = 'pages/rules.html'
    return render(request, template)
