import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("spotify-2023.csv", encoding='ISO-8859-1')

# Print out the the entire csv file
print(df.to_string())

# Find out the data in depth by analyzing the columns and types
print(df.info())

# Remove empty columns in the original dataframe
df.dropna(inplace=True)

# Show the correlation between the columns to show relationships
# print(df.corr())

print(df['artist(s)_name'])

filtered_df = df[df['artist(s)_name'] == 'Miley Cyrus']
print(filtered_df['in_spotify_playlists'].sum())

#
# df.plot(kind='bar', x='artist(s)_name', y='in_spotify_playlists', title='Most Popular Tracks in Spotify')
# plt.xlabel('Track Name')
# plt.ylabel('In Spotify Playlist')
# plt.show()