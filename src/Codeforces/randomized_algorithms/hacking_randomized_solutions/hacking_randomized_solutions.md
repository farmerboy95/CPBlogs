# Làm sao hack các solution ngẫu nhiên và cách ngăn chặn nó

## Nguồn

<img src="/CPBlogs/img/codeforces.png" width="16" height="16"/> [How randomized solutions can be hacked, and how to make your solution unhackable](https://codeforces.com/blog/entry/61675)

## Tình huống

Trong Round 507 trên Codeforces, có một cơ số các solution ngẫu nhiên gần đúng trong bài [1039B - Subway Pursuit](https://codeforces.com/contest/1039/problem/B) bị hack. Mình muốn giải thích nhanh vì sao nó lại có thể bị hack và cách để viết code sao cho nó tránh bị hack.

Đầu tiên ta cần xem đáp án của bài như nào nhé: ta có thể dùng tìm kiếm nhị phân để thu nhỏ phạm vi các vị trí có thể cho tàu xuống thành một bội số của $K$, ví dụ như $6K$. Chỉ cần đảm bảo mở rộng cả hai đầu của phạm vi này thêm $K$ sau mỗi lần lặp. Khi phạm vi tối đa là $6K$, ta có thể lặp lại các bước như sau:

1. Đoán ngẫu nhiên các số còn lại. Xác suất thành công ít nhất là $\frac{1}{6K}$.
2. Tìm kiếm nhị phân cho đến khi phạm vi lại về tối đa $6K$. Hoá ra chỉ cần một truy vấn thôi, vì sau lần đoán trước thì đoạn $6K$ của ta sẽ thành đoạn $8K$, và một truy vấn sẽ thu nhỏ đoạn này về $\frac{8K}{2} + 2K = 6K$.

Vì $K \leq 10$ và ta có 4500 truy vấn, solution này sẽ ok vì xác suất thất bại trong bất cứ test case nào sẽ không quá $(\frac{59}{60})^{2200} \approx 8 \cdot 10^{-17}$, cực nhỏ.

Tuy nhiên, điều này đưa ra giả định quan trọng rằng các vị trí tàu độc lập với truy vấn của chúng ta. Vấn đề chính của các solution bị hack là chúng đều được xác định hoàn toàn, nghĩa là chúng đều truy vấn cùng một chuỗi số trong mỗi lần chạy, cho ra cùng một kết quả. Hầu hết mọi người gặp phải vấn đề này do dùng `rand()` mà không bao giờ dùng `srand()`. Ngoài ra còn một số nguyên nhân khác: `random_device` khá kì lạ khi cũng được xác định trên Codeforces, giống `mt19937` khi không có seed. Gọi `srand()` với một giá trị cố định cũng sẽ dẫn đến kết quả giống nhau, làm cho chương trình của bạn dễ đoán và nói chung cũng không tốt.

Do có thể dự đoán được nên các chương trình này khá dễ bị hack: chỉ cần tạo ra cùng một chuỗi truy vấn mà chương trình sẽ thực hiện, và đặt tàu ở một vị trí khác ở mỗi truy vấn. Để làm cho việc này dễ hơn khi bạn hack người ta, bạn chỉ cần chọn $N = 2$ và $K = 1$, nó sẽ bỏ qua giai đoạn tìm kiếm nhị phân ban đầu, rồi đặt tàu vào chỗ không được truy vấn giữa 1 và 2 mỗi lần truy vấn.

## Cách giải quyết?

Để tránh hack thì nhiều bạn seed RNG với thời gian hiện tại bằng cách gọi `srand(time(NULL));`. Nó sẽ giúp code tránh bị xác định và ít có khả năng bị hack hơn, nhưng cái này vẫn có khả năng lớn bị hack. Vấn đề chính ở đây là `time(NULL)` chỉ đúng đến đơn vị giây thôi. Nếu mình đoán được chương trình của bạn được chạy ở thời điểm nào, code của bạn vẫn có thể bị đoán được.

Cũng chả cần đoán luôn ấy. Nếu mình đặt $N = 11$ và $K = 10$, mình có thể sinh ra tất cả các dãy truy vấn mà bạn có thể sinh ra trong 10 giây tiếp theo, vì code của bạn gần như chắc chắn sẽ chạy sau trình tạo của mình vài giây. Sau đó, với mỗi truy vấn, ít nhất một trong 11 vị trí sẽ không bị chọn bởi bất kỳ chuỗi nào trong số 10 chuỗi, và mình có thể di chuyển tàu đến vị trí đó mỗi lần. Không may (cho mình, may cho bạn) là mình chẳng có thời gian làm vậy trong contest.

## Đáp án

Sửa thì cũng dễ thôi. `time(NULL)` cũng có ý tốt đấy, nhưng ta cần một clock có độ chính xác cao hơn:

`mt19937 rng(chrono::steady_clock::now().time_since_epoch().count());`

Sau đó sinh số ngẫu nhiên bằng cách dùng `rng()`. Nhớ thêm header `<chrono>` và `<random>`. Ủa sao không dùng `rand()` và `srand()`? Đọc [bài này](https://codeforces.com/blog/entry/61587) nhé.

Một cách khác là dùng địa chỉ của một biến mới tạo trong heap:

`mt19937 rng((uint64_t) new char);`

Nó sẽ khác nhau trong mỗi lần chạy. Lưu ý rằng nó sẽ tạo ra một ít memory leak trong vòng đời của chương trình vì ta không bao giờ gọi lệnh xoá, nhưng vì đó chỉ là một biến nên cũng không sao cả.

Cá nhân mình thích kết hợp cả hai phương pháp này nhưng cũng không cần thiết. Một trong hai cách sẽ khiến chương trình của bạn trở nên khó đoán hơn nhiều, khiến nó không thể bị hack một cách hiệu quả.

Nếu bạn muốn đọc thêm, hãy đọc bài của bạn dacin21 về [sinh anti-hash test](https://codeforces.com/blog/entry/60442).
