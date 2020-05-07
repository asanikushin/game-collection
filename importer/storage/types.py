from utils.constants import STATUS

import uuid
from typing import Optional, Tuple, Dict

FILE_ID_TYPE = Optional[uuid.UUID]
FILE_TYPE = str
ID_WITH_STATUS = Tuple[FILE_ID_TYPE, STATUS]
