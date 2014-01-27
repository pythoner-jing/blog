import sys, os

ROOT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(ROOT_PATH)

print ROOT_PATH
import markdown
import pygments.highlight
