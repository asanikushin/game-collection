from utils.constants import STATUS

import typing

ID_TYPE = typing.Optional[int]

ID_WITH_STATUS = typing.Tuple[ID_TYPE, STATUS]

TOKEN = str
TOKEN_WITH_STATUS = typing.Tuple[TOKEN, STATUS]
TOKEN_PAIR = typing.Tuple[TOKEN, TOKEN]
TOKENS_WITH_STATUS = typing.Tuple[TOKEN_PAIR, STATUS]
