from typing import Mapping


remove_list = [1,5,7, 9]


new_list = [x for x in range(0,11) if x not in remove_list]


print(new_list)