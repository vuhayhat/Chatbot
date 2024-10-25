"""
Django settings for ecommerce_web project.

Generated by 'django-admin startproject' using Django 5.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""
from pathlib import Path
import dj_database_url
import os #
from pathlib import Path
if os.path.isfile('env.py'):
     import env
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = 'django-insecure-9matw63sav^-j5xje-y&ld6s%jh+8w_pcv(63gv=^rm$j^6ww)'
SECRET_KEY = os.environ.get('SECRET_KEY')





# SECURITY WARNING: don't run with debug turned on in production!





# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

#------run on (Nếu chạy trên các nền tảng cloud khác)------------------------------------------------------

# RENDER_EXTERNAL_HOSTNAME giúp bạn cấu hình ALLOWED_HOSTS tự động khi chạy trên nền tảng cloud.
# CSRF_TRUSTED_ORIGINS giúp bạn quản lý các nguồn gốc mà bạn tin tưởng khi thực hiện kiểm tra CSRF.



# ALLOWED_HOSTS = ['ecommerce.com','././.gitpod.io', 'localhost', '127.0.0.1']

# RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
# if RENDER_EXTERNAL_HOSTNAME:
#    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)


# CSRF_TRUSTED_ORIGINS = ['https://*.gitpod.io']




# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # THÊM CÁC ỨNG DỤNG
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # 'cloudinary_storage',
    'django.contrib.sitemaps',
    'cloudinary',
    'django_summernote',
    'home',
    'products',
    'bag',
    'checkout',
    'profiles',
    'blog',
        
    'crispy_forms',
    "crispy_bootstrap4",
    'ecommerce_web'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #THÊM
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'ecommerce_web.urls'
# áp dụng kiểu dáng của Bootstrap cho các biểu mẫu Django mà không cần phải viết CSS riêng
CRISPY_TEMPLATE_PACK = 'bootstrap4'
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap4"


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'), #tìm các mẫu trong thư mục templates nằm trong thư mục gốc của dự án (BASE_DIR).
            os.path.join(BASE_DIR, 'templates', 'allauth') #tìm các mẫu trong thư mục allauth nằm bên trong thư mục templates
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                #add
                'django.template.context_processors.media',
                'bag.contexts.bag_contents',
            ],
            #add
            'builtins': [
                'crispy_forms.templatetags.crispy_forms_tags',
                'crispy_forms.templatetags.crispy_forms_field',
            ]
        },
    },
]
# add 
MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'
# backend xác thực mà ứng dụng sẽ sử dụng để kiểm tra thông tin đăng nhập của người dùng
AUTHENTICATION_BACKEND = (
    #  đăng nhập bằng tài khoản user ở Django admin 
    'django.contrib.auth.backends.ModelBackend',

    'allauth.account.auth_backend.AuthenticationBackend',


)

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'dljmqgdap',
    'API_KEY': '823893773722557',
    'API_SECRET': 'TJAsM2R296Sl2fQzu89oGmk8zNs',
    'SECURE': True
}


SITE_ID = 1



ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE = True
ACCOUNT_USERNAME_MIN_LENGTH = 4
LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/'



WSGI_APPLICATION = 'ecommerce_web.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases


if 'DATABASE_URL' in os.environ:
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
else:
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'ecommerce-web',  
        'USER': 'postgres',  
        'PASSWORD': '123456',  
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },

]
  # Password validation
  # https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

# STATIC_URL = 'static/' --

MEDIA_URL = '/media/'	
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'	
STATIC_URL = '/static/'	
STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'	
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]	
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

FREE_DELIVERY_THRESHOLD  = 50
# DFREE_DELIVERY_THRESHOLD = 50
STANDARD_DELIVERY_PERCENTAGE = 10
STRIPE_CURRENCY = 'usd'
STRIPE_PUBLIC_KEY = os.getenv('STRIPE_PUBLIC_KEY', '')
STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY', '')
STRIPE_WH_SECRET = os.getenv('STRIPE_WH_SECRET', '')

# if 'DEVELOPMENT' in os.environ:
#     EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
#     DEFAULT_FROM_EMAIL = 'ecommerce_web@example.com'
# else:
#     EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#     EMAIL_USE_TLS = True
#     EMAIL_PORT = 587
#     EMAIL_HOST = 'smtp.gmail.com'
#     EMAIL_HOST_USER = os.environ.get('vuhayhatmtp@gmail.com')
#     EMAIL_HOST_PASSWORD = os.environ.get('pegr owpu sqok gort')
#     DEFAULT_FROM_EMAIL = os.environ.get('vuhayhatmtp@gmail.com')

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'vuhayhatmtp@gmail.com'
EMAIL_HOST_PASSWORD = 'pegr owpu sqok gort'
