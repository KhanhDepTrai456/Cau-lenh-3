# Import thư viện cần thiết
from eth_account import Account
import sys

try:
    # Kích hoạt tính năng HD wallet (cần thiết để tạo mnemonic)
    # HD wallet cho phép tạo nhiều địa chỉ ví từ một cụm từ gốc
    Account.enable_unaudited_hdwallet_features()

    # Tạo tài khoản mới với cụm từ mnemonic
    # - account: chứa thông tin về khóa bí mật và địa chỉ
    # - mnemonic: cụm từ gồm 12 từ để khôi phục ví
    # num_words=12: chỉ định số từ trong cụm từ mnemonic
    account, mnemonic = Account.create_with_mnemonic(num_words=12)

    # Lấy khóa bí mật dưới dạng hex string
    # hex() chuyển số thành chuỗi hexa, bỏ tiền tố '0x'
    private_key = account.key.hex()[2:]

    # Lấy địa chỉ ví (dạng chuẩn EVM)
    address = account.address

    try:
        # Mở file để ghi thông tin
        # 'w' nghĩa là ghi mới (xóa nội dung cũ nếu có)
        with open('wallet_info.txt', 'w') as f:
            # Ghi cụm từ mnemonic và khóa bí mật, mỗi thông tin một dòng
            f.write(f"{mnemonic}\n")  # Dòng 1: Cụm từ mnemonic
            f.write(f"{private_key}")   # Dòng 2: Khóa bí mật

        # Hiển thị thông tin thành công
        print("\nTạo ví thành công!")
        print(f"Địa chỉ ví của bạn là: {address}")
        print("Đã lưu cụm từ mnemonic và khóa bí mật vào file wallet_info.txt")
        print("\nLƯU Ý QUAN TRỌNG:")
        print("- Giữ bí mật file wallet_info.txt vì nó chứa thông tin nhạy cảm")
        print("- Không chia sẻ cụm từ mnemonic và khóa bí mật cho người khác")
        print("- Chỉ địa chỉ ví là thông tin có thể chia sẻ an toàn")

    except IOError as e:
        # Xử lý lỗi khi không thể ghi file
        print(f"\nLỗi: Không thể ghi file wallet_info.txt")
        print(f"Chi tiết lỗi: {str(e)}")
        sys.exit(1)

except Exception as e:
    # Xử lý các lỗi khác khi tạo ví
    print(f"\nLỗi: Không thể tạo ví")
    print(f"Chi tiết lỗi: {str(e)}")
    sys.exit(1)