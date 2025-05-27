# Import thư viện tkinter
from tkinter import *
from tkinter import messagebox

# Tạo cửa sổ chính
window = Tk()
window.title("Máy Tính Đơn Giản")
window.geometry("400x300")

# Hàm kiểm tra đầu vào có phải số tự nhiên không
def is_natural_number(str_num):
    if not str_num.isdigit():  # Kiểm tra chuỗi có chứa kí tự không phải số
        return False
    num = int(str_num)
    return num >= 0  # Số tự nhiên phải >= 0

# Hàm thực hiện phép tính
def calculate(operation):
    # Lấy giá trị từ ô nhập liệu
    num1 = entry1.get()
    num2 = entry2.get()
    
    # Kiểm tra đầu vào
    if not num1 or not num2:  # Kiểm tra ô nhập có trống không
        messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ hai số!")
        return
    
    if not is_natural_number(num1) or not is_natural_number(num2):
        messagebox.showerror("Lỗi", "Vui lòng chỉ nhập số tự nhiên!")
        return
    
    # Chuyển đổi chuỗi sang số
    num1 = int(num1)
    num2 = int(num2)
    
    # Thực hiện phép tính tương ứng
    try:
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        else:  # operation == "/"
            if num2 == 0:  # Kiểm tra chia cho 0
                messagebox.showerror("Lỗi", "Không thể chia cho 0!")
                return
            result = num1 / num2
            
        # Hiển thị kết quả
        result_label.config(text=f"Kết quả: {result}")
    except Exception as e:
        messagebox.showerror("Lỗi", f"Đã xảy ra lỗi: {str(e)}")

# Tạo và đặt vị trí các thành phần giao diện
Label(window, text="Số thứ nhất:").pack(pady=5)
entry1 = Entry(window)
entry1.pack(pady=5)

Label(window, text="Số thứ hai:").pack(pady=5)
entry2 = Entry(window)
entry2.pack(pady=5)

# Khung chứa các nút phép tính
button_frame = Frame(window)
button_frame.pack(pady=10)

# Tạo các nút phép tính
Button(button_frame, text="+", command=lambda: calculate("+"), width=5).pack(side=LEFT, padx=5)
Button(button_frame, text="-", command=lambda: calculate("-"), width=5).pack(side=LEFT, padx=5)
Button(button_frame, text="*", command=lambda: calculate("*"), width=5).pack(side=LEFT, padx=5)
Button(button_frame, text="/", command=lambda: calculate("/"), width=5).pack(side=LEFT, padx=5)

# Nhãn hiển thị kết quả
result_label = Label(window, text="Kết quả: ")
result_label.pack(pady=20)

# Chạy chương trình
window.mainloop()