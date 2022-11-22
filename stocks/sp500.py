# %%
import pandas as pd

# %% data
sp500 = pd.read_csv('data/sp500_historical.csv', index_col='date', parse_dates=True)

nber_rec = pd.read_csv('data/USREC.csv', index_col='DATE', parse_dates=True)

# %% plot recessions

# join sp500 with nber_rec
sp500 = sp500.join(nber_rec, how='left')

# %%
# plot sp500 price with recession bars
ax = sp500['nominal'].plot(title='S&P 500', figsize=(12, 6))
ax.fill_between(sp500.index, sp500['nominal'], where=sp500['USREC'] == 1, color='red', alpha=0.2)

# # set x-limit from Dec 1969 to Dec 1970
# ax.set_xlim('2001-03-01', '2001-11-01')

# # adjust y-axis to max value shown
# ax.set_ylim(0, 1400)

# set y-axis to log scale
ax.set_yscale('log')

# %% average drawdown during recessions

rec_dates = [
    ('1969-12-01', '1970-12-01'),
    ('1973-11-01', '1975-03-01'),
    ('2001-03-01', '2001-11-01')
]

acc = []
for start, end in rec_dates:
    # get the drawdown during the recession
    rec = sp500.loc[start:end, 'nominal']
    dd = rec.min() / rec.max() - 1

    acc.append(dd)

# print median acc
print(f'Median drawdown during recessions: {pd.Series(acc).median():.2%}')