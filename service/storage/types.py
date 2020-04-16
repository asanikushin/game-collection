from constants import STATUS

from service.models.game import Game as _Game

import typing

ID_TYPE = typing.Optional[int]
MODEL_TYPE = typing.Optional[_Game]
MODELS_TYPE = typing.List[MODEL_TYPE]

ID_WITH_STATUS = typing.Tuple[ID_TYPE, STATUS]
MODEL_WITH_STATUS = typing.Tuple[MODEL_TYPE, STATUS]
MODELS_WITH_STATUS = typing.Tuple[MODELS_TYPE, STATUS]
