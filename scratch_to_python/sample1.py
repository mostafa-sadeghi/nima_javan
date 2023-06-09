# sample1 (pyStage, converted from Scratch 3)

from pystage.en import Sprite, Stage

stage = Stage()
stage.add_backdrop('backdrop1')
stage.add_backdrop('blue_sky')
stage.create_variable('speed')
sprite1 = stage.add_a_sprite(None)
sprite1.set_name("Sprite1")
sprite1.set_x(-187.17898559570312)
sprite1.set_y(-107)
sprite1.go_to_back_layer()
sprite1.go_forward(1)
sprite1.point_in_direction(-90)
sprite1.add_costume('costume1', center_x=48, center_y=50)
sprite1.add_costume('costume2', center_x=46, center_y=53)
sprite1.add_sound('meow')


def when_program_starts_1(self):
    self.point_in_direction(90.0)
    self.go_to_x_y(-190.0, -104.0)
    self.set_variable("speed", 0)
    self.set_rotation_style_left_right()
    while True:
        self.move(10.0)
        self.next_costume()
        self.wait(0.1)
        self.if_on_edge_bounce()


sprite1.when_program_starts(when_program_starts_1)


def when_key_pressed_2(self):
    self.set_variable("speed", 9)
    while not (self.y_position() < -107):
        self.change_y_by(self.get_variable("speed"))
        self.change_variable_by("speed", -0.8)

    self.set_y(-107.0)
    self.set_variable("speed", 0)


sprite1.when_key_pressed("space", when_key_pressed_2)

stage.play()
