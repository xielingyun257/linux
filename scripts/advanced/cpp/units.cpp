#include "units.hpp"
#include <cmath>
double degrees_to_radians(double degrees) {
    return degrees * std::acos(-1.0) / 180.0;
}
