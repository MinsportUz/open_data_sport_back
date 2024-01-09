from decouple import config

env_name = config('ENV_NAME', default='local')

if env_name == 'local':
    from .local import *
elif env_name == 'production':
    from .production import *
else:
    from .test import *
