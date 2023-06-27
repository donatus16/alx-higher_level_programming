#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        i = a / b
        print('Inside result: {}'.format(i))
    except (ZeroDivisionError, TypeError):
        i = None
    finally:
        return(i)
