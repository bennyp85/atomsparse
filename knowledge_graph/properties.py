# knowledge_graph/properties.py

class Property:
    def __init__(self, name, value, data_type):
        self.name = name
        self.value = value
        self.data_type = data_type

    def validate(self):
        """Validate the property value against its data type."""
        if not isinstance(self.value, self.data_type):
            raise TypeError(f"Value '{self.value}' of property '{self.name}' is not of type {self.data_type}")

    def __repr__(self):
        return f"Property(name={self.name}, value={self.value}, data_type={self.data_type})"
