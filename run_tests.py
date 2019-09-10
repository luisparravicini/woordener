import unittest
from pathlib import Path


loader = unittest.TestLoader()
start_dir = Path(__file__).parent.joinpath('tests')
suite = loader.discover(start_dir)

runner = unittest.TextTestRunner()
runner.run(suite)
