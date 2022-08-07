import argparse
import cv2 as cv
import futsu.json
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
        # self.root_element = render_element(self.output_data['element'])
        self.img_f1 = np.zeros(
            (self.output_data['size']['h'], self.output_data['size']['w'], 4),
            np.float
        )
        tmp = self.img_f1
        tmp = tmp.clip(min=0, max=1)
        tmp = tmp * 255
        tmp = tmp.round()
        tmp = tmp.astype(np.uint8)
        self.img_iff = tmp
        cv.imwrite(output_path, self.img_iff)

    def get_output_data(self):
        output_dict = self.input_data['output_dict']
        if self.output_id is None:
            return list(output_dict.values())[0]
        return output_dict[self.output_id]


def main_cmd():
    main = Main()
    main.main_cmd()


def main(*argv, **kwargs):
    main = Main()
    main.main(*argv, **kwargs)


if __name__ == '__main__':
    main_cmd()
