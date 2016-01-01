import os


_env = os.environ.get('PY_ENV', 'prod')
if _env in ('dev', 'development', 'developer'):
    from .dev import *
elif _env in ('test', 'testing', 'qa'):
    from .test import *
else:
    from .prod import *
