class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        vector<vector<int>> myvec(nums.size() + 1);
        unordered_map <int, int> mymap;
        for(int i = 0; i < nums.size(); i++){ 
            mymap[nums[i]]++;
        }
        for(auto & elem: mymap){ 
            myvec[elem.second].push_back(elem.first);
        }
        vector<int> result;
        for(int i = myvec.size() - 1; i > 0; i--){ 
            for(int j = 0; j < myvec[i].size(); j++){ 
                result.push_back(myvec[i][j]); 
                if(result.size() == k){ 
                    return result;
                }
            }
        }
        return {};
    }
};
