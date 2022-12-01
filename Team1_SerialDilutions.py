from opentrons import protocol_api

metadata = {
    "apiLevel": "2.0",
    "protocolName": "Serial Dilutions",
    "description": "This protocol is the outcome of the iGEM Serial Dilution Standard Protocol",
    "author": "Robin Blackwell et al"
    }

def run(protocol: protocol_api.ProtocolContext):
    #define what goes in each position of opentrons layout. Add custom labware in labware file of .opentrons file location
    tips = protocol.load_labware("opentrons_96_tiprack_300ul", 1)
    reservoir = protocol.load_labware("4ti0131_12_reservoir_21000ul", 2)
    plate = protocol.load_labware("costar3370flatbottomtransparent_96_wellplate_200ul", 3)
    
    #define pipette attachment
    p300 = protocol.load_instrument("p300_multi_gen2", "left", tip_racks=[tips])

    #Instruction
    row = plate.rows()[0]
    p300.transfer(100, reservoir["A1"], row[1:])
    p300.pick_up_tip()
    p300.transfer(100, reservoir["A2"], row[0:2], mix_after=(3,50), touch_tip=True, new_tip='never')
    p300.transfer(100, row[1:10], row[2:11], mix_after=(3,50), touch_tip=True, new_tip="never")
    p300.transfer(100, row[10], reservoir["A3"], new_tip='never')
    p300.drop_tip()