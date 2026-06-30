#include <unordered_map> 

using namespace std;

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector <vector<string>> myvec; 
        if(strs.size()==1){ 
            myvec.push_back(strs);
            return myvec;
        }
        unordered_map<string, vector<string>> mymap;
        for(auto elem: strs){ 
            string newstr = elem;
            sort(newstr.begin(), newstr.end());
            mymap[newstr].push_back(elem);
        }

        for(auto elem: mymap){ 
            myvec.push_back(elem.second);
        }
        return myvec;
    }
};
