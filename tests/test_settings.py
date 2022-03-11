import json
import unittest

from config.settings import AppConfig, DevConfig, ProdConfig, StagingConfig


class SettingsTest(unittest.TestCase):
    LOGGING = "test"

    def setUp(self):
        self._sc = AppConfig

    def tearDown(self):
        pass

    def test_dev(self):
        dev = DevConfig
        self.assertEqual(dev.DB, "dev")
        self.assertEqual(dev.logging, self.LOGGING)

    def test_staging(self):
        dev = StagingConfig
        self.assertEqual(dev.DB, "staging")
        self.assertEqual(dev.logging, self.LOGGING)

    def test_prod(self):
        dev = ProdConfig
        self.assertEqual(dev.DB, "prod")
        self.assertEqual(dev.logging, self.LOGGING)


if __name__ == "__main__":
    unittest.main()
