import hashlib
import os
from hashlib import pbkdf2_hmac

# 사용자로부터 입력받기
string = input("문자: ")

# salt을 추가하여 보안 강화
salt = os.urandom(64)

# 문자열을 바이트로 인코딩
encoded_string = string.encode()

# 해시 적용 (중간 변수 사용)
hash_sha1 = hashlib.sha1(encoded_string).hexdigest()
encoded_string = hash_sha1.encode()

hash_sha224 = hashlib.sha224(encoded_string).hexdigest()
encoded_string = hash_sha224.encode()

hash_sha256 = hashlib.sha256(encoded_string).hexdigest()
encoded_string = hash_sha256.encode()

hash_sha384 = hashlib.sha384(encoded_string).hexdigest()
encoded_string = hash_sha384.encode()

hash_sha512 = hashlib.sha512(encoded_string).hexdigest()
encoded_string = hash_sha512.encode()

hash_sha3_512 = hashlib.sha3_512(encoded_string).hexdigest()
encoded_string = hash_sha3_512.encode()

# PBKDF2 적용 (최종 해시)
iterations = 150000  # 반복 횟수, 보안을 강화할 수 있음
key = pbkdf2_hmac('sha512', encoded_string, salt, iterations)

# 결과를 16진수로 변환
result = key.hex()
salt_hex = salt.hex()  # Salt도 16진수로 변환

print(f"Salt: {salt_hex}")
print(f"해시 결과: {result}")
