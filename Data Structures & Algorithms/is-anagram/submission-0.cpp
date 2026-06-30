#include <set>
#include <string>
using namespace std;

class Solution {
public:
   
    bool isAnagram(string s, string t) {
        if(s.size()!=t.size()){ 
            return false;
        }
        multiset <char> myset; 
        multiset <char> set2; 
        for(int i = 0; i < s.size();i++){ 
            myset.insert(s[i]);
            set2.insert(t[i]);
        }
        if(myset == set2){ 
            return true;
        }
       return false;
    }
};
