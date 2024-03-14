#include <iostream>

using namespace std;

void test(){
    for (int i = 0; i < 10; i++) {
        for (int j = 0; j < 10; j++) {
            cout << i * j << endl;
        }  
    }
}

int main(void) {
    cout << "Hello World!" << endl;
    
    test();

    return 0;
}