from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
#These lines import necessary classes and modules from the Django Rest Framework's authtoken app.
# obtain_auth_token is a view that is used to obtain authentication tokens.
# Token is the model that represents the authentication tokens.
# Response is a class used to create HTTP responses.

class CustomAuthToken(obtain_auth_token): #This line defines a new class named CustomAuthToken that inherits from the obtain_auth_token view. This allows you to customize the behavior of the authentication token view.
     def post(self, request, *args, **kwargs): #jab bhi post req mara jaega to ye function hit hoga
         serializer = self.serializer_class(data=request.data,
                                            context={'request': request}) # ki hui req k sath jo body aya hai usko serializer class me pass kr do
         serializer.is_valid(raise_exception=True)# serializer class me jo data aya hai usko validate kr do
         user = serializer.validated_data['user'] # this line extracts the user from the validated data that was sent in the request body as a value of username.
         token, created = Token.objects.get_or_create(user=user)# this line creates a new token for the user if one doesn't already exist. If a token already exists, then it retrieves the existing token.
         return Response({
             'token': token.key,
             'user_id': user.pk,
             'email': user.email
         })# this line returns the token, user ID, and email address in the response body.