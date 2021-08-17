[Link](https://leetcode.com/problems/implement-trie-prefix-tree/)<br/>
# C++ Version
Idea: to create a node structure with an array of 26 slots of pointer pointing to the next possible nodes with a boolean value to see if the currrent node marks 
an end of a word. So to insert a word, we just create new nodes from the first character to the last character and add new nodes. To search, we just need to traverse
the trie and, depend on the situation, check if we want certain character to end at certain node.
```c++
class Trie {
public:
    
    class Node{
    public:
        Node(char curr){
            c = curr;
            isEnd = false;
            for(int i = 0; i < 26; i++)
            {
                child[i] = nullptr;
            }
        }
        void setEnd(){isEnd = true;}
        Node* child[26];
       
        char c;
        bool isEnd;
    };
    
    Node * root;
    
    /** Initialize your data structure here. */
    Trie() {
        root = new Node('\0');
    }
    
    
    /** Inserts a word into the trie. */
    void insert(string word) {
        Node * temp = root;
        for (int i = 0; i < word.size(); i++)
        {
            if(temp->child[word[i]-'a'] == nullptr) // we only create a new node if the next character doesn't exist
            {
                temp->child[word[i]-'a'] = new Node(word[i]);
            }
            temp = temp->child[word[i]-'a'];
        }
        temp->setEnd();
    }
    
    /** Returns if the word is in the trie. */
    bool search(string word) {
        Node* search = searchNode(word, root);
        return search != nullptr && search->isEnd;
    }
    
    /** Returns if there is any word in the trie that starts with the given prefix. */
    bool startsWith(string prefix) {
        Node* res = searchNode(prefix,root);
        return res != nullptr;
    }
    
    // a helper function that we can use for search and startWith
    Node* searchNode(string  word, Node* root)
    {
        Node * temp = root;
        for (int i = 0; i < word.size(); i++)
        {
            if(temp->child[word[i]-'a'] == nullptr)
            {
                return nullptr;
            }
            temp = temp->child[word[i]-'a'];
        }
        return temp;
    } 
};
```
# Python Version
```python
class Node:
    def __init__(self,val = '0'):
        self.val = val
        self.children = [None]*26
        self.isEnd = False
    def setEnd(self):
        self.isEnd = True

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()
        
    def find(self,word):
        curr = self.root
        wordLen = len(word)
        for i in range(wordLen):
            index = ord(word[i])-ord('a')
            if curr.children[index] and curr.children[index].val == word[i]:
                curr = curr.children[index]
                continue
            else:
                return None
        return curr

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        curr = self.root
        for c in word:
            index = ord(c)-ord('a')
            if curr.children[index] == None:
                curr.children[index] = Node(c)
            curr = curr.children[ord(c)-ord('a')]
        curr.setEnd()

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        end = self.find(word)
        if end:
            return end.isEnd
        else:
            return False
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        return self.find(prefix) != None
```
