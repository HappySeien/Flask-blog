import os
from dotenv import load_dotenv

class Config:
    _basedir = os.path.abspath(os.path.dirname(__file__))

    DOTENV_PATH = os.path.join(_basedir, '.env')

    if os.path.exists(DOTENV_PATH):
        load_dotenv(dotenv_path=DOTENV_PATH)

    DEBUG = os.getenv('DEBUG')

    ADMINS = frozenset(os.getenv('ADMINS'))
    SECRET_KEY = os.getenv('SECRET_KEY')

    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(_basedir, 'blog.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_MIGRATE_REPO = os.path.join(_basedir, 'db_repository')
    DATABASE_CONNECT_OPTIONS = {}

    THREADS_PER_PAGE = 8

    WTF_CSRF_ENABLED = True
    WTF_CSRF_SECRET_KEY = os.getenv('WTF_CSRF_SECRET_KEY')

    RECAPTCHA_USE_SSL = False
    RECAPTCHA_PUBLIC_KEY = 'B?E(G+KbPeShVmYq3t6w9z$C&F)J@McQfTjWnZr4u7x!A%D*G-KaPdRgUkXp2s5v'
    RECAPTCHA_PRIVATE_KEY = os.getenv('RECAPTCHA_PRIVATE_KEY')
    RECAPTCHA_OPTIONS = {'theme': 'white'}
