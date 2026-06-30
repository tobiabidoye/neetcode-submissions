#include <set>
class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        set<int> myset;
        for(int i = 0; i < nums.size(); i++){ 
            myset.insert(nums[i]);
        }
       if(myset.size() < nums.size()){ 
       //set does not allow the storage of dupe values
       //if the size is smaller then there were dupe values
       //it returns true in this case
        return true;
       }
       return false;
    }
};
