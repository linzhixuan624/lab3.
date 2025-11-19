import tkinter as tk
import random


CHAR_WEIGHTS = {chr(i): i - ord('A') + 1 for i in range(ord('A'), ord('Z') + 1)}
for i in range(10):
    CHAR_WEIGHTS[str(i)] = 0 + i

KEY_PART_LENGTHS = [5, 4, 4]
PART_TARGET_AVGS = [10, 12, 8]
AVG_TOLERANCE = 0.5

def calculate_block_average(block):
    if not block:
        return 0
    total_weight = sum(CHAR_WEIGHTS[char] for char in block)
    return total_weight / len(block)

def generate_valid_block(length, target_avg):
    chars = list(CHAR_WEIGHTS.keys())
    min_avg = target_avg - AVG_TOLERANCE
    max_avg = target_avg + AVG_TOLERANCE
    
    while True:
        block = ''.join(random.choices(chars, k=length))
        avg = calculate_block_average(block)
        if min_avg <= avg <= max_avg:
            return block
        
def generate_key():
    valid_blocks = []
    for length, target_avg in zip(KEY_PART_LENGTHS, PART_TARGET_AVGS):
        valid_block = generate_valid_block(length, target_avg)
        valid_blocks.append(valid_block)
    
    key = '-'.join(valid_blocks)
    key_label.config(text=key)

window = tk.Tk()
window.geometry("500x300")
window.title("Keygen")

bg_image = tk.PhotoImage(file='mrfz.png')
lbl_bg = tk.Label(window, image=bg_image)
lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

generate_button = tk.Button(window, text="Generate a key", command=generate_key, font=("Arial", 14), bg="#24AD28", fg="white")
generate_button.pack(pady=40)

key_label = tk.Label(window, text="Click the button above", font=("Consolas", 18, "bold"), fg="white",bg="#B9318E")
key_label.pack(pady=10)

window.mainloop()
