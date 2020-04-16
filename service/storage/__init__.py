from .storage import Storage as _Storage
from .game import GameProcessor as _Game

Storage = _Storage(_Game())

__all__ = [Storage]
