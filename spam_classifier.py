
# coding: utf-8

# In[1]:


# import neccessary library for file reading # and word counting
import os
from collections import Counter


# In[2]:


# create dict function to store all words from emails with frequency of their occurrence
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
        
    for i in range(len(words)):
        if words[i].isalpha() == False: # find all non-aphabete words which are irrelevant here
            words[i] = ""
        elif len(words[i]) == 1:         # words of single length 
            words[i] = ""
       
    
    dictionary = Counter(words)
    del dictionary[""] 
    # delete all words from dict which are irrelevant # and does not contribute to feature sets.
    keys = {'in','is','and','at','we','are','it','has','of'}
    for k in keys:
        del dictionary[k]
   
    return dictionary.most_common(3000)    


# In[3]:


make_dict()


# In[4]:


# create function for features and labels to store the data in digits.
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
        #print("this is frature_sets \n",feature_set)
        if "ham" in email:
            labels.append(0)
        if "spam" in email:
            labels.append(1)
        print (c)
        #print(feature_set)
        c = c - 1
        
    
    #print("this is labels \n",labels)
    return feature_set, labels


# In[5]:


d = make_dict()
features, labels = make_dataset(d)


# In[6]:


#import model_selection to split the datasets into train and test sets
from sklearn.model_selection import train_test_split as tts
x_train, x_test, y_train, y_test = tts(features, labels, test_size=0.3) # 80% data is used to train and 20 % for testing


# In[10]:


# training the model with naive_bayes classifier
from sklearn.metrics import confusion_matrix
from sklearn.naive_bayes import MultinomialNB
clf1 = MultinomialNB()
clf1.fit(x_train, y_train)

# Predicting the accuracy of the naive_bayes classifier
from sklearn.metrics import accuracy_score
predict1 = clf1.predict(x_test)
print (accuracy_score(y_test, predict1))
print (" Confusion matrix ", confusion_matrix(y_test, predict1))


# In[11]:


# training the model with Support Vector (SVM) classifier
from sklearn.svm import LinearSVC
clf2 = LinearSVC()
clf2.fit(x_train, y_train)

# Predicting the accuracy of the SVM classifier
predict2 = clf2.predict(x_test)
print(accuracy_score(y_test, predict2))
print (" Confusion matrix ", confusion_matrix(y_test, predict2))


# In[12]:


# training the model with Random Forest Classifier
from sklearn.ensemble import RandomForestClassifier
clf3 = RandomForestClassifier()
clf3.fit(x_train, y_train)

# Predicting the accuracy of the Random Forest Classifier
predict3 = clf3.predict(x_test)
print(accuracy_score(y_test, predict3))
print (" Confusion matrix ", confusion_matrix(y_test, predict3))


# In[ ]:


"""while True:
    features = []
    inp = input(">").split()
    if inp[0] == "exit":
        break
    for word in d:
        features.append(inp.count(word[0]))
    res = clf.predict([features])
    print (["Not Spam", "Spam!"][res[0]])"""

