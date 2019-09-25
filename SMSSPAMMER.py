import os,time,sys,shutil

class Main:

	def __init__(self):
		self.detekos()

	def menu(self):
		print("""
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

                    S P A M  S M S 
		 ---------------------
		 Author : STEAVE(T.M)
                Contact: UNDERCODETESTING@HOTMAIL.COM 
                TELEGRAM: T.me/UndercodeTestingOfficial
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

1. Spam TRI                      2. Spam Grab
                            
3. Spam HooqTV                   4. Spam OYOROOMS
                            
5. Spam TelkomNyet               6. Spam Sms Gratis
                                
""")
		pilih=int(input('/INICIADO: '))
		if pilih == 1:
			import spam.smsspam
		elif pilih == 2:
			import spam.gra
		elif pilih == 3:
			import spam.hooqs
		elif pilih == 4:
			import spam.oyospam
		elif pilih == 5:
			print("""
		;;;;;;;;;;;;;;;;;;;
		; Spam TelkomNyet ;
		;;;;;;;;;;;;;;;;;;;

1. Spam TelkomNyet-v1
2. Spam TelkomNyet-v2
""")
			pilihlagi=int(input('/UndercodeTesting: '))
			if pilihlagi == 1:
				import spam.teln
			elif pilihlagi == 2:
				import spam.tel2
			else: print("[!] lihat menu dong(o)");self.menu()
		elif pilih == 6:
			import spam.grat
		else: print("[!] lihat menu dong(o)");self.menu()

	def detekos(self):
		#remove cache
		try:
			shutil.rmtree("src/__pycache__")
		except: pass

		if os.name in ['nt','win32']:
			os.system('cls')
		else: os.system('clear')
		self.menu()

try:
	Main()
except KeyboardInterrupt:
	exit('[Exit] Key interrupt')
except Exception as F:
	print('Err: %s'%(F))
