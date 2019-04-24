import spacy
import neuralcoref

nlp = spacy.load('en')
neuralcoref.add_to_pipe(nlp)
text = [u'My sister has a dog. She loves him.',
        u'Some like to play football, others are fond of basketball.',
        u'The more a man knows, the more he feels his ignorance.']

for t in text:
    t = nlp(t)
    print(t)
    if t._.has_coref:
        print(' ',t._.coref_clusters)
    else:
        print('  No coref!')