#include <iostream>
#include <cmath>

using namespace std;

double show_logic(int n, int r) {
    if (n<0) {
        return 0;
    }
    return pow(r,n)+show_logic(n-1,r);
}

int main() {
    int n = 0;
    int r = 2;
    cout << "Enter n : ";
    cin>>n;

    double result = show_logic(n,r);
    cout << result << endl;




    return 0;
}