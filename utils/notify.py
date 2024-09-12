import tkinter as tk
from PIL import Image, ImageTk
import threading


def notify_interface(icon: str, title: str, message: str, timeout: int = (60 * 5)):
    # Create root window and hide it
    root = tk.Tk()
    root.withdraw()

    window_height = 156  # Increased height to accommodate the button
    window_width = 400

    # Create the notification window
    notification_window = tk.Toplevel(root)
    notification_window.overrideredirect(True)  # Remove window borders
    notification_window.geometry(f"{window_width}x{window_height}")
    notification_window.config(bg="white")

    # Make sure the notification window stays on top
    notification_window.attributes("-topmost", True)

    # Initial position: Start below the screen (for slide-up animation)
    screen_width = notification_window.winfo_screenwidth()
    screen_height = notification_window.winfo_screenheight()
    x = screen_width - window_width  # X offset to position from right edge
    y = screen_height  # Start just below the screen
    notification_window.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # Load and resize the icon
    icon = Image.open(icon)
    icon = icon.resize((60, 60), Image.Resampling.LANCZOS)
    icon_img = ImageTk.PhotoImage(icon)

    # Create container for layout
    container = tk.Frame(notification_window, bg="white")
    container.pack(padx=16, pady=16)

    # Add image label
    image_label = tk.Label(container, image=icon_img, bg="white")
    image_label.pack(side=tk.LEFT, padx=10)

    # Text container
    text_container = tk.Frame(container, bg="white")
    text_container.pack(side=tk.LEFT, fill=tk.BOTH)

    # Title
    title_label = tk.Label(text_container, text=title, font=("Segoe UI", 14, "bold"), bg="white")
    title_label.pack(anchor="w")

    # Message
    message_label = tk.Label(text_container, text=message, font=("Segoe UI", 12), bg="white")
    message_label.pack(anchor="w")

    # Create close button
    def close_notification():
        notification_window.destroy()

    close_button = tk.Button(
        notification_window,
        text="Got it",
        font=("Segoe UI", 12, "bold"),
        background="#1dbf73",  # Blue color as per the tailwindcss
        foreground="white",
        activebackground="#19a463",  # Hover effect color
        activeforeground="white",
        relief="flat",
        borderwidth=0,
        command=close_notification
    )
    close_button.pack(fill=tk.X, padx=16, pady=10)

    # Slide-up animation function
    def slide_up(y_pos):
        if y_pos > (screen_height - (46 + window_height)):  # Target position
            y_pos -= 1  # Move up 1 pixel at a time
            notification_window.geometry(f"{window_width}x{window_height}+{x}+{y_pos}")
            notification_window.after(5, lambda: slide_up(y_pos))  # Repeat after 5 ms

    # Start the slide-up animation
    slide_up(y)

    notification_window.after(timeout * 1000, notification_window.destroy)

    # Keep the window alive
    root.mainloop()

def notify(icon: str, title: str, message: str, timeout: int = (60 * 5)):
    def init_notify():
        notify_interface(icon, title, message, timeout)
    threading.Thread(target=init_notify).start()
