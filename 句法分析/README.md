# NLP

- 使用nltk工具对以下获得以下句子的词性标注：

  the lawyer questioned the witness about the revolver

- 使用自底向上，或者自顶向下构建方法，得到所有可能的句法树，比如：

  对于句子：the boy saw the dog with a rod 一个可能的结果为：

  ```python
  (S
  (NP (DT the) (NN boy))
  (VP
  (VBD saw)
  (NP (DT the) (NN dog) (PP (IN with) (NP (DT a) (NN rod))))))
  ```

  测试答案

  使用以下代码，测试你的答案是否正确

  ```python
  grammar = nltk.CFG.fromstring(""" S -> NP VP
  VP -> VBD NP | VBD NP PP
  PP -> IN NP
  NP -> DT NN | DT NN PP
  DT -> "the" | "a" NN -> "boy" | "dog" | "rod" VBD -> "saw"
  IN -> "with"
  """)
  words = nltk.word_tokenize('the boy saw the dog with a rod')
  tags = nltk.pos_tag(words)
  rd_parser = nltk.RecursiveDescentParser(grammar)
  for tree in rd_parser.parse(words):
  print(tree)
  ```
