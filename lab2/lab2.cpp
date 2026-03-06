#include <iostream>

using namespace std;
int main() {
    cout << "Please enter a positive integer greater than 9: " << endl;
    int x = 0;
    cin >> x;
    int count = 0;
    while (x > 9) {
        cout << x << " -> ";
        int digitSum = 0;
        int tempNumber = x;
        while (tempNumber > 0) {
            digitSum += tempNumber % 10;
            tempNumber /= 10;
        }
        x = digitSum;
        count++;
    }
    cout << x << endl;
    cout << "Final Value : " << x << endl;
    cout << "Total Steps: " <<count << endl;


    int number = 0;
    string a = "";
    cout << "Enter a number: ";
    cin >> number;
    while (number < 10 || number > 100) {
        cout << "Enter a number: ";
        cin >> number;
    }
    for (int i = 1; i < number+1; i++) {
        a = "";
        if (i%7 == 0) {
            cout << i << " is skipped"<<endl;
            continue;
        }
        if (i%5 == 0 && i%3 == 0) {
            a = "FizzBuzz";
        }else if (i%3 == 0) {
            a = "Fizz";
        }else if (i%5 == 0) {
            a = "Buzz";
        }else {
            cout << i << endl;
            continue;
        }
        cout << a << endl;
    }

    int m = 0;
    cout<<"Enter a Number: ";
    cin >> m;
    while (m > 9 || m < 3) {
        cout<<"Enter a Number: ";
        cin >> m;
    }

    for (int i = 1; i < (m*2) ; i++) {
        int k = m - abs(m-i);
        for (int j = 1; j < k+1 ; j++) {
            cout<<j;
        }
        cout<<endl;
    }
    return 0;




}