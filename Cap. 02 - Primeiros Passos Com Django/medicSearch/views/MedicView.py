from medicSearch.models import Profile
from django.shortcuts import render

def list_medics_view(request):
    name = request.GET.get('name')
    speciality = request.GET.get('speciality')
    neighborhood = request.GET.get('neighborhood')
    city = request.GET.get('city')
    state = request.GET.get('state')

    medics = Profile.objects.filter(role=2)

    if name is not None and name != '':
        medics = medics.filter(user__first_name__contains=name)
    if speciality is not None:
        medics = medics.filter(specialities__id=speciality)
    if neighborhood is not None:
        medics = medics.filter(addresses__neighborhood=neighborhood)
    else:
        if city is not None:
            medics.filter(addresses__neighborhood__city=city)
        elif state is not None:
            medics.filter(addresses__neighborhood__city__state=state)
    print(medics.all())

    context = {
        'medics': medics,
    }
    return render(request, template_name='medic/medics.html', context=context, status=200)