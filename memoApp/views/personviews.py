from django.http import JsonResponse
from ..models import Person
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from ..serializers import PersonSerializer

@csrf_exempt
def person_list(request):
    """
    List all code memos, or create a new memo.
    """
    if request.method == 'GET':
        persons = Person.objects.all()
        serializer = PersonSerializer(persons, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
#        get_arg1 = request.POST.get('arg1', None)
#        get_arg2 = request.GET.get('arg2', None)
        data = JSONParser().parse(request)
        serializer = PersonSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)