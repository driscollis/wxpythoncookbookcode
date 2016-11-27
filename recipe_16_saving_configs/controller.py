# controller.py
import configobj
import os
import sys


appPath = os.path.abspath(os.path.dirname(os.path.join(sys.argv[0])))
inifile = os.path.join(appPath, "example.ini")

def create_config():
    """
    Create the configuration file
    """
    config = configobj.ConfigObj()
    config.filename = inifile
    config['update server'] = "http://www.someCoolWebsite/hackery.php"    
    config['username'] = ""
    config['password'] = ""
    config['update interval'] = 2
    config['agency filter'] = 'include'
    config['filters'] = ""
    config.write()


def get_config():
    """
    Open the config file and return a configobj
    """
    if not os.path.exists(inifile):
        create_config()
    return configobj.ConfigObj(inifile)