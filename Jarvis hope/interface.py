import customtkinter as ctk
from PIL import Image, ImageTk
import threading
import asyncio
from main import jarvis  # Import the jarvis function from main.py

# Initialize the main GUI application
class JarvisApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Jarvis AI Interface")
        self.geometry("1920x1080")

        # Configure appearance (Dark theme for Jarvis-like feel)
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # Load and set the futuristic background image
        self.background_image = Image.open("background.jpg")
        self.bg_image = ImageTk.PhotoImage(self.background_image)
        bg_label = ctk.CTkLabel(self, image=self.bg_image, text="")
        bg_label.place(relwidth=1, relheight=1)

        # Central chat display frame
        self.chat_frame = ctk.CTkFrame(self, corner_radius=15, fg_color="#0D1B2A", bg_color="transparent")
        self.chat_frame.place(relx=0.25, rely=0.2, relwidth=0.5, relheight=0.6)

        # Chat Display Section
        self.chat_display = ctk.CTkTextbox(
            self.chat_frame, width=400, height=400, font=("Courier New", 14), text_color="white",
            fg_color="#1B263B", corner_radius=10, wrap="word"
        )
        self.chat_display.pack(padx=20, pady=20, fill="both", expand=True)
        self.chat_display.configure(state="disabled")

        # Input Section
        self.input_frame = ctk.CTkFrame(self, corner_radius=15, fg_color="#0D1B2A", bg_color="transparent")
        self.input_frame.place(relx=0.25, rely=0.82, relwidth=0.5, relheight=0.1)

        self.input_box = ctk.CTkEntry(
            self.input_frame, font=("Courier New", 14), fg_color="#1B263B", text_color="white", placeholder_text="Type your message..."
        )
        self.input_box.pack(side="left", fill="x", padx=20, pady=20, expand=True)
        self.input_box.bind("<Return>", self.process_input)

        send_button = ctk.CTkButton(
            self.input_frame, text="Send", command=self.process_input, font=("Helvetica", 14, "bold"), corner_radius=8
        )
        send_button.pack(side="right", padx=20)

    def process_input(self, event=None):
        user_input = self.input_box.get()
        if user_input.strip():
            self.update_chat(f"You: {user_input}\n")
            self.input_box.delete(0, ctk.END)

            # Process the user input in a separate thread
            threading.Thread(target=self.get_jarvis_response, args=(user_input,), daemon=True).start()

    def update_chat(self, message):
        # Update the chat display in the main thread
        self.chat_display.configure(state="normal")
        self.chat_display.insert("end", message)
        self.chat_display.see("end")
        self.chat_display.configure(state="disabled")

    def get_jarvis_response(self, user_input):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        try:
            # Pass the user input to the jarvis function in main.py and get the response
            response = loop.run_until_complete(jarvis(user_input))  # Assuming jarvis now accepts user_input as argument
            self.after(0, self.update_chat, f"Jarvis: {response}\n")
        except Exception as e:
            self.after(0, self.update_chat, f"Jarvis: Sorry, an error occurred. {e}\n")
        finally:
            loop.close()

if __name__ == "__main__":
    app = JarvisApp()
    app.mainloop()
