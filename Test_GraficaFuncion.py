import unittest
import main
import math

class TestGraficaFuncion(unittest.TestCase):

    def test_f(varClase):

        #Datos de prueba
        x = (5, 5, math.pi/2, math.pi/2, math.pi, 1)
        y = (25, 125, 1, 0, 0, 0)

        for tipo in range(0, len(x)):
            f = main.f(x[tipo], tipo)
            print(f, y[tipo])
            varClase.assertTrue(math.isclose(f, y[tipo], abs_tol=1e-15))
            #varClase.assertEqual(f, y[tipo])

unittest.main()