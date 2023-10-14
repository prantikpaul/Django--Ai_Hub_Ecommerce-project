from django.urls import path
from .views import sign_in,sign_up,forget_pass,sign_out,verify_failed,verify_success,verify

urlpatterns = [
  path('Sign_In/',sign_in,name='sign_inpp'),
  path('Sign_Up/',sign_up,name='sign_uppp'),
  path('Forget_pass/',forget_pass,name='forget_passpp'),
  path('sing_out/',sign_out,name='sign_outpp'),
  path('verify_success/',verify_success,name='verify_successpp'),
  path('verify_failed/',verify_failed,name='verify_failedpp'),
  path('verify/<auth_token>/',verify,name='verifypp'),
]
