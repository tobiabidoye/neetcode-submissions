class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
       unordered_map <int, int> mymap; 
       vector <vector<int>> myvec(nums.size() + 1);
       //loop through nums array append items to hashmap count frequency
       for(int i = 0; i < nums.size(); i++){ 
            mymap[nums[i]]++;  //counting occurences of number count in hashmap     
       }

       for(auto &elem: mymap){ 
            //all elements with the same count will be added to 2d array
            myvec[elem.second].push_back(elem.first);
        }

        vector <int> result;
        for(int i = myvec.size()-1; i > 0; i--){ 
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
