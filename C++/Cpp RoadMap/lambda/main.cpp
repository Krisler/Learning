#include <iostream>

using namespace std;

int main() {
    int expiresIndays = 45;
    int multiplier = 3;

    //Lambda function with capture-by-value
    auto times = [multiplier](int a) {
        return a * multiplier;
    };
    int result = times(5); // result = 15
    
    //Lambda function with capture-by-reference
    auto updateDays = [&expiresIndays](int newDays) {
        expiresIndays = newDays;
        return expiresIndays;
    };
    int results2 = updateDays(30);

    cout<<"Result: "<<result<<endl<<"Result2: "<<results2<<endl;

    return 0;
}