from Pyro4 import expose
target = 27


class Solver:
    def __init__(self, workers=None, input_file_name=None, output_file_name=None):
        self.input_file_name = input_file_name
        self.output_file_name = output_file_name
        self.workers = workers

    def solve(self):    # done

        array = self.read_input()
        step = len(array) / len(self.workers)

        mapped = []
        for i in range(0, len(self.workers)):
            mapped.append(self.workers[i].mymap(i * step, min((i + 1) * step, len(array) - 1), array))
        reduced = self.myreduce(mapped)
        self.write_output(reduced)

    @staticmethod
    @expose
    def mymap(a, b, array):     # to do
        result = []
        for aa in range(a, b):
            for bb in range(aa + 1, len(array)):
                if array[aa] + array[bb] == target:
                    result.append([array[aa], array[bb]])
        return result

    @staticmethod
    @expose
    def myreduce(mapped):       # to do / function to gather all data
        output = []
        for x in mapped:
            output = output + x.value
        return output

    def read_input(self):           # done
        f = open(self.input_file_name, 'r')
        array = f.readline().strip().split()
        for i in range(0, len(array)):
            array[i] = int(array[i])
        f.close()
        return array

    def write_output(self, output):         # done
        f = open(self.output_file_name, 'w')
        f.write(str(output))
        f.close()
