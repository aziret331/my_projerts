from django.shortcuts import render

def index(request):
    movies = [
    {
        'title':  'Интерстеллар',
        'description': 'Фильм о путешествии через космос и времени, чтобы спасти человечество.',
        'poster': 'interstellar.jpg',
        'trailer': 'https://www.youtube.com/embed/zSWdZVtXT7E',
    },
    {
        'title':  'Начало',
        'description': 'Фильм о группе специалистов, которые внедряются в сны людей для кражи или внедрения идей.',
        'poster': 'inception.jpg',
        'trailer': 'https://www.youtube.com/embed/YoHD9XEInc0',
    },
    {
        'title':  'Бегущий по лезвию 2049',
        'description': 'Фильм о будущем, где охотник за репликантами обнаруживает секрет, который может изменить общество.',
        'poster': 'Blade_runner.jpg',
        'trailer': 'https://www.youtube.com/embed/gCcx85zbxz4',
    },
    ]
