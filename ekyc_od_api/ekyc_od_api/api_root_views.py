from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import status

class APIRootView(APIView):
    def get(self, request, format=None):
        # Generate a dictionary of all available endpoints and their URLs
        data = {
            'projects': reverse('project-list-create', request=request, format=format),
            'me': reverse('user-detail', request=request, format=format),
            # 'users':  reverse('user-create', request=request, format=format),
            # Add other endpoints here if needed
        }
        return Response(data)
