import binascii

import pymem.process
from pymem import Pymem
from win32api import GetFileVersionInfo, HIWORD, LOWORD

"""
微信聊天记录导出
"""


class WeiXin(object):

    def __init__(self):
        self.pm = Pymem("WeChat.exe")

        module = self.get_module()
        self.dll_base = module.lpBaseOfDll
        self.size_image = module.SizeOfImage
        self.bits = self.get_pe_bits()

    def get_module(self):
        return pymem.process.module_from_name(self.pm.process_handle, "WeChatWin.dll")

    def get_pe_bits(self):
        address = self.dll_base + self.pm.read_int(self.dll_base + 60) + 4 + 16
        return 64 if self.pm.read_short(address) == 0xF0 else 32

    @property
    def info(self):
        addr, key = None, None
        version = self.version
        if not version:
            return addr, key

        key_bytes = b"-----BEGIN PUBLIC KEY-----\n..."
        public_key_list = pymem.pattern.pattern_scan_all(self.pm.process_handle, key_bytes, return_multiple=True)
        key_addr = self.get_key_addr(public_key_list)
        if not key_addr:
            return

        key_len_offset = 0x8c if self.bits == 32 else 0xd0
        for addr in key_addr:
            key_len = self.pm.read_uint(addr - key_len_offset)
            print(addr, key_len_offset, key_len)
            key = self.pm.read_bytes(self.pm.read_int(addr - 0x90) if self.bits == 32 else
                                     self.pm.read_longlong(addr - 0xd8), key_len)
            key = binascii.b2a_hex(key).decode()
            if len(key) != 64:
                break
        return addr, key

    @property
    def version(self):
        dll_path = None
        for m in list(self.pm.list_modules()):
            if m.filename.endswith("WeChatWin.dll"):
                dll_path = m.filename
                break

        if not dll_path:
            return dll_path

        version = GetFileVersionInfo(dll_path, "\\")
        msv, lsv = version['FileVersionMS'], version['FileVersionLS']
        return f"""{HIWORD(msv)}.{LOWORD(msv)}.{HIWORD(lsv)}.{LOWORD(lsv)}"""

    def get_key_addr(self, public_key_list):
        key_addr = []
        buffer = self.pm.read_bytes(self.dll_base, self.size_image)
        bytes_len = int(self.bits / 8)

        for public_key in public_key_list:
            key_bits = public_key.to_bytes(bytes_len, byteorder="little", signed=True)
            offset = self.search_memory(buffer, key_bits)
            key_addr.extend([x + self.dll_base for x in offset])

        return key_addr

    @staticmethod
    def search_memory(buffer, key_bits):
        offset = []
        index = -1

        while True:
            index = buffer.find(key_bits, index + 1)
            if index == -1:
                break
            offset.append(index)

        return offset

    def get_user(self):
        pass


class DB(object):

    def __init__(self):
        pass

    def get_path(self):
        pass


if __name__ == '__main__':
    wx = WeiXin()
    print(wx.info)







