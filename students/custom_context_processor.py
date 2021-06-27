from .models import Profile

def prof(request):
    if request.user.is_authenticated:
        return {
            'prof': Profile.objects.get(user = request.user)
        }
    else:
        return {
            'prof': Profile.objects.none()
        }