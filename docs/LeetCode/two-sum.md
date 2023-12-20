# Lớp bài tập Two-Sum

## Nguồn

Bài viết này được dựa trên editorial các bài tập có dạng Two-Sum trên LeetCode, nghĩa là các bài toán có dạng: Cho một mảng các số nguyên và một số nguyên `target`, hãy tìm $X$ số trong mảng có tổng theo một tiêu chí nào đó so với `target`.

Code của các bài toán này có thể xem tại phần Luyện tập ở dưới cùng.

## LeetCode 1 - Two Sum

Cho một mảng các số nguyên `nums` có $N$ phần tử và một số nguyên `target`, hãy trả về chỉ số của hai số trong mảng có tổng bằng `target`. Bạn có thể giả sử rằng mỗi input chỉ có một lời giải duy nhất và bạn không thể dùng cùng một phần tử hai lần. Bạn có thể trả về kết quả theo bất kì thứ tự nào.

Giới hạn: $2 \le N \le 10^4$, $-10^9 \le nums_i \le 10^9$, $-10^9 \le target \le 10^9$.

Chi tiết đề bài có thể xem tại [đây](https://leetcode.com/problems/two-sum/).

??? tip "Lời giải"
    Ngoài cách duyệt trâu $O(N^2)$ ra, ta có thể để ý rằng khi xét một số $x$ (ở vị trí $i$) trong mảng, ta chỉ cần tìm xem có tồn tại một số $y$ trong mảng sao cho $x + y = target$ hay $y = target - x$. Ta có thể duy trì một hash table chứa các số nằm trước vị trí $i$ để tìm kiếm $y$ trong $O(1)$, nên nhớ là trung bình $O(1)$. Như vậy, với cách này độ phức tạp thời gian là $O(N)$, độ phức tạp bộ nhớ là $O(N)$.

    Ngoài ra ta còn có thể tạo một mảng khác lưu giá trị và vị trí của các phần tử trong mảng ban đầu, sắp xếp nó theo thứ tự tăng dần giá trị, sau đó đặt 2 con trỏ ở đầu và cuối mảng, nếu tổng giá trị của hai con trỏ nhỏ hơn `target` thì ta tăng con trỏ ở đầu, ngược lại ta giảm con trỏ ở cuối. Độ phức tạp thời gian là $O(N \log N)$, độ phức tạp bộ nhớ là $O(N)$.

## LeetCode 15 - 3Sum

Cho một mảng các số nguyên `nums` có $N$ phần tử, hãy trả về tất cả các bộ ba số không trùng vị trí với nhau trong mảng có tổng bằng 0. Kết quả không được chứa các bộ ba số trùng nhau về mặt giá trị, ví dụ nếu có hai bộ ba $[1, 2, 3]$ thì chỉ tính một lần.

Giới hạn: $3 \le N \le 3000$, $-10^5 \le nums_i \le 10^5$.

Chi tiết đề bài có thể xem tại [đây](https://leetcode.com/problems/3sum/).

??? tip "Lời giải"
    Với mỗi số $x$ (ở vị trí $i$) trong mảng, ta tìm kiếm xem bên phải nó có tồn tại một bộ đôi $(y, z)$ trong mảng sao cho $y + z = -x$ hay không. Đến đây bài toán lại trở về với bài toán Two Sum. Tuy nhiên, ta không xét các số $x$ bằng nhau vì nó sẽ tạo ra các bộ ba giống nhau. Để bớt thời gian xét bằng nhau thì ta có thể sắp xếp mảng trước, sau đó ta chỉ xét số $x$ một lần khi nó khác số $x$ ở vị trí trước đó. Còn về việc tìm $y$ và $z$. Ta có thể tìm bằng hash table hoặc 2 con trỏ như ở bài Two Sum, tuy nhiên sau khi tìm được một bộ ba, ta phải tránh trùng lặp bằng cách cho di chuyển $y$ hoặc $z$ (tuỳ theo cách làm) sang một giá trị mới. Độ phức tạp thời gian là $O(N^2)$, độ phức tạp bộ nhớ là $O(N)$.

    Ta cũng có thể làm cách không sắp xếp. Đáp án của chúng ta sẽ là một `set` luôn, ta cũng duy trì một hashset để tránh trùng lặp $x$. Khi duyệt tìm $z$ ở bên phải $x$, ta lưu lại xem ta có thấy $y = -x - z$ trong một hash table `seen` hay chưa, trick ở đây là ta lưu `seen[nums[j]] = i` để không phải xoá hash table sau mỗi lần duyệt $x$. Ta cũng không cần phải để ý xem $y$ và $z$ có khả năng trùng không vì nếu trùng thì set đáp án sẽ lo. Độ phức tạp thời gian là $O(N^2)$, độ phức tạp bộ nhớ là $O(N)$.

## LeetCode 16 - 3Sum Closest

Cho một mảng các số nguyên `nums` có $N$ phần tử và một số nguyên `target`, hãy trả về tổng của 3 số trong mảng có tổng gần nhất với `target`. Giả sử rằng mỗi input chỉ có một lời giải duy nhất.

Giới hạn: $3 \le N \le 500$, $-10^3 \le nums_i \le 10^3$, $-10^4 \le target \le 10^4$.

??? tip "Lời giải"
    Đầu tiên ta sắp xếp lại mảng, sau đó với mỗi giá trị $x$ (ở vị trí $i$), ta tìm xem trong phần bên phải của $x$ có $y$ và $z$ sao cho $y + z$ gần nhất với $target - x$ hay không. Để tìm $y$ và $z$ ta có thể dùng 2 con trỏ như ở bài Two Sum. Độ phức tạp thời gian là $O(N^2)$, độ phức tạp bộ nhớ là $O(\log N)$ hoặc $O(N)$, tuỳ vào thuật toán sắp xếp.

    Ngoài ra, ta cũng có thể chặt nhị phân tìm $y$ giữa $x$ và $z$ sau khi sắp xếp mảng. Độ phức tạp thời gian là $O(N^2 \log N)$, độ phức tạp bộ nhớ là $O(\log N)$ hoặc $O(N)$, tuỳ vào thuật toán sắp xếp.

## LeetCode 259 - 3Sum Smaller

Cho một mảng các số nguyên `nums` có $N$ phần tử và một số nguyên `target`, hãy trả về số bộ ba số trong mảng có tổng nhỏ hơn `target`.

Giới hạn: $0 \le N \le 3500$, $-100 \le nums_i \le 100$, $-100 \le target \le 100$.

??? tip "Lời giải"
    Ta cũng có hai cách như bài trước, và đều phải sắp xếp mảng trước khi tính toán.

    Đầu tiên, với chặt nhị phân, ta tìm $y$ lớn nhất làm tổng nhỏ hơn `target`, rồi thêm đoạn từ $i+1$ đến vị trí của $y$ vào kết quả. Độ phức tạp thời gian là $O(N^2 \log N)$, độ phức tạp bộ nhớ là $O(\log N)$ hoặc $O(N)$, tuỳ vào thuật toán sắp xếp.

    Với 2 con trỏ, ta đặt chúng ở $i+1$ và cuối mảng, nếu tổng 3 số nhỏ hơn target thì ta có thể thêm đoạn từ con trỏ trái đến con trỏ phải vào kết quả, sau đó ta tăng con trỏ trái, ngược lại ta giảm con trỏ phải. Độ phức tạp thời gian là $O(N^2)$, độ phức tạp bộ nhớ là $O(\log N)$ hoặc $O(N)$, tuỳ vào thuật toán sắp xếp.

## LeetCode 18 - 4Sum

Cho một mảng các số nguyên `nums` có $N$ phần tử và một số nguyên `target`, hãy trả về tất cả các bộ 4 số (riêng biệt về vị trí) trong mảng có tổng bằng `target`. Kết quả không được chứa các bộ 4 số trùng nhau về mặt giá trị.

Giới hạn: $4 \le N \le 200$, $-10^9 \le nums_i \le 10^9$, $-10^9 \le target \le 10^9$.

??? tip "Lời giải"
    Ta giải y hệt bài 3Sum, có điều ta cần duyệt 2 vòng lặp ngoài nhau để xét $x$ và $y$. Hai số còn lại ta có thể tìm bằng hash table hoặc 2 con trỏ. Độ phức tạp thời gian là $O(N^3)$, độ phức tạp bộ nhớ là $O(N)$.

## LeetCode 454 - 4Sum II

Cho 4 mảng các số nguyên `A`, `B`, `C`, `D` có $N$ phần tử, hãy trả về số bộ 4 vị trí trong 4 mảng có tổng bằng 0.

Giới hạn: $0 \le N \le 200$, $-2^{28} \le A_i, B_i, C_i, D_i \le 2^{28}$.

??? tip "Lời giải"
    Ta dùng hash table để lưu số các tổng của 2 số trong 2 mảng đầu tiên. Sau đó làm tương tự với 2 mảng còn lại, khi xét thì ta tìm xem trong hash table có âm của tổng đang xét hay không, nếu có thì thêm vào đáp án. Độ phức tạp thời gian là $O(N^2)$, độ phức tạp bộ nhớ là $O(N^2)$.

    Nếu người ta hỏi $k$ mảng thì sao? Ta chia số mảng này ra hai phần, một phần có $\lfloor k/2 \rfloor$ mảng, một phần có $\lceil k/2 \rceil$ mảng. Sau đó ta dùng hash table cho một phần, rồi duyệt phần còn lại y hệt như trên. Độ phức tạp thời gian là $O(N^{\lceil k/2 \rceil})$, độ phức tạp bộ nhớ là $O(N^{\lceil k/2 \rceil})$.

## Luyện tập

Dưới đây là code mẫu của toàn bộ các cách giải các bài toán trên.

| Problem | Status | Submission | Code | Date |
| :---: | :-----------: | :---: | :---: | :---: |
| [LC 1 - Two Sum](https://leetcode.com/problems/two-sum/) - Hash Table Approach | :white_check_mark: | Unavailable public link | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/LeetCode/LC1-two-sum(HashTable).cpp) | 20/12/2023 |
| [LC 1 - Two Sum](https://leetcode.com/problems/two-sum/) - 2-pointer Approach | :white_check_mark: | Unavailable public link | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/LeetCode/LC1-two-sum(2-pointer).cpp) | 20/12/2023 |
| [LC 15 - 3Sum](https://leetcode.com/problems/3sum/) - Hash Table Approach | :white_check_mark: | Unavailable public link | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/LeetCode/LC15-3sum(HashTable).cpp) | 20/12/2023 |
| [LC 15 - 3Sum](https://leetcode.com/problems/3sum/) - 2-pointer Approach | :white_check_mark: | Unavailable public link | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/LeetCode/LC15-3sum(2-pointer).cpp) | 20/12/2023 |
| [LC 15 - 3Sum](https://leetcode.com/problems/3sum/) - No-sort Approach | :white_check_mark: | Unavailable public link | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/LeetCode/LC15-3sum(NoSort).cpp) | 20/12/2023 |
| [LC 16 - 3Sum Closest](https://leetcode.com/problems/3sum-closest/) - 2-pointer Approach | :white_check_mark: | Unavailable public link | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/LeetCode/LC16-3sum-closest(2-pointer).cpp) | 20/12/2023 |
| [LC 16 - 3Sum Closest](https://leetcode.com/problems/3sum-closest/) - Binary Search Approach | :white_check_mark: | Unavailable public link | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/LeetCode/LC16-3sum-closest(BinarySearch).cpp) | 20/12/2023 |
| [LC 259 - 3Sum Smaller](https://leetcode.com/problems/3sum-smaller/) - 2-pointer Approach | :white_check_mark: | Unavailable public link | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/LeetCode/LC259-3sum-smaller(2-pointer).cpp) | 20/12/2023 |
| [LC 259 - 3Sum Smaller](https://leetcode.com/problems/3sum-smaller/) - Binary Search Approach | :white_check_mark: | Unavailable public link | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/LeetCode/LC259-3sum-smaller(BinarySearch).cpp) | 20/12/2023 |
| [LC 18 - 4Sum](https://leetcode.com/problems/4sum/) - Hash Table Approach | :white_check_mark: | Unavailable public link | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/LeetCode/LC18-4sum(HashTable).cpp) | 20/12/2023 |
| [LC 18 - 4Sum](https://leetcode.com/problems/4sum/) - 2-pointer Approach | :white_check_mark: | Unavailable public link | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/LeetCode/LC18-4sum(2-pointer).cpp) | 20/12/2023 |
| [LC 454 - 4Sum II](https://leetcode.com/problems/4sum-ii/) - 4Sum Approach | :white_check_mark: | Unavailable public link | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/LeetCode/LC454-4sum-ii(4sum).cpp) | 20/12/2023 |
| [LC 454 - 4Sum II](https://leetcode.com/problems/4sum-ii/) - k-Sum Approach | :white_check_mark: | Unavailable public link | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/LeetCode/LC454-4sum-ii(ksum).cpp) | 20/12/2023 |
