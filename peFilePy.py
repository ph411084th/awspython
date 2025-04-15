import pefile

path = r"/media/raskolnikov/10829e01-f963-47b9-b8b5-6982fe90ee67/raskolnikov/Documents/extractedFiles/files/file.0x880432682dd0.0x88043b174c80.ImageSectionObject.efslsaext.dll.img"

pe = pefile.PE(path)

print("Timestamp:", pe.FILE_HEADER.TimeDateStamp)
print("EntryPoint:", hex(pe.OPTIONAL_HEADER.AddressOfEntryPoint))
print("ImageBase:", hex(pe.OPTIONAL_HEADER.ImageBase))
print("Sections:")

for section in pe.sections:
    print(f"{section.Name.decode().strip()}: VA = {hex(section.VirtualAddress)}, Size = {hex(section.Misc_VirtualSize)}")
