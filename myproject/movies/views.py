from django.shortcuts import render

def index(request):
    movies = [
    {
        'title': 'интерстеллар',
        'description': 'Фильм о путешествии через червоточину в поисках нового дома для человечества.',
        'poster': 'interstellar.jpg',
        'trailer': 'https://www.youtube.com/watch?v=zSWdZVtXT7E'
    },
    {
        'title': 'начало',
        'description': 'Фильм o воров, которые проникают в сны людей, чтобы украсть их секреты.',
        'poster': 'inception.jpg',
        'trailer': 'https://www.youtube.com/watch?v=YoHD9XEInc0'
    },
    {
        'title': 'Бегущий по лезвию 2049',
        'description': 'История о новом бегущем по лезвию, который раскрывает давно скрытую тайну.',
        'poster': 'Blade_runner.jpg',
        'trailer': 'https://www.youtube.com/watch?v=gCcx85zbxz4'
    }
    ]


    return render(request, 'movies/index.html', {'movies': movies})
    