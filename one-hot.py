from keras.preprocessing.text import Tokenizer

samples = ['I study at CityU', 'I study at CityU at Seattle']

tokenizer = Tokenizer(num_words=1000)

tokenizer.fit_on_texts(samples)

sequences = tokenizer.text_to_sequences(samples)

one_hot_results = tokenizer.text_to_matrix(samples, mode='binary')

word_index = tokenizer.word_index
print('Found %s unique tokesn: ' % len(word_index))
print('Sequences: ', sequences, '\n')
print('word_index: ', tokenizer.word_index)
