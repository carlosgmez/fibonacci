import unittest
from fib import fib

"""
Clase de pruebas para comprobar el script
"""
class Test(unittest.TestCase):
    def test_result(self):
        """
        Comprueba que el quinto número de la sucesión es igual a 3.
        """
        seq = fib(5)
        self.assertEqual(seq[4],3)

"""
Python tiene una variable llamada __name__ que registra el nombre del módulo
o script que se está ejecutando en ese momento.

unittest.main() proporciona una interfaz de línea de comandos para el script de prueba.
"""
if __name__ == '__main__':
    unittest.main()