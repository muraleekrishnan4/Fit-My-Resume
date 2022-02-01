import yake

def yake_keywords(job_desc):
	counts = dict()
	result = dict()


	kw_extractor = yake.KeywordExtractor()
	language = "en"
	max_ngram_size = 2
	deduplication_threshold = 0.3
	numOfKeywords = 20
	custom_kw_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, dedupLim=deduplication_threshold, top=numOfKeywords, features=None)

	keywords = custom_kw_extractor.extract_keywords(job_desc)


	for kw in keywords:
		w = kw[0].capitalize()
		if w in counts:
			counts[w] += 1
		else:
			counts[w] = 1

	for w in sorted(counts, key=counts.get, reverse=True):
		result[w] = counts[w]

	return result