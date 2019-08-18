FILE_NAME = 'testfilename.json'


class Investigator:
    uuid = 'testinvestigatoruuid'

class Item:
    uuid = 'testitemuuid'


class Portrait:
    test = '1'
    investigator = Investigator()


class FakePortrait:
    test = '1'
    item = Item()
