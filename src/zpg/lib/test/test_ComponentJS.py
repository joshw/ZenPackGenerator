#!/usr/bin/env python
import unittest
import os
from mock import mock_open, patch, call, MagicMock
from zpg.lib.Template import Template
import inspect
import zpg


class SimpleSetup(unittest.TestCase):
    def setUp(self):
        from zpg.lib.ZenPack import ZenPack
        self.zp = ZenPack('a.a.Template')

    def tearDown(self):
        del(self.zp)


class WriteTemplatesBase(unittest.TestCase):
    def setUp(self):
        from zpg.lib.ZenPack import ZenPack
        self.zp = ZenPack('a.b.c')
        self.makedirs = os.makedirs

        os.makedirs = MagicMock(return_value=True)

    def write(self, obj, template):
        m = mock_open()
        with patch('__builtin__.open', mock_open(read_data=template), create=True) as m:
            obj.dest_file = 'dummy_dest_file.py'
            obj.tfile = 'dummy_tfile'
            obj.source_template = 'dummy_source_template.tmpl'
            obj.write()

            # Write File Handle
            wfh = m.return_value.__enter__.return_value
            self.results = wfh.write.call_args_list

    def tearDown(self):
        print "Calling teardown"
        os.makedirs = self.makedirs
        del(self.zp)

class TestWriteTemplate(WriteTemplatesBase):
    #@unittest.skip("Skipping")
    def test_processTemplate(self):
        dc = self.zp.addDeviceClass('Devices/Example')
        dc.addComponentType('Component')
        for cjs in self.zp.componentJSs.values():
            self.write(cjs, '${zenpack.id}\n${zenpack.version}\n')
            self.assertEqual(self.results[-1], call(u'a.b.c\n0.0.1\n'))


if __name__ == '__main__':
    unittest.main()
