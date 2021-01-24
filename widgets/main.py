from kivy.uix.stacklayout import StackLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.app import App
from kivy.metrics import dp
from kivy.properties import StringProperty, BooleanProperty



class WidgetsExample(GridLayout):
    counter = 1
    count_enabled = BooleanProperty(False)
    my_text = StringProperty('1')
    slider_value_txt = '0'

    def on_button_click(self):
        # print('Button clicked')
        if self.count_enabled == True:
            self.counter += 1
            self.my_text = str(self.counter)


    def on_switch_active(self, widget):
        print('switch: ' + str(widget.active))


    def on_slider_value(self, widget):
        print('slider: ' + str(int(widget.value)))
        
        self.slider_value_txt = str(int(widget.value))


    def on_toggle_button_state(self, widget): # the widget we're getting is the toggle_button from thelab.kv
        print('toggle state: ' + widget.state)
        if widget.state == 'normal':
            widget.text = 'off'
            self.count_enabled = False
        else:
            widget.text = 'on'
            self.count_enabled = True


class StackLayoutExample(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # self.orientation = 'lr-bt'
        for i in range(0, 100):
            # size = dp(100) + i * 10
            size = dp(100)
            b = Button(text=str(i + 1), size_hint=(None, None), size=(size, size))
            self.add_widget(b)


# class GridLayoutExample(GridLayout):
#     pass



class AnchorLayoutExample(AnchorLayout):
    pass


class BoxLayoutExample(BoxLayout):
    pass
    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)

    #     self.orientation = 'vertial'

    #     b1 = Button(text='A')
    #     b2 = Button(text='B')
    #     b3 = Button(text='c')

    #     self.add_widget(b1)
    #     self.add_widget(b2)
    #     self.add_widget(b3)


class MainWidget(Widget):
    pass


class TheLabApp(App):
    pass


TheLabApp().run()