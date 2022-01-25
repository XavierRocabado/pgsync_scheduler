import sys
import yaml

print(yaml.__version__)

if __name__ == '__main__':

    stream = open(sys.argv[1], 'r')
    dictionary = yaml.load(stream, Loader = yaml.FullLoader)
    for key, value in dictionary.items():
        print(key + " : " + str(value))
