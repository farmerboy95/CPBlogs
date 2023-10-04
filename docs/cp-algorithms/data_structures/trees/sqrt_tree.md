# Sqrt Tree

## Nguồn

<img src="../../../../assets/images/cpalgorithms.ico" width="16" height="16"/> [Sqrt Tree](https://cp-algorithms.com/data_structures/sqrt-tree.html)

## Lời tựa

Cho một mảng $a$ có $n$ phần tử và toán tử $\circ$ thoả mãn tính chất kết hợp: $(x \circ y) \circ z = x \circ (y \circ z)$ đúng với mọi $x$, $y$, $z$.

Cho nên, các toán tử như $gcd$, $min$, $max$, $+$, $and$, $or$, $xor$, $\ldots$ đều thoả tính chất kết hợp.

Ta cũng được cho thêm các truy vấn dạng $q(l, r)$. Với mỗi truy vấn, ta cần tính $a_l \circ a_{l+1} \circ \dots \circ a_r$

Sqrt Tree có thể xử lý những truy vấn như vậy trong $O(1)$ thời gian với $O(n \cdot \log \log n)$ thời gian tiền xử lý và $O(n \cdot \log \log n)$ bộ nhớ.

## Mô tả

### Xây dựng chia căn

Ta [chia căn]() cho mảng. Chia mảng ra thành $\sqrt{n}$ block, mỗi block có kích thước $\sqrt{n}$. Với mỗi block, ta tính:

1. Trả lời các truy vấn nằm trong block đó, với $l$ là phần tử đầu tiên của block (lưu vào $\text{prefixOp}$).
2. Trả lời các truy vấn nằm trong block đó, với $r$ là phần tử cuối cùng của block (lưu vào $\text{suffixOp}$).

Ta tính thêm một mảng nữa

1. $between_{i,j}$ (với $i \leq j$) - trả lời truy vấn bắt đầu ở phần tử đầu tiên của block thứ $i$ và kết thúc ở phần tử cuối cùng của block $j$. Lưu ý rằng ta có $\sqrt{n}$ block, nên kích thước mảng này sẽ là $O(\sqrt{n}^2) = O(n)$.

Xét ví dụ sau.

Cho $\circ$ là phép $+$ (ta tính tổng một đoạn) và có mảng $a$ như sau:

`{1, 2, 3, 4, 5, 6, 7, 8, 9}`

Nó sẽ được chia làm ba block: `{1, 2, 3}`, `{4, 5, 6}`, và `{7, 8, 9}`.

Trong block thứ nhất, $\text{prefixOp}$ là `{1, 3, 6}` và $\text{suffixOp}$ là `{6, 5, 3}`.

Trong block thứ hai, $\text{prefixOp}$ là `{4, 9, 15}` và $\text{suffixOp}$ là `{15, 11, 6}`.

Trong block thứ ba, $\text{prefixOp}$ là `{7, 15, 24}` và $\text{suffixOp}$ là `{24, 17, 9}`.

Mảng $\text{between}$ là:

```
{
    {6, 21, 45},
    {0, 15, 39},
    {0, 0,  24}
}
```

(ở đây ta giả sử nếu $i > j$ thì $between_{i,j}$ là $0$)

Ta đã có thể trả lời một số truy vấn với những mảng này. Nếu truy vấn không nằm gọn trong một block, ta có thể chia nó thành ba phần: hậu tố của một block, sau đó là một số đoạn của các block kề nhau và cuối cùng là tiền tố của một block. Ta có thể trả lời truy vấn bằng cách chia nó ra thành ba phần như trên rồi lấy một giá trị từ $\text{suffixOp}$, sau đó đến một số giá trị từ $\text{between}$, cuối cùng là một giá trị từ $\text{prefixOp}$.

Nhưng nếu truy vấn nằm gọn trong một block, ta không thể làm như thế được. Vì vậy ta cần phải làm một cái gì đó ở đây.

### Tạo cây

Ta không thể trả lời các truy vấn nằm gọn trong một block. Nhưng sẽ ra sao **nếu ta tạo một cấu trúc dữ liệu y như trên cho mỗi block**? Ta có thể làm được điều đó, và ta làm một cách đệ quy, cho đến khi kích thước block là $1$ hoặc $2$. Trả lời các truy vấn cho các block nhỏ như vậy chỉ tốn $O(1)$.

Vậy ta có một cái cây. Mỗi node trên cây quản lý một đoạn của mảng. Node quản lý đoạn kích thước bằng $k$ sẽ có $\sqrt{k}$ node con -- cho mỗi block. Thêm nữa, mỗi node chứa ba mảng $\text{prefixOp}$, $\text{suffixOp}$ và $\text{between}$ như trên cho đoạn mà nó quản lý. Gốc của cây quản lý toàn bộ mảng. Node của các đoạn có độ dài $1$ hoặc $2$ là các node lá.

Rõ ràng là cây sẽ có chiều cao là $O(\log \log n)$, vì nếu một node nào đó quản lý đoạn có độ dài là $k$, thì các node con của nó là $\sqrt{k}$. Ta có $\log(\sqrt{k}) = \frac{\log{k}}{2}$, nên $\log k$ giảm hai lần qua mỗi lớp của cây, nên chiều cao cây là $O(\log \log n)$. Thời gian và bộ nhớ cần dùng để xây dựng cây là $O(n \cdot \log \log n)$, bởi vì mỗi phần tử trong mảng xuất hiện đúng một lần trên mỗi lớp của cây.

Giờ ta có thể trả lời các truy vấn trong $O(\log \log n)$. Ta có thể đi xuống các node cho đến khi ta gặp đoạn độ dài $1$ hoặc $2$ (trả lời các truy vấn cho đoạn này có thể thực hiện trong $O(1)$), hoặc đến khi gặp đoạn đầu tiên làm cho truy vấn không nằm trong một block. Xem phần trước để trả lời các truy vấn trong trường hợp này.

OK, $O(\log \log n)$ cũng nhanh đấy. Nhưng ta có thể làm nhanh hơn được không?

### Tối ưu độ phức tạp truy vấn

Một trong những việc tối ưu rõ ràng nhất ở đây chính là việc tìm kiếm nhị phân node ta cần. Với tìm kiếm nhị phân, ta có thể truy vấn trong $O(\log \log \log n)$. Nhưng có thể nhanh hơn nữa không?

Câu trả lời là có. Giả sử ta có những điều sau:

1. Các kích thước block là luỹ thừa của $2$.
2. Tất cả các block có kích thước bằng nhau ở mỗi lớp.

Để làm được điều này, ta cần thêm các phần tử $0$ vào mảng sao cho kích thước của nó là một luỹ thừa của $2$.

Khi làm như vậy, kích thước block có thể tăng gấp đôi để trở thành một luỹ thừa của $2$, nhưng nó vẫn sẽ là $O(\sqrt{k})$ và ta giữ độ phức tạp tuyến tính khi tạo các mảng thành phần trong đoạn.

Giờ ta có thể dễ dàng kiểm tra xem truy vấn có nằm hẳn trong block có kích thước $2^k$ hay không. Viết $l$ và $r$ theo hệ nhị phân (ta đánh số vị trí từ $0$). Ví dụ, cho $k=4, l=39, r=46$. Biểu diễn nhị phân của $l$ và $r$ là:

$$l = 39_{10} = 100111_2$$

$$r = 46_{10} = 101110_2$$

Nhớ lại rằng một lớp gồm các đoạn có kích thước bằng nhau, và các block trên một lớp cũng có kích thước bằng nhau (trong trường hợp này kích thước là $2^k = 2^4 = 16$). Các block bao phủ toàn bộ mảng, nên block đầu tiên quản lý các phần tử $(0 - 15)$ ($(000000_2 - 001111_2)$ theo hệ nhị phân), block thứ hai quản lý các phần tử $(16 - 31)$ ($(010000_2 - 011111_2)$ theo hệ nhị phân) và cứ như thế. Ta thấy rằng các chỉ số vị trí trong một block chỉ khác nhau ở $k$ bit nhỏ nhất (trong trường hợp này là $4$). Nếu $l$ và $r$ có các bit bằng nhau, trừ $4$ bit nhỏ nhất, đoạn này sẽ nằm trong một block.

Vậy, ta chỉ cần kiểm tra $k$ bit nhỏ nhất của hai số có khác nhau hay không (hay nói cách khác là $l\ \text{xor}\ r$ có vượt quá $2^k-1$ hay không).

Với observation này, ta có thể tìm ra được lớp thích hợp để trả lời truy vấn rất nhanh như sau:

1. Với mỗi $i$ không vượt quá kích thước mảng, ta tìm bit $1$ lớn nhất. Để làm được thì ta dùng DP và một mảng tiền xử lý.
2. Với mỗi truy vấn $q(l,r)$, ta tìm bit $1$ lớn nhất của $l\ \text{xor}\ r$ và dùng thông tin này để chọn lớp trên sqrt tree để xử lý truy vấn. Ta cũng có thể dùng mảng tiền xử lý ở đây.

Có thể đọc code ở dưới cùng của bài viết để hiểu thêm.

Do vậy, bằng cách này, ta có thể trả lời truy vấn trong $O(1)$.

## Cập nhật giá trị

Ta cũng có thể cập nhật các phần tử trên Sqrt Tree. Cập nhật một phần tử hoặc một đoạn đều được.

### Cập nhật giá trị một phần tử

Xét một truy vấn $\text{update}(x, val)$ thực hiện phép gán $a_x = val$. Ta cần thực hiện truy vấn này đủ nhanh.

#### Cách tiếp cận đơn giản

Đầu tiên, ta xét xem những gì sẽ xảy ra trên cây khi một phần tử nào đó thay đổi giá trị. Xét một node trên cây quản lý đoạn độ dài $l$ và những mảng thành phần của nó: $\text{prefixOp}$, $\text{suffixOp}$ và $\text{between}$. Dễ thấy rằng chỉ có $O(\sqrt{l})$ phần tử trong $\text{prefixOp}$ và $\text{suffixOp}$ là thay đổi (trong block chứa phần tử bị thay đổi). $O(l)$ phần tử thay đổi trong mảng $\text{between}$. Suy ra rằng $O(l)$ phần tử trên cây thay đổi.

Nhớ rằng bất cứ phần tử $x$ nào sẽ hiện diện trên một node trên cây trên mỗi lớp. Node gốc (lớp $0$) có độ dài $O(n)$, các node trên lớp $1$ có độ dài $O(\sqrt{n})$, các node trên lớp $2$ có độ dài $O(\sqrt{\sqrt{n}})$, v.v... Vậy độ phức tạp thời gian trên mỗi lần cập nhật là $O(n + \sqrt{n} + \sqrt{\sqrt{n}} + \dots) = O(n)$.

Nhưng như vậy là quá chậm. Có thể làm nhanh hơn không?

#### Một sqrt tree trong sqrt tree

Lưu ý rằng nút thắt ở đây là việc cập nhật lại mảng $\text{between}$ của node gốc quá mất thời gian. Để tối ưu cây, ta bỏ cái mảng này luôn. Thay vì dùng mảng $\text{between}$, ta lưu một sqrt tree nữa cho node gốc. Gọi nó là $\text{index}$. Nó đóng vai trò y như $\text{between}$ - trả lời các truy vấn trên dãy các block. Chú ý rằng các node còn lại trên cây không có $\text{index}$, chúng vẫn dùng mảng $\text{between}$.

Một sqrt tree được xem là *indexed*, nếu node gốc có $\text{index}$. Một sqrt tree với mảng $\text{between}$ trong node gốc được gọi là *unindexed*. Lưu ý rằng cây $\text{index}$ **thì *unindexed***.

Vậy ta có thuật toán sau để cập nhật trên cây đã được *indexed*:

- Cập nhật $\text{prefixOp}$ và $\text{suffixOp}$ trong $O(\sqrt{n})$.
- Cập nhật $\text{index}$. Nó có độ dài $O(\sqrt{n})$ và ta chỉ cần cập nhật một giá trị trong đó thôi (giá trị đi theo block đã thay đổi). Vậy độ phức tạp thời gian của bước này là $O(\sqrt{n})$. Ta có thể dùng thuật toán được mô tả ở đầu phần này (thuật toán "chậm") để làm.
- Đi đến node con biểu diễn block được thay đổi và cập nhật nó trong $O(\sqrt{n})$ với thuật toán "chậm".

Lưu ý rằng độ phức tạp của việc truy vấn vẫn là $O(1)$: ta cần dùng $\text{index}$ trong truy vấn đúng một lần, và sẽ tốn $O(1)$ thời gian.

Vậy tổng độ phức tạp thời gian cho việc cập nhật một phần tử là $O(\sqrt{n})$.

### Cập nhật giá trị một đoạn

Sqrt tree cũng có thể gán tất cả các giá trị của một đoạn bằng một giá trị nào đó. Gọi hàm $\text{massUpdate}(x, l, r)$ nghĩa là $a_i = x$ với mọi $l \le i \le r$.

Có hai cách tiếp cận để giải quyết vấn đề này: một trong số đó chạy $\text{massUpdate}$ trong $O(\sqrt{n}\cdot \log \log n)$, với truy vấn trong $O(1)$. Cách thứ hai thì chạy $\text{massUpdate}$ trong $O(\sqrt{n})$, nhưng lại truy vấn trong $O(\log \log n)$.

Ta sẽ cập nhật lazy y như cách làm với segment tree: đánh dấu một số node là *lazy*, nghĩa là ta sẽ đẩy cập nhật xuống chỉ khi cần thiết. Nhưng điểm khác so với segment tree là: đẩy cập nhật rất tốn tài nguyên, nên sẽ không làm được trong các truy vấn. Trên lớp $0$, đẩy cập nhật tốn $O(\sqrt{n})$ thời gian. Vì thế nên ta không đẩy trong truy vấn, ta chỉ xem nếu node hiện tại hoặc cha của node đó *lazy*, và chỉ xét nó khi chạy truy vấn.

#### Cách 1

Ta giả sử rằng chỉ có các node trên lớp $1$ (với độ dài $O(\sqrt{n})$) là có thể *lazy*. Khi đẩy node xuống, nó cập nhật tất cả cây con kể cả nó trong $O(\sqrt{n}\cdot \log \log n)$. Quá trình $\text{massUpdate}$ sẽ như sau:

- Xét các node trên lớp $1$ và các block tương ứng với chúng.
- Một số block được bao phủ hoàn toàn bởi $\text{massUpdate}$. Ta đánh dấu chúng là *lazy* trong $O(\sqrt{n})$.
- Một số block được bao phủ một phần. Lưu ý rằng không có nhiều hơn hai block như vậy. Xây dựng lại chúng trong $O(\sqrt{n}\cdot \log \log n)$. Nếu chúng *lazy*, tranh thủ xét chúng.
- Cập nhật $\text{prefixOp}$ và $\text{suffixOp}$ cho các block bị bao phủ một phần trong $O(\sqrt{n})$ (vì chỉ có hai block như vậy).
- Xây dựng lại $\text{index}$ trong $O(\sqrt{n}\cdot \log \log n)$.

Ta có thể thực hiện $\text{massUpdate}$ nhanh chóng. Nhưng cập nhật *lazy* thì ảnh hưởng gì đến truy vấn? Nó sẽ tạo ra các thay đổi sau:

- Nếu truy vấn nằm hoàn toàn trong một *lazy* block, tính kết quả và xét cả *lazy*, $O(1)$.
- Nếu truy vấn gồm nhiều block, một số trong đó *lazy*, ta cần quan tâm *lazy* nằm bên trái hoặc phải ngoài cùng. Các block còn lại được tính bằng $\text{index}$, ta đã biết được kết quả trên các block *lazy* rồi (vì $\text{index}$ được xây dựng lại mỗi khi có thay đổi ở mảng), $O(1)$.

Độ phức tạp của truy vấn vẫn là $O(1)$.

#### Cách 2

Ở cách tiếp cận này, mỗi node đều có thể *lazy* (trừ node gốc). Kể cả các node trong $\text{index}$ cũng có thể *lazy*. Vì thế nên khi ta thực hiện một truy vấn, ta cần phải xem thử các biến *lazy* trên các node tổ tiên, nghĩa là độ phức tạp truy vấn sẽ là $O(\log \log n)$.

Nhưng $\text{massUpdate}$ lại nhanh hơn. Nó sẽ trông như sau:

- Một số block được bao phủ hoàn toàn bởi  $\text{massUpdate}$ nên *lazy* được thêm vào chúng, độ phức tạp  $O(\sqrt{n})$.
- Cập nhật $\text{prefixOp}$  và $\text{suffixOp}$ cho các block được phủ một phần trong $O(\sqrt{n})$ (vì chỉ có hai block như vậy thôi).
- Đừng quên cập nhật $\text{index}$. Nó tốn $O(\sqrt{n})$ (cũng dùng thuật  $\text{massUpdate}$  như vậy).
- Cập nhật mảng $\text{between}$  cho các cây con *unindexed*.
- Đi vào các node được bao phủ một phần và tiếp tục gọi $\text{massUpdate}$ như thế.

Lưu ý rằng khi gọi đệ quy, ta $\text{massUpdate}$ tiền tố hoặc hậu tố. Nhưng với việc cập nhật tiền tố và hậu tố, ta chỉ có thể có một node con được bao phủ một phần thôi. Nên ta thăm một node trên lớp $1$, hai node trên lớp $2$ và hai node trên bất cứ lớp tiếp theo nào. Nên độ phức tạp thời gian là $O(\sqrt{n} + \sqrt{\sqrt{n}} + \dots) = O(\sqrt{n})$. Cách tiếp cận này tương tự với mass update trên segment tree.

## Cài đặt

Code sau đây của Sqrt Tree có thể thực hiện các thao tác sau: xây dựng xây trong $O(n \cdot \log \log n)$, trả lời truy vấn trong $O(1)$, cập nhật một phần tử trong $O(\sqrt{n})$.

```cpp
struct SqrtTreeItem {
    // tạo item theo ý thích của bạn
};

// nhớ thêm thao tác vào
SqrtTreeItem op(const SqrtTreeItem &a, const SqrtTreeItem &b);

inline int log2Up(int n) {
    int res = 0;
    while ((1 << res) < n) {
        res++;
    }
    return res;
}

struct SqrtTree {
    int n, lg, indexSz;
    vector<SqrtTreeItem> v;
    vi clz, layers, onLayer;
    vector<vector<SqrtTreeItem>> pref, suf, between;

    inline void buildBlock(int layer, int l, int r) {
        // block [l, r)
        // tính các mảng prefix và suffix
        pref[layer][l] = v[l];
        FOR(i,l+1,r-1) {
            pref[layer][i] = op(pref[layer][i-1], v[i]);
        }
        suf[layer][r-1] = v[r-1];
        FORE(i,r-2,l) {
            suf[layer][i] = op(v[i], suf[layer][i+1]);
        }
    }

    inline void buildBetween(int layer, int lBound, int rBound, int betweenOffs) {
        // log của block size
        int bSzLog = (layers[layer]+1) >> 1;
        // log of số các block
        int bCntLog = layers[layer] >> 1;
        // block size
        int bSz = 1 << bSzLog;
        // số các block của layer này, đơn giản nó là ceilDiv(r - l, bSz)
        int bCnt = (rBound - lBound + bSz - 1) >> bSzLog;

        // build mảng "between"
        for (int i = 0; i < bCnt; i++) {
            SqrtTreeItem ans;
            for (int j = i; j < bCnt; j++) {
                SqrtTreeItem add = suf[layer][lBound + (j << bSzLog)];
                ans = (i == j) ? add : op(ans, add);
                // between[i][j]
                between[layer-1][betweenOffs + lBound + (i << bCntLog) + j] = ans;
            }
        }
    }

    inline void buildBetweenZero() {
        int bSzLog = (lg+1) >> 1;
        // thêm giá trị của các block của layer 0 vào "index" của sqrt tree và build cây đó
        for (int i = 0; i < indexSz; i++) {
            v[n+i] = suf[0][i << bSzLog];
        }
        build(1, n, n + indexSz, (1 << lg) - n);
    }

    inline void updateBetweenZero(int bid) {
        int bSzLog = (lg+1) >> 1;
        // update block value của "index" sqrt tree
        v[n+bid] = suf[0][bid << bSzLog];
        // update "index" sqrt tree
        update(1, n, n + indexSz, (1 << lg) - n, n+bid);
    }

    void build(int layer, int lBound, int rBound, int betweenOffset) {
        if (layer >= SZ(layers)) {
            // return khi layer index lớn hơn hoặc bằng số layer
            return;
        }

        // block size
        int bSz = 1 << ((layers[layer]+1) >> 1);
        for (int l = lBound; l < rBound; l += bSz) {
            int r = min(l + bSz, rBound);
            buildBlock(layer, l, r);
            build(layer+1, l, r, betweenOffset);
        }

        // build "index" sqrt tree khi ở layer 0, ngược lại build "between"
        if (layer == 0) {
            buildBetweenZero();
        } else {
            buildBetween(layer, lBound, rBound, betweenOffset);
        }
    }

    void update(int layer, int lBound, int rBound, int betweenOffset, int x) {
        if (layer >= (int)layers.size()) {
            // return khi layer index lớn hơn hoặc bằng số layer
            return;
        }

        // log của block size
        int bSzLog = (layers[layer]+1) >> 1;
        // block size
        int bSz = 1 << bSzLog;
        // block index chứa x
        int blockIdx = (x - lBound) >> bSzLog;
        // [l, r) của block chứa x
        int l = lBound + (blockIdx << bSzLog);
        int r = min(l + bSz, rBound);
        // update mảng pref và suf
        buildBlock(layer, l, r);

        // build "index" sqrt tree khi ở layer 0, ngược lại build "between"
        if (layer == 0) {
            updateBetweenZero(blockIdx);
        } else {
            buildBetween(layer, lBound, rBound, betweenOffset);
        }
        // update cho đến nút lá
        update(layer+1, l, r, betweenOffset, x);
    }

    inline SqrtTreeItem query(int l, int r, int betweenOffset, int base) {
        // đoạn [l, r]
        // độ dài 1
        if (l == r) {
            return v[l];
        }
        // độ dài 2
        if (l + 1 == r) {
            return op(v[l], v[r]);
        }

        // tìm chỉ số lớp lớn nhất bao bọc đoạn [l, r]
        int layer = onLayer[clz[(l - base) ^ (r - base)]];
        // block size của các blocks trên layer này
        int bSzLog = (layers[layer]+1) >> 1;
        // number of blocks trên layer này
        int bCntLog = layers[layer] >> 1;
        // lBound = số phần tử nằm bên trái của block chứa l
        int lBound = (((l - base) >> layers[layer]) << layers[layer]) + base;
        // lBlock và rBlock là các block trái và phải ngoài cùng không chứa l và r
        int lBlock = ((l - lBound) >> bSzLog) + 1;
        int rBlock = ((r - lBound) >> bSzLog) - 1;

        // lấy đáp án trên block trái ngoài cùng
        SqrtTreeItem ans = suf[layer][l];
        if (lBlock <= rBlock) {
            SqrtTreeItem add = (layer == 0) ? (
                // nếu nó nằm trên layer 0, ta truy vấn với "index", vì nó chứa thông tin của tất cả các block của layer 0
                query(n + lBlock, n + rBlock, (1 << lg) - n, n)
            ) : (
                // nếu layer không là node gốc, ta dễ dàng dùng "between" để lấy kết quá
                between[layer-1][betweenOffset + lBound + (lBlock << bCntLog) + rBlock]
            );
            // thêm đáp án của các block giữa vào đáp án cuối cùng
            ans = op(ans, add);
        }
        // lấy đáp án trên block phải ngoài cùng
        ans = op(ans, pref[layer][r]);
        return ans;
    }

    inline SqrtTreeItem query(int l, int r) {
        return query(l, r, 0, 0);
    }

    inline void update(int x, const SqrtTreeItem &item) {
        v[x] = item;
        update(0, 0, n, 0, x);
    }

    SqrtTree(const vector<SqrtTreeItem> &a) : n(SZ(a)), lg(log2Up(n)), v(a), clz(1 << lg), onLayer(lg+1) {
        // n = kích thước mảng ban đầu
        // lg = ceil(log2(n))

        // clz[i] = vị trí bit 1 nhỏ nhất
        clz[0] = 0;
        FOR(i,1,SZ(clz)-1) clz[i] = clz[i >> 1] + 1;

        // layers[i] là độ dài block ở layer i
        // onLayer[i] = x nghĩa là nếu dộ dài block là 2^i thì nó nên nằm trên layer x
        int tlg = lg;
        while (tlg > 1) {
            onLayer[tlg] = SZ(layers);
            layers.push_back(tlg);
            // sqrt(2^x) = 2^(x / 2)
            tlg = (tlg + 1) >> 1;
        }
        FORE(i,lg-1,0) ckmax(onLayer[i], onLayer[i+1]);

        int betweenLayers = max(0, SZ(layers) - 1);
        int bSzLog = (lg + 1) >> 1;
        int bSz = (1 << bSzLog);
        // indexSz là số cảc block độ dài bSz, chia n phần tử ra thành chừng đó block
        // nó đơn giản là ceilDiv(n, bSz)
        indexSz = (n + bSz - 1) >> bSzLog;

        v.resize(n + indexSz);
        pref.assign(layers.size(), vector<SqrtTreeItem>(n + indexSz));
        suf.assign(layers.size(), vector<SqrtTreeItem>(n + indexSz));
        between.assign(betweenLayers, vector<SqrtTreeItem>((1 << lg) + bSz));

        build(0, 0, n, 0);
    }
};
```

## Luyện tập

| Problem | Status | Submission | Code | Date |
| :---: | :-----------: | :---: | :---: | :---: |
| [Codechef - SEGPROD](https://www.codechef.com/problems/SEGPROD) | :white_check_mark: | [Submission](https://www.codechef.com/viewsolution/89329413) | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/Codechef/CODECHEF%20SEGPROD-SqrtTree.cpp) | 14/02/2023 |
