import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize, word_tokenize
import warnings

warnings.filterwarnings(action='ignore')

import gensim
from gensim.models import Word2Vec
sgns = ['9829140178', '4351524196', '9927401071', '4060676651', '6676747605', '3967532955', '9216809790',
            '4353017507', '0141509695', '4828983015', '1152219772', '0578350066', '4642344580', '2186541426',
            '3373414237', '5539328653', '7965304652', '9226262878', '6587016334', '6470440069']

# Create CBOW model
model1 = gensim.models.Word2Vec(sgns, min_count=1,
                                size=11, window=1)

# Print results
print("Cosine similarity between 'alice' " +
      "and 'wonderland' - CBOW : ",
      model1.similarity('9829140178', '9829140178'))

print("Cosine similarity between 'alice' " +
      "and 'machines' - CBOW : ",
      model1.similarity('9829140178', '4351524196'))
