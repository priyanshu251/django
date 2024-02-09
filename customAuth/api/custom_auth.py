from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.models import User #  Imports the User model from Django's authentication framework (django.contrib.auth.models). This model represents user accounts and provides functionality for managing users, including authentication.

class CustomAuthentication(BaseAuthentication): #  Imports the User model from Django's authentication framework (django.contrib.auth.models). This model represents user accounts and provides functionality for managing users, including authentication.
    def authenticate(self, request): # Defines a method named authenticate() within the CustomAuthentication class. This method is required to be implemented in custom authentication classes derived from BaseAuthentication.
# It takes two parameters: self (a reference to the instance of the class) and request (the HTTP request object).
        username = request.GET.get('username') # Retrieves the value of the 'username' parameter from the query string of the HTTP request (request.GET). This assumes that the username is passed as a query parameter in the URL.
# Stores the username in the variable username.
        if username is None: # Checks if the username is None (i.e., not provided in the query string in the request).
            return None # If the username is not provided, returns None to indicate that no authentication attempt should be made.

        try:
            user = User.objects.get(username=username) # Attempts to retrieve a User object from the database using the User.objects.get() method, filtering by the provided username. If the user is found, assigns the retrieved user object to the user variable.
        except User.DoesNotExist:
            raise AuthenticationFailed('Invalid username') # If the user is not found (i.e., User.DoesNotExist exception is raised), raises an AuthenticationFailed exception with the message 'Invalid username'.

        return (user, None) # Returns a tuple containing the authenticated user object (user) and None as the authentication credentials (since this custom authentication backend does not require any additional credentials).
