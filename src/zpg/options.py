
import os
from optparse import OptionParser
import textwrap
import inspect
import zpg

class ZpgOptionParser(OptionParser):
    description = textwrap.dedent("""\
        This Program builds zenpacks from templates.
        """)

    def __init__(self):
        OptionParser.__init__(self,description=self.description)
        destdir = "/".join(inspect.getfile(zpg).split('/')[:-1]) + "/build"
        self.add_option('-d', "--destdir", dest="dest", default=destdir, help="Destination Directory for the zenpack. [%default]")
        self.add_option('-v', "--version", dest="version", default="4", help="Zenpack type to build [%default]")
        self.add_option('-s', "--skip", action='store_true', dest="skip", default=False, help="Do Not use cached Templates.")
        self.add_option('-j', "--json", dest="json", default=None, help="json input")