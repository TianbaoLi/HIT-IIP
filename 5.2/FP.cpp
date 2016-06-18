#include<iostream>
#include<fstream>
#include<vector>
#include<cstdlib>
#include<algorithm>
using namespace std;

const int MIN_SUP_COUNT = 3;

class FPTreeNode
{
private:
    char item;
    int frequency;
    vector<FPTreeNode*> next;

public:
    FPTreeNode(char aItem, char aFrequency)
    {
        item = aItem;
        frequency = aFrequency;
        next.clear();
    }

    char getItem()
    {
        return item;
    }

    int getFrequency()
    {
        return frequency;
    }
};

class ItemNode
{
private:
    char item;
    int amount;
    ItemNode *next;

public:
    ItemNode(char aItem, int aAmount)
    {
        item = aItem;
        amount = aAmount;
        next = NULL;
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
};

class FP
{
private:
    vector<vector<char> > items;
    vector<ItemNode> itemHeadList;
public:
    FP(string dataFile)
    {
        ifstream inData(dataFile.c_str());
        cout<<dataFile.c_str()<<endl;
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
            cout<<(*iter).getItem()<<ends<<(*iter).getAmount()<<endl;
    }
};

int main()
{
    FP *fp = new FP("PPTexample.dat");
    fp->MeetSupport(MIN_SUP_COUNT);
    return 0;
}
