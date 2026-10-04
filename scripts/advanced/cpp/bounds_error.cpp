// 故意保留越界，用于 AddressSanitizer 教学。只运行自己的短生命周期进程。
#include <vector>
int main() {
    std::vector<int> values(3, 0);
    values[4] = 42;
    return values[4];
}
