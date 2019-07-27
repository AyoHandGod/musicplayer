from uuid import uuid1


class MenuItem(object):
    def __init__(self, label, data, selected=False):
        """
        Initialize a Menu Item.

        Args:
            label: Label for menu item.
            data: Raw data returned by Spotify.
            selected: Flag, whether or not item selected.
        """

        self.id = str(uuid1())
        self.data = data
        self.label = label

        def return_id():
            """
            Get it id and uri.

            Returns:
                Tuple containing item id and uri for use with Spotify.
            """
            return self.data['id'], self.data['uri']

        self.action = return_id
        self.selected = selected

    def __eq__(self, other):
        return self.id == other.id

    def __len__(self):
        return len(self.label)

    def __str__(self):
        return self.label


if __name__ == '__main__':
    for i in range(1, 101):
        out = ""
        if i % 3 == 0:
            out = "fizz"
        if i % 5 == 0:
            out += "buzz"
        if out:
            print(out)