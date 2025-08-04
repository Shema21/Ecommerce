import json
from uuid import uuid4
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
import os

@api_view(['POST'])
@permission_classes([AllowAny])
def request_api_key(request):
    key = str(uuid4())
    entry = {"key": key, "active": True}

    keys_file = os.path.join(os.path.dirname(__file__), 'keys.json')

    try:
        with open(keys_file, 'r+') as f:
            data = json.load(f)
            data.append(entry)
            f.seek(0)
            json.dump(data, f, indent=4)
    except FileNotFoundError:
        with open(keys_file, 'w') as f:
            json.dump([entry], f, indent=4)

    return Response({"api_key": key})
