import requests
import random
# import yaml
# import os

cronjobraw = "https://raw.githubusercontent.com/AdityaSeth777/AdityaSeth777/main/.github/workflows/profile-3d.yml"
cron = requests.get(cronjobraw)
croncontent = cron.text
croncontent = croncontent.split("\n")

oldcron = croncontent[3]
newcron =   f'  - cron: "0 */{str(random.randint(1, 8))} * * *"'

while (oldcron == newcron):
    newcron =  f'  - cron: "0 */{str(random.randint(1, 8))} * * *"'

croncontent[3] = newcron

yamlfile =  open('.github/workflows/Profile3D.yml', 'w')

yamlfile.write("\n".join(croncontent))

yamlfile.close()

print("Updated Cron Job")

# os.system('git add .')
# os.system('git commit -m "Cron Job Update"')
# os.system('git push')
