from enum import Enum

class RelationshipType(Enum):
    IS_A = "is_a"
    PART_OF = "part_of"
    CAUSES = "causes"
    USES = "uses"
    PARTICIPATES_IN = "participates_in"
    OCCURS_IN = "occurs_in"
    INVOLVES = "involves"
