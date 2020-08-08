from core.models import *

def run():
    for user in MyUser.objects.all():
        if hasattr(user, 'mix'):
            try:
                group, _ = Group.objects.get_or_create(title=user.platform.title.split()[0].lower())
            except Exception as e:
                print(user, e)
                continue
            user.the_group = group
            user.save()
            print(user, group)
            user.mix.editable = False
            user.mix.save()

