from model.group import Group
import random


def test_modify_random_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    random_group = random.choice(old_groups)
    group = Group(name="New group")
    app.group.modify_group_by_id(random_group.id, group)
    new_groups = db.get_group_list()
    for index in range(len(old_groups)):
        if old_groups[index].id == random_group.id:
            old_groups[index].name = group.name
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
