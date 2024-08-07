import os
import sys
from zipfile import ZipFile, ZipInfo

class MyZipFile(ZipFile):

    if sys.version_info < (3, 6):
        

        def extract(self, member, path=None, pwd=None):
            if not isinstance(member, ZipInfo):
                member = self.getinfo(member)
            if path is None:
                path = os.getcwd()
            ret_val = self._extract_member(member, path, pwd)
            attr = member.external_attr >> 16
            os.chmod(ret_val, attr)
            return ret_val

    else:

         def _extract_member(self, member, targetpath, pwd):
            if not isinstance(member, ZipInfo):
                member = self.getinfo(member)

            targetpath = super()._extract_member(member, targetpath, pwd)

            attr = member.external_attr >> 16
            if attr != 0:
                os.chmod(targetpath, attr)
            return targetpath


