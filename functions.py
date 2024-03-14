import math

def count_values(data,atributeIndex):
    valuesCount = {}
    for row in data:
         value = row[atributeIndex]
         if value not in valuesCount.keys():
            valuesCount[value] = 1
         else:
            count = valuesCount.get(value)
            valuesCount[value] = count+1
    return valuesCount, len(valuesCount)


def count_attribute_decision_values(data, attribute_index, decision_index, possible_values):
    values_count = {key: {decision: 0 for decision in possible_values} for key in set(row[attribute_index] for row in data)}
    
    for row in data:
        attribute_value = row[attribute_index]
        decision_value = row[decision_index]
        values_count[attribute_value][decision_value] += 1
    
    return values_count


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


def count_entropy_for_attribute(attribute_values_counts, decision_values):
    entropies = {}

    for value, counts in attribute_values_counts.items():
        entropy = 0
        total_count = sum(counts.values())

        if total_count > 0:
            probabilities = [counts[decision] / total_count for decision in decision_values]

            for probability in probabilities:
                if probability > 0:
                    entropy -= probability * math.log2(probability)

        entropies[value] = entropy

    return entropies


def atribute_info(data,atributeCount:dict, atributeIndex, decisionValues, decisionIndex):
    
    decisionValueCountForAttribute = count_attribute_decision_values(data, atributeIndex,decisionIndex, decisionValues)
    entropies = count_entropy_for_attribute(decisionValueCountForAttribute,decisionValues)
    print('dec value for atr', decisionValueCountForAttribute)
    print('entopies', entropies)
    print('atribute', atributeCount)
    info = 0
    for value in atributeCount:
        info += (atributeCount.get(value)/sum(atributeCount.values())) * entropies.get(value)
        
    return info


def gain(entropy_info, atributeInfo):
    return entropy_info - atributeInfo

def gain_ratio(data, attributeValues, decisionAtrValuesCount, attributeIndex, decisionAttributeIndex ):
    decisionAtributeEntropy = count_entropy(decisionAtrValuesCount)
    attributeInfo = atribute_info(data, attributeValues, attributeIndex, decisionAtrValuesCount, decisionAttributeIndex)
    
    gainValue = gain(decisionAtributeEntropy, attributeInfo)
    splitInfo = count_entropy(attributeValues)
    gain_ratio = gainValue/splitInfo
    
    
    
    return gain_ratio 