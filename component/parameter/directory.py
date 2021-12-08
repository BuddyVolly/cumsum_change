from pathlib import Path

# this directory is the root directory of all sepal dashboard app.
# please make sure that any result that you produce is embeded inside this folder
# create a folder adapted to your need inside this folder to save anything in sepal
module_dir = Path("~", "module_results").expanduser()
module_dir.mkdir(exist_ok=True)

result_dir = module_dir / "cumsum"
result_dir.mkdir(exist_ok=True)

# downloads directory where all SEPAL time series live
down_dir = Path("~", "downloads").expanduser()
down_dir.mkdir(exist_ok=True)
