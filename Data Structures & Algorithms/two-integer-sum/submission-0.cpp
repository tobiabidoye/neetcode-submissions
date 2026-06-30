#include <unordered_map>
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
      unordered_multimap <int, int> mymap;
      vector <int> myvec;
      for(int i = 0; i < nums.size(); i++){ 
        mymap.insert(make_pair(nums[i],i));
      } 
      for(const auto&elem: mymap){ 
        int target2 = target - elem.first;
       
            auto it = mymap.find(target2);
            // need to make sure we are not dereferencing a pointer
            // that doesn't exist
            if(it != mymap.end()){
            if(elem.second < it->second){ 
                 myvec.push_back(elem.second);
                 myvec.push_back(it->second);
                 return myvec;
            }
            }
      }
      return myvec;
    }

};
