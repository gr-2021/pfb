import environ
from blog.settings.base import *

env = environ.Env()

#DEBUG = env.bool("DEBUG", False)
DEBUG = False

SECRET_KEY = '5408u459ty5498th548p9h458h8th584ht5498uy954jy945hy549hy459h##%$%*&&(' #env("SECRET_KEY")

#ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")
ALLOWED_HOSTS = ['*']

DATABASES = {
    "default": env.db(),
}
