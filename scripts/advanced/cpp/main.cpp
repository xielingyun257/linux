#include "units.hpp"
#include <iomanip>
#include <iostream>
#include <string>
int main(int argc, char* argv[]) {
    if (argc != 2) return 2;
    std::cout << std::fixed << std::setprecision(6)
              << degrees_to_radians(std::stod(argv[1])) << '\n';
}
