from constants import STATUS

from service.models.game import Game as _Game
from service.models.rating import Rating as _Rating

import typing

GAME_ID_TYPE = typing.Optional[int]
GAME_TYPE = typing.Optional[_Game]
GAMES_TYPE = typing.List[GAME_TYPE]

ID_WITH_STATUS = typing.Tuple[GAME_ID_TYPE, STATUS]
GAME_WITH_STATUS = typing.Tuple[GAME_TYPE, STATUS]
GAMES_WITH_STATUS = typing.Tuple[GAMES_TYPE, STATUS]

RATING_TYPE = typing.Optional[float]
RATING_WITH_STATUS = typing.Tuple[RATING_TYPE, STATUS]

SCORE_TYPE = typing.Optional[int]
SCORE_WITH_STATUS = typing.Tuple[SCORE_TYPE, STATUS]

RAT_TYPE = typing.Optional[_Rating]
RAT_WITH_STATUS = typing.Tuple[RAT_TYPE, STATUS]
