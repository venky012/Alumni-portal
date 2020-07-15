from . import settings
from linkedin_api import Linkedin

try:
    api = Linkedin('poojariv53@gmail.com', 'marvm123')
except:
    print("Unable to handle linkedin api check for network connections...")
    api = ''