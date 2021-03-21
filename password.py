import hashlib
password = "text"
hashPassword = hashlib.sha256(password.encode()).hexdigest()
print(hashPassword)
