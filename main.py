import csv
import math
from functions import count_entropy,count_up_down_values,count_values, atribute_info, gain
data = []

with open("gielda.txt", 'r', newline='') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        data.append(row)


atr1ValuesCount, atr1Count = count_values(data,1)
atr2ValuesCount, atr2Count = count_values(data,2)
atr3ValuesCount, atr3Count = count_values(data,3)
decisionAtrValuesCount, decisionAtrCount = count_values(data,4)

# print('Atrybut 2', atr2ValuesCount, 'count ',atr2Count) - unique values and their count, count of unique values

atr1DownCount, atr1UpCount = count_up_down_values(data, 1, atr1ValuesCount)
atr2DownCount, atr2UpCount = count_up_down_values(data, 2, atr2ValuesCount)
atr3DownCount, atr3UpCount = count_up_down_values(data, 3, atr3ValuesCount)
decisionAtrDownCount, decisionAtrUpCount = count_up_down_values(data, 4, decisionAtrValuesCount)

# print(atr2DownCount) - how many down decision for each value in atribute 2 column
# print(atr2UpCount)
decisionAtributeEntropy = count_entropy(decisionAtrValuesCount)
print('Entropy for decision atribute', decisionAtributeEntropy)


atr1info = atribute_info(data, atr1ValuesCount,1)
atr2info = atribute_info(data, atr2ValuesCount,2)
atr3info = atribute_info(data, atr3ValuesCount,3)

print('Info for atribute 1 ', atr1info)
print('Info for atribute 2 ', atr2info)
print('Info for atribute 3 ', atr3info)

atr1Gain = gain(decisionAtributeEntropy, atr1info)
atr2Gain = gain(decisionAtributeEntropy, atr2info)
atr3Gain = gain(decisionAtributeEntropy, atr3info)

print('Gain for atribute 1', atr1Gain)
print('Gain for atribute 2', atr2Gain)
print('Gain for atribute 3', atr3Gain)

