from newspaper import Article

from syntok.tokenizer import Tokenizer
import syntok.segmenter as segmenter

from lexrank import LexRank
from lexrank.mappings.stopwords import STOPWORDS
from path import Path

documents = []

paths = Path('./bbc-fulltext/bbc').glob('politics/')
# print(paths)
for category in paths:
  for file_path in category.files('*.txt'):
    with file_path.open(mode='r', encoding='utf-8') as file:
      documents.append(file.readlines())

# print(documents[:5])

lxr = LexRank(documents, stopwords=STOPWORDS['en'])

# url = 'https://www.nytimes.com/2021/03/18/opinion/anti-asian-american-violence.html'
# article = Article(url)
# article.download()
# article.parse()

# text = article.text

text = '''
The grim reality of modern American life is that each new mass killing leads to a fevered study of motives and meaning. Was the latest shooter motivated by racism, misogyny, religion, revenge or some combination thereof? Those are not questions that members of a healthy society should routinely be forced to ask or answer.

After eight people — including six people of Asian descent and seven women — were shot to death in Georgia this week, a deputy sheriff chalked the killings up to the suspect’s confessed “sex addiction,” adding that “yesterday was a really bad day” for the alleged shooter. That diagnosis was met with the skepticism it deserved: The same deputy promoted the sale of anti-Asian T-shirts that referred to the coronavirus as an import from “Chy-na.”

It’s difficult to disentangle the vile pathologies that lead a man to take so many innocent lives. It’s also impossible to ignore the context in which the murders were committed and the impact that the tragedy has had on communities across America. In an analysis of nearly 4,000 hate-related incidents targeting Asian-Americans documented this year and last, nearly 70 percent of the victims were women, according to a report by the group Stop AAPI Hate. New York was the second state behind California in the total number of incidents documented by the group.

“Among large American cities,” The Times reports, “New York City had the largest increase in reported hate crimes against Asians last year, according to an analysis of police data by a center at the California State University, San Bernardino. There were 28 such incidents in 2020, up from three in 2019, according to New York Police Department data.”

A bill currently before the New York State Legislature, sponsored by State Senator Brad Hoylman and Assemblywoman Karines Reyes, would mandate better collection of data about hate crimes.

After a year of vitriol and violence against Asian-Americans amid the coronavirus pandemic, it’s long past time to admit that the country has a problem. “The Asian-American community has reached a crisis point that cannot be ignored,” Representative Judy Chu, a Democrat from California, told a congressional hearing on Thursday. It was the first such hearing on anti-Asian discrimination in three decades.

A year ago this month, after the pandemic had already established a beachhead in the United States, this board wrote that there was a long history of diseases triggering waves of violence — against Jews during the Black Death right through the animus linked to Ebola, SARS and Zika. “Chinese-Americans and other Asians lumped together with them by racists are being beaten, spat on, yelled at and insulted from coast to coast, driving some members of the maligned minority to purchase firearms in the fear of worse to come as the pandemic deepens,” the board wrote.

The president then was Donald Trump, who spent his term exploiting anti-immigrant hostility for political gain. He seized every opportunity to cast the pandemic in bigoted terms, portraying China in particular as the villain. Mr. Trump said “China virus” again this week during a Fox News interview on the very night of the Georgia shootings.

President Biden and Vice President Kamala Harris are scheduled on Friday to meet with leaders from the Asian-American and Pacific Islander communities in Atlanta, a welcome display of presidential civility.

It’s impossible not to acknowledge the nation’s history of maltreatment of Asian-Americans, nor how it has manifested over the past year — from political stump speeches, to xenophobic merchandise, to the rise in hate crimes. It falls to Americans living in the shadow of this history to demand more from ourselves — more compassion, more dignity, more grace — as we work to heal our society of its many ills.
'''

tok = Tokenizer()

split_text = segmenter.split(tok.tokenize(text))
parsed_text = []
for sentence in split_text:
  parsed_text.append(''.join([str(token) for token in sentence]))

print(parsed_text)

summary = lxr.get_summary(parsed_text, threshold=None)

print(summary)