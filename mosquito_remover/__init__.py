import time, sys 
from tqdm import tqdm

class MosquitoRemover:
  def __init__(self):
		state = input("Are mosquitoes disturbing you? Yes or No ").lower()
		if state == "yes":
			command = input("Do you want to destroy all the mosquitoes? Yes or No ").lower()

			if command == "yes":
				self.destroy()

			if command == "no":
				print("Ok, Bye!")
				exit()

		if state == "no":
			print("Ok, Bye!")
			exit()
			
	def destroy(self):
		for i in tqdm([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]):
			time.sleep(0.3)

		print("Done destroying! Bye!")
		exit()
