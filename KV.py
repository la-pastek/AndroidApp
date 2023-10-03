#:import MDCardImage kivymd.uix.card.MDCardImage

KV = '''
ScreenManager:
    LoginScreen:
    HelloScreen:
    
<LoginScreen>:
    name: 'login'
    MDTextField:
        id: username
        hint_text: "Matricule"
        width: "200dp"
        line_color_focus: 1, 0, 1, 1
        icon_left: "account"
        pos_hint: {'center_x': .5, 'center_y': .6}
        size_hint_x: None
    MDTextField:
        id: password
        hint_text: "Mot de passe"
        size_hint_x: None
        width: "200dp"
        password: True
        line_color_focus: 1, 0, 1, 1
        icon_left: "form-textbox-password"
        pos_hint: {"center_x": .5, "center_y": .5}
    MDRaisedButton:
        text: "Login"
        size_hint: None, None
        width: "100dp"
        height: "40dp"
        on_release: app.login()
        pos_hint: {"center_x": .5, "center_y": .4}  # Centrer le bouton horizontalement
        on_release: app.login()
    Image:
        source: "ACS-removebg-preview.png"
        size_hint: .36, .36
        pos_hint: {"center_x": .5, "center_y": .8}
<HelloScreen>:
    name: 'hello'
    orientation: 'vertical'
    AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'top'
        MDCard:
            orientation: 'vertical'
            size_hint: None, None
            width: root.width-20  # La largeur du MDCard est la même que celle de l'écran
            height: "150dp"
            radius: [20, 20, 20, 20]  # Coins arrondis seulement en haut
            #rgb01(0.027, 0.027, 0.349, 0)
            md_bg_color: 0, 0, 0, 0.5  # Couleur bleue

            BoxLayout:
                orientation: 'vertical'
                padding: "10dp"

                MDLabel:
                    text: "Contenu de l'écran"
                    halign: 'center'
'''
