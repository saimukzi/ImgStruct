import argparse
import cv2 as cv
import futsu.json
import img_struct.element as element
import numpy as np


class Main:

    def main_cmd(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('input_path')
        parser.add_argument('output_path')
        parser.add_argument('--output_id', nargs='?')
        args = parser.parse_args()

        self.main(
            input_path=args.input_path,
            output_path=args.output_path,
            output_id=args.output_id,
        )

    def main(self, input_path, output_path, output_id=None):
        print(f'input_path={input_path}')
        print(f'output_path={output_path}')
        print(f'output_id={output_id}')

        self.input_path = input_path
        self.output_path = output_path
        self.output_id = output_id

        self.input_data = futsu.json.path_to_data(input_path)
        self.output_data = self.get_output_data()
        self.root_element = self.render_root_element()
        self.img_f1_np = self.create_draw_buffer()
        self.draw_element()
        self.img_iff_np = self.create_output_buffer()
        cv.imwrite(output_path, self.img_iff_np)

    def get_output_data(self):
        output_dict = self.input_data['output_dict']
        if self.output_id is None:
            return list(output_dict.values())[0]
        return output_dict[self.output_id]

    def render_root_element(self):
        return element.render_element(
            self.output_data['element'],
            self
        )

    def create_draw_buffer(self):
        return np.zeros(
            (self.output_data['size']['h'], self.output_data['size']['w'], 4),
            np.float
        )

    def draw_element(self):
        pass

    def create_output_buffer(self):
        tmp = self.img_f1_np
        tmp = tmp.clip(min=0, max=1)
        tmp = tmp * 255
        tmp = tmp.round()
        tmp = tmp.astype(np.uint8)
        return tmp

def main_cmd():
    main = Main()
    main.main_cmd()


def main(*argv, **kwargs):
    main = Main()
    main.main(*argv, **kwargs)


if __name__ == '__main__':
    main_cmd()
