from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
# AbstractBaseUser : 새로운 User 모델을 상속받아 새로 정의함 / 데이터 스키마에 영향 줌 / 기본-id,pwd,last_login
# BaseUserManager : User 생성할 때 사용하는 클래스
#
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator
from django.utils import timezone
from django.core.mail import send_mail

'''
작성 X : phone, birth, sex, 기타 설정...
작성 O : (id, pwd, last_login은 ABU에서 제공), 
        email, uname(실명), nickname, isactive, 
'''
# 기존 User 모델 수정, 추가해서 확장하기
class User(AbstractBaseUser, PermissionsMixin):    
    email = models.EmailField(       
        verbose_name=_('Email address'), 
        max_length=255,        
        unique=True,    
    )
    username = models.CharField(
        verbose_name=_('Username'),
        max_length=30,
    )
    nickname = models.CharField(
        verbose_name=_('Nickname'),
        max_length=30,
        null=False,
        unique=True,
    )
    # 폰 입력받는 정규식(인데 수정해야 함)
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="형식 : 어쩌구저쩌구",
    )
    phone = models.CharField(
        _('phone number'),
        validators=[phone_regex],
        max_length=17,
        unique=True,
    )

    gender_male = "male"
    gender_female = "female"
    gender_other = "other"

    GENDER_CHOICES = (
        (gender_male, "Male"),
        (gender_female, "FeMale"),
        (gender_other, "Other"),
    )

    gender = models.CharField(
        choices=GENDER_CHOICES, max_length=10, blank=True
    )

    LOGIN_EMAIL = "email"
    LOGIN_KAKAO = "kakao"

    LOGIN_CHOICES = (
        (LOGIN_EMAIL, "Email"),
        (LOGIN_KAKAO, "Kakao"),
    )

    login_method = models.CharField(
        max_length=50, choices=LOGIN_CHOICES, default=LOGIN_EMAIL
    )
    
    birth = models.DateField(
        verbose_name=_('Date of Birth'),
        blank=True, null=True
    )

    email_verified = models.BooleanField(default=False)

    # django user model 필수 필드
    is_active = models.BooleanField(
        verbose_name=_('Is active'),
        default=True,
    )
    is_admin = models.BooleanField(
        verbose_name=_('Is active'),
        default=False,
    )
    is_superuser = models.BooleanField(
        verbose_name=_('Is active'),
        default=False,
    )
    date_joined = models.DateTimeField(
        verbose_name=_('Date joined'),
        default=timezone.now,
    )
    # 일단 user icon만 구현
    user_icon = models.ImageField(
        # null, blank 기본 값 F
        null=True, # 필드 값이 null(정보 없음)로 저장 ㅇㅋ
        blank=True, # 필드가 폼(입력 양식)에서 빈 채로 저장 ㅇㅋ / db에 '' 저장
        upload_to='', # 경로 추가
    )

    #objects = UserManager()

    # username으로 사용되는 필드. 반드시 unique일 것.
    USERNAME_FIELD = 'email'
    # createsuperuser 명령어에서 반드시 필요한 필드들 정의
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        #ordering = ('-date_joined',)

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)


# User 모델을 관리할 Manager 정의
# 꼭 settings.py의 AUTH_USER_MODEL에 '[APPNAME].User' 필드 추가해야 함
class UserManager(BaseUserManager):
    # 선택적으로 관리자를 migrations으로 직렬화함(?)
    use_in_migrations = True

    # user 생성, parameter로 전달받은 값들을 user 객체로 db에 저장함
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        # normalize -> 중복 최소화를 위한 정규화
        user = self.model(
            email=self.normalize_email(email),
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    # 일반 user 생성, is_superuser == False 이면 일반 user
    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    # superuser(관리자) 생성, is_superuser == False 인 경우 오류 출력
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)
