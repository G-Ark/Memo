from django.http import JsonResponse
from ..models import Person, MemoPerson
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from ..serializers import MemoSerializer, PersonSerializer, MemoPersonSerializer

@csrf_exempt
def memo_person_list(request):
    """
    List all code memos, or create a new memo.
    """
    if request.method == 'GET':
        memos = MemoPerson.objects.all()
        serializer = MemoPersonSerializer(memos, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def new_memo(request):
    """
    List all code memos, or create a new memo.
    """
    if request.method == 'POST':
        data = JSONParser().parse(request)
        try:
            memo_serializer = MemoSerializer(data=data["memo"])
            if memo_serializer.is_valid():
                memo = memo_serializer.save()
                print("memo saved")
            persons = data["persons"]
            for person in persons:
                try:
                    person = Person.objects.get(first_name=person["first_name"], last_name=person["last_name"])
                    print("Person already exists")
                except Person.DoesNotExist:
                    print("no person found")
                    person_serializer = PersonSerializer(data=person)
                    if person_serializer.is_valid():
                        person = person_serializer.save()
                        print("Saving person")
                memo_person = MemoPerson(memo=memo, person=person)
                memo_person.save()
                print("Saving memoPerson")
            return JsonResponse(memo_serializer.data, status=201)
        except:
            return JsonResponse(data, status=400)