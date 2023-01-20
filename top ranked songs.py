"""
title: top ranked songs
description: Find songs that have ranked in the top position. 
             Output the track name and the number of times it 
             ranked at the top. Sort your records by the number 
             of times the song was in the top position in descending order.
"""
# Import your libraries
import pandas as pd

# Start writing code
spotify_worldwide_daily_song_ranking.head()
spotify_worldwide_daily_song_ranking[spotify_worldwide_daily_song_ranking['position'] == 1].groupby('trackname').sum().reset_index().sort_values(by='position', ascending = False)
