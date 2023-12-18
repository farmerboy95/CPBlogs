# Phân tích biểu thức

## Nguồn

<img src="../../../../assets/images/cpalgorithms.ico" width="16" height="16"/> [Expression parsing](https://cp-algorithms.com/string/expression_parsing.html)

## Bài toán

Cho một xâu chứa một biểu thức toán học, trong đó có chứa các số và các toán tử. Tính giá trị của biểu thức đó trong $O(n)$, với $n$ là độ dài của xâu.

Thuật toán sau đây sẽ chuyển biểu thức về dạng được gọi là **Ký pháp nghịch đảo Ba Lan (Reverse Polish notation - RPN)** và tính giá trị của nó.

## Ký pháp nghịch đảo Ba Lan

Ký pháp nghịch đảo Ba Lan là một dạng viết biểu thức toán học, trong đó các toán tử được đặt sau các toán hạng của nó. Ví dụ ta có biểu thức sau:

$$a + b * c * d + (e - f) * (g * h + i)$$

có thể được viết dưới dạng ký pháp nghịch đảo Ba Lan như sau:

$$a b c * d * + e f - g h * i + * +$$

Ký pháp nghịch đảo Ba Lan được phát triển bởi nhà triết học và chuyên gia khoa học máy tính người Úc Charles Hamblin vào giữa những năm 1950, dựa trên ký pháp Ba Lan được đề xuất vào năm 1920 bởi nhà toán học người Ba Lan Jan Łukasiewicz.

Lợi thế của ký pháp nghịch đảo Ba Lan là nó giúp các tính các biểu thức toán học ở dạng này dễ dàng hơn trong thời gian tuyến tính. Ban đầu ta dùng một stack rỗng, sau đó duyệt qua các toán hạng và toán tử của biểu thức được viết theo ký pháp nghịch đảo Ba Lan. Nếu gặp một toán hạng, ta đẩy nó vào stack. Nếu gặp một toán tử, ta lấy ra hai toán hạng trên cùng của stack, thực hiện phép tính và đẩy kết quả vào stack. Sau khi duyệt qua toàn bộ biểu thức, sẽ chỉ còn một giá trị duy nhất trên stack, đó chính là giá trị của biểu thức.

Rõ ràng thuật toán này chạy trong $O(n)$.

## Phân tích biểu thức đơn giản

Trước hết ta sẽ giải quyết bài toán đơn giản hơn, giả sử tất cả các toán tử đều là toán tử **hai ngôi** (tức là chúng có hai toán hạng), và tất cả các toán tử đều là toán tử trái sang phải (nếu có hai toán tử có cùng độ ưu tiên, thì chúng được thực hiện từ trái sang phải). Dấu ngoặc cũng có thể được sử dụng.

Ta sẽ thiết lập hai stack: một stack để lưu các số, và một stack để lưu các toán tử và dấu ngoặc. Ban đầu cả hai stack đều rỗng. Với stack thứ hai, ta sẽ duy trì điều kiện rằng tất cả các toán tử được sắp xếp theo độ ưu tiên giảm dần. Nếu stack thứ hai có chứa dấu ngoặc, thì mỗi khối toán tử (tương ứng với một cặp dấu ngoặc) được sắp xếp, và stack thứ hai không nhất thiết phải được sắp xếp.

Ta sẽ duyệt qua các ký tự của biểu thức từ trái sang phải. Nếu ký tự hiện tại là một chữ số, ta đưa giá trị của nó vào stack thứ nhất. Nếu ký tự hiện tại là một dấu ngoặc mở, ta đưa nó vào stack thứ hai. Nếu ký tự hiện tại là một dấu ngoặc đóng, ta thực hiện tất cả các toán tử trong stack thứ hai cho đến khi gặp dấu ngoặc mở. Cuối cùng nếu ký tự hiện tại là một toán tử, ta thực hiện tất cả các toán tử trong stack thứ hai có độ ưu tiên cao hơn hoặc bằng độ ưu tiên của toán tử hiện tại, và đưa toán tử mới vào stack thứ hai.

Sau khi duyệt qua toàn bộ biểu thức, một số toán tử có thể vẫn còn trong stack thứ hai, ta thực hiện chúng.

Sau đây là cài đặt cho bốn toán tử $+$ $-$ $*$ $/$:

```cpp
// kiểm tra xem ký tự c có phải là ký tự ta không quan tâm hay không
bool delim(char c) {
    return c == ' ';
}

// kiểm tra xem ký tự c có phải là một toán tử hay không
bool isOp(char c) {
    return c == '+' || c == '-' || c == '*' || c == '/';
}

// xác định độ ưu tiên của toán tử, phép nhân và chia có độ ưu tiên cao hơn
int priority(char op) {
    if (op == '+' || op == '-') {
        return 1;
    }
    if (op == '*' || op == '/') {
        return 2;
    }
    return -1;
}

// thực hiện phép tính giữa hai toán hạng trong stack với toán tử op
void processOp(stack<int>& st, char op) {
    int r = st.top(); st.pop();
    int l = st.top(); st.pop();
    switch (op) {
        case '+': st.push(l + r); break;
        case '-': st.push(l - r); break;
        case '*': st.push(l * r); break;
        case '/': st.push(l / r); break;
    }
}

// tính giá trị của biểu thức s
int evaluate(string& s) {
    // stack st lưu các số
    stack<int> st;
    // stack op lưu các toán tử và dấu ngoặc
    stack<char> op;
    // duyệt qua các ký tự của biểu thức
    for (int i = 0; i < (int) s.size(); i++) {
        if (delim(s[i])) {
            // bỏ qua các ký tự ta không quan tâm
            continue;
        }
        
        if (s[i] == '(') {
            // nếu ký tự hiện tại là một dấu ngoặc mở, đưa nó vào stack op
            op.push('(');
        } else if (s[i] == ')') {
            // nếu ký tự hiện tại là một dấu ngoặc đóng, thực hiện tất cả các toán tử trong stack op cho đến khi gặp dấu ngoặc mở
            while (op.top() != '(') {
                processOp(st, op.top());
                op.pop();
            }
            // bỏ dấu ngoặc mở ra khỏi stack op
            op.pop();
        } else if (isOp(s[i])) {
            // nếu ký tự hiện tại là một toán tử, thực hiện tất cả các toán tử trong stack op 
            // có độ ưu tiên cao hơn hoặc bằng độ ưu tiên của toán tử hiện tại, và đưa toán tử 
            // mới vào stack op
            char curOp = s[i];
            while (!op.empty() && priority(op.top()) >= priority(curOp)) {
                processOp(st, op.top());
                op.pop();
            }
            op.push(curOp);
        } else {
            // nếu ký tự hiện tại là một chữ số, lấy tất cả các chữ số liên tiếp nhau và đưa vào stack st 
            int number = 0;
            while (i < (int)s.size() && isalnum(s[i])) {
                number = number * 10 + s[i++] - '0';
            }
            --i;
            st.push(number);
        }
    }

    // sau khi duyệt qua toàn bộ biểu thức, một số toán tử có thể vẫn còn trong stack op, ta thực hiện chúng
    while (!op.empty()) {
        processOp(st, op.top());
        op.pop();
    }
    // stack st sẽ chỉ còn một giá trị duy nhất, đó chính là giá trị của biểu thức
    return st.top();
}
```

Vậy ta đã học cách tính giá trị của một biểu thức trong $O(n)$, đồng thời ta cũng đã sử dụng ký pháp nghịch đảo Ba Lan. Bằng cách thay đổi một chút cài đặt trên, ta cũng có thể thu được biểu thức ở dạng ký pháp nghịch đảo Ba Lan.

## Toán tử đơn nguyên

Giả sử biểu thức cũng có thể chứa các toán tử **đơn nguyên** (toán tử chỉ có một toán hạng). Ví dụ, đơn giản nhất là toán tử **âm** và **dương**.

Một trong những khác biệt trong trường hợp này là ta cần xác định xem toán tử hiện tại là toán tử đơn nguyên hay toán tử hai ngôi.

Để ý rằng trước một toán tử đơn nguyên, luôn có một toán tử khác hoặc một dấu ngoặc mở, hoặc không có gì cả (nếu nó ở đầu biểu thức). Ngược lại, trước một toán tử hai ngôi luôn có một toán hạng (số) hoặc một dấu ngoặc đóng. Do đó, ta có thể dễ dàng xác định xem toán tử tiếp theo có thể là toán tử đơn nguyên hay không.

Ngoài ra, ta cũng cần thực hiện các toán tử đơn nguyên và hai ngôi khác nhau. Và ta cũng cần xác định độ ưu tiên của toán tử đơn nguyên cao hơn tất cả các toán tử hai ngôi.

Thêm nữa, cần lưu ý rằng một số toán tử đơn nguyên (ví dụ như toán tử **âm** và **dương**) thực chất là có tính **ưu tiên phải**.

## Tính ưu tiên phải

Ưu tiên phải có nghĩa là, bất cứ khi nào độ ưu tiên bằng nhau, các toán tử phải được thực hiện từ phải sang trái.

Như đã nói ở trên, các toán tử đơn nguyên thường có tính ưu tiên phải. Một ví dụ khác cho toán tử ưu tiên phải là toán tử **mũ** ($a \wedge b \wedge c$ thường được hiểu là $a^{b^c}$ chứ không phải là $(a^b)^c$).

Ta cần làm gì để xử lý trường hợp có toán tử ưu tiên phải? Cũng ít thôi. Khác biệt duy nhất là, nếu độ ưu tiên bằng nhau, ta sẽ hoãn việc thực hiện toán tử ưu tiên phải.

Dòng duy nhất cần được chỉnh là:

```cpp
while (!op.empty() && priority(op.top()) >= priority(curOp))
```

thay bằng

```cpp
while (!op.empty() && (
        (left_assoc(curOp) && priority(op.top()) >= priority(curOp)) ||
        (!left_assoc(curOp) && priority(op.top()) > priority(curOp))
    ))
```

với `left_assoc` là một hàm xác định xem toán tử có tính ưu tiên trái hay không.

Sau đây là cài đặt cho các toán tử hai ngôi $+$ $-$ $*$ $/$ và các toán tử đơn nguyên $+$ $-$:


```cpp
// kiểm tra xem ký tự c có phải là ký tự ta không quan tâm hay không
bool delim(char c) {
    return c == ' ';
}

// kiểm tra xem ký tự c có phải là một toán tử hai ngôi hay không
bool isOp(char c) {
    return c == '+' || c == '-' || c == '*' || c == '/';
}

// kiểm tra xem ký tự c có phải là một toán tử đơn nguyên hay không
bool isUnary(char c) {
    return c == '+' || c=='-';
}

// xác định độ ưu tiên của toán tử, phép nhân và chia có độ ưu tiên cao hơn, nhưng toán tử đơn nguyên có độ ưu tiên cao nhất
int priority(char op) {
    if (op < 0) // toán tử đơn nguyên
        return 3;
    if (op == '+' || op == '-')
        return 1;
    if (op == '*' || op == '/')
        return 2;
    return -1;
}

void processOp(stack<int>& st, char op) {
    if (op < 0) {
        int l = st.top(); st.pop();
        switch (-op) {
            case '+': st.push(l); break;
            case '-': st.push(-l); break;
        }
    } else {
        int r = st.top(); st.pop();
        int l = st.top(); st.pop();
        switch (op) {
            case '+': st.push(l + r); break;
            case '-': st.push(l - r); break;
            case '*': st.push(l * r); break;
            case '/': st.push(l / r); break;
        }
    }
}

// tính giá trị của biểu thức s
int evaluate(string& s) {
    // stack st lưu các số
    stack<int> st;
    // stack op lưu các toán tử và dấu ngoặc
    stack<char> op;

    // mayBeUnary xác định xem tiếp theo có thể là một toán tử đơn nguyên hay không
    bool mayBeUnary = true;
    // duyệt qua các ký tự của biểu thức
    for (int i = 0; i < (int) s.size(); i++) {
        if (delim(s[i])) {
            // bỏ qua các ký tự ta không quan tâm
            continue;
        }
        
        if (s[i] == '(') {
            // nếu ký tự hiện tại là một dấu ngoặc mở, đưa nó vào stack op
            op.push('(');
            // tiếp theo có thể là một toán tử đơn nguyên
            mayBeUnary = true;
        } else if (s[i] == ')') {
            // nếu ký tự hiện tại là một dấu ngoặc đóng, thực hiện tất cả các toán tử trong stack op cho đến khi gặp dấu ngoặc mở
            while (op.top() != '(') {
                processOp(st, op.top());
                op.pop();
            }
            // bỏ dấu ngoặc mở ra khỏi stack op
            op.pop();
            // tiếp theo không thể là một toán tử đơn nguyên
            mayBeUnary = false;
        } else if (isOp(s[i])) {
            // nếu ký tự hiện tại là một toán tử
            char curOp = s[i];
            if (mayBeUnary && isUnary(curOp)) {
                // nếu đây là một toán tử đơn nguyên, đổi dấu của nó để phân biệt với toán tử hai ngôi (+ và -)
                curOp = -curOp;
            }
            while (!op.empty() && (
                    (curOp >= 0 && priority(op.top()) >= priority(curOp)) ||
                    (curOp < 0 && priority(op.top()) > priority(curOp))
                )) {
                // nếu toán tử hai ngôi thì thực hiện tất cả các toán tử trong stack op
                // có độ ưu tiên cao hơn hoặc bằng độ ưu tiên của toán tử hiện tại

                // nếu toán tử đơn nguyên thì thực hiện tất cả các toán tử trong stack op
                // có độ ưu tiên cao hơn độ ưu tiên của toán tử hiện tại
                processOp(st, op.top());
                op.pop();
            }
            // đưa toán tử mới vào stack op
            op.push(curOp);
            // tiếp theo có thể là một toán tử đơn nguyên
            mayBeUnary = true;
        } else {
            // nếu ký tự hiện tại là một chữ số, lấy tất cả các chữ số liên tiếp nhau và đưa vào stack st
            int number = 0;
            while (i < (int)s.size() && isalnum(s[i])) {
                number = number * 10 + s[i++] - '0';
            }
            --i;
            st.push(number);
            // tiếp theo không thể là một toán tử đơn nguyên
            mayBeUnary = false;
        }
    }

    // sau khi duyệt qua toàn bộ biểu thức, một số toán tử có thể vẫn còn trong stack op, ta thực hiện chúng
    while (!op.empty()) {
        processOp(st, op.top());
        op.pop();
    }

    // stack st sẽ chỉ còn một giá trị duy nhất, đó chính là giá trị của biểu thức
    return st.top();
}
```
