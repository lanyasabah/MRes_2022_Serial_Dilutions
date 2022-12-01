from opentrons import protocol_api

metadata = {
    'apiLevel': '2.13',
    'protocolName': 'Serial Dilution Tutorial',
    'description': '''This protocol is the outcome of following the
                   Python Protocol API Tutorial located at
                   https://docs.opentrons.com/v2/tutorial.html. It takes a
                   solution and progressively dilutes it by transferring it
                   stepwise across a plate.''',
    'author': 'New API User'
    }


def run(protocol: protocol_api.ProtocolContext):
    # Define labware
    tips = protocol.load_labware('opentrons_96_tiprack_300ul', 1)
    reservoir = protocol.load_labware('4ti0131_12_reservoir_21000ul', 2)
    plate = protocol.load_labware('costar3370flatbottomtransparent_96_wellplate_200ul', 3)
    p300 = protocol.load_instrument('p300_multi_gen2', 'left', tip_racks=[tips])
    
    p300.transfer(100, reservoir['A1'], plate.rows()[0][1:])
    row = plate.rows()[0]
    p300.pick_up_tip()
    p300.transfer(200, reservoir['A2'], plate.rows()[0][0], new_tip="never")
    p300.transfer(100, row[:10], row[1:-1], mix_after=(3, 50),new_tip="never")
   
    p300.aspirate(100, row[-2])
    p300.drop_tip()