import datetime
import inspect
from pathlib import Path
from typing import Any
from typing import Optional


class MyLogger:
    def __init__(self, logger_name: str = "MyLogger", is_print_log: bool = True):
        """
        Constructor
        :param logger_name: name of this logger
        :param is_print_log: output to command line
        """
        self.loggerName: str = logger_name
        self.printFlag: bool = is_print_log
        self.filePathList: list[Path] = []

    def addLogFilePath(self, path: Path) -> None:
        """
        Specify the file path to be logged
        :param path: file path
        """
        if path in self.filePathList:
            return
        self.__makeFileIfNotExists(path)
        self.filePathList.append(path)

    def isPrintLog(self, is_print_log: bool) -> None:
        """
        Specify whether the log should be displayed to command line
        :param is_print_log: output to command line
        """
        self.printFlag = is_print_log

    def info(self, log: Any) -> None:
        """
        show Info Log
        :param log: log message
        """
        self.__addLog("INFO", log)

    def debug(self, log: Any) -> None:
        """
        show Debug log
        :param log: log message
        """
        self.__addLog("DEBUG", log)

    def warn(self, log: Any) -> None:
        """
        show Warn log
        :param log: log message
        """
        self.__addLog("WARN", log)

    def error(self, log: Any) -> None:
        """
        show Error log
        :param log: log message
        """
        self.__addLog("ERROR", log)

    def notice(self, log: Any) -> None:
        """
        show Notice log
        :param log: log message
        """
        self.__addLog("NOTICE", log)

    def startFuncLog(self) -> None:
        """
        show function start log
        """
        funcName = inspect.stack()[1].function
        self.info("Start {}".format(funcName))

    def finishFuncLog(self) -> None:
        """
        show function finish log
        """
        funcName = inspect.stack()[1].function
        self.info("Finish {}".format(funcName))

    def createLog(self, target_name: Optional[str] = None) -> None:
        """
        show create log
        :param target_name: name of the generated target
        """
        if target_name is None:
            target_name = self.loggerName
        self.info("Created {}".format(target_name))

    def __addLog(self, tag: str, log: Any) -> None:
        tag = self.__makeFormatTag(tag)
        dataString = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        logText = "{} {} {} {}".format(dataString, self.loggerName, tag, log)
        if self.printFlag:
            print(logText)

        if len(self.filePathList) == 0:
            return
        self.__addLogToFile(logText)

    def __addLogToFile(self, log_text: str) -> None:
        for filePath in self.filePathList:
            self.__makeFileIfNotExists(filePath)
            with open(filePath, "a", encoding="utf-8") as f:
                f.write(log_text + "\n")

    @staticmethod
    def __makeFormatTag(tag: str) -> str:
        return "[{}]".format(tag).ljust(8)

    @staticmethod
    def __makeFileIfNotExists(path: Path) -> None:
        if not path.exists():
            path.parent.mkdir(parents=True)
            path.touch()


if __name__ == "__main__":
    pass
