from .models import RedSocial

def ctx_dict(request):
    ctx={}
    links=RedSocial.objects.all()
    for r in links:
        ctx[r.fkey]=r.url
    return