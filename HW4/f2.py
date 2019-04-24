import nltk
from nltk.stem import LancasterStemmer
from nltk.corpus import stopwords
from nltk.tokenize import WordPunctTokenizer
import string
import re

class Process:
  def __init__(self):
    f = open("text_en.txt", "rb")
    self.text = f.read().decode('utf-8')
    self.words = self.spilt_text()
    self.stems = self.get_stems()
    self.without_stop = self.remove_stopwords()
    self.without_punc = self.delete_punctuation()
    f.close()
  
  # 分词
  def spilt_text(self):
    tokenizer=WordPunctTokenizer()
    words = tokenizer.tokenize(self.text)
    # words=nltk.word_tokenize(self.text)
    print("分词结果：")
    print(words)
    return words

  # 提取词干
  def get_stems(self):
    stemmerlan = LancasterStemmer()
    stems = []
    for i in self.words:
      stems.append(stemmerlan.stem(i))
    print("\n提取词干后：")
    print(stems)
    return stems

  # 去停用词
  def remove_stopwords(self):
    stops = set(stopwords.words('english'))
    without_stop = [stem for stem in self.stems if stem.lower() not in stops]
    print("\n去停用词后：")
    print(without_stop)
    return without_stop

  # 去标点符号
  def delete_punctuation(self):
    new_words = []
    illegal_char = string.punctuation + '【·！…（）—：“”？《》、；】'
    pattern = re.compile('[%s]'%re.escape(illegal_char))

    for word in self.without_stop:
      new_word = pattern.sub(u'', word)
      if not new_word == u'':
        new_words.append(new_word)
    print("\n去标点符号后：")
    print(new_words)
    return new_words

  # 统计词频
  def count(self):
    freq = nltk.FreqDist(self.without_punc)
    print("\n词频：")
    for key, val in freq.items():
      print(str(key) + ":" + str(val))

  # 统计分布
  def dispersion(self):
    nltk.draw.dispersion_plot(self.words, ['Elizabeth', 'Darcy','Wickham', 'Bingley', 'Jane'])

  # 低频词过滤（n <= threshold）
  def filter(self, threshold):
    freq = nltk.FreqDist(self.without_punc)
    result = {}
    for key, val in freq.items():
      if val > threshold:
        result[key] = val
    return result

  # 对前 20 个有意义的高频词，绘制频率分布图
  def draw_high_20(self):
    stops = set(stopwords.words('english'))
    without_stop = [word for word in self.words if word.lower() not in stops]
    new_words = []
    illegal_char = string.punctuation + '【·！…（）—：“”？《》、；】'
    pattern = re.compile('[%s]'%re.escape(illegal_char))

    for word in without_stop:
      new_word = pattern.sub(u'', word)
      if not new_word == u'':
        new_words.append(new_word)
    
    fdist = nltk.FreqDist(new_words)
    fdist.plot(20)

def main():
  p = Process()
  # print(p.filter(100))
  # p.dispersion()
  p.draw_high_20()

if __name__ == '__main__':
  main()
