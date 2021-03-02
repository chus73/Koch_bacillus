

def number_div(number):
    """
    Searching the divisor numbers
    :param number: number from searching the divisors
    :return: Divisor numbers list.
    """
    i = 1
    div = []
    while i < number:
        if number % i == 0:
            div.append(i)
        i +=1

    # Todo número es divisible por si mismo
    div.append(number)
    return div