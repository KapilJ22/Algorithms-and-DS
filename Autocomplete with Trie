class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.isWord = False
        self.children = {}

    def insert(self, char):
        ## Add a child node in this Trie
        self.children[char] = TrieNode()

    def suffixes(self, suffix=''):
        ## Recursive function that collects the suffix for
        ## all complete words below this point
        list = []
        if self.isWord:
            return list

        for key in self.children.keys():
            i = 0
            mylist = ['']
            mylist = self.children[key].suffixes()
            if not mylist:
                mylist = ['']
            for s in mylist:
            # remove '.'  that was added to indicate end of word
                if key == '.':
                    key = ''
                mylist[i] = key + s
                i = i + 1
            list += mylist
        return list


## The Trie itself containing the root node and insert/find functions
class Trie(object):
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        current = self.root
        i = 0
        for ch in word:
            if ch not in current.children:
                current.insert(ch)

            current = current.children[ch]
            # add '.' to indicate end of word
            if i == len(word) - 1:
                #  current.isWord = True
                ch = '.'
                current.insert(ch)
                current = current.children[ch]
                current.isWord = True
            i += 1

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        current = self.root
        for ch in prefix:
            if ch in current.children:
                current = current.children[ch]
            else:
                return False
        return current


def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            return (','.join(prefixNode.suffixes()))
        else:
            return (prefix + " not found")
    else:
        return ('')

# Tests:
MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)
print(f("tr") == "ie,igger,igonometry,ipod")
print(f("tb") == "tb not found")
print(f('') == "")

MyTrie = Trie()
wordList = []
for word in wordList:
    MyTrie.insert(word)

print(f('') == '')
print(f("tb") == "tb not found")
