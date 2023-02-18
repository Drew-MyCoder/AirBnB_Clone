#!/usr/bin/python3
"""
Init method of the models package for alx cloning of AirBnB.
"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
