# authentication.py
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.conf import settings

class JWTCookieAuthentication(JWTAuthentication):
    """
    Custom JWT authentication that reads tokens from HTTP-only cookies
    instead of Authorization headers
    """
    def authenticate(self, request):
        # Get token from cookie
        raw_token = request.COOKIES.get(settings.JWT_COOKIE_NAME)
        
        if raw_token is None:
            return None
        
        # Validate token using Simple JWT's built-in validation
        validated_token = self.get_validated_token(raw_token)
        user = self.get_user(validated_token)
        
        return (user, validated_token)