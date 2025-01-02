import hashlib
import os
from hashlib import pbkdf2_hmac

# 사용자로부터 입력받기
string = input("문자: ")

# 소금을 추가하여 보안 강화
salt = os.urandom(16)

# 여러 해시 함수로 순차적으로 해싱하고, PBKDF2 적용
encoded_string = string.encode()

# 해시 적용
one = hashlib.sha1(encoded_string).hexdigest()
encoded_string = one.encode()
two = hashlib.sha224(encoded_string).hexdigest()
encoded_string = two.encode()
three = hashlib.sha256(encoded_string).hexdigest()
encoded_string = three.encode()
four = hashlib.sha384(encoded_string).hexdigest()
encoded_string = four.encode()
five = hashlib.sha512(encoded_string).hexdigest()
encoded_string = five.encode()
six = hashlib.sha3_512(encoded_string).hexdigest()
encoded_string = six.encode()

# PBKDF2 적용
iterations = 150000  # 반복 횟수, 보안을 강화할 수 있음
key = pbkdf2_hmac('sha512', encoded_string, salt, iterations)
result = key.hex()

print(result)
