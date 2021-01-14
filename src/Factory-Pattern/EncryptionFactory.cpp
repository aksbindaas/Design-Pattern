#include "AES.cpp"
#include "DES.cpp"
#include "RSA.cpp"
#include <memory>
enum ALGOTYPE { AES_ALGO, DES_ALGO, RSA_ALGO };

class EncryptionFactory {
public:
    static std::unique_ptr<Encryption> GetAlgorithmLibrary(ALGOTYPE type) {
        switch (type) {
        case AES_ALGO:
            return  make_unique<AES>();
            break;
        
        case DES_ALGO:
            return make_unique<DES>();
            break;

        case RSA_ALGO:
            return make_unique<RSA>();
            break;
        default:
            cout << "Requested Algorithm is not available\n";
            return nullptr;
            break;
        }
    }
};