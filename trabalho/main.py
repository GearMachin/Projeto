from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.stacklayout import StackLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.metrics import dp

class ListaDeItens(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", **kwargs)

        # Título no canto superior esquerdo
        header_layout = BoxLayout(orientation="horizontal", size_hint_y=None, height=dp(50))
        titulo = Label(
            text="Contador de Estoque",
            size_hint_x=None,
            width=dp(200),
            halign="left",
            valign="middle",
            font_size="20sp"
        )
        titulo.bind(size=self._reposition_title)  # Ajuste para alinhar corretamente
        header_layout.add_widget(titulo)
        self.add_widget(header_layout)

        # Layout para entradas
        input_layout = BoxLayout(orientation="horizontal", size_hint_y=None, height=dp(60))

        # Campo de texto para adicionar itens
        self.item_input = TextInput(hint_text="Nome do Item", multiline=False, size_hint_x=0.6, height=dp(40))
        input_layout.add_widget(self.item_input)

        # Campo de texto para quantidade
        self.quantidade_input = TextInput(hint_text="Quantidade", multiline=False, input_filter="int", size_hint_x=0.2, height=dp(40))
        input_layout.add_widget(self.quantidade_input)

        # Botão para adicionar à lista
        self.add_button = Button(text="Adicionar", size_hint_x=0.2, height=dp(40))
        self.add_button.bind(on_press=self.adicionar_item)
        input_layout.add_widget(self.add_button)

        # Adicionar o layout de entrada ao principal
        self.add_widget(input_layout)

        # ScrollView para exibir os itens
        self.scroll = ScrollView(size_hint=(1, None), size=(self.width, dp(400)))
        self.item_layout = StackLayout(size_hint_y=None)
        self.item_layout.bind(minimum_height=self.item_layout.setter("height"))
        self.scroll.add_widget(self.item_layout)
        self.add_widget(self.scroll)

    def _reposition_title(self, instance, value):
        instance.text_size = instance.size

    def adicionar_item(self, instance):
        nome = self.item_input.text.strip()
        quantidade = self.quantidade_input.text.strip()

        if nome and quantidade.isdigit():
            # Criar um layout horizontal para o item
            item_layout = BoxLayout(orientation="horizontal", size_hint_y=None, height=dp(60))

            # Label do nome do item
            item_label = Label(text=nome, size_hint_x=0.4, font_size="16sp")
            item_layout.add_widget(item_label)

            # Label da quantidade
            quantidade_label = Label(text=quantidade, size_hint_x=0.2, font_size="16sp")
            item_layout.add_widget(quantidade_label)

            # Botão para aumentar a quantidade
            add_button = Button(text="+", size_hint_x=0.2, height=dp(40))
            add_button.bind(on_press=lambda x: self.alterar_quantidade(quantidade_label, 1))
            item_layout.add_widget(add_button)

            # Botão para diminuir a quantidade
            sub_button = Button(text="-", size_hint_x=0.2, height=dp(40))
            sub_button.bind(on_press=lambda x: self.alterar_quantidade(quantidade_label, -1))
            item_layout.add_widget(sub_button)

            # Adicionar o layout do item ao layout principal
            self.item_layout.add_widget(item_layout)

            # Limpar os campos de entrada
            self.item_input.text = ""
            self.quantidade_input.text = ""
        else:
            print("Por favor, insira um nome e uma quantidade válida.")

    def alterar_quantidade(self, quantidade_label, delta):
        # Atualizar a quantidade do item
        quantidade_atual = int(quantidade_label.text)
        nova_quantidade = quantidade_atual + delta
        if nova_quantidade >= 0:
            quantidade_label.text = str(nova_quantidade)


class ListaDeItensApp(App):
    def build(self):
        return ListaDeItens()


if __name__ == "__main__":
    ListaDeItensApp().run()