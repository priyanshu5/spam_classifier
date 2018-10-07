# -*- coding: utf-8 -*-
# import necessary library
import os
from collections import Counter

# function to read all the emails and add to dictionary
# with ignoring the non-alphabetics.
def make_dict():
    direc = "emails/"
    files = os.listdir(direc)
    emails = [direc + email for email in files]
    words = []
    c = len(emails)
    for email in emails:
        with open(email, encoding = "ISO-8859-1") as f:
            text = f.read()
        words += text.split(" ")
        
	
        print (c)
        c -= 1
    #print(words)
    #stop = input("wait")
    for i in range(len(words)):
        if not words[i].isalpha():
            words[i] = ""

    dictionary = Counter(words)
    del dictionary[""]
#    print("this is dictionary\n",dictionary)
#   print("this is most_common100 words\n",dictionary.most_common(1000))
    return dictionary.most_common(1000)

# creat function for features and labels to store the data in digits.
def make_dataset(dictionary):
    direc = "emails/"
    files = os.listdir(direc)
    emails = [direc + email for email in files]
    feature_set = []
    labels = []
    c = len(emails)

    for email in emails:
        data = []
        with open(email, encoding = "ISO-8859-1") as f:
            words = f.read().split(' ')
        #print("\nim printing words here",words)
        for entry in dictionary:
            data.append(words.count(entry[0]))
            #print(words.count(entry[0]))
        feature_set.append(data)
       # print("this is frature_sets \n",feature_set)
        if "ham" in email:
            labels.append(0)
        if "spam" in email:
            labels.append(1)
        print (c)
	#print(feature_set)
        c = c - 1
        
    
    #print("this is labels \n",labels)
    return feature_set, labels

# call dictionay and datasets functions.
d = make_dict()
features, labels = make_dataset(d)

#splitting the data into train and test part
from sklearn.model_selection import train_test_split as tts
x_train, x_test, y_train, y_test = tts(features, labels, test_size=0.2)

#print(features)
# training the model with classifier
from sklearn.naive_bayes import MultinomialNB
clf = MultinomialNB()
clf.fit(x_train, y_train)


# Predicting the accuracy of the classifier user in the model
from sklearn.metrics import accuracy_score
preds = clf.predict(x_test)
print (accuracy_score(y_test, preds))



while True:
    features = []
    inp = input(">").split()
    if inp[0] == "exit":
        break
    for word in d:
        features.append(inp.count(word[0]))
    res = clf.predict([features])
    print (["Not Spam", "Spam!"][res[0]])
