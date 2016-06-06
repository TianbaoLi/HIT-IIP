#include<iostream>
#include<fstream>
#include<map>
#include<algorithm>
#include<vector>
using namespace std;

const int NODEN = 30;

class Search
{
private:
    map<pair<string, string>, int> mapRomania;
    map<pair<string, string>, int> mapHIT;

public:
    Search()
    {
        ifstream inRomania("Romania.dat");
        ifstream inHIT("HIT.dat");
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
    }

    vector<string> BFS(string question, string start)
    {
        vector<string> solution;
        map<pair<string, string>, int> pathMap;
        if(question == "Romania")
            for(map<pair<string, string>, int>::iterator iter = mapRomania.begin(); iter != mapRomania.end(); iter++)
                pathMap.insert(*iter);
        else if(question == "HIT")
            for(map<pair<string, string>, int>::iterator iter = mapHIT.begin(); iter != mapHIT.end(); iter++)
                pathMap.insert(*iter);
        else
            return solution;

        vector<string> frontier;
        frontier.push_back(start);
        vector<string> explored;

        while(1)
        {
            if(frontier.empty())
                return solution;
            string current = *(frontier.begin());
            frontier.erase(frontier.begin());
            explored.push_back(current);
            solution.push_back(current);

            for(map<pair<string, string>, int>::iterator iter = pathMap.begin(); iter != pathMap.end(); iter++)
                if(iter->first.first == current)
                    if(find(frontier.begin(), frontier.end(), iter->first.second) == frontier.end() &&
                        find(explored.begin(), explored.end(), iter->first.second) == explored.end())

                            frontier.push_back(iter->first.second);
        }
    }
};

int main()
{
    Search *mySearch = new Search();

    vector<string> resultBFSRomania = mySearch->BFS("Romania", "Arad");
    cout<<"BFS:Romania:"<<endl;
    for(vector<string>::iterator iter = resultBFSRomania.begin(); iter != resultBFSRomania.end(); iter++)
        cout<<*iter<<ends;
    cout<<endl;

    vector<string> resultBFSHIT = mySearch->BFS("HIT", "ZhengxinBuilding");
    cout<<"BFS:HIT:"<<endl;
    for(vector<string>::iterator iter = resultBFSHIT.begin(); iter != resultBFSHIT.end(); iter++)
        cout<<*iter<<ends;
    cout<<endl;

    return 0;
}
