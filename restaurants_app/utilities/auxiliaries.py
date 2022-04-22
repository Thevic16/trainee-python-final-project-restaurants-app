from rest_framework.reverse import reverse as api_reverse


def get_uri(request, pk: int, model_name: str, app_name: str):
    return api_reverse(f'{app_name}:{model_name}-detail',
                       kwargs={'pk': pk}, request=request)
