#include <iostream>
#include <unordered_map>
#include <vector>
using namespace std;

vector<int> TwoSum(vector<int> arr,int target) 
{
    unordered_map<int,int> store;
    for(int i = 0; i < arr.size();i++) {
        int rem = target - arr[i];
        if((rem!=0) && (store.find(rem)!=store.end())) {
            vector<int> c = {store.at(rem),i};
            return c;
        }
        else {
            store[arr[i]] = i;
        }

        
    }
    return {0,0};
    
}

int main() {
    vector<int> arr{1,-2,5,10};
    int target =-1;
    vector<int> p = TwoSum(arr,target);
    cout<<"["<<p[0]<<","<<p[1]<<"]"<<endl;

    return 0;

}