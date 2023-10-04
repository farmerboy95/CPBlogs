# Xác suất 101, bí ẩn đằng sau Martingales và các bài tập ứng dụng

## Nguồn

<img src="../../../assets/images/codeforces.png" width="16" height="16"/> [Probability 101, the intuition behind martingales and solving problems with them](https://codeforces.com/blog/entry/110801)

## Chú ý

**Đây là một bài dịch mình không thực sự hài lòng. Có lẽ là do mình không hiểu hết ý nghĩa mà tác giả muốn truyền tải. Bài này quá nặng về toán.**

## Lời tựa (của tác giả)

Gần đây có người nhờ tôi giải thích vài bài toán kiểu như: "Tìm thời gian kì vọng trước khi XYZ xảy ra". Để ý rằng thời gian hoàn thành là một biến ngẫu nhiên, và trong lý thuyết xác suất, những biến ngẫu nhiên như thế được gọi là "thời gian dừng" (rõ ràng rồi). Hoá ra các bài toán này có thể được giải bằng thứ được gọi là martingales, hay nói cách khác là những quy trình ngẫu nhiên với các hằng số đẹp đẽ cùng một đống các tính chất.

Tôi nghĩ nhiều người không hiểu những thứ đó cùng với việc vì sao chúng lại hữu dụng. Nên tôi hi vọng bài viết sẽ giúp các bạn hiểu sâu hơn. Lưu ý rằng với tinh thần rõ ràng, tôi sẽ chỉ xử lý các tập hữu hạn và các quy trình thời gian hữu hạn (trừ khi thực sự cần thiết, và trong các trường hợp như vậy, việc giải thích cần phải rõ ràng). Tôi làm điều này vì mọi người thường lạc lối trong các khía cạnh lý thuyết đo lường của sự chặt chẽ cần thiết và bỏ qua các điểm mấu chốt mà họ cần phải hiểu. Ngoài ra, lưu ý rằng dôi khi phần giải thích sẽ có nhiều phần hơn mức cần thiết, nhưng là để giúp các bạn hiểu sâu hơn là trình bày ngắn gọn nhưng khó hiểu.

Những người đã quen với các khái niệm ban đầu có thể bỏ qua các phần này và đi tới những phần thú vị hơn, nhưng tôi vẫn sẽ khuyên các bạn đọc toàn bộ phần giải thích trong trường hợp bạn khuất mắc chỗ nào đó. Khải niệm tập hợp "tối thiểu" được dùng rất nhiều ở đây về mặt tâm lý, vì vậy có thể bạn vẫn muốn đọc các phần có liên quan được giới thiệu trong blog này.

**BONUS**: Đây là một [bài báo khoa học](https://arxiv.org/pdf/2008.13017.pdf) nói về việc dùng martingales để giải các bài toán.

## Xác suất, đại số sigma và biến ngẫu nhiên

Đầu tiên ta cùng xem lại các định nghĩa đã được đơn giản hoá của không gian xác suất. Ta nói "đã được đơn giản hoá" vì có vài kỹ thuật cần được dùng cho tập vô hạn, nhưng ta sẽ không xét tập vô hạn ở đây.

Một **không gian xác suất** là bộ ba $(\Omega, \mathcal{F}, P)$ bao gồm

1. $\Omega$ một tập nền không rỗng, hay còn gọi là không gian mẫu. Nó còn có thể được xem là tất cả các kết quả có thể xảy ra của một phép thử.
2. $\mathcal{F}$: sigma-đại số. Đây là tập hợp bao gồm các tập con của $\Omega$. Lưu ý rằng đây không phải là tập bao gồm tất cả các tập con của $\Omega$ ([tập luỹ thừa](https://vi.wikipedia.org/wiki/T%E1%BA%ADp_l%C5%A9y_th%E1%BB%ABa) của $\Omega$). Có thể xem các phần tử của tập này (các tập con được chọn) là các "biến cố". Ví dụ, khi tung một cục xúc xắc, một biến cố có thể xảy ra là "tung ra số chẵn". Với phép thử này, ta có $\Omega = \{1, 2, 3, 4, 5, 6\}$, và biến cố này là $\{2, 4, 6\}$.
3. $P$: hàm xác suất, hàm ánh xạ từ $\mathcal{F}$ sang đoạn $[0, 1]$. Đây thực ra chỉ là trọng số ta gán vào mọi biến cố mà ta chọn.

Để hàm này có các tính chất hay ho và để nó tính xác suất một cách "có lý" hơn, ta thêm vào các điều kiện sau:

1. $\Omega$ là một biến cố (hay nói cách khác là $\Omega \in \mathcal{F}$).
2. Nếu $A \in \mathcal{F}$, thì $\Omega \setminus A \in \mathcal{F}$, nghĩa là nếu cái gì đó xảy ra là một biến cố, thì nó không xảy ra cũng là một biến cố.
3. Nếu $A \in \mathcal{F}$ và $B \in \mathcal{F}$, thì $A \cup B \in \mathcal{F}$. Nghĩa là, nếu $X$ xảy ra là một biến cố, $Y$ xảy ra cũng là một biến cố, thì ít nhất một trong $X$ và $Y$ xảy ra cũng là một biến cố. Lưu ý rằng điều này kết hợp với điều kiện 2 đó cho phép ta nói rằng $A \cap B$ cũng là một biến cố và các tính chất tương tự, theo luật De Morgan.
4. $P(\Omega) = 1$, nghĩa là xác suất của toàn bộ không gian mẫu là $1$.
5. Với các tập rời rạc $A$ và $B$, $P(A \cup B) = P(A) + P(B)$. Điều kiện này, kết hợp với điều kiện 4, là đủ để có được một số điều kiện được suy ra như $P(\emptyset) = 0$ hay $P(A) + P(\Omega \setminus A) = 1$.

Giờ ta hãy xây dựng một số hiểu biết về không gian xác suất. Lưu ý rằng, các đoạn sau đây, đặc biệt là phần nói về các tập tối thiểu, chỉ áp dụng cho các tập hữu hạn, nhưng có rất nhiều điểm tương đồng trong các kết luận khi ta khái quát hoá sang các tập khác với các khái niệm lý thuyết tính toán.

Để ý rằng vì $\mathcal{F}$ đóng kín với phép giao (tức là nếu $E_i \in \mathcal{F}$ thì giao của tất cả các bộ $E_i$ cũng phải thuộc $\mathcal{F}$, theo điều kiện 3), nếu ta thực hiện quá trình sau nhiều lần: lấy hai tập và thay thế chúng bằng giao của hai tập đó, đến cuối cùng ta sẽ chỉ còn các tập "tối thiểu" không rỗng mà ta không thể nào cực tiểu thêm (điều này thực sự không chuẩn lắm nhưng ta sẽ dùng rất nhiều trong các phần sau). Xét tất cả các tập tối thiểu như thế. Rõ ràng, các tập này tạo thành các phân hoạch của $\Omega$ vì chúng rời rạc (nếu không sẽ mâu thuẫn với tính tối giản) và vì mọi phần tử đều nằm trong một tập tối giản (với thực tế là $\mathcal{F}$ đóng kín với phép bù, theo điều kiện 1, và xây dựng một tập tối thiểu nếu cần, hoặc chỉ bằng cách giao tất cả các tập chứa phần tử đó - có ít nhất một tập như vậy, đó là $\Omega$). Giờ $\mathcal{F}$ đóng kín với phép hợp (theo điều kiện 3), nên nó cũng bằng tập của tất cả các hợp có thể có của các tập con tối thiểu này. Nói cách khác, ta có một phân hoạch các phần tử của $\Omega$ thành một số tập hợp, và $\mathcal{F}$ là tập hợp được tạo thành bởi tất cả các hợp có thể có của các tập hợp trong phân hoạch đó. Bây giờ ta có thể nghĩ về các $\sigma$-đại số dưới dạng phân hoạch! Ngoài ra, lưu ý rằng xác suất của mỗi biến cố tối thiểu của $\sigma$-sigma sẽ cộng lại khi lấy các hợp.

Trong một số trường hợp, ta có thể xây dựng một không gian mẫu tương đương $(\Omega', \mathcal{F}', P')$ với $\Omega'$ là tập các biến cố tối thiểu của $\mathcal{F}$, $\mathcal{F}'$ là tập luỹ thừa của $\Omega'$ và $P'$ được định nghĩa tự nhiên từ $P$. Định nghĩa này không tiêu chuẩn lắm nhưng sẽ có ích về sau. Lưu ý rằng nếu $\mathcal{F}$ là tập luỹ thừa của $\Omega$, thì không gian mẫu tương đương sẽ giống như không gian mẫu ban đầu. Trong trường hợp này, tất cả các $\sigma$-đại số khác sẽ thô hơn tập luỹ thừa, với các tập tối thiểu của chúng đều là các phần tử đơn lẻ.

Đến bước này, ta nhận ra rằng $\mathcal{F}$ chỉ ra ta có bao nhiêu "thông tin" về $\Omega$ (ta không thể phân biệt hai phần tử trong cùng một tập tối thiểu). Ý tưởng này cùng với kiến thức phân hoạch ở trên là một cách tốt để tìm ra cách thu thập thông tin theo thời gian trong các tiến trình ngẫu nhiên. Ta sẽ đến bước đó sau.

Giờ ta đến định nghĩa chính thức của một biến ngẫu nhiên.

Một **biến ngẫu nhiên** đối với một không gian xác suất $(\Omega, \mathcal{F}, P)$ là hàm $X$ ánh xạ từ $\Omega$ sang $\mathbb{R}$ mà $X^{-1}((-\infty, x]) \in \mathcal{F}$ với mọi $x \in \mathbb{R}$. Nghĩa là, tập tiền đề của các số thực $\le x$ thuộc $\mathcal{F}$.

Lưu ý rằng do ta đang xét các tập hữu hạn, ta sẽ dùng một định nghĩa khác (nhưng tương đương với tập hữu hạn), định nghĩa này cho phép ta thay đoạn bằng $(-\infty, x]$ $\{x\}$.

Viết như thế này có thể trông hơi đáng sợ nhưng ý tưởng thì lại khá đơn giản. Ta có một không gian mẫu $\Omega$, và có một tập $\mathbb{R}$. Giờ ta muốn ánh xạ các phần tử của $\Omega$ sang $\mathbb{R}$ bằng cách nào đó sao cho ta có thể tính toán trên các phần tử của $\Omega$. Tuy nhiên, trong một không gian mẫu, $\mathcal{F}$ cho ta biết ta có bao nhiêu thông tin (hoặc cho ta thấy bao nhiêu thông tin), ta không thể phân biệt được các phần tử trong $\Omega$ nằm trong cùng một biến cố tối thiểu của $\mathcal{F}$. Do có hữu hạn các phần tử trong $\Omega$, và các phần tử nằm trong cùng một biến cố tối thiếu nên được ánh xạ sang cùng một số thực, sẽ chỉ có hữu hạn các đoạn mà $X$ phân hoạch $\mathbb{R}$ ra, và đó cũng là tất cả các điều kiện cần và đủ của định nghĩa (do tính đóng của $\mathcal{F}$ với phép giao và hợp).

Thêm một lưu ý nữa là ta cũng có thể định nghĩa các hàm của một biến ngẫu nhiên ở bước này bằng cách kết hợp hàm $X$ với một hàm ánh xạ từ $\mathbb{R}$ sang $\mathbb{R}$. Tương tự, nếu ta có hai biến ngẫu nhiên trên cùng một không gian mẫu, ta cũng có thể định nghĩa các hàm của chúng một cách khá tự nhiên. Sau cùng, ta chỉ cần chỉ định các giá trị của chúng trên các tập tối thiểu là xong.

## Giá trị kì vọng của một biến ngẫu nhiên và xác suất có điều kiện

Giả sử ta có một không gian mẫu $(\Omega, \mathcal{F}, P)$ và một biến ngẫu nhiên $X$ trên không gian mẫu này. Làm sao để ta tìm được một số loại giá trị trung bình của $X$ trên toàn bộ không gian xác suất? Một đáp án có thể là: với mỗi sự kiện tối thiểu, ta xét giá trị chung của biến ngẫu nhiều tại mỗi phần tử của biến cố đó, và thêm nó vào một tổng trọng số với trọng số bằng với xác suất của biến cố tối thiểu đó. Lưu ý rằng một số biến cố tối thiểu tạo một phân hoạch nên tổng các trọng số này là $1$. Trong một số trường hợp, đây là giá trị trung bình của biến ngẫu nhiên trên tất cả các biến cố tối thiểu, được tính trọng số theo độ quan trọng của chúng.

Nhưng mà làm sao ta có thể viết chúng theo kiểu toán học mà không liên quan gì đến biến cố tối thiểu? Cùng xem lại điều kiện trong định nghĩa biến ngẫu nhiên. Thay vì tổng các biến cố tối thiểu, ta có thể lấy tổng các giá trị $x$ khác nhau của biến ngẫu nhiên, và đánh trọng số chúng bằng xác suất để biến đó bằng $x$. Xác suất này được xác định rõ do điều kiện trong định nghĩa của biến ngẫu nhiên (vì biến cố có biến ngẫu nhiên bằng $x$ là hợp rời rạc của các biến cố tối thiểu và xác suất của chúng cộng lại). Định nghĩa này cũng phù hợp với các hiểu biết trước đó của chúng ta.

Vì thế nên ta có thể định nghĩa **giá trị kì vọng của một biến ngẫu nhiên** $X$ là $E[X] := \sum_{x \in \text{range}(X)} x \cdot P(X = x)$.

Lưu ý rằng với định nghĩa trước đó liên quan đến biến cố tối thiểu, ta cũng dễ dàng suy ra được với bất kỳ biến ngẫu nhiên $X$, $Y$ nào trên cũng một không gian xác suất, ta có $E[X + Y] = E[X] + E[Y]$.

Giờ hãy xem làm sao ta có thể cô lập một biến cố. Giả sử ta có biến cố $E$. Ta muốn bỏ qua tất cả những thứ khác và chỉ tập trung vào các phần tử của $\Omega$ (bao gồm các biến cố tối thiểu của $\mathcal{F}$ tạo thành một phân hoạch của $E$). Ta có thể tạo ra một không gian xác suất cho nó hay không? Một cách đơn giản là kế thừa cấu trúc của $\Omega$ và $\mathcal{F}$ và tập các xác suât của mọi thứ dùng các phần tử không phải tối thiểu cấu thành $E$ là $0$, nhưng ta lại gặp một rắc rối nếu ta chỉ kế thừa hàm xác suất. Tổng xác suất của tất cả các biến cố tối thiểu không bằng $1$. Một cách giải quyết là chuẩn hoá nó bằng $P(E)$, điều này khả thi khi và chỉ khi nó khác $0$. Có thể dễ dàng kiểm tra không gian xác suất này thực sự là một không gian xác suất hợp lệ.

Đây là cách ta định nghĩa không gian xác suất có điều kiện đối với một biến cố $E$ với $P(E) > 0$. Không gian mẫu và $\sigma$-đại số giữ nguyên nhưng hàm xác suất trở thành $P(A | E) := P'(A) = P(A \cap E) / P(E)$. Không gian xác suất có điều kiện này là phù hợp với các lập luận trước đó bằng cách xem xét các phần tử tối thiểu.

Một cách nhìn rõ ràng hơn là chúng ta chỉ thực sự quan tâm đến một số tập con của $\Omega$ và $\mathcal{F}$ tương ứng với các phần tử trong $E$, và chúng ta định nghĩa một không gian xác suất với $E$ là tập cơ sở. Nhưng để dám chắc rằng ta có thể tương tác với các biến cố khác trong $\mathcal{F}$, ta lấy biến cố đó, cắt bớt các phần không có trong $E$, sau đó sử dụng xác suất (hoặc trọng số tương đố) của tập hợp đó đối với xác suất (hoặc trọng số) của $E$.

Một hệ quả tất yếu của điều này là: $\sum_{E_i} P(A | E_i) P(E_i) = P(A)$ với một phân hoạch của $\Omega$ trong biến cố $E_i$. Ta có thể thấy điều này đúng khi chỉ xét các tập tối thiểu trong $A$. Trong thực tế, điều này được dùng để giải rất nhiều liên hệ lặp lại, như trong định lý Bayes.

Nó cũng có biến thể liên quan đến giá trị kì vọng, và nếu ta hạn chế một biến ngẫu nhiên trong từng không gian xác suất có điều kiện, bằng cách tổng hợp các tập tối thiểu, ta sẽ thấy rằng nếu $E[X | E_i]$ là giá trị kì vọng của $X$ đối với không gian xác suất có điều kiện đối với $E_i$, thì $\sum_{E_i} E[X | E_i] P(E_i) = E[X]$. Biến thể này cũng được dùng trong liên hệ lặp lại, như việc tìm thời gian kì vọng trước khi ta tung ra được hai mặt trên đồng xu liên tiếp (mặc dùng không gian mẫu này vô hạn, các tính chất vẫn được giữ nguyên).

## Kì vọng có điều kiện của một biến ngẫu nhiên đối với đại số sigma

Ở trên ta đã định nghĩa không gian xác suất tương đương. Nó ứng với việc thu gọn các lớp tương đương (được xác định bởi phân hoạch) thành một phần tử duy nhất, để tạo ra một không gian xác suất trên đó làm không gian mẫu. Điều gì sẽ xảy ra nếu chúng ta làm vậy lần nữa, sau khi xác định một không gian xác suất thưa / thô hơn trên không gian xác suất thu được?

Tất nhiên, điều này sẽ dẫn đến một phân vùng thô hơn của không gian mẫu trong vài trường hợp, và nếu $\mathcal{F}_1$ là $\sigma$-đại số gốc, $\mathcal{F}_2$ là $\sigma$-đại số mới (cả hai đều ứng với cùng $\Omega$, sau khi mở lần làm thô thứ hai), thì $\mathcal{F}_2 \subseteq \mathcal{F}_1$.

Giờ giả sử ta có một biến ngẫu nhiên $X$ trên không gian xác suất ban đầu. Làm sao ta điều chỉnh / giảm biến ngẫu nhiên thành không gian xác suất thô hơn này đây? Đây là nơi giá trị kì vọng xuất hiện. Ta sẽ chọn một định nghĩa cho kì vọng có điều kiện và thấy rằng nó thoả mãn nhiều tính chất hay ho và phù hợp với các đồng nhất xác suất có điều kiện mà ta tìm được trong phần trước.

Lưu ý rằng $X$ là hằng số trên tất cả tập tối thiểu của $\mathcal{F}_1$. Định nghĩa **kì vọng có điều kiện của $X$ đối với $\sigma$-đại số $\mathcal{F}_2$** là biến ngẫu nhiên $E[X | \mathcal{F_2}] := X'$ mà trên mọi phần tử của tập tối thiểu $E_i$ của $\mathcal{F}_2$, $X'$ là giá trị của $E[X | E_i]$. Điều này nghĩa là ta đang cố gắng lấy "trung bình có điều kiện" của thông tin về các giá trị của $X$ trên tập $E_i$. Dễ thấy $E[X'] = E[X]$, nơi mà kì vọng đầu tiên được thực hiện trên không gian xác suất thô hơn, và kì vọng thứ hai được lấy trên không gian xác suất sau đó. $X'$ được gọi là kì vọng có điều kiện của $X$ đối với $\sigma$-đại số $\mathcal{F}_2$.

Để dễ hiểu hơn, ta xét ví dụ sau:

??? tip "Ví dụ"
    Cho một không gian mẫu $(\Omega, \mathcal{F}_1, P)$, một biến ngẫu nhiên $X$ trên không gian mẫu này, và một $\sigma$-đại số $\mathcal{F}_2 \subseteq \mathcal{F}_1$ như sau:

    1. $\Omega = \{1, 2, \dots, 10\}$.
    2. $\mathcal{F}_1$ có các tập tối thiểu $\{1, 2, 3\}, \{4\}, \{5, 6\}, \{7\}, \{8, 9, 10\}$.
    3. $P(S)$ của các tập tối thiểu $S$ lần lượt là $1/8, 1/8, 1/4, 1/3, 1/6$.
    4. $\mathcal{F}_2$ có các tập tối thiểu $\{1, 2, 3, 5, 6\}, \{4\}, \{7, 8, 9, 10\}$.
    5. $X$ có các giá trị $[1, 1, 1, 2, 3, 3, 3, 4, 4, 4]$ lần lượt cho $[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]$.

    Thì $E[X | \mathcal{F}_2]$ được xác định như sau:

    1. Trên tập tối thiểu $S = \{1, 2, 3, 5, 6\}$, kì vọng có điều kiện $E[X | S] = (1/8 + 3/4) / (1/8 + 1/4) = 7/3$.
    2. Trên tập tối thiểu $S = \{4\}$, kì vọng có điều kiện $E[X | S] = 2$.
    3. Trên tập tối thiểu $S = \{7, 8, 9, 10\}$, kì vọng có điều kiện $E[X | S] = (3/3 + 4/6) / (1/3 + 1/6) = 10/3$.

    Nên biến ngẫu nhiên $E[X | \mathcal{F}_2]$ lấy các giá trị $[7/3, 7/3, 7/3, 2, 7/3, 7/3, 10/3, 10/3, 10/3, 10/3]$ lần lượt cho $[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]$.

Ta có vài lưu ý sau:

1. Theo một cách nào đó, ta đang cố gắng thay thế biến ngẫu nhiên bằng "xấp xỉ tốt nhất" của nó theo một nghĩa nào đó (ví dụ như nghĩa giảm thiểu phương sau, nhưng điều đó hoàn toàn không liên quan). Cũng lưu ý rằng kỳ vọng của biến ngẫu nhiên không thay đổi khi áp dụng điều này cho $X$.
2. Với $\sigma$-đại số đơn giản $\mathcal{F}_2 = \{\emptyset, \Omega\}$, biến ngẫu nhiên $E[X | \mathcal{F_2}]$ đồng nhất với hàm hằng bằng $E[X]$.

Ta cũng có thể xâu chuỗi một vài phần thô. Giả sử $\mathcal{F}_3 \subseteq \mathcal{F}_2 \subseteq \mathcal{F}_1$ và $X$ là một biến ngẫu nhiên đối với không gian xác suất $(\Omega, \mathcal{F}_1, P)$. Thì ta sẽ có $E[E[X | \mathcal{F}_2] | \mathcal{F}_3] = E[X | \mathcal{F_3}]$, có thể được chứng minh dễ dàng bằng cách xâu chuỗi các kỳ vọng có điều kiện. Trên thực tế, kỳ vọng vẫn giữ nguyên ngay cả khi làm thô là hệ quả trực tiếp của điểm này và điểm cuối cùng.

Một thuật ngữ được sử dụng phổ biến hơn là kỳ vọng có điều kiện đối với một biến ngẫu nhiên khác. Nó thường được định nghĩa như sau:

Giả sử $X$ và $Y$ là các biến ngẫu nhiên trên cùng không gian xác suất. Với bât kỳ phần tử $\omega$ nào của không gian mẫu mà $Y(\omega) = y$, ta định nghĩa $E[X | Y]\left(\omega\right) = E[X | E]$ với $E$ là biến cố mà $Y = y$. Nghĩa là, với mọi phần tử mà $Y$ có giá trị giống $y$, ta lấy kỳ vọng có điều kiện đối với biến cố mà $Y = y$ và đặt giá trị của đáp án cho kỳ vọng có điều kiện đó.

Tuy nhiên, điều ở trên cũng giống như: cho $\mathcal{F}_Y$ là $\sigma$-đại số mà các tập tối thiểu tương ứng với các giá trị khác nhau của $Y$. Khi đó $E[X | Y]$ sẽ đồng nhất với biến ngẫu nhiên $E[X | \mathcal{F}_Y]$. Lưu ý rằng $\sigma$-đại số này được gọi là $\sigma$-đại số được tạo ra bởi biến ngẫu nhiên $Y$.

Theo nghĩa này, kỳ vọng có điều kiện đối với một $\sigma$-đại số là một khái niệm rõ ràng và phức tạp hơn kỳ vọng có điều kiện đối với một biến ngẫu nhiên, mặc dù cả hai khái niệm đều tương đương (bạn luôn có thể tạo ra một $\sigma$-đại số bằng cách chọn nơi để đặt các giá trị bằng nhau cho biến ngẫu nhiên mà bạn đang điều chỉnh).

Một cách khác để suy nghĩ về khái niệm này là coi nó như là sự ánh xạ từ một tập hợp các biến cố tối thiểu sang một tập hợp các biến cố tối thiểu thô hơn. Đối với mỗi nhóm biến cố tối thiểu mà ta đang thu gọn, ta thay thế nó bằng một biến cố tối thiểu duy nhất bằng "tâm khối lượng" của các biến cố đó, trong đó "vị trí" là giá trị của biến ngẫu nhiên và "khối lượng" bằng với xác suất của các biến cố tối thiểu đó. Điều này cũng đúng về mặt toán học và chính xác cho setup này.

Để cho đầy đủ, vì định nghĩa trên nắm bắt được kỳ vọng có điều kiện đối với $\sigma$-đại số, nhưng không hoạt động khi cố gắng tổng quát nó cho các không gian mẫu vô hạn, đây là "định nghĩa chính thức" mà mọi người sử dụng (khá là phản trực giác và mất chút thời gian để hiểu rõ):

Một biến cố có điều kiện $X$ với $\mathcal{H}$ cho trước, ký hiệu là $E[X | \mathcal{H}]$, là bất kỳ biến ngẫu nhiên nào trên $(\Omega, \mathcal{H}, P)$ thoả mãn $\int_H E[X | \mathcal{H}] d\mathbb{P} = \int_H X d\mathbb{P}$ với mọi $H \in \mathcal{H}$.

Về cơ bản, định nghĩa này nói lại y hệt những gì ta đã bàn khi bạn nghĩ về khả năng $H$ có thể xảy ra, nhưng theo cách không mang tính xây dựng hơn. Hoá ra biến ngẫu nhiên này không phải là duy nhất theo nghĩa chặt chẽ nhất, nhưng $P(Y \ne Z) = 0$ đúng, trong đó $Y$ và $Z$ là hai biến của biến ngẫu nhiên này. Ngoài ra, định nghĩa này làm rõ rằng $X - E[X | \mathcal{H}]$  trực giao với hàm chỉ báo (vì vậy ta có dịnh nghĩa chính xác hơn về phép chiếu xuống).

## Martingales

Giả sử ta có một "tiến trình", mà ở mỗi bước, ta có thêm thông tin. Giả sử không gian mẫu của chúng ta cho toàn bộ phép thử là $\Omega$. Ở đây, $\Omega$ gần như luôn vô hạn, nhưng với những hiểu biết trước đó, ngay cả khi những khái niệm như tập tối thiểu không dành cho không gian mẫu vô hạn. Ta xét một ví dụ đơn giản, với mỗi bước, ta tung đồng xu. Không gian mẫu của toàn bộ phép thử là tập của tất cả các xâu nhị phân vô hạn. Giờ ta hãy nghĩ về loại thông tin mà ta sẽ có sau nhiều bước của tiến trình. Sau bước $0$, tất cả thông tin ta có (ví dụ, thông tin hoàn chỉnh về một biến ngẫu nhiên mà có thông tin về những thứ đã xảy ra đến thời điểm hiện tại) ứng với $\sigma$-đại số đơn giản $\{\emptyset, \Omega\}$. Sau bước thứ $i$, ta có thông tin về $i$ lần tung đầu tiên, nên thông tin ứng với $\sigma$-đại số với các tập "tối thiểu" chính là các tập các xâu nhị phân mà giống nhau trong $i$ vị trí đầu tiên.

Để hiểu vì sao các $\sigma$-đại số cần thiết để lấy thông tin, phép loại suy sau có thể có ích. Hãy suy nghĩ về các tập tối thiểu. Mỗi lần ta lấy thêm thông tin, ta có thể phân biệt được các phần tử trong tập tối thiểu. Để có thể thực hiện các thao tác như tìm kỳ vọng của một số biến ngẫu nhiên trong trường hợp này, ta cần phải có khả năng phân biệt các phần tử này. Theo một nghĩa nào đó, bạn đang kiểm tra nhiều vũ trụ song song cùng một lúc, và trong mỗi vũ trụ, bạn có một tiền tố nhất định về những thứ đã xảy ra, đối với mỗi sự việc mà bạn muốn phân tích được những gì sẽ xảy ra tiếp theo.

Lưu ý rằng ta luôn lấy thêm thông tin ở mỗi giai đoạn của một tiến trình ngẫu nhiên như vậy. Nên ta định nghĩa một bộ lọc như sau (mà không có bất kỳ tham chiếu nào đến một tiến trình vì mục đích tổng quát): một dãy các $\sigma$-đại số $\mathcal{F}_i$ mà $\mathcal{F}_i \subseteq \mathcal{F}_j$ khi và chỉ khi $i \le j$

Vậy thì tiến trình là cái gì? Ở mỗi bước của một tiến trình, ta có một biến ngẫu nhiên xuất hiện. Nhưng $\sigma$-đại số của biến ngẫu nhiên đó là gì? Để khắc phục, ta lấy một $\sigma$-đại số $\mathcal{F}$ mà nó lấy được toàn bộ thông tin có thể có. Vậy nên ta định nghĩa một tiến trình ngẫu nhiên như sau:

Với một không gian xác suất $(\Omega, \mathcal{F}, P)$, một tập đánh dấu $I$ với tổng thứ tự $\le$, một tiến trình ngẫu nhiên $X$ là bộ các biến ngẫu nhiên $\{X(i) | i \in I\}$.

Với mục đích của chúng ta, $I$ sẽ gần như là các số nguyên không âm, mặc dù $I = \mathbb{R}$ được dùng rộng rãi trong nhiều tình huống. $I$ có tổng thứ tự nghĩa là có một số khái niệm về thời gian liên quan đến $I$.

Giờ làm sao để ta xây dựng được một "bộ lọc tự nhiên" để lấy thông tin mà $i$ bước đầu tiên của tiến trình (nghĩa là $\{X(j) | j \le i\}$) cho chúng ta? Nhớ lại làm sao để xây dựng một $\sigma$-đại số từ một biến ngẫu nhiên không? Ta cũng có thể dùng thứ tương tự để xây dựng nó từ một tập hữu hạn các biến ngẫu nhiên, bằng cách tinh chỉnh hai phân hoạch với nhau khi có thể (tương đương với phép nối hai phân hoạch trong mạng tinh chế, nếu bạn quen với tập thứ tự một phần và mạng tinh thể). Vì vậy quá trình lọc có thể được thiết lập theo cách này, bằng cách tinh chỉnh $\sigma$-đại số hiện tại với một biến ngẫu nhiên mới mỗi lần. Ta có diễn giải từ Wikipedia, 

Với ${\displaystyle (X_{n})_{n\in \mathbb {N} }}$ là một tiến trình ngẫu nhiên trên không gian mẫu ${\displaystyle (\Omega ,{\mathcal {F}},P)}$. Thì

$${\displaystyle {\mathcal {F}}_{n}:=\sigma (X_{k}\mid k\leq n)}$$

là một $\sigma$-đại số và ${\displaystyle \mathbb {F} =({\mathcal {F}}_{n})_{n\in \mathbb {N} }}$ là một bộ lọc. Ở đây ${\displaystyle \sigma (X_{k}\mid k\leq n)}$ thể hiện rằng $\sigma$-đại số được sinh ra từ các biến ngẫu nhiên ${\displaystyle X_{1},X_{2},\dots ,X_{n}}$. ${\mathbb F}$ là một bộ lọc, vì với định nghĩa tất cả ${\displaystyle {\mathcal {F}}_{n}}$ là $\sigma$-đại số và ${\displaystyle \sigma (X_{k}\mid k\leq n)\subseteq \sigma (X_{k}\mid k\leq n+1)}$.

Thứ này được biến đến như bộ lọc tự nhiên của ${\displaystyle {\mathcal {F}}}$ đối với $X$.

Cuối cùng, ta cũng có thể định nghĩa martingale. Lưu ý rằng nếu $\sigma(X_i) \subseteq \mathcal{H}$ với một số $\sigma$-đại số $\mathcal{H}$, thì $E[X_i | \mathcal{H}] = X_i$ (nhớ lại tập tối thiểu và định nghĩa). Một martingale nói rằng tính điều kiện dựa trên thông tin chúng ta có đến thời điểm $i$, một biến ngẫu nhiên $X_j$ với $j \ge i$ trông giống như $X_i$. Nói cách khác,

Một **martingale** là một tiến trình ngẫu nhiên $X_1, X_2, \ldots$ mà $E[X_{n + 1} | \sigma(X_1, X_2, \dots, X_n)] = X_n$

Điều kiện đầu tiên có thể được viết thành $E[X_{n + 1} - X_n | \sigma(X_1, X_2, \dots, X_n)] = 0$. Lưu ý rằng ta đang bàn về sự bằng nhau "gần như chắc chắn" của các biến ngẫu nhiên khi xử lý các không gian xác suất phức tạp hơn, nhưng vì mục tiêu, ta sẽ không quan tâm đến chi tiết này.

Lưu ý rằng đây là điều kiện cần và đủ, bởi $X_j - X_i = (X_j - X_{j - 1}) + (X_{j - 1} - X_{j - 2}) + \dots + (X_{i+1} - X_i)$, và thêm vào tính chất lồng nhau thô, nó gia giảm thành $E[X_j - X_i | \sigma(X_1, \dots, X_i)] = 0$.

Tại sao martingale hữu ích? Đầu tiên, nó cho chúng ta một bất biến, và như ta đã biết, các bất biến làm mọi thứ dễ dàng hơn khi chứng minh các kết quả trong toán học. Thứ hai, nó bắt nguồn từ lý thuyết cờ bạc và đối với các trò cờ bạc công bằng, giá trị lợi nhuận kì vọng tại thời điểm sau phải bằng với lợi nhuận tại thời điểm đó, đó chính là điều kiện của martingale!

Một số cách xây dựng martingale như sau:

1. Xét việc đi bộ ngẫu nhiên, với vị trí đầu là $X_0 = 0$, và $X_i = X_{i-1} \pm 1$, với xác suất bằng nhau $p \le 1/2$, và $X_i = X_{i-1}$ với xác suất $1-2p$. Thì đây là một martingale (theo định nghĩa).
2. Xét việc đi bộ ngẫu nhiên biểu thị tổng tài sản của một bet thủ, anh ta luôn tái đầu tư vốn của mình vào trò chơi. Trò này trả $r$ phần trăm nếu anh ta thắng (xác suất là $p$), mất $r$ phần trăm nếu anh ta thua (xác suất là $p$), và tài sản giữ nguyên nếu hoà (xác suất $1-2p$). Thì tài sản của anh ta là một martingale.

Giờ ta xét kì vọng có điều kiện trong định nghĩa của martingale khi ta áp dụng hàm lồi cho một tiến trình ngẫu nhiên (nghĩa là cho tất cả các biến ngẫu nhiên trong tiến trình ngẫu nhiên). Vì các xác suất đều dương, nên bất cứ khi nào chúng ta lấy kì vọng có điều kiên, ta sẽ lấy một tổ hợp lồi các giá trị của hàm lồi của một biến ngẫu nhiên. Theo bất đẳng thức Jensen, ta nhận được điều đó thay vì đẳng thức, $\ge$ đúng trong phương trình định nghĩa cho martingale. Tương tự, nếu ta có một hàm lõm, $\le$ đúng trong phương trình định nghĩa cho martingale. Các loại tiến trình này (trong đó $\ge$ và $\le$ được giữ thay vì $=$) được gọi lần lượt là sub-martingale và super-martingale. Lưu ý rằng không phải tất cả tiến trình ngẫu nhiên đều phải là sub hoặc super-martingale. Thêm nữa là $\ge 0$ và $\le 0$ nghĩa là biến ngẫu nhiên trên LHS (Latin hypercube sampling) lần lượt gần như chắc chắn không âm và không dương.

Một ví dụ về sub-martingale:

??? tip "Ví dụ"
    Giả sử ta có martingale $X$. Ta nói $X^2$ là một sub-martingale. Theo bất đẳng thức Jensen, $\sum_{i = 1}^N \lambda_i f(x_i) \ge f \left(\sum_{i = 1}^{N} \lambda_i x_i\right)$, với $f$ lồi và $\lambda_i$ không âm có tổng bằng $1$. Áp dụng điều này khi làm thô các tập tối thiểu của $\sigma$-đại số mịn hơn (khi lấy kì vọng có điều kiện) cho ta $E[X_{N + 1}^2 \mid \sigma(X_{i}^2)_{i = 0}^{N}] \ge X_N^2$, chứng minh được $X^2$ là sub-martingale. Trong thực tế, trong trường hợp $X_n$ là độ may mắn của người cá cược khi lợi nhuận và thua lỗ (có độ lớn bằng nhau) có khả năng xảy ra như nhau, $X_n^2 - n$ là một martingale. Lưu ý rằng trong định nghĩa tổng quát nhất của martingale, bạn có thể dùng bộ lọc trước đó ($\sigma(X_i)$). Để làm được điều đó, tất cả những thứ cần thiết là để tiến trình thích ứng với bộ lọc, nhưng vì ta đã định nghĩa martingale trên bộ lọc tự nhiên, ta đã tiếp tục với một bộ lọc rõ ràng hơn.

Ta sẽ không đi quá sâu vào martingale (vì nó xứng đáng có một ngành nghiên cứu riêng), nhưng ta sẽ xem một vài tính chất hay ho:

1. **Bất đẳng thức Azuma**: Nó cho ta một giới hạn về mức độ "đóng" của ta với giá trị ban đầu của biến ngẫu nhiên, với các giới hạn chuyển động của martingale (hoặc ta đã đi sai hướng bao xa bới một sub / super-martingale). Gọi $\{X_k\}$ là một super-martingale (cũng là martingale), và giả sử $|X_k - X_{k - 1}| \le c_k$ là gần như chắc chắn. Thì ta có $P(X_N - X_0 \ge \varepsilon) \le \exp(-\varepsilon^2/(2 \sum_{k = 1}^N c_k^2))$. Vì âm của super-martingale là sub-martingale, với sub-martingale $X$, ta sẽ có $P(X_N - X_0 \le -\varepsilon) \le \exp(-\varepsilon^2/(2 \sum_{k = 1}^N c_k^2))$.Vì martingale vừa là sub-martingale, vừa là super-martingale, ta có một giới hạn xác suất về độ gần của $X_N$ với $X_0$, nghĩa là $P(|X_N - X_0| \ge \varepsilon) \le 2 \exp(-\varepsilon^2/(2 \sum_{k = 1}^N c_k^2))$. Có một phiên bản mạnh hơn của bất đẳng thức này nhưng như trên đã là đủ để thấy được martingale tốt như thế nào. 
2. **Bất đẳng thức martingale Doob**: Đây là bất đẳng thức kiểu Markov trên xác suất mà một sub-martingale sẽ vượt quá $x$. Nói cách khác, với một sub-martingale $X$, ta có $P(\max_{1 \le i \le n} X_i \ge x) \le E[\max(X_n, 0)] / x$. Điều này cũng được dùng để cho thấy bất đẳng thức Markov
3. **Định lý hội tụ martingale Doob**: Đây là hệ quả cho rằng super-martingale bị chặn dưới sẽ hội tụ (gần như chắc chắn) thành một biến ngẫu nhiên với kỳ vọng hữu hạn. Lưu ý rằng nếu ta chặn trường hợp khi biến số phân kỳ đến vô hạn theo nghĩa nào đó, thì cách khả dĩ khác để nó không hội tụ là dao động. Bất đẳng thức này đại khái nói rằng các martingale có giới hạn thì không dao động.

## Thời gian dừng (Stopping times)

Thời gian dừng khá là thú vị trong toán học, và khi kết hợp với martingale, chúng sẽ cho ra nhiều kết quả thú vị không kém và là một công cụ rất mạnh mẽ.

Giả sử ta đang trong hoàn cảnh của người chơi bạc, và ta muốn viết một thuật toán để kết thúc trò chơi, tuỳ vào một số kết quả nhất định trong tiến trình này. Thời gian dừng là một cách để chính thức hoá phân tích khi đạt đến các điều kiện thoát như vậy. Điều tốt nhất mà ta có thể làm, dựa trên lý thuyết hiện tại mà ta có, là định nghĩa nó như một biến ngẫu nhiên (có thể phụ thuộc hoặc không phụ thuộc vào tiến trình ngẫu nhiên). Ta cũng có hạn chế là không thể thấy trước tương lai, vì vậy quyết định về thời điểm dừng phải được đưa ra với tất cả các thông tin ở thời điểm hiện tại.

Xét một biến ngẫu nhiên $\tau$ (lấy giá trị trong tập đánh dấu, là tập chứa các số nguyên không âm) trên không gian xác suất $(\Omega, \mathcal{F}, P)$, và giả sử ta có một tiến trình ngẫu nhiên $X$ trên cùng không gian xác suất với bộ lọc liên quan $\{\mathcal{F}_i\}$. Ta gọi $\tau$ là **thời gian dừng** nếu biến cố $\{\tau = t\}$ là một biến cố trong $\{\mathcal{F}_t\}$. Nghĩa là, quyết định dừng ở thời điểm $t$ phải được đưa với thông tin không nhiều hơn thông tin ta có ở thời điểm $t$. Để giữ tính nhất quán với việc đánh dấu số thực, ta thay đổi điều kiện thành $\{\tau \le t\}$ là một biến cố trong $\{\mathcal{F}_t\}$.

Để hiểu tại sao điều này đảm bảo việc không hướng tới tương lai, ta xét như sau. Nhóm các phần tử của $\Omega$ có thời gian dừng $\le t$ lại với nhau, với điều kiện là ta không thể phân biệt chúng nếu không có thông tin ở thời gian sau $t$. Tương tự, không thể xảy ra trường hợp hai phần tử của $\Omega$ trong cùng một tập tối thiểu của $\mathcal{F}_t$ có thời gian dừng khác nhau, khi không phải cả hai đều $> t$. Trong ví dụ tung đồng xu của chúng ta, điều sau sẽ hợp lý nếu bạn nghĩ về lý do vì sao bạn không có thời gian dừng cho 000010110... = 4 và cho 000011000... = 6.

Một cách khác để chính thức hoá điều tương tự là nói rằng tiến trình ngẫu nhiên (biểu thị việc dừng một tiến trình) được xác định bởi $Y_t = 0$ nếu $\tau < t$ và $1$, nếu không thì là một tiến trình thích ứng đối với bộ lọc, nghĩa là $\sigma(Y_t) \subseteq \mathcal{F}_t$ với mọi $t$.

Vì thời gian dừng là một chỉ số, nên ta có thể nghĩ cách đánh dấu tiến trình ngẫu nhiên với một số hàm của thời gian dừng. Nếu ta quay về định nghĩa biến ngẫu nhiên, rõ ràng là ta cần gán một giá trị cho nó ở mọi phần tử trong $\Omega$. Trong các trường hợp đơn giản, điều này không quan trọng, vì ta có thể tính giá trị của $\tau$ ở tập tối thiểu có phần tử này (cho giá trị này là $t$), và tính lại giá trị $X_t$ ở tập tối thiểu. Từ đây, rõ ràng $X_{\tau}$ là một biến ngẫu nhiên trên không gian xác suất gốc, và nó thể hiện giá trị của một tiến trình ngẫu nhiên khi kết thúc tiến trình. Cũng lưu ý rằng với lý do trên, $X_{\min(\tau, t)}$ là một biến ngẫu nhiên có $\sigma$-đại số là tập con của $\mathcal{F}_t$. $X_{\min(\tau, t)}$ ứng với một tiến trình **đã dừng**. nghĩa là ta đã dừng một tiến tình sau khi quá thời gian cho phép. Đây là những loại tiến trình rất quan trọng và đã được nghiên cứu rộng rãi.

Cái hay của martingale và thời gian dừng là chúng đường nghiên cứu rất nhiều, và có một số kết quả quan trọng mà mình sẽ ghi ra ở đây (không chứng minh), chúng có thể giúp ta giải rất nhiều bài toán cũng như xây dựng một hiểu biết xung quang martingale và thời gian dừng:

1. **Định lý giới hạn trung tâm martingale**: Đây là sự tổng quát hoá của định lý giới hạn trung tâm thông thường đối với martingale. Tiến trình liên quan là một martingale bình thường, nhưng với sự khác biệt giữa các giá trị liên tiếp được giới hạn bởi một giới hạn gần như chắc chắn cố định. Ta chọn thời điểm dừng như sau: tại mỗi bước $i + 1$, ta tính phương sai có điều kiện của $X_{i + 1}$ đối với $\mathcal{F}_i$, và tiếp tục thêm nó vào bộ đếm. Dừng khi bộ đếm lớn hơn một giá trị nhất định $\sigma^2$ (theo nghĩa nào đó, ta đang đợi cho đến khi lấy được phương sai đủ lớn). Nếu thời gian dừng là $\tau_\sigma$, thì biến ngẫu nhiên $X_{\tau_\sigma} / \sigma$ hội tụ tại một biến phân phối chuẩn với trung bình là $0$ và phương sai $1$, vì $\sigma$ có xu hướng đến $\inf$. Điều này cũng giả định rằng tổng phương sai phân kỳ.
2. **Định lý dừng tuỳ chọn Doob**: Đây là một định lý rất quan trọng, và rất hữu ích cho việc tính toán giá trị kì vọng của thời gian dừng. Nó nói về sự công bằng của martingale khi ta dừng sau một thời gian dừng ngẫu nhiên, theo nghĩa ta đã phát triển ở trên. Ta sẽ có $E[X_\tau] = E[X_0]$, và hoá ra điều này đúng nếu một trong ba điều kiện sau thoả mãn:
    - Thời gian dừng $\tau$ bị chặn trên.
    - Martingale bị chặn và thời gian dừng $\tau$ gần như chắc chắn hữu hạn ($P(\tau = \infty) = 0$).
    - Giá trị kì vọng của $\tau$ hữu hạn, và hiệu $X_{i+1}$ và $X_i$ bị chặn. Lưu ý rằng điều này có thể được dùng để tính thời gian dừng nếu ta thay đổi martingale một chút, ta sẽ thấy sau.

## Một số bài tập toán

Ta bắt đầu với một số bài toán mà tôi đã gặp trong những năm qua (xin lỗi vì không nhớ nguồn của một số bài).

### Bài 1

Cho một bet thủ có $n$ dollar và cá cược vô số lần. Phần thưởng vòng $i$ là $X_t$, với $X_t$ là một số nguyên bị chặn hai đầu bởi một số hằng số xác định. Ta biết $E[X_t|X_{t-1},\cdots,X_1]\geq c$ với $c > 0$. Giả sử xác suất bet thủ này hết tiền là $p(n)$. Có khi nào $\lim_{n\rightarrow \infty}p(n)=0$ không?

??? tip "Lời giải sơ bộ"
    Dùng bất đẳng thức Azuma bằng cách xây dựng sub-martingale bằng với tài sản ở thời gian $t$ trừ đi $ct$.

### Bài 2

Cho một bảng vô hạn, với một số thực không âm ở mỗi ô. Giả sử rằng với mỗi ô, số trong đó là trung bình của 4 ô liền kề. Chứng minh tất cả các số bằng nhau.

??? tip "Lời giải sơ bộ"
    Xây dựng một martingale, với tiến trình bên dưới là việc đi bộ ngẫu nhiên với biến ngẫu nhiên là số trên ô đang đứng. Giờ dùng định lý hội tụ martingale, và bạn có thể phải dùng thêm luật không-một Hewitt-Savage dựa trên cách bạn dùng hội tụ.

### Bài 3 (USA IMO 2018 Winter TST 1, P2)

Tìm tất cả các hàm $f\colon \mathbb{Z}^2 \to [0, 1]$ mà với bất kỳ số nguyên $x$, $y$ nào,

$$f(x, y) = \frac{f(x - 1, y) + f(x, y - 1)}{2}$$

??? tip "Lời giải sơ bộ"
    Xây dựng một martingale tương tự bài trước.

### Bài 4 (2022 Putnam A4)

Giả sử $X_1, X_2, \ldots$ là các số thực trong khoảng $[0, 1]$ được chọn độc lập và ngẫu nhiên. Cho $S=\sum_{i=1}^kX_i/2^i$, với $k$ là số nguyên dương nhỏ nhất mà $X_k < X_{k+1}$, hoặc $k = \inf$ nếu không có số nguyên nào như vậy. Tìm giá trị kì vọng của $S$.

??? tip "Lời giải sơ bộ"
    Biến tổng từng phần $S_n$ thành một martingale. Cách dễ nhất là trừ đi kì vọng của nó, sau đó kiểm tra xem nó có thực sự trở thành một martingale hay không. Giờ xác định thời gian dừng có liên quan một cách tự nhiên bằng cách sử dụng thuật toán được xác định trong bài tập, và áp dụng định lý dừng tuỳ chọn của Doob.

### Bài 5 (AGMC 2021 P1)

Trong một bữa tiệc nhảy, ban đầu hồ bơi gồm 20 nữ mà 22 nam, và có nhiều nam nữ nữa đang chờ ở ngoài. Ở mỗi vòng, một người trong hồ bơi được chọn ngẫu nhiên. Nếu bạn nữ được chọn, bạn đó sẽ mời một bạn nam trong hồ để nhảy cùng và cả hai rời khỏi buổi tiệc sau khi nhảy xong. Nếu bạn nam được chọn, bạn đó sẽ mời một bạn nữ và một bạn nam đợi ở ngoài để nhảy cùng, sau đó cả 3 bạn ở lại buổi tiệc. Buổi tiệc kết thúc khi chỉ còn (hai bạn) nam trong hồ bơi.

(a) Xác suất để buổi tiệc không bao giờ kết thúc là bao nhiêu?

(b) Người quản lý tiệc quyết định đảo ngược luật, nghĩa là nếu bạn nữ được chọn, bạn đó sẽ mời một bạn nữ và một bạn nam đợi ở ngoài để nhảy cùng, sau đó cả 3 bạn ở lại buổi tiệc. Nếu bạn nam được chọn, bạn đó sẽ mời một bạn nữ trong hồ để nhảy cùng và cả hai rời khỏi buổi tiệc sau khi nhảy xong. Buổi tiệc kết thúc khi chỉ còn (hai bạn) nam trong hồ bơi. Giá trị kì vọng của số vòng mà buổi tiệc có thể có là bao nhiêu?

??? tip "Lời giải sơ bộ"
    Dùng phép lặp lại để giải (a). Với (b), lưu ý rằng sự lặp lại thay đổi một chút. Gọi $X_n$ là tổng số người trong nhóm. Có một $c$ sao cho $X_n^2 + cn$ là một martingale không? Giờ áp dụng Định lý dừng tuỳ chọn Doob và xem điều gì xảy ra.

### Bài 6

Cho một con khỉ đánh phím ngẫu nhiên trên một cái bàn phím có bảng chữ cái là $\Sigma$. Với một xâu $w\in\Sigma^*$, gọi $w_1,\dots,w_n$ là các xâu không rỗng đồng thời là tiền tố và hậu tố của $w$. Chứng minh kì vọng số lần bấm phím của con khỉ cần làm là $\sum_{i=1}^n|\Sigma|^{|w_i|}$.

??? tip "Lời giải sơ bộ"
    Có hai cách tạo martingale ở đây. Nhìn vào hậu tố của kích thước $\min(\text{number of steps}, |w|)$. Ta tạo một biến ngẫu nhiên như sau: với mọi hậu tố hiện tại $s_i$ mà cũng là tiền tố của $w$, biến ngẫu nhiên bằng với $\sum_{s_i} |\Sigma|^{|s_i|}$. Hãy xem điều gì xảy ra khi ta thêm kí tự mới vào, đó có phải là martingale không? Ta có thể làm gì để tạo một cái không? Giờ dùng định lý dừng tuỳ chọn Doob xem.

    Một cách tự nhiên hơn là thông qua cách nhìn cá cược. Giả sử ở mỗi thời điểm $t$, một bet thủ mới đến và trả $1$ để chơi. Anh ta tái đầu tư lần cược ($|\Sigma|$ lần so với lần cược trước) nếu chữ cái tiếp theo là một phần của tiền tố khi anh ta bắt đầu chơi. Nếu anh ta thua, anh ta nghỉ và không làm gì. Giờ thì nó là martingale, và tổng tiền mà tất cả bet thủ trả cho nhà cái là giá trị kì vọng của thời gian dừng.

Một cách giải khác cho bài này là ở [đây](https://codeforces.com/blog/entry/98808)

### Bài 7 (Alon, Spencer)

Cho đồ thị $G=(V,E)$ với số màu $\chi(G)=1000$. Gọi $U \subseteq V$ là tập con ngẫu nhiên của $V$ được chọn từ tất cả $2^{|V|}$ tập con của $V$. Gọi $H=G[U]$ là đồ thị con suy biến của $G$ trên $U$. Chứng minh rằng xác suất $H$ có một số màu $\le 400$ nhỏ hơn $0.01$.

??? tip "Lời giải sơ bộ"
    Gọi $J$ là đồ thị con suy biến trên $V \ U$. Thì rõ ràng $\chi(H) + \chi(J) \ge 1000$, ngược lại ta có thể có việc tô màu tốt hơn của $G$ so với việc tô màu tối ưu. Lưu ý là việc chọn $U$ và $V \ U$ là gần như bằng nhau, nên giá trị kì vọng của $\chi(H)$ là ít nhất $500$. Giờ ta thử dùng bất đằng thức Azuma ở đây. Nhưng làm sao tạo một martingale đây?

    Nhớ lại là nếu ta bắt đầu với một biến ngẫu nhiên trên một không gian xác suất $(\Omega, \mathcal{F}, P)$ với bộ lọc $\mathcal{F}_i$ với mọi thứ là tập con của $\mathcal{F}$, $E[X | \mathcal{F}_i]$ là một martingale. Tận dụng thực tế là ta đã được cung cấp lại số màu của đồ thị. Xét việc tô màu đồ thị và phân chia nó thành các tập $P_i$ được phân định bởi các màu của các đỉnh. Giờ hãy xem xét quả trình lọc mà sẽ cho thấy $U \cap P_i$ lần lượt (các tập này độc lập). Lưu ý rằng sự thay đổi số màu sẽ nhiều nhất chỉ là $1$. Nên theo bất đẳng thức Azuma, $P(\chi(H) \le 400) < P(\chi(H) - e \le -100) \le \exp(-100^2/(2 \cdot 1000))$, với $e$ là kì vọng số màu của $H$.

## Luyện tập

Gần như tất cả các bài tập CP trong phần này mà tôi biết được đề cập trong [blog này](https://www.cnblogs.com/TinyWong/p/12887591.html) và [solution của bài 1479E giải thích ý chính hơi khác một tí](https://codeforces.com/blog/entry/87598). Mình sẽ không lặp lại những điều đó (các phương trình sẽ dễ hiểu nếu bạn hiểu được cách tiếp cận toán học với các bài tập toán ở trên), nhưng mình vẫn ghi các bài mà họ chỉ ra ở đây cũng như các bài xuất hiện sau đó (theo thứ tự ngược thời gian).

| Problem | Status | Submission | Code | Date |
| :---: | :-----------: | :---: | :---: | :---: |
| [1575F - Finding Expected Value](https://codeforces.com/contest/1575/problem/F) | | | | |
| [1479E - School Clubs](https://codeforces.com/contest/1479/problem/E) | | | | |
| [1392H - ZS Shuffles Cards](https://codeforces.com/contest/1392/problem/H) | | | | |
| [1349D - Slime and Biscuits](https://codeforces.com/contest/1349/problem/D) | | | | |
| [1025G - Company Acquisitions](https://codeforces.com/contest/1025/problem/G) | | | | |
| [850F - Rainbow Balls](https://codeforces.com/contest/850/problem/F) | | | | |
| [USACO 2018 — Balance Beam](http://www.usaco.org/index.php?page=viewproblem2&cpid=864) | | | | |
