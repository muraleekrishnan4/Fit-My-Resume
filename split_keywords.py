import keywords
import yake



def split_keywords(job_desc):
	counts = dict()
	result = dict()

	removable_words = keywords.removable_words
	top_keywords = keywords.top_keywords


	words = job_desc.split() #keywords from splitting the string
	words = [w.capitalize().strip(".,/():") for w in words]

	for word in words:
		if word.lower() not in removable_words:
			if word in counts:
				counts[word] += 1
			else:
				counts[word] = 1

	for w in sorted(counts, key=counts.get, reverse=True):
		result[w] = counts[w]

	#counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)

	return result


