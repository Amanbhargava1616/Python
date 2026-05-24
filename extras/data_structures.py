from collections import deque
from utils import Logger

logger_object = Logger(logger_name=__name__, file_name="data_structure")
logger = logger_object.get_logger()

dq = deque([1, 2, 3, 4, 5, 6])
logger.info(f"Deque: {dq}")

first_ele = dq.popleft()
last_ele = dq.pop()
logger.info(f"First ele of Deque: {first_ele}, Last ele of Deque: {last_ele}")
logger.info(f"Deque after popping: {dq}")

dq.appendleft(first_ele)
dq.append(last_ele)
logger.info(f"Deque after append: {dq}")

tu = ("hello",)
logger.info(f"Tuple: {tu}, length: {len(tu)}")

tu2 = tuple()
logger.info(f"Empty tuple: {tu2}, length: {len(tu2)}")

set_a = set("abracadabra")
logger.info(f"set_a: {set_a}")

dict_from_list_of_tuples = dict([("sape", 4139), ("guido", 4127), ("jack", 4098)])
logger.info(f"dict_from_list_of_tuples: {dict_from_list_of_tuples}")
