import os

env = os.environ['APP_ENVIRONMENT'].lower()

if env == 'dev':
    from .dev import *  # noqa: F403, F401
elif env == 'dev1':
    from .dev1 import *  # noqa: F403, F401
elif env == 'dev2':
    from .dev2 import *  # noqa: F403, F401
elif env == 'dev3':
    from .dev3 import *  # noqa: F403, F401
elif env == 'stage':
    from .stage import *  # noqa: F403, F401
elif env == 'master':
    from .master import *  # noqa: F403, F401
else:
    raise ValueError(f'{env} not found!')
