from nltk.corpus import wordnet as wn


# 算同义词集，查看单词，查看定义
def find_synonym_set(words):
    for word in words:
        s = wn.synsets(word)
        print(word, '的同义词集')
        print(s)
        for single_word_set in s:
            print(' 词集：', single_word_set)
            words_set = single_word_set.lemma_names()
            print('     单词')
            print('     ', words_set)
            print('     同义词集的定义')
            print('     ', single_word_set.definition())
            print('     例子')
            print('     ', single_word_set.examples())
        print()


# 查看单词对的语义相似度
def semantic_similarity(words_pair):
    for word_pair in words_pair:
        synsets1 = wn.synsets(word_pair[0])
        synsets2 = wn.synsets(word_pair[1])
        score = 0
        for synset1 in synsets1:
            for synset2 in synsets2:
                temp = synset1.wup_similarity(synset2)
                if temp is not None and temp > score:
                    score = temp
        print('The similarity of ', word_pair[0], 'and', word_pair[1], 'is', score)


# 找单词的蕴含关系和反义词
def get_entailments_and_antonyms(words):
    for word in words:
        print(word)
        s = wn.synsets(word)
        print(' 蕴含关系')
        for i in s:
            for j in i.entailments():
                if j:
                    print(' ', j)
        print(' 反义词关系')
        an_set = []
        for i in s:
            for lm in i.lemmas():
                if lm.antonyms():
                    an_set.append(lm.antonyms()[0].name())
        print(' ', an_set)


def main():
    words = ['dog', 'apple', 'fly']
    words_pair = [['good', 'beautiful'], ['good', 'bad'], ['dog', 'cat']]
    words_wnta = ['walk', 'supply', 'hot']
    print('同义词集及其单词，定义，例子')
    find_synonym_set(words)
    print('\n语义相似度')
    semantic_similarity(words_pair)
    print('\n蕴含关系和反义词')
    get_entailments_and_antonyms(words_wnta)


if __name__ == '__main__':
    main()
