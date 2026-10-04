#include <cmath>
#include <iomanip>
#include <iostream>
#include <stdexcept>
#include <string>

int main(int argc, char* argv[]) {
    if (argc != 2) {
        std::cerr << "用法：angle 角度\n";
        return 2;
    }
    try {
        std::size_t consumed = 0;
        const std::string input(argv[1]);
        const double degrees = std::stod(input, &consumed);
        if (consumed != input.size() || !std::isfinite(degrees)) {
            throw std::invalid_argument("invalid angle");
        }
        const double pi = std::acos(-1.0);
        const double radians = degrees * pi / 180.0;
        std::cout << std::fixed << std::setprecision(6) << radians << '\n';
    } catch (const std::exception&) {
        std::cerr << "角度必须是一个有限数值\n";
        return 2;
    }
    return 0;
}
