from .models import Tag


def common(request):
    context={
        'tags': Tag.objects.all(),
    }
    return context