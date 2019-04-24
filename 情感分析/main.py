from fractions import Fraction


def process_str(str):
    str1 = ''
    join_str = str1.join(str)
    str = join_str.replace('-', '').replace('+', '')
    str = str.split(' ')
    if '' in str:
        str.remove('')
    return str


def get_class(data):
    neg_count = 0
    pos_count = 0
    for i in range(len(data)):
        if data[i][0] == '-':
            neg_count += 1
        else:
            pos_count += 1
    return neg_count/len(data), pos_count/len(data)


def get_prior(v, n_neg, n_pos, neg_dict, pos_dict):
    word_fraction_in_neg_present = {}
    word_fraction_in_pos_present = {}
    for i in range(len(v)):
        key = v[i]
        a = neg_dict[key] if key in neg_dict.keys() else 0
        b = pos_dict[key] if key in pos_dict.keys() else 0
        word_fraction_in_neg_present[key] = Fraction(a + 1, n_neg + len(v))
        word_fraction_in_pos_present[key] = Fraction(b + 1, n_pos + len(v))
    return word_fraction_in_neg_present, word_fraction_in_pos_present


def train(train_data):
    join_str = process_str(train_data)
    # count without dic
    v = list(set(join_str))
    neg_present, pos_present = get_class(train_data)
    neg = ''
    pos = ''
    neg_dict = {}
    pos_dict = {}
    for i in range(len(train_data)):
        if train_data[i][0] == '-':
            neg += train_data[i]
        else:
            pos += train_data[i]
    neg = process_str(neg)
    pos = process_str(pos)
    for i in range(len(neg)):
        if neg[i] in neg_dict.keys():
            neg_dict[neg[i]] += 1
        else:
            neg_dict[neg[i]] = 1

    for i in range(len(pos)):
        if pos[i] in pos_dict.keys():
            pos_dict[pos[i]] += 1
        else:
            pos_dict[pos[i]] = 1
    the_prior_in_neg, the_prior_in_pos = get_prior(v, len(neg), len(pos), neg_dict, pos_dict)
    return neg_present, pos_present, the_prior_in_neg, the_prior_in_pos, v


def predict(test, neg_present, pos_present, the_prior_in_neg, the_prior_in_pos, v):
    test = process_str(test)
    neg_possibility = neg_present
    pos_possibility = pos_present
    for i in range(len(test)):
        if test[i] in v:
            neg_possibility *= the_prior_in_neg[test[i]]
            pos_possibility *= the_prior_in_pos[test[i]]
    print('\nThe sentence in the test set is negative:', neg_possibility)
    print('The sentence in the test set is positive:', pos_possibility)
    if neg_possibility > pos_possibility:
        print('The sentence is negative!')
    elif neg_possibility == pos_possibility:
        print('possibility(negative) == possibility(positive)')
    else:
        print('The sentence is positive!')

    return neg_possibility, pos_possibility


def main():
    train_data = ['- just plain boring',
                  '- entirely predictable and lacks energy',
                  '- no surprises and very few laughs',
                  '+ very powerful',
                  '+ the most fun file of the summer']
    test_data = ['predictable with no originality']
    neg_present, pos_present, the_prior_in_neg, the_prior_in_pos, v = train(train_data)
    print('The prior for classes -')
    for key, value in the_prior_in_neg.items():
        print(key, ':', value)
    print('\nThe prior for classes +')
    for key, value in the_prior_in_pos.items():
        print(key, ':', value)
    predict(test_data, neg_present, pos_present, the_prior_in_neg, the_prior_in_pos, v)


if __name__ == '__main__':
    main()
