import os
import xlrd as xl


class ReadData:
    def __init__(self, sheet_index):
        self.current_directory = os.getcwd()
        self.excel_path = self.current_directory + '\\' + "ExcelFiles"
        self.sheet_index = sheet_index
        self.path_validator = False

        excel_file_list = os.listdir(self.excel_path)
        if len(excel_file_list) == 1:
            self.excel_path += '\\' + excel_file_list[0]
        else:
            print("There is no excel file located or there are too many located in " +
                            "{} \n".format(self.excel_path) +
                            "please install the correct excel file in said path.")

    def get_size(self):
        """ FUNCTION:
            Returns a pair list of excel size: rows, columns"""
        sheet = self.open_excel_file_sheet(self.sheet_index)
        return sheet.nrows, sheet.ncols

    def open_excel_file_sheet(self, sheet_index):
        """ FUNCTION:
        Opens the excel file and returns the sheet object """
        wb = xl.open_workbook(self.excel_path)
        sheet = wb.sheet_by_index(sheet_index)
        return sheet

    def get_row(self, row_index, from_index=None, to_index=None):
        sheet = self.open_excel_file_sheet(self.sheet_index)
        list_of_values = list()

        if from_index is None:
            from_index = 0
        if to_index is None:
            to_index = sheet.ncols
        else:
            to_index += 1
            if to_index > sheet.ncols:
                to_index = sheet.ncols

        for i in range(from_index, to_index):
            list_of_values.append(sheet.cell_value(row_index, i))

        return list_of_values

    def get_column(self, column_index, from_index=None, to_index=None):
        sheet = self.open_excel_file_sheet(self.sheet_index)
        list_of_values = list()

        if from_index is None:
            from_index = 0
        if to_index is None:
            to_index = sheet.nrows
        else:
            to_index += 1
            if to_index > sheet.nrows:
                to_index = sheet.nrows

        for i in range(from_index, to_index):
            list_of_values.append(sheet.cell_value(i, column_index))

        return list_of_values

    def get_value(self, row_index, column_index):
        sheet = self.open_excel_file_sheet(self.sheet_index)

        if row_index > sheet.nrows:
            row_index = sheet.nrows
        if column_index > sheet.ncols:
            column_index = sheet.ncols

        return sheet.cell_value(row_index, column_index)

    def get_box_of_values(self):
        """ todo extract data from a box of values """
        pass


