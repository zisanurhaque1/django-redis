import pandas
import os
from django.shortcuts import render
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from django.conf import settings
from django.http import JsonResponse
from .models import Trending


CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

# Create your views here.

def store_data(request):
    try:
        csv_file = os.path.join(settings.BASE_DIR, 'assets', 'data.csv')
        raw_data = pandas.read_csv(csv_file)
        trending_list = []
        for index, row in raw_data.iterrows():
            trending_item = Trending(
                from_social=row['fromSocial'],
                text=row['text'],
                likes_count=row['likesCount'],
                comments_count=row['commentsCount'],
                views_count=row['viewsCount'],
                input_text=row['input'],
                author_meta=row['authorMeta/name'],
                creation_date=row['creationDate']
            )
            trending_list.append(trending_item)
        
        data = Trending.objects.all()
        if data.exists():
            return JsonResponse({'message': 'Alredy data exists'})
        else:
            Trending.objects.bulk_create(trending_list)
            return JsonResponse({'message': 'Data stored successfully'})

    except:
        return JsonResponse({'message': 'There is some problem'})


def get_data(request):
    cached_data = cache.get('trending_list')
    if cached_data:
        context = {
            'trending_list': cached_data,
            'data': 'Data from Cache'
        }
        return render(request, 'csv_data.html', context)
    else:
        data = Trending.objects.all()
        cache.set('trending_list', data)
        context = {
            'trending_list': data,
            'data': 'Data from Database'
        }
        return render(request, 'csv_data.html', context)