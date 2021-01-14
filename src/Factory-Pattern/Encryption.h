// This is interface of Encryption
#ifndef ENCRYPTION_H
#define ENCRYPTION_H

#include <iostream>
using namespace std;
class Encryption {
public:
    virtual void encrypt_data() = 0;
    virtual void decrypt_data() = 0;
    virtual ~Encryption() {
        cout <<"Encryption class Destructor\n";
    }
};

#endif