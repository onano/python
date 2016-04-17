class PlayersList(list):
    def __init__(self, pName, pDob, p_timing=[]):
        list.__init__([])  # defining a empty list
        self.name = pName
        self.dob = pDob
        self.extend(p_timing)

    def getTopTime(self, val):
        return sorted(set([fix_file_data(each_t) for each_t in self]))[:val]


def open_file(filename):
    try:
        with open(filename, 'r') as fr:
            try:
                data = fr.readline().strip().split(',')
                return PlayersList(data.pop(0), data.pop(0), data)
            except ValueError:
                pass
    except IOError as err:
        print('IOError: ' + str(err))
        return (None)


def fix_file_data(time_t):
    if '-' in time_t:
        splitter = '-'
    elif '.' in time_t:
        splitter = '.'
    elif ':' in time_t:
        splitter = ':'
    else:
        return time_t

    (min, secs) = time_t.split(splitter)
    return min + '.' + secs


julie = open_file('julie.txt')

print(julie.name + "'s best 3 timings are :" + str(julie.getTopTime(3)))