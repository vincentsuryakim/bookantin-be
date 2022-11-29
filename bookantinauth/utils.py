from rest_framework.authtoken.models import Token
from.models import BooKantinAPIToken 

def generate_token(user):
    token = BooKantinAPIToken.objects.create(user=user)
    return token.key