import numpy as np
import os
import re
import pdb
import pandas as pd

class Skeleton:
    def __init__(self, skel={}):
        self.skel = skel

    def __str__(self):
        return str(self.skel)

    def __repr__(self):
        return str(self.skel)

    def __getitem__(self, key):
        return self.skel[key]

    def __setitem__(self, key, value):
        self.skel[key] = value

class BVH_parser:
    def __init__(self, file_path):
        self.file_path = file_path
        self.skel = Skeleton()
        self.motion = None
        self.parse()



    def parse_hierarchy(self, lines):
        self.skel['root'] = self.parse_node(lines)

    def parse_node(self, lines):
        node = {}
        line = lines.pop(0)
        node['name'] = line.split()[1]
        line = lines.pop(0)
        node['offset'] = [float(x) for x in line.split()[1:]]
        line = lines.pop(0)
        node['channels'] = line.split()[2:]
        line = lines.pop(0)
        if line.startswith('JOINT'):
            node['children'] = []
            while line.startswith('JOINT'):
                node['children'].append(self.parse_node(lines))
                line = lines.pop(0)
            node['children'].append(self.parse_node(lines))
        elif line.startswith('End Site'):
            node['children'] = []
        else:
            raise Exception('Invalid line: ' + line)
        return node

    def parse(self):
        with open(self.file_path, 'r') as f:
            lines = f.readlines()
            for line in lines:
                if line.startswith('HIERARCHY'):
                    self.parse_hierarchy(lines)
                elif line.startswith('MOTION'):
                    self.parse_motion(lines)
        line = lines.pop(0)
        line = lines.pop(0)
        self.motion = pd.DataFrame(columns=line.split())
        line = lines.pop(0)
        while line:
            self.motion = self.motion.append(pd.Series(line.split(), index=self.motion.columns), ignore_index=True)
            line = lines.pop(0)

    def parse_motion(self, lines):
        pass

    print(bvh_parser.motion)

if __name__ == '__main__':
    bvh_parser = BVH_parser('../data/01.bvh')
    print(bvh_parser.skel)
import numpy as np
import os
import re
import pdb

class Skeleton:
    def __init__(self, skel={}):
        self.skel = skel

    def __str__(self):
        return str(self.skel)

    def __repr__(self):
        return str(self.skel)

    def __getitem__(self, key):
        return self.skel[key]

    def __setitem__(self, key, value):
        self.skel[key] = value

    def __complex__(self):
        return complex(self.skel)
class BVH_parser:
    def __init__(self, file_path):
        self.file_path = file_path
        self.skel = Skeleton()
        self.parse()



    def parse_hierarchy(self, lines):
        self.skel['root'] = self.parse_node(lines)

    def parse_node(self, lines):
        node = {}
        line = lines.pop(0)
        node['name'] = line.split()[1]
        line = lines.pop(0)
        node['offset'] = [float(x) for x in line.split()[1:]]
        line = lines.pop(0)
        node['channels'] = line.split()[2:]
        line = lines.pop(0)
        if line.startswith('JOINT'):
            node['children'] = []
            while line.startswith('JOINT'):
                node['children'].append(self.parse_node(lines))
                line = lines.pop(0)
            node['children'].append(self.parse_node(lines))
        elif line.startswith('End Site'):
            node['children'] = []
        else:
            raise Exception('Invalid line: ' + line)
        return node

    def parse(self):
        with open(self.file_path, 'r') as f:
            lines = f.readlines()
            for line in lines:
                if line.startswith('HIERARCHY'):
                    self.parse_hierarchy(lines)
                elif line.startswith('MOTION'):
                    self.parse_motion(lines)

    def parse_motion(self, lines):
        pass


if __name__ == '__main__':
    bvh_parser = BVH_parser('../data/01.bvh')
    print(bvh_parser.skel)

