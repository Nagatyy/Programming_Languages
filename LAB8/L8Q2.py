import urllib.request
import csv

##########################      Part A      ##########################
#  downloading the data and saving it as words.csv
url = 'https://sketchengine.co.uk/wp-content/uploads/word-list/english/english-word-list-total.csv'
urllib.request.urlretrieve(url, "words.csv")

W = {}
rank = 0
with open('words.csv','rt')as f:
    data = csv.reader(f)
    for row in data:
        row = row[0].split(";")
        if row[0].isdigit():
            rank += 1
            W[rank] = row[1]

for key in range(20):
    print(repr(key+1) + ". " + W[key+1])

##########################      Part B     ##########################

url = 'http://textfiles.com/100/famous.bug'
f = urllib.request.urlopen(url)

S = f.read().decode('utf-8')

##########################      Part D     ##########################

# create a string from S which removes all non alphanumeric characters (but keep spaces)
S = "".join([c.lower() for c in S if (c.isalnum() or c == " ") and c is not ''])
list_of_story_words = S.split(" ")  #split the string by spaces (to get words)

frequency_dict = {key: 0 for key in list_of_story_words}
# populate the dictionary holding the words with frequency
for word in list_of_story_words:
    frequency_dict[word] += 1
# sort the dictionay in order of frequency (highest to lowest)
sorted_list_of_words = sorted(frequency_dict, key=frequency_dict.get, reverse=True)
# there was an erronous '', remove it
sorted_list_of_words.remove('')
# obtain a list of the 20 most frequent words in story
list_of_freq_story_words = sorted_list_of_words[:20]

for word in list_of_freq_story_words:
    print(word + ": " + repr(frequency_dict[word]))

##########################      Part E     ##########################
# invert the dictionary so that it is word:rank instead of rank:word
inv_dict = {v: k for k, v in W.items()}

list_of_english_words = sorted(inv_dict, key=inv_dict.get)
# obtain a list of lowercased 20 most frequent words
list_of_20_english_words = list(map(str.lower, list_of_english_words[:20]))
# create a list of the common words
list_of_common_words = [word for word in list_of_freq_story_words if word in list_of_20_english_words]

print(list_of_common_words)

##########################      Part F     ##########################
print(list_of_20_english_words)
print(list_of_freq_story_words)

# identify any discrepancies
for i,word in enumerate(list_of_20_english_words):
    if not word == list_of_freq_story_words[i]:
        print(word + " is a different rank")

    print(word + " is in the english dictionary but not in the story") if word not in list_of_freq_story_words else None

for word in list_of_freq_story_words:
    print(word + " is in the story but not in the dictionary") if word not in list_of_20_english_words else None






