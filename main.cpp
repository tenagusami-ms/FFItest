#include <iostream>
#include "test.h"

using namespace std;

int main(int argc,char *argv[]) {
    cout << "Hello, World!" << endl;
    //const int i = test(1);
    int i = 1;
    test(i);
    cout<<"test2="<<test2(i)<<endl;
    //cout << i << endl;
    return 0;
}
