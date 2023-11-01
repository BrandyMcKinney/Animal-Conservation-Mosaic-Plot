import json
import re
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.graphics.mosaicplot import mosaic

with open("data.json", "r") as text:
  data = json.load(text)
  for item in data:
    #go in depth with this line 8. Break it down.
    #what is regex? more info.
    #why is space important after "" in re.compile?
    item["Category"] = re.compile(" [\ .(]").split(item["Category"])[0]

  print(data)

classes = ["Mammalia", "Aves", "Reptilia"]
statuses = ["Endangered", "Critically endangered", "Vulnerable"]

mosaic_data = []
for item in data:
  if item["Category"] in statuses and item["Animal Class"] in classes:
    mosaic_data.append(item)

properties = {
    "Endangered": {
        "color": "red"
    },
    "Critically endangered": {
        "color": "purple"
    },
    "Vulnerable": {
        "color": "green"
    }
}

plt.rc("font", size=8)

mosaic_dataframe = pd.DataFrame(mosaic_data)
fig = mosaic(mosaic_dataframe, ["Category", "Animal Class"],
             title="Conservation Status by Animal Class",
             gap=[0.02, 0.02],
             axes_label=True,
             properties=lambda x: properties[x[0]])

plt.savefig("mosaic_plot.png")
