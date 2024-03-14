import csv
from functions import count_values, count_attribute_decision_values,count_entropy, count_entropy_for_attribute, atribute_info, gain, gain_ratio


data = []

with open("gielda.txt", 'r', newline='') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        data.append(row)


atr1ValuesCount, atr1Count = count_values(data,0)
atr2ValuesCount, atr2Count = count_values(data,1)
atr3ValuesCount, atr3Count = count_values(data,2)
decisionAtrValuesCount, decisionAtrCount = count_values(data,3)

decisionAtributeValues = decisionAtrValuesCount.keys()

print('Atrybut 2', atr2ValuesCount, 'count ',atr2Count) #- unique values and their count, count of unique values

atr1DecisionValuecount = count_attribute_decision_values(data, 0, 3, decisionAtributeValues)
atr2DecisionValuecount = count_attribute_decision_values(data, 1, 3, decisionAtributeValues)
atr3DecisionValuecount = count_attribute_decision_values(data, 2, 3, decisionAtributeValues)

print('Decision values count for atr 2', atr2DecisionValuecount)


decisionAtributeEntropy = count_entropy(decisionAtrValuesCount)
print('Entropy for decision atribute', decisionAtributeEntropy)



print('Entropy for attribute 1', count_entropy_for_attribute(atr1DecisionValuecount, decisionAtributeValues))
print('Entropy for attribute 2', count_entropy_for_attribute(atr2DecisionValuecount, decisionAtributeValues))
print('Entropy for attribute 3', count_entropy_for_attribute(atr3DecisionValuecount, decisionAtributeValues))


atr1info = atribute_info(data, atr1ValuesCount, 0, decisionAtributeValues, 3)
atr2info = atribute_info(data, atr2ValuesCount, 1, decisionAtributeValues, 3)
atr3info = atribute_info(data, atr3ValuesCount, 2, decisionAtributeValues, 3)

print('Info for atribute 1 ', atr1info)
print('Info for atribute 2 ', atr2info)
print('Info for atribute 3 ', atr3info)

atr1Gain = gain(decisionAtributeEntropy, atr1info)
atr2Gain = gain(decisionAtributeEntropy, atr2info)
atr3Gain = gain(decisionAtributeEntropy, atr3info)

print('Gain for atribute 1', atr1Gain)
print('Gain for atribute 2', atr2Gain)
print('Gain for atribute 3', atr3Gain)

atr1GainRatio = gain_ratio(data, atr1ValuesCount,decisionAtrValuesCount, 0, 3)
atr2GainRatio = gain_ratio(data, atr2ValuesCount,decisionAtrValuesCount, 1, 3)
atr3GainRatio = gain_ratio(data, atr3ValuesCount,decisionAtrValuesCount, 2, 3)

print('Gain ratio for atribute 1', atr1GainRatio)
print('Gain ratio for atribute 2', atr2GainRatio)
print('Gain ratio for atribute 3', atr3GainRatio)
