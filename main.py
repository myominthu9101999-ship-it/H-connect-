import flet as ft

def main(page: ft.Page):
    # App Setting များ
    page.title = "H-Connect"
    page.theme_mode = ft.ThemeMode.DARK
    page.scroll = "adaptive"
    page.padding = 20

    # 1. Header (App ရဲ့ ဆောင်ပုဒ်)
    header = ft.Column([
        ft.Text("H-Connect", size=35, weight="bold", color="blue200"),
        ft.Text("မင်းရဲ့ ခြေလှမ်းတိုင်း ငါတို့ ဂုဏ်ပြုတယ်", size=16, italic=True, color="amber"),
    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)

    # 2. Daily Win Input (အောင်မြင်မှု မှတ်တမ်းတင်ရန်)
    win_input = ft.TextField(
        label="ဒီနေ့ မင်းရဲ့ ခြေလှမ်းက ဘာလဲ?",
        hint_text="ဥပမာ - ဒီနေ့ စာအုပ် ၅ မျက်နှာ ဖတ်တယ်...",
        border_radius=15
    )

    wins_list = ft.Column()

    def share_win(e):
        if win_input.value:
            new_card = ft.Card(
                content=ft.Container(
                    content=ft.ListTile(
                        leading=ft.Icon(ft.icons.STAR, color="orange"),
                        title=ft.Text(win_input.value),
                        subtitle=ft.Text("ဂုဏ်ယူပါတယ်! မင်းလုပ်နိုင်ခဲ့ပြီ။"),
                    ),
                    padding=10
                )
            )
            wins_list.controls.insert(0, new_card) # အပေါ်ဆုံးမှာ ပေါ်အောင်
            win_input.value = ""
            page.update()

    share_btn = ft.ElevatedButton(
        "အောင်မြင်မှု မျှဝေမယ်", 
        icon=ft.icons.SEND, 
        on_click=share_win,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10))
    )

    # 3. Calling System (သူငယ်ချင်းထံ ဖုန်းခေါ်ရန်)
    def call_action(e):
        # Dialer ကို ပွင့်စေသည်
        page.launch_url("tel:09123456789") 

    call_btn = ft.FloatingActionButton(
        icon=ft.icons.PHONE,
        bgcolor="green",
        on_click=call_action,
        tooltip="သူငယ်ချင်းကို ဖုန်းခေါ်မယ်"
    )

    # App ထဲမှာ အရာအားလုံးကို ထည့်သွင်းခြင်း
    page.add(
        header,
        ft.Divider(height=40, color="transparent"),
        win_input,
        share_btn,
        ft.Divider(height=30),
        ft.Text("သူငယ်ချင်းများ၏ အောင်မြင်မှုများ -", weight="bold", size=18),
        wins_list
    )
    page.floating_action_button = call_btn

# App ကို Run ရန်
ft.app(target=main)
