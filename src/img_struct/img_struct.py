import argparse
import futsu.json

class Main:

  def main(self):
    parser = argparse.ArgumentParser()
    parser.add_argument('input_path')
    parser.add_argument('output_path')
    parser.add_argument('--output_id', nargs='?')
    self.args = parser.parse_args()

    print(f'input_path={self.args.input_path}, output_path={self.args.output_path}, output_path={self.args.output_id}')
  
    input_data = futsu.json.path_to_data(args.input_path)

  def get_output_data(input_data, args):


def main():

if __name__ == '__main__':
  main = Main()
  main.main()
