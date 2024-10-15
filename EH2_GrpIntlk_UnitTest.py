import unittest
from pycomm3 import LogixDriver

# Constants
commpath = '10.10.17.12/1'
AOI_Name = 'TestGrp_Intlk'
AOI_Type = 'EH2_GrpIntlk'
UDT_Name = 'P_Intlk_UDT'
Test_PLC_Name = 'EH2_GrpIntlk'

plc = LogixDriver(commpath, init_tags=True,init_program_tags=True)

def connect_to_plc():
    print('Connecting to PLC.')
    try:
        plc.open()
        plc_name = plc.get_plc_name()

        print('Connected to ' + plc_name + ' PLC at ' + commpath)
    except:
        print('Unable to connect to PLC at ' + commpath)
        exit()

def disconnect_from_plc():
    plc.close()

def write_and_check_tag(plc,tag,value):
    '''
    Funciton writes to a PLC tag, waits for the value to be written by reading back tag
    '''
    write_status = plc.write(tag,value)

    read_status = plc.read(tag)

    if write_status == read_status:
        return True
    else
        return False

class TestAOI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):

        connect_to_plc()
    
    @classmethod
    def tearDownclass(cls):

        disconnect_from_plc()

    def setUp(self):

        aoi_tags = [(AOI_Name+'.Inp_BypActive',0),
                    (AOI_Name+'.Cfg_OKState',0),
                    (AOI_Name+'.Cfg_Latched',0),
                    (AOI_Name+'.Cfg_Bypassable',0)]

        plc.write(*aoi_tags)

        return super().setUp()

    # check the right file is on the plc, make this first test
    #@unittest.skipUnless(plc.connected, "PLC not connected")
    def test_1_check_plc_file_loaded(self):
        self.assertEqual(plc.get_plc_name(),Test_PLC_Name,'Check correct file is loaded on bench PLC')

    #@unittest.skipUnless(plc.connected,"PLC not connected")
    def test_0_check_tags_exist(self):

        aoi_tags = [
            tag
            for tag, _def in plc.tags.items()
            if _def['data_type_name'] == AOI_Type
        ]

        self.assertTrue(AOI_Name in aoi_tags,'AOI is in tag list')

if __name__ == '__main__':
    unittest.main()
