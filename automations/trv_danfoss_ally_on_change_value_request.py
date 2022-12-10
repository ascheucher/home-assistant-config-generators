import random
from pathlib import Path
from jinja2 import Environment, PackageLoader, select_autoescape


def create_id(len: int = 13) -> str:
    if len < 1:
        return ''

    return ''.join((
        str(random.randint(0, 9)),
        create_id(len=len-1)))


trvs = [
    'trv.gf_kitchen',
    'trv.uf_living-room_west',
    'trv.uf_living-room_north',
    'trv.gf_hw_west',
    'trv.uf_office',
    'trv.gf_bath',
    'trv.gf_hw_east',
    'trv.gf_guest-room',
    'trv.uf_bedroom',
    'trv.gf_toilet']

env = Environment(
    loader=PackageLoader(package_name="templates", package_path="files"),
    autoescape=select_autoescape())

template = env.get_template("update_danfoss_ally_trvs_on_change.yaml")

outfile = Path("automations/out",
               "update_danfoss_ally_trvs_on_change_automations.yaml")
if outfile.exists():
    outfile.unlink()

with open(outfile, mode='w', encoding='utf8') as fh:
    for trv_friendly_name in trvs:

        env = dict(
            automation_id=create_id(),
            trv_friendly_name=trv_friendly_name
        )
        fh.write(template.render(env))
        fh.write('\n')
