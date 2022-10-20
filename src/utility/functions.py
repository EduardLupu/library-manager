from src.domain.container import Container


def gnome_sort(array, function, reverse=False):
    index = 0  # We start from the left.
    while index < len(array):  # While the index is lower than length of the container
        if index == 0:  # If the index is 0, we increment him with 1 because we don't have anything on his left
            index += 1
        if function(array[index], array[index-1]) is True:  # If the criteria from the function is True, we continue.
            index += 1
        else:  # Else, we interchange the items and go back a position.
            auxiliary = array[index]
            array[index] = array[index - 1]
            array[index - 1] = auxiliary
            index = index - 1
    if reverse is True:  # If the optional parameter is True, the container will be reversed.
        array.reverse()
    return array  # We return the result.



def filter_container(last_container, accept_function):
    new_container = Container()
    last_container.__iter__()
    for index in range(len(last_container)):
        if accept_function(last_container[index]) is True:
            new_container.append(last_container[index])
    return new_container

