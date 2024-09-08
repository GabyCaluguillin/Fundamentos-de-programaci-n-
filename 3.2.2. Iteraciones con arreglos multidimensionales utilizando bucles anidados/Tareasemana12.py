""""Crear una matriz 3D que represente los datos de temperaturas diarias en varias ciudades
Dentro de cada celda de la matriz, puedes almacenar las temperaturas diarias para una ciudad en un día específico de una semana determinada
Utilizar bucles anidados para calcular el promedio de temperaturas para una ciudad por cada una de las semanas.
Mostrar el promedio de temperaturas para cada ciudad y semana en la pantalla."""


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

# Calcular el promedio de temperaturas para cada ciudad y semana
for ciudad in temperaturas:
    for semana in ciudad:
        suma = 0
        for dia in semana:
            suma += dia['temp']
        print("El promedio será ",suma)

while True:
    print("Selecciona una ciudad:")
    print("1. Ciudad 1")
    print("2. Ciudad 2")
    print("3. Ciudad 3")
    print("4. salir")

    opción= input("ingrese la opcion deseada")
    if opcion == "1":
        ciudad = temperaturas[0]
        print(ciudad)
    else:
        print("No se encuentra la opcion ")
    continue