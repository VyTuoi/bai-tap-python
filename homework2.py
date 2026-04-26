# Bài tập làm quen với Vòng lặp, Function
# Đóng vai trò một Backend Developer, xây dựng các chức năng cơ bản cho hệ thống như:
# Xử lý đơn hàng
# Tính toán chi phí
# Kiểm tra điều kiện người dùng
# Áp dụng logic nghiệp vụ (business logic)

# Bài tập 1: In danh sách sản phẩm (Có index)
# Dùng for
# In theo format
# 1. Áo
# 2. Quần 
# ....

products = ["Áo", "Quần", "Giầy", "Mũ"]
for item in range(len(products)):
    print(f"{item+1}. {products[item]}") # f"" nhét biến vào chuỗi 

# Bài tập 2: 
# Tính tổng tiền giỏ hàng

prices = [100000, 200000, 150000]
total = 0 
for price in prices:
    total = total + price
print("Tổng tiền: ", total, "VND")

#  Bài tập 3
# Bài 3: Đếm sản phẩm giá cao > 300000 (Đếm số phần tử > 300000)

prices = [100000, 500000, 700000, 200000]
count = 0
for price in prices:
    if price > 300000:
        count = count + 1
print("Sản phẩm giá cao: ", count)

#Bài 4: Tìm giá lớn nhất

prices = [100000, 500000, 700000, 200000]
max_price = prices[0] # Lấy phần tử đầu tiên (ở vị trí 0) trong list giá  làm giá trị lớn nhất, max_price = 100000
for price in prices:
    if price > max_price:
        max_price = price
print("Giá cao nhất: ", max_price)

# Bài 5: Tổng số chẵn

numbers = [1, 2, 3, 4, 5, 6]
total = 0
for i in numbers:
    if i % 2 == 0:
        total = total + i
print("Tổng chẵn: ", total)

# Bài 6: Bảng cửu chương mini
# Yêu cầu:
# ● In từ 1 → 5 
# ● Format: 2 x 1 = 2 
#           2 x 2 = 4 
# …Gợ i ý: sử dụng 2 vòng lặp lồng nhau

for i in range(1, 6): # range(1, 6) tạo ra dãy số từ 1 đến n-1 => Dãy số 1, 2, 3, 4, 5.
    # Lần 1 lấy i =1, lần 2 lấy i =2, .... lần 5 lấy i = 5 => Mỗi i là một bảng cửu chương.
    print(f"Bảng {i}:") # In tiêu đề bảng cửu chương: Bảng 1, 2, 3, 4, 5. f"" giúp chèn biến i vào chuỗi.
    for j in range(1, 6): # Vòng lặp bên trong. j chạy từ 1 đến 5
        print(f"{i} x {j} = {i*j}") # In phép nhân
    
    
  # Bài 7: Kiểm tra n có phải số nguyên tố không?
  # Số nguyên tố là các số tự nhiên lớn hơn 1, chỉ chia hết cho 1 và chính nó.
  # Ví dụ: 2, 3, 5, 7, 11, 13, 17, 19, .... 
  # Số nguyên tố chỉ có đúng hai ước số dương là 1 và chính nó. Số 0 và 1 không phải là số nguyên tố
    n = 17
    is_prime = True # Giả sử n là số nguyên tố 
for i in range(2, n): # Kiểm tra từ 2 đến n-1
      if n % i == 0: # nếu n chia hết cho 1 giá trị vào đó khác 1 và chính nó => Không phải số nguyên tố => Dừng.
          is_prime = False
          break
if is_prime:
        print(f"{n} là số nguyên tố")
    
else:
        print(f"{n} không phải là số nguyên tố")
    
    # Bài 8 số lần xuất hiện của phần tử A trong mảng
orders = ["A","B", "A", "C", "A"]
count = 0
for order in orders:
        if order == "A":
            count = count + 1
            
print("A xuất hiện: ", count, "lần")

# Bài 9: Hàm tính tổng tiền
def calculate_total(price, quannity): # def = từ khóa để khai báo hàm. calculate_total => Tên hàm. (price, quannity) =  tham số, đầu vào.
    return price*quannity # Tính ra kết quả, trả ra kết quả theo tham số được gán vào hàm calculate_total với công thức price*quannity
total = calculate_total(50000, 3)
print("Tổng tiền: ", total)

# Bài 10: Kiểm tra đăng nhập
def check_login(is_logged_in):
    if is_logged_in:
        return "Đã đăng nhập"
    else:
        return "Chưa đăng nhập"
print(check_login(True)) 
print(check_login(False))

# Bài 11: Hàm giảm giá
def apply_discount(price, percent):
    new_price = price -(price*percent/100) #giá mới(giá sau giảm) = giá gốc - (giá gốc × % giảm)
    return new_price # Trả giá mới ra ngoài
print(apply_discount(5000000, 50)) # Ví dụ: price = 5000000 percent = 50% => Giá mới = 5000000 - (5000000*50/100)

# Bài 12: Hàm free ship
def is_free_shipping(order_value): # Giá trị đầu vào của hàm is_free_shipping là order_value (giá trị đơn hàng)
    if order_value >= 500000: # kiểm tra giá trị đơn hàng. Nếu giá trị đơn hàng lớn hơn hoặc bằng 500000 thì sẽ được Free ship. Nhỏ hơn 500000 sẽ không được giảm giá.
        return True # Trả kết quả True => Được Free ship
    else:
        return False # Trả kết quả False => Không được free 
    
result = is_free_shipping(400000) # Gọi hàm,dùng hàm is_free_shipping xét điều kiện giảm giá với order_value = 400000
print("Free ship: ", result) 

# Bài 13: Phân loại khách hàng
def classify_customer(total_spent): # Giá trị đầu vào của hàm classify_customer là total_spent(tổng tiền khách đã chi)
     if total_spent >= 5000000: # Nếu tổng tiền khách đã chi >= 5000000 thì phân loại khách hàng là VIP
         return "VIP"
     elif total_spent >= 2000000:  # Nếu không thuộc khách vip và  tổng tiền khách đã chi >= 2000000 thì phân loại khách hàng là Gold
         return "Gold"
     else:
         return "Normal" # Ngược lại với 2 điều kiện trên thì trả kết quả là normal
print(classify_customer(10000000)) # Gọi hàm classify_customer và trả kết quả ra màn hình đối với các trường hợp khách chi số tiền là 10000000, 3000000, 10000
print(classify_customer(3000000))
print(classify_customer(1000000))

# Bài tập 14: Validate email
# Yêu cầu email cần phải có @ và . => True => In: Email hợp lệ
def is_valid_email(email):
    if "@" in email and "." in email:
        return True
    else:
        return False
    
result = is_valid_email("tuyendung@gmail.com")
if result:
    print("Email hợp lệ")
else:
    print("Email không hợp lệ")
    
# Bài tập 15: Tổng doanh thu
# orders = [100000, 200000, 300000]
# ● Viết function: def total_revenue(orders):
# ● Dùng loop
# ● Return tổng
def total_revenue(orders): # tạo hàm total_revenue để nhận giá trị đầu vào là danh sách đơn hàng
    total = 0 # Khởi tạo biến dùng để cộng dồn giá trị doanh thu
    for order in orders: # Lặp qua từng quá trị trong danh sách đơn hàng
        total = total + order # Cộng dồn các giá trị trong danh sách đơn hàng với total được khởi tạo trước đó. Lần 1: 0 + 100000 = 100000 => lần 2: 100000 + 200000 = 300000 =>  lần 3:  300000 + 300000 = kết quả cuối cùng
    return total # Trả kết quả tổng doanh thu sau khi cộng dồn ra ngoài hàm
orders = [100000, 200000, 300000]
print("Tổng doanh thu: ", total_revenue(orders)) # Gọi hàm để tính tổng doanh thu danh sách orders và in ra kết quả tương ứng

# Bài tập bài 16: Lọc giá cao
#prices = [100000, 500000, 700000, 200000] 
# def filter_prices(prices): 
# Yêu cầu: ● Function trả về list > 300000 
# ● Ví dụ: return [500000, 700000]


def filter_prices(prices):
    result = [] # Tạo sẵn list rỗng để chứa kết quả  các số lớn hơn 300000
    for price in prices: # Chạy từ đầu list đến cuối list để xét các giá trị price cụ thể có đúng với điều kiện bên dưới không
        if price > 300000:
            result.append(price) # Nếu giá trị price cụ thể trong list prices  thỏa mãn điều kiện > 300000 => Thêm vào list rỗng đã tạo trước đó result = [] => Tiếp tục xét các giá trị tiếp theo và làm tương tự cho đến khi xét hết tất cả các giá trị  trong list.
    return result # Trả list kết quả ra ngoài hàm
prices = [100000, 500000, 700000, 200000] 
print(filter_prices(prices))

# Bài 17: Đếm đơn hợp lệ
# orders = [100000, 0, 200000, -50000]
# def check_orders(orders):
# Yêu cầu:
# ● Đơn có giá trị > 0
# ● return số lượng đơn hợp lệ
orders = [100000, 0, 200000, -50000]
def check_orders(orders):
    count = 0 # Tạo biến để đếm số đơn hợp lệ. Giá trị khởi tạo bằng không.
    for  order in orders: # Xét từng giá trị trong list đơn xem có hợp lệ không. Nếu hợp lệ, biến count vừa được khởi tạo ở trên sẽ được cộng thêm 1. Xét cho đến khi hết danh sách thì dừng lại và trả kết quả sau khi cộng dồn các lần hợp lệ.
        if order > 0:
            count = count + 1
    return count # Trả về số đơn hợp lệ sau khi đã xét tất cả ác các giá  trị.
print("Số đơn hợp lệ: ", check_orders(orders))  

# Bài 18: Tổng sau giảm giá
# prices = [100000, 200000, 300000]
# Yêu cầu:
# ● Mỗi sản phẩm giảm 10%
# ● Tính tổng cuối
# ● Viết function riêng:
# def apply_discount(prices):
prices = [100000, 200000, 300000]
def apply_discount(price): # Hàm tính giảm giá
    return price * 0.9 # giảm 10%  
def total_after_discount(prices): # Hàm tính tổng sau giảm giá.
    total = 0
    for price in prices: # Xét từng giá trong prices 
        new_price = apply_discount(price) # Gọi hàm giảm giá để tính giá mới
        total = total + new_price # Cộng dồn giá mới của từng loại vào total
    return total # trả về kết quả total sau khi cộng dồn hết các giá mới 
print("Tổng sau giảm: ", total_after_discount(prices))

# Bài 19: Lọc khách VIP
# cart = [200000, 1500000, 800000]
# def vip_checker(cart):
# Yêu cầu:
# ● Nếu khách mua >= 3tr thì được coi là khách VIP
# ● Trả về True, ngược lại trả về False
cart = [200000, 1500000, 800000]
def vip_checker(cart):
    total = 0 # Khởi tạo biến total để lưu tổng giá trị của giỏ hàng. Giá trị khởi tạo = 0
    for price in cart: # Duyệt từng price trong giỏ hàng
        total = total + price # cộng từng phần tử trong giỏ hàng.  Tổng mới = Tổng khởi tạo + từng price trong giỏ hàng.
    if total >= 3000000: # So sánh với giá trị điều kiện 3000000
        return True # thỏa mãn điều kiện => Trả về True
    else:
        return False # Ngược lại, nếu không thỏa mãn điều kiện thì trả về False.
print(vip_checker(cart)) # Gọi hàm check khách vip =>  kiểm tra giá trị tổng của cart => in ra kết quả tương ứng.

# Bài 20: Hệ thống thanh toán (mini backend)
# cart = [100000, 200000, 150000]
# balance = 500000
# Yêu cầu:
# ● Viết function: def checkout(cart, balance):
# Logic:
# 1. Tính tổng tiền
# 2. Nếu đủ tiền: return {“status”: “Thanh toán thành công”, “Số dư còn lại”:
# xxx}
# 3. Nếu không đủ: return {“status”: “Không đủ tiền”, “Số dư còn lại”: xxx}

cart = [100000, 200000, 150000]
balance = 500000
def checkout(cart, balance):
    total = 0 # Khởi tạo biến lưu trữ giá trị tổng tiền của giỏ hàng. Giá trị khởi tạo bằng 0
    for price in cart: # tính tổng tiền của giỏ hàng cần thanh toán
        total = total + price
    if balance >= total: # Kiểm tra số dư, đối chiếu số dư tài khoản với tổng tiền của đơn hàng.
        return {
            "status": "Thanh toán thành công", 
               "Số tiền còn lại là":balance - total 
               } # Nếu đủ tiền (số dư tài khoản >= số tiền hàng cần thanh toán) => Trừ tiền => Tính lại số dư sau khi thanh toán
        
    else: #Nếu không đủ tiền. => Không thanh toán thành công. Không trừ → giữ nguyên balance
        return {
            "status": "Không đủ tiền",
            "Số dư còn lại": balance
        }
print(checkout(cart, balance))

    
