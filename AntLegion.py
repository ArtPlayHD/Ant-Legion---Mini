import os, json, random, tkinter as tk
from tkinter import ttk, messagebox

# ===================================================================
#  ДАННЫЕ ИГРЫ
# ===================================================================

ALLIANCE_NAMES = [
    "Красные Муравьи", "Лесной Союз", "Колония Зари", "Тёмный Улей",
    "Союз Шесть Лапок", "Воины Формики", "Империя Хитина", "Племя Скарабеев",
    "Семья Термитов", "Армия Рабочих", "Стая Охотников", "Клан Строителей"
]

BOT_FIRST_NAMES = [
    "Алекс", "Борис", "Виктор", "Гена", "Денис", "Егор", "Жора", "Захар",
    "Игорь", "Костя", "Лёва", "Макс", "Никита", "Олег", "Петя", "Рома",
    "Стас", "Тимур", "Федя", "Юра"
]
BOT_LAST_NAMES = [
    "Муравьёв", "Жуков", "Хитинов", "Усиков", "Ползунов", "Скарабеев",
    "Термитов", "Формиков", "Лапкин", "Ульев", "Рабочих", "Строев"
]

BOT_PHRASES = [
    "Привет всем!", "Всем привет!", "Как дела, колония?", "Кто на рейд?",
    "Ферма прокачана до 5 уровня!", "Нужно больше ресурсов", "Королева родила!",
    "Казарма построена!", "Когда атака на термитник?", "У меня 500 воинов",
    "Союзники, нужна помощь!", "Защищайте ферм!", "Я нашёл сахар!",
    "Кто отдаст лишние ресурсы?", "Спасибо за помощь!", "Хороший альянс",
    "Идём на врага!", "Отступаем!", "Победа за нами!", "Враги у ворот!",
    "Какой ранг у всех?", "R4 — уважение!", "Нужен апгрейд лабы",
    "Склад почти полон", "Муравьи-солдаты готовы к бою", "Атака на колонию!",
    "Собираем армию", "Ресурсов мало, помогите", "Кто играет с фермой?",
    "Защита на максимуме!", "Строим башню обороны", "Лаборатория апгрейдится",
    "Открыли новый вид муравьёв!", "Сахарная ферма работает",
    "Какие исследования качать?", "Королеву охраняем!", "Тропа свободна",
    "Враг отброшен!", "Трофеи собраны", "Нужна координация",
    "Кто на защите гнезда?", "Муравьи-работяги — сила!", "Рад всех видеть",
    "Добрый вечер, муравьи!", "Удачи в рейде!", "Хорошая игра сегодня","Событие было запущено","Привет,ArtPlayHD,с gitHub!"
]

CAREERS = [
    "Воин", "Строитель", "Собиратель", "Учёный", "Защитник",
    "Разведчик", "Медик", "Командир", "Дипломат", "Кочевник"
]

CAREER_DESC = {
    "Воин":       "⚔️ Атака и защита. Сильные бойцы.",
    "Строитель":  "🔨 Быстрая постройка зданий.",
    "Собиратель": "🌾 Бонус к добыче пищи.",
    "Учёный":     "🔬 Ускоряет исследования.",
    "Защитник":   "🏰 Усиливает оборону колонии.",
    "Разведчик":  "🔍 Находит ресурсы быстрее.",
    "Медик":      "💊 Лечит раненых муравьёв.",
    "Командир":   "🎖️ Командует армией в рейдах.",
    "Дипломат":   "🤝 Укрепляет связи в альянсе.",
    "Кочевник":   "🧭 Бонус к перемещению войск.",
}

RANKS = ["R1", "R2", "R3", "R4"]

RANK_RIGHTS = {
    "R1": ["Чтение чата", "Участие в рейдах"],
    "R2": ["Чтение чата", "Участие в рейдах", "Донат ресурсов"],
    "R3": ["Чтение чата", "Участие в рейдах", "Донат ресурсов", "Приём в альянс", "Чат альянса"],
    "R4": ["Чтение чата", "Участие в рейдах", "Донат ресурсов", "Приём в альянс",
           "Чат альянса", "Повышение/понижение рангов", "Объявление войны", "Роспуск альянса"],
}

RANK_COLORS = {"R4": "#FFD700", "R3": "#FF6347", "R2": "#00BFFF", "R1": "#8B7D6B"}

BUILDINGS_LIST = [
    "Гнездо Королевы", "Ферма", "Казарма", "Лаборатория",
    "Склад", "Башня Обороны", "Питомник", "Тропа Снабжения"
]

BUILDING_ICONS = {
    "Гнездо Королевы":  "👑",
    "Ферма":            "🌾",
    "Казарма":          "⚔️",
    "Лаборатория":      "🔬",
    "Склад":            "📦",
    "Башня Обороны":    "🏰",
    "Питомник":         "🥚",
    "Тропа Снабжения":  "🛤️",
}

BUILDING_DESC = {
    "Гнездо Королевы":  "Сердце колонии. Здесь живёт и плодит муравьёв ваша Королева.",
    "Ферма":            "Производит пищу — основа жизни колонии.",
    "Казарма":          "Готовит солдат и рабочих для боя и труда.",
    "Лаборатория":      "Открывает новые технологии и виды муравьёв.",
    "Склад":            "Хранит ресурсы: еду, материалы, трофеи.",
    "Башня Обороны":    "Защищает колонию от вражеских набегов.",
    "Питомник":         "Здесь выращивают личинок и будущих воинов.",
    "Тропа Снабжения":  "Ускоряет доставку ресурсов и добычу.",
}

BUILDING_COLORS = {
    "Гнездо Королевы":  "#FFD700",
    "Ферма":            "#7CFC00",
    "Казарма":          "#FF6347",
    "Лаборатория":      "#00BFFF",
    "Склад":            "#DEB887",
    "Башня Обороны":    "#A9A9A9",
    "Питомник":         "#FF69B4",
    "Тропа Снабжения":  "#D2B48C",
}

SAVE_DIR = "saves"
ALLIANCE_DIR = "saves/alliances"

os.makedirs(ALLIANCE_DIR, exist_ok=True)

# ===================================================================
#  СОХРАНЕНИЕ И ЗАГРУЗКА
# ===================================================================

def player_path(name):
    return os.path.join(SAVE_DIR, f"{name}.json")

def alliance_path(name):
    return os.path.join(ALLIANCE_DIR, f"{name}.json")

def load_player(name):
    p = player_path(name)
    if os.path.exists(p):
        with open(p, "r", encoding="utf-8") as f:
            return json.load(f)
    return None

def save_player(name, data):
    with open(player_path(name), "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def load_alliance(name):
    p = alliance_path(name)
    if os.path.exists(p):
        with open(p, "r", encoding="utf-8") as f:
            return json.load(f)
    return None

def save_alliance(name, data):
    with open(alliance_path(name), "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def list_alliances():
    if not os.path.exists(ALLIANCE_DIR):
        return []
    return [f[:-5] for f in os.listdir(ALLIANCE_DIR) if f.endswith(".json")]

# ===================================================================
#  ГЕНЕРАЦИЯ БОТОВ
# ===================================================================

def gen_bot_name():
    return f"{random.choice(BOT_FIRST_NAMES)} {random.choice(BOT_LAST_NAMES)}"

def gen_bot_phrase():
    return random.choice(BOT_PHRASES)

# ===================================================================
#  ПРИЛОЖЕНИЕ
# ===================================================================

class AntLegion:
    def __init__(self, root):
        self.root = root
        self.root.title("Ant Legion: Colony Wars")
        self.root.geometry("720x620")
        self.root.configure(bg="#2B1B17")

        self.player = None
        self.player_name = None
        self.bot_job = None
        self.current_frame = None

        self.show_login()

    # ----- утилиты UI -----
    def clear(self):
        if self.current_frame:
            self.current_frame.destroy()
        self.current_frame = tk.Frame(self.root, bg="#2B1B17")
        self.current_frame.pack(fill="both", expand=True)

    def style_label(self, text, size=14, color="#F0E68C", parent=None):
        p = parent or self.current_frame
        return tk.Label(p, text=text, bg="#2B1B17", fg=color,
                        font=("Arial", size, "bold"))

    def style_btn(self, text, command, parent=None, bg="#8B4513", fg="white"):
        p = parent or self.current_frame
        return tk.Button(p, text=text, bg=bg, fg=fg, font=("Arial", 12, "bold"),
                         relief="raised", bd=3, padx=12, pady=6, command=command,
                         activebackground="#A0522D", activeforeground="white")

    # =================================================================
    #  ЭКРАН ВХОДА / РЕГИСТРАЦИИ
    # =================================================================
    def show_login(self):
        self.clear()
        self.style_label("🐜 ANT LEGION 🐜", 22, "#FFD700").pack(pady=30)
        self.style_label("Colony Wars", 16, "#DEB887").pack()

        frame = tk.Frame(self.current_frame, bg="#2B1B17")
        frame.pack(pady=20)

        tk.Label(frame, text="Имя игрока:", bg="#2B1B17", fg="#F0E68C",
                 font=("Arial", 12)).grid(row=0, column=0, pady=5, sticky="e")
        entry_name = tk.Entry(frame, font=("Arial", 12), width=25)
        entry_name.grid(row=0, column=1, pady=5, padx=10)

        btn_frame = tk.Frame(self.current_frame, bg="#2B1B17")
        btn_frame.pack(pady=10)

        def do_login():
            name = entry_name.get().strip()
            if not name:
                messagebox.showwarning("Внимание", "Введите имя!")
                return
            data = load_player(name)
            if data is None:
                messagebox.showinfo("Новый игрок", f"Игрок '{name}' не найден. Создайте нового!")
            else:
                self.player_name = name
                self.player = data
                self.show_hub()

        def do_register():
            name = entry_name.get().strip()
            if not name:
                messagebox.showwarning("Внимание", "Введите имя!")
                return
            if load_player(name) is not None:
                messagebox.showwarning("Внимание", "Игрок уже существует! Войдите.")
                return
            self.player_name = name
            self.show_career_select()

        self.style_btn("Войти", do_login, btn_frame).pack(side="left", padx=10)
        self.style_btn("Новая игра", do_register, btn_frame).pack(side="left", padx=10)

    # =================================================================
    #  ВЫБОР КАРЬЕРЫ (новый игрок)
    # =================================================================
    def show_career_select(self):
        self.clear()
        self.style_label("Выберите свою роль в колонии", 16, "#FFD700").pack(pady=15)
        self.style_label(f"Игрок: {self.player_name}", 12, "#DEB887").pack()

        grid = tk.Frame(self.current_frame, bg="#2B1B17")
        grid.pack(pady=15)

        def pick(career):
            self.player = {
                "name": self.player_name,
                "career": career,
                "buildings": {b: {"level": 0, "built": False} for b in BUILDINGS_LIST},
                "resources": {"food": 500, "materials": 200},
                "alliance": None,
                "rank": None,
                "chat_history": [],
                "troops": 10,
            }
            self.player["buildings"]["Гнездо Королевы"] = {"level": 1, "built": True}
            save_player(self.player_name, self.player)
            messagebox.showinfo("Поздравляем!",
                f"Вы — {career}!\nГнездо Королевы построено.\nУдачи в развитии колонии!")
            self.show_hub()

        for i, c in enumerate(CAREERS):
            row, col = divmod(i, 2)
            card = tk.Frame(grid, bg="#3B2B1F", relief="ridge", bd=2)
            card.grid(row=row, column=col, padx=10, pady=8, sticky="nsew")
            tk.Label(card, text=CAREER_DESC[c], bg="#3B2B1F", fg="#F0E68C",
                     font=("Arial", 11, "bold")).pack(pady=5, padx=10)
            self.style_btn(c, lambda cc=c: pick(cc), card).pack(pady=5)

    # =================================================================
    #  ГЛАВНЫЙ ЭКРАН (ХАБ)
    # =================================================================
    def show_hub(self):
        if self.bot_job:
            self.root.after_cancel(self.bot_job)
            self.bot_job = None

        self.clear()

        # Шапка
        header = tk.Frame(self.current_frame, bg="#1a0f0a")
        header.pack(fill="x", pady=(0, 10))

        self.style_label(f"🐜 {self.player_name}", 16, "#FFD700", header).pack(side="left", padx=15, pady=8)
        career = self.player.get("career", "?")
        self.style_label(f"Карьера: {career}", 11, "#DEB887", header).pack(side="left", padx=10)

        ally = self.player.get("alliance")
        rank = self.player.get("rank", "")
        if ally:
            self.style_label(f"Альянс: {ally} ({rank})", 11, "#7CFC00", header).pack(side="left", padx=10)
        else:
            self.style_label("Без альянса", 11, "#FF6347", header).pack(side="left", padx=10)

        res = self.player.get("resources", {})
        self.style_label(f"🌾 Пища: {res.get('food', 0)}  📦 Материалы: {res.get('materials', 0)}",
                         11, "#F0E68C", header).pack(side="right", padx=15)

        # Кнопки меню
        menu = tk.Frame(self.current_frame, bg="#2B1B17")
        menu.pack(pady=15)

        self.style_btn("🏛️  Здания", self.show_buildings, menu).grid(row=0, column=0, padx=8, pady=8)
        self.style_btn("🤝  Альянс", self.show_alliance_menu, menu).grid(row=0, column=1, padx=8, pady=8)
        self.style_btn("💬  Чат", self.show_chat, menu).grid(row=0, column=2, padx=8, pady=8)
        self.style_btn("⚔️  Армия", self.show_army, menu).grid(row=1, column=0, padx=8, pady=8)
        self.style_btn("📊  Профиль", self.show_profile, menu).grid(row=1, column=1, padx=8, pady=8)
        self.style_btn("🚪  Выйти", self.logout, menu).grid(row=1, column=2, padx=8, pady=8)

        self.style_label("Колония ждёт ваших приказов!", 11, "#8B7D6B").pack(side="bottom", pady=10)

    # =================================================================
    #  ЗДАНИЯ
    # =================================================================
    def show_buildings(self):
        self.clear()
        self.style_label("🏛️ Здания колонии", 16, "#FFD700").pack(pady=10)

        canvas = tk.Canvas(self.current_frame, bg="#2B1B17", highlightthickness=0)
        scrollbar = tk.Scrollbar(self.current_frame, orient="vertical", command=canvas.yview)
        scroll_frame = tk.Frame(canvas, bg="#2B1B17")

        scroll_frame.bind("<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        for b in BUILDINGS_LIST:
            info = self.player["buildings"].get(b, {"level": 0, "built": False})
            icon = BUILDING_ICONS.get(b, "🏠")
            color = BUILDING_COLORS.get(b, "#8B7D6B")

            card = tk.Frame(scroll_frame, bg="#3B2B1F", relief="ridge", bd=3)
            card.pack(fill="x", padx=15, pady=6)

            top = tk.Frame(card, bg=color)
            top.pack(fill="x")
            tk.Label(top, text=f"{icon}  {b}", bg=color, fg="black",
                    font=("Arial", 13, "bold")).pack(side="left", padx=10, pady=4)

            level = info["level"]
            status = f"Ур. {level}" if info["built"] else "Не построено"
            tk.Label(top, text=status, bg=color, fg="black",
                    font=("Arial", 11, "bold")).pack(side="right", padx=10, pady=4)

            tk.Label(card, text=BUILDING_DESC.get(b, ""), bg="#3B2B1F", fg="#DEB887",
                     font=("Arial", 10), wraplength=550, justify="left").pack(anchor="w", padx=10, pady=5)

            btns = tk.Frame(card, bg="#3B2B1F")
            btns.pack(fill="x", padx=10, pady=5)

            if not info["built"]:
                cost_food = 100
                cost_mat = 50
                tk.Label(btns, text=f"Стоимость: 🌾{cost_food}  📦{cost_mat}",
                         bg="#3B2B1F", fg="#F0E68C", font=("Arial", 10)).pack(side="left")
                self.style_btn("Построить",
                    lambda bn=b, cf=cost_food, cm=cost_mat: self.build(bn, cf, cm),
                    btns, bg="#556B2F").pack(side="right")
            else:
                next_level = level + 1
                cost_food = 100 * next_level
                cost_mat = 50 * next_level
                tk.Label(btns, text=f"След. уровень: 🌾{cost_food}  📦{cost_mat}",
                         bg="#3B2B1F", fg="#F0E68C", font=("Arial", 10)).pack(side="left")
                self.style_btn(f"Улучшить до ур.{next_level}",
                    lambda bn=b, cf=cost_food, cm=cost_mat: self.upgrade(bn, cf, cm),
                    btns, bg="#8B4513").pack(side="right")

        self.style_btn("⬅️ Назад", self.show_hub, self.current_frame).pack(side="bottom", pady=10)

    def build(self, name, cf, cm):
        if self.player["resources"]["food"] < cf or self.player["resources"]["materials"] < cm:
            messagebox.showwarning("Не хватает", "Недостаточно ресурсов!")
            return
        self.player["resources"]["food"] -= cf
        self.player["resources"]["materials"] -= cm
        self.player["buildings"][name] = {"level": 1, "built": True}
        save_player(self.player_name, self.player)
        messagebox.showinfo("Построено!", f"{BUILDING_ICONS.get(name, '')} {name} построена!")
        self.show_buildings()

    def upgrade(self, name, cf, cm):
        if self.player["resources"]["food"] < cf or self.player["resources"]["materials"] < cm:
            messagebox.showwarning("Не хватает", "Недостаточно ресурсов!")
            return
        self.player["resources"]["food"] -= cf
        self.player["resources"]["materials"] -= cm
        self.player["buildings"][name]["level"] += 1
        save_player(self.player_name, self.player)
        cur = self.player["buildings"][name]["level"]
        messagebox.showinfo("Улучшено!", f"{BUILDING_ICONS.get(name, '')} {name} → уровень {cur}!")
        self.show_buildings()

    # =================================================================
    #  АЛЬЯНС — МЕНЮ КАК В ИГРЕ
    # =================================================================
    def show_alliance_menu(self):
        self.clear()
        self.style_label("🤝 Альянс", 16, "#FFD700").pack(pady=10)

        ally = self.player.get("alliance")
        if not ally:
            self._alliance_no_ally()
        else:
            self._alliance_inside(ally)

        self.style_btn("⬅️ Назад", self.show_hub, self.current_frame).pack(side="bottom", pady=10)

    def _alliance_no_ally(self):
        self.style_label("Вы не состоите в альянсе", 12, "#FF6347").pack(pady=10)

        # Создать альянс
        create_frame = tk.LabelFrame(self.current_frame, text="Создать альянс",
                                     bg="#3B2B1F", fg="#FFD700", font=("Arial", 12, "bold"))
        create_frame.pack(fill="x", padx=20, pady=10)

        tk.Label(create_frame, text="Название:", bg="#3B2B1F", fg="#F0E68C",
                 font=("Arial", 11)).pack(side="left", padx=10, pady=10)
        entry = tk.Entry(create_frame, font=("Arial", 12), width=25)
        entry.pack(side="left", padx=5, pady=10)

        def do_create():
            name = entry.get().strip()
            if not name:
                messagebox.showwarning("Внимание", "Введите название!")
                return
            if load_alliance(name) is not None:
                messagebox.showwarning("Занято", "Альянс с таким названием уже существует!")
                return
            ally_data = {
                "name": name,
                "leader": self.player_name,
                "members": {self.player_name: "R4"},
                "description": f"Альянс '{name}' под управлением {self.player_name}",
                "created_by": self.player_name,
            }
            save_alliance(name, ally_data)
            self.player["alliance"] = name
            self.player["rank"] = "R4"
            save_player(self.player_name, self.player)
            messagebox.showinfo("Создан!", f"Альянс '{name}' создан!\nВы — лидер (R4)!")
            self.show_alliance_menu()

        self.style_btn("Создать", do_create, create_frame, bg="#556B2F").pack(side="left", padx=10, pady=10)

        # Вступить в существующий
        join_frame = tk.LabelFrame(self.current_frame, text="Вступить в альянс",
                                   bg="#3B2B1F", fg="#FFD700", font=("Arial", 12, "bold"))
        join_frame.pack(fill="both", expand=True, padx=20, pady=10)

        all_al = set(ALLIANCE_NAMES)
        for a in list_alliances():
            all_al.add(a)

        if not all_al:
            tk.Label(join_frame, text="Нет доступных альянсов", bg="#3B2B1F", fg="#DEB887").pack(pady=10)
        else:
            inner = tk.Frame(join_frame, bg="#3B2B1F")
            inner.pack(fill="both", expand=True, padx=10, pady=10)

            for i, a in enumerate(sorted(all_al)):
                row, col = divmod(i, 2)
                cell = tk.Frame(inner, bg="#2B1B17", relief="groove", bd=2)
                cell.grid(row=row, column=col, padx=8, pady=6, sticky="nsew")

                ad = load_alliance(a)
                member_count = len(ad["members"]) if ad else random.randint(3, 20)
                tk.Label(cell, text=f"🤝 {a}", bg="#2B1B17", fg="#F0E68C",
                         font=("Arial", 11, "bold")).pack(pady=3)
                tk.Label(cell, text=f"Участников: {member_count}", bg="#2B1B17", fg="#8B7D6B",
                         font=("Arial", 9)).pack()
                self.style_btn("Вступить", lambda an=a: self.join_alliance(an),
                               cell, bg="#8B4513").pack(pady=5)

    def join_alliance(self, name):
        ad = load_alliance(name)
        if ad is None:
            bot_members = {}
            for _ in range(random.randint(3, 8)):
                bot_members[gen_bot_name()] = random.choice(RANKS)
            ad = {
                "name": name,
                "leader": gen_bot_name(),
                "members": bot_members,
                "description": f"Альянс '{name}'",
                "created_by": "NPC",
            }
            save_alliance(name, ad)

        if self.player_name in ad["members"]:
            messagebox.showwarning("Уже в альянсе", "Вы уже участник этого альянса!")
            return

        ad["members"][self.player_name] = "R1"
        save_alliance(name, ad)

        self.player["alliance"] = name
        self.player["rank"] = "R1"
        save_player(self.player_name, self.player)
        messagebox.showinfo("Добро пожаловать!", f"Вы вступили в альянс '{name}'!\nВаш ранг: R1")
        self.show_alliance_menu()

    def _alliance_inside(self, ally_name):
        ad = load_alliance(ally_name)
        if ad is None:
            messagebox.showerror("Ошибка", "Альянс не найден. Возможно, он был распущен.")
            self.player["alliance"] = None
            self.player["rank"] = None
            save_player(self.player_name, self.player)
            self.show_alliance_menu()
            return

        rank = self.player.get("rank", "R1")

        # Инфо
        info = tk.LabelFrame(self.current_frame, text="Информация об альянсе",
                             bg="#3B2B1F", fg="#FFD700", font=("Arial", 12, "bold"))
        info.pack(fill="x", padx=20, pady=5)

        tk.Label(info, text=f"Название: {ad['name']}", bg="#3B2B1F", fg="#F0E68C",
                 font=("Arial", 11)).pack(anchor="w", padx=10, pady=2)
        tk.Label(info, text=f"Лидер: {ad['leader']}", bg="#3B2B1F", fg="#F0E68C",
                 font=("Arial", 11)).pack(anchor="w", padx=10, pady=2)
        tk.Label(info, text=f"Ваш ранг: {rank}", bg="#3B2B1F", fg="#7CFC00",
                 font=("Arial", 12, "bold")).pack(anchor="w", padx=10, pady=2)
        tk.Label(info, text=f"Участников: {len(ad['members'])}", bg="#3B2B1F", fg="#F0E68C",
                 font=("Arial", 11)).pack(anchor="w", padx=10, pady=2)

        rights = RANK_RIGHTS.get(rank, [])
        tk.Label(info, text="Ваши права: " + ", ".join(rights), bg="#3B2B1F", fg="#DEB887",
                 font=("Arial", 10), wraplength=500, justify="left").pack(anchor="w", padx=10, pady=5)

        # Список участников
        members_frame = tk.LabelFrame(self.current_frame, text="Участники",
                                      bg="#3B2B1F", fg="#FFD700", font=("Arial", 12, "bold"))
        members_frame.pack(fill="both", expand=True, padx=20, pady=5)

        mcanvas = tk.Canvas(members_frame, bg="#3B2B1F", highlightthickness=0)
        mscroll = tk.Scrollbar(members_frame, orient="vertical", command=mcanvas.yview)
        mcontent = tk.Frame(mcanvas, bg="#3B2B1F")
        mcontent.bind("<Configure>",
            lambda e: mcanvas.configure(scrollregion=mcanvas.bbox("all")))
        mcanvas.create_window((0, 0), window=mcontent, anchor="nw")
        mcanvas.configure(yscrollcommand=mscroll.set)
        mcanvas.pack(side="left", fill="both", expand=True)
        mscroll.pack(side="right", fill="y")

        sorted_members = sorted(ad["members"].items(),
                                key=lambda x: RANKS.index(x[1]) if x[1] in RANKS else 99,
                                reverse=True)

        for mname, mrank in sorted_members:
            row = tk.Frame(mcontent, bg="#2B1B17", relief="sunken", bd=1)
            row.pack(fill="x", padx=5, pady=3)
            tk.Label(row, text=mname, bg="#2B1B17", fg="#F0E68C",
                     font=("Arial", 11)).pack(side="left", padx=10, pady=4)
            tk.Label(row, text=mrank, bg="#2B1B17", fg=RANK_COLORS.get(mrank, "#8B7D6B"),
                     font=("Arial", 11, "bold")).pack(side="right", padx=10, pady=4)

            if rank in ("R3", "R4") and mname != self.player_name and mname != ad["leader"]:
                ctrl = tk.Frame(row, bg="#2B1B17")
                ctrl.pack(side="right", padx=5)
                cur_idx = RANKS.index(mrank) if mrank in RANKS else 0

                if cur_idx < len(RANKS) - 1:
                    tk.Button(ctrl, text="⬆ Повысить", bg="#556B2F", fg="white",
                              font=("Arial", 8),
                              command=lambda mn=mname, nr=RANKS[cur_idx + 1]: self.change_rank(mn, nr)
                              ).pack(side="left", padx=2)
                if cur_idx > 0:
                    tk.Button(ctrl, text="⬇ Понизить", bg="#8B0000", fg="white",
                              font=("Arial", 8),
                              command=lambda mn=mname, nr=RANKS[cur_idx - 1]: self.change_rank(mn, nr)
                              ).pack(side="left", padx=2)

        # Кнопки управления
        ctrl_frame = tk.Frame(self.current_frame, bg="#2B1B17")
        ctrl_frame.pack(fill="x", padx=20, pady=10)

        if rank in ("R3", "R4"):
            self.style_btn("✉️ Пригласить бота", self.invite_bot, ctrl_frame,
                           bg="#556B2F").grid(row=0, column=0, padx=5, pady=5)
            self.style_btn("🚪 Выйти из альянса", self.leave_alliance, ctrl_frame,
                           bg="#8B0000").grid(row=0, column=1, padx=5, pady=5)
        else:
            self.style_btn("🚪 Выйти из альянса", self.leave_alliance, ctrl_frame,
                           bg="#8B0000").grid(row=0, column=0, padx=5, pady=5)

        if rank == "R4":
            self.style_btn("💀 Распустить альянс", self.disband_alliance, ctrl_frame,
                           bg="#4a0a0a").grid(row=0, column=2, padx=5, pady=5)

    def change_rank(self, member_name, new_rank):
        ally = self.player["alliance"]
        ad = load_alliance(ally)
        if ad is None:
            return
        if member_name in ad["members"]:
            ad["members"][member_name] = new_rank
            save_alliance(ally, ad)
            if member_name == self.player_name:
                self.player["rank"] = new_rank
                save_player(self.player_name, self.player)
            messagebox.showinfo("Изменено", f"{member_name} → ранг {new_rank}")
            self.show_alliance_menu()

    def invite_bot(self):
        ally = self.player["alliance"]
        ad = load_alliance(ally)
        if ad is None:
            return
        bot = gen_bot_name()
        while bot in ad["members"]:
            bot = gen_bot_name()
        ad["members"][bot] = "R1"
        save_alliance(ally, ad)
        messagebox.showinfo("Приглашён!", f"{bot} присоединился к альянсу (R1)!")
        self.show_alliance_menu()

    def leave_alliance(self):
        ally = self.player["alliance"]
        ad = load_alliance(ally)
        if ad and self.player_name in ad["members"]:
            del ad["members"][self.player_name]
            if ad["leader"] == self.player_name:
                remaining = list(ad["members"].keys())
                if remaining:
                    new_leader = random.choice(remaining)
                    ad["leader"] = new_leader
                    ad["members"][new_leader] = "R4"
                    save_alliance(ally, ad)
                else:
                    p = alliance_path(ally)
                    if os.path.exists(p):
                        os.remove(p)
            else:
                save_alliance(ally, ad)
        self.player["alliance"] = None
        self.player["rank"] = None
        save_player(self.player_name, self.player)
        messagebox.showinfo("Выход", "Вы покинули альянс.")
        self.show_alliance_menu()

    def disband_alliance(self):
        ally = self.player["alliance"]
        if messagebox.askyesno("Подтверждение",
                f"Распустить альянс '{ally}'? Все участники будут удалены!"):
            p = alliance_path(ally)
            if os.path.exists(p):
                os.remove(p)
            self.player["alliance"] = None
            self.player["rank"] = None
            save_player(self.player_name, self.player)
            messagebox.showinfo("Роспуск", f"Альянс '{ally}' распущен.")
            self.show_alliance_menu()

    # =================================================================
    #  ЧАТ (с ботами)
    # =================================================================
    def show_chat(self):
        self.clear()
        self.style_label("💬 Чат альянса", 16, "#FFD700").pack(pady=5)

        ally = self.player.get("alliance")

        text_frame = tk.Frame(self.current_frame, bg="#2B1B17")
        text_frame.pack(fill="both", expand=True, padx=20, pady=5)

        chat = tk.Text(text_frame, bg="#1a0f0a", fg="#F0E68C", font=("Arial", 11),
                       relief="sunken", bd=2, wrap="word")
        chat.pack(side="left", fill="both", expand=True)
        sb = tk.Scrollbar(text_frame, orient="vertical", command=chat.yview)
        sb.pack(side="right", fill="y")
        chat.configure(yscrollcommand=sb.set, state="normal")

        for msg in self.player.get("chat_history", []):
            chat.insert(tk.END, msg + "\n")
        chat.see(tk.END)

        if ally:
            ad = load_alliance(ally)
            if ad:
                bots = [n for n in ad["members"] if n != self.player_name]
                for _ in range(random.randint(2, 5)):
                    if bots:
                        bname = random.choice(bots)
                        phrase = gen_bot_phrase()
                        line = f"[{bname}]: {phrase}"
                        chat.insert(tk.END, line + "\n")
                        self.player["chat_history"].append(line)
                chat.see(tk.END)

        input_frame = tk.Frame(self.current_frame, bg="#2B1B17")
        input_frame.pack(fill="x", padx=20, pady=5)

        entry = tk.Entry(input_frame, font=("Arial", 12), width=50)
        entry.pack(side="left", padx=5, fill="x", expand=True)

        def send():
            msg = entry.get().strip()
            if not msg:
                return
            line = f"[{self.player_name}]: {msg}"
            chat.insert(tk.END, line + "\n")
            chat.see(tk.END)
            self.player["chat_history"].append(line)
            save_player(self.player_name, self.player)
            entry.delete(0, tk.END)
            ally = self.player.get("alliance")
            if(msg=="GJ"):
                msg="GG"
            if ally:
                ad = load_alliance(ally)
                if ad:
                    bots = [n for n in ad["members"] if n != self.player_name]
                    if bots and random.random() > 0.3:
                        bname = random.choice(bots)
                        phrase = gen_bot_phrase()
                        bline = f"[{bname}]: {phrase}"
                        self.root.after(1200, lambda: self._bot_reply(chat, bline))

        self.style_btn("Отправить", send, input_frame).pack(side="left", padx=5)
        self.style_btn("🤖 Бот пишет", lambda: self._random_bot_msg(chat),
                       input_frame, bg="#556B2F").pack(side="left", padx=5)

        self.style_btn("⬅️ Назад", self.show_hub, self.current_frame).pack(side="bottom", pady=10)

        self._chat_ref = chat
        self.bot_job = self.root.after(5000, self._auto_bot_msg)

    def _bot_reply(self, chat, line):
        try:
            chat.insert(tk.END, line + "\n")
            chat.see(tk.END)
            self.player["chat_history"].append(line)
            save_player(self.player_name, self.player)
        except Exception:
            pass

    def _random_bot_msg(self, chat):
        ally = self.player.get("alliance")
        if ally:
            ad = load_alliance(ally)
            if ad:
                bots = [n for n in ad["members"] if n != self.player_name]
                if bots:
                    bname = random.choice(bots)
                    line = f"[{bname}]: {gen_bot_phrase()}"
                    chat.insert(tk.END, line + "\n")
                    chat.see(tk.END)
                    self.player["chat_history"].append(line)
                    save_player(self.player_name, self.player)
                    return
        line = f"[{gen_bot_name()}]: {gen_bot_phrase()}"
        chat.insert(tk.END, line + "\n")
        chat.see(tk.END)
        self.player["chat_history"].append(line)
        save_player(self.player_name, self.player)

    def _auto_bot_msg(self):
        if self.current_frame is None:
            return
        try:
            chat = getattr(self, "_chat_ref", None)
            if chat is None:
                return
            ally = self.player.get("alliance")
            if ally:
                ad = load_alliance(ally)
                if ad:
                    bots = [n for n in ad["members"] if n != self.player_name]
                    if bots and random.random() > 0.5:
                        bname = random.choice(bots)
                        line = f"[{bname}]: {gen_bot_phrase()}"
                        chat.insert(tk.END, line + "\n")
                        chat.see(tk.END)
                        self.player["chat_history"].append(line)
                        save_player(self.player_name, self.player)
            self.bot_job = self.root.after(8000, self._auto_bot_msg)
        except Exception:
            pass

    # =================================================================
    #  АРМИЯ
    # =================================================================
    def show_army(self):
        self.clear()
        self.style_label("⚔️ Армия колонии", 16, "#FFD700").pack(pady=10)

        troops = self.player.get("troops", 0)

        info = tk.LabelFrame(self.current_frame, text="Войска", bg="#3B2B1F",
                             fg="#FFD700", font=("Arial", 12, "bold"))
        info.pack(fill="x", padx=20, pady=10)

        barracks = self.player["buildings"].get("Казарма", {})
        bar_lvl = barracks.get("level", 0) if barracks.get("built", False) else 0

        tk.Label(info, text=f"🕷️ Солдаты: {troops}", bg="#3B2B1F", fg="#F0E68C",
                 font=("Arial", 12)).pack(anchor="w", padx=10, pady=5)
        tk.Label(info, text=f"⚔️ Уровень казармы: {bar_lvl}", bg="#3B2B1F", fg="#DEB887",
                 font=("Arial", 11)).pack(anchor="w", padx=10, pady=5)

        recruit_cost = 20 + bar_lvl * 5

        tk.Label(info, text=f"Набор 1 солдата: 🌾{recruit_cost}", bg="#3B2B1F", fg="#F0E68C",
                 font=("Arial", 11)).pack(anchor="w", padx=10, pady=5)

        if bar_lvl > 0:
            self.style_btn(f"⚔️ Нанять (+{bar_lvl} солдат)",
                lambda: self.recruit(recruit_cost, bar_lvl),
                info, bg="#556B2F").pack(pady=5)
        else:
            tk.Label(info, text="Постройте казарму для найма солдат!",
                     bg="#3B2B1F", fg="#FF6347", font=("Arial", 10)).pack(pady=5)

        raid_frame = tk.LabelFrame(self.current_frame, text="Рейд",
                                   bg="#3B2B1F", fg="#FFD700", font=("Arial", 12, "bold"))
        raid_frame.pack(fill="x", padx=20, pady=10)

        tk.Label(raid_frame, text="Отправить армию в рейд за ресурсы!",
                 bg="#3B2B1F", fg="#F0E68C", font=("Arial", 11)).pack(pady=5)

        self.style_btn("🚀 В рейд!", self.raid, raid_frame, bg="#8B0000").pack(pady=5)

        self.style_btn("⬅️ Назад", self.show_hub, self.current_frame).pack(side="bottom", pady=10)

    def recruit(self, cost, count):
        if self.player["resources"]["food"] < cost:
            messagebox.showwarning("Не хватает", "Недостаточно пищи!")
            return
        self.player["resources"]["food"] -= cost
        self.player["troops"] = self.player.get("troops", 0) + count
        save_player(self.player_name, self.player)
        messagebox.showinfo("Набор", f"+{count} солдат! Всего: {self.player['troops']}")
        self.show_army()

    def raid(self):
        if self.player.get("troops", 0) < 5:
            messagebox.showwarning("Мало войск", "Нужно минимум 5 солдат для рейда!")
            return
        loot_food = random.randint(50, 200)
        loot_mat = random.randint(20, 100)
        losses = random.randint(0, 3)
        self.player["resources"]["food"] += loot_food
        self.player["resources"]["materials"] += loot_mat
        self.player["troops"] = max(0, self.player["troops"] - losses)
        save_player(self.player_name, self.player)

        result = f"🏆 Добыча: 🌾{loot_food}  📦{loot_mat}"
        if losses > 0:
            result += f"\n💀 Потери: {losses} солдат"
        else:
            result += "\n✅ Без потерь!"
        messagebox.showinfo("Рейд завершён", result)
        self.show_army()

    # =================================================================
    #  ПРОФИЛЬ
    # =================================================================
    def show_profile(self):
        self.clear()
        self.style_label("📊 Профиль игрока", 16, "#FFD700").pack(pady=10)

        info = tk.LabelFrame(self.current_frame, text="Игрок",
                             bg="#3B2B1F", fg="#FFD700", font=("Arial", 12, "bold"))
        info.pack(fill="x", padx=20, pady=10)

        rows = [
            ("Имя", self.player.get("name", "?")),
            ("Карьера", self.player.get("career", "?")),
            ("Альянс", self.player.get("alliance") or "—"),
            ("Ранг", self.player.get("rank") or "—"),
            ("Солдаты", str(self.player.get("troops", 0))),
            ("Пища", str(self.player["resources"].get("food", 0))),
            ("Материалы", str(self.player["resources"].get("materials", 0))),
        ]
        for k, v in rows:
            tk.Label(info, text=f"{k}: {v}", bg="#3B2B1F", fg="#F0E68C",
                     font=("Arial", 12)).pack(anchor="w", padx=10, pady=3)

        b_frame = tk.LabelFrame(self.current_frame, text="Здания",
                                bg="#3B2B1F", fg="#FFD700", font=("Arial", 12, "bold"))
        b_frame.pack(fill="both", expand=True, padx=20, pady=10)

        for b in BUILDINGS_LIST:
            info_b = self.player["buildings"].get(b, {})
            icon = BUILDING_ICONS.get(b, "🏠")
            lvl = info_b.get("level", 0)
            status = f"Ур. {lvl}" if info_b.get("built") else "Не построено"
            tk.Label(b_frame, text=f"{icon} {b}: {status}",
                     bg="#3B2B1F", fg="#F0E68C" if info_b.get("built") else "#8B7D6B",
                     font=("Arial", 11)).pack(anchor="w", padx=10, pady=2)

        self.style_btn("⬅️ Назад", self.show_hub, self.current_frame).pack(side="bottom", pady=10)

    # =================================================================
    #  ВЫХОД
    # =================================================================
    def logout(self):
        if self.bot_job:
            self.root.after_cancel(self.bot_job)
            self.bot_job = None
        save_player(self.player_name, self.player)
        self.player = None
        self.player_name = None
        self.show_login()


# ===================================================================
#  ЗАПУСК
# ===================================================================
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("720x620")
    root.configure(bg="#2B1B17")
    app = AntLegion(root)
    root.mainloop()
