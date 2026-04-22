 # Bài 1
 # Viết backend cho chức năng tạo đơn hàng
 # Khởi tạo các giá trị 

price = 120000
quantity = 3
total = price*quantity
print("Tổng tiền: ",total, "VND")
# Bài 2
# Áp dụng giảm giá sản phẩm
# Xử lý giảm giá cho các sản phẩm
# Khởi tạo các giá trị
price = 500000
discount_percent = 10
discount_amount = price*discount_percent/100
print("Số tiền được giảm: ", discount_amount, "VND")
print("Giá cuối cùng sau khi giảm: ",price-discount_amount, "VND")
#Bài 3
# Tính lương nhân viên
# Viết backend cho hệ thống quản lý nhân sự
# Tính tổng lương tháng = lương ngày * số ngày làm việc
salary_per_day = 300000
working_days = 22
salary_per_month = salary_per_day*working_days
print("Lương của tháng: ", salary_per_month, "VND")
# Bài 4
# Tính phí vận chuyển
# Xử lý phí ship cho đơn hàng
# Tính tổng chi phí vận chuyển = khoảng cách * giá vận chuyển mỗi km

distance_km = 12
cost_per_km = 5000
total_shipping_cost = distance_km*cost_per_km
print("Tổng chi phí vận chuyển là: ", total_shipping_cost, "VND")

# Bài 5
# Kiểm tra dung lượng lưu trữ
# tính dung lượng còn lại = Tổng - Lượng đã dùng

total_storage = 256
used_storage = 180
remaining_storage = total_storage - used_storage
print("Dung lượng còn lại là: ", remaining_storage)

# Bài 6
# Kiểm tra khả năng thanh toán
#Viết logic kiểm tra trước khi thanh toán đơn hàng
balance = 200000 # Số tiền đang có trong tài khoản
item_price = 150000 # Tiền hàng cần trả
if item_price <= balance:
    print("Thanh toán thành công")
else:
    print("Bạn không đủ tiền trong tài khoản")
    
#Bài tập số 7
#Kiểm tra xem đơn hàng có được miễn phí ship hay không?

order_value = 250000
if order_value >= 200000:
    print("Đơn hàng được miễn chi phí vận chuyển")
    
else:
    print("Đơn hàng không đủ điều kiện để được miễn phí chi phí vận chuyển")

# Bài tập 8
# Xây dựng hệ thống phân quyền người dùng
# Kiểm tra người dùng có quyền admin hay không?
is_logged_in = True
is_admin = False
if is_logged_in and is_admin== True:
    print("User có quyền admin")
else:
    print("User không có quyền admin")    



# Bài tập 9
# Kiểm tra giờ làm việc
hour = 14
if hour >= 9 and hour <= 18:
    print("Đang trong giờ làm việc")
    
else:
    print("Không trong giờ làm việc")
    
# Bài tập 10
# Kiểm tra email hợp lệ(Cơ bản)
#Thực hiện validate dữ liệu người dùng
# Email hợp lệ nếu chứa @ và .
email = "user@gmail.com"
if "@" in email and "." in email:
    print("Email hợp lệ")
else:
    print("Email không hợp lệ")
    
# Bài tập 11
# Tính chi phí vận chuyển theo giá trị đơn hàng
# Viết backend cho hệ thống ecommerce
order_value = 180000
total = order_value
if order_value >= 200000:
    print("Đơn hàng được miễn phí ship. Tổng số tiền phải trả là: ", total)
else:
    print("Phí ship cho đơn hàng của bạn là 30000 VND. Tổng số tiền phải trả là: ", total + 30000)
    
# Bài tập 12
# Tính thưởng của nhân viên
# Xử lý hệ thống đánh giá hiệu suất
performance_score = 8.2
if performance_score >= 9:
    print("Số tiền được thưởng là: 5000000 VND")
elif 9 > performance_score >= 7:
    print("Số tiền được thưởng là: 2000000 VND")
else:
    print("Không được thưởng")    
    
# Bài tập 13
# Mapping trạng thái đơn hàng
# Xử lý trạng thái đơn hàng từ database
# Kiểm tra status_code và in ra giá trị tương ứng theo quy tắc
status_code = 2
if status_code == 1:
    print("Pending")
elif status_code == 2:
    print("Shipping")
elif status_code == 3:
    print("Dilivered")
else:
    print("Unknown")

# Bài tập 14
# Tính giá vé theo độ tuổi
# Viết hệ thống bán vé
age = 15
if age < 12:
    print("Giá vé là : 50000 VND")
elif 18 >= age >= 12:
    print("Giá vé là: 70000 VND")
else:
    print("Giá vé là: 100000 VND")
    
# Bài tập 15
# Phân loại khách hàng
# Xây dựng hệ thống CRM
total_spent = 1200000
if total_spent >= 1000000:
    print("VIP")
elif 1000000 > total_spent >= 500000:
    print("Gold")
else:
    print("Normal")

# Bài tập 16
# Xây dựng hệ thống billing 
# 0–50: 1678
# 51–100: 1734
# 101–200: 2014
# Tính tiền điện theo bậc
kwh = 135
electricity_bill = 0
if 0 <= kwh <= 50:
    electricity_bill = kwh*1678
    
elif  51 <= kwh <= 100:
    electricity_bill = 1678*kwh + (kwh-50)*1734
 
else:
    electricity_bill = 1678*50 + 50*1734 + (kwh-100)*2014
    
print("Số tiền  điện phải thanh toán là: ", electricity_bill, "VND")
    

# Bài tập 17
# Tính lương có thưởng KPI
# Xử lý bảng lương nâng cao
base_salary = 10000000
kpi = 0.85
if kpi >= 0.9:
    print("Lương của bạn là: ", base_salary + base_salary * 0.3, "VND")
    
elif 0.8 <= kpi < 0.9:
    print("Lương của bạn là: ", base_salary + base_salary*0.1, "VND")
    
else:
    print("Lương của bạn là: ", base_salary, "VND")


# Bài tập 18
# Tính giá taxi
# Viết logic tính cước cho ứng dụng gọi xe
# 1km đầu: 15000, 2-10km: 12000/km, 10km: 10000/km
distance_km = 12
taxi_cost = 0
if distance_km <= 1:
    taxi_cost = 15000
elif 2 <= distance_km <= 10:
    taxi_cost = 15000 + ((distance_km -1)*12000)
else:
    taxi_cost = 15000 + 9*12000 + ((distance_km - 10)*10000)
    
print("Số tiền taxi phải trả là: ",taxi_cost, "VND" )

# Bài tập 19
# Xây dựng hệ thống fintech
# Được vay nếu income >= 10000000, debt <= 50% income
income = 15000000
debt = 3000000
if income >= 10000000 and debt <= income*0.5:
    print("Đủ điều kiện vay")
    
else:
    print("Không đủ điều kiện vay")
    
# Bài tập 20
# Áp dụng điều kiện giảm giá
# Xử lý logic thanh toán
# Nếu là member => giảm 10%, sau đó trừ voucher. Đảm bảo giá cuối cùng không âm.
price = 1000000
is_member = True
voucher = 100000
total = 0
voucher = 100000
if is_member:
      total = price - price*0.1 - voucher
else:
    total = price - voucher
    
print("Số tiền cần thanh toán là: ", total, "VND")

      
      

    
 
    

    

    
    


    
