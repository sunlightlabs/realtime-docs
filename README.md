# Real-Time Federal Campaign Finance API


##Overview

The base url for the API is `/api/` ; any
addresses in the below must be appended to the base url. All API calls
require an active [Sunlight API
key](http://services.sunlightlabs.com/accounts/register/). For instance, a call
to  would look like `/api/new_filing/?format=json&apikey=[API key]`. API [methods](#methods) and [return
types](#return_types) are described below.

An interactive page that allows you to try and test live api calls is available [here](http://tryit.sunlightfoundation.com/realtime/). 

## Formats

The API returns results in 'json' or 'csv' formats. Json results are paginated and return a maximum of 100 results per page. The csv results are not paginated--only a single page of csv results is returned--and the number of rows is capped at 2,000. For larger result sets, see the [downloads page](http://realtime.influenceexplorer.com/download-index/). CSV results include a header row.

When the format is 'json', return objects contain top-level keys: 'count' showing the total number of objects that match the query; 'next', a url for the next page of results; 'previous' for the previous page of results. The actual result objects are returned in the 'results' array.  

    {
    "count": 88887,
    "next": "http://realtime.influenceexplorer.com/api/new_filing/?page=2&page_size=10&format=json&apikey=[APIKEY]",
    "previous": null,
    "results": [
        { …
      


   
All json API calls can be given a `page` parameter to dictate the page number of the results and `page_size` parameters. 

<a id="methods"></a>
##API Methods 


##/new_filing/
Return summary info about electronic FEC filings 

###Parameters


`format` : The format of the returned data. Default is json.

`page` : The page number of results to return. Default is 1. 

`page_size` : The number of page results to return. for json, the default is 100 and the maximum is 100. This parameter is ignored for csv downloads, which return all matching rows, with a limit of 2000 total rows returned.

`candidate_id` : The FEC's id for the candidate connected to this committee. Only authorized committees are connected to candidates; leadership pacs are unconnected.

`committee_class` : The one letter code that describes the type of committee (see the committee reference above). Multiple committee types are allowed--a search for house and senate candidate committees would use HS, for instance.

`min_coh` : The minimum cash on hand of a report to include. Not all electronic reports include a cash on hand, so using this option will exclude all of those that do not report this figure.

`min_raised` : The minimum money raised. Not all electronic reports include an amount raised, so using this option will exclude all of those that do not report this figure.

`min_spent` : The minimum money spent. Not all electronic reports include an amount spent, so using this option will exclude all of those that do not report this figure.

`period_type` : The type of periodic report to include--could be monthly, quarterly or semiannual. The value includes the type; M for monthly, Q for quarterly, and S for semiannually and the period number; so a second quarter report would be Q2 and a monthly report covering August would be M8. Using this option will only return periodic reports.

`year_covered` : The calendar year that a periodic report covers. Non-periodic reports that do not cover a particular time period will be excluded.

`time_range` : Only show reports received within one of the following time ranges: today, in the last seven days, or at any time in this cycle.

`report_type` : The type of report to include

`is_superceded` : When an amended version of an older filing is received we consider the original to have been superseded. When set to false, show only the most recent versions of an electronic filing; when set to True, show only original filings which have since been amended.

###new_filing return values


`fec_id` : The FEC id of the committee filing this report

`committee_name` : The committee's name as reported to the FEC

`filing_number` : The numeric filing number assigned to this electronic filing by the FEC

`form_type` : The type of form used.

`filed_date` : The date that this filing was processed

`coverage_from_date` : The start of the reporting period that this filing covers. Not all forms list this.

`coverage_to_date` : The end of the reporting period that this filing covers. Not all forms include this

`is_superpac` : Is this group a super PAC?

`committee_designation` : See the FEC's [committee designations](http://www.fec.gov/finance/disclosure/metadata/DataDictionaryCommitteeMaster.shtml)

`committee_type` : See the FEC's [committee types](http://www.fec.gov/finance/disclosure/metadata/CommitteeTypeCodes.shtml)

`coh_end` : The cash on hand at the end of the reporting period. 

`new_loans` : The amount of new loans taken on by the committee during this reporting period.

`tot_raised` : The total amount raised in this report. This is total receipts for periodic reports.

`tot_spent` : The total amount spent in this report.

`lines_present` : A dictionary of the type of lines present in this report by schedule. 

`form_name` : A dictionary of the type of lines present in this report by schedule. 

`skeda_url` : A dictionary of the type of lines present in this report by schedule. 

`spending_url` : A dictionary of the type of lines present in this report by schedule. 

`absolute_url` : A dictionary of the type of lines present in this report by schedule. 

`committee_url` : A dictionary of the type of lines present in this report by schedule. 

`process_time_formatted` : A dictionary of the type of lines present in this report by schedule. 

`is_superceded` : Is this filing superceded by another filing, either a later amendment, or a periodic filing? This should be false for data returned through the API.


##/independent-expenditures/
Return information about independent expenditures reported to the FEC. Independent expenditures are campaign spending by outside groups that are not made in coordination with the candidate, but support or oppose someone running for office. They must be reported within 24 or 48 hours. Any domestic entity can make an independent expenditure in any amount they want, including corporations, unions and nonprofits. 

###Parameters


`format` : The format of the returned data. Default is json.

`page` : The page number of results to return. Default is 1. 

`page_size` : The number of page results to return. for json, the default is 100 and the maximum is 100. This parameter is ignored for csv downloads, which return all matching rows, with a limit of 2000 total rows returned.

`support_oppose_checked` : Whether the expenditures supports (S) or opposes (O) a candidate.

`min_spent` : The minimum money spent on an independent expenditure.

`filer_committee_id_number` : The FEC id of the committee making the expenditure. This is a nine-character code that begins with 'C'.

`candidate_id_checked` : The FEC id of the candidate targeted (either supported or opposed) by the independent expenditure. This is a nine-character code that begins with 'H', 'S', or 'P'.

`district_checked` : The internal id of the district the candidate is running in. The id can be determined by using the /districts/ endpoint.

`candidate_state_checked` : The two-digit postal code of the state in which the candidate targeted is running, e.g. 'NC' or 'OK'

`candidate_office_checked` : A one-digit code for the office the candidate targeted by the expenditure is seeking: 'H' for House or 'S' for Senate.

`candidate_district_checked` : A two digit code showing the district number of house candidates only. The first district would be '01'. States with at-large house districts, e.g. North Dakota, are assigned '00'. This number is not reliably assigned to senate districts; sometimes a '00' is used, sometimes the value is null

`candidate_party_checked` : A one digit code representing the party of the candidate targeted by the expenditure: 'D' for Democrat and 'R' for Republican. This value is often missing for third party candidates.

###independent-expenditures return values


`form_type` : The type of from this expenditure was reported on. See more about [FEC forms](http://www.fec.gov/info/forms.shtml).

`superceded_by_amendment` :  Is this filing superceded by another filing, either a later amendment, or a periodic filing? This should be false for data returned through the API.


`candidate_id_checked` : The FEC id of the candidate targeted by this independent expenditure. This is added whenever possible from expenditures that are missing it.

`candidate_name` : The candidate's name.

`candidate_party_checked` : The candidate's party. This is added whenever possible from expenditures that are missing it.

`candidate_office_checked` : The candidate's office. This is added whenever possible from expenditures that are missing it.

`candidate_state_checked` : The state the candidate is running in. This is absent from presidential candidates. This is added whenever possible from expenditures that are missing it.

`candidate_district_checked` : The candidate's district, if applicable. This is added whenever possible from expenditures that are missing it.

`support_oppose_checked` : Whether the expenditure supports (S) or opposes (O) the candidate.

`committee_name` : The name of the committee making the expenditure

`transaction_id` : The transaction id from the original filing. These ids are unique per report, not necessarily per cycle.

`payee_organization_name` : The name of the organization being paid

`payee_street_1` : The street address of the payee

`payee_street_2` : The street address of the payee -- second part, if needed.

`payee_city` : The payee's city

`payee_state` : Payee state

`payee_zip` : Payee ZIP code

`payee_name_simplified` : Payee ZIP code

`election_code` : The code describing the election

`election_other_description` : Any additional description of the election

`expenditure_date_formatted` : The date of the expenditure

`expenditure_amount` : The expenditure amount

`expenditure_purpose_code` : The filer-entered code of the expenditure. This isn't required.

`expenditure_purpose_descrip` : The filer-described purpose of the expenditure

`date_signed_formatted` : Populated from parsing raw field

`memo_code` : This is an X for lines that are subitemizations

`memo_text_description` : A text description of unique circumstances surrounding this expenditure.

`filer_committee_id_number` : The FEC id of the committee making the expenditure.

`district_checked` : The district the expenditure was made it

`race_url` : The URL to the race page

`committee_url` : The URL to the committees page

`candidate_url` : The URL to the candidates page

`short_office` : A short version of the district

##/districts/
Summarize total spending by congressional district, including candidate spending and independent expenditures. Electioneering and 'communication cost' (promotion of candidates to members of a corporation or assocation) is not included. Also useful for retrieving IDs. 

###Parameters


`format` : The format of the returned data. Default is json.

`page` : The page number of results to return. Default is 1. 

`page_size` : The number of page results to return. for json, the default is 100 and the maximum is 100. This parameter is ignored for csv downloads, which return all matching rows, with a limit of 2000 total rows returned.

`state` : The two-letter postal code for the state where the district is located, e.g. 'AK' or 'DE'.

`office` : A one-digit code for the district's office: 'H' for House or 'S' for Senate.

`office_district` : A two digit code showing the district number of house districts only. The first district would be '01'. States with at-large house districts, e.g. North Dakota, are assigned '00'. This number is not reliably assigned to senate districts; sometimes a '00' is used, sometimes the value is null

`term_class` : The term class used to describe Senate seats' election cycle. Term class 1 is up in 2018, 2 is up in 2014 and 3 is up in 2016. This value is null for house districts.

`incumbent_party` : A one letter code for the incumbent's political party: 'D' for Democrat and 'R' for Republican. Angus King, independent Senator of Maine, is listed as 'I'

###districts return values


`id` : An internal district id

`district_url` : The URL to this district's page

`cycle` : The even-numbered year that ends a two-year cycle.

`state` : The district's state

`office` : 'H' for House, 'S' for Senate, 'P' for President

`office_district` : '00' for at-large congress; null for senate, president

`term_class` : 1,2 or 3. Pulled from US Congress repo. Only applies to senators.

`incumbent_name` : The incumbent name

`incumbent_party` : Simplified party: D for Dem, DFL etc; R for R

`next_election_date` : Date of the next eelction

`next_election_code` : A code for the next election type

`next_election` : A text version of the next election

`open_seat` : Is the incumbent stepping down?

`candidate_raised` : Total amount raised by candidates who've run in this district during the cycle. Doesn't include incumbents who are not seeking reelection.

`candidate_spending` : Total amount spent by candidates who've run in this district during the cycle. Doesn't include incumbents who are not seeking reelection.

`outside_spending` : Total amount of independent expenditures for or against candidates in this district, not including incumbents who are not seeking reelection.

`total_spending` : Total candidate spending plus independent expenditures made in this race. This doesn't include several lesser spending categories: communication cost (paid communication from a union or corporation targeting their own members); coordinated expenditures made by a national party committee that aren't reported as inkind contributions; electioneering communications (which may target multiple candidates at once.)

`rothenberg_rating_id` : The code used by Rothenberg.

`rothenberg_rating_text` : The [Rothenberg Political Report's](http://rothenbergpoliticalreport.com/) rating of this district



##/candidates/
Returns information about candidates for federal office 

###Parameters


`format` : The format of the returned data. Default is json.

`page` : The page number of results to return. Default is 1. 

`page_size` : The number of page results to return. for json, the default is 100 and the maximum is 100. This parameter is ignored for csv downloads, which return all matching rows, with a limit of 2000 total rows returned.

`fec_id` : The FEC id of the candidate by the independent expenditure. This is a nine-character code that begins with 'H', 'S', or 'P'.

`state` : The two-letter postal code for the state where the candidate is running, e.g. 'AK' or 'DE'.

`office` : A one-digit code for the candidate's office: 'H' for House or 'S' for Senate.

`office_district` : A two digit code showing the district number of house districts only. The first district would be '01'. States with at-large house districts, e.g. North Dakota, are assigned '00'. This number is not reliably assigned to senate districts; sometimes a '00' is used, sometimes the value is null

`term_class` : The term class used to describe Senate seats' election cycle. Term class 1 is up in 2018, 2 is up in 2014 and 3 is up in 2016. This value is null for house districts.

`district` : An internal district id. Can be retrieved from the districts endpoint.

`party` : A one letter code for the incumbent's political party: 'D' for Democrat and 'R' for Republican. Angus King, independent Senator of Maine, is listed as 'I'. This value is often missing for third party candidates.

`is_incumbent` : Is the candidate an incumbent?

###candidates return values

A candidate is a person running for a particular office, e.g. Joe Smith for Senate. If Joe Smith is currently a member of the house, receipts by his house committee will not be counted towards his senate campaign (until they are transferred to an candidate committee authorized to support his senate bid).


`name` : Incumbent name

`fec_id` : FEC candidate id

`pcc` : FEC id for the candidate's primary campaign committee

`party` : Simplified party

`candidate_url` : Simplified party

`race_url` : Simplified party

`ie_url` : Simplified party

`is_incumbent` : Are they an incumbent? If not, they are a challenger

`cycle` : text cycle; even number.

`not_seeking_reelection` : True if they are an incumbent who is not seeking reelection.

`other_office_sought` : E.g. are they running for senate?

`other_fec_id` : If they've declared for another federal position, what is it? This should be the *candidate id* not a committee id. 

`election_year` : year of general election

`state` : The state the candidate is running in; US for president

`office` : The office the candidate is running for

`office_district` : '00' for at-large congress; null for senate, president

`term_class` : 1,2 or 3. Pulled from US Congress repo. Only applies to senators.

`candidate_status` : leave this blank until an election has been held--this is really a 'how did they lose' type of field.

`total_expenditures` : The total independent expenditures made supporting or opposing this candidate.

`expenditures_supporting` : The total amount of independent expenditures made to support this candidate.

`expenditures_opposing` : The total amount of independent expenditures made to oppose this candidate.

`total_receipts` : The total receipts of this candidates authorized campaign committees. Outside groups and leadership pacs, neither of which are authorized, do not count towards this total. Money raised by joint fundraising committees is reported once it is listed as having been received by the candidates' primary campaign committee. This total includes contributions of $1,000 and up as disclosed during the final 20 days of a campaign on 48-hour reports (Form F6).

`total_contributions` : The total of contributions reported by this candidate. 

`total_disbursements` : The total amount of money reported as spent by this candidate's authorized committee. 

`cash_on_hand` : The cash reported at the end of the most recent reporting period. 

`cash_on_hand_date` : The end of the most recent reporting period; the day that the cash on hand is reported on.

`district` : The candidate district.

`outstanding_loans` : 

##/committee/
Return summary information about a nonprofit that reports spending to the FEC or a PAC, including candidate committees, leadership PACs, joint fundraising committees, super PACs, hybrid super PACs party committees, corporate pacs, etc 

###Parameters


`format` : The format of the returned data. Default is json.

`page` : The page number of results to return. Default is 1. 

`page_size` : The number of page results to return. for json, the default is 100 and the maximum is 100. This parameter is ignored for csv downloads, which return all matching rows, with a limit of 2000 total rows returned.

`ctype` : The FEC committee type. See more about committee types at the top of the page.

`fec_id` : The FEC id of the committee by the independent expenditure. This is a nine-character code that begins with 'C'.

`min_raised` : The minimum amount reported as having been raised by the committee during the 2014 cycle.

`min_spent` : The minimum amount reported as having been spent by the committee during the 2014 cycle.

`min_coh` : The minimum cash on hand reported in the committee's most recent periodic filing.

###committee return values


`fec_id` : The FEC id of the filing committee

`name` : The committee name.

`total_receipts` : Total receipts for this committee ceived during the entire cycle. 

`total_disbursements` : Total disbursements by this committee ceived during the entire cycle

`outstanding_loans` : Total outstanding loans as of the cash_on_hand_date

`cash_on_hand` : Cash on hand as of the end of committee's most recent periodic report; this date appears as cash_on_hand_date

`cash_on_hand_date` : The end of the most recent periodic filing; the date that the cash on hand was reported as of.

`ctype` : The FEC defined committee type.

`candidate_office` : The office of the candidate that this committee supports. Not all committees support candidates.

`candidate_name` : The office of the candidate that this committee supports. Not all committees support candidates.

`candidate_url` : The office of the candidate that this committee supports. Not all committees support candidates.

`display_type` : The office of the candidate that this committee supports. Not all committees support candidates.

`committee_url` : The office of the candidate that this committee supports. Not all committees support candidates.

`political_orientation` : The political orientation of the group, as coded by sunlight algorithms / researchers. This is only added for groups making independent expenditures.



##/outside-spenders/
Return summary information about any outside spending group, including non-committees (which are typically nonprofits, but may include individuals, LLC's, corporations or unions) 

###Parameters


`format` : The format of the returned data. Default is json.

`page` : The page number of results to return. Default is 1. 

`page_size` : The number of page results to return. for json, the default is 100 and the maximum is 100. This parameter is ignored for csv downloads, which return all matching rows, with a limit of 2000 total rows returned.

`ctype` : The FEC committee type. See more about committee types at the top of the page. Note that only some committee types are permitted to make independent expenditures.

`fec_id` : The FEC id of the committee by the independent expenditure. This is a nine-character code that begins with 'C'.

`min_ies` : The minimum amount reported as having been spent by the committee on independent expenditures during the 2014 cycle.

###outside-spenders return values


`fec_id` : The FEC id of the filing committee

`name` : The committee name.

`total_receipts` : Total receipts for this committee ceived during the entire cycle. 

`total_disbursements` : Total disbursements by this committee ceived during the entire cycle

`outstanding_loans` : Total outstanding loans as of the cash_on_hand_date

`ctype` : The FEC defined committee type.

`total_indy_expenditures` : Total independent expenditures made this cycle.

`ie_support_dems` : The total amount of independent expenditures make to support Democratic candidates

`ie_oppose_dems` : The total amount of independent expenditures make to oppose Democratic candidates

`ie_support_reps` : The total amount of independent expenditures make to support Republican candidates

`ie_oppose_reps` : The total amount of independent expenditures make to oppose Republican candidates

`political_orientation` : The political orientation of the group, as coded by sunlight algorithms / researchers. This is only added for groups making independent expenditures.

`political_orientation_verified` : Check this box if the political orientation is correct

`display_type` : Check this box if the political orientation is correct

`committee_url` : Check this box if the political orientation is correct

`get_filtered_ie_url` : Check this box if the political orientation is correct

`display_coh` : Check this box if the political orientation is correct

`display_coh_date` : Check this box if the political orientation is correct

`major_activity` : Check this box if the political orientation is correct


