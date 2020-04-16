from .storage import Storage as _Storage
from .game import GameProcessor as _Game
from .rating import RatingProcessor as _Rating

Storage = _Storage(_Game(), _Rating())

__all__ = [Storage]
