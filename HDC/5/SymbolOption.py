import enum
import string 

class SymbolOption(enum.Enum):

    uppercase = [False, string.ascii_uppercase]
    lowercase = [False, string.ascii_lowercase]
    numbers = [False, string.digits]
    special = [False, string.punctuation]
