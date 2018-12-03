import re
def clean_word(word):
    clean = re.sub('\W+', '', word.lower())
    if not clean:
        return None
    return clean

def addtowordlist(word,list):
    if word in list:
        list[word] +=1
    else:
        list[word] = 1


def openFileWordByWord(file):
    list = dict()
    with open(file,'r') as f:
        word = ""
        for c in f.read():
            if c is not " " and c is not "\n":
                word += c
            elif c is " ":
                addtowordlist(clean_word(word),list)
                word = ""
    return list


def frequencyDictToFile(file,dict):
    with open(file,'w') as f:
        for item in dict:
            f.write(str(item) + ":" + str(dict[item]) + "\n")

frequencyDictToFile("fdict.txt",openFileWordByWord("text.txt"))

class TrieNode:
    def __init__(self,value=None, n = 0):
        self.n = n
        self.d = value
    def __repr__(self, n=''):
        res = ''
        if self.n > 0:
            res += n + ":" + str(self.n) + '\n'
        
        if self.d is not None:
            for key in sorted(self.d):
                res += self.d[key].__repr__(n + key)
        return res
    
    def insert(self,word):
        if word:
            if self.d:
                if word[0] in self.d.keys():
                    self.d[word[0]].insert(word[1:])
                else:
                    self.d[word[0]] = TrieNode()
                    self.d[word[0]].insert(word[1:])
            else:
                self.d = {word[0]: TrieNode()}
                self.d[word[0]].insert(word[1:])
            
        else:
            self.n +=1
class Trie:
    def __init__(self):
        self.root = None

    def __repr__(self):
        if self.root:
            return str(self.root)
        return "empty trie"
    
    def insert(self,word):
        if self.root:
            self.root.insert(word)
        else:
            self.root = TrieNode()
            self.root.insert(word)



root_TrieNode = Trie()


for word in openFileWordByWord("text.txt"):
    root_TrieNode.insert(clean_word(word))

def trie_to_file(trie, filename):
    file = open(filename, 'w')
    file.write(str(trie))
    file.close()    
trie_to_file(root_TrieNode,"trie.txt")