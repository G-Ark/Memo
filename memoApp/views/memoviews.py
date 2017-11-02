from django.http import JsonResponse
from ..models import Memo
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from ..serializers import MemoSerializer

@csrf_exempt
def memo_list(request):
    """
    List all code memos, or create a new memo.
    """
    if request.method == 'GET':
        memos = Memo.objects.all()
        serializer = MemoSerializer(memos, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MemoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)