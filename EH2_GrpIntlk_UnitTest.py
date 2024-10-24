import unittest
from pycomm3 import LogixDriver
import time

# Constants
commpath = '10.10.17.12/1'
AOI_Name = 'TestGrp_Intlk'
AOI_Type = 'EH2_GrpIntlk'
UDT_Type = 'P_Intlk_UDT'
UDT_Name = 'TestGrp_IntlkArr'
Test_PLC_Name = 'EH2_GrpIntlk'
P_Intlk_Name = 'Test_Intlk'
WAIT_DELAY = 0.05

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

    if write_status[3] == None: # we have a good write
        '''
        while True:
            time.sleep(WAIT_DELAY)
            read_status = plc.read(tag)

            # check data matches
            if read_status[1] == write_status[1]:
        '''        
        return True
        
    else:
        return False


def read_tag(plc,tag):

    #print('Reading ' + tag)
    read_status = plc.read(tag)

    return read_status[1]
        
def run_test():

    prev_count = read_tag(plc,'Test_Counter')
    write_and_check_tag(plc,'Test_Start',1)
    while True:
        time.sleep(WAIT_DELAY)
        current_count = read_tag(plc,'Test_Counter')  

        if current_count != prev_count:
            return

def reset_test():

    write_and_check_tag(plc,'Test_Reset',1) 
    while True:
        time.sleep(WAIT_DELAY)
        test_ready = read_tag(plc,'Test_Ready')

        if test_ready:
            return

def wait_for_ready():
    
    while True:
        time.sleep(WAIT_DELAY)
        done = read_tag(plc,'Test_Ready')

        if done:
            return

def reset_interlocks():
         # reset group interlock

        write_and_check_tag(plc, AOI_Name + '.Inp_BypActive',0)
        write_and_check_tag(plc, AOI_Name + '.Cfg_OKState',0b0000_0000_0000_0000)
        write_and_check_tag(plc, AOI_Name + '.Cfg_Latched',0b0000_0000_0000_0000)
        write_and_check_tag(plc, AOI_Name + '.Cfg_Bypassable',0b0000_0000_0000_0000)

        write_and_check_tag(plc,UDT_Name + '[0].Inp_Intlk',0b0000_0000_0000_0000)
        write_and_check_tag(plc,UDT_Name + '[0].Cfg_OKState',0b0000_0000_0000_0000)
        write_and_check_tag(plc,UDT_Name + '[0].Cfg_Latched',0b0000_0000_0000_0000)
        write_and_check_tag(plc,UDT_Name + '[0].Cfg_Bypassable',0b0000_0000_0000_0000)

        write_and_check_tag(plc,UDT_Name + '[1].Inp_Intlk',0b0000_0000_0000_0000)
        write_and_check_tag(plc,UDT_Name + '[1].Cfg_OKState',0b0000_0000_0000_0000)
        write_and_check_tag(plc,UDT_Name + '[1].Cfg_Latched',0b0000_0000_0000_0000)
        write_and_check_tag(plc,UDT_Name + '[1].Cfg_Bypassable',0b0000_0000_0000_0000)

        write_and_check_tag(plc,UDT_Name + '[2].Inp_Intlk',0b0000_0000_0000_0000)
        write_and_check_tag(plc,UDT_Name + '[2].Cfg_OKState',0b0000_0000_0000_0000)
        write_and_check_tag(plc,UDT_Name + '[2].Cfg_Latched',0b0000_0000_0000_0000)
        write_and_check_tag(plc,UDT_Name + '[2].Cfg_Bypassable',0b0000_0000_0000_0000)

        write_and_check_tag(plc,UDT_Name + '[3].Inp_Intlk',0b0000_0000_0000_0000)
        write_and_check_tag(plc,UDT_Name + '[3].Cfg_OKState',0b0000_0000_0000_0000)
        write_and_check_tag(plc,UDT_Name + '[3].Cfg_Latched',0b0000_0000_0000_0000)
        write_and_check_tag(plc,UDT_Name + '[3].Cfg_Bypassable',0b0000_0000_0000_0000)

        write_and_check_tag(plc,UDT_Name + '[4].Inp_Intlk',0b0000_0000_0000_0000)
        write_and_check_tag(plc,UDT_Name + '[4].Cfg_OKState',0b0000_0000_0000_0000)
        write_and_check_tag(plc,UDT_Name + '[4].Cfg_Latched',0b0000_0000_0000_0000)
        write_and_check_tag(plc,UDT_Name + '[4].Cfg_Bypassable',0b0000_0000_0000_0000)

        write_and_check_tag(plc,UDT_Name + '[5].Inp_Intlk',0b0000_0000_0000_0000)
        write_and_check_tag(plc,UDT_Name + '[5].Cfg_OKState',0b0000_0000_0000_0000)
        write_and_check_tag(plc,UDT_Name + '[5].Cfg_Latched',0b0000_0000_0000_0000)
        write_and_check_tag(plc,UDT_Name + '[5].Cfg_Bypassable',0b0000_0000_0000_0000)

        write_and_check_tag(plc,UDT_Name + '[6].Inp_Intlk',0b0000_0000_0000_0000)
        write_and_check_tag(plc,UDT_Name + '[6].Cfg_OKState',0b0000_0000_0000_0000)
        write_and_check_tag(plc,UDT_Name + '[6].Cfg_Latched',0b0000_0000_0000_0000)
        write_and_check_tag(plc,UDT_Name + '[6].Cfg_Bypassable',0b0000_0000_0000_0000)

        write_and_check_tag(plc,UDT_Name + '[7].Inp_Intlk',0b0000_0000_0000_0000)
        write_and_check_tag(plc,UDT_Name + '[7].Cfg_OKState',0b0000_0000_0000_0000)
        write_and_check_tag(plc,UDT_Name + '[7].Cfg_Latched',0b0000_0000_0000_0000)
        write_and_check_tag(plc,UDT_Name + '[7].Cfg_Bypassable',0b0000_0000_0000_0000)

        write_and_check_tag(plc,UDT_Name + '[8].Inp_Intlk',0b0000_0000_0000_0000)
        write_and_check_tag(plc,UDT_Name + '[8].Cfg_OKState',0b0000_0000_0000_0000)
        write_and_check_tag(plc,UDT_Name + '[8].Cfg_Latched',0b0000_0000_0000_0000)
        write_and_check_tag(plc,UDT_Name + '[8].Cfg_Bypassable',0b0000_0000_0000_0000)

        write_and_check_tag(plc,UDT_Name + '[9].Inp_Intlk',0b0000_0000_0000_0000)
        write_and_check_tag(plc,UDT_Name + '[9].Cfg_OKState',0b0000_0000_0000_0000)
        write_and_check_tag(plc,UDT_Name + '[9].Cfg_Latched',0b0000_0000_0000_0000)
        write_and_check_tag(plc,UDT_Name + '[9].Cfg_Bypassable',0b0000_0000_0000_0000)

        write_and_check_tag(plc,UDT_Name + '[10].Inp_Intlk',0b0000_0000_0000_0000)
        write_and_check_tag(plc,UDT_Name + '[10].Cfg_OKState',0b0000_0000_0000_0000)
        write_and_check_tag(plc,UDT_Name + '[10].Cfg_Latched',0b0000_0000_0000_0000)
        write_and_check_tag(plc,UDT_Name + '[10].Cfg_Bypassable',0b0000_0000_0000_0000)

        write_and_check_tag(plc,UDT_Name + '[11].Inp_Intlk',0b0000_0000_0000_0000)
        write_and_check_tag(plc,UDT_Name + '[11].Cfg_OKState',0b0000_0000_0000_0000)
        write_and_check_tag(plc,UDT_Name + '[11].Cfg_Latched',0b0000_0000_0000_0000)
        write_and_check_tag(plc,UDT_Name + '[11].Cfg_Bypassable',0b0000_0000_0000_0000)

        write_and_check_tag(plc,UDT_Name + '[12].Inp_Intlk',0b0000_0000_0000_0000)
        write_and_check_tag(plc,UDT_Name + '[12].Cfg_OKState',0b0000_0000_0000_0000)
        write_and_check_tag(plc,UDT_Name + '[12].Cfg_Latched',0b0000_0000_0000_0000)
        write_and_check_tag(plc,UDT_Name + '[12].Cfg_Bypassable',0b0000_0000_0000_0000)

        write_and_check_tag(plc,UDT_Name + '[13].Inp_Intlk',0b0000_0000_0000_0000)
        write_and_check_tag(plc,UDT_Name + '[13].Cfg_OKState',0b0000_0000_0000_0000)
        write_and_check_tag(plc,UDT_Name + '[13].Cfg_Latched',0b0000_0000_0000_0000)
        write_and_check_tag(plc,UDT_Name + '[13].Cfg_Bypassable',0b0000_0000_0000_0000)

        write_and_check_tag(plc,UDT_Name + '[14].Inp_Intlk',0b0000_0000_0000_0000)
        write_and_check_tag(plc,UDT_Name + '[14].Cfg_OKState',0b0000_0000_0000_0000)
        write_and_check_tag(plc,UDT_Name + '[14].Cfg_Latched',0b0000_0000_0000_0000)
        write_and_check_tag(plc,UDT_Name + '[14].Cfg_Bypassable',0b0000_0000_0000_0000)

        write_and_check_tag(plc,UDT_Name + '[15].Inp_Intlk',0b0000_0000_0000_0000)
        write_and_check_tag(plc,UDT_Name + '[15].Cfg_OKState',0b0000_0000_0000_0000)
        write_and_check_tag(plc,UDT_Name + '[15].Cfg_Latched',0b0000_0000_0000_0000)
        write_and_check_tag(plc,UDT_Name + '[15].Cfg_Bypassable',0b0000_0000_0000_0000)

        # reset Interlock

        write_and_check_tag(plc, P_Intlk_Name + '.Inp_Intlk00',0)
        write_and_check_tag(plc, P_Intlk_Name + '.Inp_Intlk01',0)
        write_and_check_tag(plc, P_Intlk_Name + '.Inp_Intlk02',0)
        write_and_check_tag(plc, P_Intlk_Name + '.Inp_Intlk03',0)
        write_and_check_tag(plc, P_Intlk_Name + '.Inp_Intlk04',0)
        write_and_check_tag(plc, P_Intlk_Name + '.Inp_Intlk05',0)
        write_and_check_tag(plc, P_Intlk_Name + '.Inp_Intlk06',0)
        write_and_check_tag(plc, P_Intlk_Name + '.Inp_Intlk07',0)
        write_and_check_tag(plc, P_Intlk_Name + '.Inp_Intlk08',0)
        write_and_check_tag(plc, P_Intlk_Name + '.Inp_Intlk09',0)
        write_and_check_tag(plc, P_Intlk_Name + '.Inp_Intlk10',0)
        write_and_check_tag(plc, P_Intlk_Name + '.Inp_Intlk11',0)
        write_and_check_tag(plc, P_Intlk_Name + '.Inp_Intlk12',0)
        write_and_check_tag(plc, P_Intlk_Name + '.Inp_Intlk13',0)
        write_and_check_tag(plc, P_Intlk_Name + '.Inp_Intlk14',0)
        write_and_check_tag(plc, P_Intlk_Name + '.Inp_Intlk15',0)
        
        write_and_check_tag(plc, P_Intlk_Name + '.Inp_BypActive',0)
        write_and_check_tag(plc, P_Intlk_Name + '.Cfg_OKState',0b0000_0000_0000_0000)
        write_and_check_tag(plc, P_Intlk_Name + '.Cfg_Latched',0b0000_0000_0000_0000)
        write_and_check_tag(plc, P_Intlk_Name + '.Cfg_Bypassable',0b0000_0000_0000_0000)   

class TestAOI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):

        connect_to_plc()

        write_and_check_tag(plc,'Test_Bypass',0)

    @classmethod
    def tearDownclass(cls):

        write_and_check_tag(plc,'Test_Start',0)
        write_and_check_tag(plc,'StepWord',1)

        write_and_check_tag(plc,'Test_Bypass',1)

        wait_for_ready()

        disconnect_from_plc()

    def setUp(self):

        write_and_check_tag(plc,'Test_Start',0)
        write_and_check_tag(plc,'StepWord',1)

        wait_for_ready()

        return super().setUp()
    
    def tearDown(self):

        return super().tearDown()

    #@unittest.skipUnless(plc.connected,"PLC not connected")
    def test_0_check_tags_exist(self):

        aoi_tags = [
            tag
            for tag, _def in plc.tags.items()
            if _def['data_type_name'] == AOI_Type
        ]

        self.assertTrue(AOI_Name in aoi_tags,'AOI is in tag list')


    # check the right file is on the plc, make this first test
    #@unittest.skipUnless(plc.connected, "PLC not connected")
    def test_1_check_plc_file_loaded(self):
        self.assertEqual(plc.get_plc_name(),Test_PLC_Name,'Check correct file is loaded on bench PLC')
    
    def test_2_check_inputs_non_bypassable_non_latch(self):

        for i in range(16):
            groupnum = i+1

            print('Checking group ' + str(groupnum))

            for j in range(15):
                intlk_mask = 2**i

                child_trip = 2**j

                print('Checking Input ' + str(j))

                # write to first interlock in child interlock group
                intlkgrp_tagwrite = UDT_Name + '[' + str(i) + '].Inp_Intlk'
                write_and_check_tag(plc,intlkgrp_tagwrite,child_trip)

                # write to interlock in P_Intlk
                if i < 10:
                    intlk_tagwrite = P_Intlk_Name + '.Inp_Intlk0' + str(i)
                else:
                    intlk_tagwrite = P_Intlk_Name + '.Inp_Intlk' + str(i)
                write_and_check_tag(plc,intlk_tagwrite,1)

                #start the test
                run_test()

                # tests for group interlock AOI
                self.assertFalse(read_tag(plc,AOI_Name + '_SnapShot.Sts_IntlkOK'),'Bypassable Interlocks OK')
                self.assertFalse(read_tag(plc,AOI_Name + '_SnapShot.Sts_NBIntlkOK'),'Non Bypassable Interlocks OK')
                self.assertEqual(bin(abs(int(read_tag(plc,AOI_Name + '_SnapShot.Sts_Intlk')))),bin(int(intlk_mask)),'Interlock Status')
                self.assertEqual(bin(abs(int(read_tag(plc,AOI_Name + '_SnapShot.Sts_FirstOut')))),bin(int(intlk_mask)),'First Out Status')
                self.assertEqual(read_tag(plc,AOI_Name + '_SnapShot.Val_FirstOutTxt'),str((j+1)+16*i),'First Out Text Status')

                # tests to compare group interlock with P_Intlk
                self.assertEqual(read_tag(plc,AOI_Name + '_SnapShot.Sts_Intlk'),read_tag(plc,P_Intlk_Name + '_SnapShot.Sts_Intlk'),'Interlock Status Matches for Group ' + str(groupnum))
                self.assertEqual(read_tag(plc,AOI_Name + '_SnapShot.Sts_IntlkOK'),read_tag(plc,P_Intlk_Name + '_SnapShot.Sts_IntlkOK'),'Interlock OK Status Matches for Group ' + str(groupnum))
                self.assertEqual(read_tag(plc,AOI_Name + '_SnapShot.Sts_NBIntlkOK'),read_tag(plc,P_Intlk_Name + '_SnapShot.Sts_NBIntlkOK'),'Non Bypassable Interlock Status Matches for Group ' + str(groupnum))

                reset_test()
    '''
    def test_1_check_inputs_bypassable_non_latch(self):

        for i in range(16):
            groupnum = i+1

            print('Checking group ' + str(groupnum))

            for j in range(15):
                # EH2_GrpInltk Setup

                intlk_mask = 2**i
                child_mask = 2**j

                # set bypasses
                write_and_check_tag(plc,AOI_Name + '.Inp_BypActive',1)
                write_and_check_tag(plc,AOI_Name + '.Cfg_Bypassable',intlk_mask)
                write_and_check_tag(plc,AOI_Name + '.MSet_Bypass',intlk_mask)

                print('Checking Input ' + str(j))


                tagwrite_child_base = UDT_Name + '[' + str(i) + ']'

                # write to first interlock in child interlock group
                write_and_check_tag(plc,tagwrite_child_base + '.Inp_Intlk',child_mask)

                # P_Intlk Setup

                # set bypasses
                write_and_check_tag(plc,P_Intlk_Name + '.Inp_BypActive',1)
                write_and_check_tag(plc,P_Intlk_Name + '.Cfg_Bypassable',intlk_mask)
                write_and_check_tag(plc,P_Intlk_Name + '.MSet_Bypass',intlk_mask)

                # write to interlock in P_Intlk
                if i < 10:
                    intlk_tagwrite = P_Intlk_Name + '.Inp_Intlk0' + str(i)
                else:
                    intlk_tagwrite = P_Intlk_Name + '.Inp_Intlk' + str(i)
                write_and_check_tag(plc,intlk_tagwrite,1)

                #start the test
                run_test()

                # tests for group interlock AOI
                self.assertTrue(read_tag(plc,AOI_Name + '_SnapShot.Sts_BypActive'),'Bypass Enabled')
                self.assertFalse(read_tag(plc,AOI_Name + '_SnapShot.Sts_IntlkOK'),'Bypassable Interlocks OK')
                self.assertTrue(read_tag(plc,AOI_Name + '_SnapShot.Sts_NBIntlkOK'),'Non Bypassable Interlocks OK')
                self.assertEqual(bin(abs(int(read_tag(plc,AOI_Name + '_SnapShot.Sts_Intlk')))),bin(int(intlk_mask)),'Interlock Status')
                self.assertEqual(bin(abs(int(read_tag(plc,AOI_Name + '_SnapShot.Sts_FirstOut')))),bin(int(intlk_mask)),'First Out Status')
                #self.assertEqual(read_tag(plc,AOI_Name + '_SnapShot.Val_FirstOutTxt'),str((j+1)+16*i),'First Out Text Status')

                # tests to compare group interlock with P_Intlk
                self.assertEqual(read_tag(plc,AOI_Name + '_SnapShot.Sts_Intlk'),read_tag(plc,P_Intlk_Name + '_SnapShot.Sts_Intlk'),'Interlock Status Matches for Group ' + str(groupnum))
                self.assertEqual(read_tag(plc,AOI_Name + '_SnapShot.Sts_IntlkOK'),read_tag(plc,P_Intlk_Name + '_SnapShot.Sts_IntlkOK'),'Interlock OK Status Matches for Group ' + str(groupnum))
                self.assertEqual(read_tag(plc,AOI_Name + '_SnapShot.Sts_NBIntlkOK'),read_tag(plc,P_Intlk_Name + '_SnapShot.Sts_NBIntlkOK'),'Non Bypassable Interlock Status Matches for Group ' + str(groupnum))

                reset_test()
    '''


if __name__ == '__main__':
    unittest.main()
