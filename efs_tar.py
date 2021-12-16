import sys
import os
Meta = input("Give the Meta: ")
Modem_build = input("Give the Modem_build: ")
assert os.path.exists(Meta), "I did not find the file at, "+str(Meta)
fm = open(Meta,'r+')
#print("Hooray we found your Meta!")

assert os.path.exists(Modem_build), "I did not find the file at, "+str(Modem_build)
fmb = open(Modem_build,'r+')
#print("Hooray we found your Modem_build!")
#stuff you do with the file goes here
#f.close()

exef = 'Meta\common\sectoolsv2\Windows\sectools.exe'
fe = open(exef,'r+')

mb = 'Modem_build\modem_proc\core\storage\misc\efs_zip_tar.gz'
fmb = open(mb,'r+')
mb2 = 'Modem_build\modem_proc\core\securemsm\secboot\security_profile\waipio_modem_security_profile.xml'
fmb2 = open(mb2,'r+')
mb3 = 'Modem_build\modem_proc\core\bsp\efs_image_header\tools\efs_image_create.py'
fmb3 = open(mb3,'r+')
mb4 = 'Modem_build\modem_proc\build\ms\bin\waipio.gen.test\efs_image_meta.bin'
fmb4 = open(mb4,'r+')

o1 = 'C:\temp\efs_zip_tar.gz.elf'
of1 = open(o1,'r+')
o2 = 'C:\temp\efs_zip_tar.gz.mbn'
of2 = open(o2,'r+')
o3 = 'C:\temp\fs_image.tar.gz.mbn.img'
of3 = open(o3,'r+')

os.system("exef elf-tool generate --data mb --outfile o1 --elf-class 32 --align 0x4")
time.sleep(3)

os.system("exef secure-image o1 --outfile o2 --image-id EFS-TAR --security-profile mb2 --sign --signing-mode TEST")
time.sleep(3)

os.system("python mb3 mb4 o2 -o o3")
time.sleep(3)

os.system("fastboot erase modemst1")
time.sleep(3)

os.system("fastboot erase modemst2")
time.sleep(3)

os.system("fastboot flash fsg o3")
time.sleep(3)
