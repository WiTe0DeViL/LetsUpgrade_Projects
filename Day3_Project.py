import random as r # importing modules
import string as s

# OTP generator
OTP_PIN = list(s.ascii_letters + s.digits)
for i in range(6):
  otp = r.choice(OTP_PIN)
  print(otp, end="")
