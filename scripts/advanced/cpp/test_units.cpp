#include "units.hpp"
#include <cmath>
int main() {
    const double expected = std::acos(-1.0) / 6.0;
    if (std::abs(degrees_to_radians(30.0) - expected) > 1e-10) return 1;
    if (degrees_to_radians(0.0) != 0.0) return 1;
    return 0;
}
