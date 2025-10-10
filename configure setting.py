INSTALLED_APP = [
  'django.contrib.admin',
  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  'django.contrib.messages',
  'django.contrib.staticfiles',

  'rest_framework',
  'rest_framework_simplejwt',
  'django_filters',
  'corsheaders',

  'products',
  'users',

]

MIDDLEWARE = [
  'corsheaders.middleware.CorsMiddleware',

]

REST_FRAMEWORK = [
  'DEFAULT_AUTHENTICATION_CLASSES': [ 
      'rest_framework_simplejwt.authentication.JWTAuthentication',
  ],
  'DEFAULT_PERMISSION_CLASSES': [
      'rest_framework.permissions.IsAuthenticationOrReadOnly',
  ]
  'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
    ],
}


from datetime import timedelta

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(hours=1),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
}
