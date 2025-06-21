def count_words(text):
  words = text.split()
  word_count = 0
  for word in words:
    word_count += 1
  return word_count

def count_letters(words):
  words_lowercase = words.lower()
  letter_dict = {}
  for letter in words_lowercase:
    if letter in letter_dict:
      letter_dict[letter] +=1
    else:
      letter_dict[letter] = 1
  return letter_dict


def sort_by_letter(item):
  return item["num"]

def sorted_count(dict):
  list_of_dict = []
  for char,num in dict.items():
    new_dict = {"char":char,"num": num}
    list_of_dict.append(new_dict)
  list_of_dict.sort(reverse = True, key= sort_by_letter)

  return list_of_dict