
class Caesar:
  """
  This class implements the Caesar cipher.
  """

  def __init__(self):
    """Initializes the Caesar cipher with a random key."""
    self._key = random.randint(1, 25)  # Key should be between 1 and 25 for rotation

  def Encrypt(self, plaintext):
    """
    Encrypts the plaintext using the Caesar cipher.
    Returns:
      The encrypted ciphertext.
    """
    ciphertext = ''
    for char in plaintext:
      if 'a' <= char <= 'z':
        rotated_char = chr(((ord(char) - ord('a') + self._key) % 26) + ord('a'))
      elif 'A' <= char <= 'Z':
        rotated_char = chr(((ord(char) - ord('A') + self._key) % 26) + ord('A'))
      elif '0' <= char <= '9':
        rotated_char = str((int(char) + self._key) % 10)
      else:
        rotated_char = char  # Punctuation and spaces remain unchanged
      ciphertext += rotated_char
    return ciphertext

  def Decrypt(self, ciphertext):
    """
    Decrypts the ciphertext using the Caesar cipher.
    Returns:
      The decrypted plaintext.
    """
    plaintext = ''
    for char in ciphertext:
      if 'a' <= char <= 'z':
        rotated_char = chr(((ord(char) - ord('a') - self._key) % 26) + ord('a'))
      elif 'A' <= char <= 'Z':
        rotated_char = chr(((ord(char) - ord('A') - self._key) % 26) + ord('A'))
      elif '0' <= char <= '9':
        rotated_char = str((int(char) - self._key) % 10)
      else:
        rotated_char = char
      plaintext += rotated_char
    return plaintext

  def Attack(self, ciphertext):
    """
    Runs a brute-force attack on the ciphertext.
    Returns:
      A list of tuples, where each tuple contains the key value and
      the decrypted plaintext for that key.
    """
    results = []
    for key in range(26):
      plaintext = ''
      for char in ciphertext:
        if 'a' <= char <= 'z':
          rotated_char = chr(((ord(char) - ord('a') - key) % 26) + ord('a'))
        elif 'A' <= char <= 'Z':
          rotated_char = chr(((ord(char) - ord('A') - key) % 26) + ord('A'))
        elif '0' <= char <= '9':
          rotated_char = str((int(char) - key) % 10)
        else:
          rotated_char = char
        plaintext += rotated_char
      results.append((key, plaintext))
    return results