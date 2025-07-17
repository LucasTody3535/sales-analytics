from unittest import main
from pathlib import Path
import sys

# Allow python to find src directory
sys.path.append(str(Path(__file__).parent.parent))

from test_category import TestCategoryClass

if __name__ == "__main__":
    main()
