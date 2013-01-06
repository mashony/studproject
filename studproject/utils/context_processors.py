from studproject import settings

def settings_context(request):
    return {'settings': settings}
