import arcade
import breathing_square
import motion_binding
import arrow_lengths
import hidden_bird
import pause

SCRN_WIDTH = 800
SCRN_HEIGHT = 800
SCRN_TITLE = "Illusions Game"

MENU_1 = "Press 1 to start the Breathing Square!" 
MENU_2 = "Press 2 to start Motion Binding!"
MENU_3 = "Press 3 to start the Hidden Bird!"
MENU_4 = "Press 4 to start Arrow Lengths!"


class StartView(arcade.View):
    '''class that handles menu view'''
    def on_show(self):
        arcade.set_background_color(arcade.color.WHITE)


    def on_draw(self):
        arcade.start_render()
        arcade.draw_text(MENU_1, SCRN_WIDTH*0.5, SCRN_HEIGHT*0.65, (0,0,0), 20, anchor_x="center")
        arcade.draw_text(MENU_2, SCRN_WIDTH*0.5, SCRN_HEIGHT*0.55, (0,0,0), 20, anchor_x="center")
        arcade.draw_text(MENU_3, SCRN_WIDTH*0.5, SCRN_HEIGHT*0.45, (0,0,0), 20, anchor_x="center")
        arcade.draw_text(MENU_4, SCRN_WIDTH*0.5, SCRN_HEIGHT*0.35, (0,0,0), 20, anchor_x="center")


    # pass screen args to illusion classes
    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.KEY_1:
            game_view = breathing_square.BreathingSquare(SCRN_WIDTH, SCRN_HEIGHT)

        elif key == arcade.key.KEY_2:
            game_view = motion_binding.MotionBinding(SCRN_WIDTH, SCRN_HEIGHT)

        elif key == arcade.key.KEY_3:
            game_view = hidden_bird.HiddenBird(SCRN_WIDTH, SCRN_HEIGHT)

        elif key == arcade.key.KEY_4:
            game_view = arrow_lengths.ArrowLengths(SCRN_WIDTH, SCRN_HEIGHT)

        game_view.setup()
        self.window.show_view(game_view)


def main():
    window = arcade.Window(SCRN_WIDTH, SCRN_HEIGHT, SCRN_TITLE)
    start_view = StartView()
    window.show_view(start_view)
    arcade.run()


if __name__ == "__main__":
    main()
