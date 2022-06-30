import yaml
import sys

class YAMLConfig:
   def __init__(self, file_path, required_configs=[], optional_configs=[]):
      self.file_path = file_path
      self.required_configs = required_configs
      self.optional_configs = optional_configs
      self.config = None

   def load(self):
      with open(self.file_path, 'r') as f:
         self.config = yaml.load(f,yaml.CLoader)
         self.check_configs()

   def check_configs(self):
      for config in self.required_configs:
         if config not in self.config:
            print("Required configuration '{}' not found in {}".format(config, self.file_path))
            sys.exit(1)

      for config in self.optional_configs:
         if config not in self.config:
            print("Optional configuration '{}' not found in {}".format(config, self.file_path))

   def export(self, data):
      with open(self.file_path, 'w') as f:
         yaml.dump(data, f)

   def get(self, key):
      return self.config[key]
