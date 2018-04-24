from functools import reduce

Celsius = [25, 26.6, 27, 41, 36.6]

def map_celsius_to_Fahrenheit():
    '''
    Formula for converting from x Celsius: F = (9/5)x + 32
    '''
    pass

def filter_bigger_than_90(input_list):
    pass


def sum_by_reduce_operation(input_list):
	pass


if __name__ == '__main__':
    print(' '.join(str(e) for e in map_celsius_to_Fahrenheit()))
    print(' '.join(str(e) for e in filter_bigger_than_90(map_celsius_to_Fahrenheit())))
    print(sum_by_reduce_operation(map_celsius_to_Fahrenheit()))
