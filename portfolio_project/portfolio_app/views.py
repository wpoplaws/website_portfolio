from django.shortcuts import render


def main(request):
    return render(request, 'main.html', {})


def portfolio(request):
    return render(request, 'portfolio.html', {})


def resume(request):
    return render(request, 'resume.html', {})
