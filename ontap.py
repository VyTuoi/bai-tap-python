"""API của các bài được tạo riêng trong file main. File này viết hàm  chỉ xử lý tính toán logic nghiệp vụ"""

"""API chịu trách nhiệm nhận/trả dữ liệu, 
còn Class/Function chịu trách nhiệm xử lý logic nghiệp vụ."""

# Câu 1: Lọc sản phẩm còn hàng [Dễ] (Tạo API) 
# Bối cảnh: 
#     Kho thương mại điện tử chỉ muốn hiển thị những sản phẩm còn bán  được trên trang chủ. 
#     Mỗi sản phẩm có id, name, stock và is_active. 
# Đề bài: Viết hàm filter_available(products) trả về danh sách sản phẩm có stock  lớn hơn 0 và is_active bằng True. 
#                                             Giữ nguyên thứ tự ban đầu của danh sách.

# Mục tiêu:
    #    Lọc danh sách sản phẩm theo 2 điều kiện:
                #  1. stock > 0 ==> Sản phẩm còn hàng.
                #  2. is_active == True ==> Sản phẩm đang được kích hoạt/bán.
    # Không thay đổi thứ tự sản phẩm ban đầu.
    
#  Viết hàm filter_available()
def filter_available(products):
    available_products = []
    for product in products:
        if product ["stock"] > 0 and product["is_active"] == True:
            available_products.append(product)
    return available_products
        
# Dữ liệu mẫu:
products = [
    {"id": 1, "name": "Áo thun", "stock": 10, "is_active": True},
    {"id": 2, "name": "Quần jean", "stock": 0, "is_active": True},
    {"id": 3, "name": "Giày", "stock": 5, "is_active": False},
    {"id": 4, "name": "Nón", "stock": 3, "is_active": True}
]

result = filter_available(products)

print(result)

#  Kết quả:
[
{'id': 1, 'name': 'Áo thun', 'stock': 10, 'is_active': True},
{'id': 4, 'name':'Nón', 'stock': 3, 'is_active': True}
 ]

# Câu 2: Tính tổng tiền giỏ hàng [Dễ] (Tạo API) 
# Bối cảnh: Checkout service cần tính tổng tiền trước khi khách thanh toán. Mỗi  mặt hàng có price và quantity. 
# Đề bài: Viết hàm cart_total(cart) tính tổng tiền bằng price nhân quantity cho từng  item rồi cộng lại.

# Input mẫu: 
# cart = [ 
#  {"name": "Áo", "price": 120000, "quantity": 2}, 
#  {"name": "Quần", "price": 350000, "quantity": 1},  
#  {"name": "Tất", "price": 25000, "quantity": 3} 
# ] 

# cart_total(cart)
# Output mẫu: 665000

# Yêu cầu tách logic tính toán ra thành một hàm cart_total() và API chỉ nhận input → gọi hàm → trả kết quả.


def cart_total(cart):
    total = 0
    for item in cart:
        total += item["price"] * item["quantity"]
    return total
cart = [ 
 {"name": "Áo", "price": 120000, "quantity": 2}, 
 {"name": "Quần", "price": 350000, "quantity": 1},  
 {"name": "Tất", "price": 25000, "quantity": 3},
  {"name": "Mũ", "price": 5000, "quantity": 1},
] 
print(cart_total(cart))

#  Kết quả: 670000

# Tính lần lượt:
# Áo: 120000 × 2 = 240000
# Quần: 350000 × 1 = 350000
# Tất: 25000 × 3 = 75000
# Mũ: 5000 x 1

# Tổng = 240000 + 350000 + 75000  + 5000 = 670000

# Câu 3: Áp dụng giảm giá phần trăm [Dễ] 
# Bối cảnh: Hệ thống bán hàng có thể giảm giá theo phần trăm cho toàn bộ giỏ hàng. 
# Đề bài: Viết hàm apply_discount(total, discount_percent) trả về số tiền sau giảm  giá. Nếu discount_percent bằng 0 thì giữ nguyên total. 
# Input mẫu: apply_discount(total=500000, discount_percent=10)
# Output mẫu: 450000

def apply_discount(total, discount_percent):
    if discount_percent == 0: # Nếu discount_percent bằng 0 thì giữ nguyên total.
        return total
    discount_amount = total * discount_percent/100 #Bước 1: Tính số tiền được giảm
    final_total = total - discount_amount  #       Bước 2: Trừ tiền giảm
    return final_total

# Test với dữ liệu mẫu:
total=500000
discount_percent=10
result = apply_discount(total, discount_percent)
print(result)
 
#  Kết quả: 450000.0

# Trường hợp muốn kết quả là số nguyên:
def apply_discount(total, discount_percent):
    if discount_percent == 0:
        return total

    discount_amount = total * discount_percent / 100
    final_total = total - discount_amount

    return int(final_total) # Kết quả cuối cùng là số nguyên

total=500000
discount_percent=10
result = apply_discount(total, discount_percent)
print(result)
# Kết quả: 450000

# Câu 4: Kiểm tra trạng thái đơn hàng [Dễ] (Tạo API) 
# Bối cảnh: Trang quản trị cần hiển thị thông báo dễ hiểu theo trạng thái đơn hàng.
# Đề bài: Viết hàm order_message(status) nhận status và trả về thông báo:  
# - pending là Chờ xử lý
# - confirmed là Đã xác nhận 
# - shipping là Đang giao 
# - completed là Hoàn thành 
# - cancelled là Đã hủy. 
# - Trạng thái khác trả về Không hợp lệ.
def order_message(status):
    if status == "pending":
        return "Chờ xử lý"
    elif status == "shipping":
        return "Đang giao "
    elif status == "confirmed":
        return "Đã xác nhận"
    elif status == "completed":
        return "Hoàn thành"
    elif status == "cancelled":
        return "Đã hủy"
    else:
        return "Không hợp lệ"
# Test với input mẫu:
print(order_message("shipping"))
# Kết quả: Đang giao
# Test với các input khác:
print(order_message("pending"))
print(order_message("confirmed"))
print(order_message("shipping"))
print(order_message("completed"))
print(order_message("cancelled"))
print(order_message("abc"))

# Kết quả:
# Đã xác nhận
# Đang giao
# Hoàn thành
# Đã hủy
# Không hợp lệ

# Câu 5: Tính phí vận chuyển theo khoảng cách [Dễ] 
# Bối cảnh: Shipping service tính phí dựa trên khoảng cách giao hàng. 
# Đề bài: Viết hàm shipping_fee(distance_km). 
# - Nếu distance_km <= 5 phí 15000, 
# - Nếu distance_km <= 10 phí 25000 
# - Còn lại phí 40000. 
# Input mẫu: shipping_fee(8)
# Output mẫu: 25000

def shipping_fee(distance_km):
    if distance_km <= 5:
        return 15000
    elif  5 < distance_km <= 10:
        return 25000
    else:
        return 40000
# Test với các giá trị:
print(shipping_fee(1))
print(shipping_fee(5))
print(shipping_fee(6))
print(shipping_fee(10))
print(shipping_fee(8))
print(shipping_fee(15))

# Kết quả:
# 15000
# 15000
# 25000
# 25000
# 25000
# 40000



# Câu 6: Kiểm tra đăng nhập đơn giản [Dễ] 
# Bối cảnh: Auth service cần kiểm tra thông tin đăng nhập của người dùng với dữ liệu lưu sẵn. 
# Đề bài: Viết hàm login(username, password).  
# Trả về True nếu username là admin và password là 123456, ngược lại trả về False.
# Input mẫu: login("admin", "123456")
# Output mẫu: True

def login(username, password):
    if username == "admin" and password == "123456":
        return True
    else:
        return False
# Test với input mẫu:
print(login("admin", "123456"))
# Kết quả: True

# Test với trường hợp khác:
print(login("user1", "123456"))
# Kết quả: False

# Test với trường hợp khác:
print(login("admin", "123406"))
# Kết quả: False


# Câu 7: Đếm số đơn theo trạng thái [Dễ] 
# Bối cảnh: Dashboard cần biết trong ngày có bao nhiêu đơn hàng ở từng trạng  thái. 
# Đề bài: Viết hàm count_status(statuses) nhận list trạng thái 
# và trả về dict đếm số lần xuất hiện của từng trạng thái. 
# Input mẫu: statuses = ["pending", "confirmed", "pending", "shipping",  "confirmed"] 
#            count_status(statuses)
# Output mẫu: {"pending": 2, "confirmed": 2, "shipping": 1}


# Hàm đếm số đơn hàng theo từng trạng thái
def count_status(statuses):
    result = {} #tạo dictionary rỗng để lưu kết quả.
    
    for status in statuses: #Duyệt từng status trong danh sách statuses
        if status in result: #Nếu trạng thái đã tồn tại trong result → tăng số lượng lên 1.
            result[status] += 1
        else:  # Nếu chưa có trạng thái trong result → thêm trạng thái vào dictionary với giá trị ban đầu là 1.
            result[status] = 1
    return result # trả về kết quả
# Dữ liệu mẫu:
statuses = ["pending", "confirmed", "pending", "shipping",  "confirmed"]

# Gọi hàm:
print(count_status(statuses))

# Kết quả:
# {'pending': 2, 'confirmed': 2, 'shipping': 1}

# Câu 8: Tìm sản phẩm theo id [Dễ] 

# Bối cảnh: API chi tiết sản phẩm cần tìm một sản phẩm theo id trong danh sách. 

# Đề bài: 
#     Viết hàm find_product(products, product_id).
#     Nếu tìm thấy thì trả về dict  sản phẩm, nếu không có thì trả về None.

# Input mẫu:
    
# products = [ 
#  {"id": "SP01", "name": "Áo"}, 
#  {"id": "SP02", "name": "Quần"} 
# ] 
# find_product(products, "SP02")

# Output mẫu:
# {"id": "SP02", "name": "Quần"}

def find_product(products, product_id):
    for product in products: #duyệt từng sản phẩm trong danh sách.
        if product["id"] == product_id: # kiểm tra ID của sản phẩm có trùng với ID cần tìm không
            return product # nếu tìm thấy, trả về ngay dict sản phẩm đó.
    return None # sau khi duyệt hết danh sách mà không tìm thấy sản phẩm nào phù hợp
# Input mẫu:
products = [ {"id": "SP01", "name": "Áo"}, {"id": "SP02", "name": "Quần"} ] 
# Gọi hàm:
print(find_product(products, "SP02"))
# Kết quả: {'id': 'SP02', 'name': 'Quần'}

print(find_product(products, "SP01"))
# Kết quả: {'id': 'SP01', 'name': 'Áo'}

print(find_product(products, "SP03"))
# Kết quả: None <== sau khi duyệt hết danh sách nhưng  không tìm thấy sản phẩm có id là SP03

# Câu 9: Lọc đơn hàng có giá trị cao [Dễ] 

# Bối cảnh: 
#     Bộ phận kinh doanh muốn xem các đơn hàng có tổng tiền lớn hơn một  ngưỡng nhất định. 
# Đề bài: 
#     Viết hàm high_value_orders(orders, min_total) trả về danh sách đơn hàng  có total >= min_total. 
# Input mẫu 
# orders = [ 
#  {"id": 1, "total": 120000}, 
#  {"id": 2, "total": 800000}, 
#  {"id": 3, "total": 450000} 
# ] 

# high_value_orders(orders, 400000)

# Output mẫu:
    
# [{"id": 2, "total": 800000}, {"id": 3, "total": 450000}] # Vì 800000 và 450000 > 400000

def high_value_orders(orders, min_total):
    result  = [] # Tạo một list rỗng để chứa các đơn hàng có giá trị cao hơn min_total
    for order in orders: #Duyệt từng đơn hàng:
        if order["total"] >= min_total:
            result.append(order) # Khi điều kiện đúng:thêm đơn hàng vào result
    return result # Cuối cùng: trả về danh sách các đơn hàng có total >= min_total. 
# Input mẫu 
orders = [ 
 {"id": 1, "total": 120000}, 
 {"id": 2, "total": 800000}, 
 {"id": 3, "total": 450000} 
] 
# Gọi hàm:
print(high_value_orders(orders, 400000)) #Với min_total = 400000 
# Kết quả: [{'id': 2, 'total': 800000}, {'id': 3, 'total': 450000}]

print(high_value_orders(orders, 500000))  #Với min_total = 500000 
# Kết quả: [{'id': 2, 'total': 800000}]

print(high_value_orders(orders,1000000)) #  #Với min_total = 1000000 
# Kết quả: []

# Câu 10:
#     Kiểm tra số dư trước khi thanh toán [Dễ] 
# Bối cảnh: 
#     Payment service cần đảm bảo khách có đủ số dư trước khi thanh toán. 
# Đề bài: 
#     Viết hàm can_pay(balance, order_total) trả về True nếu balance >=  order_total, ngược lại False. 
# Input mẫu: can_pay(balance=500000, order_total=350000)
# Output mẫu: True


def can_pay(balance, order_total): # Hàm can_pay nhận vào 2 tham số: Số sư tài khoản của khách và Tổng tiền đơn hàng
    # Kiểm tra số dư có đủ thanh toán hay không.
    if balance >= order_total:
        # Nếu số dư lớn hơn hoặc bằng tổng tiền đơn hàng.
        return True
    else:
        # Nếu số dư nhỏ hơn tổng tiền đơn hàng
        return False
# Chạy thử
print(can_pay(balance=500000, order_total=350000))
# Kết quả: True

print(can_pay(balance=40000, order_total=350000))
# Kết quả: False

# Cách viết rút gọn
def can_pay(balance, order_total):
    return balance >= order_total 
                       #return có nhiệm vụ trả kết quả về nơi gọi hàm. 
                       # Bản chất của balance >= order_total đã tự tạo ra một giá trị Boolean:
                    #    Trả về kết quả kiểm tra xem số dư có lớn hơn hoặc bằng tổng tiền đơn hàng hay không.

print(can_pay(balance=500000, order_total=350000))
# Kết quả: True

print(can_pay(balance=40000, order_total=350000))
# Kết quả: False

# Câu 11: Cập nhật tồn kho sau khi bán [Dễ] 
# Bối cảnh: 
#     Sau khi đơn hàng thanh toán thành công, hệ thống cần trừ số lượng  tồn kho. 
# Đề bài: 
#     Viết hàm update_stock(stock, sold_quantity). 
#     Nếu stock đủ thì trả về tồn  kho mới. 
#     Nếu sold_quantity lớn hơn stock thì trả về "Không đủ hàng".
# Input mẫu: update_stock(stock=10, sold_quantity=3)
# Output mẫu: 7

def update_stock(stock, sold_quantity): # Hàm nhận 2 tham số:
                                         #stock: số lượng hàng hiện có trong kho.
                                        # sold_quantity: số lượng hàng khách đã mua.
    if stock >= sold_quantity:
        return stock - sold_quantity
    else:  #Nếu số lượng bán lớn hơn số lượng tồn kho → không đủ hàng.
        return "Không đủ hàng"
# Gọi hàm - chạy thử
print(update_stock(stock=10, sold_quantity=3))
# Kết quả: 7
print(update_stock(stock=3, sold_quantity=3))
# Kết quả: 0
print(update_stock(stock=3, sold_quantity=10))
# Kết quả: Không đủ hàng

# Cách 2:
def update_stock(stock, sold_quantity):
    if sold_quantity > stock:
        return "KHông đủ hàng"
    else:
        return stock - sold_quantity

# Gọi hàm - chạy thử
print(update_stock(stock=10, sold_quantity=3))
# Kết quả: 7
print(update_stock(stock=3, sold_quantity=3))
# Kết quả: 0
print(update_stock(stock=3, sold_quantity=10))
# Kết quả: Không đủ hàng

# Câu 12: Tính điểm tích lũy khách hàng [Dễ] 
# Bối cảnh: 
#     CRM service cộng điểm cho khách sau mỗi lần mua hàng. Cứ 10000  VND được 1 điểm. 
# Đề bài: 
#     Viết hàm loyalty_points(order_total) trả về số điểm tích lũy, lấy phần  nguyên. 
# Input mẫu: loyalty_points(235000)
# Output mẫu: 23

def loyalty_points(order_total): #
    points = order_total // 10000 # 
                         # 1. Tính số lần 10.000 VND có trong tổng tiền = order_total // 10000 = số điêmr tích lũy tương ứng với đơn hàng đã mua.
                        #  // là phép chia lấy phần nguyên.
                        #  
    return points
# Gọi hàm
print(loyalty_points(10000)) # Điểm tích lũy là 1
print(loyalty_points(25000)) # Điểm tích lũy là 2. Còn dư 5000, nhưng phần dư không được tính điểm.
print(loyalty_points(9000)) # # Điểm tích lũy là 0. 

# Câu 13: 
#     Phân loại khách hàng theo tổng chi tiêu [Dễ] (Tạo API) 
# Bối cảnh: 
#     Marketing service phân loại khách hàng để gửi ưu đãi. 
# Đề bài: 
#     Viết hàm classify_customer(total_spent). Nếu dưới 1 triệu là normal, từ 1  triệu đến dưới 5 triệu là silver, từ 5 triệu trở lên là gold. 
# Input mẫu: classify_customer(5200000)
# Output mẫu: "gold"
def classify_customer(total_spent):
    if total_spent < 1000000:
        return "normal" # Nếu total_spent dưới 1.000.000 → "normal"
    elif 1000000 <= total_spent < 5000000:
        return "silver" # Nếu total_spent từ 1.000.000 đến dưới 5.000.000 → "silver"
    else:
        return "gold" # Nếu total_spent từ 5.000.000 trở lên → "gold"

#  Gọi hàm:
print(classify_customer(5200000))
# kết quả: gold

print(classify_customer(200000))
# kết quả: normal

print(classify_customer(5000000))
# kết quả: gold

print(classify_customer(4900000))
# kết quả: silver

# Câu 14: 
#     Kiểm tra email hợp lệ cơ bản [Dễ] 
# Bối cảnh: 
#     Form đăng ký cần kiểm tra email trước khi gửi lên server. 
# Đề bài: 
#     Viết hàm is_valid_email(email) trả về True nếu email có chứa ký tự @ và  kết thúc bằng .com, ngược lại False.

# Input mẫu: is_valid_email("user@gmail.com")
# Output mẫu:True


def is_valid_email(email):
    #   Kiểm tra email có chứa kí tự @ hay không
    if "@" not in email:
        return False
    # Kiểm tra email có kết thúc bằng .com hay không?
    if not email.endswith(".com"): # endswith() có nghĩa là kiểm tra chuỗi có kết thúc bằng một đoạn nào đó hay không.
        return False
    return True
# Gọi hàm
print(is_valid_email("user@gmail.com"))
# Kết quả: True

print(is_valid_email("usergmail.com"))
# Kết quả: False

print(is_valid_email("user@gmail"))
# Kết quả: False

print(is_valid_email("usergmail"))
# Kết quả: False

# Câu 15: 
#     Lọc người dùng đang hoạt động [Dễ] (Tạo API) 
# Bối cảnh: 
#     Admin panel chỉ hiển thị các tài khoản đang hoạt động. 
# Đề bài: 
#     Viết hàm active_users(users) trả về danh sách user có is_active bằng  True. 
# Input mẫu :
# users = [ 
#  {"id": 1, "name": "An", "is_active": True}, 
#  {"id": 2, "name": "Bình", "is_active": False} 
# ] 

# active_users(users)

# Output mẫu: [{"id": 1, "name": "An", "is_active": True}]

def active_users(users): # users: dữ liệu đầu vào, là một list chứa nhiều user.
    result = []    # Tạo một danh sách rỗng để chứa những user đang hoạt động.
    for user in users: # Duyệt từng user trong danh sách users.


        if user["is_active"] == True: #  Kiểm tra giá trị is_active của user đang xét.
                                      #"is_active": True ==> thì user đang hoạt động → thêm vào result.
         result.append(user) # append() dùng để thêm user vào cuối danh sách result.
    return result  # Trả về danh sách những user đang hoạt động.
users = [ 
 {"id": 1, "name": "An", "is_active": True}, 
 {"id": 2, "name": "Bình", "is_active": False} 
]
print(active_users(users))
#  Kết quả: [{'id': 1, 'name': 'An', 'is_active': True}]

# Câu 16: 
#     Tìm đơn hàng mới nhất [Dễ] (Tạo API) 
# Bối cảnh: 
#     Hệ thống cần lấy đơn hàng mới nhất dựa trên id tăng dần. 
# Đề bài: 
#     Viết hàm latest_order(orders) trả về đơn hàng có id lớn nhất.
#     Nếu danh  sách rỗng thì trả về None. 
# Input mẫu: orders = [{"id": 101}, {"id": 105}, {"id": 103}] 
#            latest_order(orders)
# Output mẫu: {"id": 105}

# Cách 1:

def latest_order(orders): # tìm phần tử có id lớn nhất trong danh sách order = đơn hàng mới nhất
    if len(orders) == 0: # Kiểm tra thêm danh sách orders có rỗng không?
        return None  # Danh sách orders rỗng: Trả về None
    latest = orders[0]  # Nếu danh sách order không rỗng => lastet = đơn hàng đầu tiên
    
    for order in orders: # Duyệt từng order trong danh sách order 
        if order["id"] > latest["id"]: # order["id"] có lớn hơn   latest["id"] không?
            latest = order # order["id"] > latest["id"] thì cập nhật lại latest và tiếp tục duyệt, cập nhật cho hết list.
    return latest # Trả về latest
orders = [{"id": 101}, {"id": 105}, {"id": 103}]
print(latest_order(orders))
# Kết quả: {'id': 105}
# Với input mẫu:  orders = [{"id": 101}, {"id": 105}, {"id": 103}]
#                 latest ban đầu sẽ là 101
#                105 > 101 ==> Đúng  ===> cập nhật latest ==>  latest = 105
#                103 > 105 ==> Sai ==> latest vẫn là 105


# Cách 2:
def latest_order(orders):
    if not orders:
        return None
    return max(orders, key=lambda order: order["id"]) # trả về id lớn nhất trong danh 
#  max() tìm phần tử lớn nhất.
# Nhưng orders chứa dict, nên cần nói cho Python biết phải so sánh theo trường nào.
#  key=lambda order: order["id"] => Với mỗi order, lấy order["id"] ra để so sánh.

# Chạy thử
orders = [{"id": 101}, {"id": 105}, {"id": 106}]
print(latest_order(orders))
# Kết quả: {'id': 106}

# Câu 17: 
#     Tính tổng doanh thu trong ngày [Dễ] (Tạo API) 
# Bối cảnh: 
#     Báo cáo cuối ngày cần cộng tổng tiền của tất cả giao dịch thành công.
# Đề bài: 
#     Viết hàm daily_revenue(transactions) chỉ cộng amount của giao dịch có  status là success. 

# Input mẫu:
     
# transactions = [ 
#  {"amount": 100000, "status": "success"}, 
#  {"amount": 50000, "status": "failed"}, 
#  {"amount": 200000, "status": "success"} 
# ] 

# daily_revenue(transactions)

# Output mẫu: 300000
"""chỉ cộng amount của các giao dịch có status là "success"""
def daily_revenue(transactions):
    total = 0 # Biến total dùng để lưu tổng doanh thu 
    for transaction in transactions: # Duyệt từng giao dịch
        
       if transaction["status"] == "success": # Chỉ khi giao dịch có trạng thái "success" thì mới cộng tiền.
           total = total + transaction["amount"]
    return total
# Chạy thử
transactions = [ 
 {"amount": 100000, "status": "success"}, 
 {"amount": 50000, "status": "failed"}, 
 {"amount": 200000, "status": "success"} 
] 
print(daily_revenue(transactions))
# Kết quả: 300000

transactions = [ 
 {"amount": 100000, "status": "success"}, 
 {"amount": 50000, "status": "failed"}, 
 {"amount": 10000, "status": "success"},
 {"amount": 200000, "status": "success"} 
] 
print(daily_revenue(transactions))
# Kết quả: 310000


# Câu 18: 
#     Ẩn mật khẩu trong danh sách user [Dễ] 
# Bối cảnh: 
#     API trả về thông tin user không được để lộ password. 
# Đề bài: 
#     Viết hàm hide_password(users) trả về danh sách user mới, trong đó mỗi  user không còn key password. 
# Input mẫu: users = [{"id": 1, "username": "admin", "password": "123"}] 
#            hide_password(users)
# Output mẫu: [{"id": 1, "username": "admin"}]

"""mục tiêu là xóa key password khỏi mỗi user trước khi trả dữ liệu về API
    """
def hide_password(users):
    result = [] # result dùng để chứa các user đã được ẩn password.
    for user in users: # Duyệt từng user
        new_user = {} # Tạo một dictionary mới => không sửa trực tiếp user mà tạo một user mới.
        
        for key in user: # Duyệt từng key, các key lần lượt là: id, username, password
            if key != "password": # Chỉ lấy key khác "password" ==> Nếu key không phải password thì giữ lại.
                new_user[key] = user[key] # Thêm key và value thỏa mãn điều kiện trên  vào user mới
        result.append(new_user) # Thêm user mới vào danh sách kết quả
    return result # Trả về kết quả

users = [{"id": 1, "username": "admin", "password": "123"}]
print(hide_password(users))
# Kết quả: [{'id': 1, 'username': 'admin'}]

users = [{"id": 1, "username": "admin", "password": "123"}, {"id": 2, "username": "user thường", "password": "103"}]
print(hide_password(users))
# Kết quả: [{'id': 1, 'username': 'admin'}, {'id': 2, 'username': 'user thường'}]

# Câu 19: 
#     Tạo mã đơn hàng đơn giản [Dễ] (Tạo API) 
# Bối cảnh: 
#     Hệ thống cần tạo mã đơn hàng từ id số nguyên. 
# Đề bài:
#     Viết hàm order_code(order_id) trả về chuỗi có dạng ORD-<id>, 
#     trong đó  id được thêm số 0 phía trước để đủ 5 chữ số.
# Input mẫu: "order_code(27)
# Output mẫu: "ORD-00027"


def order_code(order_id):
    return "ORD-" + str(order_id).zfill(5)

    """
       order_id: tham số đầu vào, nhận mã ID dạng số nguyên.
    
       str(order_id): Chuyển order_id từ số nguyên sang chuỗi.
       zfill(5) thêm số 0 ở phía trước để chuỗi có đủ 5 ký tự.
       Ví dụ:
       "27".zfill(5)     # "00027"
       "123".zfill(5)    # "00123"
       "99999".zfill(5)  # "99999"
    """
# Chạy thử hàm 
print(order_code(27))
print(order_code(7))
print(order_code(123))
print(order_code(1234))
print(order_code(12345))

# Kết quả
"""
ORD-00027
ORD-00007
ORD-00123
ORD-01234
ORD-12345

    """
    
# Câu 20: 
#     Kiểm tra quyền admin [Dễ] 
# Bối cảnh:
#     Một chức năng chỉ cho phép tài khoản admin truy cập. 
# Đề bài: 
#     Viết hàm is_admin(user) 
#     trả về True nếu role của user là admin,
#     ngược lại  False.
# Input mẫu: user = {"id": 1, "name": "An", "role": "admin"} 
#            is_admin(user)
# Output mẫu: True

def is_admin(user):
    if user["role"] == "admin": # Nếu role là "admin" thì điều kiện đúng → Trả về True
        return True
    else: #Nếu role không phải "admin" thì trả về False.
        return False
user = {"id": 1, "name": "An", "role": "admin"}     
print(is_admin(user))
# Kết quả: True

user = {"id": 2, "name": "An", "role": "user thường"}     
print(is_admin(user))
# Kết quả: False

# Câu 21: 
#     Tính thuế VAT [Dễ] 
# Bối cảnh: 
#     Invoice service cần tính VAT cho hóa đơn. 
# Đề bài: 
#     Viết hàm add_vat(price, vat_percent) trả về giá sau VAT.
#     Ví dụ VAT 10%  thì giá sau VAT = price * 1.1. 
# Input mẫu: add_vat(200000, 10)
# Output mẫu: 220000

def add_vat(price, vat_percent):
    vat = price * vat_percent/100
    total = price + vat
    return int(total) #int() = lấy số nguyên. Lưu ý: int() không làm tròn, mà bỏ phần thập phân.
# Chạy thử:
print(add_vat(200000, 10))
# Kết quả: 220000

# Câu 22: 
#     Tìm sản phẩm rẻ nhất [Dễ] (Tạo API) 
# Bối cảnh: 
#     Trang gợi ý muốn hiển thị sản phẩm có giá thấp nhất trong một danh  sách. 
# Đề bài: 
#     Viết hàm cheapest_product(products) trả về sản phẩm có price nhỏ nhất.  
#     Nếu danh sách rỗng trả về None. 
# Input mẫu: 

"""products = [ 
 {"name": "Áo", "price": 120000}, 
 {"name": "Tất", "price": 25000} 
] 
cheapest_product(products)
    """

# Output mẫu: {"name": "Tất", "price": 25000}

# Cách 1:
"""Lấy sản phẩm đầu tiên làm sản phẩm rẻ nhất
Duyệt từng sản phẩm => Nếu sản phẩm hiện tại rẻ hơn => Cập nhật cheapest  => Trả về cheapest
    """
def cheapest_product(products):
    if len(products) == 0: # là đếm số phần tử trong danh sách => Nếu số lượng sản phẩm bằng 0 → trả về None.
        return None
    cheapest = products[0]
        
    for product in products:
        if product["price"] < cheapest["price"]:
            cheapest = product
    return cheapest

# Chạy thử:
products = [ 
 {"name": "Áo", "price": 120000}, 
 {"name": "Mũ", "price": 100000},
 {"name": "Quần", "price": 250000} 
]
print(cheapest_product(products))

"""kết quả:
    {'name': 'Mũ', 'price': 100000}


    """
products = [ ]
print(cheapest_product(products))

"""kết quả:
   None


    """


# Cách 2:
def cheapest_product(products):
    if not products: # if not products:  kiểm tra danh sách rỗng => Nếu rỗng ==> Trả về None
        return None
    else:
        
      return min(products, key=lambda product: product["price"])
"""
cần kiểm tra  products trước vì min() không thể tìm giá trị nhỏ nhất trong một danh sách rỗng.
min() → tìm giá trị nhỏ nhất.
products → danh sách sản phẩm.
key= → nói cho Python biết dựa vào tiêu chí nào để tìm nhỏ nhất.
lambda product: product["price"] → lấy price của từng sản phẩm để so sánh.
"""

# Chạy thử với dữ liệu mẫu:
products = [ 
 {"name": "Áo", "price": 120000}, 
 {"name": "Tất", "price": 25000} 
]
print(cheapest_product(products))

"""kết quả:
    {'name': 'Tất', 'price': 25000}

    """

"""
Câu 23: 
        Tính số lượng sản phẩm trong giỏ [Dễ] 
Bối cảnh: 
       Icon giỏ hàng cần hiển thị tổng số lượng sản phẩm khách đã chọn.
       Đề bài: Viết hàm cart_quantity(cart) cộng quantity của tất cả item trong giỏ.
Input mẫu: 
cart = [{"name": "Áo", "quantity": 2}, {"name": "Quần",  "quantity": 1}] 
cart_quantity(cart)

Output mẫu: 3


"""
def cart_quantity(cart):
    total = 0
    for item in cart:
        total = total + item["quantity"]
    return total

cart = [{"name": "Áo", "quantity": 2}, {"name": "Quần",  "quantity": 1}] 
print(cart_quantity(cart))
# Kết quả: 3

cart = [{"name": "Áo", "quantity": 2}, {"name": "Quần",  "quantity": 1}, {"name": "Quần",  "quantity": 1}] 
print(cart_quantity(cart))
# Kết quả : 4


"""
Câu 24: 
       Kiểm tra mã giảm giá có tồn tại [Dễ] (Tạo API) 
Bối cảnh: 
Checkout service cần kiểm tra mã người dùng nhập có nằm trong  danh sách mã hợp lệ không. 
Đề bài: 
Viết hàm coupon_exists(code, coupons) 
trả về True nếu code có trong  coupons, ngược lại False. 
Input mẫu:

coupons = ["SALE10", "VIP20", "FREESHIP"] 

coupon_exists("VIP20", coupons)

Output mẫu: True


    """
def coupon_exists(code, coupons):
    if code in coupons:
        return True
    else:
        return False
# Chạy thử:

coupons = ["SALE10", "VIP20", "FREESHIP"]
print(coupon_exists("VIP20", coupons))
# Kết quả: True

coupons = ["SALE10", "VIP20", "FREESHIP"]
print(coupon_exists("VIP30", coupons))
# Kết quả: False


"""
Câu 25:  
          Lọc sản phẩm theo danh mục [Dễ] (Tạo API) 
Bối cảnh:
      API /products cho phép người dùng lọc sản phẩm theo category. 
Đề bài: 
      Viết hàm filter_by_category(products, category) 
      trả về các sản phẩm có  category trùng với tham số truyền vào. 
Input mẫu: 

products = [ 
 {"name": "Áo thun", "category": "ao"}, 
 {"name": "Quần jean", "category": "quan"} 
] 

filter_by_category(products, "ao")

Output mẫu: [{"name": "Áo thun", "category": "ao"}]


    """
def filter_by_category(products, category):
    result = []
    for product in products:
        if product["category"] == category:
            result.append(product)
    return result

# Chạy thử:

products = [ 
 {"name": "Áo thun", "category": "ao"}, 
 {"name": "Quần jean", "category": "quan"} 
] 

print(filter_by_category(products, "ao"))
# Kết quả: [{'name': 'Áo thun', 'category': 'ao'}]

products = [ 
 {"name": "Áo thun", "category": "ao"}, 
 {"name": "Quần jean", "category": "quan"},
 {"name": "Quần đùi", "category": "quan"}
] 

print(filter_by_category(products, "quan"))
# Kết quả: [{'name': 'Quần jean', 'category': 'quan'}, {'name': 'Quần đùi', 'category': 'quan'}]

"""
Câu 26: 
           Kiểm tra giới hạn số lần đăng nhập sai [Dễ] 
Bối cảnh: 
             Auth service khóa tài khoản nếu đăng nhập sai quá nhiều lần.
Đề bài: 
             Viết hàm is_locked(failed_attempts). 
             
             Nếu failed_attempts >= 5 trả về True, ngược lại False. 
Input mẫu: is_locked(5)
Outputmẫu: True


    """
def is_locked(failed_attempts):
    
    if failed_attempts >= 5:
        return True
    else:
        return False
# Chạy thử:
print(is_locked(5))
# Kết quả: True

print(is_locked(3))
# Kết quả: False

print(is_locked(6))
# Kết quả: True

# Hoặc:
def is_locked(failed_attempts):
    return failed_attempts >= 5
"""
kiểm tra số lần đăng nhập sai có từ 5 lần trở lên hay không?
>= nghĩa là lớn hơn hoặc bằng
Nếu failed_attempts là 5 hoặc lớn hơn → trả về True
Nếu nhỏ hơn 5 → trả về False
"""
# Chạy thử:
print(is_locked(6))
# Kết quả: True

print(is_locked(2))
# Kết quả: False

print(is_locked(5))
# Kết quả: True

"""


Câu 27:  
        Chuẩn hóa tên người dùng [Dễ] (Tạo API) 
Bối cảnh: 
       Dữ liệu nhập từ form có thể thừa khoảng trắng và viết hoa không đồng  nhất. 
Đề bài: 
    Viết hàm normalize_name(name) xóa khoảng trắng đầu cuối và chuyển  mỗi từ sang dạng viết hoa chữ cái đầu. 
Input mẫu: 
         normalize_name(" nguyen van an ")
Output mẫu: "Nguyen Van An"


    """
def normalize_name(name):
    name = name.strip()
    name = name.title()
    return name
"""
Xóa khoảng trắng ở đầu và cuối tên → dùng .strip()
Viết hoa chữ cái đầu của mỗi từ → dùng .title()
    """
# Chạy thử
print(normalize_name(" nguyen van an "))
# Kết quả: Nguyen Van An

print(normalize_name("   nguyen Van an   "))
# Kết quả: Nguyen Van An

# Hoặc: 
def normalize_name(name):
    return name.strip().title()
"""
Xóa khoảng trắng đầu/cuối → viết hoa chữ cái đầu mỗi từ → trả về kết quả
    """
result = normalize_name("   dang minh anh    ")
print(result)
# Kết quả: Dang Minh Anh

"""
Câu 28: 
     Tính lương theo số giờ làm [Dễ] 
Bối cảnh: 
       HR service tính lương nhân viên theo giờ. 
Đề bài: 
       Viết hàm calculate_salary(hours, rate). 
       Nếu hours <= 40 thì lương = hours  * rate. 
       Nếu lớn hơn 40 thì số giờ vượt được tính 1.5 lần rate. 
Input mẫu 
       calculate_salary(hours=45, rate=50000)
Output mẫu: 2375000

    """
def calculate_salary(hours, rate):
    result = 0
    if hours <= 40:
        result = hours * rate
    else:
        result = 40 * rate + (hours - 40) * 1.5 * rate
    return int(result)
print(calculate_salary(hours=45, rate=50000))
# Kết quả: 2375000

print(calculate_salary(hours=40, rate=50000))
# Kết quả:2000000

# Hoặc:
def calculate_salary(hours, rate):
    if hours <= 40:
        return hours * rate
    else:
        overtime_hours = hours - 40
        normal_salary = 40 * rate
        overtime_salary = overtime_hours * rate * 1.5

        return int(normal_salary + overtime_salary)

print(calculate_salary(hours=45, rate=50000))
# Kết quả: 2375000

print(calculate_salary(hours=40, rate=50000))
# Kết quả:2000000

"""
Câu 29: 
      Đếm số ticket ưu tiên cao [Dễ] 
Bối cảnh: 
        Support dashboard cần biết có bao nhiêu ticket cần xử lý gấp.
 
Đề bài: 
     Viết hàm count_urgent(tickets) đếm ticket có priority là urgent. 
Input mẫu: 

tickets = [ 
 {"id": 1, "priority": "normal"}, 
 {"id": 2, "priority": "urgent"}, 
 {"id": 3, "priority": "urgent"} 
] 

count_urgent(tickets)
Output mẫu: 2


    """
def count_urgent(tickets):
    count = 0
    for ticket in tickets:
        if ticket["priority"] == "urgent":
            count  = count  + 1 # có thể viết ngắn gọn thành count += 1
    return count

tickets = [ 
 {"id": 1, "priority": "normal"}, 
 {"id": 2, "priority": "urgent"}, 
 {"id": 3, "priority": "urgent"} 
] 

print(count_urgent(tickets))

# Kết quả: 2
"""

Câu 30: 
          Tính phần trăm hoàn thành công việc [Dễ] 
Bối cảnh: 
         Project service cần hiển thị tiến độ task. 
Đề bài: 
         Viết hàm progress_percent(done_tasks, total_tasks). 
         Nếu total_tasks  bằng 0 thì trả về 0, ngược lại trả về phần trăm hoàn thành. 
Input mẫu: 
           progress_percent(3, 10)
Output mẫu: 30.0


    """
def progress_percent(done_tasks, total_tasks):
    if total_tasks == 0:
        return 0
    else:
        return (done_tasks/total_tasks) * 100
print(progress_percent(3, 10))
# Kết quả: 30.0

print(progress_percent(3, 0))
# Kết quả: 0

print(progress_percent(5, 10))
# Kết quả: 50.0


# Hoặc:
def progress_percent(done_tasks, total_tasks):
    if total_tasks == 0:
        return 0

    return done_tasks / total_tasks * 100
    """
Câu 31: 
    Tìm khách hàng theo số điện thoại [Dễ] (Tạo API) 
Bối cảnh: 
    CRM cần tra cứu khách hàng bằng phone. 
Đề bài: 
    Viết hàm find_customer(customers, phone) 
    trả về khách hàng có phone  trùng khớp. 
    Nếu không có trả về None.
    
Input mẫu:
    
customers = [ 
 {"name": "An", "phone": "0901"}, 
 {"name": "Bình", "phone": "0902"} 
] 
find_customer(customers, "0902")

Output mẫu: 
    
{"name": "Bình", "phone": "0902"}
    """

def find_customer(customers, phone):

    for customer in customers:
        if customer["phone"] == phone:
            return customer
    return None

    """
for customer in customers:        → Duyệt lần lượt từng khách hàng trong danh sách.
customer["phone"] == phone        → So sánh số điện thoại của khách hàng với số điện thoại cần tìm.
return customer                   → Nếu trùng khớp, trả về toàn bộ thông tin khách hàng đó.
return None                       → Sau khi duyệt hết danh sách mà không tìm thấy thì trả về None.
    """
# Chạy thử:
customers = [ 
 {"name": "An", "phone": "0901"}, 
 {"name": "Bình", "phone": "0902"} 
] 

print(find_customer(customers, "0902"))
# Kết quả: {'name': 'Bình', 'phone': '0902'}

print(find_customer(customers, "0901"))
# Kết quả: {'name': 'An', 'phone': '0901'}

print(find_customer(customers, "0903"))
# Kết quả: None


"""
Câu 32: 
         Kiểm tra tồn tại username [Dễ] 
Bối cảnh: 
          Khi đăng ký, hệ thống cần kiểm tra username đã được sử dụng chưa. 
Đề bài: 
           Viết hàm username_exists(users, username) trả về True nếu username  đã có trong danh sách users. 
Input mẫu: users = [{"username": "admin"}, {"username": "user01"}] 

            username_exists(users, "admin")
            
Output mẫu: True


    """
def username_exists(users, username):
    for user in users:
        if user["username"] == username:
            return True
    return False

    """
Hàm nhận vào 2 tham số:
users: danh sách người dùng.
username: username cần kiểm tra.
Duyệt từng user trong danh sách. Lấy username của user hiện tại và so sánh với username cần tìm.
Nếu tìm thấy username thì trả về True ngay lập tức.
Nếu duyệt hết danh sách mà không tìm thấy username thì trả về False.
    """
# Chạy thử:
users = [{"username": "admin"}, {"username": "user01"}]

print(username_exists(users, "admin"))
# Kết quả: True
print(username_exists(users, "user01"))
# Kết quả: True
print(username_exists(users, "user02"))
# Kết quả: False

"""
Câu 33: 
         Lọc đơn hàng đã thanh toán [Dễ] 
Bối cảnh: 
         Hệ thống xử lý giao hàng chỉ lấy các đơn đã thanh toán. 
Đề bài: 
         Viết hàm paid_orders(orders) trả về các đơn có is_paid bằng True. 
Input mẫu:

orders = [ 
 {"id": 1, "is_paid": True}, 
 {"id": 2, "is_paid": False} 
] 

paid_orders(orders)


Output mẫu: 
[{"id": 1, "is_paid": True}]


    """
def paid_orders(orders):
    result = []
    for order in orders:
        if order["is_paid"] == True:
            result.append(order)
    return result
# Chạy thử:
orders = [ 
 {"id": 1, "is_paid": True}, 
 {"id": 2, "is_paid": False} 
] 

print(paid_orders(orders))
# Kết quả: [{'id': 1, 'is_paid': True}]

orders = [ 
 {"id": 1, "is_paid": True}, 
 {"id": 2, "is_paid": False},
 {"id": 3, "is_paid": True},
 {"id": 4, "is_paid": True}
] 

print(paid_orders(orders))
# Kết quả: [{'id': 1, 'is_paid': True}, {'id': 3, 'is_paid': True}, {'id': 4, 'is_paid': True}]

"""
Câu 34: 
          Tính tổng tiền hoàn lại [Dễ] 
Bối cảnh: 
          Payment service cần tính tổng số tiền phải hoàn cho các giao dịch  refund. 
Đề bài:
          Viết hàm refund_total(transactions) cộng amount của các giao dịch có  type là refund.
Input mẫu: 

transactions = [ 
 {"type": "payment", "amount": 500000}, 
 {"type": "refund", "amount": 120000}, 
 {"type": "refund", "amount": 80000} 
] 

refund_total(transactions)
Output mẫu: 200000


    """
def refund_total(transactions):
    total = 0
    for transaction in transactions:
        if transaction["type"] == "refund":
            total = total + transaction["amount"] # Hoặc có thể viết gọn thành total += transaction["amount"]
    return total
# Chạy thử:
transactions = [ 
 {"type": "payment", "amount": 500000}, 
 {"type": "refund", "amount": 120000}, 
 {"type": "refund", "amount": 80000} 
] 
print(refund_total(transactions))
# kết quả: 200000

transactions = [ 
 {"type": "payment", "amount": 500000}, 
 {"type": "refund", "amount": 120000}, 
 {"type": "refund", "amount": 80000},
 {"type": "refund", "amount": 180000},
 {"type": "refund", "amount": 20000}
] 
print(refund_total(transactions))
# kết quả: 400000

"""
Câu 35: 
          Kiểm tra sản phẩm có trong wishlist [Dễ] (Tạo API) 
Bối cảnh: 
          Trang chi tiết sản phẩm cần biết sản phẩm hiện tại đã nằm trong  wishlist chưa. 
Đề bài: 
         Viết hàm is_wishlisted(product_id, wishlist) 
         trả về True nếu product_id  nằm trong set wishlist. 
Input mẫu: wishlist = {"SP001", "SP005", "SP012"} 
           is_wishlisted("SP005", wishlist)
Output mẫu: True


    """
def is_wishlisted(product_id, wishlist):
    if product_id in wishlist:
        return True
    else:
        return False
# Chạy thử
wishlist = {"SP001", "SP005", "SP012"} 
print(is_wishlisted("SP005", wishlist))
#　Kết quả: True
print(is_wishlisted("SP006", wishlist))
# Kết quả: False

# Hoặc có thể viết:
def is_wishlisted(product_id, wishlist):
    return product_id in wishlist # Kiểm tra product_id có nằm trong wishlist hay không.
                                  # "SP005" in wishlist => True
                                #   "SP003" in wishlist => False

    """
    Câu 36: 
           Lấy danh mục duy nhất [Dễ] 
Bối cảnh: 
            Trang bộ lọc cần hiển thị danh sách danh mục không trùng lặp. 
Đề bài: 
        Viết hàm unique_categories(products) 
        trả về set các category có trong  danh sách sản phẩm.
Input mẫu:

products = [ 
 {"name": "Áo", "category": "ao"}, 
 {"name": "Quần", "category": "quan"}, 
 {"name": "Áo khoác", "category": "ao"} 
] 

unique_categories(products)

Output mẫu: {"ao", "quan"}


    """
    """
    Duyệt qua danh sách sản phẩm và lấy category vào một set.
    Vì set không chứa phần tử trùng nhau nên một category chỉ xuất hiện một lần trong kết quả.
    Đối với input mẫu thì kết quả "ao" chỉ xuất hiện một lần.
    """
    
    """ 
    Nhắc lại kiến thức về set
    1. Không chứa phần tử trùng lặp
categories = {"ao", "quan", "ao"}

print(categories) ==> kết quả: {"ao", "quan"} ===> "ao" chỉ xuất hiện 1 lần.
    2. Không có thứ tự cố định: Set không đảm bảo thứ tự các phần tử. Vì vậy, không nên truy cập set bằng vị trí.
numbers = {3, 1, 2}

print(numbers) ==> Kết quả: {1, 2, 3} hoặc có thể là thứ tự khác. 

    3. Có thể thêm phần tử bằng add()
categories = {"ao", "quan"}

categories.add("giay")

print(categories) ==> Kết quả: {"ao", "quan", "giay"}

    4. Nếu thêm phần tử đã tồn tại thì không bị trùng
    
categories = {"ao", "quan"}

categories.add("ao")

print(categories) ===> Kết quả: {"ao", "quan"}

    5. Có thể xóa phần tử: 
           ví dụ: 
categories = {"ao", "quan", "giay"}

categories.remove("ao")

print(categories) ==> Kết quả: {"quan", "giay"}

    6. Kiểm tra phần tử có tồn tại rất thuận tiện
Dùng in:
categories = {"ao", "quan"}

print("ao" in categories) ==>  Kết quả: True
print("giay" in categories) ==> Kết quả: False

    7. Set thường dùng để loại bỏ dữ liệu trùng
categories = ["ao", "quan", "ao", "giay", "quan"]

unique_categories = set(categories)

print(unique_categories) ===> Kết quả: {"ao", "quan", "giay"}

===> set = tập hợp các giá trị không trùng nhau
    """
def unique_categories(products):
    categories = set() # Tạo một set rỗng để chứa các danh mục (category)
    for product in products: # Duyệt từng sản phẩm trong products.
        categories.add(product["category"]) # Lấy category của sản phẩm và thêm vào set.
    return categories
# Chạy thử:
products = [ 
 {"name": "Áo", "category": "ao"}, 
 {"name": "Quần", "category": "quan"}, 
 {"name": "Áo khoác", "category": "ao"} 
] 
print(unique_categories(products))
# Kết quả: {'quan', 'ao'}


"""Câu 37: 
      Kiểm tra dữ liệu bị thiếu [Dễ] 
Bối cảnh: 
      Data validation service cần phát hiện trường dữ liệu bị thiếu trước khi  lưu vào database. 
Đề bài: 
      Viết hàm count_missing(values) đếm số phần tử có giá trị None trong list. 
Input mẫu: values = [120, None, 350, None, 500] 
           count_missing(values)
Output mẫu: 2


    """
def count_missing(values):
    count = 0 # Tạo biến count để đếm số giá trị bị thiếu.
    for value in values: #Lần lượt lấy từng phần tử trong values. sẽ kiểm tra:
        if value is None: # Trong Python, khi kiểm tra một giá trị có phải None hay không, cách chuẩn là dùng is None thay vì if value == None:
            count += 1
    return count
# Chạy thử:
values = [120, None, 350, None, 500] 
print(count_missing(values))
# Kết quả = 2
values = [120, None, 350, None, 500, None, 350, None] 
print(count_missing(values))
# Kết quả = 4

"""
Câu 38: 
         Tính điểm đánh giá trung bình [Dễ] 
Bối cảnh: 
         Product service cần hiển thị rating trung bình của sản phẩm. 
Đề bài: 
    Viết hàm average_rating(reviews) tính trung bình rating.
    Nếu không có  review thì trả về 0. 
    
Input mẫu: reviews = [{"rating": 5}, {"rating": 4}, {"rating": 3}] 
           average_rating(reviews)
Output mẫu: 4.0


    """
def average_rating(reviews):
    if not reviews: # khi không có review thì trả về 0
        return 0
    
    rating_total = 0
    reviews_total = 0
    average = 0
    
    for review in reviews:
        rating_total += review["rating"] # Cộng tất cả rating
        reviews_total += 1 # Đếm số review
    average = rating_total/reviews_total #Tính trung bình: chỉ cần tính sau khi vòng lặp kết thúc
    # Vì reviews_total chính là số phần tử trong reviews, nên có thể dùng len()
    #  return rating_total / len(reviews)
    return average
# Chạy thử:
reviews = [{"rating": 5}, {"rating": 4}, {"rating": 3}] 
print(average_rating(reviews))
# Kết quả: 4.0

reviews = [{"rating": 5}, {"rating": 4}, {"rating": 3}, {"rating": 5}, {"rating": 5}, {"rating": 5}] 
print(average_rating(reviews))
# Kết quả: 4.5

# Hoặc có thể viết:
def average_rating(reviews):
    if not reviews: # khi không có review thì trả về 0
        return 0
    total = 0
    for review in reviews:
        total += review["rating"]
    return total/len(reviews)

# Chạy thử:
reviews = [{"rating": 5}, {"rating": 4}, {"rating": 3}] 
print(average_rating(reviews))
# Kết quả: 4.0

reviews = [{"rating": 5}, {"rating": 4}, {"rating": 3}, {"rating": 5}, {"rating": 5}, {"rating": 5}] 
print(average_rating(reviews))
# Kết quả: 4.5
reviews = [{"rating": 5}, {"rating": 4}, {"rating": 4}, {"rating": 5}, {"rating": 5}, {"rating": 5}] 
print(average_rating(reviews))
# Kết quả: 4.666666666666667

"""
Câu 39: 
         Phân loại ticket hỗ trợ [Dễ] 
Bối cảnh: 
         Support service phân loại ticket theo mức độ ưu tiên. 
Đề bài: 
         Viết hàm ticket_label(priority).
         Nếu priority là urgent trả về Xử lý ngay, 
         high trả về Ưu tiên cao, 
         normal trả về Bình thường, 
         còn lại trả về Không xác định.

Input mẫu: ticket_label("high")
Output mẫu: "Ưu tiên cao"


    """
def ticket_label(priority):
    if priority == "urgent":
        return "Xử lý ngay"
    elif priority == "high":
        return "Ưu tiên cao"
    elif priority == "normal":
        return "Bình thường"
    else:
        return "Không xác định"
# Chạy thử
print(ticket_label("urgent"))
# Kết quả: Xử lý ngay
print(ticket_label("high"))
# Kết quả: Ưu tiên cao
print(ticket_label("normal"))
# Kết quả: Bình thường
print(ticket_label("bckjachsak"))
# Kết quả: Không xác định

"""
Câu 40: 
         Tính số phòng còn trống [Dễ] 
Bối cảnh: 
       Booking service cần biết số phòng trống để hiển thị cho khách.
Đề bài: 
       Viết hàm available_rooms(rooms) đếm số phòng có status là empty. 
Input mẫu:

rooms = [ 
 {"room": "101", "status": "booked"}, 
 {"room": "102", "status": "empty"}, 
 {"room": "103", "status": "empty"} 
] 

available_rooms(rooms)

Output mẫu: 2


    """
def available_rooms(rooms):
    count = 0
    for  room in rooms:
        if room["status"] == "empty":
            count += 1
    return count
#　Chạy thử:

rooms = [ 
 {"room": "101", "status": "booked"}, 
 {"room": "102", "status": "empty"}, 
 {"room": "103", "status": "empty"} 
] 
print(available_rooms(rooms))
# Kết quả = 2

rooms = [ 
 {"room": "101", "status": "booked"}, 
 {"room": "102", "status": "empty"}, 
 {"room": "103", "status": "empty"},
  {"room": "102", "status": "empty"}, 
 {"room": "103", "status": "empty"} 
] 
print(available_rooms(rooms))
# # Kết quả = 4

"""
Câu 41: 
         Xây dựng catalog sản phẩm theo id [Khó] (Tạo API) 
         
Bối cảnh: 
      Backend API cần tối ưu tra cứu sản phẩm theo id thay vì phải duyệt list  nhiều lần. 
Đề bài: 
    Viết hàm build_catalog(products) chuyển danh sách sản phẩm thành dict  có dạng {id: product_info}. 
    Nếu có sản phẩm trùng id, giữ sản phẩm xuất hiện sau  cùng.
Input mẫu:

products = [ 
 {"id": "SP001", "name": "Áo", "price": 120000}, 
 {"id": "SP002", "name": "Quần", "price": 280000},  
 {"id": "SP001", "name": "Áo mới", "price": 150000} ] 

build_catalog(products)

Output:
{"SP001": {"id": "SP001", "name": "Áo mới", "price": 150000},

"SP002": {"id": "SP002", "name": "Quần", "price": 280000}}


    """

"""
Mô tả Input / Output

1. Input: list → danh sách chứa nhiều sản phẩm.

Mỗi sản phẩm là một dict, gồm 3 cặp key: value:

id: mã sản phẩm, kiểu str
name: tên sản phẩm, kiểu str
price: giá sản phẩm, kiểu int

2. Output: dict → dùng id của sản phẩm làm key để tra cứu.

Value là toàn bộ dict thông tin của sản phẩm tương ứng được lấy từ Input.

Mục đích: Chuyển danh sách sản phẩm (list) thành một dict có id làm key, giúp tra cứu sản phẩm theo id thuận tiện và nhanh hơn, ví dụ:

catalog["SP001"]

sẽ lấy được thông tin của sản phẩm có id = "SP001".

Lưu ý: Nếu có nhiều sản phẩm có cùng id, sản phẩm xuất hiện sau cùng trong list sẽ được giữ lại.

Duyệt từng sản phẩm trong list, 
    lấy id của sản phẩm làm key trong dict, lưu thông tin sản phẩm vào đó;
    nếu id bị trùng thì sản phẩm xuất hiện sau sẽ tự động ghi đè sản phẩm trước.
    """

"""Tại sao phải chuyển sang dict?

Nếu vẫn dùng list, muốn tìm một sản phẩm thường phải dùng duyệt qua các sản phẩm trước đó để tìm ra sản phẩm muốn tìm.
Nếu có rất nhiều sản phẩm thì việc tìm kiếm nhiều lần sẽ không tối ưu.
Nếu có rất nhiều sản phẩm thì việc tìm kiếm nhiều lần sẽ không tối ưu.
Ví dụ:
Muốn tìm SP002, phải duyệt qua danh sách products:
for product in products:
    if product["id"] == "SP002":
        ...
Sau khi chuyển sang dict, ta có thể lấy trực tiếp sản phẩm cần tìm bằng key của các cặp key:value
catalog = build_catalog(products) ==> Chuyển list sang dict bằng hàm build_catalog(products)
==> Lấy trực tiếp thông tin của từng sản phẩm: catalog["SP001"]  
==> Kết quả:
{
    "id": "SP001",
    "name": "Áo mới",
    "price": 150000
}

==> id trở thành key của dict
quy tắc:
dict[key] = value
catalog["SP001"]
    """
    
def buid_catalog(products):
    catalog = {}  # Tạo biến catalog và cho nó bằng một dict rỗng.
    
            # Duyệt từng sản phẩm. 
        # Với mỗi product trong danh sách products, hãy thực hiện các câu lệnh bên dưới.
        # Tìm key "id" của từng product trong danh sách products.
        # Lấy id của từng sản phẩm làm Key, toàn bộ thông tin của sản phẩm sẽ là Value để đưa vào catolog dạng dict đã tạo sẵn ở trên.
        #  Ví dụ:  
        #          Khi xét đến sản phẩm có id = SP001. 
        #          catalog[product["id"]] = product
        # chính là: 
        #          catalog["SP001"] = product
        #          Nghĩa là:
        #  Key: "SP001"
        # Value: {"id": "SP001", "name": "Áo", "price": 120000}
        # Nếu có sản phẩm trùng id, giữ sản phẩm xuất hiện sau  cùng.
        #        ==> dict không giữ hai key giống nhau. Vì vậy giá trị mới sẽ thay thế giá trị cũ: 
        # Lúc đầu: 
        #                 SP001 → Áo 
        # Sau đó:
        #                 SP001 → Áo mới
        #  id giống nhau: tự ghi đè sản phẩm cũ
        #        ===> Đây là lý do tại sao ta không cần dùng if để kiểm tra trùng id.
        # Sau khi hết sản phẩm thì vòng lặp dừng. Trả về catalog vừa được tạo.
    for product in products: 
        catalog[product["id"]] = product
    return catalog
# Chạy thử:
products = [ 
 {"id": "SP001", "name": "Áo", "price": 120000}, 
 {"id": "SP002", "name": "Quần", "price": 280000},  
 {"id": "SP001", "name": "Áo mới", "price": 150000} ] 
print(buid_catalog(products))

"""
    Kết quả:
    {
    'SP001': {'id': 'SP001', 'name': 'Áo mới', 'price': 150000}, 
    'SP002': {'id': 'SP002', 'name': 'Quần', 'price': 280000}
    }

    """
    
    
"""
Câu 42:
        Áp dụng mã giảm giá có điều kiện [Khó] 
Bối cảnh: 
Checkout service cần kiểm tra mã giảm giá theo loại percent hoặc  fixed và điều kiện đơn tối thiểu. 
Đề bài: 
Viết hàm apply_coupon(cart_total, code, coupon_db).
Nếu mã không tồn  tại trả về valid False. Nếu cart_total nhỏ hơn min_order trả về valid False. 
Nếu  hợp lệ, tính discount_amount, final_price và message. 

Input mẫu:

coupon_db = { 
 "SALE20": {"type": "percent", "value": 20, "min_order":  200000}, 
 "SHIP50K": {"type": "fixed", "value": 50000, "min_order":  150000} 
}
 
apply_coupon(350000, "SALE20", coupon_db)
Output mẫu:

{"valid": True, "discount_amount": 70000, "final_price":  280000, "message": "Áp dụng thành công"}


    """
"""Phân tích dữ liệu đề bài cho:

1.coupon_db là một dict chứa thông tin các mã giảm giá:
key: value => mã giảm giá: thông tin chi tiết giảm giá 
            Thông tin chi tiết giảm giá là một dict được lồng bên trong value của cặp key:value của dict chính.

Ví dụ mã "SALE20":

type = "percent" → giảm theo phần trăm
value = 20 → giảm 20%
min_order = 200000 → đơn hàng phải từ 200.000 trở lên

Mã "SHIP50K":

type = "fixed" → giảm một số tiền cố định
value = 50000 → giảm 50.000
min_order = 150000 → đơn hàng phải từ 150.000 trở lên
2. Kiểm tra điều kiện giảm giá
Ta kiểm tra theo thứ tự:

Có mã giảm giá không? 　　　　　　 → Không → valid = False
       ↓　
       ↓ Có
Đơn hàng có đủ min_order không?  →    Không → valid = False
       ↓
       ↓ Có
Mã là percent hay fixed?
       ↓
Tính discount_amount 
       ↓
Tính final_price
       ↓
Trả kết quả

3. 

    """
def apply_coupon(cart_total, code, coupon_db):
    # Kiểm tra mã giảm giá có tồn tại không.
    if code not in coupon_db:
        return {
            "valid": False,
            "discount_amount":0,
            "final_price": cart_total,
            "message": "Mã giảm giá không tồn tại"
        }
    # Lấy thông tin chi tiết của mã giảm  được nhập vào =  key của các cặp key:value 
    # code được nhập vào chính là mã giảm giá, được lưu là key trong dict chính, thông tin chi tiết của mã giảm giá là value trong dict chính.
    # Thông tin chi tiết mã giảm giá là một dict được lồng trong value của dict chính, có 3 cặp key:value
    #                            "type": "percent",
    #                            "value": 20,
    #                            "min_order":  200000
    coupon = coupon_db[code]
    #  nếu code = SALE20 thì thông tin lấy được sẽ là:
    #                            "type": "percent",
    #                            "value": 20,
    #                            "min_order":  200000   
    #  nếu code = SHIP50K thì thông tin lấy được sẽ là:
    #                            "type": "fixed", 
    #                            "value": 50000, 
    #                            "min_order":  150000 
    
    #  Kiểm tra min_order (Đơn hàng tới thiểu)
    
    if cart_total < coupon["min_order"]:
        return {
            "valid": False,
            "discount_amount": 0,
            "final_price": cart_total,
            "message": "Đơn hàng chưa đạt giá trị tối thiểu"
        }
    # Tính tiền giảm
    if coupon["type"] == "percent":
        discount_amount = cart_total * coupon["value"]/100
    elif coupon["type"] == "fixed":
        discount_amount = coupon["value"]
    # Tính giá cuối cùng:
    final_price = cart_total - discount_amount
    return {
        "valid": True,
        "discount_amount": discount_amount,
        "final_price": final_price,
        "message": "Áp dụng thành công"
    }
# Chạy với dữ liệu đề bài cho
coupon_db = { 
 "SALE20": {"type": "percent", "value": 20, "min_order":  200000}, 
 "SHIP50K": {"type": "fixed", "value": 50000, "min_order":  150000} 
}
print(apply_coupon(350000, "SALE20", coupon_db))

# Kết quả: {'valid': True, 'discount_amount': 70000.0, 'final_price': 280000.0, 'message':'Áp dụng thành công'}

print(apply_coupon(350000, "SHIP50K", coupon_db))
# Kết quả: {'valid': True, 'discount_amount': 50000, 'final_price': 300000, 'message': 'Áp dụng thành công'}
print(apply_coupon(350000, "SALE30", coupon_db))
# Kết quả: {'valid': False, 'discount_amount': 0, 'final_price': 350000, 'message': 'Mã giảm giá không tồn tại'}
print(apply_coupon(150000, "SALE20", coupon_db))
# Kết quả: {'valid': False, 'discount_amount': 0, 'final_price': 150000, 'message': 'Đơn hàng chưa đạt giá trị tối thiểu'}
print(apply_coupon(30000, "SHIP50K", coupon_db))
# Kết quả: {'valid': False, 'discount_amount': 0, 'final_price': 30000, 'message': 'Đơn hàng chưa đạt giá trị tối thiểu'}

"""
Câu 43: 
        Tổng hợp doanh thu theo ngày [Khó] (Tạo API) 
Bối cảnh: 
        Báo cáo kinh doanh cần gom các giao dịch theo ngày để tính tổng tiền,  số đơn và trung bình mỗi đơn. 
Đề bài: 
      Viết hàm daily_report(transactions)
         trả về dict dạng {date: {total, count,  avg}}. 
         Làm tròn avg đến 2 chữ số thập phân nếu cần.
Input mẫu:

transactions = [ 
 {"date": "2024-01-15", "amount": 320000}, 
 {"date": "2024-01-15", "amount": 180000}, 
 {"date": "2024-01-16", "amount": 450000} 
] 

daily_report(transactions)

Output:
{"2024-01-15": {"total": 500000, "count": 2, "avg": 250000.0},

"2024-01-16": {"total": 450000, "count": 1, "avg": 450000.0}}


    """
def daily_report(transactions):
    report = {}
    for transaction in transactions:
        # Lấy ngày
        date = transaction["date"]
        # Lấy số tiền
        amount = transaction["amount"]
        # Nếu ngày chưa tồn tại trong report
        if date not in report:
            report[date] = {
                "total": 0,
                "count": 0,
                "avg": 0
            }
        # Cộng tiền vào tổng doanh thu của ngày
        report[date]["total"] += amount
        # Tăng số lượng đơn
        report[date]["count"] += 1
    # Sau khi đã gom xong, tính trung bình
    for date in report:
        total = report[date]["total"]
        count = report[date]["count"]
        report[date]["avg"] = round(total/count, 2)
    return report
# Gọi hàm để chạy thử:
transactions = [ 
 {"date": "2024-01-15", "amount": 320000}, 
 {"date": "2024-01-15", "amount": 180000}, 
 {"date": "2024-01-16", "amount": 450000} 
] 
print(daily_report(transactions))
# Kết quả:
# {'2024-01-15': {'total': 500000, 'count': 2, 'avg': 250000.0},
#  '2024-01-16': {'total': 450000, 'count': 1, 'avg': 450000.0}}

"""
Câu 44: 
         Gợi ý sản phẩm liên quan [Khó] (Tạo API) 
Bối cảnh: 
        Recommendation service cần gợi ý sản phẩm cùng danh mục với sản  phẩm hiện tại. 
Đề bài: 
       Viết hàm related_products(product_id, products, limit). 
       Tìm category của  product_id, sau đó trả về tối đa limit sản phẩm cùng category, loại bỏ sản phẩm  hiện tại, sắp xếp rating giảm dần.
       Nếu product_id không tồn tại trả về list rỗng. 
Input mẫu:

products = [ 
 {"id": 1, "name": "Áo polo", "category": "ao", "rating": 4.5},  
 {"id": 2, "name": "Áo thun", "category": "ao", "rating": 4.8}, 
 {"id": 3, "name": "Áo khoác", "category": "ao", "rating": 4.2}, 
 {"id": 4, "name": "Quần", "category": "quan", "rating": 4.7}
 ] 

related_products(1, products, 2)

Output mẫu:

[{"id": 2, "name": "Áo thun", "category": "ao", "rating": 4.8}, 
{"id": 3, "name": "Áo khoác", "category": "ao", "rating": 4.2}]


    """
    
"""
 # 1. Tìm sản phẩm hiện tại
current_product

# 2. Lấy category của sản phẩm hiện 
current_category

# 3. Lọc sản phẩm cùng category, bỏ sản phẩm hiện tại
related

# 4. Sort rating giảm dần (Sắp xếp rating giảm dần)
related.sort(..., reverse=True)

# 5. Lấy tối đa limit
related[:limit]


ví dụ:  
      related_products(product_id, products, limit)
related_products(1, products, 2)
      
      product_id = 1: sản phẩm hiện tại là sản phẩm có id = 1
      products: danh sách tất cả sản phẩm
      limit = 2: chỉ lấy tối đa 2 sản phẩm gợi ý
Ta cần:

Tìm sản phẩm có id = 1.
Lấy category của nó → "ao".
Tìm các sản phẩm có category == "ao".
Loại bỏ chính sản phẩm id = 1.
Sắp xếp theo rating giảm dần.
Chỉ lấy tối đa limit = 2.
Nếu không tìm thấy id = 1 → [].
    """

def related_products(product_id, products, limit):
    # Bước 1: Tìm sản phẩm hiện tại
    current_product = None
    for product in products:
        if product["id"] == product_id:
            current_product = product
            break # Đã tìm thấy rồi → dừng vòng for. Không cần tiếp tục tìm những sản phẩm phía sau.
    if current_product is None:
        return []
    # Bước 2: Lấy category của sản phẩm hiện tại
    # Vì đề bài nói: Gợi ý sản phẩm cùng danh mục với sản phẩm hiện tại. => Do đó phải lấy category trước
    current_category = current_product["category"]
    # Bước 3: Lấy các sản phẩm cùng category
    #         và loại bỏ chính sản phẩm hiện tại
    related = []
    
    for product in products:
        if (
            product["category"] == current_category # phải cùng category.
            and product["id"] != product_id # không được là sản phẩm hiện tại.
        ):
            related.append(product) # Thêm các sản phẩm thỏa mãn 2 điều kiện  này vào danh sách sản phẩm liên quan: cùng category với sản phẩm hiện tại và  không phải là sản phẩm hiện tại
    # Bước 4: Sắp xếp rating giảm dần
    related.sort(
        key=lambda product: product["rating"], #dùng trường rating của từng sản phẩm để sắp xếp.
        reverse=True # sắp xếp giảm dần.Nếu không có reverse=True thì mặc định là tăng dần
    )
    # Bước 5: Chỉ lấy tối đa limit sản phẩm
    return related[:limit] # Sau khi sắp xếp, nếu limit = 2 thì lấy 2 phần tử đầu
# Chạy thử:
products = [ 
 {"id": 1, "name": "Áo polo", "category": "ao", "rating": 4.5},  
 {"id": 2, "name": "Áo thun", "category": "ao", "rating": 4.8}, 
 {"id": 3, "name": "Áo khoác", "category": "ao", "rating": 4.2}, 
 {"id": 4, "name": "Quần", "category": "quan", "rating": 4.7}
 ] 
print(related_products(1, products, 2))
# Kết quả: 
# [{'id': 2, 'name': 'Áo thun', 'category': 'ao', 'rating': 4.8}, 
# {'id': 3, 'name': 'Áo khoác', 'category': 'ao', 'rating': 4.2}]

products = [ 
 {"id": 1, "name": "Quần đùi", "category": "quan", "rating": 4.5},  
 {"id": 2, "name": "Áo thun", "category": "ao", "rating": 4.8}, 
 {"id": 3, "name": "Quần bò", "category": "quan", "rating": 4.2}, 
 {"id": 4, "name": "Quần", "category": "quan", "rating": 4.7}
 ] 
print(related_products(1, products, 2))
# Kết quả:
# [{'id': 4, 'name': 'Quần', 'category': 'quan', 'rating': 4.7},
# {'id': 3, 'name':'Quần bò', 'category': 'quan', 'rating': 4.2}]

"""
Câu 45: 
         Xếp hạng sản phẩm bán chạy [Khó] 
Bối cảnh: 
         Analytics service cần thống kê top sản phẩm bán chạy từ danh sách  các dòng sản phẩm trong đơn hàng. 
Đề bài: 
        Viết hàm top_selling(items, top_n). 
        
        Gom theo product_id, tính total_qty và 
        revenue = tổng qty * price của từng dòng.
        Trả về top_n sản phẩm theo total_qty  giảm dần.
Input mẫu:

items = [ 
 {"product_id": 1, "name": "Áo", "qty": 5, "price": 120000}, 
 {"product_id": 2, "name": "Quần", "qty": 3, "price": 350000}, 
 {"product_id": 1, "name": "Áo", "qty": 8, "price": 120000} ] 
 
top_selling(items, 2)

Output mẫu: 

[{"product_id": 1, "name": "Áo", "total_qty": 13, "revenue":  1560000}, 
{"product_id": 2, "name": "Quần", "total_qty": 3, "revenue":  1050000}]


    """
    
"""Dict dùng phù hợp để gom/tra cứu → List phù hợp để xếp hạng và trả kết quả.
    """
def top_selling(items, top_n):
    # Dict dùng để gom các sản phẩm theo product_id
    products = {}
    # Duyệt từng sản phẩm trong đơn hàng
    for item in items:
        product_id = item["product_id"]
        if product_id not in products:
            products[product_id] = {
                "product_id": product_id,
                "name": item["name"],
                "total_qty": 0,
                "revenue": 0
            }
        # Cộng số lượng bán:
        products[product_id]["total_qty"] += item["qty"]
        # Cộng doanh thu
        products[product_id]["revenue"] += item["qty"] * item["price"]
    # Chuyển dict thành list
    result = list(products.values())
    # Sắp xếp theo total_qty giảm dần. 
    result.sort(
        key=lambda product: product["total_qty"], 
        reverse=True
    )
    
    return result[:top_n] # Ví dụ: result[:5] ==> Lấy từ đầu list đến vị trí 5.
# Chạy thử:
items = [
    {"product_id": 1, "name": "Áo", "qty": 5, "price": 120000},
    {"product_id": 2, "name": "Quần", "qty": 3, "price": 350000},
    {"product_id": 1, "name": "Áo", "qty": 8, "price": 120000}
]
print(top_selling(items, 2))
# Kết quả
# [{'product_id': 1, 'name': 'Áo', 'total_qty': 13, 'revenue': 1560000}, 
#  {'product_id': 2, 'name': 'Quần', 'total_qty': 3, 'revenue': 1050000}]

"""
Câu 46: 
Phát hiện đơn hàng bất thường [Khó] (Tạo API) 
Bối cảnh: 
Fraud detection service cần tìm các đơn hàng có tổng tiền cao bất  thường so với mặt bằng chung. 
Đề bài: 
Viết hàm detect_anomalies(orders, threshold). 
Tính trung bình total của  tất cả đơn.
Trả về các đơn có total > threshold * avg.
Nếu danh sách rỗng trả về list rỗng. 

Input mẫu:

orders = [ 
 {"id": 101, "total": 250000}, 
 {"id": 102, "total": 180000}, 
 {"id": 103, "total": 920000}, 
 {"id": 104, "total": 210000} 
] 

detect_anomalies(orders, 2.0)

Output mẫu: 
[{"id": 103, "total": 920000}]


    """

"""
threshold = 2.0 nghĩa là:
Đơn hàng nào có total lớn hơn 2 lần mức trung bình thì được xem là bất thường.

orders
  ↓
Tính tổng total
  ↓
Tính trung bình avg
  ↓
threshold × avg
  ↓
Duyệt từng order
  ↓
total > threshold × avg ?
  ↓
Có → đưa vào kết quả
Không → bỏ qua

    """

# Cách 1:
def detect_anomalies(orders, threshold):
    # Nếu không có đơn hàng
    if not orders:
        return []
    # Bước 1: Tính tổng tiền của tất cả các đơn
    total_money = 0
    
    for order in orders:
        total_money = total_money + order["total"]
    # Bước 2: Đếm số lượng đơn hàng 
    number_of_orders = len(orders)
    # Bước 3: Tính giá trị trung bình của các đơn hàng
    avg = total_money / number_of_orders
    # Bước 4: Tính mức tiền được coi là bất thường 
    limit = threshold * avg
    # Bước 5: Tìm các đơn hàng bất thường
    result = []
    for order in orders:
        if order["total"] > limit:
            result.append(order)
    # Bước 6: Trả về kết quả cuối cùng
    return result
# Chạy thử:
orders = [ 
 {"id": 101, "total": 250000}, 
 {"id": 102, "total": 180000}, 
 {"id": 103, "total": 920000}, 
 {"id": 104, "total": 210000} 
] 
print(detect_anomalies(orders, 2))

# Kết quả:
# [{'id': 103, 'total': 920000}]

orders = [ 
 {"id": 101, "total": 250000}, 
 {"id": 102, "total": 180000}, 
 {"id": 103, "total": 920000}, 
 {"id": 104, "total": 210000} 
] 
print(detect_anomalies(orders, 3))
# Kết quả: []

    
# Cách 2: 
def detect_anomalies(orders, threshold):
    if not orders:
        return []
    # Tính tổng tiền của tất cả các đơn hàng
    total = sum(order["total"] for order in orders)
    # Tính số lượng đơn hàng
    count = len(orders)
    # Tính giá trị trung bình 
    avg = total/count
    # Tính ngưỡng bất thường
    limit = threshold * avg
    # Tìm các đơn có total lớn hơn ngưỡng
    result = []
    
    for order in orders:
        if order["total"] > limit:
            result.append(order)
    return result
# Chạy thử:
orders = [ 
 {"id": 101, "total": 250000}, 
 {"id": 102, "total": 180000}, 
 {"id": 103, "total": 920000}, 
 {"id": 104, "total": 210000} 
] 
print(detect_anomalies(orders, 2))

# Kết quả:
# [{'id': 103, 'total': 920000}]

orders = [ 
 {"id": 101, "total": 250000}, 
 {"id": 102, "total": 180000}, 
 {"id": 103, "total": 920000}, 
 {"id": 104, "total": 210000} 
] 
print(detect_anomalies(orders, 3))
# Kết quả: []

"""
Câu 47: 
           Kiểm tra phân quyền RBAC [Khó] (Tạo API) 
Bối cảnh: 
          Admin panel cần kiểm tra người dùng có được phép thực hiện hành  động trên tài nguyên hay không. 
Đề bài: 
          Viết hàm can_access(role, resource, action, rbac). 
          Trả về True nếu role  tồn tại, resource tồn tại trong role đó và action nằm trong danh sách quyền. 
          Ngược lại trả về False.
Input mẫu:  
rbac = { 
 "admin": {"products": ["read", "create", "update", "delete"]}, 
 "seller": {"products": ["read", "create", "update"]}} 
 
can_access("seller", "products", "delete", rbac)
Output mẫu: False


"""
"""
    RBAC (Role-Based Access Control) = Kiểm soát truy cập dựa trên vai trò.
    Không cấp quyền trực tiếp cho từng người dùng,
    mà cấp quyền cho từng vai trò (role), 
    rồi người dùng được hưởng quyền theo vai trò của mình.
    
    Ví dụ thực tế: 
    admin, seller, customer là role; 
    products, orders, users là resource; 
    read, create, update, delete là action.
    
    Hàm can_access() kiểm tra: 
    "Role này có được phép thực hiện action này trên resource này không?"
    Ví dụ:   
        can_access("seller", "products", "delete", rbac)
        ==> Seller có được phép delete products không?
        can_access("seller", "products", "update", rbac)
        ==> Seller có được phép update products không?
    
Role tồn tại?
    ↓ Có
Resource tồn tại?
    ↓ Có
Action có trong danh sách quyền?
    ↓ Có
True

Nếu bất kỳ bước nào không có
    ↓
False
    """
    
def can_access(role, resource, action, rbac):
    if role not in rbac: # Nếu role không tồn tại → False.
        return False
    if resource not in rbac[role]: # Nếu resource không tồn tại trong role → False.
        return False
    permissions = rbac[role][resource] # Nếu resource tồn tại trong role thì lấy danh sách quyền.
    
    if action in permissions: # Nếu action nằm trong danh sách quyền → True.
        return True
    return False # Nếu không nằm trong danh sách → False.

    

# input mẫu:
rbac = { 
 "admin": {"products": ["read", "create", "update", "delete"]}, 
 "seller": {"products": ["read", "create", "update"]}} 
# Gọi hàm chạy thử
print(can_access("seller", "products", "delete", rbac))
# Kết quả: False

print(can_access("seller", "products", "update", rbac))
# Kết quả: False


"""
Câu 49:
        Phân nhóm khách hàng theo số đơn [Khó] (Tạo API) 
Bối cảnh:
       Marketing service cần chia nhóm khách hàng để gửi chiến dịch phù  hợp. 
Đề bài: 
       Viết hàm segment_users(order_counts).
       Với mỗi user: 1 đơn là one_time,  từ 2 đến 4 đơn là repeat, từ 5 đơn trở lên là vip. 
       Trả về dict gồm 3 set user_id.
Input mẫu:
order_counts = {"U001": 1, "U002": 7, "U003": 3, "U004": 5} 
segment_users(order_counts)
Output mẫu
{"one_time": {"U001"}, "repeat": {"U003"}, "vip": {"U002",  "U004"}}


    """
def segment_users(order_counts):
    # Tạo 3 set để chứa user_id của từng nhóm
    one_time = set()
    repeat = set()
    vip = set()
    # Duyệt từng user và số đơn của user đó
    for user_id, order_count in order_counts.items():
        # order_counts là một dict
                            #    dict.items() = Lấy key + value
                            #    dict.keys() = Lấy key
                            #    dict.values() = Lấy value
        # Nếu đúng có 1 đơn
        if order_count == 1:
            one_time.add(user_id)
            
        # Nếu có từ 2 đến 4 đơn
        elif 2 <= order_count <= 4:
            repeat.add(user_id)
        
        # Nếu có từ 5 đơn trở lên
        elif order_count >= 5:
            vip.add(user_id)
    # Trả về dict gồm 3 set
    return {
        "one_time": one_time,
        "repeat": repeat,
        "vip": vip
    }
 #   Test với dữ liệu đầu bài
order_counts = {"U001": 1, "U002": 7, "U003": 3, "U004": 5} 
print(segment_users(order_counts))
# Kết quả: {'one_time': {'U001'}, 'repeat': {'U003'}, 'vip': {'U004', 'U002'}}

"""
Câu 50: '
    Kiểm tra xung đột sản phẩm trong chiến dịch [Khó] (Tạo API) 
Bối cảnh: 
    Trước khi tạo flash sale, hệ thống cần kiểm tra sản phẩm có bị trùng  với các chiến dịch đang hoạt động không. 
Đề bài: 
    Viết hàm check_conflicts(flash_sale_items, active_campaigns). 
    Trả về dict gồm has_conflict, conflicts và safe_items. 
    conflicts có dạng {product_id:  [campaign_name]}. 
    safe_items là sản phẩm không trùng chiến dịch nào.
Input mẫu:

active_campaigns = { 
 "clearance": {"SP001", "SP005"}, 
 "bundle": {"SP003", "SP007"} 
} 

flash_sale_items = {"SP001", "SP003", "SP020"} 

check_conflicts(flash_sale_items, active_campaigns)

Output mẫu: 

{
"has_conflict": True, 
"conflicts": {"SP001": ["clearance"], "SP003": ["bundle"]}, 
"safe_items": {"SP020"}
}


    """
def check_conflicts(flash_sale_items, active_campaigns):
    # Nơi lưu sản phẩm bị xung đột
    conflicts = {}
    
    # Nơi lưu sản phẩm an toàn
    safe_items = set()
    # Duyệt từng sản phẩm trong flash sale
    for product_id in flash_sale_items:
        # Tạo danh sách campaigns mà sản phẩm này tham gia
        campaigns = []
        # Duyệt từng campaign
        for campaign_name, products in active_campaigns.items():
            # Nếu sản phẩm nằm trong campaign
            if product_id in products:
                campaigns.append(campaign_name)
        # Nếu sản phẩm nằm trong ít nhất một campaign
        if campaigns:
            conflicts[product_id] = campaigns
        # Nếu không nằm trong campaign nào
        else:
            safe_items.add(product_id)
    # Nếu conflicts không rỗng ==> Có conflict ==> has_conflict: True
    has_conflict = len(conflicts) > 0
    
    return {
        
        "has_conflict": has_conflict,
        "conflicts": conflicts,
        "safe_item": safe_items
    }
# Chạy thử với dữ liệu đề bài cho
active_campaigns = { 
 "clearance": {"SP001", "SP005"}, 
 "bundle": {"SP003", "SP007"} 
} 

flash_sale_items = {"SP001", "SP003", "SP020"} 

print(check_conflicts(flash_sale_items, active_campaigns))
"""
 Kết quả
{'has_conflict': True, 
 'conflicts': {'SP003': ['bundle'], 'SP001': ['clearance']}, 
 'safe_item': {'SP020'}}
 """


# Thay đổi dữ liệu
active_campaigns = { 
 "clearance": {"SP002", "SP005"}, 
 "bundle": {"SP006", "SP007"} 
} 

flash_sale_items = {"SP001", "SP003", "SP020"} 

print(check_conflicts(flash_sale_items, active_campaigns))

# Kết quả:
""" 
# Kết quả:
{'has_conflict': False, 
'conflicts': {}, 
'safe_item': {'SP020', 'SP003', 'SP001'}
} 
"""
# Sản phẩm thuộc nhiều campaigns
active_campaigns = {
    "Summer Sale": [101, 105],
    "Black Friday": [101, 106],
    "VIP Sale": [101, 109]
}

flash_sale_items = {101, 103, 107} 

print(check_conflicts(flash_sale_items, active_campaigns))
"""
Kết quả:
{'has_conflict': True,
'conflicts': {101: ['Summer Sale', 'Black Friday', 'VIP S
ale']}, 
'safe_item': {107, 103}
}
"""



