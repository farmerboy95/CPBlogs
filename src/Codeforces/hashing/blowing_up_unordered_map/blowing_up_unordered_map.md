# Giải mã và chống hack cho unordered_map trong C++

## Nguồn

<img src="/CPBlogs/img/codeforces.png" width="16" height="16"/> [Blowing up unordered_map, and how to stop getting hacked on it](https://codeforces.com/blog/entry/62393)

## Giới thiệu

C++ có những cấu trúc dữ liệu rất tiện như là `std::set` hay `std::map`. Chúng là các cấu trúc dữ liệu dạng cây và tốn $O(log n)$ thời gian. Với C++11, chúng ta có thêm hash set và hash map lần lượt trong `std::unordered_set` và `std::unordered_map`. Tuy nhiên, ta thấy rằng rất nhiều bạn trên Codeforces đã bị hack hoặc tạch system test với các cấu trúc dữ liệu hash này. Trong bài này ta sẽ đi vào giải mã chúng và những thứ bạn có thể làm để tiếp tục sử dụng chúng mà không lo bị hack.

## Giải mã

Ta luôn giả sử rằng hash map có độ phức tạp $O(1)$ trong mỗi thao tác (chèn, xoá, truy cập...). Tuy nhiên, điều này lại phụ thuộc vào một giả định rất quan trọng, đó là mỗi item mới bị trùng trung bình `O(1)` lần với các item cũ. Nếu input của chúng ta hoàn toàn ngẫu nhiên, giả định ban đầu sẽ hợp lý. Ngược lại, điều này sẽ rất nguy hiểm, đặc biệt là khi ai đó thiết kế input (như trong hacking phase) để làm cho giả định trên sai lệch. Cụ thể là, nếu người ta biết hàm hash của chúng ta, người đó có thể dễ dàng sinh ra một loạt các input có cùng giá trị hash, khiến cho thời gian thực thi của chúng ta tăng lên $O(n^2)$.

Ta sẽ chứng minh điều này bằng cách tìm hiểu code của `unordered_map`. Ta có thể đọc code này trên GitHub tại đây: [https://github.com/gcc-mirror/gcc](https://github.com/gcc-mirror/gcc).

Sau khi mò mẫm một hồi thì ta đến file [unordered_map.h](https://github.com/gcc-mirror/gcc/blob/5bea0e90e58d971cf3e67f784a116d81a20b927a/libstdc%2B%2B-v3/include/bits/unordered_map.h). Trong file này thì ta có thể thấy rằng `unordered_map` dùng `__detail::_Mod_range_hashing` và `__detail::_Prime_rehash_policy`. Từ đây ta có thể đoán được map sẽ hash giá trị đầu vào rồi mod nó với một số nguyên tố, kết quả thu được sẽ được dùng để chọn vị trí thích hợp trên hash table.

Mò tiếp `_Prime_rehash_policy` thì ta đến file [hashtable_c++0x.cc](https://github.com/gcc-mirror/gcc/blob/5bea0e90e58d971cf3e67f784a116d81a20b927a/libstdc%2B%2B-v3/src/c%2B%2B11/hashtable_c%2B%2B0x.cc). Ở đây ta có thể thấy có một mảng gọi là `__prime_list`, và hash table có một policy để tự điều chỉnh kích thước khi nó quá to. Đến đây ta chỉ cần tìm danh sách các số nguyên tố thôi. Cái danh sách đó sẽ nằm trong file [hashtable-aux.cc](https://github.com/gcc-mirror/gcc/blob/5bea0e90e58d971cf3e67f784a116d81a20b927a/libstdc%2B%2B-v3/src/shared/hashtable-aux.cc).

Một điều nữa, ta cần biết hàm hash mà `unordered_map` dùng trước khi mod với các số nguyên tố này. Thực ra thì nó khá đơn giản: cái map sẽ dùng `std::hash`, với số nguyên thì đây chỉ là hàm nhận dạng. Với kiến thức này, ta có thể chèn nhiều bội của các số nguyên tố trên vào map để tăng độ phức tạp của nó lên $O(n^2)$. Tuy nhiên, không phải số nguyên tố nào cũng dùng được do cái policy tự điều chỉnh kích thước của map (cái mà ta đã nói ở trên). Để một số nguyên tố có thể phá được cái map này, ta cần nó phải tự điều chỉnh kích thước về chính số nguyên tố đó tại một thời điểm nào đó trong tập các thao tác của chúng ta. Hoá ra số nguyên tố này phụ thuộc vào phiên bản của compiler: với `gcc 6` trở về trước, số đó là `126271`, với `gcc 7` về sau, số đó sẽ là `107897`. Chạy code sau trong [Custom Invocation của Codeforces](https://codeforces.com/contest/1033/customtest) và xem nó sẽ như nào.

```cpp
#include <ctime>
#include <iostream>
#include <unordered_map>
using namespace std;

const int N = 2e5;

void insert_numbers(long long x) {
    clock_t begin = clock();
    unordered_map<long long, int> numbers;

    for (int i = 1; i <= N; i++)
        numbers[i * x] = i;

    long long sum = 0;

    for (auto &entry : numbers)
        sum += (entry.first / x) * entry.second;

    printf("x = %lld: %.3lf seconds, sum = %lld\n", x, (double) (clock() - begin) / CLOCKS_PER_SEC, sum);
}

int main() {
    insert_numbers(107897);
    insert_numbers(126271);
}
```

Cụ thể, với `gcc 6` (GNU G++14 6.4.0) thì kết quả là:

```
x = 107897: 0.032 seconds, sum = 2666686666700000
x = 126271: 3.135 seconds, sum = 2666686666700000

=====
Used: 3151 ms, 7724 KB
```

Với `gcc 7` (GNU G++17 7.3.0) thì kết quả là:

```
x = 107897: 3.330 seconds, sum = 2666686666700000
x = 126271: 0.000 seconds, sum = 2666686666700000

=====
Used: 3275 ms, 7564 KB
```

Ta có thể thấy rằng tuỳ vào phiên bản compiler, một trong hai số này sẽ làm map chậm đi nhiều so với số còn lại. Có một số số nguyên tố nữa cũng làm được, bạn có thể tự thử.

Chú ý rằng với các hash table khác như `cc_hash_table` và `gp_hash_table` (đọc [post của bạn Chilli trên Codeforces](https://codeforces.com/blog/entry/60737)), việc hack còn dễ hơn. Các hash table này dùng policy mod luỹ thừa của 2, cho nên là để tạo ra nhiều giá trị trùng, bạn có thể chèn vào nhiều giá trị tương đương, với mod $2^{16}$.

## Cách chống hack

Để chống việc input cố ý tạo ra các giá trị hash trùng nhau, ta có thể tự viết một hàm hash để thả vào trong `unordered_map` (hay `gp_hash_table` gì đó). Hàm hash sẽ trông như thế này:

```cpp
struct custom_hash {
    size_t operator()(uint64_t x) const {
        return x;
    }
};
```

Tuy nhiên, như đã nói, bất cứ một hàm hash xác định hoặc có thể đoán được nào cũng có thể được reverse-engineered để tạo ra một lượng lớn giá trị hash trùng, vì vậy điều đầu tiên ta cần làm là thêm một số tính chất không xác định (như clock độ chính xác cao) để gây khó cho việc hack hơn:

```cpp
struct custom_hash {
    size_t operator()(uint64_t x) const {
        static const uint64_t FIXED_RANDOM = chrono::steady_clock::now().time_since_epoch().count();
        return x + FIXED_RANDOM;
    }
};
```

Đọc bài về [chống hack cho các solution random](https://codeforces.com/blog/entry/61675) để có thêm thông tin. Ok, giờ nó an toàn rồi đúng không? Không, tất cả những thứ ta đã làm là thêm cùng một số vào mọi input của hàm. Nhưng nếu hai số $a$ và $b$ thoả $a \equiv b \;(\bmod\; m)$, thì $a + x \equiv b + x \;(\bmod\; m)$ với mọi $x$. Vấn đề tương tự xảy ra với mọi hàm hash đơn giản khác: nhân với một số lẻ lớn ngẫu nhiên (và tràn, với mod $2^{64}$) có thể có hiệu quả với modulo $p$, nhưng sẽ có vấn đề với policy luỹ thừa 2 của `gp_hash_table`. Tình huống tương tự cũng xảy ra với việc xor với một số ngẫu nhiên nào đó.

Một hàm hash tốt hơn một chút có thể trông hấp dẫn như sau:

```cpp
struct custom_hash {
    size_t operator()(uint64_t x) const {
        static const uint64_t FIXED_RANDOM = chrono::steady_clock::now().time_since_epoch().count();
        x ^= FIXED_RANDOM;
        return x ^ (x >> 16);
    }
};
```

Tuy nhiên, nếu bạn đang dùng `gp_hash_table`, cái này vẫn có thể khiến bạn bị hack nếu gặp một thanh niên cứng cựa. Cụ thể, sau khi chèn các số `(1 << 16) + 1`, `(2 << 16) + 2`, `(3 << 16) + 3`, ... vào hàm hash này, tất cả các output đều sẽ tương đương với nhau (khi mod $2^{16}$).

Vì thế, ta cần một hàm hash tốt hơn, lý tưởng nhất là khi việc thay đổi bất kỳ bit input nào cũng dẫn đến cơ hội 50-50 thay đổi bất kỳ bit đầu ra nào. Ví dụ, trong hàm hash `x + FIXED_RANDOM`, tính chất này không được thoả mãn, vì có khả năng thay đổi bit cao hơn trong `x` dẫn đến khả năng 0% thay đổi bit thấp hơn của output.

Cá nhân mình thì thích dùng [splitmix64](http://xoshiro.di.unimi.it/splitmix64.c), nó nhanh và có chất lượng đỉnh của chóp, cảm ơn bạn Sebastiano Vigna đã thiết kế ra nó. Gộp hết mọi thứ lại với nhau ta sẽ có hàm hash an toàn:

```cpp
struct custom_hash {
    static uint64_t splitmix64(uint64_t x) {
        // http://xorshift.di.unimi.it/splitmix64.c
        x += 0x9e3779b97f4a7c15;
        x = (x ^ (x >> 30)) * 0xbf58476d1ce4e5b9;
        x = (x ^ (x >> 27)) * 0x94d049bb133111eb;
        return x ^ (x >> 31);
    }

    size_t operator()(uint64_t x) const {
        static const uint64_t FIXED_RANDOM = chrono::steady_clock::now().time_since_epoch().count();
        return splitmix64(x + FIXED_RANDOM);
    }
};
```

Giờ ta có thể định nghĩa `unordered_map` hay `gp_hash_table` như sau:

```cpp
unordered_map<long long, int, custom_hash> safe_map;
gp_hash_table<long long, int, custom_hash> safe_hash_table;
```

Khi dùng những thứ đó cho chương trình ở trên cùng, nó chạy khá nhanh:

```
x = 107897: 0.035 seconds, sum = 2666686666700000
x = 126271: 0.031 seconds, sum = 2666686666700000

=====
Used: 109 ms, 9204 KB
```
