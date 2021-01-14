#include "EncryptionFactory.cpp"

int main () {
    cout<<"Executing Encryption Library Factory \n";
    auto enc =  EncryptionFactory::GetAlgorithmLibrary(AES_ALGO);
    enc->encrypt_data();
    enc->decrypt_data();

    enc = EncryptionFactory::GetAlgorithmLibrary(DES_ALGO);
    enc->encrypt_data();
    enc->decrypt_data();

    enc = EncryptionFactory::GetAlgorithmLibrary(RSA_ALGO);
    enc->encrypt_data();
    enc->decrypt_data();
}