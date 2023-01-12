from pathlib import Path
from typing import Any, Optional, List

class MyLogger:
    loggerName: str
    printFlag: bool
    filePathList: List[Path]
    def __init__(self, logger_name: str = ..., is_print_log: bool = ...) -> None: ...
    def addLogFilePath(self, path: Path) -> None: ...
    def isPrintLog(self, is_print_log: bool) -> None: ...
    def info(self, log: Any) -> None: ...
    def debug(self, log: Any) -> None: ...
    def warn(self, log: Any) -> None: ...
    def error(self, log: Any) -> None: ...
    def notice(self, log: Any) -> None: ...
    def startFuncLog(self) -> None: ...
    def finishFuncLog(self) -> None: ...
    def createLog(self, target_name: Optional[str] = ...) -> None: ...
