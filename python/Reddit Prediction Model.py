import json # we need to use the JSON package to load the data, since the data is stored in JSON format
import time
import numpy as np
from numpy.linalg import inv
from _operator import itemgetter
import test
import matplotlib.pyplot as plt

with open("proj1_data.json") as fp:
    data = json.load(fp)
    
# Now the data is loaded.
# It a list of data points, where each datapoint is a dictionary with the following attributes:
# popularity_score : a popularity score for this comment (based on the number of upvotes) (type: float)
# children : the number of replies to this comment (type: int)
# text : the text of this comment (type: string)
# controversiality : a score for how "controversial" this comment is (automatically computed by Reddit)
# is_root : if True, then this comment is a direct reply to a post; if False, this is a direct reply to another comment 

## Example:
#data_point = data[0] # select the first data point in the dataset

## Now we print all the information about this datapoint
#for info_name, info_value in data_point.items():
#    print(info_name + " : " + str(info_value))


###################################################################################

# 1) Split the data:

train_data = []
validation_data = []
test_data = []

for i in range (0,10000):
    train_data.append(data[i])
    
for i in range (10000,11000):
    validation_data.append(data[i])
    
for i in range (11000,12000):
    test_data.append(data[i])


# 2) Compute some text features:
    
def stringToList(pString):
    newList = pString.lower()
    newList = newList.split() 
    return newList
    
def totalWordCount(pDataList):
    totalWordList = {}
    for dataPoint in pDataList:
        newWords = stringToList(dataPoint.get("text"))
        
        for word in newWords:
            if word in totalWordList:
                totalWordList[word] = totalWordList[word] + 1
            else:
                totalWordList[word] = 1
        
    sortedList = sorted(totalWordList.items(), key = itemgetter(1))
    
    #Select the top 160:
    topWords = []
    
    index = 0
    for word in reversed(sortedList):
        topWords.append(word[0])
        index = index + 1
        if index == 160:
            break
        
    
    return topWords


def getWordCountVector(pTopWords, pWordList):
    countVector = []
    for i in range(0,160):
        countVector.append(0)
    
    for word in pWordList:
        if word in pTopWords:
            countVector[pTopWords.index(word)] = countVector[pTopWords.index(word)] + 1

    #add bias:
    countVector.append(1) 
    return countVector

def computeAllWordCountVector(pDataList):
    allWordCountVector = []
    topWords = totalWordCount(pDataList)
    for dataPoint in pDataList:
        wordCountVector = getWordCountVector(topWords, stringToList(dataPoint.get("text")))
        allWordCountVector.append(wordCountVector)
        
    return allWordCountVector

### top 60 bellow:

# numberTopWords must be an integer
def totalWordCountVary(pDataList, numberTopWords):
    totalWordList = {}
    for dataPoint in pDataList:
        newWords = stringToList(dataPoint.get("text"))
        
        for word in newWords:
            if word in totalWordList:
                totalWordList[word] = totalWordList[word] + 1
            else:
                totalWordList[word] = 1
        
    sortedList = sorted(totalWordList.items(), key = itemgetter(1))
    
    #Select the top numberTopWords:
    topWords = []
    
    index = 0
    for word in reversed(sortedList):
        topWords.append(word[0])
        index = index + 1
        if index == numberTopWords:
            break
        
    
    return topWords

def getWordCountVectorVary(pTopWords, pWordList, numberTopWords):
    countVector = []
    for i in range(0,numberTopWords):
        countVector.append(0)
    
    for word in pWordList:
        if word in pTopWords:
            countVector[pTopWords.index(word)] = countVector[pTopWords.index(word)] + 1
    #add bias:
    countVector.append(1) 
    return countVector

def computeAllWordCountVectorVary(pDataList, numberTopWords):
    allWordCountVector = []
    topWords = totalWordCountVary(pDataList, numberTopWords)
    for dataPoint in pDataList:
        wordCountVector = getWordCountVectorVary(topWords, stringToList(dataPoint.get("text")),60)
        allWordCountVector.append(wordCountVector)
    
    return allWordCountVector



#wordCountFeature = computeAllWordCountVector(train_data) # array of size equal to amount of datapoint of the input, with at each index i an array of size 160 corresponding to the vector (word count) of the ith datapoint

## Test features, including the wordCountFeature and the other basic information from the data point:
# index 0,1, ..., 159 are the wordCount,
# 160: number of children
# 161: controversiality score
# 162: is_root : if True, value of 1, if False, value of 0
# last index (currently 163): bias term (value of 1)

def addBasicFeatures(pWordCountFeature, pDataList):

    features = pWordCountFeature.copy()
    index = 0
    for dataPoint in pDataList:
        features[index].append(dataPoint.get("children"))
        features[index].append(dataPoint.get("controversiality"))

        is_rootValue = dataPoint.get("is_root")
        if is_rootValue == True:
            features[index].append(1)
        else:
            features[index].append(0)
        
        
        # bias:
        features[index].append(1)
        index = index + 1
    
    return features


#features = addBasicFeatures(wordCountFeature, train_data)


## Produce words.txt, one word per line (one extra blank line) from highest frequency to lowest.
'''
topWords = totalWordCount(train_data)

file = open("words.txt", "w")

for word in topWords:
    file.write(word + "\n")
'''

## Produce target matrix:
def produceTargetMatrix(pDataList):
    targetMatrix = []
    for datapoint in pDataList:
        targetMatrix.append(datapoint.get("popularity_score"))
        
    return targetMatrix

## Produce the simple 3 features matrix:
def produceSimpleFeatures(pDataList):
    features = []
    for dataPoint in pDataList:
        
        childrenValue = dataPoint.get("children")
        controversialityValue = dataPoint.get("controversiality")
        isRootValue = 0
        
        if dataPoint.get("is_root") == True:
            isRootValue = 1
            
        bias = 1
        
        features.append([childrenValue, controversialityValue, isRootValue, bias])
        
    return features


# Additional features:

def createEmptyFeature(pDataList):
    features = []
    for dataPoint in pDataList:
        features.append([])
        
    return features
 
def addLengthFeature(pFeatures, pDataList):
    features = pFeatures.copy()
    
    index = 0
    for dataPoint in pDataList:
        features[index].append(len(stringToList(dataPoint.get("text"))))
        index = index + 1
    return features

def addPunctuationUsage(pFeatures, pDataList):
    features = pFeatures.copy()
    
    index = 0
    
    for dataPoint in pDataList:
        
        usage = False
        
        textString = dataPoint.get("text")
        for letter in textString:
            if letter == '?' or letter == '!':
                usage = True
                
        if usage == True:
            features[index].append(1)
        else:
            features[index].append(0)
            
        index = index + 1
    return features
##################################################################

#To create the feature Matrix : (change the data set if necessary: train_data, validation_data, test_data)
#wordCountFeature = computeAllWordCountVector(train_data)    #160 top words
#features = addBasicFeatures(wordCountFeature, train_data)   #160 top words + basic features (more info above)

#simpleFeatures = produceSimpleFeatures(train_data)  # children, controversiality, is_root, bias

#To produce the target Matrix: (change the data set if necessary
#targetMatrix = produceTargetMatrix(train_data)


#####################################################################


#Actual Test:  

inputData = train_data # train_data, validation_data, test_data

# 1) 3 simple features + bias (children, controversiality, is_root, bias)

simpleFeaturesTrain = produceSimpleFeatures(inputData)
simpleFeaturesValid = produceSimpleFeatures(validation_data)


# 2) no text features vs top-60 words vs top 160 words:

top160FeaturesTrain = computeAllWordCountVector(inputData)
top60FeaturesTrain = computeAllWordCountVectorVary(inputData, 60)
top160FeaturesValid = computeAllWordCountVector(validation_data)
top60FeaturesValid = computeAllWordCountVectorVary(validation_data, 60)

# 3)

lengthFeatureTrain = addBasicFeatures(addLengthFeature(createEmptyFeature(inputData), inputData), inputData)  # length of the texts + basic features + bias
punctuationFeatureTrain = addBasicFeatures(addPunctuationUsage(createEmptyFeature(inputData), inputData), inputData) # usage of ! & ?,  plus basic features + bias
lengthFeatureValid = addBasicFeatures(addLengthFeature(createEmptyFeature(validation_data), validation_data), validation_data)
punctuationFeatureValid = addBasicFeatures(addPunctuationUsage(createEmptyFeature(validation_data), validation_data), validation_data)
multiFeatureTrain = addBasicFeatures(addLengthFeature(addPunctuationUsage(createEmptyFeature(inputData), inputData), inputData),inputData)
multiFeatureValid = addBasicFeatures(addLengthFeature(addPunctuationUsage(createEmptyFeature(validation_data), validation_data), validation_data),validation_data)



# Target data:

targetMatrixTrain = produceTargetMatrix(inputData)
targetMatrixValid = produceTargetMatrix(validation_data)
targetMatrixTest = produceTargetMatrix(test_data)

def closed(X, y):
    
    #X is n datapoints -- size : n by m where n is number of datapoints and m is number of features
    #y is n target values -- size : n by 1
    w = np.matmul(inv(np.matmul(X.transpose(), X)), np.matmul(X.transpose(), y))
    return w


#Defining function for gradient descent linear regression
def descent(X, y, learning_rate, init_type):
    
    #X is n datapoints -- size : n by m where n is number of datapoints and m is number of features
    #y is n target values -- size : n by 1
    eps = 0.1     #Threshold for stopping gradient descent steps
    i = 0           #Step number
    B = learning_rate           #Initial learning rate
    
    if init_type == 0: #initialize randomly with random numbers (with variance of 0.01)
          w = np.random.randn(X.shape[1], 1) * 0.01 #Initialize wights randomly with random numbers having zero mean and 0.01 variance
    else:
          w = np.zeros((X.shape[1], 1)) #Initialize weights with zeros
    wp = w          #Save previous w in wp 
    y = np.array(y).reshape(X.shape[0], 1)
    XtX = np.matmul(X.transpose(), X)
    Xty = np.matmul(X.transpose(), y)
    while True:     #Main loop of gradient descent
        if np.sum(np.sqrt(w-wp)) < eps and i!=1:
            print('Distance between W(i) & W(i-1) after convergence is :', np.sum(np.sqrt(w-wp)))
            break
        else:
            a = B/(1+i)     #Decrease learning rate
            wp = w
            w = w - (2/X.shape[0]) * a * (np.matmul(XtX, w)-Xty)     #Update w parameters
            i += 1          #Increase step number
        
    return w


# Method to run closed regression and return mean squared error

def findClosedErrors(training_x,training_y,validation_x,validation_y):
    w = closed(training_x,training_y)
    validation_y = np.array(validation_y)
    predicted_y = np.matmul(validation_x,w)
    accuracy = np.mean((validation_y - predicted_y)**2)
    return accuracy

# Method to run gradient descent and return mean squared error

def findDescentErrors(training_x,training_y,validation_x,validation_y):
    learning_rate = .1
    w = descent(training_x,training_y,learning_rate,1)
    validation_y = np.array(validation_y)
    predicted_y = np.matmul(validation_x,w)
    accuracy = np.mean((validation_y - predicted_y)**2)
    return accuracy

#Method that checks the run time and mean squared error of both models

def performanceCheck(training_x,training_y,validation_x,validation_y):
    training_x = np.array(training_x)
    validation_x = np.array(validation_x)
    start = time.time()
    #Checks linear regression
    errors = findClosedErrors(training_x,training_y,validation_x,validation_y)
    end = time.time()
    print("LR MSE: " , errors)
    print("Linear regression runtime: " , (end-start))
    start = time.time()
    #Checks gradient descent
    errors = findDescentErrors(training_x,training_y,validation_x,validation_y)
    end = time.time()
    print("GD MSE: ", errors)
    print("Gradient descent runtime: " , (end-start))

#Method to compare performance of different data sets

def numFeatureComparison(nofeaturetrain,nofeaturevalid,sixtyfeaturetrain,sixtyfeaturevalid,training_x,validation_x,training_y,validation_y):
    #Initialize variables as matrices
    training_x = np.array(training_x)
    training_y = np.array(training_y)
    validation_x = np.array(validation_x)
    validation_y = np.array(validation_y)
    nofeaturetrain = np.array(nofeaturetrain)
    sixtyfeaturetrain = np.array(sixtyfeaturetrain)
    nofeaturevalid = np.array(nofeaturevalid)
    sixtyfeaturevalid = np.array(sixtyfeaturevalid)
    #Check performance of basic feature data
    verify_accuracy = findClosedErrors(nofeaturetrain,training_y,nofeaturetrain,training_y)
    print("No feature training errors: ", verify_accuracy)
    valid_accuracy = findClosedErrors(nofeaturetrain,training_y,nofeaturevalid,validation_y)
    print("No feature errors: " , valid_accuracy)
    #Check performance of partial feature data
    verify_accuracy = findClosedErrors(sixtyfeaturetrain,training_y,sixtyfeaturetrain,training_y)
    print("60 feature training errors: ", verify_accuracy)
    valid_accuracy = findClosedErrors(sixtyfeaturetrain,training_y,sixtyfeaturevalid,validation_y)
    print("60 feature errors: " , valid_accuracy)
    #Check performance of full feature data
    verify_accuracy = findClosedErrors(training_x,training_y,training_x,training_y)
    print("160 feature training errors: ", verify_accuracy)
    valid_accuracy = findClosedErrors(training_x,training_y,validation_x,validation_y)
    print("160 feature errors: " , valid_accuracy)

def newFeatureComparison(lengthFeatureTrain,punctuationFeatureTrain,training_y,lengthFeatureValid,punctuationFeatureValid,validation_y):
    #Initialize variables as matrices
    lengthFeatureTrain = np.array(lengthFeatureTrain)
    punctuationFeatureTrain = np.array(punctuationFeatureTrain)
    training_y = np.array(training_y)
    lengthFeatureValid = np.array(lengthFeatureValid)
    punctuationFeatureValid = np.array(punctuationFeatureValid)
    validation_y = np.array(validation_y)
    #Test new feature improvement
    verify_accuracy = findClosedErrors(lengthFeatureTrain,training_y,lengthFeatureTrain,training_y)
    print("Length feature training errors: ", verify_accuracy)
    valid_accuracy = findClosedErrors(lengthFeatureTrain,training_y,lengthFeatureValid,validation_y)
    print("Length feature errors: " , valid_accuracy)

    verify_accuracy = findClosedErrors(punctuationFeatureTrain,training_y,punctuationFeatureTrain,training_y)
    print("Punctuation feature training errors: ", verify_accuracy)
    valid_accuracy = findClosedErrors(punctuationFeatureTrain,training_y,punctuationFeatureValid,validation_y)
    print("Punctuation feature errors: " , valid_accuracy)

def plot(train_features,train_y,valid_features,valid_y):
    train_x = train_features[0]
    valid_x = valid_features[0]

performanceCheck(simpleFeaturesTrain,targetMatrixTrain,simpleFeaturesValid,targetMatrixValid)
print("#################################################################################")
print("#################################################################################")
numFeatureComparison(simpleFeaturesTrain,simpleFeaturesValid,top60FeaturesTrain,top60FeaturesValid,top160FeaturesTrain,top160FeaturesValid,targetMatrixTrain,targetMatrixValid)
print("#################################################################################")
print("#################################################################################")
newFeatureComparison(lengthFeatureTrain,punctuationFeatureTrain,targetMatrixTrain,lengthFeatureValid,punctuationFeatureValid,targetMatrixValid)
