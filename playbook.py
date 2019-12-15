import configparser
from astropy.table import Table
import numpy as np

config = configparser.ConfigParser()
config.read('./plays.config')

plays = Table.read('./plays.txt', format='ascii')

sections = config.sections()

play_types = ["both", "both", "man", "zone"]

playbook = []
for s in sections:
    if "scorer" in s:
        pos = config[s]["pos"]
        skills = eval(config[s]["skills"])
        num = int(config[s]["num"])
        ind = np.where(plays['pos'] == pos)
        tmp = plays[ind]

        num_assigned = 0
        for skill in skills:
            skill_ind = np.char.find(tmp['type'], skill) == 0
            skill_tmp = tmp[skill_ind]

            if len(skill_tmp) == 0:
                continue
            selection = np.random.randint(len(skill_tmp))
            for_player = (skill_tmp['playbook'][selection], skill_tmp['play'][selection])
            if for_player not in playbook:
                playbook.append(for_player)
                # print(num_assigned, pos, for_player, skill)
                num_assigned += 1

        assert(num_assigned <= num)
        iter = 0
        while (num_assigned < num) & (iter < 100):
            for pt in play_types:
                if num_assigned >= num:
                    continue
                ind2 = np.where(tmp['defense'] == pt)
                tmp2 = tmp[ind2]
                if len(tmp2) == 0:
                    iter += 1
                    continue

                selection = np.random.randint(len(tmp2))
                player_types = tmp2['type'][selection].split(' ')
                for pt2 in player_types:
                    if pt2 in skills:
                        for_player = (tmp2['playbook'][selection], tmp2['play'][selection])
                        if for_player not in playbook:
                            playbook.append(for_player)
                            num_assigned += 1

for p in playbook:
    print(p)