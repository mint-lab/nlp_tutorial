from sklearn import (datasets, feature_extraction, linear_model, naive_bayes, neural_network, neighbors, svm, tree, ensemble, metrics)

# 1.1. Load the 20 newsgroup dataset
remove = ('headers', 'footers', 'quotes')
train_raw = datasets.fetch_20newsgroups(subset='train', remove=remove)
tests_raw = datasets.fetch_20newsgroups(subset='test',  remove=remove)

# 1.2. Train the vectorizer
vectorizer = feature_extraction.text.TfidfVectorizer(min_df=5, max_df=0.1, stop_words='english')
#vectorizer = feature_extraction.text.TfidfVectorizer(stop_words='english') # Try Kim's vectorizer
#vectorizer = feature_extraction.text.TfidfVectorizer(max_df=0.08, stop_words='english', strip_accents='ascii', token_pattern='[A-Za-z]{1,}', ngram_range=(1,2), sublinear_tf=True) # Try Seo's vectorizer
vectorizer.fit(train_raw.data)
print('* The size of vocabulary: ', len(vectorizer.vocabulary_))

# 1.3. Vectorize the training and test data
train_vectors = vectorizer.transform(train_raw.data)
tests_vectors = vectorizer.transform(tests_raw.data)

# 2. Instantiate classifier models
models = [
    {'name': 'linear_model.SGD',   'inst': linear_model.SGDClassifier()},
    {'name': 'naive_bayes.CompNB', 'inst': naive_bayes.ComplementNB(alpha=0.4)},
    {'name': 'svm.LinearSVC',      'inst': svm.LinearSVC(class_weight='balanced')},
    {'name': 'svm.SVC(linear)',    'inst': svm.SVC(kernel='linear', class_weight='balanced')},
    {'name': 'svm.SVC(rbf)',       'inst': svm.SVC(class_weight='balanced')},
    {'name': 'neural_network.MLP', 'inst': neural_network.MLPClassifier(learning_rate='adaptive', early_stopping=True, verbose=True)},
]

# 3. Evaluate the classifier models
for m in models:
    # Train the model
    m['inst'].fit(train_vectors, train_raw.target)
    train_predict = m['inst'].predict(train_vectors)
    train_accuracy = metrics.balanced_accuracy_score(train_raw.target, train_predict)

    # Test the model
    tests_predict = m['inst'].predict(tests_vectors)
    tests_accuracy = metrics.balanced_accuracy_score(tests_raw.target, tests_predict)

    print(f'* {m["name"]}')
    print(f'  * Training accuracy: {train_accuracy:.3f}')
    print(f'  * Test accuracy: {tests_accuracy:.3f}')
