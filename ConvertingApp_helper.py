KV="""
Screen:

    BoxLayout:
        orientation: "vertical"


        MDToolbar:
            title: "Schimb valutar"
            pos_hint: {"top": 1}
            elevation: 10

        MDGridLayout:
            cols: 2
            padding: "30dp"
            spacing: "20dp"
            row_force_default:True
            row_default_height: 40

            MDRaisedButton:
                text: "Din"
                on_release: app.show_example_list_bottom_sheet1()
                size_hint: (0.1, 0.5)

            MDLabel:
                id: label_item1
                theme_text_color: "Secondary"
                text: "Monedă"
                size_hint: (0.2, 0.5)
                halign: "center"

        MDGridLayout:
            cols: 2
            padding: "30dp"
            spacing: "20dp"
            row_force_default:True
            row_default_height: 40

            MDRaisedButton:
                text: "În"
                on_release: app.show_example_list_bottom_sheet2()
                size_hint: (0.1, 0.5)
            MDLabel:
                id: label_item2
                theme_text_color: "Secondary"
                text: "Monedă"
                size_hint: (0.2, 0.5)
                halign: "center"

        MDGridLayout:
            cols: 2
            padding: "30dp"
            spacing: "20dp"
            row_force_default:True
            row_default_height: 40

            MDTextField:
                id: user_input
                size_hint: (None, None)
                width: "100dp"
                hint_text: "Valoare"
                helper_text: "Introduceți valoarea."
                helper_text_mode: "on_focus"


            MDLabel:
                id: result_label
                text: 'Rezultat'
                theme_text_color: "Secondary"
                size_hint: (0.2, 0.5)
                halign: "center"

        MDBoxLayout:
            padding: "20dp"
            orientation: "horizontal"
            MDRectangleFlatButton:
                text: 'Schimbă'
                pos_hint: {"center_x": .5, "center_y": 1}
                size_hint: (0.5, 0.6)
                on_release: app.convert()

            MDRectangleFlatButton:
                text: 'Șterge'
                pos_hint: {"center_x": .5, "center_y": 1}
                size_hint: (0.5, 0.6)
                on_release: app.clear_info()



"""
