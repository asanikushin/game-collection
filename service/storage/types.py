from constants import STATUS

from service.models.game import Game as _Game

import typing

ID_TYPE = typing.Optional[int]
GAME_TYPE = typing.Optional[_Game]
GAMES_TYPE = typing.List[GAME_TYPE]

ID_WITH_STATUS = typing.Tuple[ID_TYPE, STATUS]
GAME_WITH_STATUS = typing.Tuple[GAME_TYPE, STATUS]
GAMES_WITH_STATUS = typing.Tuple[GAMES_TYPE, STATUS]
