"""This module wraps the mongodb interface."""

import os
from pymongo import MongoClient


def client(username : str =None, password : str=None, base_uri : str=None) -> MongoClient:
    """Creates the mongo client from the provided params.

    Args:
        username (str, optional): DB username. Defaults to None.
        password (str, optional): DB password. Defaults to None.
        base_uri (str, optional): DB base URI. Defaults to None.

    Returns:
        MongoClient: the client.
    """
    if not username:
        username = os.getenv("DB_USER")
    if not password:
        password = os.getenv("DB_PASSWORD")
    if not base_uri:
        base_uri = os.getenv("DB_BASE_URI")

    return MongoClient(f"mongodb+srv://{username}:{password}@{base_uri}"
                       "/?retryWrites=true&w=majority")
    