import json
import logging
from typing import Optional, Union


class SomeClass :   
    def __init__(self):
        self._logger = logging.getLogger()

    def _print_json(self, arg1: dict) -> None:
        self._logger.info(f"{json.dumps(arg1)}")
        return None

    def eval_arg(self, arg1: Optional[Union[dict, str]] = None) -> None:
        if isinstance(arg1, str):
            payload = {"key": arg1}
        elif isinstance(arg1, dict) and\
          arg1["key"]:
            payload = arg1
        else:
            payload = {"key": "default"}
        self._print_json(payload)
        return None

    def echo_me(self, arg1: str) -> str:
        return f"{arg1} {arg1}"
