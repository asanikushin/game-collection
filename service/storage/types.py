from utils.constants import STATUS

from service.models.game import Game as _Game
from service.models.rating import Rating as _Rating

from typing import Optional, Tuple, List

# #### original results

GAME_ID_TYPE = Optional[int]
GAME_TYPE = Optional[_Game]
GAMES_TYPE = List[GAME_TYPE]

RATING_VALUE_TYPE = Optional[float]
RATING_TYPE = Optional[_Rating]

# #### results with STATUS

COUNT_WITH_STATUS = Tuple[int, STATUS]

ID_WITH_STATUS = Tuple[GAME_ID_TYPE, STATUS]
GAME_WITH_STATUS = Tuple[GAME_TYPE, STATUS]
GAMES_WITH_STATUS = Tuple[GAMES_TYPE, STATUS]

RATING_VALUE_WITH_STATUS = Tuple[RATING_VALUE_TYPE, STATUS]
RATING_WITH_STATUS = Tuple[RATING_TYPE, STATUS]
