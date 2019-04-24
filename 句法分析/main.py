import nltk


# 分词 + 分析
def speech_tagging(text):
    text = nltk.word_tokenize(text)
    text_pro = nltk.pos_tag(text)
    print(text_pro)
    print('\n')


# 语法树
def grammar_sta():
    grammar = nltk.CFG.fromstring("""
    S -> NP VP
    VP -> VBD NP | VBD NP PP
    PP -> IN NP
    NP -> DT NN | DT NN PP
    DT -> "the" | "a" 
    NN -> "boy" | "dog" | "rod" 
    VBD -> "saw"
    IN -> "with"
    """)
    words = nltk.word_tokenize('the boy saw the dog with a rod')
    tags = nltk.pos_tag(words)
    rd_parser = nltk.RecursiveDescentParser(grammar)
    for tree in rd_parser.parse(words):
        print(tree)


def main():
    text = 'the lawyer questioned the witness about the revolver'
    speech_tagging(text)
    grammar_sta()


if __name__ == '__main__':
    main()
