from openpyxl import load_workbook

def app():
    wb = load_workbook("datos/covid.xlsx", data_only=True)
    sheet = wb.active
    print(sheet.title.upper())
    print("#######")
    print()

    for row_cell in sheet['A1199':'K1201']:
        for cell in row_cell:
            print(cell.value)


if __name__ == "__main__":
    app()
