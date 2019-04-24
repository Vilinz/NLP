# encoding=utf-8
import string
import re
import jieba.posseg as pseg


# 加载字典
def load_word_list():
	max_length = 0
	word_dict = set()
	for line in open('./data/corpus.dict.txt',encoding='utf-8',errors='ignore').readlines():
		tmp = len(line)
		if max_length < tmp:
			max_length = tmp
		word_dict.add(line.strip())
	return {'max_length': max_length, 'word_dict': word_dict}


# 去标点符号
def delete_punctuation(line):
	illegal_char = string.punctuation + '！？。＂＃＄％＆＇（）＊＋，－／：；＜＝＞＠［＼］＾＿｀｛｜｝～｟｠｢｣､、〃《》「」『』【】〔〕〖〗〘〙〚〛〜〝〞〟〰〾〿–—‘’‛“”„‟…‧﹏.\n'
	pattern = re.compile('[%s]'%re.escape(illegal_char))
	new_line = pattern.sub(u'', line)
	return new_line


# 最大正向匹配
def max_left_match(line):
	result = []
	dic = load_word_list()
	MaxLen = dic['max_length']
	word_dict = dic['word_dict']
	print("maxlen", MaxLen)
	while len(line) > 0:
		temp_len = MaxLen
		while temp_len > 0:
			if len(line) >= temp_len:
				word = line[0:temp_len]
				if temp_len == 1:
					result.append(word)
					line = line[temp_len:]
					break
				if word in word_dict:
					result.append(word)
					line = line[temp_len:]
					break
			temp_len -= 1
	return result


# 测试
def main():
	fw = open('./data/corpus.out.txt', 'w')
	fw_jieba = open('./data/jieba.result.txt', 'w')
	for line in open('./data/corpus.sentence.txt', encoding='utf-8', errors='ignore').readlines():
		# 去标点
		line_without_punc = delete_punctuation(line)
		# print(line_without_punc)

		words = pseg.cut(line_without_punc)
		for w in words:
			fw_jieba.write(w.word + " " + w.flag + "\n")
		# 最大匹配
		result = max_left_match(line_without_punc)
		# 结果
		print(result)
		write_result = ""
		for i in range(len(result)):
			if i == 0:
				write_result += result[i]
			else:
				write_result = write_result + " " + result[i]
		fw.write(write_result)
		fw.write('\n')
	fw.close()
	fw_jieba.close()


if __name__ == '__main__':
	main()
