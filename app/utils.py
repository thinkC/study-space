from passlib.context import CryptContext

# create hash password context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# function to hash password


def hash(password: str):
    return pwd_context.hash(password)


# function to verify plain password with hashed password in the database
def verify(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)
