from caballo import Caballo
from cocodrillo import Cocodrilo
from PezTropical import PezTropical
from EscarabajoRinoceronte import EscarabajoRinoceronte
from Pato import Pato

def main():
    caballo = Caballo("Relámpago", 5, "pradera", "pasto", "grande", "marrón", 60, "liso", True)
    caballo.galopar()

    croc = Cocodrilo("Fauces", 12, "río", "carnívoro", "grande", "verde", 2000, True, 4.5)
    croc.sumergirse()

    pez = PezTropical("Coralito", 1, "arrecife", "plancton", "pequeño", "azul", 35, "redonda", True)
    pez.nadar()

    esc = EscarabajoRinoceronte("Titan", 2, "selva", "savia", "pequeño", "negro", 850, "duro", 3)
    esc.excavar()

    pato = Pato("Plumitas", 3, "lago", "omnivoro", "mediano", "verde",0.75, True, "hidrofóbico")
    pato.nadar()


if __name__ == "__main__":
    main()