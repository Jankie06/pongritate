from pathlib import Path
import sys, time
path = str(Path(Path(__file__).parent.absolute()).parent.absolute().parent.absolute())
sys.path.insert(0, path)

import update
time.sleep(5)
import src.main