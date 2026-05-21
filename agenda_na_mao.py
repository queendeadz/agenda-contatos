AGENDA = {
    "sarah": {
        "tel": 11987654321,
        "email": "sarah@gmail.com",
        "endereco": "av das avenidas 1040",
    },
    "vovo":  {
        "tel": 1197777775,
        "email": "maria@gmail.com",
        "endereco": "av lanches 303",
    },
    "mamae":  {
        "tel": 11933333333,
        "email": "mamae@gmail.com",
        "endereco": "av das ruas 7",
    },
    "panda":  {
        "tel": 11945234444,
        "email": "panda@gmail.com",
        "endereco": "rua de cima 245",
    }

}

AGENDA.pop("sarah")

for contato in AGENDA:
    print(contato)