import curses
import curses.panel
from uuid import uuid1


class Panel(object):

    def __init__(self, title: str, dimensions: tuple):
        """
        Instantiate a panel object.

        Args:
            title: Title for Panel
            dimensions: Tuple representing height, width, y, and x dimensions for panel.
        """
        height, width, y, x = dimensions

        self._win = curses.newwin(dimensions)
        self._win.box()
        self._panel = curses.panel.new_panel(self._win)
        self.title = title
        self._id = uuid1()

        self._set_title()

        self.hide()

    def hide(self):
        """
        Set the state of the panel to hidden.

        Returns:
            Panel state set to hidden.
        """
        self._panel.hide()

    def _set_title(self):
        """
        Set and Format the title for Panel.

        Returns:

        """

        formatted_title = f' {self.title} '
        self._win.addstr(0, 2, formatted_title, curses.A_REVERSE)

    def show(self):
        """
        Make the panel viewable.

        Clears the window, and draws border. Sets title
        and then disables the cursor. Finally, calls show
        on panel.

        Returns:

        """

        self._win.clear()
        self._win.box()
        self._set_title()
        curses.curs_set(0)
        self._panel.show()

    def is_visible(self):
        """
        Returns whether or not panel is visible.

        Returns:
            True if panel visible, False otherwise.

        """
        return not self._panel.hidden()

    def __eq__(self, other):
        """
        Compare whether two panels are the same by comparing
        uuid values.

        Args:
            other (Panel): Panel object to be compared with.

        Returns:
            True if Panel is the same, False otherwise.
        """
        return self._id == other._id


if __name__ == '__main__':

    panel = Panel("test", (30, 30, 10, 10))
    panel.show()