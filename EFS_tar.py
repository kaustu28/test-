import time
import os

Meta = input("Give the Meta: ")
Modem_build = input("Give the Modem_build: ")
assert os.path.exists(Meta), "I did not find the file at, "+str(Meta)
fm = open(Meta,'r+')
assert os.path.exists(Modem_build), "I did not find the file at, "+str(Modem_build)
fmb = open(Modem_build,'r+')


def generate_image_file():
	sectools_file = Meta+'\\common\\sectoolsv2\\Windows\\sectools.exe'
	gz_file = Modem_build+'\\modem_proc\\core\\storage\\misc\\efs_zip_tar.gz'
	xml_file = Modem_build+'\\modem_proc\\core\\securemsm\\secboot\\security_profile\\waipio_modem_security_profile.xml'
	python_file = Modem_build+'\\modem_proc\\core\\bsp\\efs_image_header\\tools\\efs_image_create.py'
	bin_file = Modem_build+'\\modem_proc\\build\\ms\\bin\\waipio.gen.test\\efs_image_meta.bin'

	elf_file = 'C:\\temp\\efs_zip_tar.gz.elf'
	mbn_file = 'C:\\temp\\efs_zip_tar.gz.mbn'
	image_file = 'C:\\temp\\fs_image.tar.gz.mbn.img'

	os.system(sectools_file + "elf-tool generate --data" +  gz_file + "--outfile"  + elf_file + "--elf-class 32 --align 0x4")
	time.sleep(3)
	os.system(sectools_file + "secure-image" + elf_file + "--outfile" + mbn_file + "--image-id EFS-TAR --security-profile" + xml_file + "--sign --signing-mode TEST")
	time.sleep(3)
	os.system("python" + python_file + bin_file + mbn_file + "-o" + image_file)
	time.sleep(3)

def fastboot_to_adb():
	out = os.popen('fastboot devices').read()
    split_list_out = out.split('\n')
    print(split_list_out)
    print(split_list_out[1])
    if "device" in split_list_out[1] :
        print('Device is in fastboot_mode')
        os.system('fastboot reboot')
        time.sleep(10)	

def erase_modemst():
	os.system("fastboot erase modemst1")
	time.sleep(3)
	os.system("fastboot erase modemst2")
	time.sleep(3)

def flash_efs_tar_image():
	os.system("fastboot flash fsg" + image_file)
	time.sleep(3)

if __name__ == '__main__':
    generate_image_file()
    erase_modemst()
    flash_efs_tar_image()
    fastboot_to_adb()
    # check files in efs file explorer	
