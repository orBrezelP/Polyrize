class MagicList:
    list = []
    cls_type = None

    def __init__(self, cls_type=None):
        self.cls_type = cls_type

    def __getitem__(self, key):
        if self.cls_type and len(self.list) == key:
            self.list.append(self.cls_type())
            return self.list[key]
        return self.list[key]

    def __setitem__(self, key, value):
        if key == len(self.list):
            self.list.append(value)

