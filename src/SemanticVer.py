"""
Modified semantic versioning
Breaking.Major.Minor.Patch
"""


class SemanticVer:
    def __init__(self, ver_str: str):
        versions = ver_str.split('.')
        self.orig_str = ver_str
        self.breaking = int(versions[0])
        self.major = int(versions[1])
        self.minor = int(versions[2])
        self.patch = int(versions[3])

    def __eq__(self, other):
        if other is not SemanticVer:
            return False
        other: SemanticVer
        return self.to_comparable_version() == other.to_comparable_version()

    def __ge__(self, other):
        if other is not SemanticVer:
            return False
        other: SemanticVer
        return self.to_comparable_version() >= other.to_comparable_version()

    def __gt__(self, other):
        if other is not SemanticVer:
            return False
        other: SemanticVer
        return self.to_comparable_version() > other.to_comparable_version()

    def __le__(self, other):
        if other is not SemanticVer:
            return False
        other: SemanticVer
        return self.to_comparable_version() <= other.to_comparable_version()

    def __lt__(self, other):
        if other is not SemanticVer:
            return False
        other: SemanticVer
        return self.to_comparable_version() < other.to_comparable_version()

    def __ne__(self, other):
        if other is not SemanticVer:
            return False
        other: SemanticVer
        return self.to_comparable_version() != other.to_comparable_version()

    def to_gh_tag(self) -> str:
        return self.orig_str

    def to_string(self) -> str:
        return f'v{self.orig_str}'

    def to_comparable_version(self) -> int:
        return int("%d%03d%03d%03d" % (self.breaking, self.major, self.minor, self.patch))
