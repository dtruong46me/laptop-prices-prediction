


Chào bạn, với tư cách là một Senior AI Engineer, tôi đã thiết kế slide deck này theo chuẩn của các hội nghị khoa học (ví dụ: RecSys, KDD, hoặc các track ứng dụng của ACL). 

Điểm mấu chốt khi thuyết trình dự án này là: **Đừng chỉ tập trung vào model**. Thuật toán (KNN, RF, MLP) là cơ bản, nhưng **Data Engineering (dùng LLM để parse text, dùng Fuzzy để mapping)** mới là điểm sáng giá và tốn công nhất. Narrative (mạch truyện) sẽ đi từ: *Dữ liệu rác $\rightarrow$ Dùng AI (LLM) làm sạch rác $\rightarrow$ Xây dựng Feature $\rightarrow$ Train Regression Models*.

Dưới đây là cấu trúc chi tiết cho 16 slides chính, kèm Appendix và Q&A.

---

# SLIDE DECK: 2023 LAPTOP PRICE ANALYSIS AND PREDICTION

## [Slide 1] Title: Laptop Price Analysis and Prediction
**Purpose:** Giới thiệu dự án, team và tạo ấn tượng ban đầu chuyên nghiệp.

**Key Points:**
- Project: Laptop Price Analysis and Prediction.
- Course: Introduction to Data Science (IT4142E).
- Institution: Hanoi University of Science and Technology.
- Presenter: [Tên của bạn/Nhóm].

**Visual Suggestions:**
- Logo HUST.
- Hình ảnh abstract về AI/Data flow hoặc một minh họa về giá laptop.

**Speaker Notes:**
- Chào mừng ban giám khảo và các bạn. Hôm nay nhóm chúng tôi xin trình bày dự án "Phân tích và dự đoán giá Laptop". 
- Trong kỷ nguyên e-commerce, việc định giá sản phẩm công nghệ là một bài toán phức tạp cho cả người mua lẫn người bán. 
- Dự án này ứng dụng Data Engineering và Machine Learning để giải quyết bài toán đó.

**Transition Sentence:**
- Để hiểu tại sao bài toán này quan trọng, hãy xem xét bối cảnh thị trường hiện nay.

---

## [Slide 2] Title: Problem Statement & Motivation
**Purpose:** Nêu rõ lý do thực hiện dự án và khó khăn cốt lõi của bài toán.

**Key Points:**
- Định giá laptop phụ thuộc nhiều thông số (CPU, GPU, RAM).
- Dữ liệu E-commerce phân mảnh, không đồng nhất.
- Người mua: Khó xác định giá trị thực của cấu hình.
- Người bán: Cần tối ưu chiến lược giá cạnh tranh.
- Mục tiêu: Xây dựng pipeline dự đoán giá tự động (Regression).

**Visual Suggestions:**
- Hình ảnh so sánh 2 web bán hàng (Amazon vs Newegg) với cùng 1 sản phẩm nhưng format text khác nhau hoàn toàn.

**Speaker Notes:**
- Giá của một chiếc laptop không chỉ là một con số ngẫu nhiên, nó bị chi phối bởi hàng tá thông số phần cứng.
- Khó khăn lớn nhất không phải là thuật toán, mà là dữ liệu trên web vô cùng hỗn loạn.
- Mục tiêu của chúng tôi là biến đống dữ liệu văn bản hỗn độn đó thành một hệ thống dự đoán giá chuẩn xác.

**Transition Sentence:**
- Để giải quyết vấn đề này, nhóm đã đề xuất 3 đóng góp chính sau đây.

---

## [Slide 3] Title: Key Contributions
**Purpose:** Làm nổi bật giá trị cốt lõi (selling points) của bài báo cáo.

**Key Points:**
- **End-to-End Pipeline:** Tự động hóa từ thu thập đến dự đoán.
- **LLM Integration:** Dùng GPT-6B xử lý văn bản phi cấu trúc.
- **Entity Resolution:** Mapping tên linh kiện bằng Fuzzy Matching.
- **Structured Dataset:** Xây dựng bộ dữ liệu sạch >7,000 samples.
- **Baseline Models:** Benchmark chi tiết KNN, Random Forest, MLP.

**Visual Suggestions:**
- Icon minh họa cho 3 pillars: Data Pipeline, LLM NLP, Predictive ML.

**Speaker Notes:**
- Đóng góp lớn nhất của chúng tôi nằm ở khâu Data Engineering.
- Thay vì dùng Regex thông thường, chúng tôi tích hợp LLM để parse dữ liệu.
- Kết quả là tạo ra một bộ dataset sạch với hơn 7000 records, sẵn sàng cho việc train các model ML truyền thống.

**Transition Sentence:**
- Hãy đi sâu vào cấu trúc của bộ dữ liệu mà chúng tôi đã thu thập.

---

## [Slide 4] Title: Dataset Overview & Challenges
**Purpose:** Mô tả quy mô dữ liệu và các rào cản kỹ thuật khi thu thập.

**Key Points:**
- **Nguồn dữ liệu:** Amazon, Newegg, B&H Photo Video.
- **Amazon:** Có cấu trúc nhưng chứa nhiễu (hàng Refurbished).
- **Newegg:** Dữ liệu hoàn toàn phi cấu trúc, chặn scraping (CAPTCHA).
- **Passmark DB:** Nguồn tham chiếu benchmark CPU/GPU.
- **Tổng dung lượng:** >7,000 records sau khi làm sạch.

**Visual Suggestions:**
- Bảng tóm tắt số lượng records từ từng nguồn.
- Ảnh chụp màn hình CAPTCHA của Newegg.

**Speaker Notes:**
- Chúng tôi thu thập dữ liệu từ 3 nền tảng lớn. 
- Newegg là thách thức lớn nhất do cơ chế chống scraping và định dạng text tự do.
- Ngoài ra, việc dùng tên CPU/GPU trực tiếp cho Machine Learning là vô nghĩa, nên chúng tôi phải dùng thêm DB Passmark.

**Transition Sentence:**
- Vậy chúng tôi đã biến đổi raw data thành features như thế nào? Đây là pipeline tổng thể.

---

## [Slide 5] Title: System Architecture & Data Pipeline
**Purpose:** Cung cấp cái nhìn toàn cảnh về kiến trúc hệ thống (Data Flow).

**Key Points:**
- Thu thập raw HTML/Text từ web.
- Trích xuất thông tin (Information Extraction) bằng LLM.
- Khớp thực thể (Entity Resolution) bằng Fuzzy Matching.
- Tiền xử lý (Imputation, Outlier Removal, Scaling).
- Đào tạo và đánh giá mô hình Regression.

**Visual Suggestions:**
- Vẽ một Flowchart nằm ngang từ trái sang phải minh họa 5 steps trên.

**Speaker Notes:**
- Đây là pipeline hệ thống từ đầu tới cuối.
- Dữ liệu thô đi qua lớp NLP để trích xuất, sau đó qua lớp thuật toán chuỗi để chuẩn hóa.
- Cuối cùng mới được đưa vào các mô hình Machine Learning.
- Hai bước khó nhất là LLM Extraction và Fuzzy Matching.

**Transition Sentence:**
- Tôi xin phép trình bày chi tiết về bước ứng dụng LLM.

---

## [Slide 6] Title: Step 1 - LLM Information Extraction
**Purpose:** Giải thích cách biến Text thô thành JSON có cấu trúc.

**Key Points:**
- Dữ liệu Newegg: Khối văn bản lộn xộn.
- Traditional RegEx: Thất bại do format quá đa dạng.
- Giải pháp: Few-Shot Prompting với GPT-J-6B.
- Input: Product description text.
- Output: Structured Schema (CPU, GPU, RAM, OS).

**Visual Suggestions:**
- Bên trái: Đoạn text raw của 1 laptop. Mũi tên qua icon LLM. Bên phải: Khối JSON rõ ràng (Brand: ASUS, CPU: i7...).

**Speaker Notes:**
- Với dữ liệu vô cấu trúc, các bộ lọc regex tĩnh hoàn toàn bó tay.
- Chúng tôi đã thiết kế prompt cho GPT-6B với phương pháp few-shot.
- LLM hoạt động cực kỳ hiệu quả trong việc trích xuất chính xác tên CPU, GPU từ các đoạn mô tả rất dài.

**Transition Sentence:**
- Sau khi có tên CPU/GPU, chúng ta gặp bài toán thứ hai: Sự đa dạng tên gọi.

---

## [Slide 7] Title: Step 2 - Entity Resolution (Fuzzy Matching)
**Purpose:** Minh họa cách chuyển String thành Continuous Value.

**Key Points:**
- Vấn đề: 1 CPU có hàng tá biến thể tên gọi.
- Giải pháp: Thư viện `fuzzywuzzy` (Levenshtein Distance).
- Tính trung bình 4 metrics (Ratio, Partial, Token Sort/Set).
- Match với DB Passmark $\rightarrow$ Lấy điểm Benchmark.
- Chuyển Text categories $\rightarrow$ Continuous features.

**Visual Suggestions:**
- Flow text: "amd ryzen 5 7530u" $\rightarrow$ [Fuzzy Match] $\rightarrow$ "AMD Ryzen 5 7530U" $\rightarrow$ [Passmark] $\rightarrow$ Score: 16,400.

**Speaker Notes:**
- Cùng một con chip nhưng mỗi người bán viết một kiểu. Model ML không thể hiểu điều này.
- Chúng tôi dùng khoảng cách Levenshtein để so khớp tên cạo được với database chuẩn của Passmark.
- Kết quả là ta biến đổi được một chuỗi Text thành một điểm số sức mạnh toán học.

**Transition Sentence:**
- Cuối cùng, để đưa vào model, dữ liệu cần được chuẩn hóa toán học.

---

## [Slide 8] Title: Step 3 - Preprocessing & Outlier Handling
**Purpose:** Chứng minh tính chặt chẽ trong xử lý số liệu thống kê.

**Key Points:**
- Imputation: Điền khuyết bằng Median (Weight dùng Interpolation).
- Outliers: Dùng IQR loại bỏ dữ liệu lỗi (VD: Laptop giá $20).
- Categorical: One-Hot Encoding (Brand, OS).
- Continuous: Standard Scaler ($\mu=0, \sigma=1$).
- Mục tiêu: Ngăn mô hình bị nhiễu và chênh lệch scale.

**Visual Suggestions:**
- Boxplot minh họa việc cắt đuôi outliers bằng IQR.

**Equations:**
- IQR = $Q_3 - Q_1$
- Standardization: $x_{scaled} = \frac{x - \mu}{\sigma}$

**Speaker Notes:**
- Dữ liệu cạo về có những lỗi nghiêm trọng như bao chống sốc bị nhận nhầm là laptop giá 20 đô. 
- Chúng tôi dùng Interquartile Range để cắt bỏ các nhiễu này.
- Mọi dữ liệu chữ đều được One-Hot, và dữ liệu số được đưa về phân phối chuẩn để tối ưu hàm loss.

**Transition Sentence:**
- Trước khi train model, chúng tôi thực hiện phân tích EDA để tìm ra Insight.

---

## [Slide 9] Title: EDA - Feature Correlation
**Purpose:** Chứng minh bằng thống kê rằng việc mapping ra Passmark là đúng.

**Key Points:**
- Ma trận tương quan Pearson.
- Price tương quan thuận mạnh với `GPU_Mark` (0.63).
- Price tương quan thuận mạnh với `CPU_Mark` (0.61).
- RAM (0.32) và Storage (0.18) đóng vai trò phụ trợ.
- Khẳng định: Hiệu năng CPU/GPU quyết định giá máy.

**Visual Suggestions:**
- Ảnh Heatmap (Figure 6) cắt gọn, highlight bằng khung đỏ vào các ô CPU, GPU vs Price.

**Speaker Notes:**
- Ma trận tương quan xác nhận giả thuyết ban đầu của chúng tôi là đúng.
- Hai feature tự chế từ Passmark (CPU và GPU Mark) có độ tương quan mạnh nhất với Giá.
- RAM hay Ổ cứng chỉ đóng vai trò thứ yếu trong việc đẩy giá lên cao.

**Transition Sentence:**
- Nhìn vào phân phối theo hãng sản xuất, ta cũng thấy rõ chiến lược giá của họ.

---

## [Slide 10] Title: EDA - Market Segmentation
**Purpose:** Hiển thị phân bố giá theo hãng (Business Insight).

**Key Points:**
- Đa số thị trường tập trung phân khúc $500 - $1,000.
- MSI: Định vị phân khúc cao cấp (High CPU/GPU Mark).
- HP, Lenovo, Acer: Tập trung phân khúc giá rẻ/tầm trung.
- Dell, ASUS: Độ phủ rộng, từ sinh viên đến Workstation.
- Phân phối giá bị lệch phải (Right-skewed).

**Visual Suggestions:**
- Boxplot theo Brand (Figure 8).

**Speaker Notes:**
- MSI tập trung cực kỳ đậm đặc ở vùng giá cao, tương đương với điểm chuẩn CPU/GPU cao của họ.
- Ngược lại, HP hay Acer tập trung ở đuôi dưới của biểu đồ.
- Insights này rất hữu ích cho các chiến lược định giá của Retailers.

**Transition Sentence:**
- Với bộ feature đã hoàn thiện, chúng tôi đưa vào 3 kiến trúc mô hình.

---

## [Slide 11] Title: Model Architecture - KNN & Random Forest
**Purpose:** Giới thiệu 2 thuật toán Machine Learning truyền thống.

**Key Points:**
- **KNN Regressor:** Dựa trên khoảng cách Euclidean. 
- Nhạy cảm với Outliers, cần Grid Search tìm K.
- **Random Forest:** Ensemble of Decision Trees (Bagging).
- Mạnh mẽ, xử lý tốt Non-linear, không cần scale sâu.
- Grid Search tối ưu `max_depth` và `n_estimators`.

**Visual Suggestions:**
- Sơ đồ icon nhỏ: KNN (các điểm cluster), RF (nhiều cây quyết định gộp lại).

**Speaker Notes:**
- Chúng tôi chọn KNN làm baseline vì cơ chế tìm các laptop tương đồng trong không gian vector.
- Random Forest được chọn vì tính mạnh mẽ của Tree-based model với dữ liệu Tabular, đặc biệt là không bị ảnh hưởng bởi nhiễu.

**Transition Sentence:**
- Để đối trọng với Machine Learning truyền thống, chúng tôi thử nghiệm Deep Learning.

---

## [Slide 12] Title: Model Architecture - Multilayer Perceptron
**Purpose:** Giới thiệu mạng nơ-ron nhân tạo.

**Key Points:**
- Kiến trúc Feed-forward Neural Network.
- Setup 1: All features $\rightarrow$ 3x128 Hidden Layers.
- Setup 2: Chỉ CPU & GPU $\rightarrow$ 4 Hidden Layers.
- Activation: ReLU để học Non-linearity.
- Regularization: L2 Weight Decay chống Overfitting.

**Visual Suggestions:**
- Sơ đồ MLP 3 layers đơn giản (Input $\rightarrow$ Hidden $\rightarrow$ Output).

**Speaker Notes:**
- Mô hình thứ 3 là MLP. Chúng tôi thử nghiệm 2 cấu hình: 1 dùng toàn bộ features và 1 chỉ dùng 2 features mạnh nhất.
- Chúng tôi dùng ReLU và thêm hàm phạt L2 để ngăn mạng nơ-ron học vẹt dữ liệu.

**Transition Sentence:**
- Để đánh giá model nào tốt nhất, ta cần định nghĩa đúng Metrics.

---

## [Slide 13] Title: Evaluation Metrics Meaning
**Purpose:** Biện luận lý do chọn MAPE và $R^2$ làm thước đo chính.

**Key Points:**
- **MSE:** Phạt nặng sai số lớn, dùng làm Loss Function.
- **MAE:** Sai số tuyệt đối (USD), dễ hiểu nhưng phụ thuộc scale.
- **MAPE (%):** Ý nghĩa thực tiễn cao cho bài toán kinh doanh.
- **$R^2$ Score:** Đo lường phần trăm phương sai giá được giải thích.
- Focus: Đánh giá dựa trên MAPE và $R^2$.

**Equations:**
- $MAPE = \frac{100\%}{n} \sum \left| \frac{y_i - \hat{y}_i}{y_i} \right|$
- $R^2 = 1 - \frac{RSS}{TSS}$

**Speaker Notes:**
- Trong training, chúng tôi tối ưu hóa MSE. 
- Tuy nhiên, khi báo cáo kết quả, việc nói "sai số bình phương là 134 nghìn" không có ý nghĩa thực tế.
- Do đó, để so sánh hiệu quả, chúng tôi sử dụng MAPE (tỷ lệ phần trăm sai lệch) và $R^2$.

**Transition Sentence:**
- Và đây là kết quả đối đầu của 3 mô hình.

---

## [Slide 14] Title: Experimental Results - Consolidated
**Purpose:** Trình bày kết quả tổng hợp một cách minh bạch.

**Key Points:**
- Random Forest vượt trội hoàn toàn các model khác.
- RF đạt MAPE 21.78% và giải thích được ~64% phương sai.
- KNN (K=7) đứng thứ hai sau khi loại bỏ nhiễu.
- MLP có kết quả kém nhất dù phức tạp nhất.
- Setup MLP full features tốt hơn Setup chỉ có CPU/GPU.

**Visual Suggestions:**
- Bảng Master Table (như trong report), bôi đậm (bold) dòng của Random Forest.

**Speaker Notes:**
- Bảng này tổng hợp kết quả tốt nhất sau khi đã chạy Grid Search cho cả 3 thuật toán.
- Rõ ràng Random Forest là kẻ chiến thắng tuyệt đối với MAPE thấp nhất (khoảng 21%) và $R^2$ cao nhất.

**Transition Sentence:**
- Tại sao Random Forest lại thắng Neural Networks trong bài toán này?

---

## [Slide 15] Title: Results Discussion & Insights
**Purpose:** Giải thích "Why" thay vì chỉ show kết quả (tư duy nhà khoa học).

**Key Points:**
- Môi trường Tabular Data: Tree-based model luôn chiếm ưu thế.
- MLP overfits: Dataset ~7000 dòng là quá nhỏ cho Deep Learning.
- Khoảng trống 36% variance (1 - $R^2$): Do các Hidden Variables.
- Hidden variables: Premium Brand (Apple tax), chất liệu, aesthetic.
- Feature Importance: CPU/GPU là cốt lõi, nhưng RAM/SSD vẫn cần.

**Visual Suggestions:**
- Icon não bộ suy nghĩ. Pie chart biểu diễn 64% explained variance vs 36% unexplained.

**Speaker Notes:**
- Không có gì ngạc nhiên khi Random Forest thắng. Deep Learning như MLP cần hàng trăm ngàn dòng dữ liệu để hội tụ.
- Mô hình dự đoán đúng 64% sự chênh lệch giá. 36% còn lại đến từ những thứ dữ liệu không có: Ví dụ thuế thương hiệu của Apple, viền nhôm xước hay màn hình OLED.

**Transition Sentence:**
- Nhận thức được các giới hạn này, chúng tôi đề xuất các hướng đi tương lai.

---

## [Slide 16] Title: Limitations & Future Work
**Purpose:** Thể hiện tinh thần học thuật: Biết rõ điểm yếu của mình.

**Key Points:**
- Giới hạn 1: Nội suy Weight (Linear) chưa chuẩn thống kê.
- Giới hạn 2: Chi phí/độ trễ khi call LLM API quá cao.
- Tương lai 1: Thử nghiệm Gradient Boosting (XGBoost, LightGBM).
- Tương lai 2: Fine-tune model NLP nhỏ (RoBERTa) in-house.
- Tương lai 3: Cào thêm Time-series data (Mùa sale).

**Visual Suggestions:**
- Icon cảnh báo (Limitations) và icon bóng đèn (Future Work).

**Speaker Notes:**
- Dự án còn vài hạn chế, ví dụ việc dùng Linear Interpolation cho biến Weight chưa thật sự tối ưu về mặt thống kê. Việc gọi GPT API cũng đắt đỏ.
- Tương lai, chúng tôi sẽ triển khai XGBoost thay cho Random Forest, và fine-tune một model NLP cục bộ để tự parse text mà không tốn phí API.

---

## [Slide 17] Title: Conclusion
**Purpose:** Chốt lại giá trị của toàn bộ dự án.

**Key Points:**
- Trình bày thành công Pipeline dự đoán giá end-to-end.
- LLM & Fuzzy Matching xử lý triệt để E-commerce rác.
- Bộ feature mapping Passmark thể hiện sức mạnh phân tích.
- Random Forest đạt mức ứng dụng tốt làm baseline.
- Nền tảng vững chắc cho các nghiên cứu Pricing Engine tiếp theo.

**Visual Suggestions:**
- Text "Thank You" lớn. Mã QR dẫn đến Github repo của nhóm.

**Speaker Notes:**
- Tóm lại, chúng tôi đã đóng gói thành công một giải pháp end-to-end xử lý mớ bòng bong dữ liệu e-commerce.
- Dù thuật toán không mới, nhưng luồng xử lý Data Engineering chứng minh độ hiệu quả cao.
- Cảm ơn thầy và các bạn đã lắng nghe. Chúng tôi rất mong nhận được câu hỏi.

---
---

# APPENDIX SLIDES (Dùng khi bị hỏi xoáy)

## [Appendix 1] Hyperparameter Tuning Details
- **KNN:** Lưới tìm kiếm tập trung K=[3, 5, 7, 9]. Tối ưu tại K=7, Weights='distance', Algorithm='ball_tree'.
- **Random Forest:** `max_depth` = 20, `n_estimators` = 200. Hạn chế Overfitting tốt hơn cấu hình mặc định.
- **MLP:** Learning rate = 0.1, L2 Penalty (Weight Decay) = 0.001. Adam optimizer.

## [Appendix 2] Fuzzy Matching Algorithm Breakdown
- **Thư viện:** `fuzzywuzzy` (Levenshtein Distance).
- **Cơ chế:** Tính TBC của 4 metrics:
  1. Simple Ratio (so khớp trực tiếp).
  2. Partial Ratio (so khớp chuỗi con).
  3. Token Sort Ratio (Sắp xếp từ khóa rồi so).
  4. Token Set Ratio (Loại trùng lặp rồi so).
- **Ngưỡng:** Lấy TBC cao nhất.

---
---

# Q&A PREPARATION (5 Câu hỏi khó và Cách trả lời)

**Q1. Tại sao các bạn lại dùng Linear Interpolation (nội suy tuyến tính) cho dữ liệu Weight (Cân nặng) trong khi đây không phải là chuỗi thời gian (Time-series)?**
> **Trả lời:** Xin cảm ơn câu hỏi rất tinh tế. Đúng là Linear Interpolation mặc định dựa vào thứ tự index hiện tại của Dataframe, điều này mang tính ngẫu nhiên và thiếu cơ sở thống kê với Cross-sectional data. Đây là một sai lầm trong kỹ thuật mà nhóm đã note lại trong phần Limitations. Phương pháp đúng đắn hơn mà nhóm sẽ cập nhật là GroupBy theo `Brand` và `Monitor Size` sau đó dùng Median Imputation.

**Q2. Tại sao không dùng các model mạnh hơn như XGBoost hay LightGBM cho bài toán Tabular Data này?**
> **Trả lời:** Trong phạm vi môn học Introduction to Data Science, chúng em tập trung vào việc áp dụng và hiểu sâu các thuật toán cơ bản (KNN, RF, MLP). Random Forest đóng vai trò là một baseline vững chắc. Việc triển khai Gradient Boosting (như XGBoost) là hướng mở rộng chắc chắn chúng em sẽ làm trong tương lai để ép sai số MAPE xuống mức thấp nhất.

**Q3. Dùng LLM API (GPT-6B) để parse dữ liệu rất tốn kém và chậm. Nếu đưa vào Production thì hệ thống của các bạn có sập không?**
> **Trả lời:** Chắc chắn là có nếu chạy Real-time inference. Trong dự án này, LLM được dùng ở khâu *Data Preparation/Offline Processing* để tạo training dataset, chứ không phải Real-time. Trong thực tế (Production), quy trình chuẩn sẽ là: Dùng LLM API cào ra 1 tập data sạch $\rightarrow$ dùng tập đó fine-tune một model nhỏ (như RoBERTa-base ~110M params) $\rightarrow$ deploy model nhỏ đó để parse text với tốc độ mili-giây và chi phí 0 đồng.

**Q4. Mạng MLP của các bạn bị Overfitting hay Underfitting? Tại sao kết quả lại kém hơn Random Forest?**
> **Trả lời:** MLP có dấu hiệu Overfitting sớm (dù đã cài L2 Regularization). Nguyên nhân gốc rễ là **Data Starvation** (thiếu dữ liệu). Mạng NN với hàng trăm nghìn parameters cần tập dữ liệu cực lớn để tối ưu bề mặt loss function. Với chỉ khoảng 7000 rows x 9 features, Random Forest (vốn hoạt động dựa trên Information Gain/Gini Impurity) cắt không gian feature hiệu quả hơn nhiều so với việc NN cố gắng vạch ra các hyperplane.

**Q5. MAPE = 21% nghĩa là dự đoán lệch 21% giá tiền. Con số này khá cao trong thực tế mua bán. Làm sao để cải thiện?**
> **Trả lời:** Chênh lệch 21% một phần do mô hình thiếu "Hidden Features". Ví dụ: Một chiếc Dell XPS 15 và Dell Inspiron 15 có chung CPU, GPU, RAM, nhưng bản XPS đắt gấp rưỡi do vỏ nhôm nguyên khối, tản nhiệt buồng hơi và viền màn hình mỏng. Dữ liệu text cào về thường bỏ sót các yếu tố "Premium" này. Để cải thiện, ta cần crawl thêm field "Product Line/Series" (XPS, ROG, Legion) hoặc dùng Computer Vision để đánh giá độ "Premium" qua ảnh sản phẩm.
