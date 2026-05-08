# Bài tập 1: Lọc sản phẩm còn hàng [LIST]
# Bối cảnh: Kho thương mại điện tử cần Lọc sản phẩm còn tồn kho trước khi hiển thị lên trang chủ
# Đề bài: Viết hàm filter_available() nhận danh sách sản phẩm và trả về các sản phẩm có stock > 0 và is_active == True.
# => Lọc ra sản phẩm thỏa mãn điều kiện: 1. stock > 0 (Còn hàng), 2. is_active == True (Đang được bán)

#input
products = [
    {"id": 1, "name": "Áo thun", "stock": 10, "is_active": True},
    {"id": 2, "name": "Quần jean", "stock": 0, "is_active": True},
    {"id": 3, "name": "Giày sneaker", "stock": 5, "is_active": False},
    {"id": 4, "name": "Nón baseball", "stock": 3, "is_active": True},
]
# Hàm lọc sản phẩm còn hàng
def filter_availabel(product):
    result =[] # Tạo 1 list rỗng để chứa kết quả là các sản phầm còn hàng.
    for product in products: # Xét từng sản phẩm trong danh sách hàng
        if product["stock"] > 0 and product["is_active"] == True: # Nếu sản phẩm thỏa  mãn 2 điều kiện 1. Còn hàng 2. Hiện vẫn đang bán
            result.append(product) # Thì thêm sản phẩm đó vào danh sách kết quả (Là list rỗng vừa tạo ở trên)
    return result # Trả về danh sách cuối cùng, là tập hợp những sản phẩm đáp ứng 2 điều kiện còn hàng
# Gọi hàm đã tạo ở trên, kiểm tra trong danh sách sản phẩm (input) xem sản phẩm nào đáp ứng các điều kiện trong hàm vừa tạo => In ra kết quả
print(filter_availabel(products))

# Bài tập 2: Tính tổng giá trị giỏ hàng [LIST]
# Bối cảnh: Checkout service cần tính tổng tiền của giỏ hàng trước khi hiển thị hóa đơn.
# Đề bài: Viết hàm cart_total() nhận vào cart và discount tính tổng tiền. Mỗi item có price và quantity. 
#         Áp dụng discount(%) nếu có (Mặc định là 10%)

# Dữ liệu input
cart = [
    {"name": "Áo thun", "price": 120000, "quantity": 2},
    {"name": "Quần dài", "price": 350000, "quantity": 1},
    {"name": "Tất", "price": 25000, "quantity": 3},
    
]

# hàm cart_total() nhận vào cart và discount tính tổng tiền
def cart_total(cart, discount = 10):
    total = 0 # Tổng tiền ban đầu bằng 0
    # Xét từng sản phẩm trong giỏ hàng
    for item in cart:
        price = item["price"]  # Lấy giá của sản phẩm tương ứng trong giỏ hàng
        quantity = item["quantity"] # Lấy số lượng của sản phẩm tương ứng trong giỏ hàng
        item_total = price * quantity # Tổng tiền của sản phẩm đó
        total = total + item_total #  Cộng vào tổng tiền của giỏ hàng
    # Tính số tiền được giảm giá
    discount_amount = total * discount/100
    # Tính tổng tiền giỏ hàng sau khi giảm giá
    final_total = total - discount_amount
    return final_total
print(cart_total(cart, discount = 10)) # Sử dụng hàm đã tạo để tính tổng tiền của giỏ hàng sau khi đã giảm giá => in ra kết quả cuối cùng


# Bài tập số 3
# Gợi ý sản phẩm liên quan
# Bối cảnh: Engine gợi ý cần trả về các sản phẩm cùng danh mục, trừ sản phẩm hiện tại, sắp xếp theo rating.
# Đề bài: Viết hàm nhận product_id và danh sách tất cả sản phẩm. Trả về tối đa limit sản phẩm cùng category, rating cao nhất.

#input
products = [
    {"id": 1, "name": "Áo polo", "category": "ao", "rating": 4.5},
    {"id": 2, "name": "Áo thun", "category": "ao", "rating": 4.8},
    {"id": 3, "name": "Áo khoác", "category": "ao", "rating": 4.2},
    {"id": 4, "name": "Quần jeans","category": "quan","rating": 4.7},
    {"id": 5, "name": "Áo sơ mi", "category": "ao", "rating": 4.6},
]

def related_products(product_id, products, limit=3):
    # Bước 1: Tìm sản phẩm hiện tại
    current_product = None
    for p in products:
        if p["id"] == product_id:
            current_product = p
            # print("Sản phẩm hiện tại:", current_product)
            break

    if current_product is None:
        return []

    # Bước 2: Lọc sản phẩm cùng category
    related = []
    for p in products:
        same_category = p["category"] == current_product["category"]
        not_itself = p["id"] != product_id

        if same_category and not_itself:
            # print("Thêm vào related:", p)
            related.append(p)

    #  IN SAU KHI LỌC XONG 
    # print("Trước khi sort:", related)

    # Bước 3: Sắp xếp
    related.sort(key=lambda x: x["rating"], reverse=True)

    # print("Sau khi sort:", related)

    # Bước 4: Lấy limit
    return related[:limit]
# Sử dụng hàm vừa tạo để lọc ra các sản phẩm đáp ứng điều kiện đề bài đưa ra. Dùng câu lệnh print để in ra kết quả.
print(related_products(1, products, 3))

# Bài tập 4
# 04. Phát hiện đơn hàng bất thường [LIST]
# Bối cảnh:
# Hệ thống chống gian lận cần phát hiện các đơn hàng có tổng tiền vượt ngưỡng bất thường.
# Đề bài:
# Viết hàm nhận list đơn hàng, tính giá trị trung bình, trả về những đơn có total > threshold * avg.
# Input:
# orders = [
# {"id": 101, "total": 250000},
# {"id": 102, "total": 180000},
# {"id": 103, "total": 920000},
# {"id": 104, "total": 210000},
# {"id": 105, "total": 195000},]
# detect_anomalies(orders, threshold=2.5)
# Output:
# [{"id": 103, "total": 920000}] # 920000 > 2.5 × 351000
def detect_anomalies(orders, threshold=2.5):
    # Tính tổng
    total_sum = 0 
    for order in orders: # Xét tất cả các đơn hàng trong danh sách đơn hàng.
        total_sum = total_sum + order["total"] # Cộng dồn total của từng đơn hàng vào tổng.
    # Tính trung bình
    avg = total_sum/len(orders)
    print("Giá trị trung bình: ", avg)
    # Tính ngưỡng bất thường
    limit = threshold * avg
    print("Ngưỡng bất thường: ", limit)
    # Lọc đơn bắt thường 
    anomalies = []
    for order in orders: # Xét tất cả các đơn hàng trong danh sách 
        if order["total"] > limit: # Nếu total của đơn hàng được xét đến lớn hơn ngưỡng limit => Đơn bất thường
           print("Đơn bất thường: ", order)
           anomalies.append(order) # Thêm đơn hàng bất thường vào danh sách đơn hàng bất thường đã được tạo sẵn trước đó anomalies = []
    return anomalies   
# Sử dụng hàm đã tạo để để tìm kiếm đơn bất thường với dữ liệu đầu vào
orders = [
    {"id": 101, "total": 250000},
    {"id": 102, "total": 180000},
    {"id": 103, "total": 920000},
    {"id": 104, "total": 210000},
    {"id": 105, "total": 195000},
]

print(detect_anomalies(orders, 2.5))

# Bài tập 5:
# 05. Xếp hạng sản phẩm bán chạy theo tuần [LIST]
# Bối cảnh:
# Bảng phân tích cần biết top N sản phẩm bán nhiều nhất trong tuần, kèm doanh thu.
# Đề bài:
# Viết hàm nhận list order_items (product_id, name, qty, price), trả về top N theo tổng qty giảm dần.
# Input:
# items = [
# {"product_id": 1, "name": "Áo thun", "qty": 5, "price": 120000},
# {"product_id": 2, "name": "Quần jean", "qty": 3, "price": 350000},
# {"product_id": 1, "name": "Áo thun", "qty": 8, "price": 120000},
# {"product_id": 3, "name": "Giày", "qty": 2, "price": 450000},
# {"product_id": 2, "name": "Quần jean", "qty": 4, "price": 350000},]
# top_selling(items, top_n=2)
# Output:
# [{"product_id": 1, "name": "Áo thun", "total_qty": 13, "revenue": 1560000},
#  Gom các item theo product_id
# Tính:
# total_qty (tổng số lượng bán)
# revenue (doanh thu = qty × price)
# Sắp xếp theo total_qty giảm dần
# Lấy top N

def top_selling(items, top_n=2):
    # Khởi tạo biến để lưu kết quả theo từng sản phẩm (dictionary)
    # Dạng: product_id => thông tin tổng
    summary = {} 
    # Duyệt từng item trong danh sách
    for item in items: 
        # Lấy thông tin từ item
        product_id = item["product_id"]
        product_name = item["name"]
        quantity = item["qty"]
        price = item["price"]
        
        #  Nếu sản phẩm chưa có trong summary thì tạo mới
        if product_id not in summary:
            summary[product_id] = {
                "product_id": product_id,
                "name": product_name,
                "total_qty": 0,
                "revenue": 0
            }
            
        # Cộng dồn số lượng
        summary[product_id]["total_qty"] = (
            summary[product_id]["total_qty"] + quantity
        )
        # Cộng dồn doanh thu (qty * price)
        summary[product_id]["revenue"] = (
            summary[product_id]["revenue"] + quantity * price
        )
        # dictionary: tra cứu nhanh theo id nhưng không thể sort trực tiếp dictionary theo value dễ dàng
        # Chuyển dictionary sang list để xử lý tiếp
        #  => chuyển sang list => sắp xếp, lọc, lấy top dễ dàng hơn
    result_list = list(summary.values())
    # Sắp xếp theo total_qty giảm dần
    result_list.sort(
        key=lambda product: product["total_qty"],
        reverse=True
    )
    # Lấy top N sản phẩm
    top_products = result_list[:top_n]
    return top_products
items = [
    {"product_id": 1, "name": "Áo thun", "qty": 5, "price": 120000},
    {"product_id": 2, "name": "Quần jean", "qty": 3, "price": 350000},
    {"product_id": 1, "name": "Áo thun", "qty": 8, "price": 120000},
    {"product_id": 3, "name": "Giày", "qty": 2, "price": 450000},
    {"product_id": 2, "name": "Quần jean", "qty": 4, "price": 350000},
]

print(top_selling(items, 2))

# Bài tập 6
# 06. Xây dựng catalog sản phẩm [DICT]
# Bối cảnh:
# API /products cần trả về catalog dạng dict để tra cứu nhanh theo product_id.
# Đề bài:
# Chuyển list sản phẩm thành 1 dict duy nhất có dạng { product_id: product_info } để có thể tra cứu
# theo id được nhanh nhất.
# Input:
# products = [
# {"id": "SP001", "name": "Áo thun basic", "price": 120000,
# "category": "ao"},
# {"id": "SP002", "name": "Quần jogger", "price": 280000,
# "category": "quan"},
# {"id": "SP003", "name": "Nón bucket", "price": 95000,
# "category": "phu_kien"},
# ]
# build_catalog(products)
def build_catalog(products):
    
    # Bước 1: tạo dictionary rỗng
    catalog ={}
    # Duyệt từng sản phẩm trong danh sách
    for product in products:
        # lấy id sản phẩm
        product_id = product["id"]
        # Thêm vào catalog
        catalog[product_id] = product
    return catalog
# Dùng hàm đã tạo để chạy thử với dữ liệu đầu vào
products = [
 {"id": "SP001", "name": "Áo thun basic", "price": 120000, "category": "ao"},
 {"id": "SP002", "name": "Quần jogger", "price": 280000, "category": "quan"},
 {"id": "SP003", "name": "Nón bucket", "price": 95000, "category": "phu_kien"},
]

catalog = build_catalog(products)

print(catalog)
print()

# Bài tập 7
# 07. Thống kê đơn hàng theo trạng thái [DICT]
# Bối cảnh:
# Dashboard quản lý cần biết số lượng đơn hàng theo từng trạng thái trong ngày.
# Đề bài:
# Viết hàm nhận list đơn hàng và đếm số lượng theo status.
# Input:
# statuses = ["confirmed", "pending", "shipped", "confirmed", "delivered",
# "pending", "cancelled", "confirmed", "shipped", "delivered"]
# count_by_status(statuses)
# Output:
# {"confirmed": 3, "pending": 2, "shipped": 2, "delivered": 2, "cancelled":1}
def count_by_status(statuses): 
    # Tạo dictionary rỗng
    result = {}
    # Xét duyệt từng status trong danh sách trạng thái đơn hàng
    for status in statuses:
         # Nếu chưa có thì tạo mới
         if status not in result:
             result[status] = 1
         else:
             # Nếu đã có thì tăng thêm 1
            result[status]   = result[status] + 1
    return result
# Sử dụng hàm đã tạo để chạy thử với dữ liệu đầu vào
statuses = [
 "confirmed", "pending", "shipped", "confirmed", "delivered",
 "pending", "cancelled", "confirmed", "shipped", "delivered"
]

print(count_by_status(statuses))
             
# Bài tập 8
# 08. Áp dụng mã giảm giá [DICT]
# Bối cảnh:
# Checkout service cần kiểm tra mã giảm giá hợp lệ và áp dụng discount theo loại.
# Đề bài:
# Viết hàm nhận cart_total và coupon_code, kiểm tra trong coupon_db và trả về dict kết quả gồm
# discount_amount, final_price, message. Nếu không có mã trong coupon_db, valid = False và trả về
# thông báo “Mã không tồn tại”
# Input:
# coupon_db = {
# "SALE20": {"type": "percent", "value": 20, "min_order": 200000},
# "SHIP50K": {"type": "fixed", "value": 50000, "min_order":
# 150000},
# "VIP30": {"type": "percent", "value": 30, "min_order": 500000},
# }
# apply_coupon(cart_total=350000, code="SALE20", coupon_db=coupon_db)             
def apply_coupon(cart_total, code, coupon_db):
    # Kiểm tra mã có tồn tại không?
    if code not in coupon_db:
        return{
            "discount_amount": 0,
            "final_price": cart_total,
            "message": "Mã không tồn tại"
        }
    # Lấy thông tin coupon
    coupon = coupon_db[code]
    coupon_type = coupon["type"]
    coupon_value = coupon["value"]
    min_order = coupon["min_order"]
    # Kiểm tra điều kiện đơn hàng
    if cart_total < min_order:
        return {
            "discount_amount": 0,
            "final_price": cart_total,
            "message": "Chưa đạt giá trị tối thiểu"
        }
        
    # Tính giảm giá
    if coupon_type == "percent":
        discount_amount = cart_total * coupon_value/100
    else:
        discount_amount = coupon_value
    final_price = cart_total - discount_amount
    return {
        "discount_amount": discount_amount,
        "final_price": final_price,
        "message": "Áp dụng mã thành công"
    }
    
# Dùng hàm mới tạo chạy với dữ liệu đầu vào
coupon_db = {
    "SALE20": {"type": "percent", "value": 20, "min_order": 200000},
    "SHIP50K": {"type": "fixed", "value": 50000, "min_order": 150000},
    "VIP30": {"type": "percent", "value": 30, "min_order": 500000},
}

print(apply_coupon(350000, "SALE20", coupon_db))
print()

# Bài tập 9
# 09. Tổng hợp báo cáo doanh thu theo ngày [DICT]Bối cảnh:
# Báo cáo cuối ngày cần tổng hợp doanh thu, số đơn và giá trị trung bình theo từng ngày.
# Đề bài:
# Viết hàm nhận list transaction (date, amount), trả về dict {date: {total, count, avg}}.
# Input:
# transactions = [
# {"date": "2024-01-15", "amount": 320000},
# {"date": "2024-01-15", "amount": 185000},
# {"date": "2024-01-16", "amount": 450000},
# {"date": "2024-01-15", "amount": 270000},
# {"date": "2024-01-16", "amount": 390000},
# ]
# daily_report(transactions)
def daily_report(transactions):

    # Bước 1: tạo dictionary kết quả
    report = {}

    # Bước 2: duyệt từng giao dịch
    for t in transactions:
        date = t["date"]
        amount = t["amount"]

        # Bước 3: nếu chưa có ngày thì tạo mới
        if date not in report:
            report[date] = {
                "total": 0,
                "count": 0
            }

        # Bước 4: cộng dồn
        report[date]["total"] = report[date]["total"] + amount
        report[date]["count"] = report[date]["count"] + 1

    # Bước 5: tính trung bình
    for date in report:
        total = report[date]["total"]
        count = report[date]["count"]
        report[date]["avg"] = total / count

    return report
transactions = [
{"date": "2024-01-15", "amount": 320000},
{"date": "2024-01-15", "amount": 185000},
{"date": "2024-01-16", "amount": 450000},
{"date": "2024-01-15", "amount": 270000},
{"date": "2024-01-16", "amount": 390000},
]
print(daily_report(transactions))
print()


# Bài tập 10
# 10. Quản lý phiên đăng nhập [DICT]
# Bối cảnh:
# Auth service quản lý phiên làm việc của người dùng bằng in-memory session dict.
# Đề bài:
# Viết class SessionStore với các method: create, get, delete. Session hết hạn sau timeout giây.
# Input:
# store = SessionStore(timeout=1800) # 30 phút
# store.create("user_123", {"name": "An", "role": "customer"})
# session = store.get("user_123")
# print(session)
# store.delete("user_123")
# print(store.get("user_123"))
import time
class SessionStore:
    def __init__(self, timeout):
        # timeout tính bằng giây
        self.timeout = timeout
        self.sessions = {}  # nơi lưu session
        # Tạo session
    def create(self, user_id, data):
        created_at = int(time.time())
        self.sessions[user_id] = {
                "user_id": user_id,
                "data": data,
                "created_at": created_at,
                "expires_at": created_at + self.timeout
            }
        
        # Lấy session
    def get(self, user_id):
        # Nếu session không tồn tại
        if user_id not in self.sessions:
            return None
        session = self.sessions[user_id]
        # Thời điểm hiện tại
        now = int(time.time())
        # Kiểm tra hết hạn
        if now > session["expires_at"]:
            # Xóa session hết hạn
            del self.sessions[user_id]
            return None
        # Nếu còn hạn => Trả về data
        return session
    # Xóa session
    def delete(self, user_id):
        if user_id in self.sessions:
            del self.sessions[user_id]
    # Chạy thử với dữ liệu đầu vào 
store = SessionStore(timeout=1800)  # 30 phút
store.create("user_123", {"name": "An", "role": "customer"})
session = store.get("user_123")
print(session)
store.delete("user_123")
print(store.get("user_123"))
print()

# Bài tập 11
# 11. Hệ thống phân quyền RBAC [DICT]
# Bối cảnh:
# Admin panel cần kiểm tra quyền thao tác của người dùng dựa trên role-based access control.
# Đề bài:
# Viết hàm kiểm tra user có quyền thực hiện action trên resource không, dựa vào bảng phân quyền
# RBAC.
# Input:
# rbac = {
# "admin": {"products": ["read","create","update","delete"],
# "orders": ["read","update","delete"]},
# "seller": {"products": ["read","create","update"],
# "orders": ["read"]},
# "customer": {"orders": ["read","create"]},
# }
# can_access("seller", "products", "delete", rbac) # False
# can_access("admin", "orders", "delete", rbac) # True
# can_access("customer", "products", "read", rbac) # False
# Output:
# False
# True
# False
def can_access(role, resource, action, rbac):
    #  Kiểm tra role tồn tại
    if role not in rbac:
        return False
    # Kiểm tra resource tồn tại trong role
    if resource not in rbac[role]:
        return False
    # kiểm tra action có trong danh sách quyền không
    if action not in rbac[role][resource]:
        return False
    return True
# Chạy thử với dữ liệu đầu vào
rbac = {
    "admin": {
        "products": ["read", "create", "update", "delete"],
        "orders": ["read", "update", "delete"]
    },
    "seller": {
        "products": ["read", "create", "update"],
        "orders": ["read"]
    },
    "customer": {
        "orders": ["read", "create"]
    },
}

print(can_access("seller", "products", "delete", rbac))    # False
print(can_access("admin", "orders", "delete", rbac))       # True
print(can_access("customer", "products", "read", rbac))    # False

# Bài 12
# 12. Tính phí vận chuyển theo vùng [DICT]
# Bối cảnh:
# Shipping service tính phí vận chuyển dựa trên tỉnh/thành phố, trọng lượng và giá trị đơn hàng.
# Đề bài:
# Viết hàm tính phí ship: miễn phí nếu đơn >= free_threshold, ngược lại tính theo zone_rate * weight_kg, có giá tối thiểu.
# Input:
# shipping_zones = {
# "HN": {"zone_rate": 15000, "free_threshold": 300000, "min_fee":15000},
# "HCM": {"zone_rate": 15000, "free_threshold": 300000, "min_fee":15000},
# "DN": {"zone_rate": 20000, "free_threshold": 350000, "min_fee": 20000},
# "other": {"zone_rate": 30000, "free_threshold": 500000, "min_fee":30000},
# }
# calc_shipping(city="DN", weight_kg=1.5, order_total=200000,zones=shipping_zones)
# Output:
# {"fee": 30000, "free_shipping": False, "message": "Phí ship đế n DN: 30,000đ"}
def calc_shipping(city, weight_kg, order_total, zones):
    # Nếu không có công ty trong zone thì dùng other
     if city not in zones:
         zone = zones["other"]
     else:
         zone = zones[city]
    # Miễn phí ship
     if order_total >= zone["free_threshold"]:
        return {
            "fee": 0,
            "free_shipping": True,
            "message": f"Đơn hàng được miễn phí ship đến {city}"
        }
    # Tính phí ship
    
     fee = zone["zone_rate"] * weight_kg
    # áp dụng phí tối thiểu
     if fee < zone["min_fee"]:
         fee = zone["min_fee"]
     return {
        "fee": int(fee),
        "free_shipping": False,
        "message": f"Phí ship đến {city}: {int(fee):,}đ"
     }
     # Dùng hàm đã tạo để chạy thử với dữ liệu đầu vào
shipping_zones = {
    "HN": {
        "zone_rate": 15000,
        "free_threshold": 300000,
        "min_fee": 15000
    },
    "HCM": {
        "zone_rate": 15000,
        "free_threshold": 300000,
        "min_fee": 15000
    },
    "DN": {
        "zone_rate": 20000,
        "free_threshold": 350000,
        "min_fee": 20000
    },
    "other": {
        "zone_rate": 30000,
        "free_threshold": 500000,
        "min_fee": 30000
    },
}

result = calc_shipping(
    city="DN",
    weight_kg=1.5,
    order_total=200000,
    zones=shipping_zones
)

print(result)   
print()

# Bài 13
# SET là một kiểu dữ liệu trong Python dùng để lưu một tập hợp các giá trị không trùng nhau.
# SET = danh sách không trùng + tra cứu cực nhanh

# 13. Kiểm tra sản phẩm trong wishlist [SET]
# Bối cảnh:
# Trang product detail cần biết nhanh sản phẩm hiện tại có trong wishlist của user không.
# Đề bài:
# Viết hàm kiểm tra một product_id có nằm trong wishlist set của user không/(Sản phẩm này có nằm trong danh sách yêu thích của user không?).
# Input:
# wishlist = {"SP001", "SP005", "SP012", "SP018", "SP024"}
# is_wishlisted("SP005", wishlist)
# is_wishlisted("SP999", wishlist)
# Output:
# True
# False
def is_wishlisted(product_id, wishlist): # Kiểm tra xem product_id có trong whishlist(danh sách yêu thích) của user hay không?
    # Xét duyệt từng phần tử trong wishlist
    for item in wishlist:
        # nếu tìm thấy product_id trong whishlist
        if item == product_id:
            return True
        # Nếu duyệt hết tất cả phần tử trong whishlist rồi mà vẫn không thấy product_id tương ứng
    return False
# Sử dụng hàm để chạy thử với dữ liệu đầu vào
wishlist = {"SP001", "SP005", "SP012", "SP018", "SP024"}

print(is_wishlisted("SP005", wishlist)) # True  <= Sử dụng hàm is_wishlist để tìm xem có sản phẩm SP005 trong wishlist(danh sách yêu thích của user) không?
print(is_wishlisted("SP999", wishlist)) # False <= <= Sử dụng hàm is_wishlist để tìm xem có sản phẩm SP999 trong wishlist(danh sách yêu thích của user) không?
print()

# Bài 14
# 14. Tìm sản phẩm chưa được xem [SET]
# Bối cảnh:
# Recommendation engine cần biết sản phẩm nào chưa được user xem để ưu tiên gợi ý.
# Đề bài:
# Trả về danh sách product_id chưa xuất hiện trong lịch sử xem của user.
# Input:
# all_products = {"SP001","SP002","SP003","SP004","SP005","SP006"}
# viewed_products = {"SP001","SP003","SP005"}
# get_unviewed(all_products, viewed_products)
# Output:
# {"SP002", "SP004", "SP006"}
def get_unviewed(all_products, viewed_products):
    result = set() # tạo tập hợp kết quả rỗng để chứa sản phẩm chưa xem
    
    for product in all_products: # Duyệt tất cả sản phẩm 
        if product not in viewed_products: # Kiểm tra từng sản phẩm xem đã có trong danh sách sản phẩm đã xem chưa? Nếu chưa xem thì giữ lại => Thêm vào kết quả
            result.add(product) # Thêm sản phẩm chưa xem vào tập hợp kết quả rỗng đã tạo trước đó.
            
    return result # Trả về kết quả cuối cùng sau khi đã xét duyệt hết
# Sử dụng hàm vừa tạo để chạy với dữ liệu đầu bài
all_products = {"SP001", "SP002", "SP003", "SP004", "SP005", "SP006"}
viewed_products = {"SP001", "SP003", "SP005"}

print(get_unviewed(all_products, viewed_products))
print()


# Bài tập 15
# 15. Lấy danh sách danh mục duy nhất [SET]
# Bối cảnh:
# Trang filter sản phẩm cần hiển thị tất cả danh mục có sẵn mà không bị trùng lặp.
# Đề bài:
# Từ list sản phẩm có nhiều trường, trích xuất tập hợp các category duy nhất.
# Input:
# products = [
# {"name": "Áo thun", "category": "ao"},
# {"name": "Quần jean", "category": "quan"},
# {"name": "Áo khoác", "category": "ao"},
# {"name": "Giày", "category": "giay"},
# {"name": "Áo polo", "category": "ao"},
# ]u
# nique_categories(products)
# Output:
# {"ao", "quan", "giay"}
# => trích xuất dữ liệu + loại bỏ trùng bằng SET
def unique_categories(products):
    result = set()# Tạo một tập hợp rỗng (set rỗng) để chứa dữ liệu sau này => SET: chứa nhiều giá trị, không cho phép trùng lặp, không có thứ tự cố định.
    
    for product in products: # Duyệt từng sản phẩm 
        category = product["category"] # lấy category
        result.add(category) # Thêm category vào SET => SET tự động loại trùng
    return result
# Sử dụng hàm để chạy với dữ liệu đầu bài
products = [
    {"name": "Áo thun", "category": "ao"},
    {"name": "Quần jean", "category": "quan"},
    {"name": "Áo khoác", "category": "ao"},
    {"name": "Giày", "category": "giay"},
    {"name": "Áo polo", "category": "ao"},
]

print(unique_categories(products))
print()

# Bài tập 16
# 16. Gợi ý sản phẩm cùng mua (cross-sell) [SET]
# Bối cảnh:
# Cross-sell engine tìm sản phẩm thường được mua kèm dựa trên lịch sử đơn hàng chung.
# Đề bài:
# Viết hàm nhận product_id và lịch sử đơn hàng, trả về set sản phẩm hay đi kèm nhưng CHƯA có
# trong giỏ hàng hiện tại.
# Input:
# order_history = [
# {"items": ["SP001","SP002","SP005"]},
# {"items": ["SP001","SP003"]},
# {"items": ["SP001","SP002","SP004"]},
# {"items": ["SP006","SP002"]},
# ]
# current_cart = {"SP001", "SP003"}
# cross_sell("SP001", order_history, current_cart)
# Output:
# {"SP002", "SP004", "SP005"} # SP003 đã trong giỏ, loại ra

def cross_sell(product_id, order_history, current_cart):
    result = set() # Tạo một tập hợp rỗng để lưu các sản phẩm gợi ý (Không trùng lặp)
    # Xét duyệt từng đơn hàng trong lịch sử mua hàng
    for order in order_history:
        items = order["items"] # Lấy danh sách sản phẩm trong đơn hàng đó
        # Kiểm tra đơn hàng này có chứa sản phẩm đang xét không?
        if product_id in items:
            for item in items: 
            # loại bỏ chính sản phẩm đang xét(không tự gợi ý chính nó)
             if item != product_id: # Duyệt từng sản phẩm trong đơn hàng đó
                # Thêm sản phẩm đi kèm vào kết quả
                 result.add(item)
    # Loại bỏ những sản phẩm đã có trong giỏ hàng hiện tại
    result = result - current_cart
    
    # Trả về danh sách sản phẩm gợi ý cuối cùng
    return result
# Chạy thử với data sẵn có
order_history = [
    {"items": ["SP001","SP002","SP005"]},
    {"items": ["SP001","SP003"]},
    {"items": ["SP001","SP002","SP004"]},
    {"items": ["SP006","SP002"]},
]

current_cart = {"SP001", "SP003"}

print(cross_sell("SP001", order_history, current_cart))    # Tìm đơn hàng có SP001 => Lấy tất cả sản phẩm trong đơn đó=> Duyệt từng sản phẩm: nếu khác SP001 → giữ lại, nếu là SP001 → bỏ => Loại sản phẩm đã có trong giỏ
print()    

# Bài 17
# 17. Phát hiện sản phẩm bị xóa khỏi flash sale [SET]
# Bối cảnh:
# Flash sale service cần biết sản phẩm nào bị gỡ khỏi chương trình so với phiên trước.
# Đề bài:
# So sánh 2 danh sách flash sale (cũ và mới), trả về các sản phẩm bị xóa, được thêm và còn lại.
# Input:
# old_sale = {"SP001","SP002","SP003","SP004","SP005"}
# new_sale = {"SP002","SP004","SP005","SP006","SP007"}
# sale_diff(old_sale, new_sale)
# Output:
# {
# "removed": {"SP001", "SP003"},
# "added": {"SP006", "SP007"},
# "kept": {"SP002", "SP004", "SP005"}
# }
def sale_diff(old_sale, new_sale):
     # Sản phẩm bị xóa khỏi flash sale (có trong old_sale nhưng không có trong new_sale )
     removed = old_sale - new_sale
     
     # Sản phẩm được thêm vào flash sale (có trong new_sale nhưng không có trong old_sale )
     added = new_sale - old_sale
     
     # Sản phẩm còn lại (Có trong cả new_sale và old_sale)
     kept = new_sale & old_sale
     
     return {
         "removed": removed,
         "added": added,
         "kept": kept
     }
     
     # chạy thử với dữ liệu đầu bài cho
old_sale = {"SP001","SP002","SP003","SP004","SP005"}
new_sale = {"SP002","SP004","SP005","SP006","SP007"}

print(sale_diff(old_sale, new_sale))
print()
 
# Bài 18
# 18. Lọc review hợp lệ theo người dùng đã mua [SET]
# Bối cảnh:
# Hệ thống review chỉ cho phép user đã mua sản phẩm mới được đánh giá, để chống
# Đề bài:
# Viết hàm lọc ra các review có user_id nằm trong danh sách đã mua hàng.
# Input:
# verified_buyers = {"U001", "U003", "U005", "U007"} => chỉ những user này mới được review hợp lệ
# reviews = [
# {"user_id": "U001", "rating": 5, "comment": "Rất tốt!"},
# {"user_id": "U002", "rating": 1, "comment": "Kém chất lượn
# {"user_id": "U003", "rating": 4, "comment": "Ưng ý"},
# {"user_id": "U004", "rating": 5, "comment": "Tuyệt vời"},
# ]
# filter_verified_reviews(reviews, verified_buyers)
# Output:
# [{"user_id": "U001", "rating": 5, "comment": "Rất tốt!"},
# {"user_id": "U003", "rating": 4, "comment": "Ưng ý"}]

def filter_verified_reviews(reviews, verified_buyers):
    # tạo danh sách chứa review hợp lệ
    result = []
    # Duyệt từng review trong danh sách
    for review in reviews:
        # lấy user_id của review được xét đến
        user_id = review["user_id"]
        # Kiểm tra xem user này có phải người đã mua hàng không?
        if user_id in verified_buyers:
            # Nếu là user đã mua hàng => review hợp lệ => Thêm vào kết quả
            result.append(review)
    return result
# Chạy thử với dữ liệu đề bài cho
verified_buyers = {"U001", "U003", "U005", "U007"}

reviews = [
    {"user_id": "U001", "rating": 5, "comment": "Rất tốt!"},
    {"user_id": "U002", "rating": 1, "comment": "Kém chất lượng"},
    {"user_id": "U003", "rating": 4, "comment": "Ưng ý"},
    {"user_id": "U004", "rating": 5, "comment": "Tuyệt vời"},
]

print(filter_verified_reviews(reviews, verified_buyers))
print()

# Bài 19
# 19. Phân tích hành vi mua hàng theo segment [SET]
# Bối cảnh:
# Marketing team cần biết người dùng nào là one-time, repeat hay VIP để gửi chiến dịch phù hợp.
# Đề bài:
# Phân loại user theo số đơn hàng: one_time (1 đơn), repeat (2–4 đơn), vip (≥5 đơn). Trả về dict 3
# nhóm.
# Input:
# order_counts = {
# "U001": 1, "U002": 7, "U003": 3, "U004": 1,
# "U005": 5, "U006": 2, "U007": 9, "U008": 4,
# }
# segment_users(order_counts)
# Output:
# {
# "one_time": {"U001", "U004"},
# "repeat": {"U003", "U006", "U008"},
# "vip": {"U002", "U005", "U007"}
# }

def segment_users(order_counts): # Hàm để phân nhóm user theo số đơn hàng
    # tạo 4 tập hợp để chứa user theo từng nhóm
    one_time = set()
    repeat = set()
    vip = set()
    no_order = set() # thêm nhóm cho trường hợp user k có đơn hàng nào
    
    # Duyệt từng user và số đơn hàng của user
    for user_id, count in order_counts.items():
        
        # Trường hợp không có đơn hoặc dữ liệu lỗi
        if count is None or count == 0:
            no_order.add(user_id)
            
        # User có 1 đơn => one_time
        elif count == 1:
            one_time.add(user_id)
        
        # User có từ 2 đến 4 đơn => repeat
        elif 2 <= count <= 4:
            repeat.add(user_id)
            
        # User có từ 5 đơn trở lên    => thuộc nhóm VIP
        else:
            vip.add(user_id)
    # Trả về kết quả dạng dict
    return {
        "no_order": no_order,
        "one_time": one_time,
        "repeat": repeat,
        "vip": vip
    }
# Dùng hàm để chạy thử với dữ liệu đầu bài cho và in ra kết quả
order_counts = {
    "U001": 1, "U002": 7, "U003": 3, "U004": 1,
    "U005": 5, "U006": 2, "U007": 9, "U008": 4,
}

print(segment_users(order_counts))
print()

# Bài 20
# 20. Kiểm tra xung đột kho hàng trong flash sale [SET] => kiểm tra “sản phẩm đã bị dùng trong campaign khác chưa” => sản phẩm nào bị trùng campaign, sản phẩm nào an toàn => Với mỗi sản phẩm trong flash sale: đi kiểm tra nó nằm trong campaign nào
# Bối cảnh:
# Trước khi bắt đầu flash sale, hệ thống kiểm tra sản phẩm có bị xung đột với các chiến dịch đang
# chạy không.
# Đề bài:
# Viết hàm kiểm tra các sản phẩm trong flash_sale_items có bị trùng với chiến dịch đang hoạt động
# không, báo cáo chi tiết.
# Input:
# Các campaign đang chạy:
# active_campaigns = {
# "clearance": {"SP001","SP005","SP009"},
# "bundle_deal": {"SP003","SP007","SP011"},
# "new_arrival": {"SP013","SP015"},
# }
# Flash sale mới:
# flash_sale_items = {"SP001","SP003","SP007","SP020","SP025"}
# check_conflicts(flash_sale_items, active_campaigns)
# Output:{
# "has_conflict": True,
# "conflicts": {"SP001": ["clearance"],
# "SP003": ["bundle_deal"],
# "SP007": ["bundle_deal"]},
# "safe_items": {"SP020", "SP025"}
# }

def check_conflicts(flash_sale_items, active_campaigns):
    
    # Lưu sản phẩm bị xung đột theo campaign
    conflicts = {}
    
    # Lưu sản phẩm an toàn (không bị xung đột)
    safe_items = set()
    
    # Duyệt từng sản phẩm trong flash sale
    for item in flash_sale_items:
        # Biến đánh dấu có conflict hay không?
        found = False
        
        # Kiểm tra từng campaign
        for campaign_name, products in active_campaigns.items():
            
            # Nếu sản phẩm nằm trong campaign khác đang chạy
            if item in products:
                # Thêm item đó vào biến conflicts = {}
                if item not in conflicts:
                   conflicts[item] = []   
                conflicts[item].append(campaign_name)
                found = True
        # Nếu không thuộc campaign nào => an toàn
        if not found:
            safe_items.add(item)
    return {
        "has_conflict": len(conflicts) > 0,
        "conflicts": conflicts,
        "safe_items": safe_items
    }
    
    # Chạy thử với dữ liệu đề bài cho
active_campaigns = {
    "clearance": {"SP001","SP005","SP009"},
    "bundle_deal": {"SP003","SP007","SP011"},
    "new_arrival": {"SP013","SP015"},
}

flash_sale_items = {"SP001","SP003","SP007","SP020","SP025"}

print(check_conflicts(flash_sale_items, active_campaigns))
  

    

    