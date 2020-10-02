import csv

from faker import Faker  # pip install Faker

fake = Faker()

# Proceso donde se leen todas las cedulas buenas
cedulas = []
with open('cedulas.csv', newline='') as cedulasfile:
    reader = csv.reader(cedulasfile)
    for row in reader:
        cedulas.append(row[0])
cedulasfile.close()
cantidad = int(len(cedulas))
# cantidad = 10
test_cases = {}


def process(name):
    filename = '%s.csv' % name
    with open(filename, 'w', newline='') as csvfile:
        print("generando %s" % filename)
        w = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_NONE)
        w.writerow([
            'ci', 'tipoDocumento', 'nroPasaporte', 'fechaVencimiento',
            'nombre', 'apellido'
        ])
        desde = fake.pyint(min_value=0, max_value=cantidad)
        hasta = fake.pyint(min_value=(cantidad + 1), max_value=(cantidad * 2))
        for c in cedulas[0:10000]:
            # for c in cedulas:
            test_cases[name](w, c)
    csvfile.close()


def cp1(w, c):
    tipo_documento = 'ci'
    documento = c
    pasaporte = ""
    fecha = fake.date_between(start_date='+15d', end_date='+15d')
    first_name = fake.first_name()
    last_name = fake.last_name()
    w.writerow([
        documento, tipo_documento, pasaporte,
        fecha.strftime("%d/%m/%Y"), first_name, last_name
    ])


def cp2(w, c):
    tipo_documento = 'ci'
    # Cedula NO en ID Uruguay
    documento = (fake.pyint(min_value=10000000, max_value=20000000))
    pasaporte = ""
    fecha = fake.date_between(start_date='+15d', end_date='+15d')
    first_name = fake.first_name()
    last_name = fake.last_name()
    w.writerow([
        documento, tipo_documento, pasaporte,
        fecha.strftime("%d/%m/%Y"), first_name, last_name
    ])


def cp3(w, c):
    tipo_documento = 'ci'
    documento = ""  # Cedula Vacia
    pasaporte = ""
    fecha = fake.date_between(start_date='+15d', end_date='+15d')
    first_name = fake.first_name()
    last_name = fake.last_name()
    w.writerow([
        documento, tipo_documento, pasaporte,
        fecha.strftime("%d/%m/%Y"), first_name, last_name
    ])


def cp4(w, c):
    tipo_documento = 'ci'
    documento = c
    pasaporte = ""
    fecha = fake.date_between(start_date='+60d', end_date='+60d')  # Bien
    first_name = fake.first_name()
    last_name = fake.last_name()
    w.writerow([
        documento, tipo_documento, pasaporte,
        fecha.strftime("%d/%m/%Y"), first_name, last_name
    ])


def cp5(w, c):
    tipo_documento = 'ci'
    documento = c
    pasaporte = ""
    fecha = fake.date_between(start_date='+61d', end_date='+61d')  # Mal
    first_name = fake.first_name()
    last_name = fake.last_name()
    w.writerow([
        documento, tipo_documento, pasaporte,
        fecha.strftime("%d/%m/%Y"), first_name, last_name
    ])


def cp6(w, c):
    tipo_documento = 'ci'
    documento = c
    pasaporte = ""
    fecha = fake.date_between(start_date='-1d', end_date='-1d')  # Mal
    first_name = fake.first_name()
    last_name = fake.last_name()
    w.writerow([
        documento, tipo_documento, pasaporte,
        fecha.strftime("%d/%m/%Y"), first_name, last_name
    ])


def cp7(w, c):
    tipo_documento = 'ci'
    documento = c
    pasaporte = ""
    fecha = ""  # Mal
    first_name = fake.first_name()
    last_name = fake.last_name()
    w.writerow([
        documento, tipo_documento, pasaporte,
        "%s" % fecha, first_name, last_name
    ])


def cp8(w, c):
    tipo_documento = 'ci'
    documento = c
    pasaporte = ""
    fecha = "Hola"  # Mal
    first_name = fake.first_name()
    last_name = fake.last_name()
    w.writerow([
        documento, tipo_documento, pasaporte,
        "%s" % fecha, first_name, last_name
    ])


def cp9(w, c):
    tipo_documento = 'ci'
    documento = c
    pasaporte = ""
    fecha = fake.date_between(start_date='+15d', end_date='+15d')

    first_name = [
        fake.pyint(min_value=10000000, max_value=20000000), "!@#!#@"
    ][fake.pyint(min_value=0, max_value=1)]  # Mal
    last_name = fake.last_name()
    w.writerow([
        documento, tipo_documento, pasaporte,
        fecha.strftime("%d/%m/%Y"), first_name, last_name
    ])


def cp10(w, c):
    tipo_documento = 'ci'
    documento = c
    pasaporte = ""
    fecha = fake.date_between(start_date='+15d', end_date='+15d')

    first_name = ["", "     "][fake.pyint(min_value=0, max_value=1)]  # Mal
    last_name = fake.last_name()
    w.writerow([
        documento, tipo_documento, pasaporte,
        fecha.strftime("%d/%m/%Y"), first_name, last_name
    ])


def cp11(w, c):
    tipo_documento = 'ci'
    documento = c
    pasaporte = ""
    fecha = fake.date_between(start_date='+15d', end_date='+15d')

    first_name = fake.first_name()
    last_name = [fake.pyint(min_value=10000000, max_value=20000000),
                 "!@#!#@"][fake.pyint(min_value=0, max_value=1)]  # Mal
    w.writerow([
        documento, tipo_documento, pasaporte,
        fecha.strftime("%d/%m/%Y"), first_name, last_name
    ])


def cp12(w, c):
    tipo_documento = 'ci'
    documento = c
    pasaporte = ""
    fecha = fake.date_between(start_date='+15d', end_date='+15d')

    first_name = fake.first_name()
    last_name = ["", "     "][fake.pyint(min_value=0, max_value=1)]  # Mal
    w.writerow([
        documento, tipo_documento, pasaporte,
        fecha.strftime("%d/%m/%Y"), first_name, last_name
    ])


def cp13(w, c):
    tipo_documento = 'psp'
    documento = ""
    pasaporte = fake.pyint(min_value=10000000, max_value=20000000)
    fecha = fake.date_between(start_date='+15d', end_date='+15d')

    first_name = fake.first_name()
    last_name = fake.last_name()
    w.writerow([
        documento, tipo_documento, pasaporte,
        fecha.strftime("%d/%m/%Y"), first_name, last_name
    ])


def cp14(w, c):
    tipo_documento = 'psp'
    documento = ""
    pasaporte = fake.pyint(min_value=1000, max_value=2000)  # Mal
    fecha = fake.date_between(start_date='+15d', end_date='+15d')

    first_name = fake.first_name()
    last_name = fake.last_name()
    w.writerow([
        documento, tipo_documento, pasaporte,
        fecha.strftime("%d/%m/%Y"), first_name, last_name
    ])


def cp15(w, c):
    tipo_documento = 'psp'
    documento = ""
    pasaporte = ""  # Mal
    fecha = fake.date_between(start_date='+15d', end_date='+15d')

    first_name = fake.first_name()
    last_name = fake.last_name()
    w.writerow([
        documento, tipo_documento, pasaporte,
        fecha.strftime("%d/%m/%Y"), first_name, last_name
    ])


test_cases["cp1"] = cp1
test_cases["cp2"] = cp2
test_cases["cp3"] = cp3
test_cases["cp4"] = cp4
test_cases["cp5"] = cp5
test_cases["cp6"] = cp6
test_cases["cp7"] = cp7
test_cases["cp8"] = cp8
test_cases["cp9"] = cp9
test_cases["cp10"] = cp10
test_cases["cp11"] = cp11
test_cases["cp12"] = cp12
test_cases["cp13"] = cp13
test_cases["cp14"] = cp14
test_cases["cp15"] = cp15
process("cp1")
process("cp2")
process("cp3")
process("cp4")
process("cp5")
process("cp6")
process("cp7")
process("cp8")
process("cp9")
process("cp10")
process("cp11")
process("cp12")
process("cp13")
process("cp14")
process("cp15")

test_cases_16 = {}

test_cases_16["cp1"] = cp1
test_cases_16["cp2"] = cp2


def cp16(w, c):
    idx = "cp%s" % fake.pyint(min_value=1, max_value=len(test_cases_16))
    cp = test_cases_16[idx]
    cp(w, c)


with open('cp16.csv', 'w', newline='') as csvfile:
    print("++generando cp16++")
    mucha_cantidad = int(len(cedulas) / 2)
    w = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_NONE)
    w.writerow([
        'ci', 'tipoDocumento', 'nroPasaporte', 'fechaVencimiento', 'nombre',
        'apellido'
    ])
    desde = fake.pyint(min_value=0, max_value=mucha_cantidad)
    hasta = fake.pyint(min_value=(mucha_cantidad + 1),
                       max_value=(mucha_cantidad * 2))
    for c in cedulas[desde:hasta]:
        cp16(w, c)
csvfile.close()

# Aleatorio para miles
# with open('cp1.csv', 'w', newline='') as csvfile:
#     w = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_NONE)
#     w.writerow([
# 'ci','tipoDocumento','nroPasaporte','fechaVencimiento', 'nombre', 'apellido'
# ])
#     for c in cedulas[0:10]:
#         #  Aqui es donde se determina si es pasaporte (0) o cedula (1)
#         indice = fake.pyint(min_value=0, max_value=1)
#         tipo_documento = ['psp', 'ci'][indice]
#                           # 0    # 1

#         # Si es psp genera un numero, si no, no genera nada
#         documento = cedula if (indice == 1) else ""
#         pasaporte = (fake.pyint(min_value=10000000, max_value=20000000))
# if indice == 0 else ""

#         # Genera una fecha desde hoy (today) hasta +60dias
#         fecha = fake.date_between(start_date='+1d', end_date='+15d')
#         vencimiento = (fecha.day, fecha.month, fecha.year)

#         # Aqui se genera un username aleatorio
# first_name = fake.first_name()
# last_name = fake.last_name()

#         # Aqui escribe cada linea del csv
#         w.writerow([documento, tipo_documento, pasaporte,
# "%s/%s/%s" % vencimiento, first_name, last_name])
# csvfile.close()
