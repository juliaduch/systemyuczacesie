import math

def count_values(data,atributeIndex):
    valuesCount = {}
    atributeIndex -=1
    for row in data:
         value = row[atributeIndex]
         if value not in valuesCount.keys():
            valuesCount[value] = 1
         else:
            count = valuesCount.get(value)
            valuesCount[value] = count+1
    return valuesCount, len(valuesCount)

def count_up_down_values(data, atributeIndex, atributeTable:dict):
    valuesCountUp = {key:0 for key in atributeTable.keys()}
    valuesCountDown = {key:0 for key in atributeTable.keys()}
    atributeIndex -=1
    
    for row in data:
        value = row[atributeIndex]
        decisionValue = row[3]
        if decisionValue == 'up':
            count = valuesCountUp.get(value)
            valuesCountUp[value] = count+1         
        elif decisionValue == 'down':
            downCount = valuesCountDown.get(value)
            valuesCountDown[value] = downCount+1
            
    return valuesCountDown, valuesCountUp

def count_entropy(decision_class):
    total_count = sum(decision_class.values())
    entropy = 0
    for count in decision_class.values():
        probability = count / total_count
        if probability > 0:
            entropy -= probability * math.log2(probability)
        else:
            entropy = 0
    return entropy


def count_entropy_for_atribute(atributeValues, countUp, countDown):
    entropies = {}
    for  value in atributeValues.keys():
        entropy = 0
        countUpValues = countUp.get(value)
        countDownValues = countDown.get(value)
        probabilityUp = countUpValues / atributeValues.get(value)
        probabilityDown = countDownValues / atributeValues.get(value)
        probabilities = [probabilityUp, probabilityDown]
        
        for probability in probabilities:
             if probability > 0:
                entropy -= probability * math.log2(probability)
                
        entropies[value] = entropy

    return entropies


def atribute_info(data,atributeCount:dict, atributeIndex):
    
    atrDownCount, atrUpCount = count_up_down_values(data, atributeIndex, atributeCount)
    entropies = count_entropy_for_atribute(atributeCount, atrUpCount, atrDownCount)
    info = 0
    for value in atributeCount:
        info += (atributeCount.get(value)/sum(atributeCount.values())) * entropies.get(value)
        
    return info


def gain(entropy_info, atributeInfo):
    return entropy_info - atributeInfo
