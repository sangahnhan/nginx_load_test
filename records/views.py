import json, logging

from django.views     import View
from django.http      import JsonResponse
from django.conf      import settings

from records.models   import Record


class CreateView(View):
    def post(self, request):
        logging.basicConfig(filename='post_view.log', level = logging.DEBUG)

        data = json.loads(request.body)
        
        Record.objects.create(
            heart_beat        = data['heartbeat'],
            blood_pressure    = data['bloodpressure'],
            body_temperature  = data['bodytemperature'],
            oxygen_saturation = data['oxygensaturation']
        )
        logging.info(f'post_success:{data}')

        return JsonResponse({"message" : 'created'}, status=200)