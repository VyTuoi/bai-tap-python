
# Bài tập 1: 
class BrowserHistory:
    
    def __init__(self, homepage):
        self.current = homepage
        self.back_stack = []
        self.forward_stack = []
        
    def visit(self, url):
        self.back_stack.append(self.current)
        self.current = url
        
        # vào trang mới thì mất lịch sử forward
        self.forward_stack.clear()
        
    def back(self, steps):
        for _ in range(steps):
            
            # Không còn trang để lùi
            if not self.back_stack:
                break
            self.forward_stack.append(self.current)
            self.current = self.back_stack.pop()
        return self.current
    
    def forward(self, steps):
        
        for _ in range(steps):
            
            # Không còn trang để tiến 
            if not self.forward_stack:
                break
            
            self.back_stack.append(self.current)
            self.current = self.forward_stack.pop()
        return self.current

print()
print("Kết quả bài tập 1")

 # Chạy thử với dữ liệu đề bài cho

h = BrowserHistory("trang-chu")
    
h.visit("san-pham/ao-thun")
h.visit("san-pham/quan-jean")
h.visit("gio-hang")
    
print(h.back(1))
print(h.back(1))
print(h.forward(1))
print(h.back(3))

# Bài tập 2:
# 2. Kiểm tra cú pháp JSON hợp lệ [STACK]
# - Chức năng gateway cần kiểm tra payload JSON (thông tin) trước khi xử lý đơn hàng.
# Đề bài: Viết hàm is_valid_brackets(s) kiểm tra chuỗi có các cặp ngoặc {}, [], () hợp lệ không.
# Chuỗi được cho là hợp lệ nếu mở ngoặc “{“, “[“, “(“ sẽ được đóng bởi “}”, “]”, “)” tương ứng.
# Gợi ý: Dùng stack để theo kiểm tra ngoặc mở phải có ngoặc đóng tương ứng.

# ( phải đóng bằng )
# [ phải đóng bằng ]
# { phải đóng bằng }

# và phải đóng đúng thứ tự.

# def is_valid_brackets(s):
#     # Tạo một stack rỗng để lưu các ngoặc 
#     stack =[]
    
#     # Bảng quy đổi:
#     # Nếu gặp ) thì phải tìm (
#     # Nếu gặp ] thì phải tìm [
#     # Nếu gặp } thì phải tìm {
        
#     pairs = {
#         ")":"(",
#         "]":"[",
#         "}":"{"
#     }
#     # Duyệt từng kí tự trong chuỗi
#     for ch in s:
#         # Nếu là ngoặc mở

def is_valid_brackets(s):
    
    # Tạo stack rỗng để lưu các ngoặc mở
    stack = []
    # Từ điển để xác định cặp ngoặc tương ứng
    # Key là ngoặc đóng, value là ngoặc mở
    pairs = {
        ")": "(",
        "]": "[",
        "}": "{"
    } 
    
    # Duyệt từng kí tự trong chuỗi
    for char in s:
        # Nếu là ngoặc mở thì cho vào stack
        if char in "([{":
            stack.append(char)
        # Nếu là ngoặc đóng thì kiểm tra
        elif char in ")]}":
            # Trong stack không có  ngoặc mở tương ứng để ghép
            if not stack:
                return False
            
            # Lấy ngoặc mở gần nhất
            top = stack.pop()
            
            # Nếu không khớp loại ngoặc
            if top !=  pairs[char]:
                return False
        # Sau khi duyệt xong, nếu stack còn phần tử
        # nghĩa là còn ngoặc mở chưa được đóng 
    if len(stack) == 0:
        return True
    else:
        return False
    
    
print("Kết quả bài tập 2: ")
print(is_valid_brackets('{"name": "An", "items": [1, 2]}'))
print(is_valid_brackets('{"data": [{"id": 1}'))
print(is_valid_brackets('(())'))
print(is_valid_brackets('{"data": [{"id": 1]}'))

# Bài tập 3:
#  Viết hàm validate_transaction_order(events) kiểm tra list event có tuân theo flow: 
#      INIT → PROCESSING → COMPLETED hoặc INIT → PROCESSING → FAILED. 
# Input: 
# events1 = [ 
# {"txn_id": "T1", "event": "INIT"}, 
# {"txn_id": "T2", "event": "INIT"}, 
# {"txn_id": "T2", "event": "PROCESSING"}, 
# {"txn_id": "T2", "event": "COMPLETED"}, 
# {"txn_id": "T1", "event": "PROCESSING"}, 
# {"txn_id": "T1", "event": "FAILED"}, 
# ] 
# events2 = [ 
# {"txn_id": "T3", "event": "INIT"}, 
# {"txn_id": "T3", "event": "COMPLETED"}, # thieu PROCESSING 
# ] 
# validate_transaction_order(events1) 
# validate_transaction_order(events2)


# Output: 
# {"valid": True, "completed": 2, "errors": []} 
# {"valid": False, "completed": 0, 
# "errors": ["T3: thieu buoc PROCESSING"]}


def validate_transaction_order(events):
    #  Dictionnary dùng để lưu trạng thái của từng Transaction.
    #  Ví dụ:
    #     {"T1": "PROCESSING",
    #      "T2": "INIT"
    #      }
    state = {} 
    
    # Danh sách dùng để lưu các lỗi phát hiện được.
    errors = []
    
    # Đếm só transaction(giao dịch) kết thúc đúng quy trình
    completed = 0
    
    # Duyệt từng event trong danh sách events
    for item in events:
        # Lấy mã transaction.
        # Ví dụ: "T1"
        txn_id = item["txn_id"]
        # Lấy tên event.
        # Ví dụ: "INIT"
        event = item["event"]
        
        # Nếu transaction chưa từng xuất hiện trước đó.
        if txn_id not in state:
            
            # Transaction mới bắt buộc phải bắt đầu bằng INIT.
            if event == "INIT":
                # Ghi nhận trạng thái hiện tại của transaction.
                state[txn_id] = "INIT"
            else:
                # Nếu transaction mới mà không bắt đầu bằng INIT thì đây là lỗi.
                errors.append(f"{txn_id}: thiếu bước INIT")
        
        # Nếu transaction đã từng xuất hiện trước đó.
        else:
            
            # lấy trạng thái hiện tại của transaction.
            current_state = state[txn_id]
            
            # INIT => PROCESSING
            
            if current_state == "INIT": 
                
                # Sau INIT chỉ được phép là PROCESSING.
                if event == "PROCESSING":
                    
                    # Cập nhật trạng thái mới.
                    state[txn_id] = "PROCESSING"
                
                # Nếu trạng thái  mới của event này không phải là PROCESSING thì đây là lỗi.
                else:
                    errors.append(f"{txn_id}: thiếu bước PROCESSING")
            
            # PROCESSING => COMPLETED hoặc FAILED
            elif current_state == "PROCESSING":  # trạng thái hiện tại
                
                # Nếu trạng thái mới là COMPLETED hoặc FAILED
                if event in ["COMPLETED", "FAILED"]:
                    
                    # Cập nhật trạng thái cuối cùng
                    state[txn_id] = event
                    
                    #  Tăng số transaction kết thúc đúng.
                    completed += 1
                
                # # Nếu trạng thái mới không phải  là COMPLETED hoặc FAILED thì đây là lỗi. Thêm vào danh sách lỗi.
                else:
                    errors.append(f"{txn_id}: event không hợp lệ sau PROCESSING")
                
            #  Trạng thái đã lưu là COMPLETED hoặc FAILED
            # Nếu transaction đã kết thúc mà vẫn có event tiếp theo. Thì đó là lỗi. Thêm vào danh sách lỗi.
            else:
                errors.append(f"{txn_id}: transaction đã kết thúc")
    
    
    # Trả kết quả
    return{
        # Nếu không có lỗi thì valid = True
        "valid": len(errors) == 0,
        
        # số transaction kết thúc hợp lệ
        "completed": completed,
        
        # Danh sách lỗi
        "errors": errors
    }
print()
print("Kết quả bài tập 3")
# Chạy thử hàm đã tạo với dữ liệu đầu bài đã cho

# Chạy thử với events1 
  
# input
events1 = [
    {"txn_id": "T1", "event": "INIT"},
    {"txn_id": "T2", "event": "INIT"},
    {"txn_id": "T2", "event": "PROCESSING"},
    {"txn_id": "T2", "event": "COMPLETED"},
    {"txn_id": "T1", "event": "PROCESSING"},
    {"txn_id": "T1", "event": "FAILED"},
]
# Gọi hàm để chạy với dữ liệu trên và in ra kết quả tương ứng.
print('Kết quả chạy thử hàm với events1')
print(validate_transaction_order(events1))    

# Chạy thử với events2

# input

events2 = [
    {"txn_id": "T3", "event": "INIT"},
    {"txn_id": "T3", "event": "COMPLETED"},
]

# # Gọi hàm để chạy với dữ liệu trên và in ra kết quả tương ứng.
print('Kết quả chạy thử hàm với events2')
print(validate_transaction_order(events2))   


# Bài tập 4:
# Hàng đợi ưu tiên giao hàng [QUEUE]
# Priority Queue (Hàng đợi ưu tiên)
# Shipping service ưu tiên đơn VIP và đơn Express trước đơn thường. 
# Viết class PriorityShippingQueue dùng heapq. Mức ưu tiên: express=1, vip=2, normal=3. Cùng mức thì FIFO. 
# Gợi ý: Sử dụng “python priority queue” (có thể tra chatGPT) 

# Input: 
# psq = PriorityShippingQueue() 
# psq.enqueue({"id": "S1", "type": "normal", "dest": "HN"}) 
# psq.enqueue({"id": "S2", "type": "express", "dest": "HCM"}) 
# psq.enqueue({"id": "S3", "type": "vip", "dest": "DN"}) 
# psq.enqueue({"id": "S4", "type": "express", "dest": "HN"}) 
# print(psq.dequeue()) 
# print(psq.dequeue()) 
# print(psq.dequeue())



# Output:
# {"id": "S2", "type": "express", "dest": "HCM"} 
# {"id": "S4", "type": "express", "dest": "HN"} 
# {"id": "S3", "type": "vip", "dest": "DN"}

import heapq # Import thư viện heapd để tạo hàng đợi ưu tiên (Priority Queue)

class PriorityShippingQueue:
    
    def __init__(self):
        
        # Tạo một lisr rỗng để lưu các đơn hàng
        # heapq sẽ sử dụng list này như một "heap".
        self.queue = []
        
        # Biến đếm dùng để ghi thứ tự đơn hàng được thêm vào.
        # Mục đích là để sử lí FIFO khi hai đơn hàng cùng mức ưu tiên.
        self.counter = 0
        
        # Dictionary quy đổi loại đơn hàng thành mức ưu tiên
        # Số càng nhỏ thì ưu tiên càng cao
        self.priority = {
            "express": 1,
            "vip": 2,
            "normal": 3
        }
    
    def enqueue(self, shipping):
        
        # Lấy loại đơn hàng
        # Ví dụ: "express"
        shipping_type = shipping["type"]
        
        # Tra cứu mức ưu tiên từ dictionary.
        # Ví dụ: express -> 1
        priority = self.priority[shipping_type]
        
        # Thêm dữ liệu vào heap.
        # heapq sẽ sắp xếp theo tuple:
        # (priority, counter. shipping)
        
        #  heapq sẽ so sánh
        # 1. So sánh priority trước
        # 2. Nếu priority bằng nhau thì sẽ so sánh counter
        
        heapq.heappush(
            self.queue,
            (priority, self.counter, shipping)
        )
        
        #  Tăng counter lên 1 để đơn tiếp theo có số thứ tự lớn hơn.
        self.counter += 1
    
    def dequeue(self):
        
        # Nếu hàng đợi đang rỗng
        if len(self.queue) == 0:
            return None
        #
        # Lấy phần tử có ưu tiên cao nhất ra khỏi heap.
        # heappop() trả về:
        # (priority, counter, shipping)
        priority, counter, shipping = heapq.heappop(self.queue)
        return shipping

# Chạy thử hàm với dữ liệu đề bài cho
print()
print("Kết quả bài tập 4")

psq = PriorityShippingQueue()

psq.enqueue({"id": "S1", "type": "normal", "dest": "HN"})
psq.enqueue({"id": "S2", "type": "express", "dest": "HCM"})
psq.enqueue({"id": "S3", "type": "vip", "dest": "DN"})
psq.enqueue({"id": "S4", "type": "express", "dest": "HN"})

print(psq.dequeue())
print(psq.dequeue())
print(psq.dequeue())
print(psq.dequeue())
                
# Bài tập 5:
# Viết chương trình mô phỏng việc phân chia khách hàng vào nhiều quầy thanh toán. 
# Mỗi khách sẽ được đưa vào quầy đang có ít khách nhất. 
# Sau khi phân chia xong, trả về danh sách khách ở từng quầy và tổng số sản phẩm mà mỗi quầy phải xử lý.

# Mô phỏng hàng chờ thanh toán tại quầy [QUEUE] 
# POS system cần mô phỏng hàng chờ tại nhiều quầy thanh toán để tối ưu staffing. 
# Viết hàm simulate_checkout(customers, n_counters): khách xếp vào quầy ít người nhất, trả về thống kê mỗi quầy xử lý bao nhiêu khách. 
# Input: 
# customers = [ 
# {"id": "C1", "items": 5}, 
# {"id": "C2", "items": 12}, 
# {"id": "C3", "items": 3}, 
# {"id": "C4", "items": 8}, 
# {"id": "C5", "items": 1}, 
# ] 
# simulate_checkout(customers, n_counters=2)



# Output: 
# { 
#  "counter_1": {"customers": ["C1","C3","C5"], "total_items": 9},
#  "counter_2": {"customers": ["C2","C4"], "total_items": 20} 
#  }

def simulate_checkout(customers, n_counters):
    
    # Tạo danh sách các quầy thanh toán
    counters = {}
    for i in range(n_counters):
        counter_name = f"counter_{i+1}"
        counters[counter_name] = {
            "customers": [],
            "total_items": 0
        }
    
    # Duyệt từng khách hàng
    for customer in customers:
        
        # Tìm quầy có ít khách nhất
        shortest_counter = min(
            counters,
            key = lambda x: len(counters[x]["customers"])
        )
        
        # Thêm khách vào quầy đó
        counters[shortest_counter]["customers"].append(
            customer["id"]
        )
        
        # Cộng số lượng sản phẩm
        counters[shortest_counter]["total_items"] = (counters[shortest_counter]["total_items"]+ customer["items"])
        
    return counters
# Chạy thử hàm simulate_checkout với dữ liệu đầu bài cho

# Dữ liệu đầu bài cho
customers = [
    {"id": "C1", "items": 5},
    {"id": "C2", "items": 12},
    {"id": "C3", "items": 3},
    {"id": "C4", "items": 8},
    {"id": "C5", "items": 1},
]
# gọi hàm
result = simulate_checkout(customers, 2)
print("Kết quả bài tập 5")
print(result)

 
#  Kết quả bài tập 5
# {'counter_1': {'customers': ['C1', 'C3', 'C5'], 'total_items': 9},
# 'counter_2':{'customers': ['C2', 'C4'], 'total_items': 20}}



# II. Câu hỏi lý thuyết 

# Bài tập 6:
# 6. Graph và Tree khác nhau như thế nào? Khi nào dùng Graph, khi nào dùng Tree? 

# Graph là gì?
# Graph (đồ thị) là tập hợp các:

#             Node (Vertex):  Nút, các điểm, đỉnh. Đại diện cho các thực thể.  Đối tượng lưu trữ thông tin
#             Edge: cạnh, các đường nối giữa các điểm, nút. Đại diện cho mối liên kết giữa các thực thể.
#                   Cạnh có thể có hướng (mũi tên một chiều) hoặc vô hướng (hai chiều).
# => Graph mô tả các đối tượng có mối quan hệ nhiều-nhiều.

# Ứng dụng phổ biến của graph:
# Mạng xã hội (Các tài khoản là nút, mối quan hệ là cạnh).
                #    Ví dụ: Một người có nhiều bạn. Bạn bè cũng có bạn bè khác.
# Bản đồ và mạng lưới giao thông (Các địa điểm là nút, đường đi là cạnh).
        #   Ví dụ: Mỗi thành phố có thể nối với nhiều thành phố. 
                 
# Mạng máy tính hoặc thuật toán tìm đường đi ngắn nhất
# => Dùng Graph khi dữ liệu có quan hệ phức tạp, nhiều chiều.

# Tree là gì?

# Tree (cây) là một loại Graph đặc biệt có:

# Đặc điểm:
#            Có một node gốc (Root)
#            Có quan hệ cha - con
#            Không có vòng lặp (No cycle)
#            Mỗi node con chỉ có một node cha

# Ứng dụng thực tế của tree
# Cấu trúc thư mục: Các thư mục và tệp tin trên hệ điều hành.
    #  ví dụ: Folder trong máy tính:
    #                                 Computer => Documents => report.docx
    #                                 Computer => Documents => note.txt
    #                                 Computer => Images => photo1.jpg
    #                                 Computer => Images => photo2.jpg
# Cây quyết định (Decision Tree): Thuật toán phổ biến trong Trí tuệ Nhân tạo và Machine Learning (thường dùng thư viện scikit-learn).
# HTML/DOM: Các thẻ phần tử lồng nhau trong trình duyệt web.
# => Dùng Tree khi dữ liệu có quan hệ phân cấp (hierarchy).

# Trong Data Structure (cấu trúc dữ liệu):
#                Tree thực chất là một dạng đặc biệt của Graph.

#                Tree = Graph có cấu trúc đặc biệt (không có vòng lặp, có quan hệ cha-con).
#                 Graph = Mạng kết nối tổng quát hơn.
# Điểm khác biệt quan trọng nhất giữa Graph và Tree
# Graph có thể có vòng lặp. Ví dụ: A -> B -> C -> A
# Tree không được phép có vòng lặp. Ví dụ A → B → D
#                                         Không thể quay lại A từ D.

# Tree:
# - Là Graph đặc biệt
# - Có Root
# - Có Parent-Child
# - Không có vòng lặp
# - Dùng cho dữ liệu phân cấp


# Graph:
# - Linh hoạt hơn
# - Có thể có vòng lặp
# - Quan hệ nhiều-nhiều
# - Dùng cho mạng lưới kết nối

# Bài tập 7:
#     Giải thích khái niệm và so sánh DFS và BFS. 
#     Hãy suy nghĩ và đưa ra một ví dụ trong hệ thống thương mại điện tử trường hợp nào dùng DFS, trường hợp nào là BFS? 
    
#     DFS và BFS là hai thuật toán duyệt Graph/Tree
#    Mục đích: Đi qua các node trong một Graph hoặc Tree để tìm kiếm, kiểm tra hoặc xử lý dữ liệu.
#    Hai cách tiếp cận khác nhau:

# # DFS (Depth-First Search): đi chiều sâu trước
# #                          Đi sâu xuống một nhánh cho đến khi không đi được nữa, sau đó quay lại tìm nhánh khác.
# #                          DFS thường dùng:

#                         #    Recursion (đệ quy)
#                         #    hoặc Stack
#                         Ví dụ: 
#                             Bài toán: Tìm tất cả sản phẩm trong category
#                                          Xóa category và toàn bộ sản phẩm con
#                                          Duyệt cấu trúc menu website
# #                                        
                            
                        
# BFS (Breadth-First Search): đi chiều rộng trước
#                            Duyệt từng tầng, xử lý các node gần trước rồi mới đi xa hơn.
#                             BFS dùng: Queue (hàng đợi)
                            # Ví dụ: Tìm sản phẩm liên quan gần nhất
# => Nếu xây dựng hệ thống thương mại điện tử:

# DFS → phù hợp với Category Tree, xử lý toàn bộ danh mục, batch processing
# BFS → phù hợp với Recommendation, tìm sản phẩm gần nhau, tìm quan hệ người dùng - sản phẩm
# DFS phù hợp khi cần khám phá toàn bộ nhánh hoặc xử lý cấu trúc phân cấp như category sản phẩm.
# BFS phù hợp khi cần tìm kiếm theo khoảng cách hoặc ưu tiên các node gần nhất như hệ thống gợi ý sản phẩm trong thương mại điện tử.
# 