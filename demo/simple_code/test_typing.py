from typing import Callable, List, NewType, Any, NoReturn, Union, Optional, Literal, TypeVar, Generic, TypedDict, Dict, Mapping, List, Sequence, Set, Tuple, Iterable

# Blog: https://blog.csdn.net/fengbingchun/article/details/122288737

var = 9
# reference: https://docs.python.org/3/library/typing.html
if var == 1: # Callable
    def other_function(x: int, y: float) -> float:
        print(f"x: {x}, y: {y}")
        return y

    def any_function(func: Callable[[int, float], float], x: int, y: float) -> float:
        return func(x, y)

    any_function(other_function, x=10, y=20)
    any_function(other_function, x="abc", y=20) # 注:此条语句可以正常执行,类型提示(type hints)对运行实际上是没有影响的

    def get_addr(csdn: str, github: str, port: int=403) -> str:
        return f"csdn: {csdn}, github: {github}, port: {port}"

    def get_addr() -> Callable[[str, str, int], str]:
        return get_addr
elif var == 2: # Type aliases
    # Vector和List[float]将被视为可互换的同义词
    Vector = List[float]

    def scale(scalar: float, vector: Vector) -> Vector:
        return [scalar * num for num in vector]

    # a list of floats qualifies as a Vector.
    new_vector = scale(2.0, [1.0, -4.2, 5.4]); print(new_vector) # [2.0, -8.4, 10.8]
elif var == 3: # NewType
    UserId = NewType('UserId', int) # 实际上UserID就是一个int类型,可以对其像int一样正常操作
    some_id = UserId(524313); print(some_id) # 524313

    def get_user_name(user_id: UserId) -> str:
        return str(user_id)

    user_a = get_user_name(UserId(42351)); print(user_a) # 42351

    # 可以对UserId类型的变量执行所有int操作,但结果始终为int类型
    output = UserId(23413) + UserId(54341); print(output) # 77754
elif var == 4: # Any
    a: Any = None
    a = [] # OK
    a = 2 # OK

    s: str = ""
    s = a # OK
    print(s) # 2
elif var == 5: # NoReturn
    def stop() -> NoReturn:
        raise RuntimeError('no way')
    
    stop()
elif var == 6: # Union
    # 联合类型的联合类型会被展开(flattened)
    Union[Union[int, str], float] == Union[int, str, float]
    # 仅有一个参数的联合类型就是该参数自身
    Union[int] == int
    # 冗余的参数会被跳过(skipped)
    Union[int, str, int] == Union[int, str] # == int | str
    # 在比较联合类型的时候，参数顺序会被忽略(ignored)
    Union[int, str] == Union[str, int]
elif var == 7: # Optional
    # 可选类型与含默认值的可选参数不同,含默认值的可选参数不需要在类型注解(type annotation)上添加Optional限定符,因为它仅是可选的
    def foo(arg: int = 0) -> None: ...
    # 显式应用None值时,不管该参数是否可选,Optional都适用
    def foo(arg: Optional[int] = None) -> None: ...
elif var == 8: # Literal
    def validate_simple(data: Any) -> Literal[True]: ... # always returns True

    MODE = Literal["r", "rb", "w", "wb"]
    def open_helper(file: str, mode: MODE) -> str:
        return file + ":" + mode

    print(open_helper("/some/path", "r")) # /some/path:r
elif var == 9: # TypeVar, Generic
    T = TypeVar('T') # Declare type variable, Can be anything
    # 泛型类型支持多个类型变量,不过,类型变量可能会受到限制
    S = TypeVar('S', int, str) # Must be int or str

    class StrangePair(Generic[T, S]): ...

    # 泛型类型变量的参数都必须是不同的
    #class Pair(Generic[T, T]): ... # TypeError: Parameters to Generic[...] must all be unique

    length = "5.5"
    Length = TypeVar("Length", int, float, None) # Length可以使用int, float或None来表示
    def get_length() -> Length:
        return length

    print(get_length()) # 5.5
elif var == 10: # TypedDict
    class Point2D(TypedDict):
        x: int
        y: int
        label: str

    a: Point2D = {'x': 1, 'y': 2, 'label': 'good'}  # OK
    b: Point2D = {'z': 3, 'label': 'bad'}           # Fails type check

    assert Point2D(x=1, y=2, label='first') == dict(x=1, y=2, label='first')
elif var == 11: # Dict
    def count_words(text: str) -> Dict[str, int]: ...
    x: Dict[str, int] = {"beijing", 1}; print(x) # {"beijing", 1}
elif var == 12: # Mapping
    def get_position_in_index(word_list: Mapping[str, int], word: str) -> int:
        return word_list[word]

    def func(m: Mapping[int, str]) -> List[int]:
        return list(m.keys())

    print(func({0: "no", 1: "yes"})) # [0, 1]
elif var == 13: # List
    T = TypeVar('T', int, float)

    def vec2(x: T, y: T) -> List[T]:
        return [x, y]

    print(vec2(3, 2)) # [3, 2]

    def keep_positives(vector: Sequence[T]) -> List[T]:
        return [item for item in vector if item > 0]

    x: List[int] = [1, 2, 3]; print(x) # [1, 2, 3]
elif var == 14: # Set
    x: Set[int] = {1, 2, 3}; print(x) # {1, 2, 3}
elif var == 15: # Tuple
    # 指定所有元素的类型
    x: Tuple[int, float, str] = (1, 2.1, "beijing");  print(x) # (1, 2.1, "beijing")
    # 可变长度的元组
    y: Tuple[int, ...] = (1, 2.1, "beijing"); print(y) # (1, 2.1, "beijing")
elif var == 16: # Iterable
    def func(l: Iterable[int]) -> List[str]:
        return [str(x) for x in l]

    print(func(range(1, 5))) # ['1', '2', '3', '4']

print("test finish")
