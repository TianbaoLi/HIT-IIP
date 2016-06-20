#include<iostream>
#include<fstream>
#include<vector>
#include<map>
#include<cstring>
#include<cstdlib>
#include<algorithm>
using namespace std;

const int MIN_SUP_COUNT = 2;
const int MAX_NODE_AMOUNT = 20;

class FPTreeNode
{
private:
    char item;
    int frequency;
    FPTreeNode* next[MAX_NODE_AMOUNT];
    int nextAmount;

public:
    FPTreeNode(char aItem, char aFrequency)
    {
        item = aItem;
        frequency = aFrequency;
        memset(next, 0, sizeof(next));
        nextAmount = -1;
    }

    char getItem()
    {
        return item;
    }

    int getFrequency()
    {
        return frequency;
    }

    void raiseFrequency(int delta)
    {
        frequency += delta;
    }

    int getNextAmount()
    {
        return nextAmount;
    }

    FPTreeNode* isExisted(char aItem)
    {
        for(int i = 0; i <= nextAmount; i ++)
            if(next[i]->getItem() == aItem)
                return next[i];
        return NULL;
    }

    void addNext(FPTreeNode* node)
    {
        nextAmount += 1;
        next[nextAmount] = node;
    }

    FPTreeNode* getNextNode(int index)
    {
        return next[index];
    }
};

map<char, int> itemAmount;

class ItemNode
{
private:
    char item;
    int amount;
    vector<FPTreeNode> nodeOnTree;

public:
    ItemNode(char aItem, int aAmount)
    {
        item = aItem;
        amount = aAmount;
        nodeOnTree.clear();
    }

    char getItem()
    {
        return item;
    }

    int getAmount()
    {
        return amount;
    }

    void raiseAmount(int delta)
    {
        amount += delta;
    }

    static bool itemNodeCmp(ItemNode a,ItemNode b)
    {
        if(a.getAmount() != b.getAmount())
            return a.getAmount() > b.getAmount();
        else return a.getItem() < b.getItem();
    }

    static bool itemListCmpByFrequency(char a,char b)
    {
        if(itemAmount[a] != itemAmount[b])
            return itemAmount[a] > itemAmount[b];
        else
            return a < b;
    }

    void addTreeNode(FPTreeNode node)
    {
        nodeOnTree.push_back(node);
    }

    void showTreeNode()
    {
        for(vector<FPTreeNode>::iterator iter = nodeOnTree.begin(); iter != nodeOnTree.end(); iter ++)
            cout<<(*iter).getItem()<<ends<<(*iter).getFrequency()<<endl;
    }

};

class FP
{
private:
    vector<vector<char> > items;
    vector<ItemNode> itemHeadList;
    FPTreeNode *FPHead;
    map<char, vector<char> > itemPrefix;
    vector<char> fathersOnBranch;

public:
    FP(string dataFile)
    {
        ifstream inData(dataFile.c_str());
        if(!inData)
        {
            cout<<inData<<ends;
            cout <<"OPEN ERROR!"<<endl;
            return;
        }
        string tmpString;
        char tmpChar;
        while(!inData.eof())
        {
            vector<char> item;
            item.clear();
            inData>>tmpString;
            while(1)
            {
                inData>>tmpChar;
                item.push_back(tmpChar);
                bool itemFound = false;
                for(vector<ItemNode>::iterator iter = itemHeadList.begin(); iter != itemHeadList.end(); iter ++)
                    if((*iter).getItem() == tmpChar)
                    {
                        (*iter).raiseAmount(1);
                        itemFound = true;
                    }
                if(itemFound == false)
                {
                    ItemNode *itemnode = new ItemNode(tmpChar, 1);
                    itemHeadList.push_back(*itemnode);
                }
                inData>>tmpChar;
                if((tmpChar >= '0' && tmpChar <= '9') || inData.eof())
                    break;
            }
            items.push_back(item);
        }
    }

    void MeetSupport(int support)
    {
        for(vector<ItemNode>::iterator iter = itemHeadList.begin(); iter != itemHeadList.end(); iter ++)
        {
            if((*iter).getAmount() < support)
            {
                itemHeadList.erase(iter);
                iter --;
            }
        }
        sort(itemHeadList.begin(), itemHeadList.end(), ItemNode::itemNodeCmp);
        for(vector<ItemNode>::iterator iter = itemHeadList.begin(); iter != itemHeadList.end(); iter ++)
            itemAmount[(*iter).getItem()] = (*iter).getAmount();

        for(vector<vector<char> >::iterator i = items.begin(); i != items.end(); i++)
            for(vector<char>::iterator j = (*i).begin(); j != (*i).end(); j++)
            {
                bool itemExist = false;
                for(vector<ItemNode>::iterator k = itemHeadList.begin(); k != itemHeadList.end(); k++)
                    if(*j == (*k).getItem())
                    {
                        itemExist = true;
                        break;
                    }
                if(itemExist == false)
                {
                    (*i).erase(j);
                    j --;
                }
            }
        for(vector<vector<char> >::iterator i = items.begin(); i != items.end(); i++)
            sort((*i).begin(), (*i).end(), ItemNode::itemListCmpByFrequency);
    }

    FPTreeNode* getFPTreeHead()
    {
        return FPHead;
    }

    FPTreeNode* BuildFPTree()
    {
        FPHead = new FPTreeNode('\0', 0);
        FPTreeNode* current = FPHead;
        for(vector<vector<char> >::iterator i = items.begin(); i != items.end(); i++)
        {
            current = FPHead;
            for(vector<char>::iterator j = (*i).begin(); j != (*i).end(); j++)
            {
                FPTreeNode* next = current->isExisted(*j);
                if(next != NULL)
                {
                    next->raiseFrequency(1);
                    current = next;
                }
                else
                {
                    next = new FPTreeNode(*j, 1);
                    current->addNext(next);
                    current = next;
                }
            }
        }
        return FPHead;
    }

    void BuildItemList(FPTreeNode* current)
    {
        //cout<<current->getItem()<<ends<<current->getFrequency()<<endl;
        for(vector<ItemNode>::iterator iter = itemHeadList.begin(); iter != itemHeadList.end(); iter ++)
            if((*iter).getItem() == current->getItem())
                (*iter).addTreeNode(*current);
        for(int i = 0; i <= current->getNextAmount(); i ++)
            BuildItemList(current->getNextNode(i));
    }

    void ShowItemHeadList()
    {
        for(vector<ItemNode>::iterator iter = itemHeadList.begin(); iter != itemHeadList.end(); iter ++)
            (*iter).showTreeNode();
    }

    void GenPrefix(FPTreeNode* current)
    {
        char currentChar = current->getItem();
        for(vector<char>::iterator iter = fathersOnBranch.begin(); iter != fathersOnBranch.end(); iter ++)
        {
            bool existed = false;
            for(vector<char>::iterator j = itemPrefix[*iter].begin(); j != itemPrefix[*iter].end(); j ++)
                if(currentChar == *j)
                {
                    existed = true;
                    break;
                }
            if(existed == false)
                itemPrefix[*iter].push_back(currentChar);
        }
        for(int i = 0; i <= current->getNextAmount(); i ++)
        {
            fathersOnBranch.push_back(current->getItem());
            GenPrefix(current->getNextNode(i));
            fathersOnBranch.pop_back();
        }
    }

    void fun()
    {
        for(map<char, vector<char> >::iterator i = itemPrefix.begin(); i != itemPrefix.end(); i ++)
        {
            cout<<i->first<<":"<<endl;
            for(vector<char>::iterator j = itemPrefix[i->first].begin(); j != itemPrefix[i->first].end(); j ++)
                cout<<*j<<ends;
            cout<<endl;
        }
    }
};

int main()
{
    FP *fp = new FP("PPTexample.dat");
    fp->MeetSupport(MIN_SUP_COUNT);
    fp->BuildFPTree();
    fp->BuildItemList(fp->getFPTreeHead());
    //fp->ShowItemHeadList();
    fp->GenPrefix(fp->getFPTreeHead());
    fp->fun();
    return 0;
}
