import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class MyGame(arcade.Window):

    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        # Set up your game here
        pass

    def on_draw(self):
        # Your drawing code goes here
        arcade.start_render()


    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """


    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """


    def update(self, delta_time):
        # All the logic to move, and the game logic goes here.


def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()