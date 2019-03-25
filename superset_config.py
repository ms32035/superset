import os

from flask_appbuilder.security.manager import AUTH_OAUTH

redis_host = os.environ['SUPERSET__CACHE_REDIS_HOST']
redis_port = os.getenv('SUPERSET__CACHE_REDIS_PORT', 6379)
redis_db = os.getenv('SUPERSET__CACHE_REDIS_DB', 1)
sqlalchemy_uri = os.environ['SUPERSET__SQLALCHEMY_DATABASE_URI']

google_client_id = os.environ['SUPERSET__GOOGLE_CLIENT_ID']
google_secret_key = os.environ['SUPERSET__GOOGLE_SECRET_KEY']
google_domain = os.environ['SUPERSET__GOOGLE_DOMAIN']

MAPBOX_API_KEY = os.getenv('MAPBOX_API_KEY', '')
CACHE_CONFIG = {
    'CACHE_TYPE': 'redis',
    'CACHE_DEFAULT_TIMEOUT': 300,
    'CACHE_KEY_PREFIX': 'superset_',
    'CACHE_REDIS_HOST': redis_host,
    'CACHE_REDIS_PORT': redis_port,
    'CACHE_REDIS_DB': redis_db,
    'CACHE_REDIS_URL': f'redis://{redis_host}:{redis_port}/{redis_db}'}
SQLALCHEMY_DATABASE_URI = sqlalchemy_uri
SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY = os.environ['SUPERSET__SECRET_KEY']

AUTH_TYPE = AUTH_OAUTH
AUTH_USER_REGISTRATION = True
AUTH_USER_REGISTRATION_ROLE = "Public"
OAUTH_PROVIDERS = [
    {
        'name': 'google',
        'whitelist': [f'@{google_domain}'],
        'icon': 'fa-google',
        'token_key': 'access_token',
        'remote_app': {
            'base_url': 'https://www.googleapis.com/oauth2/v2/',
            'request_token_params': {
                'scope': 'email profile'
            },
            'request_token_url': None,
            'access_token_url': 'https://accounts.google.com/o/oauth2/token',
            'authorize_url': 'https://accounts.google.com/o/oauth2/auth',
            'consumer_key': google_client_id,
            'consumer_secret': google_secret_key
        }
    }
]
