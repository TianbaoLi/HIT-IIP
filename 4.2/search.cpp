#include<iostream>
#include<fstream>
#include<map>
#include<algorithm>
#include<vector>
#include<stack>
using namespace std;

const int NODEN = 30;

class Search
{
private:
    map<pair<string, string>, int> mapRomania;
    map<pair<string, string>, int> mapHIT;
    map<string, int> SLDRomania;
    map<string, int> SLDHIT;

public:
    Search()
    {
        ifstream inRomania("Romania.dat");
        ifstream inHIT("HIT.dat");
        ifstream inSLDRomania("SLD_Romania.dat");
        ifstream inSLDHIT("SLD_HIT.dat");
        string node1, node2;
        int len;
        while(!inRomania.eof())
        {
            inRomania>>node1>>node2>>len;
            mapRomania[pair<string, string>(node1, node2)] = len;
            mapRomania[pair<string, string>(node2, node1)] = len;
        }
        while(!inHIT.eof())
        {
            inHIT>>node1>>node2>>len;
            mapHIT[pair<string, string>(node1, node2)] = len;
            mapHIT[pair<string, string>(node2, node1)] = len;
        }
        while(!inSLDRomania.eof())
        {
            inSLDRomania>>node1>>len;
            SLDRomania[node1] = len;
        }
        while(!inSLDHIT.eof())
        {
            inSLDHIT>>node1>>len;
            SLDHIT[node1] = len;
        }
    }

    void chooseMap(string choice, map<pair<string, string>, int> &temMap, map<string, int> &tmpSLD)
    {
        if(choice == "Romania")
        {
            for(map<pair<string, string>, int>::iterator iter = mapRomania.begin(); iter != mapRomania.end(); iter++)
                temMap.insert(*iter);
            for(map<string, int>::iterator iter = SLDRomania.begin(); iter != SLDRomania.end(); iter++)
                tmpSLD.insert(*iter);
        }
        else if(choice == "HIT")
        {
            for(map<pair<string, string>, int>::iterator iter = mapHIT.begin(); iter != mapHIT.end(); iter++)
                temMap.insert(*iter);
            for(map<string, int>::iterator iter = SLDHIT.begin(); iter != SLDHIT.end(); iter++)
                tmpSLD.insert(*iter);
        }
    }

    vector<string> ASearch(string question, string start, string end)
    {
        vector<string> solution;
        map<pair<string, string>, int> pathMap;
        map<string, int> pathSLD;
        chooseMap(question, pathMap, pathSLD);
        map<string, int> frontier;
        vector<string> explored;
        frontier[start] = 0;

        while(1)
        {
            if(frontier.empty())
                return solution;

            for(map<string, int>::iterator iter = frontier.begin(); iter != frontier.end(); iter++)
                iter->second += pathSLD[iter->first];
            map<string, int>::iterator minNode = frontier.begin();
            for(map<string, int>::iterator iter = frontier.begin(); iter != frontier.end(); iter++)
                if(iter->second < minNode->second)
                    minNode = iter;
            string current = minNode->first;
            int d = minNode->second - pathSLD[minNode->first];
            frontier.erase(minNode);
            for(map<string, int>::iterator iter = frontier.begin(); iter != frontier.end(); iter++)
                iter->second -= pathSLD[iter->first];
            explored.push_back(current);
            solution.push_back(current);

            if(current == end)
                return solution;

            for(map<pair<string, string>, int>::iterator iter = pathMap.begin(); iter != pathMap.end(); iter++)
                if(iter->first.first == current)
                {
                    if(frontier.find(iter->first.second) == frontier.end() &&
                        find(explored.begin(), explored.end(), iter->first.second) == explored.end())
                            frontier[iter->first.second] = d + iter->second;
                    else
                    {
                        map<string, int>::iterator child = frontier.find(iter->first.second);
                        if(child != frontier.end() && child->second > d + iter->second)
                            child->second = d + iter->second;
                    }
                }
        }
    }

    vector<string> ATraversal(string question, string start)
    {
        vector<string> solution;
        map<pair<string, string>, int> pathMap;
        map<string, int> pathSLD;
        chooseMap(question, pathMap, pathSLD);
        map<string, int> frontier;
        vector<string> explored;
        frontier[start] = 0;

        while(1)
        {
            if(frontier.empty())
                return solution;

            for(map<string, int>::iterator iter = frontier.begin(); iter != frontier.end(); iter++)
                iter->second += pathSLD[iter->first];
            map<string, int>::iterator minNode = frontier.begin();
            for(map<string, int>::iterator iter = frontier.begin(); iter != frontier.end(); iter++)
                if(iter->second < minNode->second)
                    minNode = iter;
            string current = minNode->first;
            int d = minNode->second - pathSLD[minNode->first];
            frontier.erase(minNode);
            for(map<string, int>::iterator iter = frontier.begin(); iter != frontier.end(); iter++)
                iter->second -= pathSLD[iter->first];
            explored.push_back(current);
            solution.push_back(current);

            if(explored.size() == pathSLD.size())
                return solution;

            for(map<pair<string, string>, int>::iterator iter = pathMap.begin(); iter != pathMap.end(); iter++)
                if(iter->first.first == current)
                {
                    if(frontier.find(iter->first.second) == frontier.end() &&
                        find(explored.begin(), explored.end(), iter->first.second) == explored.end())
                            frontier[iter->first.second] = d + iter->second;
                    else
                    {
                        map<string, int>::iterator child = frontier.find(iter->first.second);
                        if(child != frontier.end() && child->second > d + iter->second)
                            child->second = d + iter->second;
                    }
                }
        }
    }
};

int main()
{
    Search *mySearch = new Search();

    vector<string> resultASearchRomania1 = mySearch->ASearch("Romania", "Arad", "Bucharest");
    cout<<"ASearch:Romania:Arad-Bucharest"<<endl;
    for(vector<string>::iterator iter = resultASearchRomania1.begin(); iter != resultASearchRomania1.end(); iter++)
        cout<<*iter<<ends;
    cout<<endl<<endl;

    vector<string> resultASearchRomania2 = mySearch->ASearch("Romania", "Craiova", "Bucharest");
    cout<<"ASearch:Romania:Craiova-Bucharest"<<endl;
    for(vector<string>::iterator iter = resultASearchRomania2.begin(); iter != resultASearchRomania2.end(); iter++)
        cout<<*iter<<ends;
    cout<<endl<<endl;

    vector<string> resultASearchRomania3 = mySearch->ASearch("Romania", "Lugoj", "Bucharest");
    cout<<"ASearch:Romania:Lugoj-Bucharest"<<endl;
    for(vector<string>::iterator iter = resultASearchRomania3.begin(); iter != resultASearchRomania3.end(); iter++)
        cout<<*iter<<ends;
    cout<<endl<<endl;

    vector<string> resultASearchHIT = mySearch->ASearch("HIT", "ZhengxinBuilding", "ChengyiBuilding");
    cout<<"ASearch:HIT:ZhengxinBuilding-ChengyiBuilding"<<endl;
    for(vector<string>::iterator iter = resultASearchHIT.begin(); iter != resultASearchHIT.end(); iter++)
        cout<<*iter<<ends;
    cout<<endl<<endl;

    vector<string> resultATraversalRomania = mySearch->ATraversal("Romania", "Arad");
    cout<<"ATraversal:Romania:Arad"<<endl;
    for(vector<string>::iterator iter = resultATraversalRomania.begin(); iter != resultATraversalRomania.end(); iter++)
        cout<<*iter<<ends;
    cout<<endl<<endl;
    return 0;
}
