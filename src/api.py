from django.http import HttpResponse, HttpRequest
from requests import Response
from rest_framework.decorators import api_view


@api_view(["GET"])
def health_check(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        return HttpResponse("status ok")
