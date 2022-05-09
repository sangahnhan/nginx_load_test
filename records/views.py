import json

from django.views     import View
from django.http      import JsonResponse
from django.conf      import settings

from records.models   import Record

class CreateView(View):
    def post(self, request):
        data = json.loads(request.body)
        
        Record.objects.create(
            heart_beat        = data['heartbeat'],
            blood_pressure    = data['bloodpressure'],
            body_temperature  = data['bodytemperature'],
            oxygen_saturation = data['oxygensaturation']
        )
        return JsonResponse({"message" : 'created'}, status=200)