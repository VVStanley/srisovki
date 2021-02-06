import logging.config
# from django.utils.log import DEFAULT_LOGGING

# Disable Django's logging setup
LOGGING_CONFIG = None

logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'formatters': {
        'django.server': {
            '()': 'django.utils.log.ServerFormatter',
            'format': '[{server_time}] {message}',
            'style': '{',
        },
        'verbose': {
            'format': '{levelname}: APP:{name}; {asctime}; {module}; LINE:{lineno} - {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname}: {lineno}; {message}',
            'style': '{',
        },
    },
    'handlers': {
        'django.server': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'django.server',
        },
        'console': {
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
        },
        # 'w_file': {
        #     'level': 'INFO',
        #     'class': 'logging.FileHandler',
        #     'formatter': 'verbose',
        #     'filename': 'wstanley/logs/errors.log',
        #     'filters': ['require_debug_false'],
        # },
        # 'app_log': {
        #     'level': 'DEBUG',
        #     'class': 'logging.FileHandler',
        #     'filename': 'wstanley/logs/app_log.log',
        #     'formatter': 'verbose',
        # },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'formatter': 'verbose',
            'filters': ['require_debug_false'],
        },
    },
    'loggers': {
        'django.server': {
            'handlers': ['django.server', 'console', 'mail_admins', ],
            'level': 'INFO',
            'propagate': False,
        },
        # 'app_loger': {
        #     'handlers': ['app_log', 'mail_admins'],
        #     'level': 'DEBUG',
        #     'email_backend': 'django.core.mail.backends.smtp.EmailBackend',
        #     'propagate': True,
        # },
    },
})
