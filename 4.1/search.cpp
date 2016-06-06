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

    map<pair<string, string>, int> chooseMap(string choice)
    {
        map<pair<string, string>, int> temMap;
        if(choice == "Romania")
            for(map<pair<string, string>, int>::iterator iter = mapRomania.begin(); iter != mapRomania.end(); iter++)
                temMap.insert(*iter);
        else if(choice == "HIT")
            for(map<pair<string, string>, int>::iterator iter = mapHIT.begin(); iter != mapHIT.end(); iter++)
                temMap.insert(*iter);
        return temMap;
    }

    vector<string> BFS(string question, string start, string end)
    {
        vector<string> solution;
        map<pair<string, string>, int> pathMap;
        pathMap = chooseMap(question);
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

            if(current == end)
                return solution;

            for(map<pair<string, string>, int>::iterator iter = pathMap.begin(); iter != pathMap.end(); iter++)
                if(iter->first.first == current)
                    if(find(frontier.begin(), frontier.end(), iter->first.second) == frontier.end() &&
                        find(explored.begin(), explored.end(), iter->first.second) == explored.end())
                            frontier.push_back(iter->first.second);
        }
    }

    bool R_DLS(string node, map<pair<string, string>, int> pathMap, vector<string> &solution, int limit, string end, vector<string> explored)
    {
        solution.push_back(node);
        explored.push_back(node);
        if(node == end)
            return true;
        else if (limit == 0)
            return false;
        else
        {
            bool flag;
            for(map<pair<string, string>, int>::iterator iter = pathMap.begin(); iter != pathMap.end(); iter++)
                if(iter->first.first == node && find(explored.begin(), explored.end(), iter->first.second) == explored.end())
                {
                    flag = R_DLS(iter->first.second, pathMap, solution, limit - 1, end, explored);
                    if(flag == true)
                        return true;
                }
            if(flag == false)
                return false;
        }
        return false;
    }

    vector<string> DFS(string question, string start, string end, int limit)
    {
        vector<string> solution;
        vector<string> explored;
        map<pair<string, string>, int> pathMap;
        pathMap = chooseMap(question);
        R_DLS(start, pathMap, solution, limit, end, explored);
        return solution;
    }
};

int main()
{
    Search *mySearch = new Search();

    vector<string> resultBFSRomania = mySearch->BFS("Romania", "Arad", "Bucharest");
    cout<<"BFS:Romania:"<<endl;
    for(vector<string>::iterator iter = resultBFSRomania.begin(); iter != resultBFSRomania.end(); iter++)
        cout<<*iter<<ends;
    cout<<endl;

    vector<string> resultBFSHIT = mySearch->BFS("HIT", "ZhengxinBuilding", "ChengyiBuilding");
    cout<<"BFS:HIT:"<<endl;
    for(vector<string>::iterator iter = resultBFSHIT.begin(); iter != resultBFSHIT.end(); iter++)
        cout<<*iter<<ends;
    cout<<endl;

    vector<string> resultDFSRomania = mySearch->DFS("Romania", "Arad", "Bucharest", 3);
    cout<<"DFS:Romania:"<<endl;
    for(vector<string>::iterator iter = resultDFSRomania.begin(); iter != resultDFSRomania.end(); iter++)
        cout<<*iter<<ends;
    cout<<endl;

    vector<string> resultDFSHIT = mySearch->DFS("HIT", "ZhengxinBuilding", "ChengyiBuilding", 3);
    cout<<"DFS:HIT:"<<endl;
    for(vector<string>::iterator iter = resultDFSHIT.begin(); iter != resultDFSHIT.end(); iter++)
        cout<<*iter<<ends;
    cout<<endl;

    return 0;
}
