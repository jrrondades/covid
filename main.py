from openpyxl import load_workbook

def app():
    wb = load_workbook("datos/covid.xlsx", data_only=True)
    sheet = wb.active
    print(sheet.title.upper())
    print("#######")
    print()
    incremento = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    sumar = ["M", "V"]
    for row_cell in sheet['A1199':'M1213']:
        if row_cell[0].value in sumar:
            for i in incremento:
                print(i)
            incremento = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        if row_cell[2].value == "Incremento":
            for i in range(3, 13):
                incremento[i-3] += row_cell[i].value
                #print(incremento[i-3])   


if __name__ == "__main__":
    app()
