import os

class Config(object):

    RECAPTCHA_PUBLIC_KEY = os.environ.get('6Lc_IvspAAAAAJfqdlCwYHcLRp-hCM0E4VzvZ_QH')
    RECAPTCHA_PRIVATE_KEY = os.environ.get('6Lc_IvspAAAAAMFzhw-zZP_UsQJ0_dGHyOZed9eG')
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess' 