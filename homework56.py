# Phần 1: Lý thuyết

# Câu 1: 
#     Phân biệt giữa Class và Object 
# Hãy giải thích sự khác biệt giữa Class (Lớp) và Object (Đối tượng).
# Cho ví dụ cụ thể trong bối cảnh hệ thống thương mại điện tử 
# (ví dụ: Class Product và các object của sản  phẩm cụ thể). 

# Class (Lớp) là gì?

# Class là bản thiết kế (khuôn mẫu), định nghĩa các thuộc tính và phương thức của một loại đối tượng.
# Object là một đối tượng cụ thể được tạo từ Class, chứa dữ liệu thực tế và có thể sử dụng các phương thức mà Class định nghĩa.

# Ví dụ trong hệ thống thương mại điện tử:

# Product là Class mô tả một sản phẩm với các thuộc tính như id, name, price, stock.
# Dưới đây là hai Object cụ thể, mỗi object có dữ liệu riêng nhưng đều được tạo từ cùng một Class Product:
# iphone = Product(1, "iPhone 16", 25000000, 15) 
# macbook = Product(2, "MacBook Air", 32000000, 8) 

# class Product:
#     def __init__(self, id, name, price, stock):
#         self.id = id
#         self.name = name
#         self.price = price
#         self.stock = stock
#     def show(self):
#         print(f"{self.name} - {self.price} - {self.stock}")
# # Tạo object cụ thể dựa trên  các thuộc tính đã định nghĩa trong class Product đã tạo ở trên.
# # Mỗi object sẽ bao gồm các thông tin:
# # id
# # name
# # price
# # stock
# Product1 = Product(1, "iPhone 16", 25000000, 20)
# Product2 = Product(2, "MacBook Air", 32000000, 15)
# Product3 = Product(3, "Samsung S25", 22000000, 0)
# # Gọi phương thức def show(self): để in ra các thông tin đã được định nghĩa trong hàm show() bao gồm tên, giá và tồn kho của từng object

# Product1.show()
# Product2.show()
# Product3.show()

# # Kết quả:
# # iPhone 16 - 25000000 - 20
# # MacBook Air - 32000000 - 15
# # Samsung S25 - 22000000 - 0

# #  => Ở đây Product là class. Đã định nghĩa rằng các object cụ thể được tạo ra sẽ bao gồm các thuộc tính:
# #           id, name, price, stock
# # Product1, Product2, Product3 là 3 object cụ thể được tạo ra dựa trên class Product. 
# # Thông tin cụ thể của 3 object đã tạo là:
# #                   Product1: id = 1, name = iPhone 16, price = 25000000, stock = 20
# #                   Product2: id = 2, name = MacBook Air, price = 32000000, stock =  15
# #                   Product3: id = 3, name= Samsung S25,  price = 22000000, stock = 0
# #                   => object cụ thể được tạo ra có đầy đủ  các thuộc tính:
# #           id, name, price, stock
# #         có thể gọi hàm(phương thức) def show(self): để show ra các thông tin name, price, stock của từng object đã tạo

# # Bài tập 2
# # Giải thích tác dụng của hàm __init__() trong Python.
# # Tham số self là gì và tại sao nó  luôn là tham số đầu tiên của mỗi phương thức?
# # Viết ví dụ với class Product (sản  phẩm)

# # 1. Hàm __init__() là gì?
# # __init__() là hàm khởi tạo (constructor) của một class
# # Nó được tự động gọi khi tạo một object mới từ class
# # Mục đích của hàm khởi tạo __init__() là:
# #                         Khởi tạo giá trị ban đầu cho các thuộc tính của object
# #                         Giúp mỗi object có dữ liệu riêng ngay khi được tạo
# # Ví dụ:
# class Product:
#     def __init__(self, id, name, price, stock):
#         self.id = id
#         self.name = name
#         self.price = price
#         self.stock = stock
# # Khi tạo object:
# Product1 = Product(1, "iPhone 16", 25000000, 20)
# Product2 = Product(2, "MacBook Air", 32000000, 15)
# Product3 = Product(3, "Samsung S25", 22000000, 0)
# # Python sẽ tự động gọi __init__ mà không cần gọi thủ công nữa.
# Product.__init__(Product1, 1, "iPhone 16", 25000000, 20)
# Product.__init__(Product2, 2, "MacBook Air", 32000000, 15)
# Product.__init__(Product3, 3, "Samsung S25", 22000000, 0)

# # 2. Tham số self là gì?
# # self là tham chiếu đến chính object đang làm việc.
# # self cho phép phương thức truy cập hoặc thay đổi dữ liệu của object đó.

# # Ví dụ:
    
# class Product:
#     def __init__(self, name):
#         self.name = name 
# #  Khi tạo object:
# phone = Product("iPhone")
# # thì python sẽ hiểu là 
# Product.__init__(phone, "iPhone")
# # => self chính là object phone.
# #    self.name = name
# #       ↓
# #       Nghĩa là: gán giá trị "iPhone" vào thuộc tính name của object phone.


# 3. Tạo sao self luôn là tham số đầu tiên của mỗi phương thức.
# Mỗi object có dữ liệu riêng.
# Khi gọi một phương thức, Python cần biết phương thức đó làm việc với object nào.

# Ví dụ:

# class Product:
#     def show(self):
#         print(self.name)
        
# # Tạo 2 object:

# sanpham1 = Product("iPhone")
# sanpham2 = Product("Samsung")

# # gọi phương thức show()
# sanpham1.show()
# # ↓
# # Python sẽ hiểu là
# Product.show(sanpham1)


# sanpham2.show()
# # ↓
# # Python sẽ hiểu là
# Product.show(sanpham2)

# #  ==> Nhờ có phương thức self, cùng một phước thức show() nhưng có thể hiển thị dữ liệu của chinh object được gọi.

# 4. Ví dụ đầy đủ với class Product

class Product:
    def __init__(self, id, name, price, stock):
        
        # Khởi tạo các thuộc tính của object
        self.id = id
        self.name = name
        self.price = price
        self.stock = stock
    
    def show_info(self):
        print("ID sản phẩm: ", self.id)
        print("Tên sản phẩm: ", self.name)
        print("Giá sản phẩm: ", self.price)
        print("Số lượng hàng còn lại trong kho: ", self.stock)
        
# Tạo object cụ thể bao gồm các thuộc tính đã định nghĩa trong class
Sanpham1 = Product(1, "iPhone 16", 25000000, 10)
Sanpham2 = Product(2, "MacBook Air", 32000000, 1)
# Gọi phương thức show_info() để hiển thị thông tin của các object
Sanpham1.show_info()
print()
Sanpham2.show_info()

# Kết quả:
# Giá sản phẩm:  25000000
# Số lượng hàng còn lại trong kho:  10

# ID sản phẩm:  2
# Tên sản phẩm:  MacBook Air
# Giá sản phẩm:  32000000
# Số lượng hàng còn lại trong kho:  1

# Cách self hoạt động:
    
# Khi gọi:
# Sanpham1.show_info()
# ↓
# Python thực hiện:
# Product.show_info(Sanpham1)
# ↓
# Lúc này: self là Sanpham1

# Khi gọi:
# Sanpham2.show_info()
# ↓
# Python thực hiện:
# Product.show_info(Sanpham2)
# ↓
# Lúc này: self là Sanpham2

# => Nhờ vậy cùng một phương thức sẽ truy cập đúng dữ liệu của từng object.

# ↓↓↓↓↓↓↓↓
# __init__() => Hàm khởi tạo, tự động được gọi khi tạo object mới để gán giá trị ban đầu cho các thuộc tính.
#            "Chuẩn bị dữ liệu ban đầu cho object."
# self     => Tham chiếu đến chính object đang gọi phương thức.
#             "Đây chính là object hiện tại."
# self.tên_thuộc_tính: 
#                   "Thuộc tính của object hiện tại."
#                   Vì sao self đứng đầu?
#                   Để Python biết phương thức đang thao tác trên object nào và có thể truy cập dữ liệu của object đó.
# Trong ví dụ Product, mỗi khi tạo một sản phẩm mới như Product(1, "iPhone 16", 25000000, 15), hàm __init__() sẽ khởi tạo các thuộc tính (id, name, price, stock) cho object đó, và self giúp đảm bảo các giá trị này được lưu đúng vào sản phẩm vừa được tạo.

# Bài tập 3:

#  Các loại thuộc tính và phương thức trong Class 
# Liệt kê và giải thích ba loại phương thức trong Python: 
#     Instance Method,
#     Class Method  (@classmethod), 
#     Static Method (@staticmethod). 
#     Cho ví dụ cụ thể cho mỗi loại trong  bối cảnh class Order (đơn hàng). 

# Trong Python, phương thức(Method) là các hàm được định nghĩa bên trong một Class
# Có 3 loại phương thức thường gặp:
#     1. Instance Method(Phương thức đối tượng)
#     2. Class Method(Phương thức lớp)
#     3. Static Method(Phương thức tĩnh)
    
# => Mỗi loại phương thức sẽ có mục đích sử dụng khác nhau

# 1. Instance Method (Phương thức đối tượng)
#  Đây là loại phương thức được sử dụng nhiều nhất.
#             Luôn có tham số đầu tiên là self.
#             Làm việc với dữ liệu của từng object.
#             Có thể đọc và thay đổi các thuộc tính của object
            
# Cú pháp:
# class Order:
#     def method_name(self):
#         ....
# Ví dụ trong  bối cảnh class Order (đơn hàng)
# class Order:
#     def __init__(self, order_id, customer, total):
#         self.order_id = order_id
#         self.customer = customer
#         self.total = total
        
#     def show_info(self):
#         print(f"Mã đơn hàng: {self.order_id}")
#         print(f"Khách hàng: {self.customer}")
#         print(f"Tổng tiền: {self.total}")
# # Tạo object
# order1 = Order("OD001", "Nguyen Van A", 500000)
# # Gọi phương thức
# order1.show_info() # show_info() sử dụng chính object đang gọi nó.
# Kết quả:
# Mã đơn hàng: OD001
# Khách hàng: Nguyen Van A
# Tổng tiền: 500000

# 2. Class Method(@classmethod)
# Class Method làm việc với Class, không làm việc trực tiếp với từng object.
#                  Được đánh dấu bằng @classmethod
#                  Tham số đầu tiên là cls (class)
#                  Có thể truy cập hoặc thay đổi thuộc tính của class

# Cú pháp:

# class Order:
#     @classmethod
#     def method_name(cls):
#         ...

# Ví dụ 
# # Giả sử muốn đếm tổng số đơn hàng đã tạo.

# class Order:
#     total_orders = 0
#     def __init__(self, order_id):
#         self.order_id = order_id
#         Order.total_orders += 1
        
#     @classmethod
#     def show_total_orders(cls):
#         print(f"Tổng số đơn hàng: ", cls.total_orders)
# # Tạo object(đơn hàng)
# order1 = Order("OD001")
# order2 = Order("OD002")
# order3 = Order("OD003")
# # Gọi hàm(phương thức) để show tổng số đơn hàng đếm được:
# Order.show_total_orders() # Phương thức này không hiển thị thông tin của từng đơn hàng mà hiển thị thông tin chung của cả lớp Order.

# Kết quả: 
#     Tổng số đơn hàng:  3
 
#  3. Static Method(@staticmethod)
# # staticmethod là phương thức không sử dụng self và cũng không sử dụng cls.
#                Được đánh dấu bằng @staticmethod
#                Chỉ thực hiện một chức năng hỗ trợ
#                Không truy cập dữ liệu của object hoặc class

# Cú pháp
# class Order:
    
#     @staticmethod
#     def method_name():
#         ....

# Ví dụ:
# Giả sử hệ thống quy định:
#     Đơn hàng trên 500.000 đồng được miễn phí vận chuyển.

# class Order:
#     @staticmethod
#     def free_shipping(total):
#         return total >= 500000
# # Sử dụng:
# print(Order.free_shipping(600000))
# print(Order.free_shipping(200000))
# Kết quả:
# True
# False
#  => Phương thức này chỉ kiểm tra điều kiện miễn phí vận chuyển, không cần biết đơn hàng nào đang gọi và cũng không cần truy cập dữ liệu của class

# Ví dụ tổng hợp:
# class Order:
#     total_order = 0
#     def __init__(self, order_id, customer, total):
        
#         self.order_id = order_id
#         self.customer = customer
#         self.total = total
#         Order.total_order += 1
        
#     # Instance Method
#     def show_info(self):
#         print(f"{self.order_id} - {self.customer} -  {self.total}")
#     # Class Method
#     @classmethod
#     def show_total_orders(cls):
#         print("Tổng số đơn hàng: ", cls.total_order)
    
#     # Static Method
#     @staticmethod
#     def free_shipping(total):  # Dùng khi hàm chỉ kiểm tra một số tiền bất kỳ. Khi gọi hàm cần truyền giá trị total một cách thủ công.
#         return total >= 500000
#     # tạo object
# order1 = Order("OD001", "An", 700000)
# order2 = Order("OD002", "Bình", 300000)
#     # Gọi phương thức

# order1.show_info()
    
# Order.show_total_orders()
    
# print(Order.free_shipping(700000)) 

# Kết quả:
# OD001 - An -  700000
# Tổng số đơn hàng:  2
# True

# Trường hợp  muốn kiểm tra free_shipping cho đơn hàng hiện tại.
# hàm free_shipping không dùng phương thức @staticmethod.
# free_shipping() muốn kiểm tra self.total
# muốn dùng dữ liệu của object
class Order:
    total_order = 0
    def __init__(self, order_id, customer, total):
        
        self.order_id = order_id
        self.customer = customer
        self.total = total
        Order.total_order += 1
        
    # Instance Method
    def show_info(self):
        print(f"{self.order_id} - {self.customer} -  {self.total}")
    # Class Method
    @classmethod
    def show_total_orders(cls):
        print("Tổng số đơn hàng: ", cls.total_order)
    
    # Static Method

    def free_shipping(self):  # Dùng khi muốn kiểm tra đơn hàng hiện tại.. Khi gọi hàm không cần truyền giá trị total một cách thủ công.
        return self.total >= 500000
    # tạo object
order1 = Order("OD001", "An", 700000)
order2 = Order("OD002", "Bình", 300000)
    # Gọi phương thức

Order.show_total_orders()

order1.show_info()
    
print(order1.free_shipping()) 

order2.show_info()
    
print(order2.free_shipping()) 

# Kết quả:
# Tổng số đơn hàng:  2
# OD001 - An -  700000
# True
# OD002 - Bình -  300000
# False


# Bài tập 4:
# OOP (Object-Oriented Programming)
# 1. Tính đóng gói (Encapsulation) là gì?

# Encapsulation (Đóng gói) là việc:
#     Gom dữ liệu (thuộc tính) và hành động (phương thức) vào cùng một class
#     Ẩn những dữ liệu không nên cho bên ngoài truy cập trực tiếp
#     Chỉ cho phép truy cập thông qua các phương thức được quy định.
# Hình dung tính đóng gói giống như một chiếc ATM
#        Người dùng có thể:
#            Rút tiền
#            Chuyển khoản
#            Xem số dư
#        Nhưng không thể mở máy ATM để sửa số dư tài khoản.
#        => Dữ liệu bên trong được bảo vệ
#           Người dùng chỉ thao tác thông qua các chức năng cho phép

# 2. Access Modifier trong Python

# Ở Java hay C++ có:
#     public
#     protected
#     private
# Python không có TỪ KHÓA như vậy.
# Python chỉ sử dụng QUY ƯỚC ĐẶT TÊN (Naming Convention).
# Có 3 mức:
#     public
#     protected
#     private

# 2.1 Public (không có dấu _)
# Đây là mức mặc định.
# Ví dụ:
class User:
    
    def __init__(self):
        self.name = "Vy"
# Có thể truy cập trực tiếp
user = User()

print(user.name)

#  kết quả
# Vy

# Có thể sửa luôn:
user.name = "Lan"
print(user.name)

# Kết quả:
# Lan

# => Đặc điểm: Truy cập được ở mọi nơi
# self.name

# 2.2 Protected (_name)
# Viết một dấu gạch dưới.
class User:
    
    def __init__(self):
        self._salary = 5000
        
# Có thể truy cập được
user = User()
print(user._salary)
# Vẫn chạy bình thường.
# Kết quả:
# 5000

# Nhưng dấu _ mang ý nghĩa:
# "Đây là dữ liệu nội bộ. Đừng truy cập trực tiếp nếu không cần."
# ===> Đây chỉ là quy ước, Python không cấm.
# Thông thường: 
                    # Class con vẫn dùng được.
                    # Người bên ngoài không nên sửa
                    
# 2.3 Private (_name)
# Viết 2 dấu gạch dưới

class User:
    def __init__(self):
        self.__password = "123456"
        
# Nếu truy cập:
# user = User()
# print(user.__password)
# Kết quả:
# AttributeError: 'User' object has no attribute '__password'

# Thuộc tính private (__password) không được truy cập trực tiếp
# Trong Python, thuộc tính bắt đầu bằng __ sẽ được name mangling.
# ame mangling là cơ chế Python tự động đổi tên thuộc tính hoặc phương thức bắt đầu bằng __ (hai dấu gạch dưới) để tránh bị truy cập hoặc ghi đè ngoài ý muốn, đặc biệt khi kế thừa (inheritance).

#  Python muốn tránh việc vô tình truy cập hoặc ghi đè, chứ không phải bảo mật tuyệt đối.

# 3. Kết hợp thuộc tính __private với getter/setter (hoặc @property)
# Trong Python, public, protected và private chủ yếu là quy ước đặt tên, 
# không phải cơ chế phân quyền cứng như Java hay C++.
# Tuy nhiên, kết hợp thuộc tính __private với getter/setter (hoặc @property) là cách phổ biến để hiện thực tính đóng gói (Encapsulation),
# giúp bảo vệ dữ liệu và kiểm soát việc truy cập, cập nhật thuộc tính của đối tượng.

# Getter/Setter được sử dụng để:

# Đọc hoặc cập nhật dữ liệu một cách có kiểm soát.
# Kiểm tra tính hợp lệ trước khi thay đổi giá trị.
# Giữ cho trạng thái của đối tượng luôn đúng và an toàn.

# 3.1 Getter, Setter,  @property  là gì?

# Getter, Setter và @property đều liên quan đến đóng gói (Encapsulation) trong lập trình hướng đối tượng (OOP).
# Chúng giúp kiểm soát việc đọc và ghi dữ liệu của đối tượng thay vì cho phép truy cập trực tiếp.

# Getter là một phương thức dùng để lấy(đọc) giá trị của thuộc tính.
# Ví dụ:
class User:
    def __init__(self, password):
        self.__password = password
    
    def get_password(self):
        return self.__password
    
userA = User("A123456")
userB = User("Babcxyz")
print(userA.get_password())
print(userB.get_password())

# Kết quả
# A123456
# Babcxyz



# Vì thuộc tính __password là thuộc tính private nên không thể truy cập trực tiếp:
# print(userA.__password)  => Báo lỗi: AttributeError
# print(userB.__password) => Báo lỗi: AttributeError
#  => Lúc này phải dùng Getter
# print(userA.get_password())
# print(userB.get_password())

# Setter là phương thức dùng để thay đổi(ghi) giá trị của thuộc tính.
# Ví dụ:
class User:
    
    def __init__(self, password):
        self.__password = password
    
    def set_password(self, new_password):
        self.__password = new_password
    
    def get_password(self):
        return self.__password

# Sử dụng:
userC = User("C1234567")
userD = User("D1234567")
userD.set_password("D1234567update")
print(userC.get_password())
print(userD.get_password())

# Kết quả:
# C1234567
# D1234567update

# Lí do dùng Setter:
#  Điểm mạnh nhất của Setter là kiểm tra dữ liệu trước khi lưu

# Ví dụ:
# Mật khẩu phải có ít nhất 8 ký tự
class User:
    def  __init__(self, password):
        self.__password = password
    def set_password(self, password):
        if len(password) < 8:
            print("Password quá ngắn")
            return 
        self.__password = password
        
    def get_password(self):
        return self.__password
    
# Sử dụng 

userE = User("E1234567")
print(userE.get_password())
# Kết quả:
# E1234567

userE.set_password("E123")
print(userE.get_password())

# Kết quả: 
# Password không bị đổi vì không hợp lệ.

# Password quá ngắn
# 1234567
class User:
    # Hàm khởi tạo, chạy khi tạo đối tượng
    def __init__(self, password):
        # Thuộc tính private
        self.__password = password
    
    # Hàm thay đổi mật khẩu
    def set_password(self, new_password):
        # Kiểm tra độ dài mật khẩu:
        if len(new_password) < 8:
            print(" Mật khẩu phải có ít nhất 8 ký tự.")
            return
        # Nếu hợp lệ thì cập nhật mật khẩu
        self.__password = new_password
        print("Đổi mật khẩu thành công.")
        
    # Hàm lấy mật khẩu
    def get_password(self):
        return self.__password
# Sử dụng class đã tạo:

# Tạo một đối tượng user
userF = User("F1234567")
# Xem mật khẩu hiện tại
print(userF.get_password())
# Thử đổi mật khẩu quá ngắn 
userF.set_password("F123")
# Xem lại mật khẩu(Do mật khẩu mới  không hợp lệ nên hệ thống vẫn giữ mật khẩu trước đó, không thay đổi)
print(userF.get_password())
# Thử đổi mật khẩu hợp lệ
userF.set_password("F1234567update")
# Xem mật khẩu mới
print(userF.get_password())

# Kết quả:
# F1234567

#  Mật khẩu phải có ít nhất 8 ký tự.

# F1234567

# Đổi mật khẩu thành công.

# F1234567update

#  ==> Tuy nhiên Getter/Setter có vấn đề là nhìn hơi dài. Do đó cần @property để viết gọn, đẹp hơn
        #   user.set_password("abc123456")
        #   print(user.get_password())
# @property
# @property biến một phương thức thành thuộc tính.
# Thay vì phải viết:
            #   user.get_password
            #   Ta chỉ cần viết:
            #    user.password => Nhưng thực chất bên trong vẫn gọi hàm get_password
# Ví dụ @property
class User:
    def __init__(self, password):
        self.__password = password
        
    @property
    def password(self):
        return self.__password
# Sử dụng
userG = User("G1234567")
userH = User("H1234567")
print(userG.password)
print(userH.password)
# Kết quả:
# G1234567
# H1234567

# Trong lệnh print chỉ có password  không có () như khi không dùng  @property
# Vì password giờ đã trở thành thuộc tính.

# print(userG.password)
# print(userH.password)

# Setter với @property

# Muốn gán 
            # userK.password = "K1234567update"
# Ta dùng:
class User:
    def __init__(self, password):
        self.__password = password
    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, new_password):
        self.__password = new_password
    
# Sử dụng
userK = User("K1234567")
# Xem password hiện tại: K1234567
print(userK.password) 
# Thay đổi password thành K1234567update
userK.password = "K1234567update"
# Xem password mới
print(userK.password)

# Kết quả: K1234567update

# Ví dụ Setter có kiểm tra dữ liệu khi dùng @property
class User:
    
    def __init__(self, password):
        self.__password = password
    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, new_password):
        if len(new_password) < 8:
            print("Password phải từ 8 ký tự")
            return
        self.__password = new_password
userL = User("L1234567")
# Xem mật khẩu hiện tại: L1234567
print(userL.password)
# Sửa mật khẩu không hợp lệ
userL.password = "L123" # Kết quả: Password phải từ 8 ký tự
# Xem mật khẩu sau khi tiến hành thay đổi.
print(userL.password) #L1234567
# Sửa mật khẩu hợp lệ: L1234567update
userL.password = "L1234567update"
print(userL.password) # L1234567update

#  ==> Nếu chỉ có @property mà không có @password.setter thì userL.password = "L123" / userL.password = "L1234567update"
#  sẽ báo lỗi: AttributeError: can't set attribute
    # Thuộc tính lúc này chỉ được đọc.

class User:
    def __init__(self, password):
        self.__password = password
    @property
    def password(self):
        """Getter"""
        return self.__password
    @password.setter
    def password(self, new_password):
        """Setter"""
        if len(new_password) < 8:
            raise ValueError("Mật khẩu phải có ít nhất 8 ký tự")
        self.__password = new_password
userM = User("M1234567")
print(userM.password) # Gọi Getter
userM.password = "M1234567update" #Gọi Setter
print(userM.password) # Gọi Getter

# Kết quả
# M1234567
# M1234567update

# Câu 5: Kế thừa (Inheritance) và ghi đè phương thức (Method Overriding)
#1. Kế thừa (Inheritance) là một tính chất quan trọng của lập trình hướng đối tượng (OOP)

# Nó cho phép LỚP CON (child class) sử dụng lại các thuộc tính (attributes) và phương thức (methods) của LỚP CHA (parent class)
# Thay vì viết lại những phần giống nhau, ta chỉ cần viết một lần trong lớp cha, sau đó các lớp con sẽ kế thừa
# và lớp con có thể bổ sung hoặc thay đổi những gì cần thiết.

# Ví dụ thực tế:
# Person(Người):
            #  Customer(Khách hàng)
            #  Employee(Nhân viên)
            #  Student(Học sinh)
            # => Cả Customer, Employee, Student đều là Person nên tất cả dều có các thuộc tính chung là:
            #                  Tên
            #                  Tuổi
            #                  Giới thiệu bản thân
#             Nhưng mỗi Customer, Employee, Student lại có những đặc điểm, thuộc tính riêng:
#                 Customer có mã khách hàng
#                 Employee có mức lương
#                 Student có tên trường
# => Ta sẽ khai báo các thuộc tính Tên, Tuổi, Giới thiệu bản thân trong class Person. Các class Customer, Employee, Student sẽ sử dụng luôn các thuộc tính đã được khai báo trong class Person chứ không cần phải khai báo riêng ở từng class này nữa.
# ====> Đó chính là kế thừa.
 
# Lợi ích của kế thừa:

# 1.1 Tái sử dụng code: Không cần viết lại những phần giống nhau.
# Ví dụ: 
# Mọi người đều có:
#                      name
#                      age
#                      introduce()
# => Thì chỉ cần viết một lần trong lớp Person

# 1.2 Dễ bảo trì: 
# Nếu cần sửa cách giới thiệu bản thân: 
                        # Chỉ cần sửa trong lớp Person
                        # => Mọi lớp con đều được cập nhật theo.
                        
# 1.3 Dễ mở rộng
#  Sau này muốn thêm 
                    #    Teacher
                    #    Doctor
                    #    Manager
                    #    => Chỉ cần kế thừa từ lớp Person

# Cú pháp kế thừa trong Python
class Person:
    pass
class Customer(Person):
    pass
#  => Customer kế thừa các thuộc tính và phương thức đã được khai báo trong lớp Person.
#   Hay nói cách khác, Customer là một Person.

# 2. Ghi đè phương thức (Method Overriding)
# Ghi đè (Override) là việc lớp con viết lại một phương thức đã có trong lớp cha.
# Tên phương thức giống nhau. Nhưng nội dung khác nhau.
# Python sẽ ưu tiên gọi phương thức của lớp con

# Ví dụ:
# Lớp cha:
class Person:
    
    def introduce(self):
        print("Tôi là một người.")
# Lớp con:
class Customer(Person):
    
    def introduce(self):
        print("Tôi là khách hàng")
# Khi sử dụng:
customerA = Customer()
customerA.introduce() 
# Kết quả: Tôi là khách hàng. 
# chứ không phải: Tôi là một người.
# ===> Vì phương thức thức introduce của lớp cha(Person) đã bị ghi đè ở lớp con (Customer)

# Ví dụ:
# Lớp cha:
class Person :
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduce(self):
        print(f"Tôi tên là {self.name}, năm nay {self.age} tuổi. ")
# Lớp con kế thừa thuộc tính và phương thức của Person
class Customer(Person):
    
    def __init__(self, name, age, customer_id):
        super().__init__(name, age) # Hàm khởi tạo của lớp cha
        self.customer_id = customer_id
    # Ghi đè phương thức introduce 
    def introduce(self):
        print(
            f"Tôi tên là {self.name}, năm nay {self.age} tuổi. "
            f"Mã khách hàng là: {self.customer_id}"
            )
# Sử dụng
personB= Person ("Minh Anh", 2)
customerB = Customer("Vy", 32, "KH001")

personB.introduce()
customerB.introduce()

# Kết quả:

# Tôi tên là Minh Anh, năm nay 2 tuổi.

# Tôi tên là Vy, năm nay 32 tuổi. Mã khách hàng là: KH001

# Vì sao phải dùng super()
# Trong lớp Customer(lớp con), nếu không gọi: super().__init__(name, age)
# thì: các thuộc tính self.name, self.age sẽ chưa được tạo.
# => Khi chạy: customer.introduce() thì sẽ báo lỗi: AttributeError
# Vì vậy:
# super().__init__(...) =====> Giúp gọi hàm khởi tạo của lớp cha để khởi tạo các thuộc tính chung.


# Kế thừa giúp tái sử dụng mã nguồn, giảm lặp code và dễ mở rộng chương trình.
# Ghi đè phương thức (override) cho phép lớp con thay đổi cách hoạt động của phương thức được kế thừa để phù hợp với nhu cầu riêng.
# super() giúp lớp con tận dụng phần khởi tạo hoặc chức năng của lớp cha thay vì phải viết lại từ đầu.

# Câu 6: Scope(Phạm vi hoạt động) của biến trong Class 

# 1. Scope(Phạm vi hoạt động): Là phạm vi mà một biến có thể được truy cập và sử dụng trong chương trình.
# Biến được khai báo ở đâu thì chỉ có thể dùng trong phạm vi đó(Hoặc các phạm vi khác)
# Nếu sử dụng biến ngoài phạm vi của nó sẽ xảy ra lỗi.

# Ví dụ:
def hello():
    x = 10 # Biến x chỉ tồn tại trong hàm hello()
# print(x)
# Kết quả: NameError: name 'x' is not defined
            #   => Vì x chỉ tồn tại trong hàm hello()
# Trong Python có 4 loại biến thường gặp.

# 1. Global Variable(Biến toàn cục)
# Biến toàn cục là biến được khai báo bên ngoài class và bên ngoài hàm
# Biến toàn cục có thể được đọc ở hầu hết mội nơi trong chương trình.
# Ví dụ:
tax = 0.1 # Biến toàn cục (global)

class ShoppingCart:
    def calculate(self, price):
        total = price + price * tax
        print(total)
        
cart = ShoppingCart()
cart.calculate(100)

# Kết quả: 110.0
# ===> Ở ví dụ này, tax được tạo ngoài class nên nó là biến toàn cục (global variable)

# 2. Local Variable(Biến cục bộ)
# Biến cục bộ là biến được tạo bên trong hàm.
# Biến cục bộ chỉ tồn tại khi hàm đang chạy.
# Ví dụ:
class ShoppingCart:
    def add_product(self):
        product = "Laptop" #  Biến cục bộ (Local Variable)
        print(product)
cart = ShoppingCart()
cart.add_product() # Nếu viết là print(product) thì sẽ NameError. Vì product chỉ tồn tại trong hàm add_product().

# Kết quả: Laptop

# 3. Instance Variable(Biến của object)
# Được tạo bằng cú pháp: self.tên biến
# Mỗi object sẽ có một bản sao riêng.

# Ví dụ:
class ShoppingCart:
    def __init__(self, customer):
        self.customer = customer
        self.products = []
cart1 = ShoppingCart("Vy")
cart2 = ShoppingCart("Minh Anh")
print(cart1.customer)
print(cart1.products)

print(cart2.customer)

print(cart2.products)

# Kết quả:
# Vy
# []
# Minh Anh
# []



# ==> Ở đây: self.customer và self.products là Instance Variable(Biến của object)

# cart1: customer = "Vy"           products = []
# cart2: customer = "Minh Anh"     products = []
# ===> 2 object cart1 và cart2 không ảnh hưởng đến nhau.

# Ví dụ: Thêm sản phẩm vào cart1
cart1.products.append("Laptop")
cart1.products.append( "iPhone15 Promax")

# in ra số lượng của 2 giỏ hàng
print(cart1.products)
print(cart2.products)

# Kết quả:
# ['Laptop', 'iPhone15 Promax']

# []

# 4. Class Variable (Biến của Class)
# Biến của Class: được khai báo trực tiếp trong class, ngoài các method.
#                Mọi object dùng chung một biến.

# Ví dụ:
class ShoppingCart:
    shop_name = "ABC Store" # Biến của Class
    
    def __init__(self, customer):
        self.customer = customer
        
cart3 = ShoppingCart("Vy")
cart4 = ShoppingCart("Minh Anh")

print(cart3.shop_name)
print(cart4.shop_name)

# Kết quả:
# ABC Store
# ABC Store

# Nếu sửa 
ShoppingCart.shop_name = "XYZ Store"
 
#  thì
print(cart3.shop_name)
print(cart4.shop_name)
# Kết quả đều là:
# XYZ Store
# XYZ Store

# Vì đây là biến dùng chung.

# Ví dụ:

# Biến toàn cục(Glabal Variable): Có thể dùng ở nhiều nơi trong chương trình.
tax = 0.1

class ShoppingCart:
    
    # Class Variable(Biến của lớp): Mọi giỏ hàng đều dùng chung.
    shop_name ="MeoMeo Store"
    
    # Mỗi giỏ hàng tạo ra sẽ bao gồm tên khách hàng và danh sách sản phẩm riêng.
    
    def __init__(self, customer):  
        
        # Biến của object(Instance Variable): 
        self.customer = customer # Mỗi khách hàng có tên riêng
        self.products = [] # Mỗi khách hàng danh sách sản phẩm riêng.
    
    # Dùng hàm này để thêm sản phẩm vào giỏ hàng mong muốn  
    def add_product(self, product):
        #  Biến cục bộ (Local Variable)
        message = f"Đã thêm {product} vào giỏ hàng."
        self.products.append(product)
        print(message)
    
    # Dùng hàm này để tính tổng tiền cần thanh toán cho từng giỏ hàng riêng biệt.
    def calculate_total(self, price):
        # Biến cục bộ (Local Variable)
        total = price + price * tax # biến total: là biến cục bộ, chỉ tồn tại trong hàm calculate_total()
        print("Tổng tiền: ", total)

dangtuan_cart = ShoppingCart("Dang Tuan") #Tên gio hang = Tên class(Tham số nhận vào vào)
vytuoi_cart = ShoppingCart("Vy Tuoi") #Tên gio hang = Tên class(Tham số nhận vào vào)
minhanh_cart = ShoppingCart("Minh Anh") #Tên gio hang = Tên class(Tham số nhận vào vào)

# Thêm sản phẩm vào giỏ hàng của dangtuan, tính tổng tiền cần thanh toán, in ra tên khách hàng, list sản phẩm đã mua, tên shop
dangtuan_cart.add_product("Laptop") #tengiohang.tenham("Ten san pham")
dangtuan_cart.calculate_total(10000000) #tengiohang.tenham(gia san pham)

print(dangtuan_cart.customer) #tengohang.tenbien
print(dangtuan_cart.products) #tengiohang.tenbien
print(ShoppingCart.shop_name) #Tenclass.tenbien

# Thêm sản phẩm vào giỏ hàng của vytuoi, tính tổng tiền cần thanh toán, in ra tên khách hàng, list sản phẩm đã mua, tên shop
vytuoi_cart.add_product("iPhone 15 ProMax")
vytuoi_cart.calculate_total(35000000)

print(vytuoi_cart.customer)
print(vytuoi_cart.products)
print(ShoppingCart.shop_name)

# Giỏ hàng minhanh không có sản phẩm được thêm vào.
print(minhanh_cart.customer)
print(minhanh_cart.products)
print(ShoppingCart.shop_name)


# Kết quả

# Đã thêm Laptop vào giỏ hàng.
# Tổng tiền:  11000000.0

# Dang Tuan
# ['Laptop']
# MeoMeo Store


# Đã thêm iPhone 15 ProMax vào giỏ hàng.
# Tổng tiền:  38500000.0

# Vy Tuoi
# ['iPhone 15 ProMax']
# MeoMeo Store


# Minh Anh
# []
# MeoMeo Store

# Câu 7
# POLYMORPHISM (Đa hình) và ABSTRACTION (Trừu tượng)

# 1. POLYMORPHISM ( Tính đa hình) 
# Polymorphism (đa hình) là một trong 4 tính chất quan trọng của lập trình hướng đối tượng (OOP).
# Polymorphism(Đa hình) nghĩa là:
#     Cùng một phương thức(method), nhưng mỗi class sẽ thực hiện theo cách khác nhau.
#     Cùng một phương thức (method) nhưng khi được gọi trên các object khác nhau thì sẽ cho ra các hành vi khác nhau.

#  Ví dụ không có đa hình:
class Dog:
    def sound(self):
        print("Gâu Gâu")
class Cat:
    def sound(self):
        print("Meo Meo")

dog = Dog()
cat = Cat()

dog.sound()
cat.sound()
# Kết quả:
# Gâu Gâu
# Meo Meo

#  ===> Mỗi class có cách triển khai riêng.

# Ví dụ thể hiện tính đa hình(Polymorphism)
# Tạo một hàm để dùng chung
class Dog:
    def sound(self):
        print("Gâu Gâu")
class Cat:
    def sound(self):
        print("Meo meo")
class Bird:
    def sound(self):
        print("Chíp chíp")
def make_sound(animal):
    animal.sound()

dog = Dog()
cat = Cat()
bird = Bird()

make_sound(dog)
make_sound(cat)
make_sound(bird)

# Kết quả:
# Gâu Gâu
# Meo meo
# Chíp chíp

# Polymorphism thông qua Method Overriding

# Class cha
class Animal:
    def move(self):
        print("Động vật đang di chuyển")
# Class con ghi đè
class Dog(Animal):
    def move(self):
       print("Chó chạy bằng 4 chân")
class Bird(Animal):
    def move(self):
        print("Chim bay trên trời")
# Sử dụng
animals = [
    Dog(),
    Bird()
]

for animal in animals:
    animal.move()

# Kết quả:
# Chó chạy bằng 4 chân
# Chim bay trên trời
#  => Cùng gọi animal.move() nhưng kết quả khác nhau => Đây chính là Polymorphism(Tính đa hình)

# Ví dụ trong hệ thống thanh toán:
class Payment:
    def pay(self, amount):
        pass
class CreditCard(Payment):
    def pay(self, amount):
        print(f"Thanh toán {amount} bằng thẻ tín dụng")
class Paypal(Payment):
    def pay(self, amount):
        print(f"Thanh toán {amount} bằng Paypal")
class BankTransfer(Payment):
    def pay(self, amount):
        print(f"Thanh toán {amount} bằng chuyển khoản")
# Sử dụng
payments = [
    CreditCard(),
    Paypal(),
    BankTransfer()
]

for payment in payments:
    payment.pay(10000)
# Kết quả:
# Thanh toán 10000 bằng thẻ tín dụng
# Thanh toán 10000 bằng Paypal
# Thanh toán 10000 bằng chuyển khoản

#     Ưu điểm của Polymorphism(Đa hình):
#         + Code ngắn gọn: Không cần nhiều if...elif....
#         + Linh hoạt: Cùng một lời gọi (payment.pay()) nhưng xử lý khác nhau tùy đối tượng.
#         + Dễ mở rộng 
#         + Dễ bảo trì
# Ví dụ: Chương trình bán hàng hỗ trợ 4 hình thức thanh toán: Card, Paypal, Bank, Momo
        #  Code không dùng Polymorphism mà sử dụng if...elif....
class CardPayment:
    def pay(self):
        print("Thanh toán bằng thẻ.")
class PaypalPayment:
    def pay(self):
        print("Thanh toán bằng Paypal.")
class BankPayment:
    def pay(self):
        print("Thanh toán bằng chuyển khoản.")
class MomoPayment:
    def pay(self):
        print("Thanh toán bằng Momo")
payment = "bank"
if payment == "card":
    card = CardPayment()
    card.pay
elif payment == "paypal":
    paypal = PaypalPayment()
    paypal.pay()
elif payment == "bank":
    bank = BankPayment()
    bank.pay()
elif payment == "momo":
    momo = MomoPayment()
else:
    print("Phương thức thanh toán không hợp lệ.")
# Kết quả: Thanh toán bằng chuyển khoản.
# Nếu muốn thêm phương thức mới thì bắt buộc phải thêm code đoạn if...elif....
# Ví dụ: thêm class ApplePayPayment:
class CardPayment:
    def pay(self):
        print("Thanh toán bằng thẻ.")
class PaypalPayment:
    def pay(self):
        print("Thanh toán bằng Paypal.")
class BankPayment:
    def pay(self):
        print("Thanh toán bằng chuyển khoản.")
class MomoPayment:
    def pay(self):
        print("Thanh toán bằng Momo")
class ApplePayPayment:
    def pay(self):
        print("Thanh toán bằng Apple Pay")
#  Thì bắt buộc phải thêm điều kiện ở phần if...elif....
payment = "applepay"

# Ta phải kiểm tra từng trường hợp rồi mới quyết định gọi phương thức nào.

if payment == "card":
    card = CardPayment()
    card.pay
elif payment == "paypal":
    paypal = PaypalPayment()
    paypal.pay()
elif payment == "bank":
    bank = BankPayment()
    bank.pay()
elif payment == "momo":
    momo = MomoPayment()
elif payment == "applepay":
    apple = ApplePayPayment()
    apple.pay()
else:
    print("Phương thức thanh toán không hợp lệ.")

# Kết quả: Thanh toán bằng Apple Pay

#  Ví dụ: Dùng Polymorphism, không dùng if...elif....

# Tạo lớp cha
class Payment:
    def pay(self):
        pass
# Tạo các lớp con ghi đè phương thức pay()
class CardPayment(Payment):
    def pay(self):
        print("Thanh toán bằng thẻ.")
class PaypalPayment(Payment):
    def pay(self):
        print("Thay toán bằng Paypal.")
class Bankpayment(Payment):
    def pay(self):
        print("Thanh toán bằng chuyển khoản.")
class MomoPayment(Payment):
    def pay(self):
        print("Thanh toán bằng Momo.")
# Sử dụng:
# Muốn thanh toán bằng Paypal
payment = PaypalPayment()
payment.pay()
# Kết quả: Thay toán bằng Paypal.

# Muốn đổi sang Momo:
payment = MomoPayment()
payment.pay()
# Kết quả: Thanh toán bằng Momo.
#  ===> Khi dùng Polymorphism, dòng gọi phương thức luôn giống nhau:payment.pay()
#     Không cần biết đối tượng là gì.
                # Nếu đổi thành:
                #     payment = CardPayment()
                # hoặc 
                #     payment = BankPayment()
                # thì vẫn chỉ có:
                #     payment.pay()
                # ==>  Không cần if...elif.... Python tự biết payment đang là đối tượng của lớp nào và gọi đúng phương thức pay() đã được override.
                
# Ví dụ thực tế trong dự án
# Nếu website bán hàng có 20 phương thức thanh toán:
# Không dùng Polymorphism:
# if payment == "card":
#     ...
# elif payment == "paypal":
#     ...
# elif payment == "bank":
#     ...
# ...
# elif payment == "visa":
#     ...
# elif payment == "master":
#     ...
# elif payment == "applepay":
#     ...
# elif payment == "googlepay":
#     ...
# Code sẽ ngày càng dài và mỗi lần thêm phương thức mới đều phải sửa chuỗi if...elif....
# Dùng Polymorphism: 
            #   payment.pay()
        # Mỗi phương thức thanh toán chỉ cần là một lớp mới có pay(). Phần gọi thanh toán không cần thay đổi, nên code ngắn gọn, dễ mở rộng và dễ bảo trì hơn. 
        # Đây chính là ưu điểm lớn nhất của Polymorphism trong OOP.



# 2. ABSTRACTION (Tính trừu tượng)
# Abstraction(Trừu tượng) là:
#           Ẩn đi các chi tiết phức tạp bên trong và chỉ cung cấp những gì người dùng cần sử dụng.
#           Người dùng chỉ cần biết gọi chức năng, không cần biết bên trong chức năng đó hoạt động như thế nào.
# Ví dụ ngoài đời:
# Máy giặt: Bạn chỉ cần bấm nút Start, không cần biết máy cấp nước, giặt, xả hay vắt theo thứ tự nào.
# ATM: Bạn chỉ cần chọn Rút tiền, không cần biết hệ thống kiểm tra PIN, kiểm tra số dư rồi mới trừ tiền.
# ===> Đó chính là Abstraction.
                
# Ví dụ không có Abstraction
# Giả sử việc thanh toán gồm 6 bước:
# 1. Kiểm tra số dư
# 2. Kiểm tra thẻ
# 3. Kết nối ngân hàng
# 4. Xác thực OTP
# 5. Trừ tiền
# 6. Gửi hóa đơn
# Nếu không dùng Abstraction, người sử dụng phải gọi từng bước.
class CardPayment:
    def check_balance(self):
        print("Kiểm tra số dư.")
    def check_card(self):
        print("Kiểm tra thẻ.")
    def connect_bank(self):
        print("Kết nối ngân hàng.")
    def verify_otp(self):
        print("Xác thực OTP.")
    def withdraw_money(self):
        print("Trừ tiền.")
    def send_invoice(self):
        print("Gửi hóa đơn.")
# Người dùng phải tự gọi:
payment = CardPayment()
payment.check_balance()
payment.check_card()
payment.connect_bank()
payment.verify_otp()
payment.withdraw_money()
payment.send_invoice()
# Kết quả:
# Kiểm tra số dư.
# Kiểm tra thẻ.
# Kết nối ngân hàng.
# Xác thực OTP.
# Trừ tiền.
# Gửi hóa đơn.

# Nhược điểm khi không dùng Abstraction
        #    Code dài
        #    Người dùng phải nhớ đúng thứ tự các bước
        #    Nếu gọi sai thứ tự sẽ có thể gây lỗi
        # ví dụ:
        # payment.withdraw_money()
        # payment.verify_otp()
        #  => Sai thứ tự, quy trình không hợp lý.
        
# Ví dụ CÓ Abstraction
# ẩn toàn bộ quy trình vào một phương thức pay().

class CardPayment:
    def pay(self):
        # ẩn toàn bộ quy trình vào một phương thức pay()
        self.check_balance()
        self.check_card()
        self.connect_bank()
        self.verify_otp()
        self.withdraw_money()
        self.send_invoice()
        
        print("Thanh toán thành công.")
    def check_balance(self):
        print("Kiểm tra số dư")
    def check_card(self):
        print("Kiểm tra thẻ")
    def connect_bank(self):
        print("Kết nối ngân hàng.")
    def verify_otp(self):
        print("Xác thực OTP")
    def withdraw_money(self):
        print("Trừ tiền.")
    def send_invoice(self):
        print("Gửi hóa đơn.")
# Người dùng chỉ cần:
payment = CardPayment()
payment.pay() # Người dùng không cần biết pay() đã gọi những phương thức nào bên trong. Đây chính là Abstraction.
# Kết quả:
# Kiểm tra số dư
# Kiểm tra thẻ
# Kết nối ngân hàng.
# Xác thực OTP
# Trừ tiền.
# Gửi hóa đơn.
# Thanh toán thành công.

# không có Abstraction:
            # Người dùng phải biết toàn bộ quy trình:
                #   check_balance()
                #   check_card()
                #   connect_bank()
                #   verify_otp()
                #   withdraw_money()
                #   send_invoice()
                
# Có Abstraction 
            # Người dùng chỉ cần gọi pay(), còn việc pay() sẽ kiểm tra số dư, kiểm tra thẻ, xác thực OTP, trừ tiền và gửi hóa đơn được xử lý bên trong lớp.
            # check_balance()
            # check_card()
            # connect_bank()
            # verify_otp()
            # withdraw_money()
            # send_invoice()

# Abstraction khác Encapsulation như thế nào?

# Encapsulation (Tính đóng gói):
                # Bảo vệ dữ liệu
                # Quy định cách truy cập dữ liệu
                # Dùng public, _protected, __private, getter/setter, @property
                # Tập trung vào dữ liệu
# Abstraction (Tính trừu tượng)
                # Ẩn đi sự phức tạp
                # Chỉ cung cấp chức năng cần thiết
                # Dùng Abstract Class và @abstracmethod
                # Tập trung vào chức năng

# Câu 8: Schema (Sơ đồ thiết kế class) - Cách lập kế hoạch xây dựng class 
# Giải thích khái niệm Schema trong thiết kế OOP. Các bước cần làm trước khi viết code: 
# • Xác định các thuộc tính (attributes) và phương thức (methods) cần thiết  
# • Xác định mối quan hệ giữa các class (kế thừa, composition)  
# • Xác định public/private cho mỗi thành phần  
# Hãy vẽ/mô tả schema cho class PaymentProcessor (xử lý thanh toán) với các class con  CreditCardPayment, BankTransferPayment, E-WalletPayment.

# Schema(Sơ đồ thiết kế Class) trong OOP là bản thiết kế mô tả cấu trúc của hệ thống trước khi viết code.
# Schema giúp lập trình viên xác định:
                #  Có nhữn class nào?
                #  Mỗi class có những thuộc tính (attributes) gì?
                #  Mỗi class có những phương thức (methods) gì?
                #  Các class liên hệ với nhau như thế nào?
                        # Kế thừa (Inheritance)
                        # Thành phần bên trong (Composition)
                        # Sử dụng (Dependency)
                #  Thành phần nào được phép truy cập từ bên ngoài(public)?
                # Thành phần nào chỉ dùng nội bộ (private)?
        #  ==>   Schema giống như bản vẽ kiến trúc của một ngôi nhà.
            #    Code là quá trình xây dựng ngôi nhà dựa trên bản vẽ đó.
# Các bước cần làm trước khi viết code:
# 
# Bước 1: Xác định các class cần có.
# Trước tiên cần phân tích bài toán.
# Ví dụ bài toán: Xây dựng hệ thống xử lý thanh toán hỗ trợ nhiều phương thức.
                    #  Thanh toán bằng thẻ tín dụng
                    #  Chuyển khoản ngân hàng
                    #  Ví điện tử
                # ==> Ta nhận thấy, hệ thống này có một chức năng chung là: Xử lý thanh toán => Tạo class cha: PaymentProcessor
                #                                 có các phương thức thanh toán khác nhau:
                                                    #    CreditCardPayment
                                                    #    BankTransferPayment
                                                    #    EWalletPayment
# Bước 2: Xác định các thuộc tính (Attributes)
#         Trả lời cho câu hỏi: Class này cần lưu trứ dữ liệu gì?
            # Ví dụ:
            # class PaymentProcessor(Xử lý thanh toán), lưu trữ dữ liệu chung của thanh toán như:
                    #  transaction_id  Mã giao dịch
                    #  amount          Số tiền
                    #  status          Trạng thái thanh toán
                    # ===> Schema:
                        # PaymentProcessor
                            #    transaction_id: str
                            #    amount: float
                            #    status: str
            # class CreditCardPayment(Thanh toán bằng thẻ), sẽ cần thêm thông tin:
                    # card_number  Số thẻ
                    # card_holder  Chủ thẻ
                    # ====>Schema:
                        # CreditCardPayment
                            #  card_number: str
                            #  card_holder: str
            # class BankTransferPayment(Chuyển khoản ngân hàng), sẽ cần thêm:
                    # bank_name: tên ngân hàng
                    # account_number: số tài khoản ngân hàng
                    #  ===> Schema:
                        # BankTransferPayment
                                # bank_name: str
                                # account_number: str
            # class E-WalletPayment(Ví điện tử), cần thêm:
                    # wallet_id   
                    # provider
                    #   ===> Schemas:
                        # EWalletPayment
                                # wallet_id: str
                                # provider: str
# Bước 3: Xác định Methods(phương thức)
#       Trả lời cho câu hỏi: Class này thực hiện hành động gì?
            # class PaymentProcessor(Xử lý thanh toán) sẽ thực hiện các hành động chung:
                    # process_payment()
                    # validate_payment()
                    # show_status()
            # Các class con: Mỗi phương thức thanh toán có cách xử lí khác nhau.
            # Ví dụ:
            # CreditCard:
            #       process_payment()
                        #  Kiểm tra thẻ
                        #  Xác thực OTP
                        #  Trừ tiền
            # Bank Transfer:
            #       process_payment()
                        # Kiểm tra tài khoản
                        # Xác nhận ngân hàng
                        # nhận tiền
                         
            # E-Wallet:
            #        process_payment()
                        # Kiểm tra số dư của ví điện tử
                        # Xác nhận ví
                        # Trừ tiền
# Bước 4: Xác định quan hệ giữa các class
        # 1. Quan hệ Kế thừa(Inheritance)
        # 2. Composition
# Bước 5: Xác định Public/Private

# Ví dụ: code theo Schema trên
from abc import ABC, abstractmethod
class PaymentProcessor(ABC):
    def __init__(self, transaction_id, amount):
        self.__transaction_id = transaction_id
        self.__amount = amount
        self.__status = "Pending"
    @abstractmethod
    def process_payment(self):
        pass
    def show_status(self):
        print(self.__status)
class CreditCardPayment(PaymentProcessor):
    def __init__(self, transaction_id, amount, card_number):
        super().__init__(transaction_id, amount)
        self.card_number = card_number
    def process_payment(self):
        print("Kiểm tra thẻ tín dụng")
        print("Xác thực OTP")
        print("Thanh toán bằng thẻ tín dụng")
class BankTransferPayment(PaymentProcessor):
    def __init__(self, transaction_id, amount, bank_name):
        super().__init__(transaction_id, amount)
        self.bank_name = bank_name
    def process_payment(self):
        print("Kiểm tra ngân hàng")
        print("Xác nhận chuyển khoản")
class EWalletPayment(PaymentProcessor):
    def __init__(self, transaction_id, amount, wallet_id):
        super().__init__(transaction_id, amount)
        self.wallet_id = wallet_id
    def process_payment(self):
        print("Kiểm tra số dư ví")
        print("Thanh toán bằng ví điện tử")

# Lợi ích của việc thiết kế Schema trước khi code:
            # Có kế hoạch rõ ràng
            # Class có trách nhiệm rõ ràng
            # Dễ thêm phương thức mới
            # Tuân thủ Encapsulation, Inheritance, Polymorphism
# Ví dụ: Sau này thêm các phương thức thanh toán mới như:
            #   CryptoPayment
            #   ApplePayPayment
            #   GooglePayPayment
        # ===> Chỉ cần tạo các class mới CryptoPayment, ApplePayPayment, GooglePayPayment và kế thừa từ PaymentProcessor.
        #       Không cần sửa code cũ 
# Nếu không thiết kế Schema:
            # Code ngay => Dễ bị rối
            # Class bị dư thừa
            # Khó mở rộng
            # Dễ vi phạm OOP 

# Câu 9: Cách vẽ sơ đồ tư duy (Mind Map) để thiết kế class 
# Giải thích lợi ích của việc vẽ sơ đồ tư duy trước khi code. 
# Các thành phần chính trong  sơ đồ tư duy:  
                #   • Tên class ở trung tâm 
                #   • Các nhánh chính: Thuộc tính, Phương thức, Quan hệ với class khác 
                #   • Chi tiết: tên, kiểu dữ liệu, access level  
# Hãy mô tả sơ đồ tư duy cho class InventoryManager (quản lý kho hàng)

            
# Cách vẽ sơ đồ tư duy (Mind Map) để thiết kế class
# 1. Mind Map (sơ đồ tư duy) trong thiết kế class là gì?
# Mind Map (sơ đồ tư duy) trong thiết kế class là cách biểu diễn trực quan cấu trúc của một class trước khi bắt đầu viết code.
# Thay vì viết code ngay, chúng ta phân tích:
                    # Class này đại diện cho đối tượng nào trong hệ thống?
                    # Nó cần lưu trữ dữ liệu gì?
                    # Nó cần thực hiện những hành động gì?
                    # Nó liên kết với những class nào khác?
#  ===>> Sau khi có Mind Map, việc viết code sẽ dễ dàng hơn, giảm lỗi thiết kế và dễ mở rộng hệ thống.

# 2. Lợi ích của việc vẽ Mind Map trước khi code
        #    Hiểu rõ yêu cầu hệ thống.
        #    Xác định đúng trách nhiệm của class
        #    Xác định thuộc tính và phương thức trước
        #    Dễ thiết kế quan hệ giữa các class
# Ví dụ:
# Yêu cầu: Xây dựng hệ thống quản lý kho hàng

# Nếu code ngay có thể viết:
class InventoryManager:
    pass
        #  Nhưng chưa biết: 
                # Kho quản lý sản phẩm gì?
                # Có nhập kho không?
                # Có xuất kho không?
                # Có kiểm tra tồn kho không?
                # ===> Mind Map giúp phân tích trước những điều này.

# Theo nguyên lý Single Responsibility Principle (SRP) trong OOP:
            #    Một class nên có một trách nhiệm chính
            #    Ví dụ: 
            # class InventoryManager có trách nhiệm:
                # Quản lý tồn kho
                # Thêm sản phẩm
                # Xóa sản phẩm
                # Cập nhật số lượng
                # Không nên:
                    #   Gửi email khách hàng
                    #   Thanh toán
                    #   Quản lý ttài khoản người dùng.
# Mind map giúp trả lời:
    #    Class cần lưu dữ liệu gì?
    #    Ví dụ:
    #         InventoryManager
                    # Attributes:
                            #  inventory_id
                            #   products
                            #   total_items
    # Class làm được gì?
    #     Ví dụ:
    #         InventoryManager
                    # Methods:
                            #  add_product()
                            #  remove_product()
                            #  update_stock()
                            #  check_inventory()
# Một kho hàng có nhiều sản phẩm: 
# class InventoryManager:
#     def __init__(self):
#         self.products = []

# Mô tả Mind Map cho class InventoryManager
    # Trung tâm:
            #                   InventoryManager(Quản lý kho hàng)
    # Nhánh 1: Attributes (Thuộc tính)
            #   Các dữ liệu mà object InventoryManager cần lưu.
            
            # InventoryManager
            #     ↓
            #     Attributes
            #     ↓                         ↓                          ↓                                        ↓
            #     inventory_id : int        warehouse_name : str       products : list                          total_items : int
            #      Access: private          Access: public             Access: private                           Access: public
            #      Ý nghĩa:Mã kho hàng      Ý nghĩa: Tên kho           Ý nghĩa: Danh sách sản phẩm trong kho     Ý nghĩa: Tổng số lượng sản phẩm  
    
    # Nhánh 2: Methods(Phương thức)
            #  Các hành động mà InventoryManager thực hiện.
            
            # InventoryManager
                        #     ↓
                        #     Methods
                        #     ↓                            ↓                          ↓                                        ↓                          ↓ 
                        #     add_product()                 remove_product()       update_stock()                          check_inventory()             calculate_total_items()
                        #     Input:Product object          Input:product_id       Input:product_id, quantity                           
                        #     Output:Thêm sản phẩm vào kho  Output:Xóa sản phẩm    Output:Cập nhật số lượng tồn kho        Output:Danh sách sản phẩm     Output:Tổng số lượng hàng
    
    # Nhánh 3:Relationships (Quan hệ với class khác)
    #         InventoryManager không hoạt động độc lập. Nó liên quan đến:
    
                #    Quan hệ với Product: Một kho chứa nhiều sản phẩm
                # InventoryManager -----> Product
class Product:
    def __init__(self, id, name, quantity):
        self.id = id
        self.name = name
        self.quantity = quantity
        
                # Quan hệ với Supplier: Nhà cung cấp thực hiện cung cấp hàng cho kho
                # Supplier ----> InventoryManager
class Supplier:
    def supply_product(self):
        pass
               
                # Quan hệ với Order: Đơn hàng làm thay đổi tồn kho
                # Order ---> InventoryManager
                # Khi khách mua hàng: Order ---> InventoryManager ---> Giảm quantity

# Chuyển Mind Map thành Class Python
# Sau khi có Mind Map, ta sẽ thực hiện code:
class InventoryManager:
    def __init__(self, inventory_id, warehouse_name):
        # Private attribute
        self.__inventory_id = inventory_id
        # Public attribute
        self.warehouse_name = warehouse_name
        # Private list chứa sản phẩm
        self.__products = []
        # Tổng số lượng sản phẩm
        self.total_items = 0
    # Thêm sản phẩm
    def add_product(self, product):
        self.__products.append(product)
        self.total_items += product.quantity
    # Xóa sản phẩm
    def remove_product(self, product):
        self.__products.remove(product)
    # Cập nhật tồn kho
    def update_stock(self, product, quantity):
        product.quantity = quantity
        
    # Kiểm tra kho
    def check_inventory(self):
        return self.__products
    
    # Tính tổng số lượng
    def calculate_total_items(self):
        total = 0
        for product in self.__products:
            total += product.quantity
        return total
    
# Phần 2: Thực hành
# (Tạo class cho hệ thống thương mại điện tử - E-Commerce System)

#  Bài tập 1: Xây dựng class Product 
# Xây dựng một class Product với các yêu cầu sau:  
# • Thuộc tính: product_id, name, price, quantity (tồn kho), category  
# • Hàm __init__() khởi tạo các thuộc tính trên  
# • Phương thức apply_discount(discount_percent): giảm giá sản phẩm (trả về giá sau  giảm)  
# • Phương thức is_in_stock(): kiểm tra xem sản phẩm còn trong kho hay không 
# Yêu cầu: Viết code và chạy với 2-3 sản phẩm khác nhau. 

class Product:
    """Class Product dùng để quản lý thông tin một sản phẩm."""
    # Hàm __init__(): 
            # Hàm khởi tạo các thuộc tính: product_id, name, price, quantity (tồn kho), category
    
    def __init__(self, product_id, name, price, quantity, category):
        # Mã sản phẩm
        self.product_id = product_id
        # Tên sản phẩm
        self.name = name
        # Giá sản phẩm
        self.price = price
        # Số lượng 
        self.quantity = quantity
        # Danh mục sản phẩm
        self.category = category
    # Phương thức giảm giá sản phẩm
    # discount_percent: phần trăm giảm giá
    # Ví dụ:  giảm 10% => 10 
    def apply_discount(self, discount_percent):
        # Tính số tiền được giảm
        discount_amount = self.price * discount_percent/100
        # Giá sau khi giảm
        new_price = self.price - discount_amount
        # Trả về giá sau khi giảm
        return new_price
    
    #  • Phương thức is_in_stock(): kiểm tra xem sản phẩm còn trong kho hay không 
    def is_in_stock(self):
        if self.quantity > 0:
            return True
        else:
            return False
        
    # Tạo các đối tượng Product
    
product1 = Product("P001", "Laptop Dell", 20000000, 5, "Laptop")
product2 = Product("P002", "Chuột Logitech", 500000, 0, "Phụ kiện")
product3 = Product("P003", "Bàn phím cơ", 1500000, 12, "Phụ kiện")

# Hiển thị thông tin sản phẩm
print("Thông tin của sản phẩm")
products = [product1, product2, product3]

for product in products:
    
    
    print("=" * 40) # Lặp lại kí tự = 40 lần để tạo đường phân cách giúp kết quả dễ đọc hơn.
    
    print("Mã sản phẩm: ", product.product_id)
    print("Tên sản phẩm: ", product.name)
    print("Giá gốc: ", format(product.price, ","), "VND")
    # Giảm giá 10%
    print("Giá sau khi giảm giá 10%: ", format(int(product.apply_discount(10)), ","), "VND")
    print("Số lượng tồn: ", product.quantity)
    print("Danh mục: ", product.category)
    
    # Kiểm tra tồn kho:
    if product.is_in_stock():
        print("Trạng thái: Còn hàng")
    else:
        print("Trạng thái: Hết hàng")
# # Kết quả: 


# Thông tin của sản phẩm
# ========================================
# Mã sản phẩm:  P001
# Tên sản phẩm:  Laptop Dell
# Giá gốc:  20,000,000 VND
# Giá sau khi giảm giá 10%:  18,000,000 VND
# Số lượng tồn:  5
# Danh mục:  Laptop
# Trạng thái: Còn hàng
# ========================================
# Mã sản phẩm:  P002
# Tên sản phẩm:  Chuột Logitech
# Giá gốc:  500,000 VND
# Giá sau khi giảm giá 10%:  450,000 VND
# Số lượng tồn:  0
# Danh mục:  Phụ kiện
# Trạng thái: Hết hàng
# ========================================
# Mã sản phẩm:  P003
# Tên sản phẩm:  Bàn phím cơ
# Giá gốc:  1,500,000 VND
# Giá sau khi giảm giá 10%:  1,350,000 VND
# Số lượng tồn:  12
# Danh mục:  Phụ kiện
# Trạng thái: Còn hàng


# Bài tập 2: Xây dựng class Customer với Encapsulation 
# Xây dựng class Customer (khách hàng) với:  
# • Thuộc tính public: customer_id, name 
# • Thuộc tính protected: _email  
# • Thuộc tính private: __password, __credit_balance (số dư tài khoản)  
# • Hàm getter và setter cho __credit_balance (setter chỉ cho phép giá trị >= 0)  
# • Phương thức add_credit(amount): nạp tiền vào tài khoản  
# • Phương thức use_credit(amount): sử dụng tiền từ tài khoản (kiểm tra đủ số dư)  
# Yêu cầu: Kiểm tra access control - đảm bảo không thể truy cập trực tiếp __password từ bên ngoài
class Customer:
    def __init__(self, customer_id, name, email, password, credit_balance = 0):
        # Thuộc tính public
        self.customer_id = customer_id
        self.name = name
        # Thuộc tính protect
        self._email = email
        # Thuộc tính private
        self.__password = password
        self.__credit_balance = credit_balance
    # Hàm Getter cho  __credit_balance
    def get_credit_balance(self):
        return self.__credit_balance
    # Hàm setter cho  __credit_balance
    def  set_credit_balance(self, amount):
        if amount >= 0:
            self. __credit_balance = amount
        else:
            print("Số dư không được nhỏ hơn 0.")
            
    # nạp tiền vào tài khoản 
    def add_credit(self, amount):
        if amount > 0:
            self. __credit_balance += amount
            print(f"Nạp {amount:,} VND thành công.")
            print(f"Số dư hiện tại: {self. __credit_balance:,} VND")
        else:
            print("Số tiền nạp phải lớn hơn 0.")
    # Sử dụng tiền
    def use_credit(self, amount):
        if amount <= 0:
            print("Số tiền sử dụng phải lớn hơn 0.")
        elif amount > self.__credit_balance:
            print("Không đủ số dư để thực hiện giao dịch.")
        else:
            self.__credit_balance -= amount
            print(f"Đã sử dụng {amount: ,} VND.")
            print(f"Số dư còn lại: {self.__credit_balance:,} VND.")
# Tạo object Customer

customer = Customer(
    "C001",
    "Dang Minh Anh",
    "dangminhanh@gmail.com",
    "MA09090909",
    500000
)
# Truy cập thuộc tính public
print("Mã khách hàng: ", customer.customer_id)
print("Tên khách hàng: ", customer.name)
# Kết quả:
            # Mã khách hàng:  C001
            # Tên khách hàng:  Dang Minh Anh

# Truy cập thuộc tính protected
print("Email: ", customer._email)
# Kết quả:
            
            # Email:  dangminhanh@gmail.com
# Truy  cập credit balance thông qua getter
print(f"Số dư tài khoản:  {customer.get_credit_balance()} VND")

# Kết quả:
            
            # Số dư tài khoản:  500000 VND
            
# Nạp tiền vào tài khoản
customer.add_credit(200000)
# Kết quả:
            # Nạp 200,000 VND thành công.
            # Số dư hiện tại: 700,000 VND
            
# Sử dụng tiền
customer.use_credit(-1) #===> Số tiền sử dụng phải lớn hơn 0.
customer.use_credit(0)  #  ===> Số tiền sử dụng phải lớn hơn 0.
customer.use_credit(300000)
# Kết quả:
            # Đã sử dụng  300,000 VND.
            # Số dư còn lại: 400,000 VND.

# Kiểm tra setter
customer.set_credit_balance(100000)
print(f"Số dư tài khoản được update mới nhất: {customer.get_credit_balance()} VND." )

# Kết quả:
            # Số dư tài khoản được update mới nhất: 100000 VND.
# Thử đặt số dư tài khoản là số âm.
customer.set_credit_balance(-500000)
# # Kết quả:
            # Số dư không được nhỏ hơn 0.

# Kiểm tra lại số dư tài khoản:
print(f"Số dư tài khoản hiện tại là: {customer.get_credit_balance()} VND")
# # Kết quả:
            # Số dư tài khoản hiện tại là: 100000 VND

# Kiểm tra Private __password từ bên ngoài
try: 
    print(customer.__password)
except AttributeError:
    print("Không thể truy cập trực tiếp __password từ bên ngoài.")
# Kết quả:
#         #  Không thể truy cập trực tiếp __password từ bên ngoài.


# Bài tập 3: Xây dựng class Order và tính tổng tiền 
# Xây dựng class Order (đơn hàng) với:  
# • Thuộc tính: order_id, customer (đối tượng Customer), order_date, items (danh sách  các sản phẩm đã mua), quantities (danh sách số lượng)  
# • Phương thức add_item(product, quantity): thêm sản phẩm vào đơn hàng 
# • Phương thức calculate_total(): tính tổng tiền đơn hàng  
# • Phương thức apply_discount(discount_percent): áp dụng mã giảm giá cho toàn bộ đơn  

# Yêu cầu: Tạo 2-3 đơn hàng với sản phẩm khác nhau và kiểm tra tính tổng 

class Order:
    def __init__(self, order_id, customer, order_date):
        # Mã đơn hàng
        self.order_id = order_id
        # Đối tượng Customer
        self.customer = customer
        # Ngày đặt hàng
        self.order_date = order_date
        # Danh sách sản phẩm
        self.items = []
        # Danh sách số lượng tương ứng với từng sản phẩm
        self.quantities = []
        # Phần trăm giảm giá 
        self.discount_percent = 0
    
        
     # Phương thức thêm sản phẩm vào giỏ hàng
    def add_item(self,product, quantity):
         self.items.append(product)
         self.quantities.append(quantity)
    # Tính tổng tiền đơn hàng.
    def calculate_total(self):
        #Biến lưu tổng tiền
        total = 0
        for i in range(len(self.items)):
            # Lấy sản phẩm tại vị trí i
            product = self.items[i]
            # Lấy số lượng tương ứng
            quantity = self.quantities[i]
            # tính total
            total = total + product.price * quantity
        return total
    def apply_discount(self, discount_percent):
        # Lưu phần trăm giảm giá
        self.discount_percent = discount_percent
        # tính tổng tiền trước khi giảm
        total = self.calculate_total()
        # Tính số tiền được giảm
        discount_amount = total * discount_percent/100
        # Tính số tiền cuối cùng
        final_total = total - discount_amount
        return final_total
# tạo sản phẩm (Class Product ở bài 1)
product4 = Product( "P004","Laptop",20000000,10,"Electronics")
product5 = Product("P005","Mouse",500000,50,"Accessories")
product6 = Product("P006","Keyboard",1000000,30,"Accessories"
)
# Tạo khách hàng (class Customer ở bài 2)
customer4 = Customer("C004", "Vy Tuoi", "vy@gmail.com", "T89720974209", 50000000)
customer5 = Customer("C004", "Dang Tuan", "dang@gmail.com", "D8978738909", 30000000)

# Tạo đơn hàng 1
order4 = Order("ORD004", customer4, "2026-08-10")
order4.add_item(product4, 2)
order4.add_item(product5, 3)
# Tạo đơn hàng 2
order5 = Order("ORD005", customer5, "2026-08-10")
order5.add_item(product6, 2)
order5.add_item(product5, 2)
# Tính tiền
total4 = order4.calculate_total()
total5 = order5.calculate_total()

print("Đơn hàng: ", order4.order_id)
print("Khách hàng: ", order4.customer.name)
print("Tổng tiền:", format(total4, ","))

print("-" * 40)

print("Đơn hàng:", order5.order_id)
print("Khách hàng:", order5.customer.name)
print("Tổng tiền:", format(total5, ","))

# Kết quả
                # Đơn hàng:  ORD004
                # Khách hàng:  Vy Tuoi
                # Tổng tiền: 41,500,000


# ----------------------------------------
                # Đơn hàng: ORD005
                # Khách hàng: Dang Tuan
                # Tổng tiền: 3,000,000

# Áp dụng giảm giá
final_total4 = order4.apply_discount(10)
print("-" * 40)
print("Đơn hàng 4 sau giảm 10%:",
      format(final_total4, ","))
# Kết quả:
# Đơn hàng 4 sau giảm 10%: 37,350,000.0

# Bài tập 4: Kế thừa - Tạo class SpecialCustomer từ Customer 
# Xây dựng class SpecialCustomer kế thừa từ Customer với:  
# • Thêm thuộc tính: loyalty_points (điểm thành viên), loyalty_level (mức VIP: Bronze,  Silver, Gold)  
# • Override phương thức __init__() sử dụng super() 
# • Phương thức add_loyalty_points(points): tích lũy điểm từ mỗi mua hàng  
# • Phương thức get_discount(): trả về mức giảm giá dựa trên loyalty_level (Bronze: 5%,  Silver: 10%, Gold: 15%)  
# • Phương thức __str__(): in thông tin khác với Customer thường  
# Yêu cầu: Tạo một SpecialCustomer, mua hàng, tích lũy điểm và xem mức giảm giá  tương ứng. 

# class Customer
class Customer:
    def __init__(self, customer_id, name, email, password, credit_balance = 0):
        # Thuộc tính public
        self.customer_id = customer_id
        self.name = name
        # Thuộc tính protect
        self._email = email
        # Thuộc tính private
        self.__password = password
        self.__credit_balance = credit_balance
    # Hàm Getter cho  __credit_balance
    def get_credit_balance(self):
        return self.__credit_balance
    # Hàm setter cho  __credit_balance
    def  set_credit_balance(self, amount):
        if amount >= 0:
            self. __credit_balance = amount
        else:
            print("Số dư không được nhỏ hơn 0.")
            
    # nạp tiền vào tài khoản 
    def add_credit(self, amount):
        if amount > 0:
            self. __credit_balance += amount
            print(f"Nạp {amount:,} VND thành công.")
            print(f"Số dư hiện tại: {self. __credit_balance:,} VND")
        else:
            print("Số tiền nạp phải lớn hơn 0.")
    # Sử dụng tiền
    def use_credit(self, amount):
        if amount <= 0:
            print("Số tiền sử dụng phải lớn hơn 0.")
        elif amount > self.__credit_balance:
            print("Không đủ số dư để thực hiện giao dịch.")
        else:
            self.__credit_balance -= amount
            print(f"Đã sử dụng {amount: ,} VND.")
            print(f"Số dư còn lại: {self.__credit_balance:,} VND.")
            
# class SpecialCustomer  Kế thừa từ class Customer
class SpecialCustomer(Customer):
    """SpecialCustomer là khách hàng VIP.
       Kế thừa từ class Customer."""
    def __init__(self, 
                 customer_id, 
                 name, 
                 email, 
                 password, 
                 credit_balance=0,
                 loyalty_points=0,
                 loyalty_level="Bronze"
                 ):
        """Khởi tạo khách hàng VIP"""
        """Gọi__init__ của class Customer. """
        
        super().__init__(
            customer_id, 
            name, email, 
            password, 
            credit_balance)
        
        # Các thuộc tính riêng của SpecialCustomer
        self.loyalty_points = loyalty_points
        self.loyalty_level = loyalty_level
        
        # Phương thức add_loyalty_points
    def add_loyalty_points(self, points):
        """Cộng thêm điểm thành viên"""
        if points > 0:
            self.loyalty_points += points
            print(
                f"Đã cộng {points} điểm."
                f"Tổng điểm: {self.loyalty_points}"
                  )
        else:
            print("Số điểm phải lớn hơn 0.")
    
    # Phương thức GET_DISCOUNT()
    def get_discount(self):
        """ Trả về mức giá dựa trên loyalty_level"""
        if self.loyalty_level == "Bronze":
            return 5
        if self.loyalty_level == "Silver":
            return 10
        if self.loyalty_level == "Gold":
            return 15
    
    # OVERRIDE __STR__()
    

    def __str__(self):
            """Override __str__() của Customer.
               Hiển thị thêm thông tin VIP.
               """
            return(
            f"Special Customer ID: {self.customer_id}\n"
            f"Tên: {self.name}\n"
            f"Email: {self._email}\n"
            f"Số dư: {self.get_credit_balance():,} VNĐ\n"
            f"Điểm thành viên: {self.loyalty_points}\n"
            f"Cấp độ VIP: {self.loyalty_level}\n"
            f"Giảm giá: {self.get_discount()}%"
            )
    # Sử dụng
    
    # Tạo một khách VIP
special_customer = SpecialCustomer(
    customer_id="SC001",
    name="Nguyễn Văn A",
    email="a@gmail.com",
    password="123456",
    credit_balance=1_000_000,
    loyalty_points=100,
    loyalty_level="Gold"
)
# Hiển thị thông tin khách hàng VIP
# ---------------------------------------------------------

print("=" * 50)
print("THÔNG TIN KHÁCH HÀNG VIP")
print("=" * 50)

print(special_customer)

# Kết quả:
# ==================================================
# THÔNG TIN KHÁCH HÀNG VIP
# ==================================================
# Special Customer ID: SC001
# Tên: Nguyễn Văn A
# Email: a@gmail.com
# Số dư: 1,000,000 VNĐ
# Điểm thành viên: 100
# Cấp độ VIP: Gold
# Giảm giá: 15%

# Khách hàng mua hàng
# ---------------------------------------------------------

print("\n" + "=" * 50)
print("MUA HÀNG")
print("=" * 50)

purchase_amount = 500_000

print(f"Giá trị đơn hàng: {purchase_amount:,} VNĐ")


# Tích lũy điểm
# Ví dụ: mỗi 10.000 VNĐ = 1 điểm
# ---------------------------------------------------------

points_earned = purchase_amount // 10_000

special_customer.add_loyalty_points(points_earned)


# ---------------------------------------------------------
# Xem mức giảm giá
# ---------------------------------------------------------

print("\n" + "=" * 50)
print("THÔNG TIN SAU KHI MUA HÀNG")
print("=" * 50)

print(f"Điểm thành viên: {special_customer.loyalty_points}")
print(f"Cấp độ VIP: {special_customer.loyalty_level}")
print(f"Mức giảm giá: {special_customer.get_discount()}%")

# Kết quả:
# ==================================================
# MUA HÀNG
# ==================================================
# Giá trị đơn hàng: 500,000 VNĐ
# Đã cộng 50 điểm.Tổng điểm: 150

# ==================================================
# THÔNG TIN SAU KHI MUA HÀNG
# ==================================================
# Điểm thành viên: 150
# Cấp độ VIP: Gold
# Mức giảm giá: 15%

# Bài tập 5:
# Polymorphism (Đa )
# - Tạo class cho các loại sản phẩm khác nhau 
# Xây dựng 3 class kế thừa từ Product: 
# 1. PhysicalProduct (sản phẩm vật lý): thêm thuộc tính weight (cân nặng), shipping_fee  (phí vận chuyển)  
# 2. DigitalProduct (sản phẩm số): thêm thuộc tính file_size (MB), license_type (một lần /  vĩnh viễn)  
# 3. ServiceProduct (dịch vụ): thêm thuộc tính duration_days (ngày dùng), renewal_fee  (phí gia hạn)  
# Mỗi class phải override phương thức calculate_final_price():  
# - PhysicalProduct: giá + phí vận chuyển  
# - DigitalProduct: nếu license_type = 'one-time' thì giảm 20%, không thì giá gốc 
# - ServiceProduct: tính giá cho duration_days, có phí gia hạn  
# Yêu cầu: Tạo danh sách sản phẩm hỗn hợp, duyệt qua và in giá cuối cùng của mỗi sản  phẩm. 

# Product
#    │
#    ├── PhysicalProduct
#    ├── DigitalProduct
#    └── ServiceProduct
        #   ===> Cả 3 class con đều có cùng một phương thức:
        #                      calculate_final_price()
        #   Nhưng mỗi class tính giá theo cách khác nhau.
        #  ===> Cùng gọi calculate_final_price(), nhưng tùy đối tượng thuộc class nào mà Python thực hiện cách tính tương ứng.

# CLASS CHA: 
class Product:
    """Class cha Product: 
      Dùng để tạo thông tin cơ bản cho sản phẩm.
    """
    def __init__(self, product_id, name, price, quantity, category):
        # Mã sản phẩm
        self.product_id = product_id
        # Tên sản phẩm
        self.name = name 
        # Giá sản phẩm
        self.price = price
        # Số lượng
        self.quantity = quantity
        # Danh mục sản phẩm
        self.category = category
    def calculate_final_price(self):
        """
        Phương thức tính giá cuối cùng.
        Class con sẽ override(ghi đè) phương thức này
        """
        return self.price

# Class PhysicalProduct
# Sản phẩm vật lý
class PhysicalProduct(Product):
    def __init__(self, product_id, name, price, quantity, category, weight, shipping_fee):
        # Gọi __init__() của class cha(class Product)
        super().__init__(product_id, name, price, quantity, category)
        # Cân nặng sản phẩm
        self.weight = weight
        # Phí vận chuyển
        self.shipping_fee = shipping_fee
    def calculate_final_price(self):
        """Giá cuối cùng của sản phẩm vật lý.
           Giá sản phẩm + phí vận chuyển
           
        """
        return self.price + self.shipping_fee
# Class DigitalProduct
# Sản phẩm số

class DigitalProduct(Product):
    def __init__(self, product_id, name, price, quantity, category, file_size, license_type):
        # Gọi __init__ của class cha(Class Product)
        super().__init__(product_id, name, price, quantity, category)
        # Kích thước file, Đơn vị MB
        self.file_size = file_size
        # Loại bản quyền
        # "one-time" = mua một lần
        # "permanent" = vĩnh viễn
        self.license_type = license_type
    def calculate_final_price(self):
        """Nếu license_type là "one-time":
               giảm 20%
           Nếu không: Giữ nguyên giá gốc.
        """
        if self.license_type == "one-time":
            # Giảm 20%
            final_price = self.price * 0.8
        else:
            # Không giảm 
            final_price = self.price
        return final_price        

# class ServiceProduct
# Sản phẩm dịch vụ
class ServiceProduct(Product):
    def __init__(self, product_id, name, price, quantity, category, duration_days, renewal_fee):
        #  Gọi __init__() của class cha(class Product)
        super().__init__(product_id, name, price, quantity, category)
        #  Số ngày sử dụng dịch vụ
        self.duration_days = duration_days
        # Phí gia hạn
        self.renewal_fee = renewal_fee
    def calculate_final_price(self):
        """Tính giá dịch vụ dựa trên số ngày sử dụng và
           cộng thêm phí gia hạn.
           Giả sử: price = giá cho 30 ngày
                   duration_days = Số ngày sử dụng
            => Công thức:
            Giá dịch vụ = price/30 * duration_days
            Sau đó cộng phí gia hạn.
        """
        service_price = (
            self.price/30) * self.duration_days
        final_price = service_price + self.renewal_fee
        return final_price
# Tạo các sản phẩm
sanphamvatly = PhysicalProduct(
    "SP001",
    "Laptop",
    20000000,
    10,
    "Elictronics",
    2.5,
    500000
)
# Sản phẩm số
sanphamso = DigitalProduct(
    "SP002",
    "Python Course",
    5000000,
    100,
    "Education",
    500,
    "one-time"
    
)

# Sản phẩm dịch vụ
sanphamdichvu = ServiceProduct(
    "SP003",
    "Cloua Storage",
    300000,
    50,
    "Cloud Service",
    90,
    50000
)
# Tạo danh sách sản phẩm hỗn hợp
products = [sanphamvatly, sanphamso, sanphamdichvu]

# Duyệt qua danh sách sản phẩm và tính giá
for product in products:
    print("=" * 50)
    print("Mã sản phẩm: ", product.product_id) 
    print("Tên sản phẩm: ", product.name)
    print("Giá gốc: ", format(product.price, ","))
    # Gọi cùng một phương thức
    # Nhưng mỗi class sẽ có cách tính khác nhau.
    final_price = product.calculate_final_price()
    print("Giá cuối cùng: ", format(final_price, ","))
print("=" * 50)

# Kết quả:
# ==================================================
# Mã sản phẩm:  SP001
# Tên sản phẩm:  Laptop
# Giá gốc:  20,000,000
# Giá cuối cùng:  20,500,000
# ==================================================
# Mã sản phẩm:  SP002
# Tên sản phẩm:  Python Course
# Giá gốc:  5,000,000
# Giá cuối cùng:  4,000,000.0
# ==================================================
# Mã sản phẩm:  SP003
# Tên sản phẩm:  Cloua Storage
# Giá gốc:  300,000
# Giá cuối cùng:  950,000.0
