//
// Created by ML201 on 2/27/2026.
//

#include "coordinate_geometry.h"


#include <iostream>
#include <cmath>
using namespace std;

int main() {

    int first_x;
    int first_y;
    int second_x;
    int second_y;

    cout << "Enter first x" << endl;
    cin >> first_x;
    cout << "Enter first y" << endl;
    cin >> first_y;
    cout << "Enter second x" << endl;
    cin >> second_x;
    cout << "Enter second y" << endl;
    cin >> second_y;

    int result = sqrt(pow(second_x - first_x,2) + pow(second_y - first_y,2));
    cout << "Distance is: " << result << endl;





    return 0;
}