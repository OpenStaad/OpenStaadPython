"""
table.py — dominio Table (reportes/tablas) del subpaquete ops, sobre bridge.

Módulo nuevo respecto al paquete antiguo. Métodos alineados al oficial (PascalCase);
sin manejo de errores por ahora. `GetCellValue` usa el estilo BSTR-byref (out_bstr).
"""

from .bridge import Bridge
from ._com import acquire


class Table:
    def __init__(self, connection=None, bridge=None, filePath=None):
        staad = connection if connection is not None else acquire(filePath)
        self._b = bridge if bridge is not None else Bridge()
        self._table = staad.Table

        self._functions = [
            "CreateReport", "SaveReport", "SaveReportAll", "GetReportCount",
            "AddTable", "RenameTable", "DeleteTable", "ResizeTable", "SaveTable",
            "GetTableCount", "SetCellValue", "GetCellValue", "SetColumnHeader",
            "SetColumnUnitString", "SetRowHeader", "SetCellTextColor", "SetCellTextBold",
            "SetCellTextItalic", "SetCellTextUnderline", "SetCellTextHorzAlignment",
            "SetCellTextVertAlignment", "SetCellTextSize", "SetCellTextSizeAll",
            "DeleteReport",
        ]
        for function_name in self._functions:
            self._table._FlagAsMethod(function_name)

    def CreateReport(self, report_title: str):
        return self._table.CreateReport(report_title)

    def SaveReport(self, report_no: int):
        self._table.SaveReport(report_no)

    def SaveReportAll(self):
        self._table.SaveReportAll()

    def GetReportCount(self):
        return self._table.GetReportCount()

    def AddTable(self, report_no: int, table_name: str, row_count: int, col_count: int):
        return self._table.AddTable(report_no, table_name, row_count, col_count)

    def RenameTable(self, report_no: int, table_no: int, table_name: str):
        self._table.RenameTable(report_no, table_no, table_name)

    def DeleteTable(self, report_no: int, table_no: int):
        self._table.DeleteTable(report_no, table_no)

    def ResizeTable(self, report_no: int, table_no: int, row_nos: int, col_nos: int):
        self._table.ResizeTable(report_no, table_no, row_nos, col_nos)

    def SaveTable(self, report_no: int, table_no: int):
        self._table.SaveTable(report_no, table_no)

    def GetTableCount(self, report_no: int):
        return self._table.GetTableCount(report_no)

    def SetCellValue(self, report_no: int, table_no: int, row_no: int, col_no: int, value: str):
        self._table.SetCellValue(report_no, table_no, row_no, col_no, value)

    def GetCellValue(self, report_no: int, table_no: int, row_no: int, col_no: int) -> str:
        cell = self._b.out_bstr()
        self._table.GetCellValue(report_no, table_no, row_no, col_no, cell.ref)
        return cell.value

    def SetColumnHeader(self, report_no: int, table_no: int, col_no: int, header: str):
        self._table.SetColumnHeader(report_no, table_no, col_no, header)

    def SetColumnUnitString(self, report_no: int, table_no: int, col_no: int, unit_string: str):
        self._table.SetColumnUnitString(report_no, table_no, col_no, unit_string)

    def SetRowHeader(self, report_no: int, table_no: int, row_no: int, header: str):
        self._table.SetRowHeader(report_no, table_no, row_no, header)

    def SetCellTextColor(self, report_no: int, table_no: int, row_no: int, col_no: int, red: int, green: int, blue: int):
        self._table.SetCellTextColor(report_no, table_no, row_no, col_no, red, green, blue)

    def SetCellTextBold(self, report_no: int, table_no: int, row_no: int, col_no: int):
        self._table.SetCellTextBold(report_no, table_no, row_no, col_no)

    def SetCellTextItalic(self, report_no: int, table_no: int, row_no: int, col_no: int):
        self._table.SetCellTextItalic(report_no, table_no, row_no, col_no)

    def SetCellTextUnderline(self, report_no: int, table_no: int, row_no: int, col_no: int):
        self._table.SetCellTextUnderline(report_no, table_no, row_no, col_no)

    def SetCellTextHorzAlignment(self, report_no: int, table_no: int, row_no: int, col_no: int, align: int):
        self._table.SetCellTextHorzAlignment(report_no, table_no, row_no, col_no, align)

    def SetCellTextVertAlignment(self, report_no: int, table_no: int, row_no: int, col_no: int, align: int):
        self._table.SetCellTextVertAlignment(report_no, table_no, row_no, col_no, align)

    def SetCellTextSize(self, report_no: int, table_no: int, row_no: int, col_no: int, size: float):
        self._table.SetCellTextSize(report_no, table_no, row_no, col_no, size)

    def SetCellTextSizeAll(self, report_no: int, table_no: int, size: float):
        self._table.SetCellTextSizeAll(report_no, table_no, size)

    def DeleteReport(self, report_no: int):
        self._table.DeleteReport(report_no)
