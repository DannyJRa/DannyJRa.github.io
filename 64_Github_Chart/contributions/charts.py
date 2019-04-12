#%%
import os
try:
	os.chdir(os.path.join(os.getcwd(), '64_Github_Chart'))
	print(os.getcwd())
except:
	pass

#%%
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.dates as mdates
#%%

filename = 'contributions/stats.json'

#%%
import json

with open(filename) as fp:
    data = json.load(fp)
    contributions = pd.DataFrame({
        'name': c['repo']['name'],
        'week': pd.to_datetime(stat['w'], unit='s'),
        'additions': stat['a'],
        'deletions': stat['d'],
        'commits': stat['c']
    } for c in data for stat in c['stats']['weeks'] if stat['c'])
    
contributions

#%%
# # time slice
#contrib = contributions[(pd.Timestamp('2014-09-01') < contributions.week) &
#                        (contributions.week < pd.Timestamp('2015-09-01'))]

# get top 20 contributions
nameg = contributions.groupby('name')
longest = (nameg.aggregate('max') - nameg.aggregate('min')).nlargest(20, 'week')
#contrib = contributions[contributions.name.isin(longest.index)]

# # all contributions
contrib = contributions

#%%
contrib = contrib.sort_values('week', ascending=True)

streaks = []
for repo_name, repo_group in contrib.groupby('name'):
    for _, streak_group in repo_group.groupby((repo_group.week.diff().dt.days > 30).cumsum()):
        start = streak_group.week.min()
        streaks.append(pd.Series({
            'name': repo_name,
            'start': start,
            'duration': streak_group.week.max() - start + pd.Timedelta('7 days'),
            'commits': streak_group.commits.mean()
        }))

sdf = pd.DataFrame(streaks)
sdf

#%%

names = sdf.sort_values('start', ascending=True).name.unique()
#%%
fig, ax = plt.subplots(figsize=(15, len(names) * .5), dpi=300)
ax.grid(linewidth=0.2, zorder=0)
for spine_name in ax.spines:
    if spine_name != 'bottom':
        ax.spines[spine_name].set_visible(False)

ax.xaxis_date()
ax.yaxis.set_ticks(range(0, len(names) * 2, 2))
for tic in ax.yaxis.get_major_ticks():
    tic.tick1On = tic.tick2On = False
    tic.label1On = tic.label2On = False
    
norm = mpl.colors.Normalize(vmin=sdf.commits.min(), vmax=sdf.commits.max())
color_map = plt.cm.copper

for i, repo_name in enumerate(names[::-1]):
    streak_group = sdf[sdf.name == repo_name]
    text_x = mdates.date2num(min(streak_group.start))
    ax.text(text_x, i * 2 + 1, repo_name, verticalalignment='center')
    for _, streak in streak_group.iterrows():
        start_dn = mdates.date2num(streak.start)
        end_dn = mdates.date2num(streak.start + streak.duration)
        color = color_map(norm(streak.commits))
        #ax.barh(bottom=i*2, width=(end_dn - start_dn), left=start_dn, 
        #        color=color, label=streak.name, align='center',zorder=2)
        
# add colorbar
cax, kw = mpl.colorbar.make_axes(ax, location='right',
                                fraction=0.02,
                                # shrink=0.2, aspect=22
                                )
cbar = mpl.colorbar.ColorbarBase(cax, norm=norm, cmap=color_map,
                                 label='Average # of commits per streak', **kw)
cbar.outline.set_visible(False)

ax.margins(0.01)
bxlim, exlim = ax.get_xlim()
span = (exlim - bxlim)
ax.set_xlim(bxlim - span * 0.05, exlim + span * 0.05)

plt.show()

#%%
fig.savefig('my-stats.png', dpi=300, bbox_inches='tight')