# Election_Analysis

## Project Overview
The purpose of this election audit analysis is to comb through the election data for a Colorado congressional election, and return the results in an easy-to-read concise report. 

## Election-Audit Results

* There were 369,711 total votes cast

* Total votes broken down by county are as follows:
    
    * County: Arapahoe, number of votes: 24,801 (6.7% of total votes)
    
    * County: Denver, number of votes: 306,055 (82.8% of total votes)
    
    * County: Jefferson, number of votes: 38,855 (10.5% of total votes)
    
 * The county of Denver had the largest number of votes with 306,055
 
 * Total votes broken down by candidate are as follows:
 
   * Candidate: Charles Casper Stockham, votes recieved: 85,213 (23% of total votes cast)

   * Candidate: Diana DeGette, votes received: 272,892 (73.8% of total votes cast)

   * Candidate: Raymon Anthony Doane, votes received: 11,606 (3.1% of total votes cast)
   
 * The winning candidate was __Diana DeGette__. She recieved __272,892__ votes which accounted for __73.8% of the total votes cast in the election.__

## Election-Audit Summary:
The script written for this campaign did exactly what it was supposed to and returned all the results we were looking for. However, this script could be modified to work beyond just this single election. Something else we might be interested in would be number of registered voters per county vs. the number of votes cast per county to give us a an active voter percentage per county. This might look like this:

votes = county_votes.get(county_name)

active_voter_percentage = float(votes) / float(county_voters) * 100

Something else we could change based on what level the election is would be the variables. If if was a mayoral campaign we could change the "county" variables to "district". We could also add other variables like candidates or different districts with the append. function.
