
from metodos import divide_string  # Importa a la función divide_string.

from metodos import measure_area  # Importa a la función measure_area.


def test_divide_correcto():  # Función que realiza el test del funcionamiento correcto de ambas operaciones
    # de divide_string.
    assert divide_string("12$Prueba_De_Frase34%", 1) == ("$rueba_e_rase%", "12PDF34")  # Assert verifica que divida
    # correctamente minúsculas y no alfanuméricos de mayúsculas y números.
    assert divide_string("12$Prueba_De_Frase34%", 2) == ("12$Prueba_D", "e_Frase34%")  # Assert verifica que divida
    # correctamente a la mitad la frase.


def test_divide_frase_str():  # Función que realiza el test de verificación del primer parámetro como únicamente string.
    assert divide_string(1, 1) == 42  # Assert verifica que al enviar algo que no sea string, la función retorna
    # el error de código 42.


def test_divide_operacion_int():  # Función que realiza el test de verificación del
    # segundo parámetro como únicamente entero.
    assert divide_string("12$Prueba_De_Frase34%", "1") == 56  # Assert verifica que al enviar algo que no sea int,
    # la función retorna el error de código 56.


def test_measure_correcto():  # Función que realiza el test del funcionamiento correcto de ambas operaciones
    # de measure_area.
    assert measure_area(4) == (16, 12.5664)  # Assert que verifica que la función calcula correctamente las áreas.


def test_measure_parametro_int():  # Función que realiza el test de verificación del
    # parámetro como únicamente entero.
    assert measure_area("4") == 33  # Assert verifica que al enviar algo que no sea int,
    # la función retorna el error de código 33.
