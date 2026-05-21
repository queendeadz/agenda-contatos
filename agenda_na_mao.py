AGENDA = {
    "sarah": {
        "tel": 11970964821,
        "email": "eppluged@gmail.com",
        "endereco": "av das cerejeiras 1040",
    },
    "vovo":  {
        "tel": 11974774475,
        "email": "maria@gmail.com",
        "endereco": "av manoel 303",
    },
    "mamae":  {
        "tel": 11996076433,
        "email": "mamae@gmail.com",
        "endereco": "av das ruas 7",
    },
    "panda":  {
        "tel": 11996122070,
        "email": "panda@gmail.com",
        "endereco": "rua de cima 245",
    }

}

AGENDA.pop("sarah")

for contato in AGENDA:
    print(contato)