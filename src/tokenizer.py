from collections import Counter
import matplotlib.pyplot as plt
import re
import os

def get_words(s,do_lower=True):
	return s.lower().split() if do_lower else s.split()

def tokenize(s, do_lower=False):
	s = s.lower() if do_lower else s
	tokens = re.split(r"(\W)", s)
	tokens = [token for token in tokens if token !=''
			  and re.match(r"\s", token) is None]
	return tokens

def filter_nonwords(string_list):
	return [word for word in string_list if word.isalpha()]

def count_words(words):
	return Counter(words)

def words_by_frequency(words,n=0):
	counts = count_words(words)
	s = sorted(counts.items(),key=lambda x:x[1],reverse=True)
	return s[:n] if n else s

def plot_frequency(tokens):
	keys = [t[0] for t in tokens]
	values = [t[1] for t in tokens]
	plt.bar(keys,values)
	plt.xlabel("Words")
	plt.xticks(rotation=90)
	plt.xticks(fontsize=6)
	plt.ylabel("Frequency counts")
	plt.title("Words by frequency")
	plt.xticks(rotation=90)
	plt.show()

def plot_frequency_by_length(tokens):
	tokens = sorted(tokens,key=lambda x:len(x[0]))
	keys = [(t[0]) for t in tokens]
	values = [t[1] for t in tokens]
	plt.scatter(keys,values)
	plt.xlabel("Words")
	plt.xticks(rotation = 90)
	plt.xticks(fontsize=6)
	plt.ylabel("Frequency counts")
	plt.title('Words by frequency in Project Gutenberg')
	plt.show()

def main():
	with open("carroll-alice.txt","r") as file:
		file_text = file.read()

	words = get_words(file_text)
	words_counted = words_by_frequency(words)
	tokens = tokenize(file_text, do_lower=True)
	tokens_counted = words_by_frequency(tokens)
	filtered_tokens = filter_nonwords(tokens)
	filtered_tokens_counted = words_by_frequency(filtered_tokens)

	directory = "gutenberg_data"
	files = os.listdir(directory)


	for file in files[:5]:
		infile = open(os.path.join(directory,file),"r", encoding="latin1")
		infile_text = infile.read()

		lower_words = get_words(infile_text,do_lower=True)
		upper_words = get_words(infile_text,do_lower=False)

		## words => punctuation not removed
		lower_words_counted = words_by_frequency(lower_words, 100)
		upper_words_counted = words_by_frequency(upper_words, 100)

		plot_frequency_by_length(lower_words_counted)
		# plot_frequency_by_length(upper_words_counted)

		# tokens => punctuation removed
		lower_tokens = tokenize(infile_text, do_lower=True)
		upper_tokens = tokenize(infile_text, do_lower=False)
		lower_tokens_counted = words_by_frequency(lower_tokens, 100)
		upper_tokens_counted = words_by_frequency(upper_tokens, 100)

		plot_frequency_by_length(lower_tokens_counted)
		# plot_frequency_by_length(upper_tokens_counted)


		# print(f'Top 5 words in {file} are {upper_tokens_counted[:5]}')



if __name__ == '__main__':
	main()