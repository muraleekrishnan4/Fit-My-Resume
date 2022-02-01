
def find_keywords(job_desc):
	counts = dict()
	result = dict()

	removable_words = ['for', 'and', 'nor', 'but', 'or', 'yet', 'so', 'whose', 'that', 'which', 'whichever', 'who', 'whoever', 'whom', 'whomever', 'what', 'whatever','a', 'an', 'the','yes', 'not', 'aha', 'phooey', 'thanks','up', 'down', 'in', 'out', 'around', 'over', 'among', 'of','have','has','had','is','with','been','ever','since','to']

	top_keywords = ['design','operations','technical','training','sales','marketing','reporting','compliance','strategy','research','analytical','engineering','policies','budget','finance','project management','health','customer service','documentation','content','presentation','brand','presentations','safety','certification','accounting','regulations','metrics','legal','engagement','database','analytics','distribution','coaching','testing','vendors','consulting','writing','contracts','inventory','retail','healthcare','regulatory','scheduling','construction','logistics','mobile','C (programming language)','correspondence','controls','human resources','specifications','recruitment','procurement','partnership','partnerships','management experience','negotiation','hardware','programming','agile','forecasting','advertising','business development','audit','architecture','supply chain','governance','staffing','continuous improvement','product development','networking','recruiting','product management','CRM','SAP','troubleshooting','computer science','budgeting','electrical','customer experience','I-DEAS','economics','information technology','transportation','social media','automation','lifecycle','filing','modeling','investigation','SQL','editing','purchasing','KPIs','hospital','forecasts','acquisition','expenses','billing','change management','video','invoices','administrative support','payments','lean','process improvement','installation','risk management','transactions','investigations','payroll','R (programming language)','data analysis','statistics','coding','protocols','program management','quality assurance','windows','banking','outreach','sourcing','Microsoft Office','merchandising','business requirements','drawings','Salesforce','documenting','information systems','nursing','business administration','consumers','financial services','legislation','strategic planning','MS Office','counseling','technical support','frameworks','performance management','BI','fashion','HTML','publications','internship','QA','software development','oracle','Java'
]

	words = job_desc.split()

	for word in words:
		word = word.capitalize().strip(".,/")
		if word.lower() not in removable_words:
			if word in counts:
				counts[word] += 1
			else:
				counts[word] = 1

	for w in sorted(counts, key=counts.get, reverse=True):
		result[w] = counts[w]

	#counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)

	return result

#print(find_keywords("I am an of example of an boy of girl"))