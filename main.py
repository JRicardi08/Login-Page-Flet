import flet as ft

class Login(ft.Container):
    def __init__(self, on_color_change):
        super().__init__()
        self.on_color_change = on_color_change
        self.input_name = ft.TextField(width=200, height=40, color="black",bgcolor="white")
        self.label_name = ft.Text("Name", color="grey")
        self.company = ft.Dropdown(
            width=200,
            height=40,
            color="black",
            bgcolor="white",
            options=[
                ft.dropdown.Option("Schlumberger"),
                ft.dropdown.Option("Halliburton"),
                ft.dropdown.Option("Baker Hughes"),
                ft.dropdown.Option("Weatherford"),
            ],
            on_change=self.container_color_bg  # Add event listener for dropdown change
        )
        self.label_company = ft.Text("Company", color="grey")
        self.continue_button = ft.ElevatedButton(
            text="Continue",
            width=200, 
            height=40,
            bgcolor="#CFCFCF",
            color="black",
            style=ft.ButtonStyle(shape={"":ft.RoundedRectangleBorder(radius=5)}),
            )
        
        # Add components to the container's children
        self.content = ft.Column(
            controls=[
                self.input_name,
                self.label_name,
                self.company,
                self.label_company,
                self.continue_button
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )

    def container_color_bg(self, e):
        color = None
        if self.company.value == "Schlumberger":
            color = "#0014dc"
            self.label_name.color = "white"
            self.label_company.color = "white"
            self.continue_button.bgcolor = "white"
        elif self.company.value == "Halliburton":
            color = "#cc0000"
            self.label_name.color = "white"
            self.label_company.color = "white"
        elif self.company.value == "Baker Hughes":
            color = "#013025"
            self.label_name.color = "white"
            self.label_company.color = "white"
        elif self.company.value == "Weatherford":
            color = "#ce1141"
            self.label_name.color = "white"
            self.label_company.color = "white"
        
        if color:
            self.bgcolor = color
            self.update()
            self.continue_button.update()
            self.on_color_change(color)

class Layout(ft.Container):
    def __init__(self):
        super().__init__()
        login = Login(self.container_color_bg)

        self.content = ft.Container(
            width=400,
            height=400,
            border_radius=5,
            border=ft.border.all(color="black", width=1),
            content=ft.Column(
                controls=[login],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            alignment=ft.alignment.center
        )

    def container_color_bg(self, color):
        self.content.bgcolor = color
        self.content.update()

def main(page: ft.Page):
    page.title = "Login Page"
    page.bgcolor = "white"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    app_layout = Layout()
    page.add(app_layout)

    page.update()

ft.app(target=main)

