import argparse
import cv2 as cv
import futsu.json
import numpy as np

class Main:

  def main(self):
    parser = argparse.ArgumentParser()
    parser.add_argument('input_path')
    parser.add_argument('output_path')
    parser.add_argument('--output_id', nargs='?')
    self.args = parser.parse_args()

    print(f'input_path={self.args.input_path}, output_path={self.args.output_path}, output_path={self.args.output_id}')
  
    self.input_data = futsu.json.path_to_data(self.args.input_path)
    self.output_data = self.get_output_data()
    #self.root_element = render_element(self.output_data['element'])
    self.img = np.zeros((self.output_data['size']['h'], self.output_data['size']['w'], 4), np.uint8)
    cv.imwrite(self.args.output_path, self.img)

  def get_output_data(self):
    output_dict = self.input_data['output_dict']
    if self.args.output_id == None:
      return list(output_dict.values())[0]
    return output_dict[self.args.output_id]


def main():
  main = Main()
  main.main()

if __name__ == '__main__':
  main()
