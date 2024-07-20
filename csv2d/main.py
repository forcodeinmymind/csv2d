"""A module for 2D CSV (Comma-separated Values) data
"""


def create(shape: tuple[int, int], value: int):
    return [[value] * shape[0] for _ in range(shape[1])]

def conv_index(data: tuple[tuple[int]], coord: tuple[int, int]) -> int:
    return (coord[1] * len(data[0])) + coord[0]

def conv_coord(data: tuple[tuple], index: int) -> tuple[int, int]:
    return index % len(data[0]), index // len(data[0])

def index_in(data: tuple[tuple[int]], index: int) -> bool:
    return index >= 0 and index < length(data)

def coord_in(data: tuple[tuple[int]], coord: tuple[int, int]) -> bool:
    return coord[0] >= 0 and \
           coord[0] < len(data[0]) and \
           coord[1] >= 0 and \
           coord[1] < len(data)

def string(data: tuple[tuple]) -> str:
    string = str()
    for y in range(len(data)):
        for x in range(len(data[0]) - 1):
            string += f"{data[y][x]}, "
        else:
            string += f"{data[y][-1]}\n"
    return string

def get_item(data: tuple[tuple[int]], index: int | tuple[int, int]):
    if type(index) is int:
        return data[index // len(data[0])][index % len(data[0])]
    else:
        return data[index[1]][index[0]]

def set_index(data: tuple[tuple[int]], index: int | tuple[int, int], value: int):
    if type(index) is int:
        data[index // len(data[0])][index % len(data[0])] = value
    else:
        data[index[1]][index[0]] = value

def length(data: tuple[tuple]):
    return len(data) * len(data[0])

def shape(data: tuple[tuple[int]]) -> tuple[int, int]:
    # width, height = len(data[0]), len(data)
    return len(data[0]), len(data)

def save(data: tuple[tuple[int]], filename: str) -> None:
    with open(filename, "w") as file:
        for line in string(data).splitlines(True):
            file.write(line)

def load(filename: str) -> tuple[tuple[int]]:
    with open(filename, "r") as file:
        _list = list()
        for line in file.read().splitlines():
            _list.append([int(x) for x in line.split(", ")])
        return _list
