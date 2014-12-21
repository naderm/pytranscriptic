

BASE_URL = "https://secure.transcriptic.com"
TRANSCRIPTIC_EMAIL = None
TRANSCRIPTIC_KEY = None
ORGANIZATION = None
PROJECT = None

def get_base_url():
    return BASE_URL

def get_email():
    if TRANSCRIPTIC_EMAIL is not None:
        return TRANSCRIPTIC_EMAIL
    return os.environ['TRANSCRIPTIC_EMAIL']

def get_key():
    if TRANSCRIPTIC_KEY is not None:
        return TRANSCRIPTIC_KEY
    return os.environ['TRANSCRIPTIC_KEY']

def get_organization():
    return ORGANIZATION

def get_project():
    return PROJECT

def get_headers():
    return {
        "X-User-Email": get_email(),
        "X-User-Token": get_key(),
        "Content-Type": "application/json",
        "Accept": "application/json",
        }
