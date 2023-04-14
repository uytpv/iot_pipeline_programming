from typing import Callable, TypedDict


class MenuOption(TypedDict):
    desc: str
    action: Callable