import traceback
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from users.serializers import UserSerializer, UserLoginSerializer
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from drf_yasg.utils import swagger_auto_schema

class UserCreationView(generics.CreateAPIView):
    """
    Create a new user.
    """
    serializer_class = UserSerializer
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)


class UserProfile(generics.RetrieveAPIView):
    """
    Retrieve the user profile.
    """
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    def get_object(self):
        return self.request.user
    
    def get(self, request):
        serializer = self.get_serializer(self.get_object())
        return Response(serializer.data)


@swagger_auto_schema(
    method='post',
    operation_description="Login to obtain an authentication token.",
    request_body=UserLoginSerializer,
    responses={
        200: UserSerializer,
    },
)
@api_view(['POST'])
def login(request):
    try:
        ''' API for login '''
        username = request.data.get('username')
        password = request.data.get('password')
        user = User.objects.get(username=username)
        if not user.check_password(password):
            return Response({
                'error': 'Username or password is incorrect.'
            }, status=status.HTTP_400_BAD_REQUEST)
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': str(token.key),
            **UserSerializer(user).data
        }, status=status.HTTP_200_OK)
    
    except User.DoesNotExist:
        return Response({
            'error': 'Username or password is incorrect.'
        }, status=status.HTTP_400_BAD_REQUEST)
    except:
        print(traceback.format_exc())
        return Response({'error': 'An error occurred during login'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)