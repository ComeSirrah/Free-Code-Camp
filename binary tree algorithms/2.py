# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None

#     def retrieve_data(self):
#         value = self.val
#         left = self.left
#         right = self.right
#
#         return value, left, right
#
#     @staticmethod
#     def depth_first(node=None):
#         if node:
#             tree_values = ""
#             stack = [node]
#             child_counter = 0
#             while stack:
#                 has_child = False
#                 current = stack.pop()
#                 tree_values += f'({current.val}'
#                 if current.right:
#                     stack.append(current.right)
#                     has_child = True
#                 if current.left:
#                     stack.append(current.left)
#                     has_child = True
#                 if has_child:
#                     child_counter += 1
#                 if has_child and not current.left:
#                     tree_values += '()('
#                 if not has_child:
#                     tree_values += ')' * child_counter
#                     child_counter = 0
#             tree_values += ')'
#             tree_values = tree_values.lstrip('(')
#             return tree_values
#
#
# if __name__ == '__main__':
#     a = Node('a')
#     b = Node('b')
#     c = Node('c')
#     d = Node('d')
#
#     a.left = b
#     a.right = c
#     b.left = d
#
#     print(Node.depth_first(None))

wordz = "once upon a midnight dreary whilst i pondered weak and weary"
let = "ad"


def canBeTypedWords(text: str, brokenLetters: str) -> int:
    applicable_words = text.split(' ')
    for char in brokenLetters:
        print('='*80)
        print(applicable_words)
        print(char)
        print('='*80)
        for word in applicable_words[::-1]:
            print(word)
            if char in word:
                print(f'deleting {word}: {char} found.')
                applicable_words.remove(word)
    return len(applicable_words) - 1


print(canBeTypedWords(wordz, let))
