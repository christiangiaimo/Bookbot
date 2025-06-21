
from stats import count_words, count_letters, sorted_count
import sys

#Function for reading as a list of strings the text
def get_book_text(filepath):
  with open(filepath) as f:

    file_contents = f.read()
    return(file_contents)

if len(sys.argv)!= 2:
  print("Usage: python3 main.py <path_to_book>") #Explain that the requirements ofhe functions takes 2 parameters
  sys.exit(1) #Exit with error code

#main counter, it reads a file, and count how much time every letter is repeated i also orders it by the amount
def main():
  file = sys.argv[1]
  file_text = get_book_text(file)
  word_counter = count_words(file_text)
  letter_count_dict = count_letters(file_text)
  sorted_count_list = sorted_count(letter_count_dict)
  sorted_list = []
  print("============BOOKBOT============")
  print(f"Analyzing book found at {file}...")
  print("----------- Word Count -----------")
  print(f"Found {word_counter} total words")
  print("--------- Character Count ---------")
  for i in sorted_count_list:
    if i["char"].isalpha():
      print(f"{i["char"]}: {i["num"]}")


main()