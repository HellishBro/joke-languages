import sys
import random


pointer_array = [0]


def encode(command):
	global pointer_array
	pointer = 0
	pointer_array = [0]

	def increment_pointer_array(num):
		pointer_array[pointer] += num

	def get_pointer_value():
		return pointer_array[pointer]

	for curr_char in command:
		if curr_char == "+":
			increment_pointer_array(1)
		elif curr_char == "-":
			increment_pointer_array(-1)
		elif curr_char == "<":
			pointer -= 1
			if pointer == -1:
				pointer == 0
		elif curr_char == ">":
			pointer += 1
			if pointer == len(pointer_array):
				pointer_array.append(0)
		elif curr_char == "!":
			try:
				print(chr(get_pointer_value()), end="")
			except ValueError:
				print(f"\n{get_pointer_value()} is not in the unicode table.")
				sys.exit()
		elif curr_char == "?":
      try:
			  pointer_array[pointer] = ord(input("")[0])
      except IndexError:
        pass
		elif curr_char == "@":
			increment_pointer_array(30)
		elif curr_char == " ":
			pointer_array[pointer] = random.randint(0, 100)
		elif curr_char == ".":
			print(get_pointer_value(), end="")
		elif curr_char == "#":
			increment_pointer_array(10)
		elif curr_char == "$":
			pointer_array[pointer] = 0
	print("\n")


while True:
	encode(input(""))


# simple hello world: @@#++!$@@#-!$@@##----!$@@##----!$@@##-!$@#++++!$@++!$@@@---!$@@##-!$@@##++!$@@##----!$@@#--!$@+++!$
# ik
