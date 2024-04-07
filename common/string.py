import random
import string

class String:
    def __init__(self, value=None):
        self.value = value
    
    def camelcase_to_underscore(self):
        return ''.join(['_'+i.lower() if i.isupper() else i for i in self.value]).lstrip('_')
    
    def lowercase_first_letter(self):
        return self.value[0].lower() + self.value[1:]
    
    def underscore_to_camelcase(self):
        words = self.value.split('_')
        # Capitalize the first letter of each word
        camelcased_words = [word.capitalize() for word in words]
        # Join the words without underscores
        camelcased_string = ''.join(camelcased_words)
        return camelcased_string

    def dbfile_to_class_name(self):
        # Remove the '.py' extension from the file name
        module_name = self.value.replace('.py', '')
        # Remove the prefix dynamically
        prefix_length = 0
        if module_name.endswith('migration'):
            prefix_length = 12
            
        class_name = module_name[prefix_length:]
        # Convert the class name to camel case
        words = class_name.split('_')
        # Capitalize the first letter of each word
        camelcased_words = [word.capitalize() for word in words]
        # Join the words without underscores
        class_name = ''.join(camelcased_words)
        
        return module_name, class_name

    def transform_class_name(self):
        # Convert class name to lowercase
        lowercased = self.value[0].lower() + self.value[1:]
        # Remove 'Model' from the end of the class name
        if lowercased.endswith('Model'):
            lowercased = lowercased[:-5]
        elif lowercased.endswith('Migration'):
            lowercased = lowercased[:-9]
        elif lowercased.endswith('Seeder'):
            lowercased = lowercased[:-6]
        # Convert class name to plural form
        # Example: User -> users, Product -> products
        if not lowercased.endswith('s'):
            if lowercased.endswith('y'):
                lowercased = lowercased[:-1] + 'ies'
            else:
                lowercased += 's'
        return lowercased
    
    def random_string(self, length=8):
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))