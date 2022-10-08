#ifndef TESTE_H_
#define TESTE_H_

class Objeto{
    private:
        string *var = new string;
    public:
        Objeto();
        ~Objeto();
        int x = 5;
        string setString();
        string getString();
};
Objeto::Objeto(){
    *var = "";
}

Objeto::~Objeto(){
    delete var;
}
string Objeto::setString(){
    cin >> *var;
    return *var;
}
string Objeto::getString(){
    return *var;
}

#endif