from django.forms.models import model_to_dict
from django.http import JsonResponse

from products.models import Product


def api_home(request):
    model_data = Product.objects.first()
    print(model_data.title, model_data.content)

    data = {}

    if model_data:
        # data['id'] = model_data.id
        # data['title'] = model_data.title
        # data['content'] = model_data.content
        # data['price'] = model_data.price
        # Mejor serializar haciendo un diccionario Python desde Model
        data = model_to_dict(model_data)  # puedo declarar las fields como argumento

    return JsonResponse(data)
