# Interface Segregation Principle (ISP) - Interface Splitting
from abc import abstractmethod


class Printer:
    @abstractmethod
    def print(self, document):
        pass


class Scanner:
    @abstractmethod
    def scan(self, document):
        pass


class MyPrinter(Printer):
    def print(self, document):
        print(document)


class Photocopier(Printer, Scanner):

    def scan(self, document):
        pass

    def print(self, document):
        pass


class MultiFunctionDevice(Printer, Scanner):
    @abstractmethod
    def scan(self):
        pass

    @abstractmethod
    def print(self):
        pass


class MultiFunctionMachine(MultiFunctionDevice):
    def __init__(self, printer, scanner):
        self.scanner = scanner
        self.printer = printer

    def print(self):
        self.printer.print()

    def scan(self):
        self.scanner.scan()



