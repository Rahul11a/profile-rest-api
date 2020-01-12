from rest_framework.views import APIView
from rest_framework.response import Response
# When we call the APIView it returns a Standanrd respose object


class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs',
        ]

        # It returns a response object, which is further converted into json.
        # Hence it should either return dictionary or list
        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
