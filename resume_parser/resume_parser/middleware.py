from django.conf import settings
from django.http import HttpResponseForbidden


class APIKeyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if the request path is the API endpoint you want to guard
        if request.path == "/api/uploads":
            # Retrieve the API key from the request headers
            api_key = request.headers.get("Authorization").replace("Bearer ", "")

            # Compare the API key with the one stored in settings.py
            if api_key == settings.SESSION_API_KEY:
                # API key is valid, allow the request to proceed
                return self.get_response(request)
            else:
                # API key is invalid, return unauthorized response
                return HttpResponseForbidden("Unauthorized")

        # For all other requests, allow them to proceed
        return self.get_response(request)
