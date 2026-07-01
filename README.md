# Project-1---PTCG
# Phantom Dive Across NOLA

## Project Overview
This project aims to give a high level overview of the competitive scene surrounding the Pokémon Trading Card Game, introduce the concept of meta share, and highlight the meta share at a recent international tournament.

I found, as expected, that one deck in particular was highly favored among players. Not only was this deck popular it was also very successful.

## Data Collection
Data collection was largely already done by the [Limitless TCG](https://limitlesstcg.com) website, which works closely with Play Pokémon at competitive events. This website is the repository for most sanctioned tournaments, their results, and deck lists.

I scraped this website and did some analysis with Python and pandas, then exported the data to a CSV and created charts in Datawrapper.

## Process
Scraped tournament standings from Limitless TCG
Analyzed data using Python and pandas
Exported results to CSV
Built visualizations in Datawrapper

## Challenges & Reflections
This project was entirely new skills for me, especially while feeling behind as a result of working alongside the program. It felt like in one day I was able to compile all of the bits of information I needed to get started, and eventually piece them together.

The most challenging area — and where I grew the most was scraping, as this was a completely new skill to me.

## What I Wanted To Do But Couldn't

This is a 2 day tournament with Day 2 having 512 players out of nearly 4,000 who competed. I initially wanted to analyze the full 4,000 players, as both my fiancé and brother competed but did not make Day 2, I thought it would be fun to highlight them in the project.

However, scraping past the 512 player default filter on the Limitless website was difficult. I tried multiple scraping approaches, one successfully scraped multiple pages but far exceeded the 4,000 count, going into the tens of thousands by counting pages repeatedly.
For the sake of time, I decided to move forward with just the Day 2 list of 512 players

I also would have liked to do more in depth analysis on average tournament performance by deck, but when I sought help from AI for with this script it became very involved with multiple merges and complex details, I didnt want to use code that was completely foreign to me. I went with a simpler deck count limited to the top 64 players instead.

## Tools Used
Python
pandas
BeautifulSoup
Datawrapper

