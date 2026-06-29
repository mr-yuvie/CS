#include <iostream>

namespace test{
    int z = 2;
    int a = 67;
}

int main(){
    std::cout << "Hello Cpp" << std::endl; // endl flushes the output buffer, :: is scope resolution operator
    std::cout << "Bye" << '\n'; // \n is better for performance

    int x = 10;
    float y = 10.5;
    char hashtag = '#';
    std::cout << hashtag << '\n';

    // string
    std::string name = "Yuvie";
    std::cout << name << std::endl;

    // const: read-only value preventing modification
    const double PI = 3.14159;

    // Namespace prevents naming conflicts. It allows for indentically named entities as long as the namespace is different.
    int z = 1;
    std::cout << z << '\n'; // Uses locally declared variable
    std::cout << test::z << '\n'; // Uses the variable declared in that namespace
    std::cout << test::a << '\n';
}