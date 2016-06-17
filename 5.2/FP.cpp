#include<iostream>
#include<fstream>
#include<vector>
#include<cstdlib>
using namespace std;

class FPNode
{
private:
    char item;
    int frequency;
    vector<FPNode*> next;

public:
    FPNode(char aItem, char aFrequency)
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

class itemNode
{
private:
    char item;
    itemNode *next;

public:
    itemNode(char aItem)
    {
        item = aItem;
    }

    char getItem()
    {
        return item;
    }
};

class FP
{
private:
    vector<vector<char> > items;
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
            //cout<<tmpString<<endl;
            while(1)
            {
                inData>>tmpChar;
                item.push_back(tmpChar);
                //cout<<tmpChar<<endl;
                //system("pause");
                inData>>tmpChar;
                //cout<<"!!!"<<tmpChar<<endl;
                if((tmpChar >= '0' && tmpChar <= '9') || inData.eof())
                    break;
            }
            items.push_back(item);
            for(vector<char>::iterator iter = item.begin(); iter != item.end(); iter ++)
                cout<<(*iter)<<ends;
            cout<<"******"<<endl;
        }
        for(vector<vector<char> >::iterator iter = items.begin(); iter != items.end(); iter ++)
            cout<<(*iter).size();
    }
};

int main()
{
    FP *fp = new FP("PPTexample.dat");
    return 0;
}
