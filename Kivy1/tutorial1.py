from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from main import main
class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 9
        self.tiles = []
        for i in range(81):
            self.tile  = TextInput(multiline=False)
            self.add_widget(self.tile)
            self.tiles.append(self.tile)
        self.add_widget(Label(text=''))
        self.add_widget(Label(text=''))
        self.add_widget(Label(text=''))
        self.add_widget(Label(text=''))
        self.solveBtn = Button(text='Solve', font_size=15)
        self.add_widget(self.solveBtn)
        self.solveBtn.bind(on_press=self.solve)
    def solve(self, instance):
        print('Pressed')
        tiles = self.tiles
        board = []
        output = []
        print(len(tiles))
        for i in range(1,82):
            print(i)
            if tiles[i-1].text == '':
                output.append(0)
            else:
                output.append(int(tiles[i-1].text))
            if (i % 9 == 0):
                board.append(output)
                output = []
        main(board)
        

class MyApp(App):
    def build(self):
        return MyGrid()
if __name__ == '__main__':
    MyApp().run()