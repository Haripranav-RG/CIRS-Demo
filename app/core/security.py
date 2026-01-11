import hashlib
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    print("PASSWORD LENGTH:", len(password.encode("utf-8")))
    sha256_hash = hashlib.sha256(password.encode("utf-8")).hexdigest()
    print("SHA256 LENGTH:", len(sha256_hash.encode("utf-8")))
    return pwd_context.hash(sha256_hash)

