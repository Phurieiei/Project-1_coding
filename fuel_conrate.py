import tkinter as tk
from tkinter import messagebox

def fuel_consumption_rate():
    try:
        cartype = car_type_var.get()
        if cartype not in ["O", "H"]:
            messagebox.showerror("ข้อผิดพลาด", "กรุณาเลือกประเภทของรถยนต์ให้ถูกต้อง")
            return
        
        d = float(distance_entry.get())
        c = float(fuel_entry.get())

        if d <= 0 or c <= 0:
            messagebox.showerror("ข้อผิดพลาด", "กรุณากรอกค่าที่มากกว่า 0")
            return

        result = (c * 100) / d
        messagebox.showinfo("ผลลัพธ์", f"มีอัตราการสิ้นเปลืองน้ำมัน: {result:.2f} ลิตร/100กิโลเมตร")

    except ValueError:
        messagebox.showerror("ข้อผิดพลาด", "กรุณากรอกตัวเลขที่ถูกต้อง")

# สร้างหน้าต่างหลัก
root = tk.Tk()
root.title("คำนวณอัตราการสิ้นเปลืองน้ำมัน")
root.geometry("400x350")

# หัวข้อใหญ่ขึ้น
tk.Label(root, text="คำนวณอัตราการสิ้นเปลืองน้ำมัน", font=("Arial", 16, "bold")).pack(pady=10)

# เลือกชนิดของรถ
tk.Label(root, text="เลือกชนิดของรถยนต์:", font=("Arial", 12)).pack()
car_type_var = tk.StringVar(value="O")
tk.Radiobutton(root, text="Oil (O)", variable=car_type_var, value="O", font=("Arial", 12)).pack()
tk.Radiobutton(root, text="Hybrid (H)", variable=car_type_var, value="H", font=("Arial", 12)).pack()

# กรอกระยะทาง
tk.Label(root, text="ระยะทางที่เดินทาง (กม.):", font=("Arial", 12)).pack()
distance_entry = tk.Entry(root, font=("Arial", 12))
distance_entry.pack()

# กรอกปริมาณน้ำมัน
tk.Label(root, text="ปริมาณน้ำมันที่ใช้ (ลิตร):", font=("Arial", 12)).pack()
fuel_entry = tk.Entry(root, font=("Arial", 12))
fuel_entry.pack()

# ปุ่มคำนวณ
tk.Button(root, text="คำนวณ", font=("Arial", 12, "bold"), command=fuel_consumption_rate).pack(pady=10)

# เริ่ม GUI
root.mainloop()
