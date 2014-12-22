
import os

BASE_URL = "https://secure.transcriptic.com"
TRANSCRIPTIC_EMAIL = None
TRANSCRIPTIC_KEY = None
ORGANIZATION = None
PROJECT = None

def get_base_url():
    """
    Gets the base url used to access Transcriptic's services.

    Returns
    -------
    str
    """
    return BASE_URL

def get_email():
    """
    Gets the email of the account used for Transcriptic's services.

    Returns
    -------
    str
    """
    if TRANSCRIPTIC_EMAIL is not None:
        return TRANSCRIPTIC_EMAIL
    return os.environ['TRANSCRIPTIC_EMAIL']

def get_key():
    """
    Gets the private key used to access Transcriptic's services.

    Returns
    -------
    str
    """
    if TRANSCRIPTIC_KEY is not None:
        return TRANSCRIPTIC_KEY
    return os.environ['TRANSCRIPTIC_KEY']

def get_organization():
    """
    Gets the currently active organization.

    Returns
    -------
    str
    """
    return ORGANIZATION

def get_project():
    """
    Gets the currently active project.

    Returns
    -------
    str
    """
    return PROJECT
