
# Two channels so we don't cross the streams
pusher_channel ='listening-channel'
pusher_channel_out ='output-channel'

plugins = ['event_debugger', 'pusherclient','pusher']

# logging levels can be changes to any stnadard level: i.e. INFO
log = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simple": {
            "format": "%(asctime)s %(levelname)6s %(name)s - %(message)s",
            "datefmt": "%H:%M:%S"
        }
    },

    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "stream": "ext://sys.stdout"
        },

        "file_handler": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": "DEBUG",
            "formatter": "simple",
            "filename": "event.log",
            "maxBytes": 1000000,
            "backupCount": 3
        },
    },

    "loggers": {
        "plugins.event_debugger": {
            "level": "DEBUG",
            "handlers": ["file_handler"],
            "propagate": "no",

        }
    },
    "root": {
        "level": "DEBUG",
        "handlers": ["console"]
    }
}
