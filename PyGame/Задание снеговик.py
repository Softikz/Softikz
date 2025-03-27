import tkinter as tk
import random
import webbrowser

search_engines = {
    "Google": "https://www.google.com/search?q=",
    "Wikipedia": "https://en.wikipedia.org/wiki/",
    "YouTube": "https://www.youtube.com/results?search_query=",
    "DuckDuckGo": "https://duckduckgo.com/?q=",
    "Bing": "https://www.bing.com/search?q=",
    "Unsplash": "https://unsplash.com/s/photos/"
}

def perform_search():
    query = entry.get().strip()
    if not query:
        status_label.config(text="Введите запрос!", fg="red")
        return

    search_engine, url = random.choice(list(search_engines.items()))
    search_url = url + query.replace(" ", "+")
    
    status_label.config(text=f"Поиск через: {search_engine}", fg="green")
    webbrowser.open(search_url)
    
    history_list.insert(tk.END, f"{search_engine}: {query}")

root = tk.Tk()
root.title("Поисковик")
root.geometry("500x500")

entry_label = tk.Label(root, text="Введите запрос:", font=("Arial", 14))
entry_label.pack(pady=10)

entry = tk.Entry(root, width=40, font=("Arial", 14))
entry.pack(pady=10)

search_button = tk.Button(root, text="Искать!", command=perform_search, bg="blue", fg="white", font=("Arial", 14, "bold"))
search_button.pack(pady=15)

status_label = tk.Label(root, text="", fg="black", font=("Arial", 12))
status_label.pack(pady=10)

history_label = tk.Label(root, text="История запросов:", font=("Arial", 14))
history_label.pack(pady=10)

history_list = tk.Listbox(root, height=10, width=50, font=("Arial", 12))
history_list.pack(pady=10)

root.mainloop()
