#include "Encryption.h"

class AES : public Encryption {
public:
    void encrypt_data() {
        cout<<"Encryped data with AES\n";
    }

    void decrypt_data() {
        cout<<"Decryped data with AES\n";
    }

    virtual ~AES() {
        cout <<"AES class Destructor\n";
    }
};