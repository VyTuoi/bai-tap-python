
"""API không chứa logic nghiệp vụ; API chỉ nhận dữ liệu → gọi hàm → trả kết quả."""
# Bài tập 1:
# Viết API lọc danh sách sản phẩm
#API không trực tiếp chứa logic lọc. API chỉ nhận input và gọi hàm filter_available()
# API sẽ nhận danh sách sản phẩm → gọi hàm filter_available() → trả về danh sách sản phẩm còn hàng
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# ========================================
# Model Product
# ========================================

class Product(BaseModel):
    id: int
    name: str
    stock: int
    is_active: bool


# ========================================
# Hàm lọc sản phẩm còn hàng
# ========================================

def filter_available(products):
    available_products = []

    # Duyệt qua từng sản phẩm
    for product in products:

        # Kiểm tra 2 điều kiện:
        # 1. stock > 0: còn hàng
        # 2. is_active == True: đang hoạt động
        if product.stock > 0 and product.is_active == True:

            # Thêm sản phẩm đạt điều kiện vào danh sách
            available_products.append(product)

    # Trả về danh sách sản phẩm còn bán
    return available_products


# ========================================
# API lọc sản phẩm
# ========================================

@app.post("/products/filter-available")
def filter_available_api(products: list[Product]):

    # API chỉ nhận dữ liệu
    # và gọi hàm filter_available()
    return filter_available(products)

# Bài tập 2: Tính tổng tiền giỏ hàng
# Tạo API bằng FastAPI
from fastapi import FastAPI #Lấy FastAPI từ thư viện fastapi để sử dụng trong chương trình. 
                            # FastAPI là framework giúp chúng ta tạo API bằng Python.
                            # Nếu không có dòng này thì Python không biết FastAPI là gì.

from  pydantic import BaseModel #BaseModel được sử dụng để định nghĩa cấu trúc dữ liệu đầu vào và kiểm tra dữ liệu.

app  = FastAPI()

# Model cho từng sản phẩm trong giở hàng: Một sản phẩm trong giỏ hàng phải có name, price, quantity.

class CartItem(BaseModel):  #Tạo một class tên là CartItem, kế thừa từ BaseModel, Class CartItem là mẫu dữ liệu của một sản phẩm
                            #BaseModel của Pydantic giúp FastAPI:
                            # Kiểm tra dữ liệu
                            # Xác định kiểu dữ liệu
                            # Chuyển JSON thành object Python
                            # Tạo tài liệu Swagger tự động

    name: str  #name phải là kiểu str (chuỗi)
    price: int  # price phải là số nguyên
    quantity: int # quantity phải là số nguyên
    
# Hàm tính tổng tiền giỏ hàng
# cart là tham số đầu vào của hàm.
# Hàm nhận vào một giỏ hàng, xét duyệt từng item trong giỏ hàng. tính total của từng item sau đó cộng total của từng item với nhau.
def cart_total(cart): 
    total = 0 #Tạo biến total để lưu tổng tiền.
    for item in cart: # Lấy từng sản phẩm trong cart ra và xử lý.
        total += item["price"] * item["quantity"] # item là một dictionary. item = {"name": "Áo","price": 120000,"quantity": 2} =>  item["price"]: Lấy giá của item. item["quantity"]: Lấy số lượng của item.
                                                    #  total += item["price"] * item["quantity"]   => total = total + item["price"] * item["quantity"]
                                                    # 
    return total        #return dùng để trả kết quả của hàm

# API tính tổng tiền
@app.post("/cart/total")  
               
               # @ : Đây là cú pháp decorator trong Python. Decorator dùng để gắn thêm chức năng cho một hàm. Hàm ngay bên dưới sẽ xử lý request POST đến địa chỉ /cart/total.
               # post là HTTP method. 
            #    Một số HTTP method phổ biến: GET = Lấy dữ liệu. POST = Gửi/tạo dữ liệu. PUT = Cập nhật toàn bộ. PATCH = Cập nhật một phần. DELETE = Xóa dữ liệu
            # Bài này gửi giỏ hàng lên server để tính tổng tiền nên dùng: POST
            # /cart/total : Đây là đường dẫn endpoint. API này  sẽ có địa chỉ: http://127.0.0.1:8000/cart/total Trong đó: /cart/total là endpoint.
def calculate_cart_total_api(cart:list[CartItem]): 
    #Đây là hàm mà FastAPI sẽ gọi khi client gửi request đến: POST /cart/total. 
    # cart: list[CartItem]: cart là một danh sách (list) gồm nhiều CartItem.
    # list[CartItem]: Một danh sách chứa các đối tượng kiểu CartItem.
    
    
    cart_data = [item.model_dump() for item in cart] 
    
    total = cart_total(cart_data)
    
    return {
        "total": total
    }

# Bài tập 4: Viết API cho hàm  xử lý hiển thị thông báo dễ hiểu theo trạng thái đơn hàng order_message()
from fastapi import FastAPI
app = FastAPI()
# hàm  xử lý hiển thị thông báo dễ hiểu theo trạng thái đơn hàng order_message()
def order_message(status):
    if status == "pending":
        return "Chờ xử lý"
    if status == "confirmed":
        return "Đã xác nhận"
    if status == "shipping":
        return "Đang giao"
    if status == "completed":
        return "Hoàn thành"
    if status == "cancelled":
        return "Đã hủy"
    else:
        return "Không hợp lệ"
    
    # API
@app.get("/order/message")  #tạo một API sử dụng phương thức GET. Endpoint: /order/message

def get_order_message_api(status: str):    #  status: str = khai báo status phải là kiểu chuỗi
        message = order_message(status)
        return {
        "status": status,
        "message": message
    }
# Test với input mẫu:
# status: shipping
# 	
# Response body:
# {
#   "status": "shipping",
#   "message": "Đang giao"
# }

# Test với trường hợp  khác:
# Status: cancelled
# Kết quả:
	
# Response body

# {
#   "status": "cancelled",
#   "message": "Đã hủy"
# }

 # Câu 13: 
#     Phân loại khách hàng theo tổng chi tiêu [Dễ] (Tạo API) 
# Bối cảnh: 
#     Marketing service phân loại khách hàng để gửi ưu đãi. 
# Đề bài: 
#     Viết hàm classify_customer(total_spent). Nếu dưới 1 triệu là normal, từ 1  triệu đến dưới 5 triệu là silver, từ 5 triệu trở lên là gold. 
# Input mẫu: classify_customer(5200000)
# Output mẫu: "gold"

# Tạo API bằng FastAPI
from fastapi import FastAPI
app = FastAPI()

# Hàm phân loại khách hàng 
def classify_customer(total_spent):
    if total_spent < 1000000:
        return "normal" # Nếu total_spent dưới 1.000.000 → "normal"
    elif 1000000 <= total_spent < 5000000:
        return "silver" # Nếu total_spent từ 1.000.000 đến dưới 5.000.000 → "silver"
    else:
        return "gold" # Nếu total_spent từ 5.000.000 trở lên → "gold"
# API phân loại khách hàng
# Người dùng gửi total_spent
# API nhận dữ liệu
# Gọi hàm classify_customer(total_spent)
# Hàm kiểm tra mức chi tiêu
# Trả về normal / silver / gold
# API trả kết quả cho người dùng
@app.get("/classify-customer")
def get_customer_type(total_spent: int):
   customer_type = classify_customer(total_spent)
   return {
       "total_spent": total_spent,
       "customer_type": customer_type
   }
   
# Test
# total_spent: 5000000

# Kết quả: 	
# Response body
# {
#   "total_spent": 5000000,
#   "customer_type": "gold"
# }

# total_spent: 900000
	
# Response body

# {
#   "total_spent": 900000,
#   "customer_type": "normal"
# }


# total_spent: 4000000
	
# Response body

# {
#   "total_spent": 4000000,
#   "customer_type": "silver"
# }

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

# Tạo API
from fastapi import FastAPI
from pydantic import BaseModel # dùng Pydantic Model để FastAPI nhận JSON đúng kiểu.
app = FastAPI()

"""Model cuar User"""
class User(BaseModel):
    id: int
    name: str
    is_active: bool
    
"""Hàm để lọc user đang hoạt động"""

def active_users(users):
    result = []
    for user in users:
        if user.is_active == True: # thì user là một object User, nên phải viết: user.is_active, user.id, user.name chứ không viết được dạng user["is_active"], user["id"], user["name"]
            result.append(user)
    return result
"""API lọc user đang hoạt động"""

@app.post("/active-user")
def get_active_user(users: list[User]):
    return active_users(users)

# Test
# Request body:

# [
#   {
#     "id": 1,
#     "name": "An",
#     "is_active": true
#   },
#   {
#     "id": 2,
#     "name": "Bình",
#     "is_active": false
#   }
# ]

# Response body:
# [
#   {
#     "id": 1,
#     "name": "An",
#     "is_active": true
#   }
# ]

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

from fastapi import FastAPI
app = FastAPI()

def latest_order(orders):
    # Kiểm tra danh sách order có rỗng không?
    if len(orders) == 0:
        return None
    # Lấy đơn hàng đầu tiên làm giá trị khởi tạo của latest (Đơn hàng mới nhất)
    latest = orders[0]
    # Duyệt từng đơn hàng. So sánh id của đơn hàng được xét tới với id của lastest khởi tạo.
    # Nếu id của đơn hàng được xét tới hơn hơn id của latest thì cập nhập latest thành  của đơn hàng đang xét.
    # Nếu id của đơn hàng được xét tới nhỏ hơn  id của latest thì giữ nguyên latest hiện tại.
    for order in orders:
        # So sánh id của đơn hàng hiện tại với id của latest
        if order["id"] > latest["id"]:
            latest = order
    return latest # Trả về đơn hàng có id lớn nhất
@app.post("/latest-order")
def get_latest_order(orders: list[dict]):
    return latest_order(orders)

# Test API
# Request body:
# [
#   {"id": 101},
#   {"id": 105},
#   {"id": 103}
# ]

	
# Response body:
# {
#   "id": 105
# }

# Request body:
# [
#   {"id": 101},
#   {"id": 105},
#   {"id": 106},
#   {"id": 109}

# ]

	
# Response body:
# {
#   "id": 109
# }

# cách 2:
from fastapi import FastAPI
app = FastAPI()

def latest_order(orders):
    if not orders:
        return None
    return max(orders, key=lambda order: order["id"])
@app.post("/latest-order")
def get_latest_order(orders: list[dict]):
    return latest_order(orders)

# Test API
# Request body:
# [
#   {"id": 101},
#   {"id": 105},
#   {"id": 106},
#   {"id": 109}, 
#   {"id": 110}

# ]
# Response body:
# {
#   "id": 110
# }

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

from fastapi import FastAPI
app = FastAPI()

def daily_revenue(transactions):
    total = 0 # Biến total dùng để lưu tổng doanh thu. Giá trị khởi tạo = 0
    for transaction in transactions: # Duyệt từng giao dịch
        # Chỉ cộng tiền nếu giao dịch có status là success
        if transaction["status"] == "success":
            total = total +transaction["amount"]
    return total
@app.post("/daily-revenue")
def get_dailly_revenue(transactions: list[dict]):
    result = daily_revenue(transactions)
    return {
        "daily_revenue": result
    }
    
# Test API
# Request body:
"""
[ 
 {"amount": 100000, "status": "success"}, 
 {"amount": 50000, "status": "failed"}, 
 {"amount": 200000, "status": "success"} 
] 

"""
# 	
# Response body:
"""
    {
  "daily_revenue": 300000
}
    
"""

# Request body:
"""
[ 
 {"amount": 100000, "status": "success"}, 
 {"amount": 50000, "status": "failed"},
{"amount": 100000, "status": "success"}, 
 {"amount": 200000, "status": "success"} 
] 

"""
# 	
# Response body:
"""
{
  "daily_revenue": 400000
}  
"""
# Câu 19: 
#     Tạo mã đơn hàng đơn giản [Dễ] (Tạo API) 
# Bối cảnh: 
#     Hệ thống cần tạo mã đơn hàng từ id số nguyên. 
# Đề bài:
#     Viết hàm order_code(order_id) trả về chuỗi có dạng ORD-<id>, 
#     trong đó  id được thêm số 0 phía trước để đủ 5 chữ số.
# Input mẫu: "order_code(27)
# Output mẫu: "ORD-00027"

from fastapi import FastAPI
app = FastAPI()

"""Hàm xử lý logic tạo mã đơn hàng
    """
def order_code(order_id):
    return "ORD-"  + str(order_id).zfill(5)

@app.get("/order-code/{order_id}")
def get_order_code(order_id: int):  # Hàm API gọi hàm order_code()
    return {
        "order_code": order_code(order_id)
    }

# Test API
# order_id *: 7
# Response body:
# {
#   "order_code": "ORD-00007"
# }


# order_id *: 1234
# Response body:
# {
#   "order_code": "ORD-01234"
# }

# order_id *: 12345
# Response body:
# {
#   "order_code": "ORD-12345"
# }

"""
 Câu 22: 
    Tìm sản phẩm rẻ nhất [Dễ] (Tạo API) 
Bối cảnh: 
     Trang gợi ý muốn hiển thị sản phẩm có giá thấp nhất trong một danh  sách. 
 Đề bài: 
     Viết hàm cheapest_product(products) trả về sản phẩm có price nhỏ nhất.  
     Nếu danh sách rỗng trả về None. 
 Input mẫu: 
 products = [ 
 {"name": "Áo", "price": 120000}, 
 {"name": "Tất", "price": 25000} 
] 
cheapest_product(products)

Output mẫu: {"name": "Tất", "price": 25000}
 """

from fastapi import FastAPI
app = FastAPI()

def cheapest_product(products):
    if len(products) == 0: # là đếm số phần tử trong danh sách => Nếu số lượng sản phẩm bằng 0 → trả về None.
        return None
    cheapest = products[0]
        
    for product in products:
        if product["price"] < cheapest["price"]:
            cheapest = product
    return cheapest

    """
GET	Lấy dữ liệu
POST	Gửi dữ liệu lên server ==> Ở bài này, bạn gửi cả một danh sách sản phẩm lên API để server xử lý, nên dùng: POST
PUT	Cập nhật dữ liệu
DELETE	Xóa dữ liệu

    Returns:
        _type_: _description_
    """
@app.post("/cheapest_product") 
def get_cheapest_product(products:list[dict]): #API nhận vào một danh sách các dictionary từ JSON.
    return {
        "cheapest_product": cheapest_product(products)
    }
    
    """Test API
    Request body:
    [ 
 {"name": "Áo", "price": 120000}, 
 {"name": "Tất", "price": 25000} 
] 

	
Response body:
{
  "cheapest_product": {
    "name": "Tất",
    "price": 25000
  }
}
    """

# cách 2
from fastapi import FastAPI
app = FastAPI()

def cheapest_product(products):
    if not products:
        return None
    else:
        return min(products, key=lambda product: product["price"])
@app.post("/cheapest-product")
def get_cheapest_product(products: list[dict]):
    return cheapest_product(products)
"""
Test API
Request body:
[
    {
        "id": 1,
        "name": "Laptop",
        "price": 20000000
    },
    {
        "id": 2,
        "name": "Chuột",
        "price": 500000
    },
    {
        "id": 3,
        "name": "Bàn phím",
        "price": 1000000
    }
]

	
Response body:

{
  "id": 2,
  "name": "Chuột",
  "price": 500000
}

"""


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

from fastapi import FastAPI
app = FastAPI()

def coupon_exists(code, coupons):
    if code in coupons:
        return True
    else:
        return False
@app.post("/check-coupon-exist")
def check_coupon_exists(code: str):
    coupons = ["SALE10", "VIP20", "FREESHIP"] 
    return {
        "code": code,
        "exists": coupon_exists(code, coupons)
    }
    
    """TestAPI

    code: VIP20
    	
Response body:
{
  "code": "VIP20",
  "exists": true
}

code: VIP30

Response body:
{
  "code": "VIP30",
  "exists": false
}

    
    """
# Cách 2:
  
from fastapi import FastAPI

app = FastAPI()


def coupon_exists(code, coupons):
    return code in coupons

    """
    1. def coupon_exists(code, coupons):

Tạo một hàm tên là coupon_exists, nhận vào 2 tham số:

code: mã giảm giá cần kiểm tra.
coupons: danh sách các mã giảm giá hợp lệ.

2. return code in coupons

in dùng để kiểm tra code có nằm trong danh sách coupons hay không.
 Có =>  True
 Không có => False
    """

@app.get("/coupon")
def check_coupon(code: str):
    coupons = ["SALE10", "VIP20", "FREESHIP"]

    return {
        "code": code,
        "exists": coupon_exists(code, coupons)
    }
    
"""TestAPI

    code: FREESHIP
        
Response body:
{
  "code": "FREESHIP",
  "exists": true
}

code: hskjd

Response body:
{
  "code": "hskjd",
  "exists": false
}

    
    """
    

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
from fastapi import FastAPI
from typing import List, Dict, Any

app = FastAPI()


def filter_by_category(products, category):
    result = []

    for product in products:
        if product["category"] == category:
            result.append(product)

    return result

@app.post("/products/filter")
def filter_products(
    # phần khai báo kiểu dữ liệu để FastAPI hiểu dữ liệu đầu vào.
    products: List[Dict[str, Any]], 
    # products là một danh sách các dictionary: products là danh sách.
    # Mỗi phần tử trong List là một dictionary.
    # Dict[str, ...] => key là chuỗi
    # Dict[str, Any] => Any => → value có thể là bất kỳ kiểu dữ liệu nào.
    # ==> Một danh sách, bên trong chứa các dictionary, key là chuỗi và value có thể là bất kỳ kiểu dữ liệu nào.
    category: str
    # tham số category phải là chuỗi. 
):
    return filter_by_category(products, category)

    """Test API:
 Tham số(Parameter):
    1. category: ao
    
    2. Request body: 
    [ 
 {"name": "Áo thun", "category": "ao"}, 
 {"name": "Quần jean", "category": "quan"} 
] 

    
    
Response body: 

[
  {
    "name": "Áo thun",
    "category": "ao"
  }
]


Tham số(Parameter):
    1. category: 
    
    2. Request body: 
 [ 
 {"name": "Áo thun", "category": "ao"}, 
 {"name": "Quần jean", "category": "quan"},
 {"name": "Quần đùi", "category": "quan"}
] 

    
    
Response body: 

[
  {
    "name": "Quần jean",
    "category": "quan"
  },
  {
    "name": "Quần đùi",
    "category": "quan"
  }
]
    """
    
    
    
    
    
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

from fastapi import FastAPI
app = FastAPI()

# Hàm tìm khách hàng thông qua số điện thoại
def find_customer(customers, phone):
    for customer in customers:
        if customer["phone"] == phone:
            return customer
    return None
# List khách hàng:
customers = [ 
 {"name": "An", "phone": "0901"}, 
 {"name": "Bình", "phone": "0902"} 
] 

# API tìm khách hàng thông qua số điện thoại
"""
    bài này là “tìm/tra cứu khách hàng”, nên GET phù hợp hơn POST
    Ta không tạo mới hay thay đổi dữ liệu → dùng GET.
    GET = Lấy dữ liệu
    POST = Gửi dữ liệu lên server để tạo dữ liệu mới/xử lý.
    """
@app.get("/find-customer")
def get_customer(phone: str):
    customer = find_customer(customers, phone)
    if customer is None:
        return {
            "message": "Không tìm thấy khách hàng"
        }
    return customer
    """Test API
    Parameters: 
          phone: 0901
    	
    Response body:
             {
  "name": "An",
  "phone": "0901"
}

    Parameters: 
          phone: 
    	
    Response body: 0902
  {
  "name": "Bình",
  "phone": "0902"
}


    Parameters: 
          phone: 0903
    	
    Response body:
 {
  "message": "Không tìm thấy khách hàng"
}


    """
    
    """Trường hợp 2:
Trường hợp này danh sách khách hàng không có sẵn trên server, mà client muốn:
      Gửi customers lên server.
      Gửi thêm phone của khách hàng cần tìm kiếm từ danh sách customer.
      Server tìm khách hàng có số điện thoại trùng với số điện thoại đươc nhập vào.
      Trả về khách hàng nếu tìm thấy kết quả tương ứng  hoặc trả về None nếu không tìm thấy kết quả tương ứng.
      ===> vì client đang gửi một danh sách dữ liệu lên server để server xử lý ==> POST là hợp lý
      
    """
"""
    Lưu ý: nếu dữ liệu khách hàng thực tế là dữ liệu nhạy cảm, không nên tùy tiện gửi cả danh sách qua API chỉ để tìm một người; 
    trong hệ thống thật thường server/database đã lưu danh sách và API chỉ nhận phone
    """
    
# POST body chứa danh sách, phone là query parameter
from fastapi import FastAPI
from typing import List, Dict, Any

app = FastAPI()
# Hàm tìm kiếm khách hàng thông qua số điện thoại
def find_customer(customers, phone):
    for customer in customers:
        if customer["phone"] == phone:
            return customer
    return None
# API tìm kiếm khách hàng thông qua số điện thoại
@app.post("/find-customer")
def get_customer(   # khai báo một hàm Python có tên get_customer, đồng thời sử dụng type hint (gợi ý kiểu dữ liệu)
                 #  customers: List[Dict[str, Any]] => customers là một danh sách các khách hàng, mỗi khách hàng là một dictionary.  
                 # Dict[str, Any] ===> Dictionary có key là str, còn value có thể là bất kỳ kiểu nào (Any).
                # phone: str ==> tham số tìm kiếm phone dự kiến là kiểu str (chuỗi)
    customers: List[Dict[str, Any]],
    phone: str
):
    return find_customer(customers, phone)
    """Test API
    
    Parameters:
         phone: 0901
         
         Request body: Đây là dữ liệu lớn cần gửi lên server, nên để trong request body
                   customers = [ 
 {"name": "An", "phone": "0901"}, 
 {"name": "Bình", "phone": "0902"},
{"name": "Anh", "phone": "0903"},
{"name": "Tuấn", "phone": "0904"}
 
] 

	
Response body: 


         {
  "name": "An",
  "phone": "0901"
}


   Parameters:
         phone: 0905
         
         Request body: 
                   customers = [ 
 {"name": "An", "phone": "0901"}, 
 {"name": "Bình", "phone": "0902"},
{"name": "Anh", "phone": "0903"},
{"name": "Tuấn", "phone": "0904"}
 
] 

    
Response body: null

    """
    
# Gửi cả customers và phone trong Body
# Nếu muốn request rõ ràng hơn, mình có thể đưa cả danh sách và phone vào body
# client gửi danh sách khách hàng + số điện thoại cần tìm lên API bằng POST, server tìm khách hàng và trả về kết quả.
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Customer(BaseModel): # mẫu dữ liệu của một khách hàng.
    name: str
    phone: str
class FindCustomerRequest(BaseModel): #dữ liệu mà API yêu cầu client gửi lên
    customers: list[Customer]
    phone: str

def find_customer(customers, phone):
    for customer in customers:
        if customer.phone == phone: # customers sau khi FastAPI/Pydantic xử lý sẽ chứa các object kiểu Customer, không phải dictionary ==> do đó thay vì viết if customer["phone"] == phone ta sẽ viết thành if customer.phone == phone:
            return customer
    return None
@app.post("/find-customer")
def get_customer(data: FindCustomerRequest):
    return find_customer(data.customers, data.phone)
# Test API

    """
    Request body:
    {
  "customers": [
    {
      "name": "string",
      "phone": "string"
    }
  ],
  "phone": "string"
}

Test lần 1:
  Request body:
{
    "customers": [
        {
            "name": "An",
            "phone": "0901"
        },
        {
            "name": "Bình",
            "phone": "0902"
        }
    ],
    "phone": "0902"
}
	
Response body:
{
  "name": "Bình",
  "phone": "0902"
}


Test lần 2:
  Request body:
{
    "customers": [
        {
            "name": "An",
            "phone": "0901"
        },
        {
            "name": "Bình",
            "phone": "0902"
        }
    ],
    "phone": "0900"
}

Response body:
	
Response body: null

    """
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

"""Bài toán là:

Kiểm tra sản phẩm product_id có nằm trong wishlist hay không.
Đây là thao tác đọc/kiểm tra dữ liệu, không tạo mới, không sửa, không xóa.
==> Vì vậy nên dùng HTTP method là GET
Nếu wishlist đã tồn tại trên server/database, thì GET là phù hợp nhất.
Wishlist đã có trên server → chỉ kiểm tra ==> GET 
Client gửi wishlist lên server để kiểm tra ==> POST

    """
    
from fastapi import FastAPI
app = FastAPI()
# Danh sách sản phẩm trong wishlist
wishlist = {"SP001", "SP005", "SP012"}
# Hàm kiểm tra sản phẩm có trong wishlist hay không?
def is_wishlisted(product_id, wishlist):
    if product_id in wishlist:
        return True
    else:
        return False
# API kiểm tra wishlist
@app.get("/wishlist/check")
def check_wishlist(product_id: str):
    result = is_wishlisted(product_id, wishlist)
    return {
        "product_id": product_id,
        "is_wishlist": result
    }
    
    """Test API
Case 1:

    Parameters:
            product_id: SP005
    Response body:
    {
  "product_id": "SP005",
  "is_wishlist": true
}
# Case 2
    Parameters:
            product_id: SP006
    Response body:
{
  "product_id": "SP006",
  "is_wishlist": false
}


    """
# Cách 2:
from fastapi import FastAPI
app = FastAPI()

# Wishlist có sẵn
wishlist = {"SP001", "SP005", "SP012"}
# Hàm check wishlist
def is_wishlisted(product_id, wishlist):
    return product_id in wishlist
# API check wishlist
@app.get("/wishlist/check")
def check_wishlist(product_id: str):
    result = is_wishlisted(product_id, wishlist)
    return {
        "Mã sản phẩm": product_id,
        "Kết quả kiểm tra": result
    }
    """Test API
    
    case1:
    Parameters:
           product_id: SP005
    Response body:
         
          {
  "Mã sản phẩm": "SP005",
  "Kết quả kiểm tra": true
}

   Case2:
    Parameters:
           product_id: SP006
    Response body:
         
{
  "Mã sản phẩm": "SP006",
  "Kết quả kiểm tra": false
}

    """
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
# Tạo API  bằng cách sử dụng FastAPI + phương thức POST
# Lý do dùng POST: client cần gửi cả danh sách sản phẩm lên server để server xây dựng catalog
from fastapi import FastAPI
from pydantic import BaseModel

# Tạo ứng dụng FastAPI
app = FastAPI()

# Mô tả cấu trúc của một sản phẩm(schema)
class Product(BaseModel):
    id: str
    name: str
    price: int

# Hàm xử lý nghiệp vụ.
# Tạo dict rỗng để lưu catalog
# Duyệt từng sản phẩm trong list
# Lấy id làm key
# Lưu toàn bộ thông tin sản phẩm làm value
# Trả về catalog đã tạo sau khi duyệt hết tất cả sản phẩm
def buid_catalog(products):
    catalog = {}
    for product in products:
        catalog[product["id"]] = product
    return catalog
# API nhận danh sách sản phẩm và trả về catolog tra cứu sản phẩm dạng dict có key là id của product
@app.post("/catalog") #Tạo một API sử dụng phương thức POST, có đường dẫn /catalog.
def create_catalog(products: list[Product]): # products là một list chứa nhiều đối tượng Product.
     # Tạo list rỗng để chứa dữ liệu của sản phẩm
    product_list = []
    # Duyệt từng Product
    for product in products:
            # Chuyển Product thành dict
        product_dict = product.model_dump()
         # Thêm dict vào list
        product_list.append(product_dict)
    # Gọi hàm buid_catalog để tạo catalog
    catalog = buid_catalog(product_list)
    # Trả về catalog cho client
    return catalog
    
  


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
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Model của một giao dịch

class Transaction(BaseModel):
    date: str
    amount: int

# Hàm xử lý nghiệp vụ
def daily_report(transactions):
    report = {}
    
    for transaction in transactions:
        date = transaction.date
        amount = transaction.amount
        
        if date not in report: # Tạo nhóm mới theo date của giao dịch vừa được xét duyệt tới
                               #  Chính là key: value  của report
                            #     ===> group by theo ngày
            report[date] = {
                "total": 0,
                "count": 0,
                "avg": 0
            }
        report[date]["total"] += amount
        report[date]["count"] += 1
    for date in report:
        total = report[date]["total"]
        count = report[date]["count"]
        report[date]["avg"] = round(total/count, 2)
    return report

# API
@app.post("/daily-report")
def create_daily_report(transactions: list[Transaction]):
    return daily_report(transactions)
    """Test API
    Request body:
    [
    {
        "date": "2024-01-15",
        "amount": 320000
    },
    {
        "date": "2024-01-15",
        "amount": 180000
    },
    {
        "date": "2024-01-16",
        "amount": 450000
    }
]

Response body:
{
  "2024-01-15": {
    "total": 500000,
    "count": 2,
    "avg": 250000
  },
  "2024-01-16": {
    "total": 450000,
    "count": 1,
    "avg": 450000
  }
}
    """
    
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
    
"""
API của bài này dùng GET vì bản chất của API là lấy dữ liệu, không phải tạo hay sửa dữ liệu.
Cụ thể đề bài yêu cầu:
Tìm sản phẩm cùng category và trả về danh sách sản phẩm liên quan.
Nó chỉ đọc dữ liệu từ products và trả kết quả. Không thay đổi products.
Dữ liệu trong database/list không bị thay đổi.
Không có thao tác tạo, sửa hoặc xóa dữ liệu → GET là phù hợp.
Một điểm rất đáng chú ý: related_products() có xử lý dữ liệu (lọc, sort), nhưng vẫn là GET, vì "xử lý" không đồng nghĩa với "thay đổi dữ liệu nguồn".
GET vẫn có thể thực hiện rất nhiều logic phía server miễn là mục đích chính là đọc/truy xuất dữ liệu.

    """
from fastapi import FastAPI
app = FastAPI()

products = [
    {
        "id": 1,
        "name": "Áo polo",
        "category": "ao",
        "rating": 4.5
    },
    {
        "id": 2,
        "name": "Áo thun",
        "category": "ao",
        "rating": 4.8
    },
    {
        "id": 3,
        "name": "Áo khoác",
        "category": "ao",
        "rating": 4.2
    },
    {
        "id": 4,
        "name": "Quần",
        "category": "quan",
        "rating": 4.7
    }
]

def related_products(product_id, products, limit):
    # Tìm sản phẩm hiện tại
    current_product = None # Tạo một biến để tạm thời chứa sản phẩm cần tìm, nhưng ban đầu chưa tìm thấy sản phẩm nào. 
                        #    Tạo chỗ để chứa sản phẩm cần tìm; hiện tại chưa tìm thấy nên giá trị là None.
                           # None: Không có giá trị / chưa có dữ liệu.
                        #    Khi tìm thấy thì thay None bằng sản phẩm
    
    for product in products:
        if product["id"] == product_id:
            current_product = product # Đã tìm thấy → lưu sản phẩm vào biến này.
            break # # Đã tìm thấy rồi → dừng vòng for. Không cần tiếp tục tìm những sản phẩm phía sau.
    # Kiểm tra xem cuối cùng có tìm thấy sản phẩm hay không.
    # Không tìm thấy sản phẩm. Nếu sau khi tìm kiếm mà current_product vẫn là None → không tìm thấy sản phẩm → trả về [].
    if current_product is None:
        return []
    # Lấy category của sản phẩm hiện tại
    current_category = current_product["category"]
    # Tìm sản phẩm  cùng category
    # Đồng thời loại bỏ sản phẩm hiện tại
    
    related = []
    
    for product in products:
        if (
            product["category"] == current_category
            and product["id"] != product_id
        ):
            related.append(product)
    # Sắp xếp danh sách related dựa trên rating, từ cao xuống thấp.
    related.sort(
        key=lambda product: product["rating"],
        reverse=True
    )
    return related[:limit]
@app.get("/products/{product_id}/related")
def get_related_products(product_id: int, limit: int = 5): #limit là số nguyên và nếu người dùng không truyền limit thì mặc định lấy 5 sản phẩm.
    return related_products(
        product_id, products, limit
    )
    """
    Test API
    Parameters:
         product_id: 1
         limit: 2
    	
    Response body:
    [
  {
    "id": 2,
    "name": "Áo thun",
    "category": "ao",
    "rating": 4.8
  },
  {
    "id": 3,
    "name": "Áo khoác",
    "category": "ao",
    "rating": 4.2
  }
]
    """

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

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Model của một đơn hàng nhận vào
# 
class Order(BaseModel):
    id: int
    total: int
# Model dữ liệu API nhận vào
class AnomalyRequest(BaseModel):
    orders: list[Order]
    threshold: float

    
# Hàm phát hiện đơn bất thường

def detect_anomalies(orders, threshold):
    # Nếu không có đơn hàng
    if not orders:
        return []
    # Bước 1: Tính tổng tiền của tất cả các đơn hàng
    total_money = 0
    
    for order in orders:
        total_money = total_money + order.total
    # Bước 2: Đếm số lượng đơn hàng
    number_of_orders = len(orders)
    # Bước 3: Tính giá trị trung bình của các đơn hàng
    avg = total_money / number_of_orders
    # Bước 4: Tính mức tiền được coi là bất thường
    limit = threshold * avg
    # Bước 5: Tìm các đơn hàng bất thường
    result = []
    
    for order in orders:
        if order.total > limit:
            result.append(order)
    # Bước 6: Trả về kết quả cuối cùng của hàm
    return result

# Tạo API
@app.post("/orders/anomalies")
def get_anomalies(request: AnomalyRequest):
    return detect_anomalies(
        request.orders, 
        request.threshold
    )

    """Test API
    
case1:
    Request body: 
    
    {
  "orders": [
    {
      "id": 101,
      "total": 250000
    },
    {
      "id": 102,
      "total": 180000
    },
    {
      "id": 103,
      "total": 920000
    },
    {
      "id": 104,
      "total": 210000
    }
  ],
  "threshold": 2
}

	
Response body:

[
  {
    "id": 103,
    "total": 920000
  }
]

case2:
Request body:
{
  "orders": [
    {
      "id": 101,
      "total": 250000
    },
    {
      "id": 102,
      "total": 180000
    },
    {
      "id": 103,
      "total": 920000
    },
    {
      "id": 104,
      "total": 210000
    }
  ],
  "threshold": 3
}

	
Response body:
[]
    """
    
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
"""API có nhiệm vụ nhận role, resource, action từ request, sau đó gọi hàm để kiểm tra và trả về True/False"""
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Dữ liệu phân quyền
rbac = { 
 "admin": {
     "products": ["read", "create", "update", "delete"]
     }, 
 "seller": {
     "products": ["read", "create", "update"]
     }
 } 
# Hàm kiểm tra quyền

def can_access(role, resource, action, rbac):
    if role not in rbac: # Nếu role không tồn tại → False.
        return False
    if resource not in rbac[role]: # Nếu resource không tồn tại trong role → False.
        return False
    permissions = rbac[role][resource] # Nếu resource tồn tại trong role thì lấy danh sách quyền.
    
    if action in permissions: # Nếu action nằm trong danh sách quyền → True.
        return True
    return False # Nếu không nằm trong danh sách → False.

# Định nghĩa dữ liệu request

class AccessRequest(BaseModel):
    role: str
    resource: str
    action: str
    
# Tạo API kiểm tra quyền
@app.post("/check-access")
def check_access(request: AccessRequest):
    # Gọi hàm kiểm tra quyền
    result = can_access(
        request.role,
        request.resource,
        request.action,
        rbac
    )
    # Trả kết quả cho client
    return {
        "allowed": result
    }
    
    """Test API:
Case1:

Request body:
    {
  "role": "seller",
  "resource": "products",
  "action": "delete"
}
Response body:
{
  "allowed": false
}

Case2:

Request body:
    {
  "role": "seller",
  "resource": "products",
  "action": "update"
}
Response body:
{
  "allowed": true
}
    """
    
""" 
Câu 48:
          So sánh chiến dịch flash sale [Khó] (Tạo API) 
Bối cảnh:
         Flash sale service cần biết 
                sản phẩm nào bị gỡ, 
                sản phẩm nào mới  thêm 
                và sản phẩm nào giữ nguyên giữa hai phiên bản chiến dịch. 
Đề bài: 
        Viết hàm sale_diff(old_sale, new_sale) trả về dict gồm removed, added và  kept.
        removed là sản phẩm có ở old_sale nhưng không có ở new_sale, 
        added là  sản phẩm mới, 
        kept là sản phẩm có ở cả hai. 
Input mẫu: 

old_sale = {"SP001", "SP002", "SP003"} 
new_sale = {"SP002", "SP003", "SP004"} 

sale_diff(old_sale, new_sale)

Output mẫu: 
{"removed": {"SP001"}, "added": {"SP004"}, "kept": {"SP002",  "SP003"}}


    """
""" Ôn tập kiến thức về set
Trong Python, set = tập hợp.

Set là một kiểu dữ liệu dùng để chứa nhiều giá trị, nhưng mỗi giá trị chỉ xuất hiện 1 lần

Ví dụ: 
     numbers = {1, 2, 3, 4}
     numbers là một set gồm 4 phần tử: 1, 2, 3, 4
Nếu cho phần tử trùng nhau:
     numbers = {1, 2, 2, 3, 3, 3}
     print(numbers)
     Kết quả: {1, 2, 3}
     ====> Set tự động loại bỏ phần tử trùng.
Ví dụ:
              products = ["A", "B", "A", "C", "B"]

              unique_products = set(products)

              print(unique_products) 
              Kết quả: {"A", "B", "C"}
            ====> set(products):  
                         Lấy danh sách products và biến thành tập hợp để loại bỏ sản phẩm trùng.
3 phép toán của set dùng trong bài này:
A - B ===> Có ở A, không có ở B ===> removed
B - A ===> Có ở B, không có ở A ===> added
A & B ===> Có ở cả A và B ===> kept

===> các bài Python backend kiểu so sánh 2 danh sách, tìm phần tử thêm/xóa/giữ nguyên, set cực kỳ phù hợp.
Bài này không cần for, không cần if, cũng không cần dict để xử lý dữ liệu. Đây chính là ưu điểm của set: khi bài toán hỏi so sánh hai nhóm dữ liệu, hãy nghĩ ngay đến -, &, |
A - B    # Có trong A nhưng không có trong B
A & B    # Có trong cả A và B
A | B    # Gộp tất cả A và B
    """

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Định nghĩa dữ liệu đầu vào
class SaleRequest(BaseModel):
    old_sale: list[str]
    new_sale: list[str]
# Hàm xử lý nghiệp vụ
def sale_diff(old_sale, new_sale):
    # Chuyển list thành set
    old_sale = set(old_sale)
    new_sale = set(new_sale)
    # Sản phẩm có trong old_sale nhưng không có trong new_sale
    removed = old_sale - new_sale
    # Sản phẩm có trong new_sale nhưng không có trong old_sale
    added = new_sale - old_sale
    # Sản phẩm có trong cả old_sale và new_sale
    kept = old_sale & new_sale
    # Trả về kết quả dưới dạng dict
    return {
        "removed": removed,
        "added": added,
        "kept": kept
    }
    
# API
@app.post("/sale/diff")
def compare_sale(request: SaleRequest):
    result = sale_diff(
        request.old_sale,
        request.new_sale
        
    )
    return result
    """
    Test API

Schema của Edit Value trong Request body:
    {
  "old_sale": [
    "string"
  ],
  "new_sale": [
    "string"
  ]
}

Thực hiện test: 
Request body
{
  "old_sale": [
    "SP001",
    "SP002",
    "SP003"
  ],
  "new_sale": [
    "SP002",
    "SP003",
    "SP004"
  ]
}

Response body
{
  "removed": [
    "SP001"
  ],
  "added": [
    "SP004"
  ],
  "kept": [
    "SP002",
    "SP003"
  ]
}
    """

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
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Hàm phân nhóm khách hàng

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


# Model nhận dữ liệu từ API
class OrderCountsRequest(BaseModel):
    order_counts: dict[str, int]
# API
@app.post("/users/segment")
def segment_users_api(request: OrderCountsRequest):
    # Gọi hàm xử lý nghiệp vụ
    result = segment_users(request.order_counts)
    # Trả kết quả
    return result
    """
    Test API
    
Schema của Edit Value trong Request body:
{
  "order_counts": {
    "additionalProp1": 0,
    "additionalProp2": 0,
    "additionalProp3": 0
  }
}

Thực hiện test:

Request body:
{
  "order_counts": {
    "U001": 1,
    "U002": 7,
    "U003": 3,
    "U004": 5
  }
}

	
Response body:
{
  "one_time": [
    "U001"
  ],
  "repeat": [
    "U003"
  ],
  "vip": [
    "U002",
    "U004"
  ]
}

    """
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
from fastapi import FastAPI
from pydantic import BaseModel

# Tạo ứng dụng FastAPI
app = FastAPI()

# Định nghĩa dữ liệu đầu vào
class ConflictRequest(BaseModel):
    # Danh sách sản phẩm đang tham gia Flash Sale
    flash_sale_items: list[str]
    
    # Các campaign đang hoạt động
    # Key = tên campaign
    # Value = danh sách product_id
    active_campaigns: dict[str, list[str]]
# Hàm xử lý nghiệp vụ
def check_conflicts(falsh_sale_items, active_campaigns):
    # Nơi lưu sản phẩm bị xung đột
    conflicts = {}
    # Nơi lưu sản phẩm an toàn
    safe_items = set()
    
    # Vòng lặp ngoài: Duyệt từng sản phẩm trong Flash Sale
    for product_id in falsh_sale_items:
        # Khởi tạo 1 danh sách chứa campaign có sự tham gia của sản phẩm đang xét tới.
        campaigns = []
        # Vòng lặp trong: Duyệt từng campaign đang hoạt động.
        for campaings_name, products in active_campaigns.items():
            # Kiểm tra product_id có nằm trong campaign đang xét tới hay không.
            if product_id in products:
                # Nếu có thì thêm campaign vào danh sách campaign của sản phẩm đang xét duyêth.
                campaigns.append(campaings_name)
        # Sau khi khi kiểm tra xong tất cả các campaign
        if campaigns:
            # Lưu product_id và các campaign bị xung đột vào conflicts đã được khởi tạo trước đó
            # Key = product_id
            # Value = Danh sách các campaign chứa product_id đang được xét tới.
            conflicts[product_id] = campaigns
        # Nếu campaigns rỗng thì sản phẩm này an toàn. Thêm vào danh sách sản phẩm an toàn.
        
        else:
            safe_items.add(product_id)
    # Sau khi duyệt hết tất cả các sản phẩm trong Flash Sale, kiểm tra danh sách conflict
    # Nếu danh sách conflicts của danh sách Flash sale rỗng thì trả về False.
    # Danh sách conflicts có ít nhất một sản phẩm bị conflict thì trả về True 
    has_conflict = len(conflicts) > 0
    
    # Trả kết quả
    return {
        "has_conflict": has_conflict,
        
        "conflicts": {
    campaign: list(items)
    for campaign, items in conflicts.items()},
        
        "safe_items": list(safe_items)
    }
    
# Tạo API
@app.post("/campaigns/check-conflicts")
def check_conflicts_api(request: ConflictRequest):
    
    # Lấy dữ liệu từ request
    result = check_conflicts(
        request.flash_sale_items,
        request.active_campaigns
    )
    # Trả kết quả về cho client
    
    return result
            
    """Test API
    Schema của Edit Value trong Request body
    
{
  "flash_sale_items": [
    "string"
  ],
  "active_campaigns": {
    "additionalProp1": [
      "string"
    ],
    "additionalProp2": [
      "string"
    ],
    "additionalProp3": [
      "string"
    ]
  }
}

case1:
Request Body:

{
  "flash_sale_items": [
    "SP001",
    "SP003",
    "SP020"
  ],
  "active_campaigns": {
    "clearance": [
      "SP001",
      "SP005"
    ],
    "bundle": [
      "SP003",
      "SP007"
    ]
  }
}
	
Response body:

{
  "has_conflict": true,
  "conflicts": {
    "SP001": [
      "clearance"
    ],
    "SP003": [
      "bundle"
    ]
  },
  "safe_items": [
    "SP020"
  ]
}

case 2:
Request Body
{
  "flash_sale_items": [
    "SP001",
    "SP003",
    "SP020"
  ],
  "active_campaigns": {
    "clearance": [
      "SP001",
      "SP005"
    ],
    "bundle": [
      "SP001",
      "SP007"
    ]
  }
}
Responses Body:
{
  "has_conflict": true,
  "conflicts": {
    "SP001": [
      "clearance",
      "bundle"
    ]
  },
  "safe_items": [
    "SP003",
    "SP020"
  ]
}

Case 3:
Request body:

{
  "flash_sale_items": [
    "SP001",
    "SP003",
    "SP020"
  ],
  "active_campaigns": {
    "clearance": [
      "SP002",
      "SP005"
    ],
    "bundle": [
      "SP004",
      "SP007"
    ]
  }
}

Responses Body:
{
  "has_conflict": false,
  "conflicts": {},
  "safe_items": [
    "SP003",
    "SP001",
    "SP020"
  ]
}

    """