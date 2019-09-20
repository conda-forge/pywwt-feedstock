import logging
import sys

from jupyterlab.commands import get_app_info
from notebook.nbextensions import validate_nbextension
from notebook.serverextensions import validate_serverextension

# If there's a problem and we don't provide this, the validate function crashes :-(
logger = logging.getLogger('')

if validate_nbextension('pywwt/extension', logger=logger) != []:
    print("Issue detected with nbextension")
    sys.exit(1)
print("nbextension OK")

info = get_app_info()

if 'pywwt' not in info['extensions'] or 'pywwt' in info['disabled']:
    print("Issue detected with labextension")
    sys.exit(1)
print("labextension OK")

if validate_serverextension('pywwt', logger=logger) != []:
    print("Issue detected with serverextension")
    sys.exit(1)
print("serverextension OK")
