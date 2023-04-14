# Làm thế nào để giỏi hơn trong lập trình thi đấu?

## Nguồn

[How to get better? - lukipuki.github.io](https://lukipuki.github.io/contest-wiki/get-better.html)

## Lời tựa

Trước tiên mình muốn trình bày rằng mình không xem bản thân là một người thành công trong cộng đồng Lập trình thi đấu (Competitive Programming - CP) cũng như không phải là một người có khả năng chiến thuật tốt. Bài viết này là một bài mình dịch từ một bài viết trong blog của một cao thủ trong cộng đồng. Đây là một bài khá hay và mình nghĩ sẽ có ích cho các đội thi.

Sơ lược về tác giả: **Lukáš Poláček** - hiện đang là nghiên cứu sinh tại KTH Royal Institute of Technology, Thụy Điển (profile này là năm 2016). Anh ấy từng đạt huy chương đồng tại ACM ICPC 2010 và từng có rating cao nhất là 2676 trên TopCoder.

Sơ lược về kì thi: **ACM-ICPC** (giờ rút gọn thành **ICPC**) là kì thi lập trình thi đấu lớn và uy tín nhất thế giới. Kì thi kéo dài 5 giờ đồng hồ, mỗi đội 3 người sẽ phải suy nghĩ và giải quyết 10-12 bài toán bằng máy tính.

Sau đây là nội dung bài dịch của mình. Ngôi thứ nhất trong bài là chỉ tác giả, không phải chỉ mình.

## Mở đầu

Khi đi nhà sách, bạn thường gặp những tựa sách như "Dạy Java trong 7 ngày". Trong những cuốn sách như vậy, tác giả muốn thuyết phục bạn rằng lập trình dễ vãi trong khi thực ra nó không như vậy. Peter Novig đã viết một bài luận rất hay về chủ đề này là [Teach Yourself Programming in Ten Years](http://norvig.com/21-days.html) (Tự học lập trình trong 10 năm) mà mình đánh giá rất cao. Ngoài ra có một [biếm họa](https://abstrusegoose.com/249) vui về chủ đề này của Abstruce Goose. Mình đồng ý với Peter rằng cần nhiều thời gian và nỗ lực để học lập trình. Tuy nhiên bạn vẫn nên luyện tập một cách hiệu quả nhất có thể.

Có rất ít thông tin có sẵn về việc luyện tập cho các cuộc thi lập trình, nên mình quyết định tạo ra một chương trình luyện tập (training program), có lẽ được lần đầu được viết ra. Nó dựa trên kinh nghiệm lập trình thi đấu của bản thân mình. Nếu có bình luận gì xin hãy để lại ở dưới.

## Chương trình luyện tập

### Triết lý đào tạo

Trước năm 16 tuổi, mình tham gia thi Orienteering (đi từ điểm A đến điểm B trong rừng, dùng bản đồ và la bàn). Mình luyện tập rất nhiều, chạy 1700 km mỗi năm trên núi. Sau đó mình gặp một số vấn đề sức khỏe và nghỉ thi đấu. Mình có nhiều thời gian rảnh nên đã luyện tập cho các cuộc thi toán và tin học. Mình dùng một số phương pháp luyện tập trong thể thao để áp dụng cho việc luyện tập của mình.

Mình nghĩ thể thao và lập trình thi đấu có nhiều điểm chung. Tương tự như thể thao, bạn sẽ không cải thiện nhiều nếu chỉ luyện 1 kiểu. Luyện tập phải **đa dạng** và cần tập trung vào những **điểm yếu** của bạn.

Lấy ví dụ như trong bóng đá, giả sử bạn là một tiền đạo. Bạn rất giỏi ghi bàn nhưng yếu trong việc sút penalty. Bạn có thể luyện tập như trước đây và đá 2-3 quả pen một tuần khi có cơ hội trong một trận đấu tập hoặc trong một trận chính thức. Nhưng không phải sẽ tốt hơn nếu bạn ở lại tập đá pen thêm 15 phút mỗi buổi nữa sao?

Lập trình thi đấu cũng y vậy thôi. Nếu bạn hiếm khi giải bài tập hình học trong một contest, và bạn luyện trên TopCoder nhiều, bạn sẽ không thu được gì cả, vì TopCoder cũng hiếm bài hình y như vậy. Bạn cần tìm cách khác để luyện.

Luyện tập cần đa dạng. Mình để ý rằng nhiều trường đại học chỉ luyện theo đội cho ACM-ICPC. Tại KTH (trường của tác giả), bọn mình luyện cá nhân vào mùa xuân và team vào mùa thu. Mình nghĩ cả 2 kiểu luyện này đều quan trọng. Ví dụ, bạn có thể không bao giờ giải một bài Quy hoạch động (Dynamic Programming - DP) trong suốt quá trình train team, vì đồng đội luôn giải được kiểu bài đó trước khi bạn có cơ hội đọc xem đề bài viết gì. Khi train cá nhân, bạn sẽ bị buộc phải giải những bài đó, và có thể học được nhiều thứ hơn.

Chương trình luyện tập của bọn mình gồm 7 mảng. Chương trình luyện tập trong thể thao thường yêu cầu bạn nên làm thứ này 2 lần mỗi tuần trong vòng 1 tiếng, làm thứ khác 1 lần 1 tuần trong 30 phút, hoặc thứ gì đó đại loại thế. Khó mà làm y vậy trong lập trình thi đấu, vì mỗi người có một xuất phát điểm khác nhau, thậm chí rất khác nhau. Thay vào đó, bạn nên tự đánh giá bản thân, xác định điểm mạnh, yếu và chọn phương pháp cho riêng mình. Bạn có thể nhờ một người kinh nghiệm hơn hoặc huấn luyện viên đội bạn giúp bạn tìm ra cách luyện hiệu quả nhất.

Nên hoàn thành cả 7 mảng, nhưng thời gian cần cho mỗi mảng thì khác nhau đối với mỗi bạn.

### Học thuật toán và cấu trúc dữ liệu

Khi cố gắng để giỏi hơn trong lập trình thi đấu, đầu tiên mọi người học thuật toán và cấu trúc dữ liệu. Trong cả 7 mảng, mảng này được phát triển mạnh nhất. Có hàng tá sách, hướng dẫn và khóa học giúp bạn nâng cao mảng này.

Mình giới thiệu các bạn cuốn [Introduction to Algorithms](http://amzn.com/0262033844) của Cormen, Leiserson, Rivest và Stein. Ngoài ra còn có những [tutorial tốt trên TopCoder](http://www.topcoder.com/tc?d1=tutorials&d2=alg_index&module=Static). Với các khóa học thuật toán, bạn nên tìm trong trường của chính mình hoặc tìm trên mạng xem có khóa online nào không. Nếu bạn ở KTH (trường của tác giả), đăng ký khóa [Algoritmer, datastrukturer och komplexitet](http://www.csc.kth.se/utbildning/kth/kurser/DD1352/) và [Problemlösning och programmering under press](http://www.csc.kth.se/utbildning/kth/kurser/DD2458/) càng sớm càng tốt trong năm 1 và năm 2. Từ 2013, khóa thứ 2 ở trên được dạy bởi [Peter Austrin](https://www.topcoder.com/members/Per) (red coder trên TopCoder) và một số bạn thi lập trình thi đấu của KTH thường tham gia trợ giảng.

Tuy nhiên, đây chỉ là phần nhỏ của việc trở thành lập trình viên giỏi và nó hơi bị đánh giá cao quá mức. Bạn hoàn toàn có thể tiến xa mà không phải biết quá nhiều thuật toán và các mảng khác của chương trình luyện tập có thể giúp bạn nhiều hơn.

Để mình giải thích tại sao bạn không nên học quá nhiều bằng phép loại suy nha. Giả sử bạn quyết định đi xe đạp leo núi mà chưa bao giờ đạp xe trước đó. Bạn lên mạng, coi clip trên YouTube và mua một quyển sách dày 150 trang về xe đạp leo núi. Sau 2 tháng cày cuốc, bạn quyết định thử đi xem sao. Bạn cố gắng nhớ mọi thứ bạn đọc, xem và thực sự nó quá nhiều, áp đảo tâm trí bạn. Bạn bắt đầu nóng giận với bản thân, vì bạn ngã nhiều quá trong khi bạn học nhiều chả kém. Bạn bỏ đạp xe luôn.

Nghe buồn cười không? Giờ thay "đạp xe" bằng "lập trình" đi. Tất nhiên 2 thứ đó không phải là 1, nhưng việc nhồi nhét tất cả kiến thức có sẵn thường gây hại hơn là có lợi cho bạn. Thay vào đó, bạn nên bắt đầu giải bài và học thuật toán song song với nhau. Bạn sẽ thấy khi nào và làm thế nào để thuật toán được sử dụng trong các bài toán. Con người học bằng cách thực hành và bạn cần phải tạo  ra sai lầm để học tốt hơn. Nếu không thất bại, bạn sẽ không học được gì. Bạn có thể đọc về thất bại ở phần dưới.

Những luận điểm này được chứng minh bằng [nghiên cứu](http://ideas.time.com/2012/04/25/why-floundering-is-good/) rồi. Hóa ra sẽ tốt hơn nếu bạn tự giải bài trước khi đọc hướng dẫn. Ví dụ, trong lớp học thuật toán, bạn có thể được yêu cầu để viết thuật tìm đường đi ngắn nhất trong đồ thị không trọng số mà không có thông tin gì về cấu trúc dữ liệu và độ phức tạp thời gian. Bạn sẽ có thể mò ra được gì đó giống BFS (Breadth First Search - tìm kiếm theo chiều rộng) nhưng vì bạn chưa bao giờ nghe đến Queue (hàng đợi) hay độ phức tạp thời gian, thuật của bạn sẽ chậm hơn một tí. Trong tiết tiếp theo giáo viên sẽ trình bày solution liên quan đến hàng đợi và sẽ nói cho bạn biết làm thế nào để đánh giá độ phức tạp thời gian của code. Phương pháp này hiệu quả hơn việc trình bày thuật trước rồi giải bài sau.

### Cải thiện khả năng giải quyết vấn đề

Đây là mảng khó nhất trong chương trình luyện tập. Mục tiêu tối thượng là **tăng cường sự thông minh**. Bạn có thể đã nghe nói rằng trí thông minh là thứ được kế thừa và không thể thay đổi được, nhưng thật ra bạn có thể [tăng nhẹ nó](http://www.ams.org/notices/201103/rtx110300432p.pdf) (hoặc giảm nhẹ bằng sự lười nhác). Đáng tiếc là không có nhiều thông tin về chủ đề này.

Khi bạn nhìn vào [bảng rating của mình trên TopCoder](http://community.topcoder.com/tc?module=MemberProfile&cr=14769155), bạn có thể thấy rằng trong cả 2 năm 2006 và 2007, rating của mình tăng nhưng tăng nhiều hơn trong năm 2007. Phần lớn năm 2006 rating mình là 1900 - 2100 trong khi 2007 mình tăng lên 2300. Nửa đầu 2006, sau khi không tăng được rating, mình nghĩ mình đã đạt đỉnh và mình sẽ kẹt ở khoảng 2000 - 2100 mãi mãi.

Có thể bạn nghĩ rằng mình luyện nhiều hơn trong năm 2007, nhưng không phải. Năm 2007 mình làm 2 ngày 1 tuần cho 1 công ty, phải viết luận án tốt nghiệp, dạy và giúp đội Olympic Slovakia, chơi frisbee không chuyên và trở nên năng động hơn trong xã hội. Mình có ít thời gian luyện tập lập trình.

Thay vì tăng số lượng, mình tăng chất lượng luyện tập. Mình bắt đầu **làm các bài khó hơn**. Khi giải nhiều bài dễ, bạn học cách đánh máy nhanh hơn và không mắc sai lầm, nhưng không thách thức bản thân nhiều. Mặc khác, bạn không nên thử thách bản thân quá nhiều, vì khi đó bạn sẽ tuyệt vọng nếu bài quá khó. Tâm lý học gọi hiện tượng này là [Zone of proximal development](https://en.wikipedia.org/wiki/Zone_of_proximal_development).

Mình thích giải bài theo hướng "ẩn dụ nội thất" (furniture metaphor). Tưởng tượng bạn có 1 cái nhà và bạn mua 1 cái bàn to để mang lên tầng 2. Nếu cửa và cầu thang quá nhỏ, bạn phải tháo cái bàn hoặc cắt nó ra. Sau khi mang các mảnh nhỏ lên tầng 2, bạn ghép chúng lại nhưng mất nhiều thời gian. Không phải sẽ tốt hơn nếu có cửa to và cầu thang rộng sao?

Khi giải 1 bài tập, bạn cố gắng cho bài toán vào não bộ mình theo cách tương tự cái bàn trong nhà. Nếu bài toán quá phức tạp, bạn phải cắt nhỏ chúng ra, giải quyết hết các bài toán nhỏ, ghép lại thành bài toán lớn. Khi bạn thông minh hơn, não bạn "to lên", thì khi đó bạn có thể cho các bài toán khó hơn vào mà không cần cắt nhỏ nữa.

Câu hỏi còn lại là làm sao tìm được bài tập nằm ngoài vùng an toàn mà không quá khó. Bạn có thể tìm cách khác nhưng đây là cách mình làm. Mình thích SPOJ vì có nhiều bài hay. Với mỗi bài bạn có thể xem số người làm được. Lúc đầu, mình coi bài có 150 - 200 người giải và làm trong vài tháng. Khi mình thấy nó dễ vãi rồi, mình làm các bài 100 - 150 và cứ như thế. Bạn có thể làm tương tự trên TopCoder. Bắt đầu với Div 2 Easy và đến Div 1. Khi có vấn đề khi giải bài, hỏi ai đó kinh nghiệm hơn, huấn luyện viên hoặc trên diễn đàn. Có nhiều cộng đồng online, nơi có nhiều bạn sẵn lòng giúp bạn.

### Cải thiện kĩ năng lập trình

Sau khi tìm ra được solution, bạn phải code nó. Trong điều kiện lý tưởng, bạn viết code hoàn hảo mà không cần debug. Bạn có thể nghĩ rằng điều này là không thể nhưng nếu bạn xem các cao thủ trên TopCoder, đây chính là thứ mà họ làm. Sau khi ra solution, họ code thường trúng luôn trong phát đầu tiên. Tất nhiên, việc này không dễ và phải mất nhiều thời gian.

Tương tự như mảng "**Cải thiện khả năng giải quyết vấn đề**", bạn cải thiện khả năng lập trình với các bài nằm trong vùng "ra solution" an toàn nhưng nằm ngoài vùng "code" an toàn. Đây là các bài bạn nghĩ ra solution nhanh nhưng code chúng tốn nhiều thời gian và làm bạn sai nhiều khi submit.

Khi bắt đầu luyện tập, mình giải rất nhiều bài dễ. Có tuần mình toàn làm Div 2 Easy trên TopCoder. Tất nhiên, bạn sẽ trở nên phát chán nhưng cuối cùng bài của bạn đúng trong lần submit đầu tiên. Sau đó lên Div 2 Medium và cứ như thế.

### Code và Debug trên giấy

Bây giờ không nhiều bạn code trên giấy, nhưng đó cũng là cách luyện tập hay. Bạn phải nghĩ nhiều hơn trước khi bắt đầu code vì hiển nhiên là khó mà sửa code trên giấy được. Khi code trên máy, bạn thường code ngay, kể cả trước khi chắc rằng solution của mình đúng. Bạn sẽ nghĩ rằng bạn có thể sửa code nhanh trên máy khi có bug. Tuy nhiên, nhiều lúc những bug đó nặng đến mức bạn cần code lại mọi thứ. Code trên giấy giúp bạn tránh những thứ đó, vì nó buộc bạn phải nghĩ tất cả các trường hợp. Ngoải ra, mục tiêu của chúng ta là học code đúng trong lần đầu tiên mà không phải sửa nhiều, cách này rất hoàn hảo để đạt đến mục tiêu đó.

Đây cũng là một kĩ năng hữu ích trong ACM-ICPC, vì bạn chỉ có 1 máy tính và bạn nên code trên giấy càng sớm càng tốt khi có solution, đến khi bạn dùng máy thì bạn không phí thời gian nghĩ những thứ khác nữa.

À mà cũng cần debug trên giấy nữa. In một số output cần thiết khi chạy chương trình, in code ra và đọc khi bạn ngồi trên xe bus hoặc tàu. Debug trên máy tốn nhiều thời gian và trong nhiều trường hợp debug trên giấy nhanh hơn.

### Thi đấu

Bạn nên thi đấu càng nhiều càng tốt vì mục tiêu của bạn là thành công trong các cuộc thi. Khi giải bài ở nhà, bạn không căng thẳng và bạn có nhiều thời gian. Trong kì thi, thời gian là áp lực, nó có thể làm giảm khả năng giải bài của bạn. Trong điều kiện lý tưởng, bạn sẽ thi đấu tốt trong áp lực hơn là không có áp lực nào.

Bằng việc luyện tập, bạn học được cách xử lý căng thẳng và bạn cũng có thể học những chiến thuật cơ bản. Ví dụ, 1 giờ trước khi hết kì thi 5 tiếng, sẽ rất tệ nếu làm bài mới khi bạn có 3 bài chưa làm xong với nhiều submission sai.

### Cải thiện chất lượng code

Sau khi submit và accepted, quay lại đọc và sửa code cho đẹp hơn và ngắn hơn. Đọc code của người khác và sửa lại. Thường cao thủ như Petr hay tourist có những code cực đẹp và chúng có thể giúp bạn trong tương lai.

Bạn cũng có thể sửa code cho nó chạy nhanh hơn sau khi accepted. Điều này có thể làm code dài hơn và khó hiểu hơn. Các trang như SPOJ có ranking của nhưng code nhanh nhất, hãy cố gắng làm code của bạn vươn cao nhất có thể. Bạn sẽ học được nhiều thứ về tốc độ của các câu lệnh trong ngôn ngữ lập trình bạn đang dùng.

### Chăm sóc bản thân

Cái này nghe có vẻ lạ, nhưng mình nghĩ thể dục và một chế độ ăn khỏe mạnh sẽ rất quan trọng cho lập trình viên. Não là một phần của cơ thể và chúng ta có thể xem phần còn lại như là trợ lý của não bộ. Nếu bạn không chăm sóc đám trợ lý này cho tốt, nó có thể ảnh hưởng xấu đến não bạn.

## Động lực

Các kì thi giúp tăng khả năng lập trình của bạn. Nhiều người cho rằng các bài tập lập trình thi đấu không giống các vấn đề trong thế giới thực lắm và điều này đúng trong nhiều trường hợp. Khi đi làm, các vấn đề mang tính thuật toán chỉ chiếm 5 - 10% công việc nếu bạn may mắn thôi. Các bài toán khi đi làm không được nêu ra rõ ràng, lấy được input tốt rất khó và nhiều solution quá phức tạp hoặc quá chậm khi chạy.

Tuy nhiên, vẫn tốt khi bạn luyện môn này. Trong trường mọi người đều học toán, đọc và viết nhưng ít người làm nhà toán học, nhà văn hoặc reader (nếu có cái nghề đó). Chúng ta cần những kĩ năng này trong cuộc sống hàng ngày. Ngay cả khi bạn không nghiên cứu toán, nó giúp bạn suy nghĩ một cách logic. Có thể bạn không viết nhiều, nhưng viết giúp bạn luyện não để hình thành suy nghĩ theo một hướng dễ hiểu.

Tất nhiên, có nhiều kĩ năng cần để thành 1 lập trình viên giỏi. Bạn nên học cách làm việc nhóm, cách dùng git, vân vân... Nhưng trong lập trình thi đấu, nó dạy bạn cách chia nhỏ bài toán lớn thành các bài toán con, giải chúng rồi ghép lại. Ít bug xuất hiện hơn và bạn sẽ quan tâm nhiều hơn đến độ phức tạp thời gian của code.

Như bạn thấy đấy, có nhiều lợi ích của lập trình thi đấu. Tuy nhiên, mình thi vì mình thấy vui. Phần luyện tập cũng hay phết, nhưng cái này thường không ép bạn cày ngày đêm được nếu bạn không thấy thích.

Thật vậy, nếu không thấy vui, bạn nên nghỉ đi và làm gì đó khác. Mình từng gặp nhiều bạn rất khủng, nhưng họ có vẻ không thích món này lắm. Nếu bạn thích các dự án mã nguồn mở hoặc nghiên cứu khoa học, cứ làm đi, không sao đâu.

Tuy nhiên, nếu bạn phân vân giữa thi đấu và chơi game, lướt Reddit hoặc Facebook, bạn nên nghĩ cách tạo động lực cho mình nhiều hơn. Thử trò này xem: nghĩ về bản thân 10 năm nữa. Bạn có nghĩ rằng người đó sẽ nói với bạn rằng "Minh ước mình chơi game nhiều hơn, lướt Reddit và Facebook nhiều hơn và luyện code ít hơn khi còn là sinh viên" không? Mình không cấm các bạn làm những việc đó, ví dụ Reddit rất có ích khi tìm tài liệu viết bài blog này. Cứ làm, nhưng vừa phải thôi.

## Thất bại

Thất bại là tốt, nó cho thấy bạn đang sai cái gì. Ngoài ra, não bạn làm việc theo kiểu bạn học tốt nhất từ những sai lầm của bản thân. Đây là một trích dẫn hay trong bài [Why Floundering Is Good](http://ideas.time.com/2012/04/25/why-floundering-is-good/):

!!! tip "Trích dẫn"
    Hãy gọi nó là nghịch lý học tập: khi bạn học, bạn càng loay hoay, thậm chí thất bại nhiều, bạn càng nhớ lâu hơn và ứng dụng những thứ bạn học tốt hơn sau này.

Thất bại rất quan trọng trong quá trình học, bạn cần biết cách đương đầu với nó. Đó được gọi là self-compassion (tự vị tha) trong tiếng Anh. Đây là các trích dẫn về self-compassion trong [To Succeed, Forget Self-Esteem](http://blogs.hbr.org/cs/2012/09/to_succeed_forget_self-esteem.html).

!!! tip "Trích dẫn"
    Self-compassion là việc sẵn sàng nhìn vào sai lầm và thiếu sót của bản thân với lòng tốt và sự hiểu biết, đó là việc chấp nhận thực tế rằng bạn thực sự là con người. Khi bạn self-compassionate khi gặp khó khăn, bạn không đánh giá bản thân khắc nghiệt quá, cũng không cảm thấy cần tập trung vào tất cả những gì tốt nhất của mình để bảo vệ bản ngã. (*Self-compassion is a willingness to look at your own mistakes and shortcomings with kindness and understanding — it’s embracing the fact that to err is indeed human. When you are self-compassionate in the face of difficulty, you neither judge yourself harshly, nor feel the need to defensively focus on all your awesome qualities to protect your ego.*)

!!! tip "Trích dẫn"
    Đây là thực tế không tránh khỏi: Bạn sẽ hoảng loạn. Tất cả mọi người, kể cả những người thành công nhất, tạo ra cả đống sai lầm. Chìa khóa sự thành công, như mọi người đều biết, là rút kinh nghiệm và tiến lên. Nhưng không phải ai cũng biết phải làm như thế nào. Self-compassion là thứ bạn cần. Cho nên, hãy cho bản thân nghỉ ngơi đi. (*Here’s an unavoidable truth: You are going to screw up. Everyone — including very successful people — makes boatloads of mistakes. The key to success is, as everyone knows, to learn from those mistakes and keep moving forward. But not everyone knows how. Self-compassion is the how you’ve been looking for. So please, give yourself a break.*)

Các bạn nên đọc cả bài viết đó thì sẽ tốt hơn.
