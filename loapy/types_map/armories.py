from types.armories import *

"""
@breif API Json 수신 시 Armories type 리턴
"""
class ArmoriesMap:
    def __init__(self):
        self._armoryEquipment = ArmoryEquipment()
        self._armoryEquipmentDetails = ArmoryEquipmentDetails()