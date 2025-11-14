class Vigenere:
  """
  This class implements the Vigenère cipher.
  """

  def __init__(self, key):
    """
    Initializes the Vigenère cipher with a key.
    """
    self._key = key

  def Encrypt(self, plaintext):
    """
    Encrypts the plaintext using the Vigenère cipher.
    Returns:
      The encrypted ciphertext.
    """
    ciphertext = ""
    key_index = 0
    for char in plaintext:
      if 'a' <= char <= 'z':
        shift = ord(self._key[key_index % len(self._key)].lower()) - ord('a')
        encrypted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
      elif 'A' <= char <= 'Z':
        shift = ord(self._key[key_index % len(self._key)].lower()) - ord('a')
        encrypted_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
      else:
        encrypted_char = char
      ciphertext += encrypted_char
      key_index += 1
    return ciphertext

  def Decrypt(self, ciphertext):
    """
    Decrypts the ciphertext using the Vigenère cipher.
    Returns:
      The decrypted plaintext.
    """
    plaintext = ""
    key_index = 0
    for char in ciphertext:
      if 'a' <= char <= 'z':
        shift = ord(self._key[key_index % len(self._key)].lower()) - ord('a')
        decrypted_char = chr(((ord(char) - ord('a') - shift) % 26) + ord('a'))
      elif 'A' <= char <= 'Z':
        shift = ord(self._key[key_index % len(self._key)].lower()) - ord('a')
        decrypted_char = chr(((ord(char) - ord('A') - shift) % 26) + ord('A'))
      else:
        decrypted_char = char
      plaintext += decrypted_char
      key_index += 1
    return plaintext

  def EncryptFile(self, filename):
    """
    Encrypts a file using the filename as the key.
    Returns:
      The encrypted content of the file.
    """
    try:
      with open(filename, 'r') as file:
        plaintext = file.read()
        return self.Encrypt(plaintext)
    except FileNotFoundError:
      return "File not found."

  def DecryptFile(self, filename):
    """
    Decrypts a file using the filename as the key.
    Returns:
      The decrypted content of the file.
    """
    try:
      with open(filename, 'r') as file:
        ciphertext = file.read()
        return self.Decrypt(ciphertext)
    except FileNotFoundError:
      return "File not found."
    
