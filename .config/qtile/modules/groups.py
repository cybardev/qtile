from libqtile.config import Scratchpad, DropDown, Key, Group
from libqtile.command import lazy
from .keys import keys, mod

groups = [
    Scratchpad(
        "dropdown",
        [
            DropDown(
                "terminal", "xfce4-terminal", width=0.6, height=0.4, opacity=0.8
            )
        ],
    ),
    *[Group(i) for i in "123456789"],
]

keys.extend([
    Key([mod], "grave", lazy.group["dropdown"].dropdown_toggle("terminal"))
])

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod],
            i.name,
            lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),

        Key([mod], "Right", lazy.screen.next_group(),
            desc="Switch to next group"),

        Key([mod], "Left", lazy.screen.prev_group(),
            desc="Switch to previous group"),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"],
            i.name,
            lazy.window.togroup(i.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(i.name)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
        #     desc="move focused window to group {}".format(i.name)),
    ])
