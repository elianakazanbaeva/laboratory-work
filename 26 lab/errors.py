class ErrorHandler:
    def __init__(self):
        self.status = 'ok'
        self.log = []

    def checkFile(self, path):
        try:
            handle = open(path, 'r')
            content = handle.read()
            handle.close()
            if len(content) == 0:
                self.showError('файл пуст: ' + path)
                return False
            self.status = 'found'
            return True
        except FileNotFoundError:
            self.showError('файл не найден: ' + path)
            return False
        except PermissionError:
            self.showError('нет доступа: ' + path)
            return False
        except Exception as e:
            self.showError('ошибка файла: ' + str(e))
            return False

    def checkNumber(self, val):
        try:
            res = int(val)
            return res
        except ValueError:
            self.showError('не число: ' + str(val))
            return None
        except Exception as e:
            self.showError('ошибка числа: ' + str(e))
            return None

    def checkInputNumber(self, val):
        try:
            res = int(val)
            return res
        except ValueError:
            self.showError('введено не число: ' + str(val))
            return None
        except Exception as e:
            self.showError('ошибка ввода: ' + str(e))
            return None

    def checkOperation(self, op):
        validops = ['+', '-', '*', '/', '%', '^']
        if op in validops:
            return True
        self.showError('недопустимая операция: ' + str(op))
        return False

    def checkDivision(self, divisor):
        if divisor == 0:
            self.showError('деление на ноль')
            return False
        return True

    def showError(self, message):
        errtext = 'ОШИБКА: ' + message
        print(errtext)
        self.log.append(errtext)

    def getLog(self):
        return self.log

    def reset(self):
        self.status = 'ok'
        self.log = []