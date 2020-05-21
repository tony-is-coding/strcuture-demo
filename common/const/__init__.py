# 常量定义, 配合数据库层面做的常量枚举,
# 建议统一在Python3 使用 Enum 及派生类作为枚举限定,


from enum import IntEnum, unique, Enum


@unique
class E(IntEnum):
    A = 1
    B = 2
    C = 3


class CombineE(tuple, Enum):
    A = (1, "tony")
    B = (2, "park")
    C = (3, "jane")


if __name__ == '__main__':
    e = E(1)
    assert e.value == 1
    assert E.A.value == 1
    try:
        e1 = E(4)
    except ValueError:
        ...

    print(CombineE.A.value)
