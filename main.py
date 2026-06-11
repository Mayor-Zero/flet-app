
import ssl
ssl._create_default_https_context= ssl._create_unverified_context

import flet as ft
NAME_DATABASE = {
    "မောင်": "Maung",
    "မ": "Ma",
    "ကျော်": "Kyaw",
    "မင်း": "Min",
    "အောင်": "Aung",
    "သူရ": "Thura",
    "စိုး": "Soe",
    "နိုင်": "Naing",
    "ဦး": "U",
    "လွင်": "Lwin",
    "ထွန်း": "Htun",
    "ထက်": "Htet",
    "သူ": "Thu",
    "ဇင်": "Zin",
    "ဖြိုး": "Phyo",
    "ဝင်း": "Win",
    "အေး": "Aye",
    "မြတ်": "Myat",
    "သန်း": "Than",
    "ဌေး": "Htay",
    "မြ": "Mya",
    "သီရိ": "Theiri",
    "ယမင်း": "Yamin",
    "ဟန်": "Han",
    "လင်း": "Linn",
    "ဦး": "U",
    "ခိုင်": "Khine",
    "စု": "Su",
    "စန္ဒီ": "Sandi",
    "ကောင်း": "Kaung",
    "ခန့်": "Khant",
    "ကို": "Ko",
    "ဝေ" :"Wai",
    "ယံ" :"Yan",
    "ဦး" :"Oo",
    "နှင်း" :"Hnin",
    "ထွန်း":"Htun",
    "ညီ":"Nyi"
}
def main(page: ft.Page):
    page.title="Myanmar name to English"
    page.vertical_alignment=ft.MainAxisAlignment.CENTER
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    page.theme_mode=ft.ThemeMode.DARK
    page.window.width=450
    page.window.height=500

    #UI Element
    title_text= ft.Text("Myanmar ->> English", size=24,
                        weight=ft.FontWeight.BOLD,color="amber")
    name_input=ft.TextField(label="မြန်မာနာမည်ရေးပါ….!",width=350,text_align=ft.TextAlign.CENTER)
    result_text=ft.Text(value="",size=22,weight=ft.FontWeight.BOLD,color="green_accent")

    # Translate function
    def transtate_name(e):
        input_val= name_input.value.strip()
        if not input_val:
            result_text.value="မြန်မာနာမည်ရေးပါကွာ…."
            result_text.color="red_accent"
            page.update()
            return
        traslated_parts=[]
        temp_name=input_val
        for key in NAME_DATABASE.keys():
            if key in temp_name:
                temp_name=temp_name.replace(key, f"{NAME_DATABASE[key]}")
        final_result="".join(temp_name.split())
        
        if final_result== input_val or not any(char.isalpha() for char in final_result):
            result_text.value="No name in DATA BASE"
            result_text.color="orange"
        else:
            result_text.value=f"English Name: {final_result}"
            result_text.color="green_accent"
        page.update()
    
    #Traslate Button
    translate_btn=ft.ElevatedButton(
        "Translate",
        on_click=transtate_name
    )
    def clear(e):
        name_input.value=""
        result_text.value=""

    #Reset Button
    reset_btn=ft.ElevatedButton(
        "Reset",
        on_click=clear
    )

    # page on UI
    page.add(
        ft.Column(
            controls=[
                title_text,
                ft.Divider(height=20,color="transparent"),
                name_input,
                translate_btn,
                reset_btn,
                ft.Divider(height=20,color="transparent"),
                result_text
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER

            
        )
    )
        
    

  

ft.app(target=main)
#ft.run(main)