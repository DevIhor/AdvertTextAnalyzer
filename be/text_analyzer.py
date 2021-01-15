import string

import nltk
import numpy as np
import ssl


def analyze_text(content):
	"""Analyze text and print lexical_diversity, mean_word_len, mean_sentence_len,
	commas_per_thousand.
	"""
	tokens = nltk.word_tokenize(content)

	remove_punctuation = str.maketrans('', '', string.punctuation)
	tokens_ = [x for x in [t.translate(remove_punctuation).lower() for t in tokens] if len(x) > 0]

	# Calculate lexical diversity
	text = nltk.Text(tokens_)
	lexical_diversity = (len(set(text)) / len(text)) * 100

	# Calculate mean word length
	words = set(tokens_)
	word_chars = [len(word) for word in words]
	mean_word_len = sum(word_chars) / float(len(word_chars))

	# Calculate mean sentence length
	sentences = nltk.sent_tokenize(content)
	sentence_word_length = [len(sent.split()) for sent in sentences]
	mean_sentence_len = np.mean(sentence_word_length)

	# Calculate count of commas per 1000
	fdist = nltk.probability.FreqDist(nltk.Text(tokens))
	commas_per_thousand = (fdist[","] * 1000) / fdist.N()

	print(f"Лексичне різноманіття - {lexical_diversity}")
	print(f"Середня довжина слова - {mean_word_len}")
	print(f"Середня довжина речення - {mean_sentence_len}")
	print(f"Частота появи коми (на 1000 символів) - {commas_per_thousand}")


if __name__ == "__main__":
	# Update ssl certificate for nltk downloader
	try:
		_create_unverified_https_context = ssl._create_unverified_context
	except AttributeError:
		pass
	else:
		ssl._create_default_https_context = _create_unverified_https_context

	# Update punkt tokenizer
	try:
		nltk.data.find('tokenizers/punkt')
	except LookupError:
		nltk.download("punkt")

	text = input("Введіть будь ласка текст для аналізу: ")
	analyze_text(text)
