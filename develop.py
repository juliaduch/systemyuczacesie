import csv
from functions import *


class TreeNode:
    def __init__(self, attribute_index=None, decision=None, branches=None):
        self.attribute_index = attribute_index
        self.decision = decision
        self.branches = branches if branches else {}


data = []

with open("gielda.txt", 'r', newline='') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        data.append(row)


attributes = [0, 1, 2]  
decision_attribute_index = 3


def build_tree(data, attributes, decision_attribute_index, depth=0):
    decision_values, _ = count_values(data, decision_attribute_index)
    if len(decision_values) == 1:  # If all decisions are the same, return a leaf node
        majority_decision = max(decision_values, key=decision_values.get)
        print('  ' * depth, 'Decision:', majority_decision)
        return TreeNode(decision=majority_decision)
    if not attributes:  # If there are no attributes left, return the majority decision
        majority_decision = max(decision_values, key=decision_values.get)
        print('  ' * depth, 'Decision:', majority_decision)
        return TreeNode(decision=majority_decision)
    best_attribute_index = get_best_split(data, attributes, decision_attribute_index)
    if best_attribute_index is None:  # If no best attribute found, return the majority decision
        majority_decision = max(decision_values, key=decision_values.get)
        print('  ' * depth, 'Decision:', majority_decision)
        return TreeNode(decision=majority_decision)
    branches = {}
    attribute_values, _ = count_values(data, best_attribute_index)
    print('  ' * depth, 'Attribute Index:', best_attribute_index)
    for value in attribute_values:
        subset = [row for row in data if row[best_attribute_index] == value]
        if not subset:  # If subset is empty, return the majority decision
            majority_decision = max(decision_values, key=decision_values.get)
            print('  ' * (depth + 1), 'Value:', value, 'Decision:', majority_decision)
            branches[value] = TreeNode(decision=majority_decision)
        else:
            subset_attributes = [attribute for attribute in attributes if attribute != best_attribute_index]
            print('  ' * (depth + 1), 'Value:', value)
            branches[value] = build_tree(subset, subset_attributes, decision_attribute_index, depth=depth+2)
    return TreeNode(attribute_index=best_attribute_index, branches=branches)


tree = build_tree(data, attributes, decision_attribute_index)
