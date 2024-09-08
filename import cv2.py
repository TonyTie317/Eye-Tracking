import tkinter as tk
import subprocess

class EyeTrackingApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Eye Tracking App")
        self.root.geometry("800x600")

        self.background_image = tk.PhotoImage(file="background.png")
        self.background_label = tk.Label(self.root, image=self.background_image)
        self.background_label.place(x=0, y=0)

        self.start_button = tk.Button(self.root, text="Start Eye Tracking", command=self.start_eye_tracking)
        self.start_button.place(x=350, y=250)

    def start_eye_tracking(self):
        self.root.destroy()  # đóng giao diện hiện tại của ứng dụng


    def run(self):
        self.root.mainloop()

# Khởi tạo và chạy ứng dụng
app = EyeTrackingApp()
app.run()
