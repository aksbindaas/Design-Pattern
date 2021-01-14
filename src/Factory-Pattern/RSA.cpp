#include "Encryption.h"

class RSA : public Encryption {
public:
    void encrypt_data() {
        cout<<"Encryped data with RSA\n";
    }

    void decrypt_data() {
        cout<<"Decryped data with RSA\n";
    }

    virtual ~RSA() {
        cout <<"RSA class Destructor\n";
    }
};