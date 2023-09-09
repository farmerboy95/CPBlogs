# Ngưng xài rand() - Tổng quan về các trình sinh số ngẫu nhiên trong C++

## Nguồn

<img src="/CPBlogs/img/codeforces.png" width="16" height="16"/> [Don't use rand(): a guide to random number generators in C++](https://codeforces.com/blog/entry/61587)

## Tình huống

Nói chung cả bài này sẽ tựu chung lại thành một câu: Đừng dùng `rand` trong C++. Vì sao à? Ta xét code sau.


```cpp
#include <cstdlib>
#include <iostream>
using namespace std;

const int ITERATIONS = 1e7;

int main() {
    double sum = 0;

    for (int i = 0; i < ITERATIONS; i++)
        sum += rand() % 1000000;

    cout << "Average value: " << sum / ITERATIONS << '\n';
}
```

Giá trị được in ra mà bạn có thể đoán là xấp xỉ bao nhiêu?

Chắc nó phải nằm quanh 500000 nhỉ? Nhưng không, hoá ra nó lại tuỳ vào trình biên dịch, và trên Codeforces nó in ra 16382, quá xa so với giá trị kỳ vọng. Bạn có thể tự thử trên Codeforces với Custom Invocation.

## Cái quái gì đang xảy ra vậy?

Nếu bạn đã đọc về rand() trên [cppreference](https://en.cppreference.com/w/cpp/numeric/random/rand), bạn sẽ thấy nó trả về "một giá trị tích phân giả ngẫu nhiên giữa `0` và `RAND_MAX`". Xem thử `RAND_MAX` trên [cppreference](https://en.cppreference.com/w/cpp/numeric/random/RAND_MAX) nào, nó ghi là "Giá trị này tuỳ vào cài đặt. Nhưng nó được đảm bảo là ít nhất `32767`". Trên Codeforces thì `RAND_MAX` là `32767` luôn. Nhỏ vãi!!!

Chưa dừng lại ở đó, `random_shuffle()` cũng dùng `rand()` bên trong. Nhớ lại rằng để thực hiện xáo mảng ngẫu nhiên, ta cần [sinh các chỉ số ngẫu nhiên](https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle#The_modern_algorithm) đến $n$ - độ dài mảng. Nhưng nếu `rand()` chỉ lên được đến `32767`, điều gì sẽ xảy ra nếu ta gọi `random_shuffle()` trên một mảng nhiều phần tử hơn như vậy, thậm chí hơn như vậy nhiều? Xét thử một đoạn code nữa nào. Bạn nghĩ nó sẽ in ra gì?

```cpp
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

const int N = 3000000;

double average_distance(const vector<int> &permutation) {
    double distance_sum = 0;

    for (int i = 0; i < N; i++)
        distance_sum += abs(permutation[i] - i);

    return distance_sum / N;
}

int main() {
    vector<int> permutation(N);

    for (int i = 0; i < N; i++)
        permutation[i] = i;

    random_shuffle(permutation.begin(), permutation.end());
    cout << average_distance(permutation) << '\n';
}
```

Cái code trên tính kỳ vọng khoảng cách mà mỗi giá trị sẽ đi xa khỏi vị trí ban đầu của nó nếu ta xáo mảng ngẫu nhiên. Nếu bạn tính một chút thì sẽ thấy rằng kết quả cho một lần xáo mảng hoàn hảo sẽ là $\frac{N}{3} = 1000000$. Nếu bạn lười quá không muốn làm toán thì bạn cũng có thể thấy kết quả sẽ nằm giữa $\frac{N}{2} = 1500000$ (khoảng cách trung bình của chỉ số $0$) và $\frac{N}{4} = 750000$ (khoảng cách trung bình của chỉ số $\frac{N}{2}$).

Vâng, kết quả in ra lại làm bạn thất vọng rồi, nó là 64463. Tự thử trên Codeforces nhé. Nói cách khác, `random_shuffle()` chỉ di chuyển mỗi phần tử một khoảng cách trung bình bằng tầm khoảng 2% độ dài mảng. Dựa trên những lần test của mình thì cài đặt của `random_shuffle()` trên Codeforces về cơ bản sẽ y hệt như sau:

```cpp
for (int i = 1; i < N; i++)
    swap(permutation[i], permutation[rand() % (i + 1)]);
```

Nói chung là nếu `RAND_MAX` nhỏ hơn nhiều so với $N$, xáo mảng sẽ khá là chán đấy.

`rand()` cũng có nhiều vấn đề về chất lượng hơn là chỉ có việc `RAND_MAX` bị nhỏ. Nó thường được cài đặt như một trình sinh đồng dư tuyến tính ([linear congruential generator - LCG](https://en.wikipedia.org/wiki/Linear_congruential_generator)) đơn giản. Trên trình biên dịch Codeforces, nó trông như thế này:

```cpp
static long holdrand = 1L;

void srand(unsigned int seed) {
    holdrand = (long) seed;
}

int rand() {
    return (((holdrand = holdrand * 214013L + 2531011L) >> 16) & 0x7fff);
}
```

Cụ thể, các trình sinh đồng dư tuyến tính có nhược điểm là các bit thấp có khả năng dự đoán cực cao. Bit thứ k (bắt đầu từ k = 0, bit nhỏ nhất) có chu kỳ tối đa là $2^{k+1}$ (tức là mất bao lâu cho đến khi chuỗi lặp lại). Vậy bit nhỏ nhất có chu kỳ là 2, bit thứ hai có chu kỳ là 4, v.v. Đây là lý do tại sao hàm trên bỏ đi 16 bit nhỏ nhất, và kết quả thu được tối đa là 32767 (nghĩa là bỏ 16 bit, ta còn lại 16 bit).

## Rồi giải pháp là sao?

Đừng lo, C++11 cho ta những trình sinh số ngẫu nhiên (RNG) tốt hơn nhiều. Điều duy nhất bạn cần làm là nhớ dùng `mt19937`, nằm trong header `<random>`. Đây là một thuật toán [Mersenne Twister](https://en.wikipedia.org/wiki/Mersenne_Twister) dựa trên số nguyên tố $2^{19937} - 1$, cũng là chu kỳ của nó luôn. Đây là một RNG tốt hơn rất nhiều so với `rand()`, và cũng nhanh hơn nhiều nữa (389 ms để sinh và thêm $10^8$ số từ `mt19937` trong Custom Invocation, so với 1170 ms với `rand()`). Nó cũng sinh được số 32-bit không dấu nằm giữa $0$ và $2^{32} - 1 = 4294967295$, tốt hơn nhiều so với $32767$ của `rand()`.

Để thay thế `random_shuffle()`, ta có thể dùng `shuffle()` và truyền `mt19937` của bạn vào tham số thứ 3, thuật toán xáo sẽ dùng trình sinh của bạn để thực hiện xáo.

C++11 cũng cho ta một số cách [phân phối](https://en.cppreference.com/w/cpp/numeric/random) tiện lợi. `uniform_int_distribution` cho ta phân phối đều các số nguyên trong một khoảng, mà không bị sai lệch về mod, ví dụ, `rand() % 10000` sẽ có xu hướng cho ra các số nằm giữa 0 và 999 hơn là các số nằm giữa 9000 và 9999, vì 32767 không phải là bội của 10000. Có nhiều cách phân phối hay ho khác, ví dụ như `normal_distribution` và `exponential_distribution`.

Để dễ hiểu hơn, bên dưới sẽ là code sử dụng một số thứ được nói ở trên. Lưu ý rằng code khởi tạo RNG bằng cách dùng clock có độ chính xác cao. Điều này rất quan trọng để tránh hack được thiết kế riêng cho code của bạn, vì việc sử dụng seed cố định cũng có nghĩa là bất kỳ ai cũng có thể biết được rằng RNG của bạn sẽ xuất ra gì. Để biết thêm chi tiết, bạn có thể đọc bài [Làm sao hack các solution ngẫu nhiên và cách ngăn chặn nó](https://codeforces.com/blog/entry/61675).

Cuối cùng, nếu bạn muốn sinh số ngẫu nhiên 64-bit, bạn chỉ cần dùng `mt19937_64`.

```cpp
#include <algorithm>
#include <chrono>
#include <iostream>
#include <random>
#include <vector>
using namespace std;

const int N = 3000000;

double average_distance(const vector<int> &permutation) {
    double distance_sum = 0;

    for (int i = 0; i < N; i++)
        distance_sum += abs(permutation[i] - i);

    return distance_sum / N;
}

int main() {
    mt19937 rng(chrono::steady_clock::now().time_since_epoch().count());
    vector<int> permutation(N);

    for (int i = 0; i < N; i++)
        permutation[i] = i;

    shuffle(permutation.begin(), permutation.end(), rng);
    cout << average_distance(permutation) << '\n';

    for (int i = 0; i < N; i++)
        permutation[i] = i;

    for (int i = 1; i < N; i++)
        swap(permutation[i], permutation[uniform_int_distribution<int>(0, i)(rng)]);

    cout << average_distance(permutation) << '\n';
}
```

Kết quả của cả hai phép xáo đều gần khoảng cách kì vọng $10^6$, giống như ta muốn.

## Tham khảo

Bài này được lấy cảm hứng từ một phần từ [bài nói chuyện của Stephan T. Lavavej](https://channel9.msdn.com/Events/GoingNative/2013/rand-Considered-Harmful).

Nếu bạn muốn một trình sinh số ngẫu nhiên nhanh và chất lượng cao, hãy ghé qua [trang này của Sebastiano Vigna](http://xoshiro.di.unimi.it/).
