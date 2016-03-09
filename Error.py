import logging

class Error(Exception):
    def __init__(self, msg):
        self.message = msg
        logging.error("WYSTAPIL WYJATEK: " + msg)

    def __str__(self):
        return self.message
