# knowledge_graph/properties.py

class Property:
    def __init__(self, name, value, data_type):
        self.name = name
        self.data_type = data_type
        self.value = self._convert_value(value)
        self.validate()  # Validate the property upon initialization

    def _convert_value(self, value):
        try:
            return self.data_type(value)
        except ValueError:
            raise TypeError(f"Property '{self.name}' must be of type '{self.data_type.__name__}'")

    def validate(self):
        """Validate the property value against its data type."""
        if not isinstance(self.value, self.data_type):
            raise TypeError(f"Property '{self.name}' must be of type '{self.data_type.__name__}'")

    def __repr__(self):
        return f"Property(name={self.name}, value={self.value}, data_type={self.data_type})"
