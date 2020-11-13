#include <iostream>
#include <bitset>

using namespace std;

bool isUnique(const string& input){
    bitset<128> asciiTable;
    for (char c : input){
        if (asciiTable[(int) c]){
            return false;
        }
        asciiTable.flip((int) c); // xor em asciiTable e c
    }
    return true;
}

