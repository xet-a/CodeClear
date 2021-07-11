import os, requests
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import redirect
from .models import User
from django.core.files.base import ContentFile
from config.settings import SOCIAL_OUTH_CONFIG

# Create your views here.
def users_login(request):
    if request.method=='POST':
        username=request.POST["username"]
        password=request.POST["password"]
        user=authenticate(username=username,password=password)
        if user is not None:
            print("인증성공")
            login(request,user)
        else:
            print("인증실패")
    return render(request,"login.html")
 
 
def users_logout(request):
    logout(request)
    return redirect("user:login")
 
 
def users_signup(request):
    if request.method=="POST":
        print(request.POST)
        username=request.POST["username"]
        password=request.POST["password"]
        lastname=request.POST["lastname"]
        email=request.POST["email"]
 
        user=User.objects.create_user(username,email,password)
        user.last_name=lastname
        user.save()
        return redirect("user:login")
 
    return render(request,"join.html")

def kakao_login(request):
    CLIENT_ID = SOCIAL_OUTH_CONFIG['KAKAO_REST_API_KEY']
    REDIRET_URL = SOCIAL_OUTH_CONFIG['KAKAO_REDIRECT_URI']
    url = "https://kauth.kakao.com/oauth/authorize?response_type=code&client_id={0}&redirect_uri={1}".format(
        CLIENT_ID, REDIRET_URL)
    return redirect(url)

class SocialLoginException(Exception):
    pass

class KakaoException(Exception):
    pass

def kakao_login_callback(request):
    try:
        # kakao_login에서 request를 보내면, url의 code 값을 얻음
        code = request.GET.get("code")
        CLIENT_ID = SOCIAL_OUTH_CONFIG['KAKAO_REST_API_KEY']
        REDIRET_URL = SOCIAL_OUTH_CONFIG['KAKAO_REDIRECT_URI']
        # 얻은 code를, ~token으로 POST함
        token_request = requests.get("https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id={0}&redirect_uri={1}&code={2}".format(
        CLIENT_ID, REDIRET_URL, code))
        # JSON을 얻고
        token_json = token_request.json()
        error = token_json.get("error", None)
        if error is not None:
            raise KakaoException("Can't get authorization code.")
        # access_token을 얻음
        access_token = token_json.get("access_token")
        
        # kapi.~로 access_token을 보내고, profile_json을 받음
        profile_request = requests.get(
            "https://kapi.kakao.com/v2/user/me",
            headers={"Authorization": f"Bearer {access_token}"},
        )
        profile_json = profile_request.json()

        email = profile_json.get("kakao_account", None).get("email")
        if email is None:
            raise KakaoException()
        gender = profile_json.get("kakao_account").get("gender")

        properties = profile_json.get("properties")
        nickname = properties.get("nickname")
        profile_image = properties.get("profile_image")
        # 모델에 추가
        try:
            user = User.objects.get(email=email)
            if user.login_method !=User.LOGIN_KAKAO:
                raise KakaoException()
        except User.DoesNotExist:
            user = User.objects.create(
                email=email,
                username=nickname,
                nickname=nickname,
                login_method=User.LOGIN_KAKAO,
                email_verified=True,
            )
            user.set_unusable_password()
            user.save()
            if profile_image is not None:
                photo_request = requests.get(profile_image)
                user.user_icon.save(
                    f"{nickname}-icon", ContentFile(photo_request.content)
                )
        login(request, user)
        return redirect(reverse("life:main"))
    except KakaoException:
        return redirect(reverse("user:login"))