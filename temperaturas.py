
Temperatura = [
    [
        [   # CIUDAD QUITO SEMANA 1
            {"QUITO": "Lunes", "temp": 68},
            {"QUITO": "Martes", "temp": 70},
            {"QUITO": "Miércoles", "temp": 85},
            {"QUITO": "Jueves", "temp": 89},
            {"QUITO": "Viernes", "temp": 89},
            {"QUITO": "Sábado", "temp": 88},
            {"QUITO": "Domingo", "temp": 92}
        ],

        [   # CIUDAD QUITO SEMANA 2
            {"QUITO": "Lunes", "temp": 78},
            {"QUITO": "Martes", "temp": 79},
            {"QUITO": "Miércoles", "temp": 76},
            {"QUITO": "Jueves", "temp": 80},
            {"QUITO": "Viernes", "temp": 87},
            {"QUITO": "Sábado", "temp": 87},
            {"QUITO": "Domingo", "temp": 99}
        ],

        [   # CIUDAD QUITO SEMANA 3
            {"QUITO": "Lunes", "temp": 775},
            {"QUITO": "Martes", "temp": 88},
            {"QUITO": "Miércoles", "temp": 83},
            {"QUITO": "Jueves", "temp": 78},
            {"QUITO": "Viernes", "temp": 98},
            {"QUITO": "Sábado", "temp": 76},
            {"QUITO": "Domingo", "temp": 89}
        ],

        [  # CIUDAD QUITO SEMANA 4
            {"QUITO": "Lunes", "temp":65},
            {"QUITO": "Martes", "temp": 67},
            {"QUITO": "Miércoles", "temp": 90},
            {"QUITO": "Jueves", "temp": 99},
            {"QUITO": "Viernes", "temp": -87},
            {"QUITO": "Sábado", "temp": -65},
            {"QUITO": "Domingo", "temp": 71}
        ]
    ],

    [
        [   # CIUDAD AZUAY SEMANA 1
            {"AZUAY ": "Lunes", "temp": 60},
            {"AZUAY ": "Martes", "temp": 87},
            {"AZUAY ": "Miércoles", "temp": 98},
            {"AZUAY ": "Jueves", "temp": 60},
            {"AZUAY ": "Viernes", "temp": 79},
            {"AZUAY ": "Sábado", "temp": 67},
            {"AZUAY ": "Domingo", "temp": 89}
        ],
        [   #CIUDAD AZUAY SEMANA 2
            {"AZUAY ": "Lunes", "temp": 56},
            {"AZUAY ": "Martes", "temp": 78},
            {"AZUAY ": "Miércoles", "temp": 78},
            {"AZUAY ": "Jueves", "temp": 89},
            {"AZUAY ": "Viernes", "temp": 89},
            {"AZUAY ": "Sábado", "temp": 69},
            {"AZUAY ": "Domingo", "temp": 70}
        ],
        [  #CIUDAD AZUAY SEMANA 3
            {"AZUAY ": "Lunes", "temp": 87},
            {"AZUAY ": "Martes", "temp": 87},
            {"AZUAY ": "Miércoles", "temp": 98},
            {"AZUAY ": "Jueves", "temp": 56},
            {"AZUAY ": "Viernes", "temp": 67},
            {"AZUAY ": "Sábado", "temp": 87},
            {"AZUAY ": "Domingo", "temp":90}
        ],
        [   #CIUDAD AZUAY SEMANA 4
            {"AZUAY ": "Lunes", "temp": 64},
            {"AZUAY ": "Martes", "temp": 68},
            {"AZUAY ": "Miércoles", "temp": 65},
            {"AZUAY ": "Jueves", "temp": 79},
            {"AZUAY ": "Viernes", "temp": 73},
            {"AZUAY ": "Sábado", "temp": 72},
            {"AZUAY ": "Domingo", "temp": 67}
        ]
    ],
        [

            [   #CIUDAD ESMERALADAS SEMANA 1
                {"ESMERALADAS": "Lunes", "temp": 80},
                {"ESMERALADAS": "Martes", "temp": 71},
                {"ESMERALADAS": "Miércoles", "temp": 83},
                {"ESMERALADAS": "Jueves", "temp": 99},
                {"ESMERALADAS": "Viernes", "temp": 77},
                {"ESMERALADAS": "Sábado", "temp": 94},
                {"ESMERALADAS": "Domingo", "temp": 81}
            ],
            [   # #CIUDAD ESMERALADAS SEMANA 2
                {"ESMERALADAS": "Lunes", "temp": 71},
                {"ESMERALADAS": "Martes", "temp": 97},
                {"ESMERALADAS": "Miércoles", "temp": 85},
                {"ESMERALADAS": "Jueves", "temp": 72},
                {"ESMERALADAS": "Viernes", "temp": 84},
                {"ESMERALADAS": "Sábado", "temp": 82},
                {"ESMERALADAS": "Domingo", "temp": 93}
           ],
            [ #CIUDAD ESMERALADAS SEMANA 3
                {"ESMERALADAS": "Lunes", "temp": 87},
                {"ESMERALADAS": "Martes", "temp": 97},
                {"ESMERALADAS": "Miércoles", "temp": 60},
                {"ESMERALADAS": "Jueves", "temp": 80},
                {"ESMERALADAS": "Viernes", "temp": 45},
                {"ESMERALADAS": "Sábado", "temp": 57},
                {"ESMERALADAS": "Domingo", "temp": 78}
            ],
            [ #CIUDAD ESMERALADAS SEMANA 4
                {"ESMERALADAS": "Lunes", "temp": 88},
                {"ESMERALADAS": "Martes", "temp": 89},
                {"ESMERALADAS": "Miércoles", "temp": 85},
                {"ESMERALADAS": "Jueves", "temp": 67},
                {"ESMERALADAS": "Viernes", "temp": 78},
                {"ESMERALADAS": "Sábado", "temp": 85},
                {"ESMERALADAS": "Domingo", "temp": 60},
           ],



    ]

]

# PROMEDIO DE  TEMPERATURAS DE 3 CIUDADES
ciudades = ["QUITO", "AZUAY", "ESMERALDAS"]
for ciudad_idx, ciudad in enumerate(Temperatura):
    for semana_idx, semana in enumerate(ciudad):
        suma_temperaturas = sum([dia["temp"] for dia in semana])
        promedio = suma_temperaturas / len(semana)
        print(f"LA TEMPERATURA PROMEDIO EN : {ciudades[ciudad_idx]}: ,SEMANA Nº {semana_idx + 1}: {promedio:.2f} grados centigrados")