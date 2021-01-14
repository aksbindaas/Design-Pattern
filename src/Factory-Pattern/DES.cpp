#include "Encryption.h"

class DES : public Encryption {
public:
    void encrypt_data() {
        cout<<"Encryped data with DES\n";
    }

    void decrypt_data() {
        cout<<"Decryped data with DES\n";
    }

    virtual ~DES() {
        cout <<"DES class Destructor\n";
    }
};