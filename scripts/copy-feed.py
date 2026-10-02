# Keep the old Jekyll feed URL (/feed.xml) working for existing RSS subscribers.
import os
import shutil
from pathlib import Path

out = Path(os.environ.get("QUARTO_PROJECT_OUTPUT_DIR", "_site"))
if (out / "index.xml").exists():
    shutil.copyfile(out / "index.xml", out / "feed.xml")
