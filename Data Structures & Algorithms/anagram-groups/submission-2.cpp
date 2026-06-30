class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> mymap;
        vector <vector<string>> myvec;
        string mystring;
        //since we used a hashmap 
        for(int i = 0; i < strs.size(); i++){ 
            mystring = strs[i]; 
            sort(mystring.begin(),mystring.end());
            mymap[mystring].push_back(strs[i]);
            //sorting string in o(nlogn)
            //pushing back into .second for map key
        }

        for(auto &elem: mymap){ 
            myvec.push_back(elem.second);
        }
        return myvec;

    }
};
