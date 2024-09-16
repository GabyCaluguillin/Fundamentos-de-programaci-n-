# Crear una matriz 3D para almacenar datos de temperaturas
# Primera dimensión: Ciudades (3 ciudades)
# Segunda dimensión: Semanas (4 semanas)
# Tercera dimensión: Días de la semana (7 días)
temperaturas = [
    [   # Ciudad 1
        [   # Semana 1
            {"day": "Lunes", "temp": 73},
            {"day": "Martes", "temp": 60},
            {"day": "Miércoles", "temp": 42},
            {"day": "Jueves", "temp": 39},
            {"day": "Viernes", "temp": 45},
            {"day": "Sábado", "temp": 58},
            {"day": "Domingo", "temp": 62}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 86},
            {"day": "Martes", "temp": 59},
            {"day": "Miércoles", "temp": 83},
            {"day": "Jueves", "temp": 35},
            {"day": "Viernes", "temp": 57},
            {"day": "Sábado", "temp": 99},
            {"day": "Domingo", "temp": 63}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 78},
            {"day": "Martes", "temp": 41},
            {"day": "Miércoles", "temp": 85},
            {"day": "Jueves", "temp": 62},
            {"day": "Viernes", "temp": 98},
            {"day": "Sábado", "temp": 61},
            {"day": "Domingo", "temp": 85}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 35},
            {"day": "Martes", "temp": 78},
            {"day": "Miércoles", "temp": 50},
            {"day": "Jueves", "temp": 89},
            {"day": "Viernes", "temp": 54},
            {"day": "Sábado", "temp": 57},
            {"day": "Domingo", "temp": 71}
        ]
    ],
    [   # Ciudad 2
        [   # Semana 1
            {"day": "Lunes", "temp": 62},
            {"day": "Martes", "temp": 64},
            {"day": "Miércoles", "temp": 68},
            {"day": "Jueves", "temp": 70},
            {"day": "Viernes", "temp": 73},
            {"day": "Sábado", "temp": 75},
            {"day": "Domingo", "temp": 79}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 63},
            {"day": "Martes", "temp": 66},
            {"day": "Miércoles", "temp": 70},
            {"day": "Jueves", "temp": 72},
            {"day": "Viernes", "temp": 75},
            {"day": "Sábado", "temp": 77},
            {"day": "Domingo", "temp": 81}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 61},
            {"day": "Martes", "temp": 65},
            {"day": "Miércoles", "temp": 68},
            {"day": "Jueves", "temp": 70},
            {"day": "Viernes", "temp": 72},
            {"day": "Sábado", "temp": 76},
            {"day": "Domingo", "temp": 80}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 64},
            {"day": "Martes", "temp": 67},
            {"day": "Miércoles", "temp": 69},
            {"day": "Jueves", "temp": 71},
            {"day": "Viernes", "temp": 74},
            {"day": "Sábado", "temp": 77},
            {"day": "Domingo", "temp": 80}
        ]
    ],
    [   # Ciudad 3
        [   # Semana 1
            {"day": "Lunes", "temp": 90},
            {"day": "Martes", "temp": 92},
            {"day": "Miércoles", "temp": 94},
            {"day": "Jueves", "temp": 91},
            {"day": "Viernes", "temp": 88},
            {"day": "Sábado", "temp": 85},
            {"day": "Domingo", "temp": 82}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 89},
            {"day": "Martes", "temp": 91},
            {"day": "Miércoles", "temp": 93},
            {"day": "Jueves", "temp": 90},
            {"day": "Viernes", "temp": 87},
            {"day": "Sábado", "temp": 84},
            {"day": "Domingo", "temp": 81}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 91},
            {"day": "Martes", "temp": 93},
            {"day": "Miércoles", "temp": 95},
            {"day": "Jueves", "temp": 92},
            {"day": "Viernes", "temp": 89},
            {"day": "Sábado", "temp": 86},
            {"day": "Domingo", "temp": 83}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 88},
            {"day": "Martes", "temp": 90},
            {"day": "Miércoles", "temp": 92},
            {"day": "Jueves", "temp": 89},
            {"day": "Viernes", "temp": 86},
            {"day": "Sábado", "temp": 83},
            {"day": "Domingo", "temp": 80}
        ]
    ]
]


 # Funcion para calcular el promedio de temperatura por semana

def calcular_promedio(ciudad):
    for semana_index, semana in enumerate(ciudad, start=1):
            suma = sum(dia["temp"] for dia in semana)
            promedio = suma / len(semana)
            print(f"Semana {semana_index}: Promedio de temperatura: {promedio:.2f}")
# Menu interactivo
while True:
    print("seleccione una ciudad ")
    print("1 - ciudad 1")
    print("2 - ciudad 2")
    print("3 - ciudad 3")
    print("4 - salir ")


    # Función para calcular el promedio total de temperatura de una ciudad
    def calcular_promedio_total(ciudad):
        suma_total = 0
        num_dias = 0
        for semana in ciudad:
            suma_total += sum(dia["temp"] for dia in semana)
            num_dias += len(semana)
        promedio_total = suma_total / num_dias
        return promedio_total


    # Menú interactivo
    while True:
        print("\nSeleccione una opción:")
        print("1 - Calcular promedio semanal de temperaturas para una ciudad")
        print("2 - Calcular promedio total de temperaturas para cada ciudad")
        print("3 - Salir")

        opcion = input("Ingrese el número de la opción deseada: ")

        if opcion == '1':
            print("\nSeleccione una ciudad:")
            print("1 - Ciudad 1")
            print("2 - Ciudad 2")
            print("3 - Ciudad 3")
            ciudad_opcion = input("Ingrese el número de la ciudad: ")

            if ciudad_opcion == '1':
                print("\nDatos de la Ciudad 1")
                calcular_promedio_semanal(temperaturas[0])
            elif ciudad_opcion == '2':
                print("\nDatos de la Ciudad 2")
                calcular_promedio_semanal(temperaturas[1])
            elif ciudad_opcion == '3':
                print("\nDatos de la Ciudad 3")
                calcular_promedio_semanal(temperaturas[2])
            else:
                print("Ciudad no válida. Por favor, intente de nuevo.")

        elif opcion == '2':
            print("\nPromedio total de temperaturas para cada ciudad:")
            for ciudad_index, ciudad in enumerate(temperaturas, start=1):
                promedio_total = calcular_promedio_total(ciudad)
                print(f"Ciudad {ciudad_index}: Promedio total de temperatura: {promedio_total:.2f}")

        elif opcion == '3':
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Por favor, intente de nuevo.")

    opcion = input("ingrese la opcion : ")
    if opcion == "1":
        calcular_promedio(temperaturas[0])
    elif opcion == "2":
        calcular_promedio(temperaturas[1])
    elif opcion == "3":
         calcular_promedio(temperaturas[2])








