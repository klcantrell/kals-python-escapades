# from utils import output, is_even
from KalUtils import utils
from KalUtils.InputOutput.utils import output

my_list = ['Kalalau', 5, 'Zack', 6, 'Red XIII', 7]

for item in my_list:
    #     if is_even(item):
    #         output(item)
    if utils.is_even(item):
        output(item)
