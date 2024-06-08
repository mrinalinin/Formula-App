import math
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class FormulaApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        self.input_label = Label(text='CALCULATOR')
        self.input_field = TextInput(hint_text='Enter value for X', input_filter='float')
        self.result_label = Label(text='Result:')
        self.calc_button = Button(text='Calculate')
        self.calc_button.bind(on_press=self.calculate_result)
        
        self.layout.add_widget(self.input_label)
        self.layout.add_widget(self.input_field)
        self.layout.add_widget(self.calc_button)
        self.layout.add_widget(self.result_label)

        return self.layout
    
    def calculate_result(self, instance):
        try:
            X = float(self.input_field.text)
            result = ((math.sqrt(X)*180) - 225) % 360
            self.result_label.text = f'Result: {result:.2f}'
        except ValueError:
            self.result_label.text = 'Invalid input. Please enter a numeric value.'
        
FormulaApp().run()