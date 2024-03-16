# from functions import count_attribute_decision_values
# import math





# def count_entropy_for_attribute(attribute_values_counts, decision_values):
#     entropies = {}

#     for value, counts in attribute_values_counts.items():
#         entropy = 0
#         total_count = sum(counts.values())

#         if total_count > 0:
#             probabilities = [counts[decision] / total_count for decision in decision_values]

#             for probability in probabilities:
#                 if probability > 0:
#                     entropy -= probability * math.log2(probability)

#         entropies[value] = entropy

#     return entropies





# def atribute_info(data,atributeCount:dict, atributeIndex, decisionValues, decisionIndex):
    
#     decisionValueCountForAttribute = count_attribute_decision_values(data, atributeIndex,decisionIndex, decisionValues)
#     entropies = count_entropy_for_attribute(decisionValueCountForAttribute,decisionValues)
#     print('dec value for atr', decisionValueCountForAttribute)
#     print('entopies', entropies)
#     print('atribute', atributeCount)
#     info = 0
#     for value in atributeCount:
#         info += (atributeCount.get(value)/sum(atributeCount.values())) * entropies.get(value)
        
#     return info


# def gain(entropy_info, atributeInfo):
#     return entropy_info - atributeInfo



# def gain(entropy_info, atributeInfo):
#     return entropy_info - atributeInfo
