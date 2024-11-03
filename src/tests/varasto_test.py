import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_negatiivinen_tilavuus(self):
        self.varasto = Varasto(-10)
        # negatiivinen tilavuus konstruktorissa asettaa tilavuuden nollaksi
        self.assertAlmostEqual(self.varasto.tilavuus, 0)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_negatiivinen_alkusaldo(self):
        self.varasto = Varasto(10, alku_saldo=-5)
        # varaston alkusaldon pitäisi olla nolla
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_ylisuuri_alkusaldo(self):
        self.varasto = Varasto(10, 15)
        # saldon pitäisi olla yhtä suuri kuin tilavuus
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_negatiivinen_lisays(self):
        self.varasto.lisaa_varastoon(5)
        self.varasto.lisaa_varastoon(-4)
        # saldon pitäisi yhä olla 5
        self.assertAlmostEqual(self.varasto.saldo, 5)

    def test_ylisuuri_lisays(self):
        self.varasto.lisaa_varastoon(15)
        # Yritetään laittaa enemmän kuin on tilavuutta:
        # saldo sama kuin tilavuus
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_ottaminen_vahentaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)
        self.varasto.ota_varastosta(3)
        # saldon pitäisi pienentyä viiteen
        self.assertAlmostEqual(self.varasto.saldo, 5)

    def test_ota_negatiivinen_maara(self):
        self.varasto.lisaa_varastoon(5)
        self.varasto.ota_varastosta(-4)
        # saldon pitäisi yhä olla 5
        self.assertAlmostEqual(self.varasto.saldo, 5)

    def test_ota_enemman_kuin_saldo(self):
        self.varasto.lisaa_varastoon(5)
        # Yritetään ottaa enemmän kuin on saldoa, saldo on 0
        self.varasto.ota_varastosta(10)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_str_esitys(self):
        # tyhjän varaston string-esitys
        self.assertEqual(str(self.varasto), "saldo = 0, vielä tilaa 10")
