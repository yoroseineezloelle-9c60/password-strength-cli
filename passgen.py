#!/usr/bin/env python3
"""Password strength checker + passphrase generator."""
import secrets, string, math
def strength(pw):
      pool = sum(c in string.ascii_lowercase for c in pw) and 26
      pool += sum(c in string.ascii_uppercase for c in pw) and 26
      pool += sum(c in string.digits for c in pw) and 10
      pool += sum(c in "!@#$%^&*" for c in pw) and 8
      ent = len(pw) * math.log2(max(pool, 1))
      return f"entropy ~{ent:.0f} bits ({'kuat' if ent > 60 else 'lemah'})"
  def gen(words=4):
        wl = ["kucing","laptop","kopi","gunung","kereta","bulan","kertas","angin"]
        sep = secrets.choice(["-","_","."])
        pw = sep.join(secrets.choice(wl) for _ in range(words)) + secrets.choice(string.digits*3)
        return pw
    if __name__ == "__main__":
          pw = input("test password (kosong = generate): ").strip()
          print(strength(pw) if pw else gen())
      
