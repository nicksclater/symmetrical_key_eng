#!/usr/local/bin/python3

import numpy as np
import random as rd

def create_key():
	arr = np.full((8000),0)
	return [rd.choice([0,1]) for i in arr]

key = create_key()


def encryption_eng(input_string: str) -> str:

  convert2bin = lambda char: np.binary_repr(ord(char),8)
  apply_gate = lambda x, key: 1 if (x == 1 and key == 1) or (x == 0 and key == 0) else 0

  bin_array = []
  encrypted_list = []
  encrypted_str = ''

  for i in input_string:
    bin_array.append(convert2bin(i))

  for i in range(0, len(bin_array)):
    bin_array[i] = [0 if j == '0' else 1 for j in bin_array[i]]

  bin_array = np.reshape(bin_array, (len(input_string) * 8,))

  encrypted_list = list(map(apply_gate, bin_array, key))
  encrypted_arr = np.array(encrypted_list).reshape(len(input_string), 8)
  encrypted_list =[]

  for i in range(0,len(encrypted_arr)):
    temp = ''
    for j in range(8):
      temp += str(encrypted_arr[i][j])

    encrypted_list.append(chr(int(temp,2)))

  for i in encrypted_list:
    encrypted_str += i

  return encrypted_str

print('\n')
plain = 'the cat sat on the mat'
print(f'plain text: {plain}')

encrypted = encryption_eng(plain)
print(f'encrypted text: {encrypted}')

decrypted = encryption_eng(encrypted)

print(f'decrypted text: {decrypted}')


