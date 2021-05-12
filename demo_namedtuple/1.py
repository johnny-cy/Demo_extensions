from collections import namedtuple
from enum import Enum, auto

Service = namedtuple('ServiceClass', ['base_url', 'login_api', 'add_api', 'upload_api', 'aes_key', 'aes_iv'])



class CloudService(Enum):
    notifier = Service('https://1.1.1.1:1111', '/user/login', 'patient/add', 'patient/dicom_set/upload', 'aes_key', 'aes_iv')
    # def lolgin(self):
    #     print(self)
    #     # print(self.value.base_url)
        
    RED = auto() # auto  會自動依照上到下的順序給予1,2,3,...的int
    BLUE = auto()
    GREEN = auto()
# print(dir(CloudService.notifier))
# print("CloudService.notifier.__class__", CloudService.notifier.__class__)
# print("CloudService.notifier.name", CloudService.notifier.name)
# print("CloudService.notifier.value", CloudService.notifier.value)


# print(CloudService.RED.name)
# print(type(CloudService.notifier.value))

import tempfile

with tempfile.TemporaryDirectory() as temp_dir:
    # print(temp_dir)
    pass

print(CloudService.RED.value)
print(CloudService.GREEN.value)
print(CloudService.BLUE.value)

import pathlib
import os
# print(pathlib.Path(os.path.abspath(__file__)).parents[1])
print(pathlib.Path(os.path.abspath(__file__)).parents[0])
print(pathlib.Path(os.path.abspath(__file__)))
# print(pathlib.Path(os.path.abspath(__file__)))