from carro_deportivo import CarroDeportivo
from camioneta_carga import CamionetaCarga

def main():
    deportivo = CarroDeportivo("BMW Z4", "Negro", "3.0 Turbo", 2, 2, "Gasolina")
    camioneta = CamionetaCarga("Hyundai H100", "Blanca", "2.5 Diesel", 4, 3, "Diesel", 1500)

    print(deportivo.descripcion())
    print(deportivo.aceleracion_frenado())
    print(deportivo.info_extra())

    print()

    print(camioneta.descripcion())
    print(camioneta.climatizacion())
    print(camioneta.info_extra())

main()