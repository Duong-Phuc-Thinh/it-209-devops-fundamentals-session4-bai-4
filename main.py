import os
import subprocess

def main():
    print("=== Git Management Automation Script ===")
    
    # Tao .gitignore neu chua co
    try:
        with open(".gitignore", "w", encoding="utf-8") as f:
            f.write("credentials.txt\n")
        print("[+] Da tao/cap nhat .gitignore de bo qua credentials.txt")
    except Exception as e:
        print(f"[-] Loi khi tao .gitignore: {e}")

    print("\n[HUONG DAN CAC BUOC THUC HIEN THU CONG EMULATE CHUAN]:")
    print("1. Neu lo commit credentials.txt, chay lenh sau de xoa khoi cache ma khong xoa file vat ly:")
    print("   git rm --cached credentials.txt")
    print("2. Them file .gitignore vao khu vuc cho (Staging area):")
    print("   git add .gitignore")
    print("3. Ghi de va sua lai commit gan nhat bang cach dung --amend:")
    print("   git commit --amend -m \"Khoi tao du an va bo qua file credentials.txt\"")
    print("4. Kiem tra lai lich su va trang thai:")
    print("   git status")
    print("   git log -n 1")

if __name__ == "__main__":
    main()
