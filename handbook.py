import os
import unicodedata

# Default handbook content and metadata.
HANDBOOK_TEXT = """
 
   
 Last Issued: 02.04.20251
PAID TIME OFF - U.S. At A&F we realize how hard our associates work and we want to reward you with a PTO plan that 
promotes a healthy work/life balance. This plan provides you with the opportunity to take your 
PTO in a way that is most advantageous to you. 
THIS PACKET APPLIES TO ALL HOURLY STORES AND HOURLY AP ASSOCIATES.
IN THIS PACKET: 
THINGS TO CONSIDER: 
Encourage associates to use all of their PTO and Volunteer time. Plan as a team and 
schedule well in advance so no time goes unused. PTO Balances will reset every year 
for associates in Models 1, 2 and 5, while Models 3 and 4 will accrue and rollover PTO.
Supervisors should set a clear expectations for requesting and approving days off. Do 
your best to accommodate the request or work together to find an alternative solution. 
Be understanding of unplanned events like medical emergencies and personal 
situations. Be sure to communicate these events to your manager(s) as soon as 
possible. 
Allow your team to be fully removed from work on their days off. 
STATE SPECIFIC PTO CHART                                                                                                 2 
U.S. MODELS 1-5                                                                                        3-7       
         
PART TIME ASSOCIATE PAID TIME OFF                                                                           8
VOLUNTEER DAY INFORMATION                                                                                         9
COMP DAY INFORMATION                                                                            10
FREQUENTLY ASKED QUESTIONS                                                                112025
Last Issued: 02.04.20252
PAID TIME OFF - U.S. Utilize the chart below to find out what PTO model your city/state follows.
State PTO Model
Alabama Model 1
Arizona Model 2
Arkansas Model 1
California Model 4
Colorado Model 4
Connecticut Model 2
Delaware Model 1
D.C. Model 5
Florida Model 1
Georgia Model 1
Hawaii Model 1
Idaho Model 1
Illinois Model 3
*Chicago, IL Model 4
Indiana Model 1
Iowa Model 1
Kansas Model 1
Kentucky Model 1
Louisiana Model 1
Maine Model 3
Maryland Model 5
Massachusetts Model 2
Michigan Model 2
Minnesota Model 2
Mississippi Model 1
Missouri Model 1State PTO Model
Montana Model 3
Nebraska Model 3
Nevada Model 1
New Hampshire Model 1
New Jersey Model 2
New Mexico Model 2
New York Model 2
North Carolina Model 1
North Dakota Model 1
Ohio Model 1
Oklahoma Model 1
Oregon Model 2
Pennsylvania Model 1
*Philadelphia County, PA Model 2
*Allegheny County, PA Model 2
Rhode Island Model 2
South Carolina Model 1
Tennessee Model 1
Texas Model 1
Utah Model 1
Vermont Model 2
Virginia Model 1
Washington Model 2
*Seattle, WA Model 5
West Virginia Model 1
Wisconsin Model 1
* Chicago Stores (11822, 11995, 12520, 33564) * Philadelphia County, PA (31724)
* Allegheny County, PA (11508, 11864, 30333, 31277)STATE SPECIFIC PAID TIME OFF CHART
FOR FULL TIME ASSOCIATES
Last Issued: 02.04.20253
PAID TIME OFF - U.S. Full Time associates in Model 1 locations follow a February 1st – January 31st PTO cycle.
 New full time associates who are eligible for PTO will have up to 40 hours available for use 
immediately, depending upon their month of hire. Any additional hours will be available for use 
after 90 days.
 Associates who terminate may be eligible to receive a PTO payout for unused accrued time based 
on the Termination Payout chart below.
 At the start of any new PTO Cycle, an associate will receive 160 PTO hours for use during that 
cycle. Any unused PTO remaining at the end of the cycle will be forfeited. 
Total PTO Hours Available During PTO Cycle *
February
160March
144April
128May
112
June
96July
80August
64September
48
October 
32November
16December
8January
0HELPFUL INFORMATION
*Associates with 4+ years of FT service and reach their 5th year 
anniversary in the PTO calendar will have 40 additional hours available
Payout in hours - PTO used = PTO Termination Payout 
Example: 16 Payout in Hours - 8 PTO hours used = 8 PTO hours paid upon term
16 Payout in Hours - 24 PTO hours used = 0 PTO hours paid upon term Termination Payout for associates with 0-4 years 
Months of work completed 
in benefit yearPayout in Hours * 
(less hours used)
0 - 1 0
2 - 3 16
4 - 5 24
6 - 7 40
8 - 9 56
10 - 11 72Termination Payout for associates with 5 years 
Months of work completed 
in benefit yearPayout in Hours * 
(less hours used)
0 - 1 0
2 - 3 24
4 - 5 40
6 - 7 56
8 - 9 72
10 - 11 88U.S. MODEL 1
*If PTO has been used:
Last Issued: 02.04.20254
PAID TIME OFF - U.S. Full Time associates in Model 2 locations follow a February 1st – January 31st PTO cycle.
HELPFUL INFORMATIONU.S. MODEL 2
 New full time associates who are eligible for PTO will have up to 40 hours available for use 
immediately, depending upon their month of hire. Any additional hours will be available for use 
after 90 days.
 Associates in some states are granted sick days in addition to their PTO. 
 At the start of any new PTO Cycle, an associate will receive 120 PTO hours for use during that 
cycle, and an amount of sick time that corresponds to their work location according to the chart 
below. 
 Any unused PTO and sick time remaining at the end of the cycle will be forfeited. 
 Associates who terminate will be eligible to receive a PTO payout for unused accrued time based 
on the Termination Payout chart below. Associates who terminate will not be paid out unused sick 
time. 
Total PTO Hours Available During PTO Cycle *
February
120March
112April
104May
96
June
88July
72August
56September
40
October 
24November
16December
8January
0
*Associates with 4+ years of FT service and reach their 
5th year anniversary in the PTO calendar will have 40 
additional hours availableSick hours granted at time of hire by location
AZ, CT, MA, NJ, OR, RI, VT,
Philadelphia & Allegheny 
Counties, PA40 hours
NY 56 hours
WA 72 hours
MI, MN, NM 80 hours
NOTE:  Sick hours are in addition to PTO hours
Payout in hours - PTO used = PTO Termination Payout 
Example: 40 Payout in Hours - 24 PTO hours used = 16 PTO hours paid upon term
40 Payout in Hours - 56 PTO hours used = 0 PTO hours paid upon term *If PTO has been used:Termination Payout for associates with 0-4 years
Months of work completed 
in benefit yearPayout in Hours * 
(less hours used)
0 - 1 0
2 - 3 16
4 - 5 24
6 - 7 32
8 - 9 40
10 - 11 48Termination Payout for associates with 5+ years
Months of work completed 
in benefit yearPayout in Hours * 
(less hours used)
0 - 1 0
2 - 3 16
4 - 5 24
6 - 7 40
8 - 9 56
10 - 11 72
Last Issued: 02.04.20255
PAID TIME OFF - U.S. Full Time associates in Model 3 locations follow a February 1st – January 31st PTO cycle.
HELPFUL INFORMATIONU.S. MODEL 3
 New full time associates who are eligible for PTO will have up to 40 hours available for use 
immediately, depending upon their month of hire. 
 Associates can carry over unused PTO hours from one PTO Cycle to the following, up to an overall 
cap equivalent to 1.5 times the applicable “Total PTO hours” amount in the below chart. PTO will 
only accrue when an associate is below the “PTO hours accrual max”.
 Associates who terminate will be paid out unused, accrued PTO time.
Month of hirePTO hours at 
time of hirePTO hours 
accrual max *Total PTO hours 
for benefit year **
February 40 120 160
March 40 104 144
April 40 88 128
May 40 72 112
June 40 56 96
July 40 40 80
August 40 24 64
September 40 8 48
October 32 0 32
November 24 0 24
December 16 0 16
January 8 0 8
*10 hours is accrued each pay period up to the accrual max
**Associates with 4+ years of FT service and reach their 5th year anniversary in 
the PTO calendar will have 40 additional hours available
Last Issued: 02.04.20256
PAID TIME OFF - U.S. Full Time associates in Model 4 locations follow a February 1st – January 31st PTO cycle.
HELPFUL INFORMATIONU.S. MODEL 4
 New full time associates who are eligible for PTO will have up to 40 hours for use immediately, 
depending upon the month of hire. 
 Associates in some locations (as noted below) are granted sick hours in addition to their PTO.
 Associates can carry over unused PTO hours from one PTO Cycle to the following, up to an 
overall cap equivalent to 1.5 times the applicable “Total PTO” amount in the below chart. PTO 
will only accrue when an associate is below the “PTO accrual max”.
 Associates who terminate will be paid out unused, accrued PTO time.
 Associates who terminate will not be paid out unused sick time.
*10 hours is accrued each pay period up to the accrual max
**Associates with 4+ years of FT service and reach their 5th year 
anniversary in the PTO calendar will have 40 additional hours 
availableMonth of 
hirePTO hours 
at time of 
hirePTO hours 
accrual 
max*Total PTO 
hours for 
benefit 
year**
February 40 80 120
March 40 72 112
April 40 64 104
May 40 56 96
June 40 48 88
July 40 32 72
August 40 16 56
September 40 0 40
October 32 0 32
November 24 0 24
December 16 0 16
January 8 0 8Sick hours allotment by location 
CO, CA (statewide) 48 hours
Los Angeles, CA  
(11682)
San Francisco, CA
Santa Monica, CA  
(11697, 33555)72 hours 
San Diego, CA  
(11357, 11646, 21532, 
30132, 30701, 31611)40 hours 
Chicago, IL 
(11822, 11995, 12520, 3356440 hours
NOTE:  Sick days are in addition to PTO days
Last Issued: 02.04.20257
PAID TIME OFF - U.S. Full Time associates in Model 5 locations follow a January 1st – December 31st PTO cycle.
HELPFUL INFORMATIONU.S. MODEL 5
Total PTO Hours Available During PTO Cycle *
January
120February
112March
104April
96
May
88June
72July
56August
40
September 
24October
16November
8December
0
*Associates with 4+ years of FT service and reach their 5th 
year anniversary in the PTO calendar will have 40 additional 
hours availableSick hours allotment by location 
MD 64 hours
Montgomery County, MD  
(30451, 11998)56 hours
Washington D.C.  
(10561)56 hours
NOTE:  Sick hours are in addition to PTO hours
Payout in hours - PTO used = PTO Termination Payout 
Example: 40 Payout in Hours - 24 PTO hours used = 16 PTO hours paid upon term
40 Payout in Hours - 40 PTO hours used = 0 PTO hours paid upon term *If PTO has been used:Termination Payout for associates with 0-4 years
Months of work completed 
in benefit yearPayout in Hours * 
(less hours used)
0 - 1 0
2 - 3 16
4 - 5 24
6 - 7 32
8 - 9 40
10 - 11 48 New full time associates who are eligible for PTO will have up to 40 hours available for use 
immediately, depending upon their month of hire. Any additional hours will be available for use 
after 90 days.
 Associates in some states are granted sick hours in addition to their PTO. 
 Associates who terminate will be eligible to receive a PTO payout for unused accrued time based on 
the Termination Payout chart below.
 Associates who terminate will not be paid out unused sick time. 
 At the start of any new PTO Cycle, an associate will receive 120 PTO hours for use during that 
cycle. Any unused PTO hours remaining at the end of the cycle will be forfeited.
Termination Payout for associates with 5+ years
Months of work completed 
in benefit yearPayout in Hours * 
(less hours used)
0 - 1 0
2 - 3 16
4 - 5 24
6 - 7 40
8 - 9 56
10 - 11 72
Last Issued: 02.04.20258
PAID TIME OFF - U.S. 1 ACCRUAL AMOUNT EXAMPLE : 1:30 = 1 HOUR SICK LEAVE ACCRUED FOR EVERY 30 HOURS WORKED
* This is provided solely to comply with the Paid Leave for All Workers Act (and the Cook County Paid Leave Ordinance, where 
applicable). It is not part of a vacation or general PTO bank.
** Chicago = 11822, 11995, 12520, 33564LOCATIONACCRUAL 
AMOUNT1 ANNUAL USAGE CAPWAITING PERIOD FOR 
USAGE
ARIZONA 1:30 40 hours 90 days from hire
CALIFORNIA 1:30 40 hours 90 days from hire
LOS ANGELES, CA 1:30 48 hours 90 days from hire
SAN DIEGO, CA 1:30 40 hours 90 days from hire
SAN FRANCISCO, CA 1:30 No cap 90 days from hire
SANTA MONICA, CA 1:30 No cap 90 days from hire
COLORADO 1:30 48 hours None
CONNECTICUT 1:30 40 hours 120 days from hire
ILLINOIS (Paid Leave) * 1:40 40 hours 90 days from hire
CHICAGO, IL (PTO) ** 1:35 No cap 90 days from hire
CHICAGO, IL ** 1:35 No cap 30 days from hire
MAINE (PTO) 1:40 40 hours 120 days from hire
MARYLAND 1:30 64 hours 106 days from hire
MONTGOMERY COUNTY, MD 1:30 80 hours 90 days from hire
MASSACHUSETTS 1:30 40 hours 90 days from hire
MICHIGAN 1:30 72 hours None
MINNESOTA 1:30 No cap None
NEVADA (PTO) 1:52 40 hours 90 days from hire
NEW JERSEY 1:30 40 hours 120 days from hire
NEW MEXICO 1:30 64 hours None
NEW YORK 1:30 56 hours None
OREGON 1:30 40 hours 90 days from hire
ALLEGHENY COUNTY, PA 1:35 40 hours 90 days from hire
PHILADELPHIA, PA 1:35 40 hours 90 days from hire
RHODE ISLAND 1:35 40 hours 90 days from hire
WASHINGTON D.C. 1:37 56 hours 90 days from hire
WASHINGTON 1:40 No cap 90 days from hire
SEATTLE, WA 1:30 No cap 90 days from hireSICK LEAVE & PAID TIME OFF
FOR PART TIME, TEMPORARY, AND SEASONAL ASSOCIATES
Last Issued: 02.04.20259
PAID TIME OFF - U.S. A&F VOLUNTEER DAY
A&F believes in supporting the communities where we do business. The Company is continuing the 
Volunteer Day program for management associates in good standing. 
VOLUNTEER DAY  - HOW IT WORKS 
This program is designed to provide eligible associates with the opportunity to take one additional paid 
day off work each year to volunteer with an organization of their choosing!
 
 The program is open to all KHs and above in good standing with the Company
 The Volunteer opportunity must be within the normal daily commute at an organization of your 
choice and the duration of the shift should be equal to the length of a regular workday
 All requests must be made in advance and approved by your supervisor
 Approved requests must be coded as a Volunteer Day in the system
KEY PARTNERS  - A&F GIVES BACK
Our Volunteer Day offers an opportunity for associates to volunteer their time at an organization of their 
choosing.  Below are just a few of the organizations and programs A&F currently supports. Spend your 
volunteer day helping out one of these amazing causes, or reach out to an organization in your area for 
suggestions and opportunities.
Any additional questions can be directed to OneNumber@anfcorp.com  

Last Issued: 02.04.202510
PAID TIME OFF - U.S. All Full Time hourly associates, in the US, will receive 3 Comp Days regardless of start date.
FREQUENTLY ASKED QUESTIONS
HOW DO I REQUEST COMP DAYS?
All comp day requests should be submitted through Time & Labor (T&L); comp days must be used in 8 hour 
increments. Your supervisor will approve submitted days taking into consideration both the needs of the 
business and the associate. Comp days should be submitted as soon as possible to allow for proper planning 
and scheduling.
HOW DO I CODE COMP DAYS?
Comp days should be coded in T&L upon usage, if not submitted prior to taking, using the ‘comp day off’ code.
WILL COMP DAYS IMPACT MY HOURS BUDGET?
Comp days will be processed like all other benefit takes. Any store receiving greater than 120 management 
hours will see their management budget reduced by the number of hours submitted for the comp day. The 
benefit hours, if submitted before the week begins, will be removed the Thursday before the week begins. If not 
submitted until in-week, the hours will not be removed until the Monday after the week is complete.
CAN I CARRY OVER COMP DAYS FOR MYSELF/FULL TIME ASSOCIATES?
Comp days cannot be carried over to the following year. Please ensure that all time is taken by the end of the 
cycle.
WHEN A FULL TIME ASSOCIATE LEAVES THE COMPANY, ARE THEY PAID OUT FOR UNUSED COMP DAYS?
No, comp days are not paid out upon termination.COMP DAYS
Last Issued: 02.04.202511
PAID TIME OFF - U.S. WHEN WILL MY PTO “AVAILABLE FOR USE” AMOUNTS BE VISIBLE IN THE SYSTEM?
“Available for use” amounts should be accurately reflected in the system in real time, depending upon the 
weekly absence calculation process and provided PTO is coded properly. There may be a slight delay when PTO 
time refreshes at the beginning of each PTO cycle.
MODEL 5:   You are eligible to use your available PTO time on January 1st.
MODELS 1-4:   You are eligible to use your available PTO time on February 1st.
IS THERE A WAITING PERIOD FOR NEW HIRES BEFORE THEY ARE ALLOWED TO USE PTO TIME?
No, FT associates are given up to 40 hours to use as of their first day of work.  There is a 90 day waiting period 
to receive the additional hours. 
HOW FAR IN ADVANCE SHOULD PTO REQUESTS BE MADE? 
To maximize the likelihood that the request can be approved, requests for time off should be made as soon as 
possible - e.g. at least two weeks in advance, ideally prior to the monthly management schedule or part time 
associate schedule being made. Talk to your supervisor to allow for proper planning. 
WHEN SHOULD PTO BE ENTERED INTO THE SYSTEM?
As soon as possible! PTO must be coded no later than the end of the pay period to ensure accuracy. Reminder, 
if benefit time is not entered properly this could delay the payment to the associate.
DO I HAVE TO APPROVE EVERY REQUEST I RECEIVE AS A SUPERVISOR?
The business and associate’s needs should be taken into consideration when approving requests. Supervisors 
should set expectations that associates are encouraged to request and take PTO. Not all requests may be 
approved if there is a justifiable business reason. Please use the Store’s Calendar for reference as PTO is 
requested and schedules are created. 
HOW CAN I ACCOMMODATE PTO REQUESTS WHEN I HAVE STAFFING OPPORTUNITIES?
We want to ensure that all managers have the ability to utilize their PTO. Please work within the store first, then 
with other DMs/stores to request borrowed coverage if necessary.
CAN I CARRY OVER PTO FOR MYSELF/MANAGERS?
For the majority of PTO models, time is neither paid out nor carried over between cycles, unless legally required. 
Please ensure that all time is taken by the end of the cycle.
CAN I USE PTO TIME DURING MY LAST TWO WEEKS? 
No, associates may not use PTO time during the last two weeks of employment unless approved by the District 
Manager in advance or if they work in a jursidiction with statutory PTO - e.g. Maine, Nevada, Illinois. 
WHEN A FULL TIME ASSOCIATE LEAVES THE COMPANY, ARE THEY PAID OUT FOR ALL UNUSED PTO 
TIME?
Unused PTO time is paid out based on the informatin in the applicable PTO model for the associate’s work 
location. To the extent applicable legal requirements differ from from the applicable model, we will follow 
applicable law.  
HOW ARE VOLUNTEER DAY REQUESTS CONSIDERED?
Volunteer Day requests are evaluated based on whether the event or organization is in line with our overall 
Company strategy, while also balancing the request with business needs.
DO I NEED TO PROVIDE PROOF THAT I VOLUNTEERED?
No, associates do not need to provide proof from the organization with which they volunteered.   
ANY ADDITIONAL QUESTIONS? 
Contact your HRBP at onenumber@anfcorp.com or the Payroll department at uspayroll@anfcorp.com.FREQUENTLY ASKED QUESTIONS


Abercrombie & Fitch Stores Inc. 
US Store Associate Handbook 

Issued June 2024 


Page│ i  US Store Associate Handbook 
2024 TABLE OF CONTENTS 
Section 1: Introduction  ............................................................................................................................................ 1 
INTRODUCTION  ........................................................................................................................................................ 2 
ABOUT THIS HANDBOOK  ......................................................................................................................................... 2 
EMPLOYMENT AT-WILL  ........................................................................................................................................... 3 
REPORTING PROCEDURES AND COMPANY DIRECTORY  ...................................................................................... 4 
KEY POLICIES & EXPECTATIONS  .............................................................................................................................. 7 
Section 2: Inclusive Workplace Policies  .................................................................................................................. 9 
EQUAL EMPLOYMENT OPPORTUNITY .................................................................................................................. 10 
DISCRIMINATION, HARASSMENT, AND RETALIATION PREVENTION  ................................................................ 10 
COMMITMENT TO DIVERSITY, EQUITY, AND INCLUSION  .................................................................................. 13 
REASONABLE ACCOMMODATIONS FOR DISABILITIES  ....................................................................................... 13 
REASONABLE ACCOMMODATIONS FOR RELIGIOUS BELIEFS  ............................................................................ 14 
IMMIGRATION COMPLIANCE  ................................................................................................................................ 14 
Section 3: Employment Expectations  .................................................................................................................... 15 
ATTENDANCE  .......................................................................................................................................................... 16 
DRESS CODE  ............................................................................................................................................................ 16 
INTIMATE RELATIONSHIPS AT WORK (NON-FRAT) ............................................................................................. 17 
TRANSFERS AND PROMOTIONS  ........................................................................................................................... 19 
EMPLOYMENT/INCOME VERIFICATION  ................................................................................................................... 19 
CONDUCT OUTSIDE OF WORK  .................................................................................................................................. 19 
SOCIAL MEDIA AND THE WORKPLACE  ................................................................................................................. 20 
COMMUNICATING WITH THE MEDIA AND OTHER THIRD PARTIES  .................................................................. 22 
EXTERNAL SPEAKING OPPORTUNITIES  .................................................................................................................... 22 
EXTERNAL SPEAKING SUPPORT  ................................................................................................................................ 23 
MEDIA ENGAGEMENT  ................................................................................................................................................ 24 
PHONE CALLS, TEXTING, AND ELECTRONIC RECORDING DEVICES  ........................................................................ 24 
TECHNOLOGY SYSTEMS  ......................................................................................................................................... 25 
COMPANY SURVEILLANCE  ......................................................................................................................................... 26 
PERSONNEL RECORDS  ................................................................................................................................................ 26 
RELOCATION  ........................................................................................................................................................... 27 
GOVERNMENT REPRESENTATIVES  ........................................................................................................................... 27 
EMPLOYMENT OF MINORS  ................................................................................................................................... 27 
FITTING ROOM PROCEDURES  ................................................................................................................................... 27 
ASSET PROTECTION STANDARDS  ............................................................................................................................. 28 
Section 4: EMPLOYMENT Standards  ..................................................................................................................... 30 
 
Page│ ii  US Store Associate Handbook 
2024 
 GENERAL STANDARDS OF BUSINESS CONDUCT  .................................................. ...................................................  31 
CODE OF BUSINESS CONDUCT & ETHICS  .................................................. ................................................... ........ 32 
CONFLICT OF INTEREST  .................................................. ................................................... ......................................... 32 
CONFIDENTIAL INFORMATION  .................................................. ................................................... ........................ 33 
COMPANY INVESTIGATIONS  .................................................. ................................................... ............................ 35 
POLITICAL CONTRIBUTIONS  .................................................. ................................................... ............................. 35 
SOLICITATION AND DISTRIBUTION  .................................................. ................................................... .................. 35 
OPERATING A VEHICLE ON COMPANY BUSINESS  .................................................. ............................................. 36 
POLICY ON UNION  .................................................. ................................................... ................................................. 36  
COMPANY PROPERTY  .................................................. ................................................... ....................................... 36 
SECTION 5: HEALTH AND SAFETY....................... ................................................... ........................................... 37  
WORKPLACE SAFETY  .................................................. ................................................... ............................................. 38 
WEAPONS-FREE WORKPLACE  .................................................. ................................................... .............................. 40 
SEARCHES AND INSPECTIONS  .................................................. ................................................... .............................. 40 
DRUG-FREE WORKPLACE  .................................................. ................................................... ...................................... 41 
NO SMOKING  .................................................. ................................................... ................................................... ...... 42 
Section 6: The Workday and Compensation  .................................................. ................................................... .... 43 
EMPLOYMENT STATUS CLASSIFICATION  .................................................. ................................................... ............ 44 
WORK HOURS AND SCHEDULES  .................................................. ................................................... ...................... 44   
TIMEKEEPING FOR NON-EXEMPT (HOURLY) ASSOCIATES  .................................................. ............................... 45 
MEAL AND REST BREAKS  .................................................. ................................................... .................................. 46 
BREAKS FOR NURSING/PUMPING MOTHERS  .................................................. ...................................................  46 
OVERTIME FOR NON-EXEMPT ASSOCIATES  .................................................. ................................................... ... 46 
PAYROLL  .................................................. ................................................... ................................................... .......... 47 
REVIEW OF PAY STUBS  .................................................. ................................................... ..................................... 47 
WAGE DEDUCTION ACKNOWLEDGEMENT  .................................................. ................................................... ..... 48 
EXPENSE AND TRAVEL REIMBURSEMENT  .................................................. ................................................... ...... 48 
PERSONAL DEVICE REIMBURSEMENT  .................................................. ................................................... ............. 49 
INCLEMENT WEATHER  .................................................. ................................................... .......................................... 49 
Section 7: Time Away From Work  .................................................. ................................................... .................... 50 
HOLIDAYS  .................................................. ................................................... ................................................... ........ 51 
PAID TIME OFF FOR FULL-TIME ASSOCIATES  .................................................. ................................................... ..... 51 
PAID SICK AND SAFE LEAVE POLICY (PSSL)  .................................................. ................................................... ..... 52 
LEAVES OF ABSENCE  .................................................. ................................................... ......................................... 52 
DISCRETIONARY LEAVES OF ABSENCE  .................................................. ................................................... ............ 52 
MILITARY LEAVE  .................................................. ................................................... ................................................ 53 
 
Page│ iii  US Store Associate Handbook 
2024 
 BEREAVEMENT LEAVE  .................................................. ................................................... ........................................... 53 
CRIME VICTIM LEAVE & DOMESTIC / SEXUAL VIOLENCE LEA VE  .................................................. ..................... 53 
VOTING LEAVE  .................................................. ................................................... ................................................... .... 54 
JURY DUTY LEAVE  .................................................. ................................................... .................................................. 54 
Section 8: INSURANCE AND OTHER Benefits  .................................................. ................................................... ... 55 
OVERVIEW OF BENEFITS  .................................................. ................................................... ................................... 56 
ASSOCIATE DISCOUNTS AND PERSONAL PURCHASES  .................................................. ...................................... 56 
BRAND LOYALTY PROGRAM  .................................................. ................................................... ............................ 58 
Section 9: End of Employment  .................................................. ................................................... ......................... 59 
END OF EMPLOYMENT GUIDELINES  .................................................. ................................................... ................ 60 
HANDBOOK ACKNOWLEDGMENT  .................................................. ................................................... .................... 61 
 
 
Page│ 1  US Store Associate Handbook 
2024 
  
 
 
Section 1: 
Introduction 
Section One: Introduction 
Page│ 2  US Store Associate Handbook 
2024 
 INTRODUCTION 
Welcome to Abercrombie & Fitch Co.! Abercrombie & F itch Co. is a leading specialty retailer comprised of our brands 
including Abercrombie & Fitch, Abercrombie kids, Ho llister, Gilly Hicks, and Social Tourist. All US st ores are operated by 
Abercrombie & Fitch Stores Inc., which is your dire ct employer. In this Handbook, “Abercrombie” and “t he Company” refers 
generally to all of our store brands operated by Ab ercrombie & Fitch Stores Inc., and particularly to the brand store in which 
you will be working.  
The Company’s most important asset is its associate s. We constantly work to create the most favorable environment 
possible – one where you can grow and excel. We are  committed to providing a collaborative and inclusi ve work 
environment that encourages growth and development and rewards achievements. This Handbook explains ma ny of the 
programs and benefits that make this environment po ssible. We are proud of our programs, and we believ e they are among 
the finest available.  
As an associate of the Company, we expect you to wo rk hard, be honest, and get the job done. We expect  you to learn and 
broaden your experience. We strive for openness and  trust, and we encourage a spirit of cooperation an d loyalty.  
If you are reading this because you just joined the  Company, we’re happy to have you here. We hope you  will be proud of 
your position and enthusiastically contribute to ou r goals. We look forward to working with you to max imize your 
contribution to our mutual success. If you have que stions or need further information, please do not h esitate to reach out. 
Again, welcome! We are glad to have you with us! 
  
Section One: Introduction 
Page│ 3  US Store Associate Handbook 
2024 
 ABOUT THIS HANDBOOK 
This Handbook is designed to provide you with gener al information regarding your employment with the C ompany. Below 
are important housekeeping provisions to familiariz e yourself with before reading the remaining polici es in this Handbook.  
Employment at the Company is contingent upon your c ompliance with our policies and procedures, includi ng those 
described in this Handbook. This Handbook supersede s all previously issued Handbooks and inconsistent written or verbal 
policies or statements made or issued before this H andbook. However, to the extent the terms of this H andbook contradict 
the terms of an applicable written employment contr act, business code of conduct, written insurance po licy, or Handbook 
State Supplement, the terms of those documents cont rol.  
On occasion, the law or the Company’s policies will  change. The Company will comply with all changes i n the law as they 
take effect, but those changes may not appear in th e Handbook until the next edition is published. To the extent this 
Handbook conflicts with the law, the applicable law  will be followed. 
Please note the Company may amend, supplement, or r escind the policies described in this Handbook or m odify or deviate 
from the policies at any time. Each benefit plan or  program is subject to the terms of the specific be nefit plan documents. 
The Company has discretion to determine benefit eli gibility and interpret the terms of each plan or pr ogram. The Company 
may likewise amend, modify, or terminate any benefi t plans or programs at any time, subject to applica ble law. 
Because you are responsible for complying with the policies described in this Handbook, it is importan t that you ask 
questions if you have them. When you have questions , please contact the designated team member, as ide ntified in the 
Policy that follows. 
EMPLOYMENT AT-WILL  
YOU ARE AN “AT-WILL” ASSOCIATE. Meaning, both you a nd/or the Company may terminate the employment rela tionship 
at any time, for any lawful reason, or for no reaso n at all, with or without cause or notice. The poli cies in this Handbook are 
not intended to, and do not, create a contract. 
Unless modified by written agreement, that is signe d by both you and a Vice President of Human Resourc es, no 
representative of the Company may enter into an agr eement for employment or make an agreement contrary  to the 
provisions of this Handbook.  
 
Section One: Introduction 
Page│ 4  US Store Associate Handbook 
2024 
 REPORTING PROCEDURES AND COMPANY DIRECTORY 
Throughout this Handbook, you are directed to vario us partners or teams. Their contact information is below for ease of 
reference. In addition, if you have concerns, sugge stions, or complaints relating to your employment, please utilize the 
reporting procedures below.  
Reporting Procedures: 
General Workplace Questions or Concerns. If you have general workplace questions or concerns , such as questions about 
work assignments or scheduling, trouble with a co-w orker or manager, or concerns about your own or som eone else’s 
health, safety, or adherence to Company policies, w e encourage you to contact the following people in this order: your Store 
Manager, General Manager, District Manager, Regiona l Manager, and Human Resources.  
Reporting Discrimination, Harassment, or Retaliatio n. For issues of perceived discrimination, harassment,  or retaliation, 
please follow the reporting procedure in the Discri mination, Harassment, and Retaliation Prevention Po licy. 
Reporting Unlawful or Unethical Conduct . If you believe unlawful or unethical conduct occu rred, you are expected to report 
related information to your manager, Human Resource s, the Chief Ethics and Compliance Officer (CECO), the Legal 
Department, or the Ethics Reporting Website or Hotl ine.  
Reporting Concerns about Your Direct Supervisor. If you have concerns about your direct supervisor, please report this 
information directly to Human Resources, the Chief Ethics and Compliance Officer (CECO), the Legal Dep artment, or the 
Ethics Reporting Website or Hotline. 
Reporting Complaints Regarding Compensation, Hours Worked, and Meal/Rest Breaks. Promptly bring general questions 
regarding these policies to the attention of your S tore Manager or General Manager. If you believe tha t a violation of these 
policies occurred, you must promptly report the con cern to the One Number.  
Questions About or Requesting an Accommodation. To request an accommodation or for issues related t o an 
accommodation, please follow the reporting procedur e in the Reasonable Accommodations for Disabilities  Policy and/or 
the Reasonable Accommodations for Religious Beliefs  Policy. 
Questions About or Requesting a Leave of Absence. T o request a leave of absence or for questions regarding leaves of 
absence, contact the Benefits Hotline. To request a  family and medical leave of absence under the FMLA , contact Sedgwick 
CMS, our third-party disability and leave program a dministrator (refer to the Company Director y below). 
Questions About Payroll. For questions regarding payroll, please contact the  following people in this order: your manager, 
District Manager, the Payroll Department, or call t he One Number (refer to the Company Directory below ). 
Questions About Benefits.  For questions about associate benefits, please con tact the Benefits Hotline (refer to the Company 
Directory below). 
 
 
 
 
Section One: Introduction 
Page│ 5  US Store Associate Handbook 
2024 
 Company Directory: 
Managers  
Assistant Manager, Store Manager, 
General Manager, District Manager, 
Regional Manager The managers in your reporting chain depend on your  store location. 
Please refer to the break room at your store locati on for manager contact 
information. 
Human Resources  
Human Resources  866 -367 -1892  
Additional Reporting Avenues  
The One Number  866 -367 -1892  
onenumber@anfcorp.com 
Ethics Reporting  800.965.1892  
www.abercrombie-ethics.com 
Chief Ethics and Compliance Officer: CECO@anfcorp.c om 
CECO  CECO@anfcorp.com  
Asset Protection  
Asset Protection (Health & Safety)  From a store phone: x 7322  
800-965-1892 
800-976-1892 
Public Relations  
Corporate Communications &  
Public Relations Department 614 -283 -6192  
public_relations@anfcorp.com 
Payroll  
Payroll Department  uspayroll@anfcorp.com  
Benefits  
Benefits Department  associatebenefits@anfcorp.com  
Benefits Hotline  877 -263 -4968 or associatebenefits@anfcorp.com  
Family and Medical Leave (FMLA) 
Administrator Sedgwick CMS: 866 -576 -9368  
Short Term Disability  Sedgwick CMS: 866 -576 -9368  
Healthcare and Dental / PPO Network of 
Providers 
Medical Group #:  
0839231-012-00001 
Dental Group #:  
0839231-022-00001 Aetna: 855 -222 -2096  
www.aetna.com 
Vision  EyeMed: 866 -800 -5457  
www.eyemed.com 
401(k) Savings and Retirement Plans  Fidelity Customer Service: 800 -835 -5097  
netbenefits.fidelity.com 
Risk Management Department  
(Workers’ Compensation) 614 -765 -INJR  
risk@anfcorp.com 
Employment Verifications (The Work 
Number) 800 -367 -5690 or 800 -367 -2884  
www.theworknumber.com 
www.theworknumber.com/verifier  
Associate Assistance Program (AAP)  www.mylifevalues.com  
(Username: Abercrombie, Password: aap)  
 
Section One: Introduction 
Page│ 6  US Store Associate Handbook 
2024 
 Customer Service  
Customer  Service Department  1-888 -856 -4480  
customer_service@anfcorp.com 
Home Office  
Mailing Address Abercrombie & Fitch  
P.O. Box 182168 
Columbus, OH 43218-2168 
Main Phone  Number  800 -666 -2595  
Select: 
   1 = FT Associates 
   2 = PT Associates 
Select : 
   1 = Voicemail User Access 
   2 = Home Office Departments 
OR 
614-283-6500 
   1 = Enter extension or associate’s name 
   2 = New Order 
   3 = Customer Service 
   4 = Distribution Center  
   5 = Human Resources    
   6 = Investor Relations 
   0 = Operator  
 
  
Section One: Introduction 
Page│ 7  US Store Associate Handbook 
2024 
 KEY POLICIES & EXPECTATIONS 
You are responsible for understanding and complying  with all policies described in this Handbook. The following, however, 
are brief summaries of some  of the critical policies found later in this Handb ook that you should be especially aware of 
during your employment. If you violate one of these  policies, the Company may discipline you up to and  including 
termination.  
1.  Discrimination, Harassment, and Retaliation Prevent ion  
A&F offers equal employment opportunity to all Asso ciates and potential Associates. It is our policy i n all employment 
matters to ensure that Associates and potential Ass ociates are evaluated based on qualifications and a bility, without regard 
to sex, age, race, color, religion or belief, ethni c or national origin, sexual orientation, gender re assignment, marital or civil 
partner status, pregnancy or maternity, or disabili ty, or any other category protected by law. The Com pany is also committed 
to providing a working environment free from harass ment and bullying and ensuring all associates are t reated, and treat 
others, with dignity and respect.  
2.  Confidentiality  
You are expected to maintain appropriate confidenti ality regarding sensitive conversations and busines s information. This 
includes, for example, any conversation related to an internal investigation, any conversation with Hu man Resources in which 
sensitive topics are discussed, personal or sensiti ve information about other associates that you may gain through any 
means, information about future staffing changes, a nd anything else that could be reasonably viewed as  sensitive or 
confidential by the Company or other associates. 
3.  Retaliation  
The Company prohibits retaliation, including for ma king any good-faith complaint pursuant to the polic ies outlined in this 
Handbook, for encouraging someone else to make a re port or complaint, for participating in a Company i nvestigation, for 
opposing practices or conduct prohibited by policie s in this Handbook, or for testifying or assisting with a related legal 
proceeding. If you believe you are experiencing ret aliation, or you witness retaliation against someon e else, please follow 
the reporting procedure in the Discrimination, Hara ssment, and Retaliation Prevention Policy. 
4.  Intimate Relationships  
The Company strongly believes that a work environme nt where associates maintain clear boundaries betwe en personal and 
business interactions is necessary for effective bu siness operations. Romantic and social relationship s between a manager 
and subordinate can compromise the manager’s positi on of trust and authority,  and impair the manager’ s ability to manage 
without bias or perceived bias. Because of the resu lting inherent problems, romantic and social relati onships between a 
manager or supervisor and any subordinate—with whom  they directly or indirectly supervise, assign work , evaluate, or 
influence employment or compensation decisions—are strictly prohibited. While an intimate relationship  between two 
associates at the same-level is not prohibited, suc h relationships may create workplace problems. Asso ciates involved in an 
intimate personal relationship are expected to cond uct themselves in an appropriate workplace manner t hat does not 
interfere with others, with overall productivity, o r put other associates or our customers in an uncom fortable position.  
5.  Attendance  
To effectively operate our business, the Company ex pects and requires that you regularly report to wor k. Regular attendance 
is an essential requirement for all positions and f ailure to follow the Attendance Policy, including r ules for reporting tardiness, 
absence, or early departure, and requesting time of f, will result in disciplinary action, up to and in cluding termination. 
Section One: Introduction 
Page│ 8  US Store Associate Handbook 
2024 
 6.  Drug & Smoke Free Workplace  
Unless specifically permitted under the full Policy , when reporting to work and while on the job, the following conduct is 
strictly prohibited: use, possession, transportatio n, manufacture, sale, dispensation, or other distri bution of an illegal or 
controlled substance or drug paraphernalia; use, po ssession, sale, dispensation, or other distribution  of alcohol; and 
performing work for the Company while impaired by o r under the influence of illegal drugs, controlled substances, or alcohol. 
Smoking is not permitted anywhere on Company premis es. This includes the use of chewing tobacco  and electronic 
cigarettes/vapor devices . Smoking is only permitted in designated mall area s or outside of the store. 
7.  Social Media  
Associates are ambassadors for our brands and the C ompany in everything we do, and posting on social m edia can have an 
impact on the Company’s reputation and business. Pl ease be mindful that you are always responsible for  what you publish 
on social media, even when published outside of wor k. Associates’ use of social media should not viola te the law, adversely 
affect the associate’s job performance or ability t o do their job or to function effectively in the wo rkplace, or violate A&F’s 
policies on discrimination and harassment. 
8.  Clean & Safe Workplace 
Every associate must do their part in maintaining a  clean, safe workplace. We also need to be able to safely move about our 
workplaces without risk of injury. If you witness s omeone being unsafe or if you get injured on the jo b, no matter how minor 
the injury, you have a duty to report it immediatel y to your manager. All associates also are required  to follow the minor 
safety rules, specifically the prohibition against any use of a trash compactor or freight elevator, a s required by relevant laws 
and Company policy. 
9.  True & Accurate Records 
We all create records while working for A&F. Record s can be anything from timesheets, to recording mea l and rest breaks, 
to product inventory to travel expenses—even the ca sh in one of our registers is a type of record. Wha tever your role in 
recording or reporting information for A&F, it is y our duty to make sure that this information is accu rate and complete and 
that you follow all of the Company’s internal accou nting policies and controls. Do not lie! 
10.  Speak Up!  
You are encouraged to raise issues, concerns, and q uestions as soon as possible so that they may be in vestigated and resolved 
quickly. And if you think something is wrong – Spea k Up! When you need guidance or to make a report, y ou may contact 
your manager, HR (directly or through Ethics Point) , or the CECO (directly or through Ethics Point). P lease reference the 
Company Directory above for contact information.  
 
 
  
 
 
Section 2: 
Inclusive Workplace Policies 
Section Two: Inclusive Workplace Policies 
Page│ 10  US Store Associate Handbook 
2024 
 EQUAL EMPLOYMENT OPPORTUNITY 
The Company strives to provide a respectful and inc lusive work environment for all associates. In keep ing with this goal, we 
provide equal employment opportunity to all individ uals without consideration of any status or charact eristic protected by 
applicable state and federal law. Protected charact eristics include, for example, race (including a na tural, protective, or 
cultural hairstyle, or hair texture), color, religi on, national origin or ancestry, citizenship, ethni city, disability, pregnancy 
(including childbirth and conditions related to pre gnancy), sex, gender, sexual orientation, gender id entity or expression, 
age, military/veteran status, or genetic informatio n (collectively, these are called “Protected Charac teristics” or referred to 
as a “Protected Characteristic” throughout this Han dbook).  
The Company prohibits discrimination and harassment  based on any person’s Protected Characteristic. Th e Company also 
prohibit s retaliation for raising good-faith concerns relate d to the Company’s commitment to an equal employmen t 
opportunity workplace. 
This Policy applies to all terms and conditions of employment, including recruitment, hiring, classifi cation, compensation, 
promotion, transfer, leaves of absence, and termina tion. If you learn of, observe, or have reason to b e concerned about 
conduct in violation of this Policy, you must immed iately disclose it to Human Resources.  
DISCRIMINATION, HARASSMENT, AND RETALIATION PREVENT ION 
Our Commitment to an Inclusive Workplace. We are committed to a work environment that respect s and includes all 
associates.  
Inappropriate workplace behavior and unlawful condu ct creates a work environment that is inconsistent with this 
commitment. We foster a work environment that is fr ee from all forms of discrimination, harassment, an d retaliation based 
on any Protected Characteristic. We also prohibit d iscrimination and harassment based on a person’s pe rceived Protected 
Characteristic or association with a person’s Prote cted Characteristic. Simply put, discrimination, ha rassment, and 
retaliation are inconsistent with the Company’s val ues and will not be tolerated.  
When this Policy Applies. This  Policy applies not only in the workplace, but whene ver and wherever you are representing 
or conducting Company business and when you are ass ociating with co-workers. This includes when you ar e on Company 
property, traveling on Company business, associatin g with co-workers outside of work, or at an event s ponsored or 
authorized by the Company. This Policy applies to i n-person conduct, email, text message, social media , and other 
communications, oral or written. This Policy applie s to associates, applicants ,  and third parties with whom the Company 
does business. 
Discrimination. For purposes of this Policy, discrimination refers to differential treatment or making an employment 
decision based on, or because of, an individual’s P rotected Characteristic. 
Harassment. For purposes of this Policy, harassment is any cond uct that involves unwelcome verbal, non-verbal, or physical 
conduct that degrades or shows hostility or aversio n toward an individual because of their Protected C ategory and creates 
an intimidating, hostile, or offensive work environ ment or unreasonably interferes with an individual’ s work performance. 
Examples of this type of prohibited harassment incl ude, but are not limited to: 
• Using racial or religious epithets, slurs, or physi cal gestures; 
• Mocking, ridiculing, or mimicking someone’s culture , accent, appearance, or customs; and/or 
• Making jokes, pranks, or behaving in a threatening,  intimidating, or hostile way because of someone’s protected 
status. 
Section Two: Inclusive Workplace Policies 
Page│ 11  US Store Associate Handbook 
2024 
 Sexual Harassment. For purposes of this Policy, sexual harassment is a  type of harassment that specifically refers to 
unwelcome sexual advances, requests for sexual favo rs, and other unwelcome verbal, non-verbal, or phys ical conduct of a 
sexual nature when: 
• Submitting to the conduct is explicitly or implicit ly made a term or condition of employment; 
• Submitting to or rejecting the conduct is used as t he basis for an employment decision; or 
• The conduct is severe or pervasive enough that it u nreasonably interferes with an associate’s work per formance or 
creates an intimidating, hostile, or offensive work ing environment, even if the person making the repo rt is not the 
intended target of the conduct. 
Sexual harassment includes harassment based on sex,  sexual orientation, gender identity, gender expres sion, and the status 
of being transgender or gender non-conforming. It c an occur between males and females, persons of the same sex, and 
involve individuals who are transgender or gender n on-conforming. An act may be sexual harassment rega rdless of the 
sexual desire, sexual orientation, or intent of the  harasser. Sexual harassment is a form of sex discr imination and is unlawful. 
Examples of prohibited sexual harassment include, b ut are not limited to: 
• Physical acts of a sexual nature such as touching, pinching, kissing, grabbing, tickling, or brushing against an 
associate’s body; 
• Unwelcomed and/or inappropriate commentary about an  individual’s body or appearance; 
• Sexual crimes (including rape, sexual battery, mole station, or attempts to commit these assaults); 
• Hostile actions against an individual because of th eir sex, sexual orientation, gender identity, or st atus of being 
transgender; 
• Subtle or obvious pressure for unwanted sexual adva nces or requests for sexual activities; 
• Sexual jokes and innuendo; 
• Verbal abuse of a sexual nature; 
• Sexually-oriented gestures, noises, remarks, jokes,  or comments about a person’s sexuality or sexual e xperience; 
• Insulting or obscene sexual comments or gestures; 
• Displaying or circulating sexually suggestive objec ts, pictures, or messages; and/or 
• Any other physical, verbal, or visual conduct of a sexual nature that would reasonably be considered o ffensive or 
harassing. 
Reporting Procedures . If for any reason you do not feel comfortable com municating directly with the person who has said 
or done something that you find offensive, or if yo u have done so but the offensive words or actions c ontinue, submit your 
concern according to the following reporting proced ures. This procedure ensures our workplace remains respectful, 
professional, and free from prohibited conduct as d escribed in this Policy. If possible, document in w riting the date, time, 
place, witnesses, what was said or done, and the su rrounding circumstances. Submit your concern to the  following people: 
your manager, the next level of management ( e.g ., if your immediate manager is a Store Manager, yo ur next level manager 
is a District Manager), Human Resources via the One  Number, an Officer of the Company, the Ethics Hotl ine or the Chief 
Ethics & Compliance Officer (CECO). 
When making a report or complaint under this Policy , you may provide your name or remain anonymous. An onymous 
complaints, however, are often more difficult to in vestigate. With that in mind, we strongly recommend  that anyone who 
makes an anonymous complaint provide as much specif ic information as possible. 
Section Two: Inclusive Workplace Policies 
Page│ 12  US Store Associate Handbook 
2024 
 If you are a manager and you learn of an associate’ s concern about conduct in violation of this Policy , whether informally or 
through a formal complaint, you must immediately re port it to Human Resources. 
Investigative & Remedial Action . When you disclose conduct you believe violates th is Policy, the Company will take the 
matter seriously and conduct a prompt, fair, thorou gh, and timely investigation into your concerns. Yo u and everyone in the 
investigation will be treated with respect. The Com pany will typically interview the complainant and t he accused, conduct 
further interviews as necessary, and review relevan t documents and information. We strive to maintain confidentiality 
throughout the investigative process to the extent practicable. However, our duty to investigate and t ake corrective action 
may require the disclosure of information, and ther efore, confidentiality cannot be guaranteed. We wil l, of course, only 
disclose what is necessary to facilitate a prompt, fair, and thorough investigation. Upon completion o f the investigation, we 
will evaluate the information gathered and take rem edial, corrective, and/or disciplinary action as ne cessary. The Company 
may, in its discretion, require confidentiality fro m associates during the investigative process. In t hose circumstances, failure 
to maintain confidentiality may result in disciplin e. The intent of this Policy is to protect the inte grity of workplace 
investigations to help ensure a fair outcome for an y involved parties. It is not intended to—and shoul d not be interpreted 
to—restrict your rights under any federal, state, o r local laws, including without limitation the Nati onal Labor Relations Act. 
No Retaliation . Retaliation is any type of action that adversely af fects the terms of employment or the working enviro nment 
because the individual made a complaint pursuant to  this Policy, encouraged someone to make a report o r complaint, 
participated in a Company investigation, opposed pr actices or conduct prohibited by this Policy, or te stified or assisted with 
a related legal proceeding. The Company will not re taliate against you for reporting concerns in good faith or for participating 
in subsequent investigations. “Good faith” as refer red to throughout this Handbook means that you make  your report 
sincerely and honestly believe that a violation occ urred. 
Policy Violation Consequences . If the Company determines that you have engaged in conduct that violates this Policy, you 
will be disciplined. Discipline may include verbal or written warning, suspension, or termination. You  may also be held 
personally liable for engaging in unlawful discrimi nation, harassment, or retaliation. Please note tha t conduct may violate 
this Policy and our expectations regarding workplac e behavior even if it is not considered unlawful.  
COMMITMENT TO DIVERSITY, EQUITY, AND INCLUSION  
At A&F, diversity, equity, and inclusion is woven i nto everything we do. We believe that fostering, cu ltivating, and preserving 
a culture of inclusion and diversity in all forms m ake us stronger. 
Our investments in inclusion, diversity, and belong ing at A&F are intentionally centered around embrac ing our associates’ 
differences and ensuring representation regardless of any Protected Characteristic or attributes that make our associates 
unique. The collective sum of individual difference s, life experiences, self-expression, unique capabi lities and talent that our 
associates invest in their work represents not only  our culture, but our reputation and company’s achi evement as well. 
We are committed to the ongoing development of educ ation, experiences, processes, and programs to ensu re that our 
associates, customers, and organizational partners are included, respected, supported, and empowered -  positively 
impacting the global community. 
Our inclusion and diversity initiatives are applica ble—but not limited—to our practices and policies o n talent recruitment 
and selection, training and development, promotions , transfers, compensation and benefits. 
While we believe everyone is on their own journey o f being and becoming, all associates are responsibl e for treating others 
with dignity, respect, and inclusivity, always, dur ing work, at work functions on or offsite, Company- sponsored and 
participative events. We expect these standards to be upheld outside of work in any form of communicat ion and actions 
(inclusive of social media platforms). All associat es are required to complete any trainings related t o this space. 
Section Two: Inclusive Workplace Policies 
Page│ 13  US Store Associate Handbook 
2024 
 Any associate found to have exhibited any inappropr iate behavior or conduct – that otherwise violates Company policy – 
against others, undermines inclusion and diversity principles may be subject to disciplinary action, u p to and including 
termination. We strongly encourage associates who e xperience, witness, or become aware of discriminato ry, harassing, 
and/or retaliatory conduct—or conduct that is incon sistent with our inclusion and diversity principles  to seek assistance 
from a supervisor, HR representative, or submit a r eport to A&F Ethics and Compliance Hotline. Please reference the 
Discrimination, Harassment, and Retaliation Prevent ion Policy. 
REASONABLE ACCOMMODATIONS FOR DISABILITIES 
Commitment to Reasonable Accommodations. The Company is committed to providing reasonable ac commodations to 
qualified individuals with disabilities—to perform the essential functions of their job— provided ther e is no undue hardship 
on the Company’s operations and provided the accomm odation does not pose a direct threat to the health  or safety of 
those in the workplace. The goal of reasonable acco mmodations is to enable people with disabilities to  overcome work-
related barriers. An individual may be considered d isabled if they have an impairment that substantial ly limits one or more 
of their major life activities, a record or history  of such an impairment, or is perceived as having s uch an impairment. The 
definition of disability includes pregnant associat es impacted by medical conditions related to pregna ncy or childbirth. 
Accommodation Requests & Process. If a disability-related limitation impacts your abi lity to perform your job duties, 
participate in training, or otherwise access benefi ts of employment, you should contact Human Resource s to request a 
reasonable accommodation. Reasonable accommodations  require an interactive process, and generally, it is the associate’s 
responsibility to initiate the process by informing  the Company they need an accommodation. During the  interactive 
process, Human Resources will partner with you, man agement, healthcare provider(s), and others, as app ropriate, to assess 
whether a reasonable accommodation is possible. Com munication with healthcare professionals may be nec essary to verify 
the existence of a disability or work restrictions,  to identify potential reasonable accommodations, a nd/or to assess if an 
accommodation would cause undue hardship. The Compa ny will treat medical information as confidential. All requests for 
an accommodation are addressed on a case-by-case ba sis. 
Additional Information Applicable to a Leave of Abs ence as an Accommodation . If your medical condition necessitates 
time away from work, including a leave of absence u nder the Family and Medical Leave Act (FMLA), state /local leave laws, 
or the Company’s Discretionary Leave of Absence Pol icy, please review the applicable leave of absence policies for additional 
information. A discretionary leave of absence is a type of accommodation that may be available to asso ciates who do not 
meet eligibility requirements under the FMLA, state /local leave laws, or other leave policies. The dur ation of a leave of 
absence is dependent on the circumstances, such as the nature and duration of the request for leave an d the business 
impact of the absence from work. If you request an extension of a leave, the Company may require addit ional 
documentation from your healthcare provider certify ing the need for continued leave due to a disabilit y. 
Leave as an accommodation is unpaid, unless availab le paid leave is applied or you are eligible for sh ort-term disability (STD), 
long-term disability (LTD), workers’ compensation, or pay continuation under a state or local law. STD  pay, LTD pay, workers’ 
compensation, and/or other state or local paid leav e benefits will not exceed 100% of your pay during the period in which 
you are receiving benefits. 
Additional Information. The Company strictly prohibits discrimination and r etaliation against qualified individuals with 
disabilities who, with or without reasonable accomm odation, can perform the essential functions of the ir job. If you believe 
you were retaliated against, you should promptly co ntact Human Resources. 
Section Two: Inclusive Workplace Policies 
Page│ 14  US Store Associate Handbook 
2024 
 REASONABLE ACCOMMODATIONS FOR RELIGIOUS BELIEFS 
The Company recognizes and respects diversity of re ligious beliefs, practices, and observances. When w ork obligations 
conflict with religious beliefs, the Company is com mitted to exploring whether the Company may provide  an 
accommodation that will eliminate the conflict, whi le preserving your ability to fully perform the ess ential functions of your 
job. Accommodation must be reasonable and may not i mpose an undue hardship on the Company.  
If you need a religious accommodation, discuss your  request with Human Resources. The Company will not  retaliate against 
you for requesting an accommodation under this Poli cy. If you believe you were retaliated against, pro mptly notify Human 
Resources.  
IMMIGRATION COMPLIANCE 
The Company only employs individuals authorized to work in the United States, in compliance with the I mmigration Reform 
and Control Act. The Company is required to verify the identity and employment authorization of all ne wly hired associates, 
which is achieved by requiring new hires to complet e the I-9 form and reviewing and verifying the supp orting documentation 
provided in person. In some circumstances, the Comp any may require re-verification of authorization to  work in the United 
States. Providing a false statement and/or using a false or fraudulent document in connection with the  completion of an I-
9 will result in termination and, pursuant to feder al law, may also result in imprisonment and/or fine s.  
 
  
 
 
Section 3: 
Employment Expectations  
  
Section Three: Employment Expectations 
Page│ 16  US Store Associate Handbook 
2024 
 ATTENDANCE 
The Company depends on associates to attend work as  scheduled. Dependability, attendance, and punctual ity are critical 
to our mutual success and are essential functions o f all positions. You are expected to work on all sc heduled workdays 
and during all scheduled work hours, and to report to work on time. Absenteeism and tardiness affect b oth your 
productivity and business results. As such, violati ons of this Policy may result in disciplinary actio n—imposed at the 
Company’s discretion based on the violation and rel evant circumstances—up to and including termination . 
Running late to work call-in procedure. If you are running late to work, you must notify yo ur manager by phone that you 
are running late as far in advance as possible so y our manager can plan accordingly. This notification  does not excuse the 
tardiness, but when determining whether to issue di scipline, your manager will consider your efforts t o inform them that 
you were running late, the amount of advance notice  you provided, and underlying reason for your tardi ness.  
Absence call-in procedure: Depending on the reason you are unable to come to w ork, you must: 
• Follow the procedures in the Paid Time Off (PTO) Pa cket;  
• Follow the procedures in the Family Medical Leave A ct (FMLA) Policy if you are eligible for FMLA and t he reason 
for the absence qualifies for FMLA time off; 
• Follow the procedures in the applicable Handbook po licy (or Handbook State Supplement) if the reason f or the 
absence is related to jury duty, voting, bereavemen t leave, family leave, or a specific state recogniz ed leave;  
• Follow the procedures in the Discretionary Leave of  Absence Policy if you are requesting a leave of ab sence that 
is not otherwise covered by a policy in the Handboo k or State Supplement; or 
• If you have no PTO or PSSL available, or if the rea son for the absence does not fit within one of the above-
referenced policies, ask your manager for permissio n and receive approval prior to the start of your s hift. 
If you need to end work early. You must contact your manager to obtain advanced pe rmission if you need to end work 
prior to the end of your scheduled workday. If an e mergency, however, or other unforeseen situation th at is a Qualifying 
Reason under an applicable paid sick or safe leave law prevents you from providing advance notice of t he need to end 
work (for example, you or a spouse goes into labor) , you must inform your manager of the circumstances  as soon as 
possible following resolution of the emergency, or if an emergency or other unforeseen situation preve nts you from giving 
notice personally (for example, if you are hospital ized), a friend or family member may provide notice  on your behalf. 
After the emergency has been resolved, you must ens ure your time records accurately reflect your hours  worked.  
Repercussions for unexcused absences. If you are absent from work and you did not provide  notice 2 hours in advance 
of your scheduled shift (did not receive advance ap proval if applicable) following the procedures abov e, your absence will 
be considered “unexcused,” and you may be subject t o discipline depending on the surrounding circumsta nces. If you 
have more than two consecutive unreported absences,  the Company will consider your absences to be aban donment of 
your employment. Nothing in this policy is intended  to interfere with protections for domestic violenc e leave as applicable 
under state or federal law.  
DRESS CODE & APPEARACE POLICY  
  
We believe that pride in both yourself and the Comp any is reflected in your appearance and in the imag e you create.  
Appropriate dress, grooming, and hygiene standards contribute to the professional image we strive to p resent to our 
customers. Therefore, while style and grooming are highly personal and subject to your own tastes and preferences, it is 
important that we have guidelines to maintain an ap propriate standard of professionalism in our stores , adhere to 
Section Three: Employment Expectations 
Page│ 17  US Store Associate Handbook 
2024 
 commonly recognized standards of personal hygiene, and make you identifiable as an associate to custom ers.  The 
Company respects your right to dress consistent wit h your gender identity/expression.  
  
The following requirements apply to store associate s while working:  
• Regardless of the hairstyle that you choose, hair m ust be kept clean and neat;  
• Facial hair, including beards and mustaches, must b e neat, trimmed, and well kept;  
• Nails are to be kept neatly manicured;  
• Jewelry and watches must be discreet;   
• Sunglasses are prohibited;  
• Sweatpants, or any fleece pants, are prohibited* 
• Tattoos/body art that may be perceived as vulgar, o ffensive, threatening, or obscene cannot be visible  to 
a customer or co-worker and must be covered;  
• Sleepwear, including pajama pants, is prohibited;   
• Sportswear inconsistent with the Company’s style, i ncluding high school and collegiate apparel and spi rit 
wear, is prohibited;  
• Clothing may not be sexually revealing, suggestive,  or explicit; low-cut or sheer/see-through/fish-net  
clothing, even if fashionable, is not acceptable, a nd any clothing that reveals your undergarments is not 
acceptable;  
• Clothing, apparel, or accessories, may not have tex t or symbols that display or promote any personal, 
political, or sexual messages, or any messages that  may be considered offensive, disrespectful, or 
controversial to a reasonable person, because such apparel may cause disruption in the workplace and 
interfere with the Company’s public image; you may,  however, wear small, non-distracting union insigni a in 
customer-facing areas.  
• All clothing must be clean (no stains), wrinkle-fre e, and you are prohibited from wearing clothing, 
footwear or accessories that are dirty or otherwise  unpresentable.  
  
We do not require you to buy or wear clothing, foot wear, accessories, or other items from our Company.  You should, 
however, wear clothes, accessories, and footwear th at are consistent with/ similar in style to our bra nds. You are also 
prohibited from wearing clothes that are clearly th ose of a competitor (i.e., have a large or obvious label, name, logo, or 
identifiable trademark of a competitor).   
  
In some locations, certain associates are required to wear closed-toe footwear for safety reasons. Ple ase consult with 
Store Management to determine if you must wear clos ed-toe footwear.  
  
If you are unsure about whether a particular item o f clothing, footwear or accessory is permissible, a sk your Store Manager 
for clarification.   
  
To the extent your sincerely-held religious beliefs  and/or practices conflict with this Policy or you need a medical 
accommodation in connection with this Policy, a rea sonable accommodation may be requested in accordanc e with the 
Reasonable Accommodations Policy.  
Any associate who is not dressed in attire consiste nt with this Policy will be considered unsuitable t o work and will be 
asked to return to work appropriately dressed. Asso ciates who disregard this Policy and its standards will be subject to 
discipline.  
 
* This dress code requirement does not apply to Gill y Hicks standalone associates 
 
 
Section Three: Employment Expectations 
Page│ 18  US Store Associate Handbook 
2024 
 INTIMATE RELATIONSHIPS AT WORK (NON-FRAT) 
The Company strongly believes that a work environme nt where associates maintain clear boundaries betwe en personal 
and business interactions is necessary for effectiv e business operations. We recognize that bonds betw een individuals 
sometimes develop in the workplace. However, the Co mpany believes it is important to manage such relat ionships when 
they develop in order to prevent any risk of negati ve impact to the workplace or individual associates . This Policy 
establishes boundaries around permissible intimate relationships and, if permitted, how they should be  conducted during 
working hours and within the working environment. 
Policy Definitions.  
An Intimate Relationship is a consensual dating or other relationship that i s or may be reasonably expected to lead to the 
formation of a consensual romantic or consensual se xual relationship. Even with this definition, we re cognize that you 
may have different definitions and understandings a s to what constitutes an intimate relationship; if you have questions 
or need further clarification, you should speak to Human Resources. 
A Manage r includes anyone in your management chain upwards including District Managers (and above), General 
Managers, Store Managers, Assistant Managers, and a ny non-manager associate that has supervisory autho rity. For 
example, Full-Time Keyholders do not have the abili ty to hire, terminate, or discipline and are not ma nagers, but for 
purposes of this Policy, they are considered part o f the management team and subject to the restrictio ns applicable to 
managers.   
A Subordinate  means anyone that reports into you, directly or in directly. 
Relationships Between Associates and Managers or ot her Associates with Supervisory Responsibilities. The manager 
position and/or supervisory role requires the trust  and confidence such that intimate relationships be tween a 
manager/supervisor and a subordinate associate can compromise the manager’s position of trust and auth ority and impair 
the ability to manage or supervise without bias or perceived bias. In addition, the Company recognizes  that there may be 
a difference in what an individual in a managerial or supervisory role and an associate considers to b e consensual, due to 
the unequal power dynamic in the workplace between them. Because of the resulting inherent problems, m anagers and 
associates with supervisory responsibilities may no t have an intimate relationship with their subordin ates. Additionally, 
subordinates cannot be hired, transferred, or promo ted to a role in which they are in an intimate rela tionship with their 
manager or an associate with supervisory responsibi lities over them. If you become aware of or are/bec ome involved in 
an intimate relationship as described above, you mu st notify Human Resources. The Company will then re view the 
circumstances and determine whether further action is necessary. The initial solution may be to make s ure the associates 
involved no longer work together on matters where o ne is able to influence the other or act for the ot her. Hiring, firing, 
promotions, performance management, distribution of  work duties, compensation decisions, and financial  transactions 
are examples of situations that may require realloc ation of duties to avoid an actual or perceived rew ard or advantage. 
Should a change in marital status or promotional op portunity create a conflict of interest, a transfer , job change, or 
reassignment may be necessary and will made in a no n-discriminatory fashion consistent with the Compan y’s best 
interest. Where other resolutions are not practical , separation from employment may be necessary. 
Regarding socializing, managers may only socialize with their subordinates provided they receive Distr ict Manager 
approval in advance, the event takes place in a pub lic setting, and all of the following is observed:  
• Every management team member is invited and is reas onably able to attend (manager covering store rotat es, 
etc.). The activity must be lawful and work appropr iate;  
Section Three: Employment Expectations 
Page│ 19  US Store Associate Handbook 
2024 
 • Everyone observes the Discrimination and Harassment  Policy as well as the Standards of Conduct, behavi ng 
responsibly and respectfully at all times; and  
• Everyone understands that their actions while toget her create impressions, impact working relationship s, and can 
impact their careers.  
Store management teams may lose the privilege of so cializing together outside of work if doing so has compromised their 
objectivity, created a perception of favoritism, or  has negatively impacted the work environment in an y other way.  
Intimate Relationships at the Same-Level. While intimate relationships between two associates , or between two 
managers, at the same level—and  therefore do not f all directly or indirectly above or beneath each ot her within the 
management reporting chain—is  not prohibited, such  relationships may create workplace problems. Assoc iates involved 
in an intimate personal relationship are expected t o conduct themselves in an appropriate workplace ma nner that does 
not interfere with others, with overall productivit y, or put other associates or our customers in an u ncomfortable position. 
Specially, we have established the following additi onal procedures and expectations for individuals en gaged in a 
permissible intimate relationship: 
1.  During work time, you are expected to conduct yours elf in an appropriate manner that does not interfer e with 
others or with overall productivity. 
2.  During nonworking time, such as lunches, breaks, an d before and after work periods, if you engage in p ersonal 
exchanges in non-work areas, you should observe an appropriate workplace manner to avoid putting other s in 
an uncomfortable position.  
3.  You are strictly prohibited from engaging in physic al contact at work that a reasonable person could d eem 
inappropriate for the workplace. 
4.  If you allow personal relationships with co-workers  to adversely affect the work environment, you will  be 
disciplined.  
5.  Where doubts exist as to the specific meaning of th e terms used above, you should make judgments based  on 
the overall spirit and intent of this Policy.  
Company Action. The Company reserves the right to take appropriate action in instances where intimate relationships 
cause disruption to the business and working enviro nment. Such actions may include termination of one or both 
associates. In all cases, the terms of the Company’ s policy against sexual harassment remain in effect .  
Failure to cooperate with the Company to resolve a conflict or problem caused by an intimate relations hip, refusal to 
accept a reasonable solution, or other conduct in v iolation of this Policy may result in disciplinary action, up to and 
including termination. 
Please raise questions or concerns about this Polic y with Human Resources. 
TRANSFERS AND PROMOTIONS 
The Company promotes associates according to their performance, ability to get the job done, willingne ss and ability to 
assume additional responsibility, and based on gene ral business needs. If you are interested in a tran sfer or promotion, 
notify your manager. While we review requests on a case-by-case basis, everyone will be given equal co nsideration.  
To transfer to a new store and/or be promoted, Stor e Managers must be in their position and location f or at least six 
months. Assistant Managers may transfer and/or be p romoted to a different location after achieving a m inimum full-time 
status of at least nine months and after six months  in their current position and current location. As sistant Managers may 
Section Three: Employment Expectations 
Page│ 20  US Store Associate Handbook 
2024 
 be promoted within their current location with a mi nimum full-time status of six months in the current  position and 
current location. The Company reserves the right to  transfer and/or promote managers, regardless of th e parameters set 
forth in this Policy, when the Company’s business n eeds require such transfer and/or promotion. 
EMPLOYMENT/INCOME VERIFICATION 
Moving into an apartment? Buying a home? Purchasing  or leasing a car? Chances are you will have to get  your employment 
and income verified. The Company has contracted a t hird-party, The Work Number, to provide an automate d service that 
is available anytime-anywhere. This service is used  for mortgage applications, reference checks, loan applications, 
apartment leases, and anything you need that requir es proof of employment and/or income. The Work Numb er is secure, 
accurate, and available 24/7.  
For Proof of Employment: 
Contact The Work Number through www.theworknumber.c om/verifier, 800-367-5690, or 800-367-2884. Give th e person 
needing your proof of employment (the verifier) the  Company’s Employer Code: 10902  and your Social Security Number 
For Proof of Employment plus  Income: 
1) Visit www.theworknumber.com/employee or call 1-8 00-367-2884 
2) Enter the following information: Employer Code ( 10902); Your SSN; Your PIN (Birth Month, Birth Date , and last four 
digits of your SSN  MM-DD-#### ) 
3) Select to obtain a Salary Key – Write down the s alary key given to you 
4) Give the person needing proof of your employment  and income (the verifier) the following informatio n: Your SSN; 
Employer Code (10902); Your Salary Key (from #3 abo ve); and The Work Number Access Options 
(www.theworknumber.com/verifier or 800-367-5690)  
CONDUCT OUTSIDE OF WORK 
Your cooperation in observing reasonable and proper  standards of conduct is expected both at work and outside of work. 
In general, outside activity that violates the law or adversely affects your job performance or your a bility to perform your 
job is not permitted.  
The Company does not prohibit you from having anoth er job if the job does not prevent or distract you from your work 
obligations and does not create a potential or actu al conflict of interest. For example, it is a confl ict of interest to work for 
a competitor as such work would necessarily interfe re with your job duties and also require you to bre ach your duties 
owed to the Company with respect to Confidential In formation. If you have doubt regarding current outs ide employment 
or other outside activity, discuss the situation wi th Human Resources.  
SOCIAL MEDIA AND THE WORKPLACE 
Popular social media platforms like Facebook, Twitt er, LinkedIn, Instagram, Snapchat, WeChat, Weibo, a nd others make 
it easy to build a web of friends and acquaintances  and share your photos, whereabouts, contact inform ation, and other 
user-generated content. In many cases, when you use  social media outside of work and on your own time,  it is personal. 
However, it is important to remember that you are a n ambassador for our brands and the Company in ever ything you do, 
and posting on social media can affect the Company’ s reputation and business. You must take particular  care with any 
content you post or engage with online. Your conten t or comments may be interpreted as reflective of t he Company’s 
opinions and values, even if that is not your inten tion. 
Section Three: Employment Expectations 
Page│ 21  US Store Associate Handbook 
2024 
 Please be mindful that you are always responsible f or what you publish on social media, even when publ ished outside of 
work. If you use social media in ways which violate  the law, which adversely affect your performance, ability to do your 
job, to function effectively in the workplace, or v iolates Company policies, you may be subject to dis cipline up to and 
including termination of employment. If ever in dou bt, please speak with your manager, the One Number,  or the 
Corporate Communications & Public Relations team before  engaging online (refer to the Company Directory at  the 
beginning of the Handbook for contact information).  
What You Should Do on Social Media:  
• Follow the Company’s Respect Policy and the Platinu m Rule – treat others as you would like to be treat ed when 
using social media. 
• When you make statements about the Company and/or i ts products or services, you must  disclose the fact you 
are employed by the Company. You must also disclose  your affiliation with the Company if you comment a bout 
the Company or work-related matters or if it can be  inferred from your post that you work at the Compa ny. This 
disclosure can be made in the copy of the post (e.g ., I work at A&F and love our new fall line), or by  including a 
hashtag (#AbercrombieAssociate, #HCoAssociate) in t he first three lines of the post, so that it is vis ible without 
clicking “…more.” 
• Any posts and personal blogs must comply with the C ompany’s policies regarding confidentiality. This a lso applies 
to comments posted on other blogs, forums, and soci al networking sites.  
• Be mindful. Anything posted on social media could r emain public forever, even if you try to change or remove it 
later. Keep in mind the speed with which informatio n posted on social media is shared (and often misun derstood). 
Use your best judgment, and when in doubt, do not p ost! 
• Strive for integrity, honesty and kindness. You are  accountable for the content you post on social med ia, including 
written postings, comments, photos, videos, and “li kes”.  
• Honor our policies and values. All Company policies  apply equally to social media activities. Conduct or behavior 
that is not permitted in “real life” is also prohib ited via social media. We expect you to act on soci al media with 
common courtesy, decency, and respect for others, a nd to exercise mature judgment. 
• Be safe. Be careful about posting personal informat ion online. Remember what you post online is rarely  (if ever) 
truly private and may be seen and forwarded by othe rs.  
What You Should Not Do: 
• You should never represent that you speak on behalf  of the Company or management, or as a representati ve or 
agent of the Company or management, unless you are specifically authorized to do so.  
• Harassment, bullying, discrimination, or retaliatio n that would not be permissible against other assoc iates in the 
workplace is not permissible online, even if done a fter hours, from home, and on home computers. Posti ngs that 
include discriminatory remarks, harassment, threats  of violence, and any similar inappropriate or unla wful 
conduct are not allowed and violate Company policy.  
• The Company values a diverse workforce, and conside rs differing viewpoints a strength. While social me dia sites 
may provide some insight into the different qualifi cations applicants bring to a role, when recruiting  online, you 
should not review or consider any information relat ing to a recruit’s Protected Categories. 
• The Company relies on intellectual property and tra de secrets to maintain its edge, market share, and identity. 
We take pride in our unique brands and the business  infrastructure that supports them. Accordingly, yo u may not 
Section Three: Employment Expectations 
Page│ 22  US Store Associate Handbook 
2024 
 share on social media anything that is confidential . Please refer to the Confidential Information Poli cy for a full 
description of confidential information that may no t be disclosed.  
• The Company regularly monitors postings, comments, and discussions on the Internet and in social media  
pertaining to the Company, its competitors, custome rs and the industry. You should have no expectation  of 
privacy with respect to your publicly accessible po stings on social media. Your postings can be review ed by anyone, 
including the Company. 
• Do not disclose or use customer or vendor informati on. Do not share non-public customer or vendor info rmation. 
Do not post on social media photos, videos, logos, or trademarks concerning the Company’s customers an d 
vendors, or otherwise identify, through hashtags or  other means, the Company’s customers and vendors, without 
their consent. 
• When posting about the Company, you may not pretend  to be someone you are not. 
• Do not use the Company’s brand to endorse, promote,  denigrate, or otherwise comment on another company , 
another company’s product/service, or person. 
• Do not use the Company’s image, logos, or trademark s on social media for commercial purposes or to end orse a 
product or service. 
• Do not require other associates or applicants to pr ovide information regarding their use of personal s ocial media 
(for example, the social media sites that they freq uent) or to disclose the content of their personal social media 
accounts. 
• Do not request or require associates or applicants to access their personal social media accounts for work-related 
purposes. For example, you cannot require associate s to access their Facebook Page so that you can rec ruit their 
Facebook friends. 
• Do not request or require associates or applicants to disclose personal social media log-in credential s or passwords 
or to access personal social media in your presence . 
• Do not request or require associates or applicants to change the privacy settings on their personal so cial media 
accounts. 
Do not request or require associates or applicants to add Company associates to the contact lists for their personal 
social media accounts. 
• On the Company’s sites, or when posting about the C ompany: 
o Do not engage in any communication that is defamato ry or infringes upon the intellectual property or p rivacy 
and publicity rights of others. 
o Do not make any statement that in any way promotes unsafe or dangerous activities. 
o Do not make any statement that violates local, stat e, or federal law. 
Final Reminders: 
• You are personally responsible for the content you publish on blogs, social networking sites, and othe r user-
generated media. 
• If you have a work-related complaint or issue, we a sk that you make use of the workplace resources ava ilable to 
you. Your manager, Human Resources, and other depar tments are here to help and will be productive aven ues 
for conversations about anything work-related. 
Section Three: Employment Expectations 
Page│ 23  US Store Associate Handbook 
2024 
 • You are personally responsible for the content you publish online and will be held accountable for vio lating this 
Policy. 
• Readers of social media who consider posts by an as sociate to be racist, anti-Semitic, sexist, homopho bic, 
transphobic, obscene, harassing, bullying or otherw ise offensive may submit a complaint to Human Resou rces. 
The Company takes complaints seriously. 
• You should have no expectation of privacy with resp ect to social media activity or while using the Com pany’s 
Technology Systems. The Company may monitor social media activities regardless of when or where they o ccur. 
COMMUNICATING WITH THE MEDIA AND OTHER THIRD PARTIE S 
You may be contacted by  media to provide a comment or information on behalf  of the Company. You are prohibited from 
interacting with the media on behalf of the Company  unless expressly authorized by the Public Relation s Department. If 
you receive any media inquiries for comments and in formation on behalf of the Company, even informally , please 
immediately direct the request to the attention of the Public Relations Department. Violation of this Policy can lead to 
discipline, including and up to termination.  
Media may be present at external events. Participan ts should assume that any comments made during a pa nel, a speech, 
Q&A session, or socializing before or after a speak ing engagement (where journalists may often be mode rators) are public 
and on-the-record. It should be assumed that attend ees, including media, at any event may be active on  social media and 
that any statements made will be in the public doma in. The provisions of the Standards of Conduct and Media Policy (both 
available on the intranet) apply at speaking events .   
If you receive any media inquiries for comments or interviews during or after an event that are beyond  the scope originally 
agreed with the Communications and Public Relations  team, please direct the inquiries to the Communica tions and Public 
Relations Department (refer to the Company Director y at the beginning of the Handbook for contact info rmation).  
 
EXTERNAL SPEAKING OPPORTUNITIES  
Associates may be contacted by organizations, inclu ding partners, vendors and media organizations, to participate in their 
events either as a panelist or speaker, or to provi de a comment or information for related marketing m aterials. 
Participation in such activities can be beneficial for your own development and to the Company. Howeve r, the process for 
managing who speaks on the Company’s behalf (formal ly and informally) is one that needs to be managed carefully; it is 
a critical component of managing and protecting the  Company’s reputation.  
Approval Process . Before agreeing to speak at any external event, w here you are identified as a member of the Company 
or are speaking (or may be perceived to be speaking ) as a representative of the Company, you must foll ow a simple review 
and approval process.  Acting as a ‘representative’ can be formal or impli ed, based on subject matter and event, i.e ., 
whether a reasonable person would conclude an indiv idual is speaking as a representative of the Compan y or purely in a 
personal capacity. Prior   to agreeing to participation, you must first:  
1.  Obtain approval from your direct manager  
2.  Submit the following information by email for revie w/approval to public_relations@anfcorp.com 
Name of speaker & department: 
Manager: 
Section Three: Employment Expectations 
Page│ 24  US Store Associate Handbook 
2024 
 Event name & date: 
Topic of the event: 
Brand(s): 
Event details: (include audience demographic, proposed topics, rel evant website, organizing company, have we 
attended the event before, etc.)  
Will any materials be presented, distributed or pub lished?   
Has the organizer requested corporate or brand asse ts (logos etc.) for use in marketing materials or e vent 
signage? 
Will you be the only A&F speaker? (if not, provide the additional names that will be speaking)  
Will you be the only corporate speaker? (if not, details of others on panel as appropriate)   
Are any other apparel brands participating? 
Is media expected to be in attendance?  
3.  The Communications & Public Relations team will rev iew and respond promptly. As needed, it will liaise  with the 
leadership team, in line with existing external com munications sign-off process. 
4.  Following approval by the Communications team, any marketing materials and plans, presentation materia ls, 
script and/or talking points must be shared with th e Communications & Public Relations team in advance  of the 
event to allow sufficient time for review and appro val. The Communications & Public Relations team wil l liaise 
with finance, legal, Human Resources, etc., where t heir input is required.  
In certain circumstances, you may be offered gifts,  entertainment, travel or accommodation costs to pa rticipate in an 
event or contribute to related marketing content, s uch as a case study. If any such inducement is offe red in conjunction 
with participation, inform the Communications & Pub lic Relations team, and seek prior approval from th e Chief Ethics and 
Compliance Officer, in keeping with the Company’s C ode of Business Conduct & Ethics and Standards of C onduct (both 
available on the intranet). 
This Policy and approval process does not apply to speaking on the Company’s behalf about the Company’ s financial 
performance, or sharing any material, non-public in formation with anyone outside the Company. Such dis closures may 
only be made by a small number of designated roles and named individuals. Presentations on the Company  to the 
investment community, analysts, stockholders, or co mments to any external audience about its financial  performance and 
expectations, or any material non-public informatio n, are subject to the Company’s Disclosure Controls , Policies, and 
Procedures and a Public Disclosure Policy, and requ ire formal review and sign-off. In general, you are  not authorized to 
respond under any circumstances to inquiries from t he investment community or stockholders unless spec ifically 
authorized to do so. If you have any questions rega rding any of these expectations, please contact you r AR Representative 
or the Legal team.  
EXTERNAL SPEAKING SUPPORT 
The Communications & Public Relations team works wi th you to evaluate opportunities and prepare for al l (non-
investment community) events where you may be (or b e perceived to be) speaking on the Company’s behalf . This support 
includes:    
• Ensuring an opportunity does not present potential for reputational risk due to the subject matter, th e publication 
or presenting/sponsoring organizations, and/or spea kers sharing a public platform; 
Section Three: Employment Expectations 
Page│ 25  US Store Associate Handbook 
2024 
 • Securing content approval and providing advance not ification in line with existing formal approval pro cess, 
according to type of content and media engagement; 
• Supporting talking points or speech development; 
• Conducting rehearsal/preparation for effective deli very of key messages to relevant stakeholders; 
• Providing media/journalist/co-panelist background r esearch and management; 
• Leveraging content developed for follow-on earned, shared and owned media opportunities; 
• Agreeing on guidelines around sharing and amplifyin g related content on shared/social platforms; 
• Attendance/on-site support at event if appropriate;  and 
• Managing any related media conversation to ensure a ccurate record and allow for effective follow-up. 
GOVERNMENT REPRESENTATIVES 
If a government agency representative enters the st ore, or otherwise contacts you related to your empl oyment at the 
Company, inform the government representative that you are not authorized to speak on behalf of the Co mpany and that 
someone from the Company will contact them regardin g their request. Also obtain the government represe ntative’s 
contact information and ask for their business card  to verify their identify. Immediately notify your District Manager who 
will contact Human Resources for guidance. You shou ld be respectful and polite at all times to the gov ernment 
representative.  
PHONE CALLS, TEXTING, AND ELECTRONIC RECORDING DEVI CES 
This Policy outlines the Company’s expectations and  requirements regarding using personal cell phones at work, the 
personal use of Company-issued cell phones, and use  of camera phones and recording devices. For purpos es of this Policy, 
“cell phone” refers to handheld electronic devices with capability to receive and transmit voice, text , or data messages, 
and “usage” includes receiving or initiating phone calls, texts, or emails as well as accessing the in ternet or other 
applications. 
Personal Cell Phone Usage: Please limit your personal use of the telephone to essential calls and keep them brief. Personal 
cell phones are permitted on the sales floor but on ly on vibrate mode. You may not make outgoing perso nal phone calls 
or texts while on the sales floor. Incoming persona l phone calls on the floor are only acceptable if t here is an emergency. 
You may use your personal cell phone during a break  in which you are clocked out and off the sales flo or. 
Work-Related Cell Phone Usage. Depending on your position with the Company, you ma y receive a Company cell phone 
or you may be eligible for reimbursement of a perce ntage of your personal cell phone costs. If you are  not provided with 
a cell phone or cell phone reimbursement, use of a personal cell phone for business purposes is not ma ndatory or required. 
If you believe you believe you were required to use  your personal cell phone for work-related purposes  but the request 
for reimbursement was rejected and/or you were told  you are ineligible, promptly notify Human Resource s. 
Recording Devices and Taking Pictures. You may not record another associate or other third  parties or take pictures 
without all parties’ knowledge and consent. This en courages open communication among associates by eli minating the 
impact on the business that may occur when one pers on is concerned that their conversation with anothe r is being secretly 
recorded. You are prohibited from using personal re cording device (including but not limited to a came ra, camcorder, cell 
phone, tablet, or other electronic device with came ra or recording functions) anywhere on Company prop erty and/or at 
a Company-sponsored event, at any time to film or r ecord: (1) trade secret or Confidential Information ; (2) in restrooms; 
Section Three: Employment Expectations 
Page│ 26  US Store Associate Handbook 
2024 
 or (3) in any other manner that violates individual  privacy rights or applicable law. This prohibition  does not apply to you 
if you are required to record/capture content in th e workplace as part of your job duties. 
While  Driving On Company Business.  You may not use cell phones or any other wireless communication devices while 
driving on Company business unless you are doing so  with a hands-free device. This includes, but is no t limited to, making 
phone calls, texting, and accessing the Internet. T hese restrictions do not apply to calls made to rep ort an emergency. You 
must be as cautious as possible when driving and yo u must abide by all relevant federal, state, and lo cal laws pertaining 
to the use of wireless communication devices.  
TECHNOLOGY SYSTEMS 
The Company’s technology, including Company-owned a nd Company-provided computers, related hardware, so ftware, 
networks, tablets, telephones, voicemail, email, an d internet systems (collectively “Technology System s”), are Company 
property and are intended for business purposes and  use during work time. If you are authorized to rec eive a Company-
issued electronic device, you must take the proper precautions to protect the device. This Policy appl ies regardless of 
whether the Company’s Technology Systems are access ed through Company-issued electronic devices or thr ough 
personally owned electronic devices.  
Monitoring and Access. You have no legitimate expectation of privacy as to  your use of the Company’s Technology 
Systems. The Company may monitor and/or access our Technology Systems and obtain the communications an d data 
within these systems (such as emails, voicemails, a nd internet usage), whether business-related or per sonal in nature. 
Additionally, we may store electronic communication s after the communication is created. By using the Company’s 
Technology Systems, you provide your consent to mon itoring, recording, reviewing, accessing, deleting,  and disclosing of 
all communications received or sent on those system s, when the Company deems it appropriate to do so, and within the 
limits of applicable law. 
Permitted Use . You may access only files or programs that you ha ve permission to enter. Unauthorized review of file s or 
use of passwords, installation of non-Company owned  software or hardware, removal of files or programs , or improper 
use of information contained in the electronic comm unications systems is prohibited. 
Technology Usage Must Comply with Company Policies and Applicable Law. Personal use of the Company’s Technology 
Systems may not interfere with Company operations. All Company policies apply to use of the Company’s Technology 
Systems. For example, you are prohibited from using  Technology Systems to engage in any communication or action that 
is illegal, threatening, unlawfully discriminatory or harassing, or that in any way violates any other  Company policy. It is 
also prohibited to use Technology Systems to view o r store pornography.  
Personal Use . The Company recognizes that limited personal use of Technology Systems is inevitable. However, at no  time 
may these systems be used in a manner contrary to t he Company’s policies. Personal use should not inte rfere with your 
job performance or the Company’s and other associat es’ use of these systems. 
Passwords . User IDs and passwords may not be shared with oth er associates  or third parties. Upon request, you must 
inform the Company of password or other private acc ess codes for Company-issued devices. You are respo nsible for 
changing their passwords on a regular basis. Any su spected loss or misuse of a password must be report ed immediately 
to the Company.  
Protecting Technology Systems . You should not copy, store, or distribute on the Company’s electronic communications 
systems or any software or other copyrighted materi al of a third party without first confirming in adv ance that the 
Company has the right to do so. The Company respect s all software and other copyrights and adheres to the terms of all 
Section Three: Employment Expectations 
Page│ 27  US Store Associate Handbook 
2024 
 licenses to which the Company is a party. It is you r responsibility to ensure that the software and ha rdware computer 
resources owned, leased, or licensed to the Company  are properly secured and controlled.   
Remote and Wireless Network Access. Access to the Company’s wireless network is limited  to authorized users. You may 
not share wireless network access with non-associat es.  
Ensuring Data Security.  The Company is dedicated to protecting and maintai ning the security of associate and customer 
information. Security concerns can include any actu al or suspected incident that poses a threat to the  effective use of 
information, such as the confidentiality, integrity , and availability of information. You have an obli gation to protect our 
information assets, systems, and infrastructure, in cluding the information of our associates and custo mers. You are also 
required to maintain the confidentiality of informa tion assets of third parties, regardless of whether  that protection is 
contractually or legally required.  If you discover a violation of this Policy or suspe ct an incident that has somehow 
compromised the Company’s Technology Systems or the  security of an associate or customer information, you must notify 
your Manager and/or District Manager, and/or IT (th rough the One Number) immediately.  
You May Not Use the Company’s Technology Systems: while driving; to further the business activity of an entity other 
than the Company; to conduct a job search unless it  is part of a Company-authorized outplacement proce ss; to engage in 
activities for personal , financial profit during work time; to access, down load, or transmit adult-networking sites such as 
Tinder, Hinge, Grindr, Bumble, etc.; to transmit in formation that is false; to send Confidential Infor m ation  to a personal 
email address without the Company’s permission; to transmit copyrighted materials or other intellectua l property without 
authorization; to engage in activities that result or may result in unauthorized billing or cost to th e Company; or to engage 
in a violation of the law or the Company’s policies . 
SURVEILLANCE 
The Company utilizes surveillance technology for pu rposes of workplace safety, security, to prevent th eft and other 
misconduct, and for other lawful purposes. It is po ssible that such surveillance may monitor activitie s not related to the 
Company's business. The Company respects the privac y of associates and customers and, therefore, does not maintain 
surveillance technology in restrooms or lactation a reas. The Company will not use surveillance technol ogy for any unlawful 
purpose such as monitoring, or giving the impressio n of monitoring, activity protected under the Natio nal Labor Relations 
Act. By accepting and continuing employment with th e Company, you consent to workplace surveillance, a s described in this 
Policy.  
PERSONNEL RECORDS  
It is important for tax and other purposes that the  Company maintain certain personal information abou t you in a 
personnel file. Please provide your manager with no table personal information changes, such as changes  that will or may 
impact your benefit eligibility or our ability to c ontact your family members in an emergency (e.g., l egal name, address, 
phone number, emergency contacts, income tax exempt ions, etc).  
All personnel files are confidential Company record s. You may view the contents of your personnel file  with a member of 
management present. Upon request, copies of file do cuments may be made by a manager. If you are intere sted in 
reviewing you file, you should contact your Distric t Manager.  Unauthorized access to or disclosure of confidentia l 
personnel records (personnel file contents, etc.) m ay result in disciplinary action up to and includin g termination.  
RELOCATION 
In certain circumstances, Company associates are re imbursed for expenses incurred for relocation as pa rt of an offer of 
employment or a transfer to another position within  the Company. If you receive reimbursement for relo cation expenses 
Section Three: Employment Expectations 
Page│ 28  US Store Associate Handbook 
2024 
 and subsequently violate the terms of the relocatio n agreement, you will be expected to reimburse the Company for all 
relocation expenses per the terms of their relocati on agreement.  
EMPLOYMENT OF MINORS  
Minors (under the age of 18 years old) are permitte d to work at certain stores. Refer to your State Su pplement document 
or contact Human Resources for additional informati on.  
FITTING ROOM PROCEDURES 
• Greet the customer. 
• Take the items from the customer and count them (on ly 10 items may be in the fitting room at any given  time). 
• Place the items in a fitting room that is clean and  clear of tags, size stickers and clothing. 
• Only allow one person per fitting room, with the fo llowing exceptions: 
o The customer is accompanied by a parent/guardian;  
o The customer has a disability, whether that disabil ity is visually obvious or not, and requests to hav e another 
person accompany them in the fitting room. 
• If two people need to be in the fitting room for th e exceptions stated above, they are still only perm itted to have 
a max of ten (10) total items in the fitting room. 
• Count the number of items the customer exits with ( if the number of items is different than what they entered 
with provide a customer service statement). 
• Check inside the room and clear out any merchandise . Take merchandise to designated go-back area. 
• The fitting room number tag should be placed on the  inside handle of the fitting room door when the fi tting room 
is NOT occupied. When the fitting room IS occupied by a customer, the fitting room number tag should b e placed 
on the outside door handle displaying the amount of  units the customer has taken into the fitting room . 
As an associate, you may not: 
Enter an occupied fitting room. 
• Use a camera, smart phone, or other recording devic e in the fitting room area of the store. 
ASSET PROTECTION STANDARDS 
It is critical that you follow the Company’s Asset Protection standards below. Any questions regarding  Asset Protection 
should be directed to your Asset Protection Team. I f you witness an associate stealing or if you suspe ct an associate to be 
dishonest, notify your Asset Protection Regional Te am or call the One Number immediately.  
You may not: 
1.  Wear store-owned merchandise unless expressly autho rized and supervised by management, such as during fit 
sessions.  
2.  Misuse the associate discount or brand loyalty prog ram privilege.  
3.  Allow, during non-business hours, anyone, other tha n Company associates currently scheduled by managem ent 
and working on the clock, anywhere in the store (in cluding the back stock room of the store).  
Section Three: Employment Expectations 
Page│ 29  US Store Associate Handbook 
2024 
 4.  Allow, during business hours, associates who are no t on the clock in the back room ( i.e. , non-sales area), unless 
approved by a manager.  
5.  Allow anyone, other than associates, in non-sales a reas. This also means that you may not receive visi tors in non-
sales areas.  
6.  Cash out friends or family members.  
7.  Cash out your own purchases, exchanges, or returns.  All associate purchases made at the Point Of Sale (“POS”) 
machine must utilize the associate discount card. A ll purchases outside of the POS need to be refunded  and 
repurchased at the POS in conjunction with the asso ciate discount card.  
8.  Apply customer appeasements to transactions in bad faith, or in an irresponsible manner, e.g. , where the nature 
of the appeasement is disproportionate to the custo mer issue, or where the appeasement is not related to a 
genuine and reasonable customer concern.  
9.  Remove money from the register without management d ocumentation being placed in the register at the ti me of 
removal.  
10.  Conduct pat-down searches of an associate or custom er. 
11.  Attempt to apprehend or follow a person who you bel ieve may have taken merchandise.  
12.  Accuse customers of shoplifting or imply that a cus tomer is dishonest.  
13.  Use code words to alert other associates of custome rs you believe are or may be stealing.  
14.  Raise your voice to, threaten, fight with, or inten tionally cause bodily harm to a customer.  
15.  Request that customers leave the store, unless the customer is causing significant disruption to the s tore. 
Examples of significant disruption can include but are not limited to catcalling, verbally or physical ly harassing 
customers, etc. Customers are allowed to simply han g out in the store.  
You are expected to follow and be aware of the addi tional asset protection standards  at all times : 
1.  You may obtain price adjustments on items purchased  within seven days.  
2.  All returns must be accompanied by a receipt or pro of of purchase.  
3.  All transactions including purchases, returns, and exchanges must be rung by the District Manager or a  member 
of store management. You must comply with your coun try specific return policies.  
4.  Immediately before clocking out, the Company checks  each associate’s purse/bag, packages, coat and oth er 
belongings. This occurs at the cash wrap (within vi ew of Closed Circuit TV Cameras where applicable) b y 
management each time an associate leaves the premis es. Coats must be taken off prior to being checked.  You will 
then be immediately walked out to the front of the store by management.  
5.  Remove trash from the store in the presence of mana gement. Management must personally inspect the cont ents 
of each container for company property of value. Cl ear trash bags must be used.  
6.  Comply with all fine print rules for individual cou pon usage.  
7.  When ringing in a sale transaction, you must accoun t for each item of merchandise, ensure that the app ropriate 
payment is successfully received/processed, and ens ure that the customer receives the merchandise purc hased 
with the register sales receipt for that merchandis e. If a customer leaves behind their receipt, gift card, or 
merchandise card, give it to the floor manager imme diately.  
Section Three: Employment Expectations 
Page│ 30  US Store Associate Handbook 
2024 
 8.  If a customer leaves their personal items behind, s uch as a wallet, phone, camera, or shopping bag, yo u must 
notify the manager on duty immediately and they wil l contact the mall office or mall security to come and retrieve 
the item. In the circumstance where the mall will n ot take the item(s), contact your local Asset Prote ction team 
member. 
9.  If the alarm system sounds, you may suggest to the customer that they could have a sensor in their bel ongings 
and ask if you can assist them in finding it. If th e customer indicates that they do not have a sensor  and/or do not 
want assistance, disengage and allow the customer t o leave the store. This applies to any EAS activati on regardless 
of the type/brand of bags in the customer’s possess ion.  
This list is not intended to be all-inclusive.  
Section Four: Standards of Conduct  
Page│ 31  US Store Associate Handbook 
2024 
  
 
 
Section 4: 
Employment Standards 
  
Section Four: Standards of Conduct  
Page│ 32  US Store Associate Handbook 
2024 
 GENERAL STANDARDS OF BUSINESS CONDUCT 
Your cooperation in observing reasonable and approp riate standards of conduct is expected. The Company  has specific 
policies designed for the protection of both you an d other associates. We expect your conduct on the j ob to be governed 
by good judgment, consideration of others, and resp ect for the safety and efficiency of the Company. W hile it is impossible 
to list all types of misconduct or unacceptable beh avior, the following are some examples of behavior that will not be 
tolerated (whether on Company premises, performing work, or otherwise representing the Company): 
• Falsifying employment-related records (including, b ut not limited to, your employment application or r esume, I-9, 
time records, and time off requests) or other Compa ny records; 
Engaging in illegal or unethical conduct, including  theft of Company property; 
• Engaging in discriminatory or abusive behavior, inc luding, but not limited to, sexual or other prohibi ted harassment;  
• Failing to maintain appropriate confidentiality reg arding sensitive conversations and business informa tion as it 
relates to investigations and conversations with St ore Management and Human Resources;  
• Possessing, selling, using, or being under the infl uence of unlawful drugs on Company property, during  work hours, 
or at Company-sponsored events;  
• Fighting, horseplay, or otherwise engaging in unsaf e activities, such as failing to observe safety rul es or failing to 
adhere to health and sanitation requirements; 
• Carrying or bringing a weapon or concealed weapon t o work (unless state or local law permits you to ke ep the 
weapon in a locked vehicle); 
• Acting inappropriately or offensively towards or in  the presence of an associate, a customer, or other  third parties; 
• Making misrepresentations to associates or customer s; 
• Being rude or disrespectful to associates or custom ers; 
• Misusing, stealing, neglecting, damaging, or destro ying Company property (including, but not limited t o, vehicles, 
equipment, or supplies) or of another associate’s o r third party’s property; 
• Misusing Confidential Information, intellectual pro perty, or trade secrets belonging to the Company or  another 
individual or entity, including the copying or down loading of trademarks, copyrighted materials, or lo gos; 
• Refusing to follow a lawful work directive or accep t a work assignment, sleeping during work time, or engaging in 
another act of insubordination; 
• Refusing to participate in an internal investigatio n; 
• Failing to properly disclose and/or misrepresenting  your diagnosis or exposure to a contagious disease ; 
• Entering or leaving Company premises and/or locatio ns without notifying a manager, or frequently being  absent 
from your work area during work time; 
• Failing to perform job duties and responsibilities;  
• Failing to follow the Attendance Policy, the Meal a nd Rest Break Policy, the Dress Code Policy, or smo king on 
Company property; 
• Gambling or participating in an illegal lottery on the Company’s property, excluding sports-related fa ntasy leagues 
and similar activities; 
• Aiding or assisting any person in gaining unauthori zed entrance to or exit from Company premises; 
Section Four: Standards of Conduct  
Page│ 33  US Store Associate Handbook 
2024 
 Originating or making maliciously false statements or reports concerning the Company or its associates ; 
Chewing gum while on the sales floor;  
• Negligently or intentionally failing to abide by th e Company’s health and safety programs, policies an d procedures; 
Violating any Company policy contained in the Handb ook;  
• Adding personal software to, or deleting Company so ftware from, Company computers without prior writte n 
authorization; or 
• Violating traffic or parking regulations while usin g Company or customer vehicles, failing to properly  report any type 
of accident involving a Company or customer vehicle , or using a Company vehicle for personal use. 
This list is not intended to be all-inclusive. Ther e are other situations which, based upon the circum stances, could result in 
immediate discharge. The Company will decide what d isciplinary action is appropriate based upon the se verity of the 
circumstances.  
CODE OF BUSINESS CONDUCT & ETHICS 
The Company adheres to the highest standards of int egrity and applies those standards consistently in all locations where 
we do business. We conduct business with a dedicati on to our principles: honesty, integrity, respect, and doing the right 
thing. Our Code of Business Conduct and Ethics (the  “Code”) exists to support these commitments by giv ing us the guidance 
and resources to ensure we are acting ethically at all times. The Code is available on the Company web site in the Investors 
section under Corporate Governance. Please carefull y review the Code in conjunction with this Handbook .  
The Code reflects the importance that we place on e thical conduct. Following our Code helps us protect  the integrity, 
reputation, and future of our brands. It also helps  us fulfill our commitments to all of our stakehold ers and the public, and 
ultimately contributes to our success.  
While we look to the Code for guidance, it is our a ctions that ultimately define us. Acting with integ rity and honesty ensures 
that we meet our high standards and enhance our eth ical culture. Everyone at the Company – all associa tes, managers, 
officers, and directors worldwide, are responsible for following the Code, regardless of seniority or title.  
If you wish to report a suspected Code violation or  seek guidance, the following resources are availab le: your manager, 
Human Resources Representative, the CECO, the Compa ny’s Legal Department. If you are uncomfortable wit h these 
methods of reporting suspected Code violations, the  following resources are also available to you: our  ethics hotline and 
reporting website. Please refer to the Company Dire ctory at the beginning of the Handbook for contact information. 
When using the Ethics Hotline and Website, you may choose to report suspected violations anonymously. Regardless of the 
method you choose to make your report, we will keep  all reports confidential to the fullest extent pos sible and consistent 
with applicable law and the Company’s responsibilit y to conduct an investigation of your report. Remem ber, no matter how 
you choose to report, your concern will be taken se riously. 
CONFLICT OF INTEREST 
A conflict of interest can arise when an associate takes actions or has interests that may make it dif ficult to perform their 
work for the Company objectively and effectively. C onflicts of interests also arise when an associate,  or members of their 
immediate family, receive improper personal benefit s as a result of their position in the Company. We expect you to avoid 
situations that could be a possible conflict of int erest or adversely affect your ability to meet the requirements of your job. 
Never place yourself or the Company in a conflict o f interest.  
Section Four: Standards of Conduct  
Page│ 34  US Store Associate Handbook 
2024 
 You are expected to carry out your business activit ies in a prudent manner, be objective in decision-m aking, and refrain 
from enhancing your personal position by virtue of your association with the Company. Business judgmen t in dealing with 
third parties in the name of the Company must never  be influenced inappropriately by your personal int erests. You are 
expected to exercise good judgment at all times whe n engaged in Company business,  or when engaged in personal activities 
that could affect your ability to perform your job objectively and effectively. 
You may not:  
• Hold a secondary position with a competitor of the Company while employed with the Company that would 
interfere with your job duties to the Company or wo uld necessarily require you to breach the duties ow ed to the 
Company with respect to Confidential Information. A   competitor: (i) is engaged or planning to engage in a business 
that designs, manufactures, promotes, sells, or oth erwise supports the design, manufacture, or sale of  men’s, 
women’s, or children’s apparel and/or accessories, or other merchandise, that are in any way similar t o Company 
merchandise.  
• Take business opportunities for yourself that arise  or are discovered due to your position with the Co mpany or 
through your use of the Company’s property or Confi dential Information; 
• Use the Company’s assets, Confidential Information,  or your position for personal financial gain and/o r to compete 
with the Company; 
• Solicit customers for a competing business;  
• Solicit associates to work for a competing business ;  
• Have a financial interest in a business supplying t he Company, a customer of the Company, or a competi tor of the 
Company;   
• Accept services or receive payment from a supplier,  customer, or competitor that personally benefits o r appears to 
personally benefit you; or 
• Engage in a transaction on behalf of the Company wh en the other party to the transaction is your immed iate or 
extended family member, an entity in which you have  a material financial interest, or if you are an of ficer, director, 
or general partner of the entity.  
If you have an actual or potential conflict of inte rest, you must remove yourself from the situation a nd you must immediately 
report the situation to Human Resources.  
CONFIDENTIAL INFORMATION  
The Company relies on Confidential Information to m aintain its edge, market share, and identity. We ta ke pride in our 
unique business infrastructure. Accordingly, we ask  that you treat certain types of information with h eightened sensitivity 
and discretion. You are responsible for safeguardin g the Company’s Confidential Information, and you m ay only use 
Confidential Information for valid business purpose s. The term “Confidential Information” in this poli cy means all non-public 
information and/or trade secrets of the Company, it s parents, subsidiaries, and/or other affiliates, i n any format whether 
electronic, printed, typewritten or handwritten doc uments, or sound recordings. The term “Confidential  Information,” as 
referenced throughout this Handbook, includes, for example:  
• Customer and Other Third-Party Private Information : the names, addresses, and contact details of the Company’s 
customers and potential customers, and other inform ation regarding the Company’s current, past, or pot ential 
customers, suppliers, distributors, and other busin ess partners, or the Company’s current, past, or po tential 
products, services, technologies, operations, or af fairs; 
Section Four: Standards of Conduct  
Page│ 35  US Store Associate Handbook 
2024 
 • Non-Public Company Financial Information: the Company’s financial information such as budgets , business models 
and plans, financial accounts, attendance reports a nd utilization statistics, revenue reports, operati on metrics, bank 
account details, earnings, sales, assets, debts, pr ices, fee structures, volumes of purchases or sales , expenses, payroll 
data, insurance, or claims statistics; 
• Product Development and Design Strategy:  the Company’s research and development programs an d plans; 
confidential techniques and processes used in conne ction with the research and development of the Comp any’s 
products and services, including product design con cepts, patterns and formulations, manufacturing met hods, 
material sourcing information and lists, research a nd development data, buying practices, financial da ta, operational 
data, technical data, innovations, computer program s, un-patented inventions, and trade secrets; 
• Business and Marketing Strategy:  business and marketing plans and strategy includin g the planning and/or launch 
of new products, partnerships, marketing forecasts,  results of marketing efforts, information about im pending 
transactions, and/or databases created and/or maint ained by the Company to record marketing efforts an d 
information; 
• Changes in Assets or Management: information relating to acquisitions, joint venture s, franchises, or changes in 
control or in management; 
• Contractual Terms between the Company and Third Par ties:  the terms of partnerships, joint ventures, or othe r 
forms of commercial co-operations or agreements the  Company enters into with a third-party; the conten t of any 
bids or proposals submitted by the Company to third  parties; and copies of any contracts between the C ompany 
and its customers that are not readily available to  third parties; 
• Non-Public Company Real Estate Information : information regarding the Company’s expansion pla ns, sites under 
consideration, property and real estate negotiation s, site and/or leasehold pricing, construction desi gns, methods, 
plans, solutions, and/or techniques; 
• Non-Public Company Technology Information : aspects of the Company’s computer technology infr astructure and 
systems, including source and object codes, informa tion, including but not limited to, Trade Secrets, relating to 
proprietary computer hardware or software (includin g patches, updates, and upgrades) not generally kno wn to the 
public, or patent and trademark applications during  preparation or consideration by the relevant autho rities; and 
• Competitive Information and Company Ideas : other non-public information which a competitor o f the Company 
could use to the competitive disadvantage of the Co mpany. Ideas which are derived from or relate to yo ur access 
to/knowledge of any of the above enumerated materia ls and information owned by the Company or its cust omers. 
Additional Confidentiality Obligations:  
• In addition to this Policy, you may be required to sign a confidentiality agreement, which is incorpor ated by 
reference into this Policy and will control in the event of a conflict; 
• If you, by virtue of your job responsibilities, hav e access to other types of sensitive personal infor mation ( e.g. , social 
security numbers, medical information, drivers’ lic ense numbers, associate or customer contact informa tion, credit 
card or bank information), you are required to safe guard the confidentiality of such information and o nly provide 
that information when there is a legitimate busines s need to know the information or when required by law; and 
• If you are authorized to work remotely, you must co mply with the Company’s policies regarding informat ion security 
and technology use, which includes but is not limit ed to maintaining appropriate security at the remot e work 
location, that non-associates cannot access electro nic files, and that all paper files are secured whe n not in use or 
when you are away from the work location. 
Section Four: Standards of Conduct  
Page│ 36  US Store Associate Handbook 
2024 
 Our Confidentiality Policy is best protected using good judgment. If you have questions as to whether certain information is 
Confidential Information, please contact your manag er or Human Resources. Unauthorized use of Confiden tial Information 
or violation of this Policy will subject you to dis ciplinary action, up to and including termination.  
COMPANY INVESTIGATIONS  
You are expected to assist with Company investigati ons by honestly disclosing all relevant information . If you are questioned 
as part of an investigation or if you become aware of an investigation, you are expected to participat e, maintain appropriate 
discretion and confidentiality as directed by the C ompany, and not take actions that may interfere wit h the Company’s 
ability to investigate. Failure to cooperate, parti cipate, or otherwise assist with investigations wil l result in disciplinary 
action. The Company may, in its discretion, require  confidentiality during the investigatory process. In those circumstances, 
failure to maintain confidentiality may result in d iscipline. The intent of this policy is to protect the integrity of workplace 
investigations and to ensure a fair outcome for any  involved parties. It is not intended to—and should  not be interpreted 
to—restrict your rights under any federal, state, o r local laws, including without limitation the Nati onal Labor Relations Act.  
POLITICAL CONTRIBUTIONS 
Due to strict laws that govern the way a Company co ntributes to political activities and causes, you m ay not ever donate 
money, goods, or services on behalf of the Company or allow any Company resources to be used for polit ical activities. 
Contact your District Manager for more information.   
SOLICITATION AND DISTRIBUTION 
To minimize interruptions in the workplace, which c an be both detrimental to the quality and efficienc y of work, we have 
established the following rules that govern solicit ation, distribution of written material, and access  to Company property: 
• You may not engage in solicitation activities durin g working time. Solicitation is limited to non-work ing time. This 
applies both to the associate doing the soliciting and the associates (or non-associates) at whom thes e activities are 
directed; 
• You may distribute/circulate written or printed mat erial, but only in non-work areas, and only during your own non-
working times as long as materials are consistent w ith our Discrimination, Harassment, and Retaliation  Prevention 
Policy and a reasonable person would not be offende d; and 
• Solicitation and/or distribution on Company premise s by non-associates is always prohibited. 
For purposes of this Policy : 
• Solicitation includes, but is not limited to, colle ction of a debt or obligation, raffles or chance-ta king, the sale of 
merchandise or business services, or the attempt to  sell a product or service ( e.g.,  selling or collecting for personal 
beauty products, religious institutions, schools, G irl Scout ® cookies, etc.); 
• “Working time” means periods when you are working o r should be working and does not include non-workin g 
periods ( e.g. , breaks, meals, or other periods when you are not performing and are not scheduled to work); and 
• “Work areas” include areas controlled by the Compan y where associates are performing work and does not  include 
break rooms and parking lots. 
Excluded from this Policy are charitable and commun ity activities supported by the Company. 
Section Four: Standards of Conduct  
Page│ 37  US Store Associate Handbook 
2024 
 OPERATING A VEHICLE ON COMPANY BUSINESS 
Whether you’re in your car or ours, when driving on  Company business, you are responsible for followin g all local, state, 
and federal transportation laws and procedures. The  possession, use, distribution or sale of alcohol o r drugs, or being subject 
to the effects of alcohol or drugs when providing s ervices for the Company is prohibited.  
POLICY ON UNION 
The Company treats our associates honestly, fairly and with respect. We firmly believe in and follow a  practice of dealing 
directly with each associate as an individual with their own needs or interests. We will actively and sincerely continue this 
practice of working directly with our associates. A s an associate you enjoy: 
• The best in career advancement opportunities; 
• Equal opportunity and treatment; 
• Equitable and competitive wages; 
• Excellent benefits; 
• Open and honest communication; and 
• A rewarding and safe work environment. 
The ability of our associates to work together as a  team and deal directly with one another without in terference will prove 
to be a key factor in our growth and success as a C ompany. We will continually strive to maintain this  cooperative 
atmosphere and protect the Company’s right to deal directly with its most valuable assets, you and our  other associates. 
This policy in no way inhibits associates' rights u nder the NLRA, including the right to discuss wages  and other terms and 
conditions of employment, or to join together with other associates in seeking to improve your terms a nd conditions of 
employment. 
COMPANY PROPERTY 
Any associate caught stealing, damaging, or defacin g Company property will be terminated. If you witne ss or have 
knowledge of a criminal act, you must immediately r eport it to your manager, District Manager, or Regi onal Asset Protection 
Manager. 
Good sense in the care and use of Company property,  equipment and supplies eliminates waste and can re sult in substantial 
savings in operating expenses. Your cooperation wil l benefit you and the Company. Abuse of Company pro perty may result 
in termination. 
Any designs, inventions or innovations conceived or  developed using the Company’s confidential informa tion, trade secrets 
or the Company’s time, facilities, or assets are th e property of the Company and not the individual as sociate. 
 
  
 
 
Section 5: 
Health and Safety 
  
Section Four: Standards of Conduct  
Page│ 39  US Store Associate Handbook 
2024 
 WORKPLACE SAFETY 
The Company is committed to providing associates wi th a safe place to work. You are required to comply  with the 
workplace safety expectations below. In addition to  the below, please reference the Crisis Management Manual for 
additional assistance. The Crisis Management Manual  can be found on The Loop, within the Asset Protect ion section of 
the A&F Library (https://anfcorp.sharepoint.com/sit es/TheLoop). 
No Workplace Violence. Whether verbal, non-verbal, physical, electronic, o r otherwise, conduct that threatens, 
intimidates, coerces, endangers, or creates the per ception of an intent to harm anyone is strictly pro hibited and will not 
be tolerated. This applies to both physical actions  and actions in writing, on social media, by phone,  email, or text message. 
There is no room for joking when it comes to threat s of violence. Even a statement made in jest or in the "heat of the 
moment" will be taken seriously.  
Lookout for Dangerous Situations. Your safety is very important to us. Take time to d o your job in a safe manner. If you 
notice any hazardous or potentially dangerous situa tions that could cause injury, notify your manager or through the One 
Number immediately. Behavior like horseplay can end anger the health and welfare of yourself and others . Exercise good 
judgment and inform your manager, Human Resources, or Asset Protection if anyone at the worksite exhib its behavior 
that could be a sign of a potentially dangerous sit uation. Such behavior includes, for example: discus sing weapons or 
bringing them to the workplace; displaying overt si gns of extreme stress, resentment, hostility, or an ger; making 
threatening remarks; showing sudden or significant deterioration of performance; and/or displaying irr ational or 
inappropriate behavior. 
Report Safety Concerns and Issues.  Contact 911 immediately if appropriate under the c ircumstances. For non-
emergencies, please still report. Notify Asset Prot ection of unsafe conditions, potential hazards, vio lence, or threats of 
violence, actual or potential criminal activity, or  another emergency. If Asset Protection is not imme diately reachable, you 
must report the threat or conduct to your manager o r another member of the management team. Reports ma y also be 
made anonymously through the ethics reporting websi te at  www.abercrombie-ethics.com . If you believe you are being 
retaliated against for reporting a workplace safety  issue, promptly contact Human Resources. The Compa ny will not 
retaliate against you for reporting a good-faith wo rkplace safety issue. 
State laws specifically govern an individual's righ t to conceal or open carry firearms. If you notice a customer with a firearm 
and you have questions or concerns, please contact the GSOC for further direction. If there is an emin ent risk to your 
safety or the safety of customers and associates, c ontact 911.  
Practice Safety Awareness. If you are unsure of safety procedures, ask a manag er. If you leave work after dark and you 
are uncomfortable walking to your car or transporta tion alone, attempt to coordinate leaving times wit h a colleague to 
create a buddy-system. If this is not possible and you are still uncomfortable walking to your car or mode of transportation 
by yourself, please contact your manager in advance  to discuss a solution or contact Mall Security or Home Office Provided 
Guard Services and ask for an escort to your car. 
Sickness. Stay home if you are sick, frequently wash your han ds and observe proper hygiene practices, and during  times 
of a pandemic, practice social distancing. The Comp any will provide you with additional expectations, policies, and 
procedures to be followed related to COVID-19. 
First Aid and Emergencies. Know the locations of first-aid and firefighting eq uipment. Always know the nearest escape 
routes. If a threatening situation occurs, decide t he best course of action to get yourself to safety as quickly as possible. 
Calling Mall Security. You or store management should contact mall securit y and/or the police if you are threatened 
with physical harm. In instances of verbal altercat ions, mall security should be called if it rises to  a threatening level and 
Section Four: Standards of Conduct  
Page│ 40  US Store Associate Handbook 
2024 
 if you feel unsafe. You may also contact Home Offic e Provided Guard Services in the event of a safety related situation at 
your store. Always inform your Regional Asset Prote ction Manager if you feel your safety or the safety  of your customers 
is at risk. 
Company and Personal Property. You are expected to take reasonable measures to ens ure Company assets and property 
assigned or entrusted to you is adequately secured when not in your possession or control. Store keys,  including the 
manager key/card for the register, must be in the p ossession of the authorized management and/or key h older at all 
times. Store keys and manager swipe cards must be o n a manager’s and/or key holder’s person or secured  in the safe. In 
addition, you should not leave personal belongings of value in the workplace. Report damage, loss, or suspected theft to 
your manager. 
Housekeeping . Good work habits and a neat place to work are ess ential for job safety and efficiency. For these rea sons, 
it is important that you take an active interest in  the safety and security of the workspace. You are expected to keep your 
workspace and materials organized. When you use com mon areas such as lunchrooms and restrooms, you are  expected 
to clean up after yourself and dispose of trash pro perly. Report anything that needs repair or replace ment to a manager. 
Injury and Accident Reporting. In the event that you or a customer is involved in an accident or injury within the store, 
you must notify your Store Manager as soon as pract ically possible. You should assist your Store Manag er in completing 
an Accident Report Form, which is available on Thin kLP. The completed form will promptly notify the Ri sk Management 
and Health and Safety Department. ThinkLP also cont ains a Witness Statement Form which should be compl eted 
whenever applicable. For customers who want follow- up after they leave the store, they can contact the  Company’s 
Customer Service Department. Please refer to the Co mpany Directory at the beginning of the Handbook fo r contact 
information. 
Responding to Threatening Situations.  It is important to have a plan in place in the unl ikely event that the workplace is 
threatened. Below is information that will help you  make quick decisions and determine the best course  of action.  
• Always know the escape routes nearest your current location. Please consult the Crisis Manual.  
• If a threatening situation occurs and you decide th e best course of action is to evacuate, exit as qui ckly as possible. 
Keep moving until you find safety and then notify t he police, as well as Asset Protection or your mana ger, as soon 
as possible.  
o You may attempt to direct others to safety, but you  should go quickly whether anyone follows you or no t. If 
you see someone who is hurt, you can try to assist them in evacuating but do not put yourself at risk.   
o Don’t worry about your stuff—you can get it later o r have it replaced. 
• If you cannot safely evacuate and decide that the b est course of action is to hide, make sure that the  area is safe 
and secure, and remain in your location.  
o Make sure your hiding spot does not prevent you fro m evacuating, should the opportunity later arise. 
o If you are in one of our stores and have safely det ermined that you can close without harm, shut and s ecure 
the front door of your store. If you are in the sto ckroom, deploy the Nitelock device.  
o Try to remain as quiet as possible, silence all cel l phones and, if at any point you think it becomes safe to 
evacuate, do so.  
• If you can safely place a call about a threatening situation, notify local police or GSOC.  
Protective or Restraining Orders. If you have a protective or restraining order again st another associate, or if you have a 
protective or restraining order against another ind ividual who may come on Company property, or which lists Company 
Section Four: Standards of Conduct  
Page│ 41  US Store Associate Handbook 
2024 
 locations as a protected area, you must provide to the Asset Protection department a copy of the petit ion. If you obtain a 
stay-away, protective, or restraining order that do es not identify the workplace as a protected area, you are strongly 
encouraged to provide a copy of that order to Asset  Protection immediately after securing the order. T he Company will 
treat information you share confidentially to the e xtent possible. Asset Protection will create a pers onalized security plan 
for any associate with a stay-away, protective or r estraining order. 
Visitors. We do not allow unauthorized visitors to our stores . All visitors must show identification and may not  be allowed 
in the back rooms of the stores unless authorized.  
Conclusion. This Policy is intended to be a helpful guide only to assist in preparing for the unlikely event of a dangerous 
situation involving an extreme act of violence whil e at work. This is not a step-by-step action plan a nd should not be 
interpreted as such. Actions should be determined o n a case-by-case basis, reflecting the individual s ituation and using 
personal judgment. You are, at all times, responsib le for your decisions and actions. You must always put your own safety 
first, and follow the instructions given by the pol ice or other officials, even if they are in conflic t with the guidance above. 
You should not take any action that endangers your own safety or that of other associates or customers .  
WEAPONS-FREE WORKPLACE 
Firearms and other types of weapons are prohibited on the Company’s property, including parking lots, break areas, and 
at Company–sponsored events. The Company further pr ohibits associates from carrying a weapon while wor king or 
conducting Company business, regardless of whether such work or Company business occurs at Company fac ilities or 
elsewhere (including while conducting Company busin ess virtually, at a customer’s place of business, o r in a public place). 
For purposes of this Policy, weapons include, but a re not limited to guns and other firearms, ammuniti on, knives, blades, 
explosives materials, martial arts weapons, toxic o f flammable chemicals, or any other object, whether  model or toy 
weapons that could be used to harass, intimidate, o r injure another individual.  
If you see a prohibited weapon on the Company’s pro perty or believe another associate or a guest on ou r premises is 
carrying a weapon, you should immediately report th e situation to a manager or Human Resources. If you  have concerns 
about the immediate safety of you or anyone else, p romptly call emergency personnel (911). 
The only exception to this Policy is if you own a r egistered firearm, in which case you may keep the f irearm or ammunition 
properly locked and secured in your personal vehicl e on Company property, only if permitted by applica ble state or local 
law. Otherwise, conduct in violation of this Policy  will result in disciplinary action, up to and incl uding termination. 
SEARCHES AND INSPECTIONS 
For the safety of our associates and customers as w ell as the protection of our property, we reserve t he right to question 
you and to search or inspect a package, parcel, pur se, handbag, briefcase, luggage, or other articles carried onto and from 
Company property. In addition, we may search or ins pect your work area or other areas or articles on o ur premises. As 
mentioned in the Asset Protection Policy, purses, b ackpacks, packages and coats will be searched whene ver an associate 
leaves the store.  
You will be disciplined, up to and including termin ation, if you: (1) refuse to allow a search or insp ection; (2) are found to 
be in possession of property belonging to the Compa ny, another associate, a customer, or other visitor  without 
authorization or a reasonable explanation; or (3) a re found to be in possession of items in violation of Company policy, 
such as a controlled substance, alcohol, illegal dr ugs or paraphernalia, weapons, or sexually explicit  material. 
Section Four: Standards of Conduct  
Page│ 42  US Store Associate Handbook 
2024 
 DRUG-FREE WORKPLACE 
The Company is committed to achieving and maintaini ng a drug and alcohol free workplace. This  Policy applies not only 
in the workplace, but whenever and wherever you are  representing or conducting business for the Compan y (“on the 
job”). In other words, this Policy applies whether you are on Company property, traveling on Company b usiness, or at a 
Company-authorized or sponsored event or activity. 
Prohibited Conduct. Unless specifically permitted in this Policy, when reporting to work and while on the job, the followi ng 
conduct is strictly prohibited: 
• Use, possession, transportation, manufacture, sale,  dispensation, or other distribution of an illegal or controlled 
substance or drug paraphernalia; 
• Use, possession, sale, dispensation, or other distr ibution of alcohol; and 
• Performing work for the Company while impaired by o r under the influence of illegal drugs, controlled substances, 
or alcohol. 
Definition of Unlawful Drugs. For purposes of this Policy, “illegal” and/or “cont rolled substance” refers to conduct or 
substances that are prohibited/deemed unlawful purs uant to federal law – such as cannabis – regardless  of whether it 
may be considered lawful pursuant to state or local  law. This Policy does not prohibit use of medicati on pursuant to a 
licensed medical practitioner’s instructions when t he licensed medical practitioner authorized you to report to work. 
However, to the extent permitted by and in accordan ce with applicable law, this exception does not cre ate the option or 
right to report to work in possession of, under the  influence of, or to use medical or recreational ca nnabis at the workplace. 
However, if you believe you need an accommodation r elated to this Policy, contact Human Resources. 
Drug and Alcohol Testing. In the event you are directed to take an alcohol or  drug test, the Company may suspend you 
(with or without pay) or temporarily change your jo b duties until the results are received by the Comp any. If notice of a 
positive test is received for an illegal substance,  and as permissible by state law, you will be disci plined, up to and including 
termination. If you refuse to timely comply with dr ug or alcohol testing under provisions of this Poli cy, such refusal will be 
treated as a positive test and may also result in i mmediate termination. Attempts to adulterate or tam per with a specimen 
or interfere with a drug or alcohol test may result  in termination of employment.  
Discipline. If the Company has reason to believe you are under the influence, the Company may discipline you for t he 
underlying conduct. The Company is not required to conduct a drug or alcohol test prior to issuing suc h discipline. 
Use of Alcohol at Company-Authorized Events. You may consume alcohol, in moderation, at Company- sponsored or 
Company-authorized events, or during business-relat ed meals or social occasions. In these circumstance s, you are 
required to conduct yourself in a professional mann er – this means, for example, acting responsibly an d limiting alcohol 
consumption so as not to pose a risk to the safety of yourself or others. In addition, you are strictl y prohibited from 
operating a vehicle when you are under the influenc e of alcohol. Prior approval from Human Resources i s required in 
order to have a Company sponsored or hosted event. Contact your District Manager for more information.  
Overcoming Substance Abuse. We recognize that a variety of treatment options ar e available for associates suffering 
from alcohol or drug dependencies. The Company main tains a policy of non-discrimination and will consi der 
accommodations in accordance with the Reasonable Ac commodations for Disabilities Policy and applicable  law. If you 
have a substance abuse or dependency issue, we enco urage you to seek professional medical treatment or  care prior to 
violation of this Policy, as you may not request an  accommodation to avoid discipline for a policy vio lation.  
Section Four: Standards of Conduct  
Page│ 43  US Store Associate Handbook 
2024 
 NO SMOKING 
Smoking is not permitted anywhere on Company premis es. This includes the use of chewing tobacco and el ectronic 
cigarettes/vapor devices. Smoking is only permitted  in designated mall areas or outside of the store. 
 
  
 
 
Section 6: 
The Workday and Compensation 
  
Section Five: The Workday and Compensation 
Page│ 45  US Store Associate Handbook 
2024 
 FULL-TIME/PART-TIME CLASSIFICATIONS 
Your employment status is classified based on your work schedule as follows: 
• Full-time associate*: if you regularly work at leas t 32 hours per week; 
• Part-time associate: if you regularly work fewer th an 32 hours per week; or 
• Temporary/seasonal associate: if you are hired for a finite period. Temporary associates are generally  not eligible 
for Company benefits. 
*For purposes of determining eligibility for health insurance benefits only, full-time associates are d efined as averaging 30 
or more hours per week.  
Additionally, your position is classified as “exemp t” or “non-exempt” based on various factors that ma y include 
responsibilities and compensation.  
Non-exempt associates are paid at least minimum wag e and overtime as described in the Overtime Policy.  
Exempt associates receive a salary that is intended  to cover all hours worked and are not eligible for  overtime pay. 
The Company will inform you of your employment clas sification upon commencing employment and if there is a change in 
status and/or classification. 
WORK HOURS AND SCHEDULES 
Store hours are set to meet the needs of our custom ers. Because the flow and volume of work differs be tween locations, 
daily schedules will vary depending on your positio n and your store’s location. 
Your position will require hours of hard work, trai ning, commitment, and sacrifice. The number of hour s you are scheduled 
will be consistent with the needs of the business. Consequently, the number of hours you are scheduled  to work will vary 
from week to week as well as month to month. Your f lexibility, availability, and performance may direc tly impact the number 
of hours you are scheduled. We ask for your underst anding of the fluctuating hours based on business n eeds and we know 
that, with your help, we will succeed both as a tea m and an organization. 
Managers are expected to work a minimum of 37.5 hou rs per week, unless taking time off pursuant to a P olicy in this 
Handbook or the applicable Handbook State Supplemen t. However, in the scope of a Manager’s job expecta tions, work 
beyond 40 in the workweek may also be required. Thi s might include work during evenings and weekends, extended days, 
and travel. Within reason, you are expected to work  as much as you need to get the job done well. 
We also recognize you may need to be away from work  at times to handle personal matters. To the extent  possible, the 
Company will try to work with you in providing some  flexibility in work schedules. Modifying your work  schedule, however, 
should be the exception, not the rule. Please consi der co-workers and operational needs of the Company  when requesting 
a variation to your usual work schedule. You must r eceive advance written approval from your manager p rior to changing 
your regularly scheduled hours.  
TIMEKEEPING FOR NON-EXEMPT (HOURLY) ASSOCIATES 
Reviewing Time Records . You must review your time records at the end of e ach pay period to confirm the records are 
accurate and complete. Changes to time records must  be approved in writing by a manager. 
Section Five: The Workday and Compensation 
Page│ 46  US Store Associate Handbook 
2024 
 Submitting Time Records. You are responsible for ensuring the accuracy of ti me records submitted to the Company. You 
also must maintain and submit time records to the C ompany, following the procedures below. 
Clocking In and Out: 
• Clock in when you arrive at work and begin your wor kday;  
• Clock out at the beginning of a meal break. Clock b ack in after completing the meal break and upon res uming work; 
• Clock out promptly when you stop working; 
• If you work on an electronic or mobile device ( i.e. , computer, tablet, telephone, etc.), you are not p ermitted to use 
the device for work purposes outside of regularly s cheduled work hours, unless you received advance wr itten 
permission from your manager; and 
• If you work (whether on an electronic or mobile dev ice, work-related travel other than your ordinary c ommute, 
attending an off-site training or meeting, or other wise) outside of regularly scheduled work hours or when you are 
not clocked-in (such as if you forget to clock in),  you are responsible for promptly reporting all suc h time to your 
manager. You are responsible for ensuring that all work time is recorded. You must involve your manage r if you are 
ever unsure whether an activity should be recorded as hours worked.  
It Violates This Policy To: 
• Engage in off-the-clock work. This means that you c annot perform work for the Company when you are not  clocked 
in. For example, you should not work during any bre ak, before your scheduled start time, or after your  scheduled 
end time. Off-the-Clock Work is Prohibited ; 
• Over- or under-report hours worked; 
• Fail to review your time records each pay period; 
• Clock in or out for other associates; 
• Instruct others to perform work when they are not c locked-in; 
• Perform work from home or outside the office withou t prior written approval from your manager; 
• Direct or encourage an associate to misrepresent ho urs worked or alter another associate’s time record s; 
• Falsify information or signatures on a time record;  
• Tamper with the Company’s timekeeping system; 
• Leave the office or worksite while clocked-in (unle ss it is during a break); or 
• Earn commissions while off-the-clock.  
Duty to Report. By acknowledging receipt of this Handbook, you agre e to promptly report to Human Resources or another 
member of management if: (a) you believe your time records or paychecks are inaccurate; (b) anyone pre vented you from 
recording all time worked accurately; and (c) if an yone directed or encouraged you to incorrectly repo rt hours worked, not 
record all hours worked in the timekeeping system, to alter another associate’s time records, or to cl ock in or out for another 
associate.  
You must provide Human Resources: (a) your name and  work location; (b) the date(s) and time(s) at issu e; and (c) a brief 
description of the circumstance(s). The Company wil l promptly investigate all such reports and will ta ke corrective action 
Section Five: The Workday and Compensation 
Page│ 47  US Store Associate Handbook 
2024 
 when necessary and adjust your compensation if an e rror occurred. You will not be retaliated against f or making a good-
faith report under this Policy.  
Policy Violations. Following this Policy is critical to ensuring accur ate timekeeping records and compensation. As such, 
failure to comply with the Company’s expectations m ay result in the immediate termination of employmen t. 
Questions. Please discuss questions or concerns regarding this  Policy with Human Resources.  
MEAL AND REST BREAKS  
Because expectations surrounding meal and rest brea ks vary from location to location and change due to  needs of the 
business, please refer to the Meal and Rest Break P olicy in the Handbook Supplement applicable to the state in which you 
work for more information regarding the timing and length of meal and/or rest breaks available to you.  If there is not a 
policy in your Handbook Supplement, consult your ma nager for guidance on meal and rest breaks applicab le to the store in 
which you work. 
BREAKS FOR NURSING/PUMPING MOTHERS 
The Company provides a lactation-friendly environme nt and supports associates who continue to express milk after 
returning to work from having a baby. All associate s are responsible for providing a respectful and su pportive atmosphere 
for breastfeeding associates. Discrimination agains t or harassment of associates who breastfeed is pro hibited and will be 
subject to discipline, up to and including terminat ion.  
The Company will make reasonable efforts to provide  associates with the use of a private room or locat ion other than a 
restroom to express milk. If alternative or additio nal break time is necessary to express milk, please  inform your manager 
or Human Resources of your needs so an arrangement for other reasonable break times can be made. For n on-exempt 
associates, the break time will be unpaid if it can not run concurrently with rest or meal periods. The  Company will not 
discriminate or retaliate against you for exercisin g your right to express breast milk. 
OVERTIME FOR NON-EXEMPT ASSOCIATES 
It is sometimes necessary to work overtime. When ov ertime is necessary, you are expected to cooperate.  You will be paid 
overtime at the rate of one and one-half (1.5) time s your regular rate of pay for all hours worked ove r 40 hours in a 
workweek. If the law of the state in which you work  requires daily overtime, you will be paid consiste nt with state law.  
Overtime must be approved in writing, in advance by  a manager. Anyone working unauthorized overtime wi ll be subject to 
discipline, up to and including termination. Howeve r, all overtime worked must still be recorded, even  if not authorized, and 
you will be paid for all hours worked. 
Pay for Company-recognized holidays and other non-w orking time off is not counted as hours worked for the purpose of 
computing overtime.  
PAYROLL 
Workweek . For purposes of calculating overtime, the Company ’s workweek is defined as hours worked from 6 a.m. Sunday 
through 5:59 a.m. the next Sunday. Work  day is defined as hours between 6:00am-5:59am the n ext day. 
Pay Periods/Paydays . You will typically be paid on a bi-weekly basis f or all work performed through the end of the previo us 
payroll period. If a particular pay day falls on a holiday or a weekend, you normally will be paid on the last business day 
Section Five: The Workday and Compensation 
Page│ 48  US Store Associate Handbook 
2024 
 before the regularly-scheduled payday. You will rec eive information about your rate of pay through you r offer letter and 
your pay rate is printed on each pay statement. Any  question about your pay rate, paid hours, benefit pay, deductions, or 
any other pay issue should first be discussed with your manager. Any pay issue that is not satisfactor ily resolved can be 
escalated to your District Manager. Issues can also  be escalated to Payroll or the One Number (refer t o the Company 
Directory at the beginning of the Handbook for cont act information).  
Methods of Wage Payment . The Company strongly encourages you to enroll in our direct deposit program. Direct deposit 
means that, with your authorization, the Company wi ll deposit your pay directly into the bank account of your choice. On 
paydays, instead of a check, you will receive a det ailed statement explaining how much you were paid a nd itemized 
deductions. If you do not want to be paid via direc t deposit, you will be paid by check or ADP Wisley Pay Card. By signing 
the acknowledgement at the end of this Handbook, yo u consent to opting into the pay card program if yo u do not enroll in 
the Company’s direct deposit program.  
Electronic Records. Electronic pay statements are available on the ADP iPay website at http://ipay.adp.com. In accordance 
with applicable laws, associates in some states can  elect to receive printed pay statements through th e 
http://my.anfcorp.com self-service pages. In such s tates, you have the option to print out pay stateme nts at work.   
REVIEW OF PAY RECORDS  
The Company makes every effort to ensure that all a ssociates are paid correctly. Occasionally, however , inadvertent 
mistakes can happen. When mistakes occur and are br ought to the Company’s attention, we will promptly investigate and 
make necessary corrections.  
Please review your pay stubs to make sure that you were paid correctly each workweek. If you believe a  mistake has 
occurred, if you have questions about deductions fr om our pay, or if you believe wages were improperly  deducted, please 
immediately contact your  District Manager and the One Number at 1-866-367-18 92, and the Company will investigate and 
take necessary remedial action. 
WAGE DEDUCTION ACKNOWLEDGMENT 
The Company is required to make certain deductions from your pay each pay-period, including federal, s tate, and local 
income taxes (as applicable), social security (FICA ) taxes, state disability insurance taxes (as appli cable), and deductions 
required by wage garnishment or child support order s. With your written authorization, other voluntary  deductions such as 
your portion of insurance premiums and 401(k) plan contributions will be made. In addition, exempt ass ociates receive the 
same predetermined amount each pay period, which, a s a general matter, is not subject to deductions ba sed on the quality 
or quantity of the work performed.  
By signing the enclosed Handbook acknowledgement, y ou agree that the Company may also deduct money fro m your pay 
for the additional reasons, such as: 
• Installment payments on loans or wage advances give n to you by the Company. If there is a balance rema ining when 
you leave the Company, the balance of such loans or  advances; 
• If you receive an overpayment of wages, repayment t o the Company of such overpayments (the deduction f or such 
a repayment will be equal to the entire amount of t he overpayment, unless the Company and you agree in  writing 
to a series of smaller deductions in specified amou nts); 
• If you take paid time off or sick leave before the date you would normally be entitled to it and you s eparate from 
the Company before accruing time to cover such adva nce leave, the value of such leave taken in advance  that is not 
so covered; 
Section Five: The Workday and Compensation 
Page│ 49  US Store Associate Handbook 
2024 
 • The value of time off for absences to which paid le ave is not applied; and 
• If the Company pays insurance premiums or retiremen t system contributions on your behalf that you woul d 
normally make under the applicable Company benefit plan, the amount of such payments made by the Compa ny, 
such payments being an advance of future wages. 
EXPENSE AND TRAVEL REIMBURSEMENT 
If you travel during the workday for business-relat ed reasons, you will be reimbursed up to 300 miles at the standard mileage 
rate set by the United States Internal Revenue Serv ice if you complete a mileage reimbursement request . This does not 
include travel commuting to and from the regular wo rk site/home store at the beginning and end of the workday. 
You will also be reimbursed at the standard mileage  rate set by the United States Internal Revenue Ser vice for certain miles 
when borrowed to another store if you complete a mi leage reimbursement request. When you are borrowed to another 
store, you will be reimbursed for all miles that ex ceed the number of miles that you normally travel t o and from your home 
store.  
For example, Associate A normally commutes 30 miles  round trip to and from her home store. In week 1, Associate A is 
borrowed to work in a store that is 60 miles roundt rip from her home. Associate A will receive reimbur sement for 30 miles. 
In week 2, Associate A is borrowed to a store that is 20 miles round trip from her home. Associate A w ill not be reimbursed 
for traveling to the store in week 2. 
You will also be reimbursed for approved business-r elated expenses, such as purchasing supplies. The C ompany will only 
reimburse those expenses that were approved by mana gement prior to purchase.  
Management-level associates may submit reimbursemen ts through the T&E site called Concur using this li nk 
(Travel.anfcorp.com). Associates who are accessing Concur for the first time will need to contact the expense concur team 
at Expense_Concur@anfcorp.com  to get their accounts set up.  
 
All reimbursements should be submitted within fourt een (14) days of the transaction date. Requests sub mitted later than 
that may not be approved. Associates should keep a copy of all their receipts until their reimbursemen t has been paid out. 
Failing to keep receipts could result in their reim bursement being rejected.  
To the extent applicable state law imposes requirem ents that differ from those in this Policy, those r equirements are 
incorporated by reference into this Policy  and may also be reflected in the State specific Han dbook Supplement. 
PERSONAL DEVICE REIMBURSEMENT  
If you incur expenses as the result of using a pers onal device for reasonably necessary business purpo ses, you will be eligible 
for a reimbursement. The amount of that reimburseme nt will vary depending on the associate’s individua l circumstances.  
Personal Device expenses will only be reimbursed if  you if submitted through Concur using this link (T ravel.anfcorp.com). 
Associates who are accessing Concur for the first t ime will need to contact the expense concur team at  
Expense_Concur@anfcorp.com to get their accounts se t up.  
All reimbursements should be submitted within fourt een (14) days of the transaction date or within thi rty (30) days  if the 
charges appear on a monthly invoice. Requests submi tted later than that may not be approved.  Associat es will also need 
receipts that match the total requested to be reimb ursed. Failing to attach a receipt could result in their reimbursement 
Section Five: The Workday and Compensation 
Page│ 50  US Store Associate Handbook 
2024 
 being rejected. Manager creates a claim on “Concur”  within 14 days of the expense, attaching any neces sary and valid 
receipts. If Concur is not established, the manager  may submit paper T&Es (found on the Link) with rec eipts.  
If you are given a Company-issued smartphone or sim ilar device, you are not eligible for reimbursement  for use of a personal 
device.  
To the extent applicable state law imposes requirem ents that differ from those in this Policy, those r equirements are 
incorporated by reference into this Policy  and may also be reflected in the State specific Han dbook Supplement.  
 
INCLEMENT WEATHER 
In the event that severe weather prevents a store f rom opening, a member of store management will make  every possible 
effort to notify the associates scheduled to work t hat day.  
We expect you to adhere to the instructions of Mall  Management and to follow local procedures in the e vent of an 
evacuation. You should contact your next level mana gement if you are unsure whether or not the store s hould be closed. 
PARKING STIPEND POLICY 
If there is not a free parking option at a full-tim e associate’s home store, an associate may seek rei mbursement for the 
lowest reasonable parking amount, at the discretion  of the DM and home office staff. In order to be el igible for this benefit, 
an associate must be full-time and drive to work at  least 80% of the time. Public Transit costs are no t eligible for 
reimbursement.  Parking fees will not be paid in ar rears.  
Associates and their DM are responsible for notifyi ng the home office of any changes to the cost of pa rking, including if 
lower cost parking becomes available.   Also, if th e associate is no longer considered full-time and/o r no longer drives at 
least 80% of the time, it is up to the associate an d DM to communicate those changes to home office.  Failure to report 
changes could result in formal documentation or eve n termination depending on the circumstances. 
 
 
  
 
Section 7: 
Time Away From Work 
  
Section Six: Time Away From Work 
Page│ 52  US Store Associate Handbook 
2024 
 PAID HOLIDAYS 
The following days are considered holidays for the purposes of this Policy. These holidays apply to al l associates unless 
specified below. 
• New Year’s Day 
• Memorial Day 
• July 4th 
• Labor Day 
• Thanksgiving Day 
• Christmas Day 
• Martin Luther King Day  • Presidents’ Day  
• Columbus Day (MA and RI only) 
• Veterans Day (MA and RI only) 
• Victory Day (RI only)  
• Juneteenth 
All non-exempt associates will be paid time and a h alf for all hours worked on the holidays listed abo ve., except holidays not 
applicable to their respective state.  
Pay for a holiday is based on the work  day on which the shift originates, except as otherw ise required by applicable state 
law. Please refer to your specific store for the ho urs that qualify for the holiday premium rate.  
PAID TIME OFF FOR FULL-TIME ASSOCIATES  
Eligibility . This Paid Time Off (“PTO”) Policy applies to full -time associates. 
Amount . Please refer to the PTO Packet for details regard ing the amount of PTO available to you and any appl icable accrual, 
based on your location of employment ( Click here for the PTO Packet ). If you are away from work on an approved leave o f 
absence for more than four weeks, you do not accrue  PTO while you are on leave. 
No Carryover . Unused PTO will not be carried over to the follow ing calendar year unless otherwise required by appl icable 
law. Where carryover is required, carryover is capp ed at 1.5 times the annual accrual total. 
PTO Use . PTO may be used for any purpose, including time off  to relax, travel, personal/family reasons, for doc tor 
appointments, for religious observations, for sick days, and for any other personal reason. You are re quired to use available 
PTO when taking time off from work unless you are r eceiving pay through another benefit (such as short -term disability 
benefits of workers’ compensation) or taking a Comp any-required leave of absence.  
Scheduling . All PTO must be approved in advance by your manager . The approval of PTO requests is based on factors 
including the Company’s operational and staffing ne eds, the date the request was made, and seniority. You should be aware 
that in some cases, PTO requests may not be granted , or the Company may request that you adjust approv ed PTO due to 
business or other needs. If you are requesting PTO for reasons related to sickness or a personal emerg ency and you do not 
know of the need to use PTO in advance, let your ma nager know within one hour of the beginning of your  shift or as soon 
as possible under the circumstances. 
Compensation . PTO is paid at your usual salary or hourly rate a t the time that you take the PTO. Use of PTO is not  considered 
hours worked for purposes of calculating overtime.  
Section Six: Time Away From Work 
Page│ 53  US Store Associate Handbook 
2024 
 Separation of Employment. If you work in a state that requires payout of unus ed PTO upon termination of employment, 
you will be paid for all accrued and unused PTO, re gardless of the reason for the separation. In all o ther states, the Company 
does not pay out unused PTO upon separation of empl oyment. If you have taken PTO beyond the amount acc rued, this will 
be considered an overpayment, and the applicable am ount may be deducted from your final paycheck to re imburse the 
Company, to the extent permitted by and in accordan ce with applicable state law. Details of PTO payout  by location can be 
found in the PTO Packet . 
Notice and Policy Compliance. PTO is a fringe benefit that the Company voluntaril y offers to eligible associates. The 
Company reserves the right to suspend or eliminate the PTO benefit and, therefore, suspend the accrual  and use of PTO, 
for any reason, including, but not limited to, busi ness necessity, and subject to applicable law. In a ddition, the Company 
may mandate or prohibit the use of PTO (including a pproved PTO requests) in certain instances. Specifi cally, once an 
associate has submitted their resignation, PTO will  not be approved during the notice period (typicall y two weeks). 
PAID SICK AND SAFE LEAVE POLICY (PSSL)  
Please refer to both the PTO Packet and applicable State Supplement for information regarding PSSL. If  you work in a location 
that receives paid sick leave, the State Supplement  will provide you with information you need to know  related to the use 
of PSSL  
LEAVES OF ABSENCE  
Please refer to the HR Corkboard in PeopleSoft HR ( https://my.anfcorp.com) – and, if applicable, your State Supplement to 
this Handbook – for details regarding certain types  of leaves of absence not described elsewhere in th is Handbook, 
specifically:  
• Unpaid Leave under the Family Medical Leave Act (“F MLA”);  
• Paid Parental Leave;  
• Paid Caregiver Leave; and  
• Unpaid and/or paid leave under state law.  
UNPAID DISCRETIONARY LEAVE 
Discretionary unpaid leaves are reserved for circum stances in which you are not eligible for other Com pany leave of absence 
and/or have exhausted all other leave entitlements.  For example, if you need time off for a medical re ason, but you do not 
qualify for FMLA leave, you may apply for an unpaid  discretionary leave of absence under this policy. Alternatively, if you 
use your full 12-weeks of FMLA leave, and need addi tional time off work, you may apply for an unpaid d iscretionary leave 
under this policy and/or in conjunction with the Re asonable Accommodation Policy, through which you ma y be approved 
to extend your leave of absence. 
Requesting a Discretionary Leave. You must submit a written request for a leave to Hu man Resources at least 30 days 
before the requested start of the leave, except in cases of emergency, in which case the request shoul d be made as soon as 
possible. Your request should include the dates, pr oposed duration, and general reason for leave. 
Evaluating Leave Requests. Requests are considered based on a variety of busin ess-related factors such as business needs, 
staffing, the reason for the requested leave, your performance , and the anticipated length of the leave. If this l eave is 
requested as a form of an accommodation for medical  reasons, the Company may require submission of med ical 
certifications prior to and during the leave.  
Section Six: Time Away From Work 
Page│ 54  US Store Associate Handbook 
2024 
 PTO During a Discretionary Leave. If you have PTO available, you will be required to use PTO concurrently with an unpaid 
leave provided through this policy.  
Health Insurance Benefits During a Discretionary Le ave . Taking a discretionary leave of absence will like ly impact your 
associate health insurance benefits. If your insura nce benefits continue during your leave, you may be  required to pay the 
full premium of your benefits to maintain your heal th plans. Alternatively, you may become ineligible to participate in the 
Company’s benefit plans, in which case Human Resour ces will notify you when your participation in the Company’s benefit 
plans will end, and when you will become eligible f or continued benefits at your own expense through C OBRA (the 
Consolidated Omnibus Budget Reconciliation Act).  
Short-Term Disability (STD) and Long-Term Disabilit y (LTD) Benefits During a Discretionary Leave. If the reason for the 
discretionary leave of absence is related to a medi cal condition or injury that occurred outside of th e workplace, you may 
be eligible for STD and/or LTD income replacement d uring all or a portion of the discretionary leave o f absence. or a leave 
of absence as a reasonable accommodation. Please re fer to the STD/LTD Policy in this Handbook and the applicable Plan 
documents for additional information; it is your re sponsibility to request STD/LTD benefits. 
Overlap with Statutory Leaves During Discretionary Leave. To the extent you are eligible for family and/or me dical leave 
under a state or local law, leave under this FMLA P olicy will run concurrently with such leave if perm itted under the state 
and/or local law. If you are eligible for disabilit y or paid family leave benefits through an applicab le state program, you must 
apply for such benefits, as permitted by law, as a condition of this policy, by completing applicable paperwork. At the onset 
of a FMLA leave, Human Resources will provide you w ith additional information about the overlap of FML A leave with any 
applicable state or local statutory benefits.  
Outside Employment. Absent approval from Human Resources, if you are on  a leave provided under this Policy, you may 
not maintain employment or otherwise perform unauth orized work for personal financial gain during the leave. 
Returning from Leave. You must return to work when a leave of absence is scheduled to end, or you must obtain an 
approved extension before the scheduled end date of  the leave of absence. The Company will assume that  you resigned 
from employment if you fail to return from a leave of absence or fail to obtain approval for an extens ion. Please note that 
reinstatement is not guaranteed unless required by applicable law. Failure to advise the Company of re turn-to-work plans, 
failure to return to work after notifying the Compa ny of your expected return to work, or remaining ab sent from work 
beyond the time approved by the Company is typicall y considered a voluntary resignation of employment.   
MILITARY LEAVE 
If you are called into active military service or i f you enlist in the uniformed services, you are eli gible to receive a military 
leave of absence in accordance with applicable fede ral and state laws. Additionally, if you are requir ed to attend Reserves 
or National Guard duty, you may apply for an unpaid  temporary military leave of absence not to exceed the number of days 
allowed by law. 
You must provide your manager and Human Resources w ith advanced notice of your service obligations unl ess you are 
prevented from providing such notice due to militar y necessity or it is otherwise impossible or unreas onable to provide such 
notice. Military leave is unpaid, but you may use a vailable paid time off during this time. During you r leave, all benefits are 
governed by the terms and conditions of the applica ble plan documents and law. 
You will retain re-employment rights and accrue sen iority and benefits in accordance with applicable f ederal and state laws. 
Contact Human Resources for additional information about military leave. 
Section Six: Time Away From Work 
Page│ 55  US Store Associate Handbook 
2024 
 BEREAVEMENT LEAVE 
When a death occurs in your immediate family, you m ay take up to four paid days off if you are a full- time associate, or up 
to five days if extended travel is involved (discus s with your manager). Bereavement leave is paid at your usual salary or 
hourly rate at the time of absence for the number o f hours you otherwise would have worked that day. B ereavement leave 
is not counted as hours worked for purposes of calc ulating overtime. 
If you need to take bereavement leave, you must not ify your manager as soon as possible. Bereavement l eave is available 
on the days (and at the time) that you would have o therwise been scheduled to work. The Company may pr ovide additional 
bereavement time off, subject to the approval of Hu man Resources. If you require additional bereavemen t time off, you 
should contact Human Resources. 
For purposes of this policy, an immediate family me mber includes parents, spouse, life partner, childr en, grandparents, 
sisters, brothers, mothers-and-fathers-in-law, sist ers-and-brothers-in-law, or any individual related by blood or affinity 
whose close association with you, the Associate, is  the equivalent of a family relationship.  
 
If you work in a location with a bereavement leave law, refer to the Handbook State Supplement applica ble to the state in 
which you work. To the extent applicable state or l ocal law imposes requirements that differ from thos e in this Policy, the 
policy in the Handbook State Supplement will provid e you with additional information. 
CRIME VICTIM LEAVE & DOMESTIC / SEXUAL VIOLENCE LEA VE 
The Company provides unpaid time off to victims of crimes and domestic/sexual violence. Please refer t o the Handbook 
Supplement applicable to the state in which you wor k for specific information related to eligibility f or leave and requests 
for time off. If there is no specific policy in the  Handbook Supplement, please follow the procedures for requesting time off 
that are described in the Discretionary Leave Polic y or contact Human Resources for additional informa tion. 
VOTING  
Time off to vote is unpaid for non-exempt associate s unless otherwise required by applicable law. Exem pt associates will 
not incur a reduction in pay due to voting time off . To take time off to vote, you must notify your ma nager at least two days 
prior to the election so that the Company can ensur e adequate staffing. 
JURY DUTY  
Jury duty time off is unpaid for part-time associat es unless otherwise required by applicable law. Jur y duty time off is paid 
for full-time associates. Exempt associates will no t incur a reduction in pay for a partial week of ab sence due to jury duty.  
To take time off for jury duty, you must notify you r manager as soon as you receive a jury notice/summ ons from the court 
and provide your manager with a copy of the jury du ty summons. If the required absence presents a seri ous staffing or other 
issue for the Company, we may ask that you attempt to postpone your service.  
During your jury duty service, if you are not requi red to report to court one day or are released earl y, you are required to 
contact your manager as to your availability to wor k. Upon completion of jury duty, you are required t o provide your 
manager with a certification that includes the spec ific dates you served. 
 
 
  
 
 
Section 8: 
Insurance and Other Benefits 
 
Section Seven: Additional Benefits 
Page│ 57  US Store Associate Handbook 
2024 
 OVERVIEW OF BENEFITS 
Employment benefits vary according to the position and employment status. This Handbook provides only a brief description 
of the benefit plans and programs that are currentl y in effect. These descriptions of insurance benefi ts highlight certain 
aspects of the Company’s plans and are provided as general information only. The specific provisions o f the plans, including 
eligibility and benefits provisions, are summarized  in each plan’s summary plan description (“SPD”). T he official plan 
documents are available for review upon request. 
Associates can also find relevant details about ben efits on the Corkboard in your PeopleSoft HR profil e (at 
https://my.anfcorp.com) titled “New Hire & Newly El igible Guide”. Additional documents are also posted  there, including 
details about Leaves of Absence.  
In the determination of benefits or other matters u nder each plan, the terms of the official plan docu ments will govern over 
the language of plan descriptions, including SPDs. Further, the Company and/or the plan administrators  retain full 
discretionary authority to interpret the terms of t he plans as well as discretionary authority with ad ministrative matters 
arising in connection with the plans and all issues  concerning benefit eligibility and entitlement. Th e Company reserves the 
right, in its discretion to modify, change, or elim inate benefits, including but not limited to those described below. 
The A&F benefits package includes the following: 
• PPO Medical Plan; 
• Dental Plan;  
• Vision Plan;  
• Flexible Spending Accounts (FSA);  
• Life Insurance;  
• Short- and Long-Term Disability Plans;  
• Associate Assistance Program;  
• 401(k) Savings Plan;  
• Employee Stock Purchase Plan (ESPP);  
• Headspace (free subscription); and  
• Fertility & Adoption Benefits through Carrot.  
Depending on your role, you may be eligible for add itional benefits beyond what is outlined in this ha ndbook.  
Generally, Associates are eligible after one (1) mo nth of full-time employment, or upon promotion from  part-time to full-
time employment. Review additional details, includi ng eligibility under the Affordable Care Act (“ACA” ) via the materials 
found on the HR Corkboard.  
Associates will enroll for benefits in PeopleSoft H R at https://my.anfcorp.com. 
ASSOCIATE DISCOUNTS AND PERSONAL PURCHASES 
Effective the first day of employment, all associat es including part-time and full-time, management an d non-management 
(“Associates”) of Abercrombie & Fitch Co. entities (“Company”) are eligible to use an Associate discou nt of 40% on the price 
Section Seven: Additional Benefits 
Page│ 58  US Store Associate Handbook 
2024 
 of Company branded merchandise, as outlined below. The discount applies only to the original retail pr ice of the 
merchandise. The discount cannot be applied to temp orarily or permanently reduced prices, including re d-lined and other 
clearance pricing. The Associate will receive which ever price is lower – either 40% off the original r etail price, or the reduced 
price, but not both together. Additional merchandis e may be excluded from the Associate discount from time to time, and 
exclusions will be communicated, as applicable. The  Associate discount is only applicable at stores wi thin the country in 
which the Associate works. 
Discount Restrictions . Associates are encouraged to use their discount b ut may only do so to purchase merchandise for 
personal use or as a genuine gift (i.e., when not r eceiving reimbursement). The discount cannot be use d to purchase gift 
cards. When making purchases, Associates must alway s present their Associate card so that purchases ar e added to their 
Associate purchase log. The Associate discount may never be used by friends or relatives, either direc tly or indirectly. For 
example, if you are shopping with a group of friend s, you may not purchase clothing for them using you r discount. Further, 
the Associate discount may not be exchanged for any thing of value (such as free or discounted items or  services at other 
businesses). Any violation of these rules will lead  to discipline, up to and including termination. 
Each time an Associate makes a purchase, store mana gement must approve the sale. Any tender used for p urchases must 
be in the Associate’s name. A sales receipt must ac company all returns by Associates, and returns must  be made within the 
return period located on the receipt. To prevent ab use of the Associate discount, any Associate may be  questioned about a 
purchase that does not appear to comply with this p olicy. Any violation of these rules will lead to di scipline, up to and 
including termination. 
Associate purchases are typically made before or af ter an Associate’s shift. All store purchases are t o be kept in a place 
specified by the store management for the duration of your shift, and store management will inspect al l Associate 
bags/packages during the walk-out procedure. 
An annual limit of $5,000 USD (or equivalent to $5, 000 USD, as outlined in the below chart) will be im posed for all Associates. 
The limit will reset each fiscal year. 
Merchandise Resale . Associates are strictly prohibited from selling o r reselling, directly or indirectly, any Company br anded 
merchandise. This sale or resale detracts from our brand and constitutes a conflict of interest, as ou tlined in the Abercrombie 
& Fitch Co. Code of Business Conduct & Ethics. Any violation of this rule will lead to discipline, up to and including 
termination. Examples of prohibited behavior includ e but are not limited to:  
• Reselling discounted A&F merchandise, sample sale m erchandise, wear-test merchandise, samples, promoti onal 
items, or any other product received or purchased t hrough any special sale or event; 
• Selling any A&F products on any marketplace website s, for example but not limited to eBay, Facebook Ma rketplace, 
Craigslist, Amazon, Taobao, Mercari, OfferUp, or an y social media platforms; 
• Selling any A&F products at, for example but not li mited to, Plato’s Closet, flea markets, or any othe r type of personal 
transaction; 
• Buying merchandise for people who are not eligible for a discount and receiving reimbursement; 
• Selling any A&F visual displays or any other type o f promotional material; and 
• Returning discounted merchandise for an original pr ice refund or exchange. 
Premium Discount . During certain periods, Associates are eligible t o use a Premium Discount. The Premium Discount is a  
higher-than-normal discount percentage off the orig inal ticket price of qualifying merchandise and exc eeds the regular 40%. 
The Home Office determines the specific discount ra te, the specific items and number of items eligible , and the specific time 
Section Seven: Additional Benefits 
Page│ 59  US Store Associate Handbook 
2024 
 period in which a Premium Discount applies. Unlike the regular Associate Discount, the Premium Discoun t is restricted to 
certain brands, as outlined in the table above. For  further details on the Premium Discount, please sp eak with your Store 
Manager. 
A&F a&f kids Hollister/Gilly Hicks Outlet Stores (any brand) 
Associates working 
at A&F receive the 
Premium Discount 
at A&F only Associates working 
at a&f kids also 
receive the 
Premium Discount 
at the A&F adult 
store Associates working at 
Hollister or Gilly Hicks 
receive the Premium 
Discount at both 
Hollister and Gilly 
Hicks only Associates working in 
outlet locations (any 
brand) will receive the 
Premium Discount at the 
same brand’s full-price 
store 
BRAND LOYALTY PROGRAM 
The Company’s loyalty programs, the A&F Club and Cl ub Cali, are designed to deepen the emotional and t ransactional 
relationship that our customers have with our brand s. The programs track customer transactions and rew ard loyal 
customers with various benefits that include, but a re not limited to, rewards, special promotions, exc lusive experiences, 
and product.  
Associates are welcome to join the Company’s loyalt y programs and there is no cost associated with joi ning but joining is 
also completely voluntary for Associates. If an Ass ociate chooses to join a loyalty program, there are  special rules that apply. 
Associates may not use their loyalty program accoun t for customer purchases to fraudulently accrue poi nts and/or other 
rewards. Associates may only use their loyalty prog ram account for personal purchases in accordance wi th the Associate 
Discount Policy. Associates may not use a personal loyalty program account or a store loyalty program account to 
fraudulently increase a store’s loyalty program com pliance. Any loyalty program account associated wit h fraudulent activity 
will be forfeited and any rewards or benefits assoc iated with that account will be removed. Any violat ion of loyalty program 
rules will lead to discipline, up to and including termination.  
For more information about the Company’s loyalty pr ograms, refer to the A&F Club and Hollister Club Ca li terms and 
conditions available on abercrombie.com and hollist erco.com. 
 
  
 
 
Section 9: 
End of Employment 
Section Nine: End of Employment 
Page│ 61  US Store Associate Handbook 
2024 
 END OF EMPLOYMENT GUIDELINES 
Employment with the Company may end for a variety o f reasons, including: 
• Voluntary Termination (Resignation or Retirement) . If you decide to end your employment with the Com pany or 
will be retiring, we ask that you provide two weeks ’ notice in writing to your manager and Human Resou rces to 
facilitate a smooth transition out of the Company. Failure to provide a two-week written notice may im pact your 
eligibility for re-hire; 
• Job Abandonment . Absent extenuating circumstances (which must be c ommunicated to the Company), if you are 
absent from work for two consecutive workdays witho ut notifying the Company (“no-call/no-show”), you w ill have 
voluntarily abandoned your position with the Compan y, and your employment with the Company will end. I f you 
abandon your job, you are generally ineligible for rehire; and 
• Involuntary Termination . An involuntary termination occurs when the Company decides to end the working 
relationship. 
If you participate in a health or dental insurance plan, you will receive a letter shortly after your separation from the 
Company’s COBRA administrator explaining extended i nsurance coverage and your obligations to maintain those rights. 
The following are additional guidelines that you mu st follow when leaving the Company: 
• You are responsible for returning any Company prope rty ( i.e ., keys, phones, laptops, other electronic 
communication devices, etc.) prior to leaving the C ompany. Failure to return the property may result i n deductions 
from your final paycheck or charges for theft; 
• Regardless of the reason for your separation of emp loyment, you may have ongoing contractual and legal  
obligations to the Company, including but not limit ed to continuing to protect the Company’s 
Proprietary/Confidential/Trade Secret Information a s described in the Confidential Information Policy and any 
separate agreement that you may have signed. If you  have questions about your ongoing confidentiality obligations, 
please contact Human Resources; 
• You must return all materials in your possession or  control that contain Confidential Information or t rade secrets as 
defined in the applicable policy and/or any applica ble stand-alone agreement. Upon the Company’s reque st, you 
must sign a written confirmation that you have comp lied with this obligation; 
• All outstanding and legitimate business expenses mu st be submitted in accordance with the terms of the  Expense 
Reimbursement Policy; and 
 
• If your address and/or contact information changes,  you are responsible for updating that information with 
Human Resources to ensure that important documents can reach you after your separation.  
 
Page│ 62  US Store Associate Handbook 
2024 
 HANDBOOK ACKNOWLEDGMENT 
Please review and sign this Acknowledgement and ret urn it to Human Resources.  
By signing below, I acknowledge that I have receive d and read the Abercrombie & Fitch, Abercrombie kid s, 
HOLLISTER,  GILLY HICKS, and Social Tourist (“the C ompany”) Associate Handbook. I understand the pract ices, policies, 
and procedures described in this Handbook are desig ned to provide a summary of what I can expect from the Company 
and what the Company expects from me. I also unders tand and acknowledge: 
• It is my responsibility to familiarize myself with and understand all information in this Handbook; 
• I agree to comply with the standards of conduct in this Handbook, including, without limitation, the e xpectations 
in the following policies: Discrimination, Harassme nt, and Retaliation Prevention; Attendance; Intimat e 
Relationships at Work; Conduct Outside of Work; Soc ial Media; Internal Reporting Procedures; Confident ial 
Information; Company Investigations; Timekeeping; a nd Health and Safety Policies; 
• I consent to opting into the pay card program if I do not enroll in the Company’s direct deposit progr am; 
• By signing the acknowledgement at the end of this H andbook, I consent to opt into the pay card program  if I do 
not enroll in the Company’s direct deposit program;  
• The Company may discipline me, including terminatio n of my employment, if I violate Company policy; 
• I have a duty to report certain conduct as specifie d in the policies within this Handbook; 
• This Handbook supersedes all previously issued hand books and inconsistent written or verbal policy sta tements 
made or issued before this Handbook; 
• The Company reserves the right to amend, supplement , or rescind the policies described in this Handboo k or to 
modify or deviate from such policies at any time wi thout notice. Delay or failure by the Company to en force a 
policy or does not waive the Company’s right to do so in the future; 
• Neither this Handbook nor any other Company guideli nes, policies, or practices create, or are intended  to create 
a promise or representation of continued employment  or an employment agreement. I understand and agree  that 
I am an at-will associate. The Company or I may ter minate my employment with or without cause and with  or 
without notice, at any time; 
• Currently, I have no employment-related claims of u nlawful conduct pending with the Company or concern s that 
I have not yet raised with a member of management, Human Resources, or the One Number; 
• By accepting and continuing employment with the Com pany, and signing the below, I consent to workplace  
surveillance, as described in this Handbook; 
• Immediately upon the termination of my employment, I must return all Company property, including, but not 
limited to keys, access/ID cards, credit/purchase c ards, cell phones, computers, laptops, tablets or o ther electronic 
devices, software, Confidential Information; and 
• I will contact Human Resources with questions about  this Handbook. 
____________________________________        _______ _______________________________ 
Name (Print)       Signature 
Date _____________________________ 
 
 
  


_______________________
Abercrombie & Fitch Stores Inc.  
US HANDBOOK STATE SUPPLEMENTS  
 
TABLE OF CONTENTS  
Arizona Supplement  
California Supplement  
Colorado Supplement  
Connecticut Supplement  
Delaware Supplement  
District of Columbia Supplement  
Hawaii Supplement  
Illinois Supplement  
Iowa Supplement  
Kentucky Supplement  
Louisiana Supplement  
Maine Supplement  
Maryland Suppleme nt 
Massachusetts Supplement  
Michigan Supplement  
Minnesota  Supplement  
Missouri Supplement  
New Hampshire Supplement  
New Jersey Supplement  
New Mexico Supplement  
New York Supplement  
North Dakota Supplement  
Oregon Supplement  
 Pennsylvania Supplement  
Rhode Island Suppl ement  
South Carolina Supplement  
Tennessee Supplement  
Texas Supplement  
Utah Supplement  
Vermont Supplement  
Virginia Supplement  
Washington Supplement  
West Virginia Supplement  
Wisconsin Supplement  
 
 
 
 
 
 
 
Associate Handbook 
Arizona Supplement  
  

Page | 2 
Arizona Supplement  Arizona Supplement  
This document supplements the Handbook for  Abercrombie & Fitch Co.  referred to as “the Company.”  Abercrombie & 
Fitch Co. is a leading specialty retailer comprised of our brands including Abercrombie & Fitch, abercrombie kids, 
HOLLISTER,  GILLY HICKS, and Social Tourist. In this Handbook  Supplement , “Abercrombie” and “the Company” refers 
generally to all our brands, and particularly to the brand for which you will be working.  
Throughout this Supplement, you are directed to various team members. Their contact information is in the Company -
wide Handbook for ease of reference. If you have concerns, suggestions, or complaints relating to your employment, 
please utilize the reportin g procedures  in the Handbook and this Supplement . 
Time Away From Work  
PAID SICK AND SAFE LEAVE  
For additional information about Paid Sick and Safe Leave (“PSSL”), please view the applicable poster below or contact Human Resources:  
English Poster, 
https://www.azica.gov/sites/default/files/media/AZ%20Earned%20Paid%20Sick%20Time%20Poster%202020%20English
.pdf 
Spanish Poster,  
https://www.azica.gov/sites/default/files/media/EPST%20Poster_SPANISH%202020_0.pdf    
  
Page | 3 
Arizona Supplement  Handbook Supplement Acknowledgment– Arizona  
By signing below, I acknowledge receipt of this Handbook  Supplement “(“Supplement”) . I understand the practices, 
policies, and procedures described in this Supplement and the Handbook together are designed to provide a summary of 
what I can expect from my employer, Abercrombie & Fitch, abercrombie kids, HOLLIST ER,  GILLY HICKS, and Social Tourist 
(referred to as “ the Company”)  and what the Company expects from me. I also understand and acknowledge:  
• It is my responsibility to familiarize myself with and understand all information in this Supplement;  
• The Company m ay discipline me, including termination of my employment, if I violate any Company policy;  
• I have a duty to report certain conduct as specified in the policies within this Supplement; 
• This Supplement supersedes all previously issued supplements and  any inconsistent written or verbal policy 
statements made or issued before this Supplement;  
• The Company reserves the right to amend, supplement, or rescind the policies described in this Supplement or to 
modify or deviate from such policies at any time without no tice. Delay or failure by the Company to enforce a 
policy or rule will not constitute a waiver of the Company’s right to do so in the future; 
• Neither this Supplement nor any other Company guidelines, policies, or practices create, or are intended to create  
a promise or representation of continued employment or an employment agreement. I understand and agree that 
I am employed at -will. The Company or I may terminate my employment with or without cause and with or 
without notice, at any time;  
• At this time, I  have no employment -related claims of unlawful conduct pending with the Company or concerns 
that I have not yet raised with a member of management, Human Resources, or the One Number; and  
• I will contact Human Resources with any questions about this Supplement . 
Signature _________________________________   Date _____________________  
Name ____________________________________ 
 
 
 
 
 
 
Associate Handbook 
California Supplement  

Page | 2 
California Supplement  California Supplement  
This document supplements the Handbook for  Abercrombie & Fitch Co.  referred to as “the Company.”  Abercrombie & 
Fitch Co. is a leading specialty retailer comprised of our brands including Abercrombie & Fitch, abercrombie kids, 
HOLLISTER,  GILLY HICKS, and Social Tourist. In this Handbook  Supplement , “Abercrombie” and “the Company” refers 
generally to all our brands, and particularly to the brand for which you will be working.  
Throughout this Supplement, you are directed to various team members. Their contact information is in the Company -
wide Handbook for ease of reference. If you have concerns, suggestions, or complaints relating to your employment, 
please utilize the reporting procedures  in the Handbook and this Supplement.  
 Inclusive Workplace Policies  
DISCRIMINATION , HARASSMENT , AND RETALIATION PREVENTION POLICY  
This Policy  supplements the Discrimination, Harassment, and Retaliation Prevention Policy in the Handbook . 
The Company is committed to a work environment that respects and includes all associates. In addition, consistent with the Company’s values, you have a right to be free from discrimination, harassment, and retaliation. If you have concerns about unfair treatment, please refer to the Discrimination, Harassment, and Retaliation Prevention Policy in the Handbook  
and Contact the One Number. While we hope that y ou will raise any concerns with us directly so we can promptly 
investigate and resolve the matter, you may also report potential harassment to the Equal Employment Opportunity Commission or the California Department of Fair Employment and Housing. You can find additional information about the illegality of sexual harassment and the remedies available to victims here:  
https://www.dfeh.ca.gov/wp -content/uploads/sites/32/2020/03/SexualHarassmentFactSheet_ENG.pdf
 
Employment Expectations  
CALIFORNIA ASSOCIATE  PRIVACY  
The Company is committed to protecting the privacy and security of your personal information. This California Associate  
& Applicant Privacy Policy describes the personal information the Company collects about you and how we use that information.  
Informati on We Collect About You . The Company collects, maintains, and uses different types of personal information. 
Below are examples of information that the Company may collect about you, as well as an explanation of the primary purpose for the collection and us e of such information. Please note that not all collection categories will apply to your 
employment with the Company.  
CONTEXT  CATEGORIES OF INFORMATION  PRIMARY PURPOSE FOR COLLECTION AND 
USE OF INFORMATION  
Bank Account 
Information  We collect bank account numbers . To ensure that Company cards are only used 
for Company -related purchases.  
Page | 3 
California Supplement  CONTEXT  CATEGORIES OF INFORMATION  PRIMARY PURPOSE FOR COLLECTION AND 
USE OF INFORMATION  
Benefits  Wage and benefit information, such as 
salary, bonus, leave, retirement information, 
and related compensation history and 
benefits information.  To make sure you are paid correctly and to 
retain compensation and benefit records 
consistent with applicable laws.  
Certifications and 
Qualifications  We collect information from people who 
have access to our facilities and equipment, 
including when applicable, l icenses, and 
certifications.  To secure our facilities and equipment and 
track people with access to either for security 
and maintenance purposes. In some 
jurisdictions, we are also required by law to 
validate and record information about the 
individuals that access our facilities and 
equipment.   
Contact Details  Personal contact details such as name, title, 
addresses, telephone numbers, and work 
and personal email address.  To communicate with you and in some cases to 
comply with applicable laws.  
Electronic 
Communications  Information about your use of our 
technology and communication systems.  To monitor your use of our technology and 
communication systems, to ensure the security 
of our IT system, and to ensure compliance 
with Company policies.  
Health Related  Medical information related to time away 
from work for medical or sick -related 
reasons, and information related to requests 
for reasonable accommodations for 
disabilities.  To assess reasonable accommodation requests, 
your ability to perform the  essential functions 
of your position with or without a reasonable 
accommodation, and to manage sickness -
related absences.   
Identification  Name, date of birth, driver’s license, social 
security numbers, taxpayer identification 
numbers, and/or passport information.  To identify you and in some cases to comply 
with the law.  
Investigations  Details of any internal investigations and 
subsequent Company -related actions.  To conduct a prompt, fair, thorough, and 
timely investigation related to possible 
violations of Company policy. To determine 
whether you, or another associate, has 
complied with our policies, procedures, and 
protocols.   
Other Categories of 
Sensitive 
Information  Information about your gender, race and/or 
ethnicity.  To collect EEO -1 reporting information, to 
promote and monitor equal opportunities and 
diversity, to manage or facilitate your 
participation in workplace affinity groups.  
Payroll and Taxes  Payroll information, including but not limited 
to social security number or equivalent, tax 
status information (i.e., marital status, 
dependents, etc.), payroll records, bank 
account details, direct deposit/credit 
arrangements and retirement plan 
contribut ions.  To calculate and pay your salary, tax, social 
security, and any applicable benefit 
contributions. In some cases, to comply with 
legal obligations.  
Page | 4 
California Supplement  CONTEXT  CATEGORIES OF INFORMATION  PRIMARY PURPOSE FOR COLLECTION AND 
USE OF INFORMATION  
Photographs  Photographs.  To maintain external and internal directories 
and/or a security badge (if applicable).  
Recruitment and 
Onboarding  Information to verify your identity by 
completing the I -9 form and supporting 
documentation; references and other 
information included in a CV, resume, or 
cover letter or as part of the application 
process; criminal background; references 
and interview notes; employment offer 
letters, and employment agreements.  To evaluate your eligibility for employment (if 
applicable). As it relates to the I -9 and related 
documentation, to comply with legal 
requirements under the I mmigration Reform 
and Control Act to verify you are legally 
authorized to work in the United States.  
Security Related  Security camera footage or other 
information obtained through electronic 
means.  To protect Company property and maintain 
Company security.  
Terms of 
Employment  Employment records including job 
titles/duties, job location, working 
arrangements, seniority, performance 
ratings, self- assessments, hire/re -hire date, 
termination date, job history, training 
records, professional memberships, and 
business travel records.  To conduct business management and 
planning, including accounting and auditing; 
conducting performance reviews, managing 
performance, and determining performance 
requirements;  making decisions about sa lary 
reviews and compensation; assessing 
qualifications for a particular job or task, 
including decisions about promotions; making 
decisions about your continued employment or 
engagement.  
Training  We collect information concerning the 
training you receive  from us, or from third 
parties.  Understanding and recording the qualifications 
and training of our associates.  We may also be 
required by law, or by contract, to share 
training or qualifications with third parties such 
as regulators or clients (if applicable).  We may 
also choose to share the training or 
qualification of certain staff with third parties.  
Sensitive Information. As outlined above , we collect the following categories of sensitive personal information (as defined 
under California law): Social Security Number, driver’s license or identification number, or passport number; racial or 
ethnic origin; contents of mail, email, and text message s where we are not the intended recipient; and information 
concerning health; and information concerning sexual orientation. This information is collected in order to administer your relationship with us, including fulfilling any obligation that we have to  provide you with compensation and/or 
benefits; determine eligibility for employment; conduct background checks (where permitted by applicable law); comply with applicable laws and regulations; create, maintain, and secure online associate  accounts; busine ss travel; manage and 
monitor associate  access to Company facilities, equipment, and systems; investigate and enforce compliance with and 
potential breaches of the Company’s internal policies and procedures; and exercise or defend our legal rights and the rights of associate s and affiliates, customers, contractors, and agents.  Note that we do not use such information for any 
purposes that are not identified within the California Privacy Rights Act Section 1798.121. We do not “sell” or “share” sensitive pers onal information for purposes of cross -context behavioral advertising.  
Page | 5 
California Supplement  How We Collect Your Personal Information . Most often, we collect personal information from you directly, including 
through the application and recruitment process as well as in the course of your employment or working relationship with 
us. In addition to the information that we collect from you directly, we may also receive information about you from other sources, including third parties, business partners, our affiliates, or publicly available sources. For example, we may 
conduct a background check or collect information from your references or previous employers; you will be provided 
additional information and authorization forms prior to any background check.  
How Else We Use Your Personal Information. In addition to the purposes and uses described  above, we use your personal 
information to:  
• Administer your relationship with us, including fulfilling any obligation to provide you with compensation or benefits.  
• Effectively conduct bus iness.  
• Comply with applicable laws or regulations.  
• Comply with contractual obligations.  
• Detect and prevent fraud or crime.  
• Enforce, exercise, and/or defend legal claims.  
• Investigate potential misconduct, which may include monitoring communications and use of Company IT equipment and systems.  
• Keep your personal information and that of other associates secure and to prevent unauthorized access, loss, damage, destruction, or corruption of data.  
• Protect the interest of our customers, vendors, and other third parties with whom we work.  
Disclosure of Your Personal Information.  The table below describes the categories of personal information collected and 
disclosed for a business purpose. Please note that in addition to the recipients identified below, we m ay also disclose any 
of the categories of personal information we collect with government entities, as may be needed to comply with law or 
prevent illegal activity. We do not use third party cookies or similar tracking technologies that collect data over t ime and 
across different websites for purposes of targeted advertising with our staff.  We do not sell your personal information.  
CATEGORIES OF PERSONAL 
INFORMATION COLLECTED  RECIPIENTS TO WHOM INFORMATION IS DISCLOSED FOR A BUSINESS 
PURPOSE  
Identifiers – this may include real 
name, alias, postal address, unique 
personal identifier, online identifier, 
email address, account name, or 
other similar identifiers.  • Affiliates or subsidiaries  
• Business partners  
• Internet service providers  
• Operating systems and platforms  
• Other Service Providers  
• Payment processors and financial institutions  
• Professional services organizations, this may include auditors and 
law firms  
Government Issued Identification – 
this may inc lude social security 
number, driver’s license number, or • Affiliates or subsidiaries  
• Business partners  
• Internet service providers  
• Other Service Providers  
• Payment processors and financial institutions  
Page | 6 
California Supplement  CATEGORIES OF PERSONAL 
INFORMATION COLLECTED  RECIPIENTS TO WHOM INFORMATION IS DISCLOSED FOR A BUSINESS 
PURPOSE  
state issued identification number, 
passport number.  • Professional services organizations, this may include auditors and 
law firms Operating systems and platforms  
Financial Information – this may 
include bank account number, credit 
card number, debit card number, 
and other financial information.  • Affiliates o r subsidiaries  
• Business partners  
• Other Service Providers  
• Payment processors and financial institutions  
Health Related Information – this 
may include medical information, 
mental or physical condition or 
treatment, or health insurance 
information.  • Affiliates or subsidiaries  
• Business partners  
• Internet service providers  
• Operating systems and platforms  
• Other Service Providers  
• Payment processors and financial institutions  
• Professional services organizations, this may include auditors and 
law firms  
Characteristics of protected 
classifications – this may include 
age, sex, race, ethnicity, physical, or 
mental handicap, etc.  • Affiliates or subsidiaries  
• Business partners  
• Internet service providers  
• Operating systems and platforms  
• Other Service Providers  
• Payment processors and financial institutions  
• Professional services organizations, this may include auditors and 
law firms  
Commercial information – this may 
include information about products 
or services purchased, obtained, or 
considered, or other purchasing or 
consuming histories or tendencies.  • Affiliates or subsidiaries  
• Business partners  
• Internet service providers  
• Operating systems and platforms  
• Other Service Providers  
• Payment processors and financial institutions  
• Profession al services organizations, this may include auditors and 
law firms  
Biometric information – this may 
include imagery of the iris, retina, 
fingerprint, face, hand, palm, vein 
patterns, and voice recordings, from 
which an identifier template, such 
as a faceprint, a minutiae template, 
or a voiceprint, can be extracted, 
and keystroke patterns or rhythms, 
gait patterns, or rhythms, and sleep, 
health, or exercise data that contain 
identifying information  • Affiliates or subsidiaries  
• Business partners  
• Internet service providers  
• Operating systems and platforms  
• Other Service Providers  
• Payment processors and financial institutions  
• Professional services organizations, this may include auditors and 
law firms  
Page | 7 
California Supplement  CATEGORIES OF PERSONAL 
INFORMATION COLLECTED  RECIPIENTS TO WHOM INFORMATION IS DISCLOSED FOR A BUSINESS 
PURPOSE  
Internet or other electronic 
network activity information – this 
may include browsing history, 
search history, and information 
regarding an individual’s interaction 
with an internet website, 
application, or advertisement.  • Affiliates or subsidiaries  
• Busines s partners  
• Internet service providers  
• Operating systems and platforms  
• Other Service Providers  
• Payment processors and financial institutions  
• Professional services organizations, this may include auditors and 
law firms  
Geolocation data  • Affiliates or subsidiaries  
• Business partners  
• Internet service providers  
• Operating systems and platforms  
• Other Service Providers  
• Payment processors and financial institutions  
• Professional services organizations, this may include auditors and 
law firms  
Audio, electronic, visual, thermal, 
olfactory, or similar information • Affiliates or subsidiaries  
• Business partners  
• Internet service providers  
• Operating systems and platforms  
• Other Service Providers  
• Payment processors and financial institutions  
• Profession al services organizations, this may include auditors and 
law firms  
Professional or employment -
related information • Affiliates or subsidiaries  
• Business partners  
• Internet service providers  
• Operating systems and platforms  
• Other Service Providers  
• Payment processors and financial institutions  
• Professional services organizations, this may include auditors and 
law firms  
Non -public education information 
(as defined in the Family 
Educational Rights and Privacy Act)  • Affiliates or subsidiaries  
• Business partners  
• Internet service providers  
• Operating systems and platforms  
• Other Service Providers  
• Payment processors and financial institutions  
• Professional services organizations, this may include auditors and 
law firms  
Inferences drawn from any of the 
information listed above • Affiliates or subsidiaries  
• Business partners  
• Internet service providers  
Page | 8 
California Supplement  CATEGORIES OF PERSONAL 
INFORMATION COLLECTED  RECIPIENTS TO WHOM INFORMATION IS DISCLOSED FOR A BUSINESS 
PURPOSE  
• Operating systems and platforms  
• Other Service Providers  
• Payment processors and financial institutions  
• Professional services organizations, this may include auditors and 
law firms  
Additional categories of personal 
information described in 
the California  Customer Records 
statute  (Cal.  Civ. Code  § 1798.80(e)) 
– this may include signature, 
physical characteristics, or 
description, insurance policy 
number.  • Affiliates or subsidiaries  
• Business partners  
• Internet service providers  
• Operating systems and platforms  
• Other Service Providers  
• Payment processors and financial institutions  
• Professional services organizations, this may include auditors and 
law firms  
Additionally, we may share your information in the following ways: 
• Affiliates and Acquisitions . We may share information with our corporate affiliates ( e.g., parent company, sister 
companies, subsidiaries, joint ventures, or other companies under common control). If another company acquires, 
or plans to acquire, our company, business, or our assets,  we will also share information with that company, 
including at the negotiation stage.  
• Other Disclosures without Your Consent . We may disclose information in response to subpoenas, warrants, or 
court orders, or in connection with any legal process, or to comply with relevant laws. We may also share your information in order to establish or exercise our rights, to defend against a legal claim, to investigate, prevent, or take action regarding possible illegal activities, suspected fraud, safety of person or property, or a violation of our 
policies, or to comply with your request for the shipment of products to or the provision of services by a third -
party intermediary.  
• Service Providers . We may share your information with service providers. Among other things service providers 
may help us to administer our website, conduct surveys, provide technical support, process payments, and assist in the fulfilment of orders.  
• Other Disclosures with Your Consent.  We may disclose your information to other third parties when we have 
your consent or direction to do so.  
Retention of Your Personal Information. We retain your personal information for only as long as necessary to fulfil the purposes outlined in this Policy, including for the purposes of satisfying any legal, ac counting, or reporting requirements, 
unless a longer retention period is required or permitted by law. To determine the appropriate retention period for personal information, we consider the amount, nature and sensitivity of the information, the potential risk of harm from unauthorized use or disclosure of the information, the purposes for which we obtained the information and whether we can achieve those purposes through other means, as well as applicable legal requirements.  
Your choices.  In some circumst ances, you may have the right to make the following choices regarding your personal 
information:  
• Request access to and obtain a copy of the personal information we have about you, or confirmation that we have information about you, including information ab out how we process your personal information;  
Page | 9 
California Supplement  • Request correction (or rectification) of any inaccurate or incomplete personal information we have about you;  
• Request erasure (or deletion) of your personal information, subject to certain limitations and excep tions;  
• Restrict or object to the processing of your personal information under certain circumstances; and  
• If applicable , request to receive access to your personal information in a portable, machine -readable format.  
Please note, not all these rights are absolute, and they do not apply in all circumstances. In some cases, we may limit or 
deny your request. This ma y occur because the law permits or requires us to do so.  
If you want to exercise any of the above rights, please contact Human Resources in writing , or contact us as indicated in 
the “Questions” section below. We do not discriminate against individuals that exercise state- conferred rights. Please 
note that in order to fulfil your request, we may need you to provide certain persona l information to verify your identity. 
We may verify your identity in person, by phone call, or via email. Depending on your request, we will ask for information such as your name, your associate
 ID, or the name of your direct mana ger. We may also ask you to provide a signed and 
declaration confirming your identity.  
You may designate an authorized agent to submit a request on your behalf to access, correct, or delete your personal information. To do so, you must (1) provide that authorized agent written, signed, and notarized permission to submit such request, and (2) verify your own identity directly with us.  
If you are submitting a request on behalf of another person, please  email privacy@anfcorp.com
 or submit a request 
following the instructions under the California Disclosures – CA Privacy Rights section of our website, found here: 
www.abercrombie.com/privacy . You must provide written and notarized proof that you have been authorized by the 
individual to act on his or her behalf.  The associate  can request reasonable reimbursement for the cost of s uch 
notarization.  Please note, we may deny a request from an authorized agent that does not submit proof that they have been authorized to submit such request.  
How We Protect Your Personal Information.  We maintain reasonable physical, technical, and procedural safeguards that 
are appropriate to the sensitivity of the personal information in question. These safeguards are designed to help protect your personal information against loss, unauthorized access or disclosure, modification, or destruction. While w e use 
reasonable efforts to protect your personal information, we cannot guarantee the security of your personal information. In the event that we are required by law to inform you of any privacy or security event relating to your personal information we m ay notify you electronically, in writing, or by telephone, if permitted to do so by law  
Changes to this Policy . The Company may change information collection practices over time.  To the extent that our 
practices materially change, the Policy that was in p lace at the time that you submitted personal information will generally 
govern.  In addition, this Policy may be updated to notify you of additional purposes for which we process your personal 
information.  
Questions. If you have any questions about this Pol icy, please contact the Privacy team at privacy@anfcorp.com
.  If you 
are visually impaired or if you require additional assistance to access this Policy, you may request to have a member of Human Resources read this Policy to you.  
The Workday and Compensation  
MEAL AND REST BREAKS  
This Policy supplements the Meal and Rest Break Policy in the Handbook . 
Page | 10 
California Supplement  This Policy applies to non- exempt associates  only. 
Rest Breaks. If you are a non -exempt associate , you are provided and may take uninterrupted, work -free, and paid breaks 
as described in the chart below. Rest breaks should occur as close to the middle of each four- hour (or major fraction 
thereof) work period as is practicable. For example, if you have  an eight -hour workday, the first rest break should occur 
near your second hour of work, and the second rest break should occur near your sixth hour of work, and the third rest 
break should occur near your tenth hour of work.  
Length of Workday:  Number of Rest Breaks:  
Less than 3.5 hours  None  
At least 3.5 hours, up to 6 hours  One 10 -minute rest break  
More than 6 hours, up to 10 hours  Two 10 -minute rest breaks  
More than 10 hours, up to 14 hours  Three 10 -minute rest breaks  
More than 14 hours, up to 18 hours  Four 10 -minute rest breaks  
More than 18 hours up to 22 hours  Five 10 -minute rest breaks  
Meal Breaks . If you are a non -exempt associate , you are provided the opportunity to and are encouraged and expected 
to take uninterrupted, work -free, and unpaid 30 -minute meal breaks as described in the chart below. You may begin  your 
first meal break no later than before the end of your fifth hour of work. You may begin  your second meal break no later 
than before the end of your tenth hour of work.  
Length of Workday:  Number of Meal Breaks:  
Less than 5 hours  None  
More than 5 hours, up to 10 hours  One 30 -minute meal break  
More than 10 hours, up to 15 hours  Two 30 -minute meal breaks  
More than 15 hours, up to 20 hours  Three 30 -minute meal breaks  
More than 20 hours  Four 30 -minute meal breaks  
Meal Break Waiver . With written approval from Human Resources, you may voluntarily waive meal breaks under the 
circumstances that follow. If you wish to waive a meal break, you must contact Human Resources to obtain and complete 
a waiver form.  
• If your  total work period is more than five, but not  more than six hours, you may voluntarily waive the first meal 
break upon completion of a meal break waiver form; or  
• If your total work period is more than ten, but not more than  more than 12 hours, and if you did not waive the 
first meal break, you may voluntarily waive the second meal break upon completion of a meal break waiver form.  
Page | 11 
California Supplement  Recap of Rest and Meal Breaks: 
If your workday is:  You are authorized, permitted, and expected to take the 
following rest and/or meal breaks (*unless mutually waived): 
At least 3.5 hours, and up to 5 hours  • One 10 -minute paid rest period  
• No meal period  
More than 5 hours, and up to 6 hours  • One 10 -minute paid rest period  
• One 30 -minute unpaid meal period*  
More than 6 hours, and up to 10 hours  • Two 10 -minute paid rest periods  
• One 30 -minute unpaid meal period  
More than 10 hours, and up to 12 hours  • Three 10 -minute paid rest periods  
• Two 30 -minute unpaid meal periods*  
More than 12 hours, and up to 14 hours  • Three 10 -minute paid rest periods  
• Two 30 -minute unpaid meal periods  
Logistics of Meal and Rest Breaks . Within the timeframes noted above, the Company may schedule meal and rest breaks 
to best accommodate operating requirements. If, however, your meal and/or rest breaks are not scheduled in advance, 
please use your best judgment to decide when – within the timeframes noted above  – it is bes t to take your breaks, based 
on your workload and operational demands. Please then attempt to contact your manager before you start your meal and/or rest breaks to help the Company ensure proper staffing. If you cannot connect with your manager, please still proceed with your meal and/or rest breaks. Meal and/or rest breaks should occur away from your work area to the extent possible.  
Recording Meal and Rest Breaks . You must follow the timekeeping procedures set forth in the Timekeeping Policy in the 
Handbo ok. 
No Off -the-Clock Work . During breaks, you are relieved of all work duties and may not perform any work. Working off the 
clock is strictly prohibited. This also means that during breaks, you are not expected to be available to take assignments or respond to work messages such as text messages, telephone calls, or emails.  If you believe that you have been required 
to work during a break, follow the Duty to Report process below.  
Duty to Report . No one  (manager or non -manager) is permitted to prevent or discourage you from taking a break as 
described above. If you believe you were prevented, interrupted, or discouraged from taking all or part of a break as 
provided in this Policy, or if you experience any other circumstances inconsistent with this Policy, yo u have a duty to report 
the circumstances to your General Manager and to the One Number  immediately. You must provide: (1) your name and 
work location; (2) the date(s) and time(s) at issue; and (3) a brief description of the conduct or circumstance(s).  
The Company will promptly investigate all such reports and will take corrective action when necessary to ensure that you 
are provided meal and rest breaks in compliance with this Policy  and that a premium is provided to you if necessary, 
according to California law . You will not be retaliated against for making a good -faith report under this Policy.  
BREAKS FOR NURSING /PUMPING MOTHERS  
This replaces the Breaks for Nursing/Pumping Mothers Policy in the Handbook. 
Page | 12 
California Supplement  The Company supports associates  who choose to breastfeed and/or express breast milk for their infant child(ren) and will 
provide lactation accommodations in accordance with applic able law.  
The Company will provide a reasonable amount of break time for this purpose, which, to the extent possible, will run 
concurrently with other available break times already being provided. Breaks of more than 30 minutes that do not run 
concurrently  with paid rest breaks provided by the Company are unpaid. The Company recognizes that your lactation schedule 
may need to vary over time, and we will do our best to accommodate such needs. We will provide a private location  other 
than a bathroom to expres s breast milk that complies with applicable law.  
To request a lactation accommodation, notify your District Manager or call the One Number. The Company will respond to all 
such requests promptly in writing within five business days.  
The Company will strive to make accommodations in furtherance of this Policy, and if necessary, we will engage in an 
interactive process with you to determine the appropriate break time(s) and/or lactation location. If accommodating your request imposes an undue hardship o n our business, we will provide a written response identifying the basis upon which the 
request is being denied.  
The Company will not retaliate against you for requesting an accommodation under this Policy or otherwise exercising 
rights under applicable law. If you believe you experienced such conduct, you must promptly contact the One Number . 
While we hope you will raise any such concerns with the One Number  to provide the Company an opportunity to respond, 
you also have the right to file a complaint with the Labor Commissioner for any perceived violation of a right under California law. If you have any questions or concerns regarding this Policy, please cont act Human Resources  of the One 
Number . 
PAYROLL  
This Policy supplements the Payroll Policy in the Handbook. 
If you receive your wage statements electronically, you can contact the Payroll Department  to: 
• Obtain a printed copy of any such statement; or  
• Elect  to receive pay statements in writing (instead of electronically).  
Time Away From Work  
DAY OF REST 
The Company will not schedule or require you to work all seven days in a workweek. However, you may choose to work 
seven consecutive days, if, for example, y ou voluntarily pick up an extra shift on a day you were otherwise off work. The 
only exception to the Company’s obligation to provide a day off is if you work: (1) less than six hours in each of the seven 
consecutive days; or (2) less than 30 total hours i n the workweek.  
PAID TIME OFF 
This Policy supplements the Paid Time Off (PTO)  Policy in the Handbook to the extent it provides greater benefits/rights.  
If you do not use all your earned PTO  within the calendar year, it will be carried over from year to year, but only up to a 
maximum of 1.5 times your then -applicable annual accrual. Once this cap on accrual is reached, PTO will stop accruing 
Page | 13 
California Supplement  until you use some PTO time and your balance falls below the cap.  The Company will pay out any accrued but unused PTO 
upon termination of employment, for any reason, in accordance with state law.  
PAID FAMILY LEAVE  
You may apply to the Employment Development Department (“EDD”) for up to eight weeks of paid family care leave for 
the following reasons:  
• Birth of your child or the child of your registered domestic partner;  
• Placement of a child for adoption or foster care with you or your registered domestic partner;  
• To care for a serious health condition affecting your child, parent (or parent -in-law), spouse, registered domestic 
partner, grandparent, grandchild, or sibling; or  
• To participate in a qualifying event because of the military deployment of your spouse, registered domestic 
partner, parent (or pare nt-in-law), or child to a foreign country.  
These benefits are available through the State of California “Paid Family Leave” (“PFL”) program, which is administered by 
the EDD and financed solely through your contributions. That program is solely responsible  for determining if you are 
eligible for such benefits.  
If you need to take time off work for one of the reasons noted above, contact Human Resources for information about 
the EDD’s PFL program and how to apply for benefits. You also may contact your local EDD office for further information.  
You may use paid sick leave and receive PFL benefits at the same time, but the combined benefits cannot exceed 100% of regular earnings, or PFL benefits will be reduced by the amount of paid sick leave paid out. Additio nally, benefits may be 
reduced if you are: (1) working part -time or on an intermittent schedule; or (2) receiving PTO for this purpose pursuant to 
another Company policy.  
If you take time off work in connection with receipt of PFL benefits, you are not gua ranteed job reinstatement unless you 
qualify for such reinstatement under federal or California family and medical leave laws. Any time off for PFL purposes will run concurrently with other leaves of absence, such as FMLA, NPLA, and/or CFRA leave, if applicable and permitted by law. 
PAID PARENTAL LEAVE  
This Policy applies to associates  in San Francisco.  
The Company is committed to providing time off to parents following the birth or adoption of a child. The Company also provides partial wage replacement ben efits (“Supplemental Compensation”) to eligible associates  who are on an approved 
leave of absence for a qualifying reason. If you are eligible, you may receive up to eight weeks of Supplemental Compensation in a 12 -month period.  
Eligible Associates . To be eligible for benefits as described below, you must:  
(1) Be absent from work due to an approved leave of absence for the purpose of bonding with a new child during the first year after birth of the child or placement of the child with you thro ugh foster care or adoption;  
(2) Have worked at least 180 calendar days for the Company before beginning parental leave;  
Page | 14 
California Supplement  (3) Perform at least eight hours of work per week for the Company within the geographic boundaries of the City and 
County of San Francisco;  
(4) Perform at least 40% of your total weekly hours within the geographic boundaries of the City and County of San Francisco;  
(5) Be receiving wage replacement benefits from the State of California’s Paid Family Leave (“PFL”) program for the purpose of bonding wit h a new child;  
(6) Agree to allow the Company to deduct up to two weeks of accrued PTO from your leave bank to offset the cost of 
any Supplemental Compensation benefits; and  
(7) Comply with the procedures for requesting Supplemental Compensation benefits described  below.  
If you do not  meet all the above criteria, you are not eligible to receive Supplemental Compensation under this Policy, but 
you may still be eligible for benefits in accordance with the State of California Paid Family Leave program.  
Supplemental Compensation Benefit . You may receive up to six weeks of supplemental compensation benefits. The 
weekly supplemental compensation benefit is calculated based on your wages and will be calculated in accordance with the applicable ordinance. Unless otherwise p rovided by law, your weekly supplement compensation benefit will be equal 
to the difference between the weekly benefit you receive from the Paid Family Leave program and the weekly wage associated with that Paid Family Leave benefit amount. Supplemental compensation is only available during the period you are eligible for and are receiving weekly Paid Family Leave benefits to bond with a new child.  
Procedure for Receiving Supplemental Compensation. To receive supplemental compensation, you must comply with the following procedures:  
(1) Send an email to  the Benefits Department stating that you understand and agree that up to two weeks of PTO 
will be deducted from your balance to offset the Company’s costs in providing Supplemental Compensation;  
(2) Provide the Compa ny with a copy of your Notice of Computation of California Paid Family Leave Benefits (“Notice”) 
from California’s Employment Development Department (EDD) and provide EDD with permission to share your California PFL weekly benefit amount with the Company;  
(3) Complete and sign the San Francisco Paid Parental Leave Form (“PPL Form”), available here: http://sfgov.org/olse/paid -parental- leave -ordinance
.  The Notice and PPL Form must be submitted within a 
reasonable amount of time following your receipt of the Notice from EDD;  
(4) Notify the Company in writing when you rec eive the first payment from EDD; and 
(5) Submit a copy of the Notice of Payment from EDD to confirm your receipt of PFL benefits.  
If you do not fully comply with these procedures, receipt of supplemental compensation may be delayed or denied. If you complete the above procedures for receiving supplemental compensation prior to or during the period in which you are also receiving Paid Family Leave benefits, the Company will make a good faith effort to make the first Supplemental Compensation benefit payment on t he first pay period after you satisfy the above procedures. If you do not satisfy the 
above procedures until after the period in which you received Paid Family Leave benefits has been completed, you will receive the total Supplemental Compensation no later  than 30 days after satisfaction of the above procedures.  
You may be required to reimburse the Company for any supplemental Compensation benefits provided under this Policy if you: (1) do not return to work from a leave of absence during which you received  supplemental compensation benefits; 
or (2) voluntarily resign from employment within 90 days of the end of any leave during which you received supplemental compensation benefits.  
Page | 15 
California Supplement  No Retaliation. The Company will not retaliate against you for requesting a leave under this Policy. If you believe you were 
retaliated against, promptly contact  the One Number . 
PAID SICK AND SAFE LEAVE  
For additional information about Paid Sick and Safe Leave (“PSSL”), please view the applicable poster below or contact 
Human Resources:  
State of California:  
English Poster,  
https://www.dir.ca.gov/DLSE/Publications/Paid_Sick_Days_Poster_Template_(11_2014).pdf  
Spanish Poster,  
https://www.dir.ca. gov/dlse/Publications/Paid_Sick_Days_Poster_Template_Spanish.pdf  
Berkeley:  
English Poster,  
https:/ /berkeleyca.gov/sites/default/files/2022 -04/English%20 -%20MWO -and-Labor -Notice -Multi -year%20FY23.pdf  
Spanish Poster,  
https://berkeleyca.gov/sites/default/files/2022 -04/Spanish%20MWO -and-Labor -Notice -Multi -year%20FY23.pdf  
Emeryville:  
English Poster,  
https://www.ci.emeryville.ca.us/DocumentCenter/View/14155/MWO- PSL-Workplace -Poster -English   
Spanish Poster,  
https://www.ci.emeryville.ca.us/DocumentCenter/View/14154/MWO- PSL-Workplace -Poster -2022 -SPANISH   
Los Angeles:  
English Poster,  
https://wagesla.lacity.org/sites/g/files/wph1941/files/2022 -02/2022- MWO -Poster -EN-11.pdf  
Spanish Post er, 
https://wagesla.lacity.org/sites/g/files/wph1941/files/2022 -02/2022- MWO -Poster -SP-11.pdf  
Oakland:  
English Poster ,  
https://cao -94612.s3.amazonaws.com/documents/Measure_FF_English_Poster_Set_2022.pdf  
Spanish Poster,  
https://cao -94612.s3.amazonaws.com/documents/Measure_FF_Spanish_Poster_Set_2022.pdf  
San Diego: 
English Poster,  
https://www.sandiego.gov/sites/default/files/esl_notice_english.pdf  
Spanish Poster,  
https://www.sandiego.gov/sites/default/files/esl_notice_spanish.pdf  
San Francisco: 
Page | 16 
California Supplement  Multilingual Poster,  
https://sfgov.org/olse/sites/default/files/Document/Paid%20Sick%20Leave%20Poster%20 -%20Post.pdf  
Santa Monica: 
English Poster,  
https://santamonica.gov/media/Minimum_Wage/22 -23_Notification_English.pdf  
Spanish Poster,  
https://santamonica.gov/media/Minimum_Wage/22 -23_Notification_Spanish.pdf  
West Hollywood: 
English Poster,  
https://www.weho.org/home/showpublisheddocument/53021/637872784267800000  
Spanish Poster,  
https://www.weho.org/home/showpublisheddocument/53017/637872784259370000  
PREGNANCY DISABILITY LEAVE  
This Policy supplements the Reasonable Accommodations for Disabilities Policy in the Handbook . 
Eligibility. The Company is committed to providing time off to pregnant associates and those exper iencing related medical 
conditions. If you are disabled by pregnancy, childbirth, or a related medical condition (including medical conditions 
relating to lactation), you are eligible for up to four months of unpaid Pregnancy Disability leave per pregnancy . 
Compensation and Use of Leave . Leave under this Policy is unpaid. You may use available paid sick and safe leave or other 
PTO benefits during the unpaid leave of absence.  
Use of Pregnancy Disability Leave. If you are also eligible for leave under the federal Family and Medical Leave Policy , the 
FMLA leave and the Pregnancy Disability leave will run concurrently. If you are eligible for California’s Family Rights Act (“CFRA”) leave, you may take both a Pregna ncy Disability leave and a CFRA leave for the birth of a child. When medically 
necessary, leave may be taken on an intermittent or reduced work schedule. If you are taking a leave for the birth, adoption, or foster care placement of a child, the basic minimum duration of the leave is two weeks, and you must conclude the leave within one year of the birth or placement for adoption or foster care.  
Requesting Time Off . If possible, you must provide 30 days' advance notice to  the Benefits Department and to your  
manager requesting a Pregnancy Disability leave for foreseeable events such as the birth of a child or a planned medical 
treatment. For events that are unforeseeable, we ask that you notify us as soon as you learn of the need for the leave. The Company ma y require certification from a healthcare provider.  
Benefits Continuation.  Taking a leave under this Policy may impact certain benefits and your seniority date. If you want 
more information regarding the impact of leave on your seniority and benefits, please contact the Benefits Department. 
Reinstatement.  Following a Pregnancy Disability leave, the Company will reinstate you to the same position when 
possible.  
No Retaliation. The Company will not retaliate against an  associate for requesting a leave under this Policy. If you believe 
you were retaliated against, promptly notify your manager, the next level of management, Human Resources, or the One 
Number . 
Page | 17 
California Supplement  FAMILY AND MEDICAL  LEAVE 
The Company provides leave to eligible associates in California under the California Family Rights Act (“CFRA”), which is 
like the leave provided under the Family and Medical Leave Policy in the HR Corkboard in PeopleSoft HR 
(https://my.anfcorp.com ). To the extent you qualify for both leaves, they will run concurrently, to the maximum extent 
permitted by law. Questions concerning CFRA leave should be directed to the Benefits Department . 
Eligibility. Under CFRA, you may have a right to an unpaid family care or medical leave (CFRA leave) if you:  
(1) Worked for the Company for a total of at least 12 months prior to the commencement of a CFRA leave; and  
(2) Worked for the Company for at least 1,250 hours in the 12 -month period before the date you want to begin CFRA 
leave (to the extent permitted by applicable law).  
Basic Family and Medical Leave Entitlement . FMLA provides eligible associates  up to 12 workweeks of unpaid leave for 
certain family and medical reasons during a 12 -month period. CFRA leave may be up to 12 workweeks in a 12 -month 
period and can be used for the birth, adoption, or foster care placement of a child; your own serious health condition 
(except that leave for your disability due to pregnancy, childbirth or related medical condition does not count toward CFRA entitlement); or the serious health condition of your child, parent, parent -in-law, spouse, domestic partner, sibling , 
grandchild, or grandparent (“covered family member”). If you are CFRA -eligible, you have certain rights to take both a 
pregnancy disability leave (“PDL”) and a CFRA leave for reason of the birth of a child.  
Qualifying Military Exigency Leave Entitlement . Under the FMLA and CFRA, you can use your 12 -workweek leave 
entitlement for a “qualifying exigency” related to the covered active duty or call to covered active duty of your spouse, child, or parent in the U.S. Armed Forces. CFRA also provides use of qualifying exigency leave in connection with a domestic partner in the U.S. Armed Forces.  
Bonding Leave . You may take intermittent leave for bonding with a child following birth or placement for adoption or 
foster care. Bonding leave must be taken within one year after the child’s birth or placement.  Intermittent leave for 
bonding purposes generally must be taken in two -week increments, but the Company permits two occasions where the 
leave may be for less than two weeks.  Bonding leave is in addition to time off taken for pregnancy disability leave.  
Definition of Serious Health Condition. Under the FMLA and CFRA, a serious health condition is an illness, injury (including, but not limited to, on -the-job injuries), impairment, or physical or mental condition that involves either inpatient care or 
continuing treatment, including but not lim ited to, treatment for substance abuse. Unlike the FMLA, “inpatient care” 
under the CFRA is more broadly defined and means a stay in a hospital, hospice, or residential healthcare facility, subsequent treatment in connection with inpatient care, or a perio d of incapacity. You will be considered an “inpatient” 
when a heath care facility formally admits you to the facility with the expectation that you will remain at least overnight and occupy a bed, even if it later develops that you can be discharged or tra nsferred to another facility and does not 
actually remain overnight.  
Your Responsibilities . If possible, you must provide at least 30 days advance notice for foreseeable events such as the 
expected birth of a child, your own planned medical treatments, or a family member’s planned medical treatment. For unforeseeable events, the Company requires that you provide notice the Benefits Department  and Sedgwick CMS (refer 
to the Company Directory)  as soon as  you learn of the need for leave. Failure to comply with  these notice rules is grounds 
for, and may result in, deferral of the requested leave until compliance with this notice is achieved.  
Page | 18 
California Supplement  We may require certification from a healthcare provider before allowing leave to be taken for: (1) pregnancy disability or  
a serious health condition; or (2) a covered family member who has a serious health condition. When medically necessary, 
leave may be taken on an intermittent or reduced work schedule.  
We will require second or third certifications from healthcare provide rs only in the event the Company has reason to 
doubt the initial certification of your need for leave due to your own serious health condition. Recertification of the need for leave due to your serious health condition or a family member’s serious health c ondition will be requested only when 
the original certification has expired.  
Substitution of Paid Leave for Unpaid Leave . If CFRA leave is unpaid, we require that you use available PTO  benefits, 
including paid sick leave, to the maximum extent permitted by law. CFRA leave is paid if you are receiving compensation 
from the State of California under the State Disability Insurance program. CFRA leave is also paid if you are receiving Paid 
Family Leave, workers’ compensation, or benefits pursuant to the Company’s disability pay program. In these instances, you may -but are not required to - use accrued PTO  benefits or paid sick leave. Substituting paid for unpaid leave does not 
extend leave en titlements.  
Job Benefits . Taking CFRA leave or PDL may impact certain benefits and your seniority date. More information regarding 
eligibility for a leave and/or the impact of the leave on seniority and benefits can be obtained by contacting the Benefits Hotline . 
Returning to Work . At the end of CFRA leave, you are eligible for reinstatement to the same or to a comparable position 
(subject to defense s allowed under the law). If your anticipated return to work date changes and it becomes necessary to 
take a different length of leave  than originally anticipated, you must provide the Company with reasonable notice ( i.e., 
within two business days) of the changed circumstances and a new return to work date. If you give the Company unequivocal notice of your inten t not to return to work, you will be considered to have voluntarily resigned, and the 
Company’s obligation to maintain health benefits (subject to COBRA requirements)  and to job restoration, will cease.  
Reporting Procedures . We encourage you to promptly contact the Benefits Hotline if you have questions about this Policy . 
If you  believe that this Policy was not followed , promptly contact Human Resources or the One Number . If possible, 
document the surrounding circumstances. If you are a manager and you le arn of an associate’s  concern about conduct in 
violation of this Policy , whether informally or through a formal complaint, you must immediately report it to Human 
Resources  or the One Number . 
Investigation. When you disclose conduct you believe violates th is Policy , we will undertake a prompt, fair, and thorough 
investigation appropriate to the circumstances . We strive to maintain confidentiality throughout the investigative process 
to the extent practicable. However, our duty to investigate and take correc tive action may require the disclosure of 
information, and therefore, confidentiality cannot be guaranteed. We will, of course, only disclose what is necessary to facilitate a prompt, fair, and thorough investigation. Upon completion of the investigation, we will evaluate the information gathered and take remedial, corrective, and/or disciplinary action as necessary.  
Page | 19 
California Supplement  PAID TIME OFF CARRYOVER  
This Policy supplements the Paid Time Off (PTO) Policy in the Handbook. Please note, the information regarding 
carryover of PTO in the Handbook does not apply to you.  
If you do not use all your earned PTO  within the calendar year, you may carry it over, up to a maximum overall accrual of 
1.5 times the applicable maximum accrual cap set forth in the Handbook (“accrual cap”). For example, if your maximum accrual cap is 15 days, your accrual cap is 22.5 days.  Once this accrual cap is reached, PTO  will stop accruing until you use 
PTO, and your balance falls below the accrual cap.  
Any accrued, unused PTO  will be paid out at separation from employment.  
LEAVE FOR VICTIMS OF VIOLENCE  
The Company is committed to yo ur health and safety. Should you or your family member be a victim of domestic violence 
or other similarly abusive behavior, promptly  communicate with  your manager and  the Benefits Department if you need 
to take a leave of absence or seek other support. If  you need more time off than is provided in this Policy, please contact 
the Benefits Department . 
Notice and Documentation Requirements. If you need to take time off under this Policy, you must notify your manager and the Benefits Department  as soon as possible. Whenever possible, you should also include the expected duration of 
the absence. If the need for leave is foreseeable, we ask that you make a reasonable effort to take time off in a manner that does not unduly disrupt our operations. You are not requ ired to look for or secure a replacement to cover work hours. 
The Company may require you to provide reasonable documentation supporting the reason for the leave. Documentation may include, for example, a court appearance ticket or subpoena, a police report, an affidavit/letter from an attorney involved in the court proceeding, or an affidavit/letter from a social worker or other organization providing you with related assistance.  
No Retaliation. The Company will not retaliate against an associate for reque sting a leave under this Policy. If you believe 
you were retaliated against, promptly contact the One Number.  
MILITARY LEAVE 
The Company recognizes that you may need to be absent from work to serve in the military. If you need a related leave of absence, please refer to the Military Leave  Policy in  the Handbook . In addition, under the FMLA and CFRA, you may use 
your 12- workweek leave entitlement for a “qualifying exigency” related to the covered active duty or call to covered active 
duty of your s pouse, child, or parent in the U.S. Armed Forces. CFRA also provides use of qualifying exigency leave in 
connection with a domestic partner in the U.S. Armed Forces.  
SUPPLEMENTAL BEREAVEMENT LEAVE  
Bereavement leave through this Policy runs concurrently wit h time off under the Bereavement Leave Policy .  
When a death of a family member occurs, you may take up to five days of unpaid bereavement leave. Bereavement leave  
is used concurrently with available PTO. 
Page | 20 
California Supplement  If you need to take bereavement leave, you must notify your manager as soon as possible. Bereavement leave is available 
on the days (and at the time) that you would have otherwise been scheduled to work and must be used within three 
months of the family member’s death.  
For purposes of this Policy, a “family member” includes a spouse or a child, parent, sibling, grandparent, grandchild, domestic partner, or parent -in-law. 
The Company may provide additional bereavement time off, subject to the approval of the department manager and Human Resources. If you require additional bereavement time off, promptly notify Human Resources.  
Health and Safety  
PROPOSITION 65 WARNING  
Proposition 65 requires the Company to notify you about significant amounts of chemicals in the products that you may be exposed to in the wo rkplace. The list contains a wide range of naturally occurring and synthetic chemicals that are 
known to cause cancer or birth defects. These chemicals include additives or ingredients in pesticides, common household products, food, drugs, dyes, vehicle fu el, and/or solvents. The list is updated annually by the State of California and can be 
found either online or by contacting a manager.  
Consequently, the Company provides a “clear and reasonable” warning that, in the course of your normal employment, 
you m ay encounter  certain chemicals known to the State of California that may cause cancer, birth defects, or other 
reproductive harm.  
SUITABLE SEATS 
You will be provided with a suitable seat when the nature of your work reasonably permits the use of a seat. Wh en you 
are not engaged in active work duties, and the nature of your work requires standing, an adequate number of suitable seats will be placed in reasonable proximity to the work area, and you are permitted to use such seats when sitting does 
not interfere with the performance of your duties.  
If you believe suitable seats are not being provided, please immediately contact the One Number , so the Company can 
determine whether the nature of your work reasonably permits the use of seats or requires standing, and whether sitting interferes with the performance of your work duties.   
Page | 21 
California Supplement  Handbook Supplement  Acknowledgment–California 
By signing below, I acknowledge receipt of  this Handbook Supplement. I understand the practices, policies, and 
procedures described in this Supplement  and the Handbook together  are designed to provide a summary of what I can 
expect from my employer, Abercrombie & Fitch, abercrombie kids, HOLLISTER,  GILLY HICKS, and Social Tourist ( referred 
to as “the Company”) the Company an d what the Company expects from me. I also understand and acknowledge: 
• It is my responsibility to familiarize myself with and understand all information in this Supplement;  
• I agree to comply with the standards of conduct in this Supplement; 
• The Company may  discipline me, including termination of my employment, if I violate any Company policy;  
• I acknowledge receipt of the California Department of Fair Employment & Housing’s brochure entitled Sexual 
Harassment, The Facts About Sexual Harassment;  
• I have a duty  to report certain conduct as specified in the policies within this Supplement;  
• This Supplement supersedes all previously issued supplements and any inconsistent written or verbal policy 
statements made or issued before this Supplement;  
• The Company reserves the right to amend, supplement, or rescind the policies described in this Supplement or to 
modify or deviate from such policies at any time without notice. Delay or failure by the Company to enforce a 
policy or rule will not constitute a waiver of the Co mpany’s right to do so in the future;  
• Neither this Supplement nor any other Company guidelines, policies, or practices create, or are intended to create 
a promise or representation of continued employment or an employment agreement. I understand and agree that 
I am employed at -will. The Company or I may terminate my employment with or without cause and with or 
without notice, at any time;  
• At this time, I have no employment -related claims of unlawful conduct pending with the Company or concerns 
that I have not yet raised with a member of management, Human Resources, or the One Number; and  
• I will contact Human Resources with any questions about this Supplement . 
Signature _________________________________   Date _____________________  
Name ____________________________________ 
 
  
 
 
 
  
Associate Handbook 
Colorado Supplement  
 
 
  

Page | 2 
Colorado Supplement  Colorado Supplement  
This document supplements the Handbook for  Abercrombie & Fitch Co.  referred to as “the Company.”  Abercrombie & 
Fitch Co. is a leading specialty retailer comprised of our brands including Abercrombie & Fitch, abercrombie kids, 
HOLLISTER,  GILLY HICKS, and Social Tourist. In this Handbook  Supplement , “Abercrombie” and “the Company” refers 
generally to all our brands, and particularly to the brand for which you will be working.  
Throughout this Supplement, you are directed to various team members. Their contact information is in the Company -
wide Handbook for ease of reference. If you have concerns, suggestions, or complaints relating to your employment, 
please utilize the reporting procedures  in the Handbook and this Supplement.  
Inclusive Workplace Policies  
PREGNANCY  ACCOMMODATIONS AND PREGNANCY DISCRIMINATION , HARASSMENT , AND RETALIATION 
PREVENTION  
This Policy supplements the Reasonable Accommodations  for Disabilities and the Discrimination, Harassment, and 
Retaliation Prevention Policies in the Handbook.  
Consistent with the Company’s values and in compliance with the Colorado Pregnant Workers Fairness Act, you have a 
right to be free from discrimination and unfair employment practices because of pregnancy, childbirth, or related conditions. The Company is committed t o providing reasonable accommodations for known limitations related to 
pregnancy. If you need a reasonable accommodation or if you have concerns about unfair treatment, please refer to the Reasonable Accommodations for Disabilities and the Discrimination, Harassment, and Retaliation Prevention Policies in the Handbook and/or notify the One Number . You may also view additional information about the Pregnant Workers 
Fairness Act, available here:  
https://www.colorado.gov/pacific/sites/default/files/CCRD%20Notice%20re%20Pregnant%20Workers%20Fairness%20A
ct%20%282%29.pdf  
The Workday and Compen sation  
MEAL AND REST BREAKS  
This Policy supplements the Meal and Rest Break Policy in the Handbook.  
This Policy applies to non- exempt associate s only. 
Rest Breaks. If you are a non -exempt associate , you are provided and may take uninterrupted, work -free, and paid breaks 
as described in the chart below. Rest breaks should occur as close to the middle of each four -hour work period as 
practicable.  
Length of Workday:  Number of Rest Breaks:  
Less than 2 hours  None  
More than 2 hours, up to 6 hours  One 10-minute rest break  
Page | 3 
Colorado Supplement  More than 6 hours, up to 10 hours  Two 10-minute rest breaks  
More than 10 hours, up to 14 hours  Three 1 0-minute rest breaks  
More than 14 hours  Four 1 0-minute rest breaks  
Meal Breaks. If you are a non -exempt associate  and work five or more hours during the workday, you are provided and 
may take an uninterrupted, work -free, and unpaid 30 -minute meal break . To the extent practical, the break should occur 
at least one hour aft er the start of your workday and one hour before the end of your workday.  
Working Through a Meal Break . If the nature of business activity or other circumstances make a meal break impractical, 
you may consume an on -duty meal break. If this occurs, please contact Human Resources to ensure the break is properly 
documented.  
Logistics of Meal and Rest Breaks . Within the required window, the Company may schedule meal and rest breaks to best 
accommodate operating requirements. If, however, a meal or rest break is not scheduled in advance, please use your best 
judgment to decide when – within the required window – it is best to take your breaks, based on your workload and 
operational demands. Please then attempt to contact your manager before you start your  meal and/or rest breaks to help 
the Company ensure proper staffing. If you cannot connect with your manager, please still proceed with your meal and/or rest break. Meal and/or rest breaks should occur away from your work area to the extent possible.  
Recor ding Meal and Rest Breaks . You must follow the timekeeping procedures set forth in the Timekeeping Policy in the 
Handbook.  
No Off -the-Clock Work. During breaks, you are relieved of all work duties and may not perform any work. Working off the 
clock is strictly prohibited. This also means that during breaks, you are not expected to be available to take assignments or respond to work messages such as text messages, telephone calls, or emails.  
Duty to Report . No one (manager or non -manager) is permitted to prevent or discourage you from taking a break as 
described above. If you believe you were prevented, interrupted, or discouraged from taking all or part of any break as provided in this Policy, or if you experience other circumstances inconsistent with this P olicy, you have a duty to report 
the circumstances to the One Number  immediately. You must provide: (1) your name and work location; (2) the date(s) 
and time(s) at issue; and (3) a brief description of the conduct or circumstance(s).  
The Company will promp tly investigate all such reports and will take corrective action when necessary to ensure that you 
are provided meal and rest breaks in compliance with this Policy. You will not be retaliated against for making a good -faith 
report under this Policy.  
Time Away From Work and Benefits  
PAID TIME OFF CARRYOVER  
This Policy supplements the Paid Time Off (PTO) Policy in the Handbook. Please note, the information regarding carryover of PTO in the Handbook does not apply to you.  
If you do not use all your earned PTO within the calendar year, you may carry it over to the following year. However, your 
PTO accrual remains subject to the applicable cap set forth in the Handbook. Once this cap on accrual is reached, PTO will 
stop accru ing until you use PTO, and your balance falls below the accrual cap.  
Page | 4 
Colorado Supplement  Any accrued, unused PTO will be paid out at separation from employment.  
PAID SICK AND SAFE LEAVE  
For additional information about Paid Sick and Safe Leave (“PSSL”), please view the applicable poster below or contact 
Human Resources:  
English Poster, 
https://cdle.colorado.gov/sites/cdle/files/%5BCLEAN%20June%201%2C%202022%5D%20Poster%2C%20Paid%20Leave%
20%26%20Whistleblower.pdf  
Spanish Poster, 
https://cdle.colorado.gov/sites/cdle/files/Poster%2C%20Paid%20Leave%20%26%20Whistleblower%20%5BCLEAN%20Ju
ne%201%2C%202022%5D_SPANISH.pdf  
FAMILY LEAVE 
We are committed to providing time off to associates  for family and medical reasons. Please refer to the Family and 
Medical Leave Policy in the HR Corkboard in PeopleSoft HR ( https://my.anfcorp.com )for more information about the 
Company’s leave -related benefits. The Company also provides leave to eligible associates  under the Colorado Family Care 
Leave Act (“CFCLA”).  
In addition to the qualifying reasons for leave as listed in the Family and Medical Leave Policy in the HR Corkboard in PeopleSoft HR ( https://my.anfcorp.com
), if you are an eligible associate, you may take CFCLA leave if you are in a 
registered domestic partnership or a civil union to care for your domestic or civil union partner with a serious health condition. If you are seeking leave under this Policy, you must comply with the eligibility, notice, certification, and other requirements set forth in the Family and Medical Leave Policy in the HR Corkboard in PeopleSoft HR (
https://my.anfcorp.com ). 
The Company will not retaliate against an associate  for requesting a leave under this Policy. If you believe you were 
retaliated against, promptly contact  the One Number . 
PAY CONTINUATION DURING FAMILY AND MEDICAL LEAVE 
Eligibility for Compensation Replace ment Begins January 1, 2024: Starting in 2024, if you are on a Company approved 
leave of absence for one of the Qualifying Reasons below, and after you have earned $2,500 in total wages, you will be eligible for paid leave benefits through the state’s Family and Medical Leave Insurance (FAMLI) Program. To receive the paid leave benefits, you must apply – and be approved for – a leave of absence by  following the procedures in the 
applicable Company Handbook policy  or in the HR Corkboard in PeopleSoft HR ( https://my.anfcorp.com
).  
Qualifying Reasons: Eligible employees may receive FAMLI benefits for the following Qualifying Reasons: 
• Caring for a new child during the first year after the birth, adoption, or foster care placement of the child;  
• Caring for a family member with a serious health condition;  
• Caring for your own serious health condition;  
• Making arrangements for a family member’s military deployment;  
Page | 5 
Colorado Supplement  • Obtaining s afe housing, care, and/or legal assistance in response to domestic violence, stalking, sexual assault, or 
sexual abuse.  
For purposes of this policy, a “family member” includes your child, parent, spouse, domestic partner, grandparent, 
grandchild, sibling, or any individual with whom you have a significant personal bond that is like a family relationship.  
Wage Replacement Benefit.  You may receive up to 12 weeks of FAMLI benefits per year, or up to 16 weeks of FAMLI 
benefits if the reason for the leave is due  to a serious health condition related to pregnancy or childbirth complications. 
The benefits through the FAMLI Program, which are funded through employee payroll contributions and potentially employer contributions (as described below), will provide you w ith up to 90% of your average weekly wage, based on a 
sliding scale. You may estimate your benefits by using the benefits calculator available at fmli.colorado.gov. Instructions on how to apply for benefits will be available on fmli.colorado.gov in the last quarter of 2023. You or your designated representative may apply for FAMLI benefits by applying and submitting the required documentation directly to the FAMLI Division. Any appeals to the determination should be submitted to the FAMLI Division, not the Company. The FAMLI Division indicates it will issue the compensation benefits within two weeks after the FAMLI Division approves a claim, and every two weeks thereafter, for the duration of the approved leave.  
Automatic Payroll Deduction. The Company automatically deducts 0.45% of your paycheck and contributes it to the 
FAMLI Program. The Company also contributes an additional 0.45% of wages to the FAMLI Program, for a total contribution of .09%.  
Overlap With Other Policies . To the extent legally permitted: you must follow the leave of absence procedures outlined 
in the applicable leave policy in the Handbook  or in the HR Corkboard in PeopleSoft HR ( https://my.anfcorp.com
); and 
benefits provided through this Policy will run concurrently with other benefits provided by the Company.  
Additional Information.  The Company will not retaliate against you for exercising your right to apply for and receive FAMLI 
benefits. For additional information about the FAMLI Program, please visit the website below:  
https://famli.colorado.gov/sites/famli/files/FAMLI%20Break%20Room%20Poster%20Officialv3.pdf   
 
  
Page | 6 
Colorado Supplement    

Page | 7 
Colorado Supplement  Handbook Supplement Acknowledgment– Colorado  
By signing below, I acknowledge receipt of this  Handbook Supplement  (“Supplement”) . I understand the practices, 
policies, and procedures described in this Supplement and the Handbook together are designed to provide a summary of 
what I can expect from my employer, Abercrombie & Fitch, abercrombie kids, HOLLISTER,  GILLY HICKS, and Socia l Tourist 
(referred to as “the Company”) , and what the Company expects from me. I also understand and acknowledge:  
• It is my responsibility to familiarize myself with and understand all information in this Supplement;  
• I agree to comply with the standards of  conduct in this Supplement;  
• The Company may discipline me, including termination of my employment, if I violate Company policy;  
• I have a duty to report certain conduct as specified in the policies within this Supplement; 
• This Supplement supersedes all previously issued supplements and any inconsistent written or verbal policy 
statements made or issued before this Supplement;  
• The Company reserves the right to amend, supplement, or rescind the policies described in this Supplement or to 
modify or deviate from such policies at any time without notice. Delay or failure by the Company to enforce a policy or rule will not constitute a waiver of the Company’s right to do so in the future; 
• Neither this Supplement nor any other Company guidelines, policies, or practices create, or are intended to create a promise or representation of continued employment or an employment agreement. I understand and agree that I am employed at -will. The Compan y or I may terminate my employment with or without cause and with or 
without notice, at any time;  
• At this time, I have no employment -related claims of unlawful conduct pending with the Company or concerns 
that I have not yet raised with a member of manage ment, Human Resources, or the One Number; and  
• I will contact Human Resources with any questions about this Supplement . 
Signature _________________________________   Date _____________________  
Name ____________________________________ 
  
 
 
 
  
Associate Handbook 
Connecticut Supplement  
  

Page | 2 
Connecticut Supplement  Connecticut Supplement  
This document supplements the Handbook for  Abercrombie & Fitch Co.  referred to as “the Company.”  Abercrombie & 
Fitch Co. is a leading specialty retailer comprised of our brands including Abercrombie & Fitch, abercrombie kids, 
HOLLISTER,  GILLY HICKS, and Social Tourist. In this Handbook  Supplement , “Abercrombie” and “the Company” refers 
generally to all our brands, and particularly to the brand for which you will be working.  
Throughout this Supplement, you are directed to various team members. Their contact information is in the Company -
wide Handbook for ease of reference. If you have concerns, suggestions, or complaints relating to your employment, 
please utilize the reporting procedures  in the Handbook and this Supplement.  
Inclusive Workplace Policies  
ACCOMMODATIONS AND DISCRIMINATION , HARASSMENT , AND RETALIATION PREVENTION  
This Policy supplements the Reasonable Accommodations  for Disabilities and the Discrimination, Harassment, and 
Retaliation Prevention Policies in the Handbook . 
The Company is committed to a work environment that respects and includes all associates . The Company is also 
committed to providing reasonable accomm odations for known limitations related to pregnancy and enforcing your right 
to be free from discrimination and unfair employment practices, including such conduct because of pregnancy, childbirth, or related conditions. If you have concerns about unfair t reatment, please refer to the Discrimination, Harassment, and 
Retaliation Prevention Policy in the Handbook  and contact the One Number . If you need a reasonable accommodation, 
please refer to the Reasonable Accommodations for Disabilities Policy and notify  your manager, who will escalate the 
request to  Human Resources. You can find additional information about the illegality of sexual harassment and the 
remedies available to victims of sexual harassment here:  
https://www.ct.gov/chro/lib/chro/CHRO_Sexual_Harassment_Written_Materials.pdf
 
The Workday and Compensation  
MEAL BREAKS  
This Policy replaces the Meal and Rest Break Policy in the Handbook.  
Meal Breaks . If you work at least 7.5 consecutive hours, you are provided and may take an uninterrupted and work -free 
30-minute meal break. The meal break is unpaid if you are a non -exempt associate . The meal break should occur after the 
first two hours of work and before the 5.5 hour of work.  
Meal Break Waiver . With written approval from Human Resources, you may voluntarily waive the meal break and agree 
to a different meal break schedule . If you wish to waive a meal break, you must contact Human Resources to obtain and 
complete a waiver form.  
Logistics of Meal Breaks . Within the required window, the Company may schedule your meal break to best accommodate 
operating requirements . If, however, your meal break is not scheduled in advance, please  use your best judgment to 
decide when – within the required window – it is best to take your meal break, based on your workload and operational 
demands. Please then attempt to contact your manager before you start your break to help the Company ensure pro per 
Page | 3 
Connecticut Supplement  staffing . If you cannot connect with your manager, please still proceed with your break. Meal break should occur away 
from your work area to the extent possible.  
Recording Meal Breaks . You must follow the timekeeping procedures set forth in the Timekeeping Policy in the Handbook . 
No Off -the-Clock Work . During meal breaks, you are relieved of all work duties and may not perform any work. Working 
off the clock is strictly prohibited  for non -exempt associate s. This also means that during breaks, you are no t expected to 
be available to take assignments or respond to work messages such as text messages, telephone calls, or emails.  
Duty to Report . No one (manager or non -manager) is permitted to prevent or discourage you from taking a break as 
described above. If you believe you were prevented, interrupted, or discouraged from taking all or part of a break as 
provided in this Policy, or if you experience other circumstances contrary to Company Policy, you have a duty to report the circumstances to the One Number immediately. You must provide: (1) your name and work location; (2) the date(s) 
and time(s) at issue; and (3) a brief description of the conduct or circumstance(s).  
The Comp any will promptly investigate all such reports and will take corrective action when necessary to ensure that all 
associates  are provided meal breaks in compliance with this Policy . You will not be retaliated against for making a good- 
faith report under th is Policy.  
Employment Expectations  
PRIVACY PROTECTION  
The Company generally will collect personally identifiable information (PII) from you and will create and maintain records about you that contain PII, but only for legitimate business purposes. PII incl udes information capable of being associated 
with a particular individual through one or more identifiers, including, but not limited to, a Social Security number (SSN), a driver’s license number, a state identification card number, an account number, a credit or debit card number, a passport number, an alien registration number or a health insurance identification number; PII does not include  publicly available 
information that is lawfully made available to the general public from federal, state or local government records or widely distributed media.  
From time to time, the Company may use your PII for purposes unrelated to administration of the employment relationship.  
We are committed to safeguarding the confidentiality, integrity,  and availability of your PII using reasonable and 
appropriate physical, administrative, and technical safeguards.  
The records and databases that contain your PII are the property of the Company, and access to the information they contain is restricted. Accessing, disclosing, and/or using PII without our authorization or contrary to our policies and procedures can result in discipline, up to and including termination of employment.  
Human Resources is responsible for establishing appropriate authorization. For more information about whether and under what circumstances you may have access to PII, contact Human Resources.  
If you encounter  PII without authorization from the Company or under circumstances outside of your assigned tasks, you 
may not use or disclose the information, but must contact Human Resources to turn over all copies of the information in whatever form.
 
Page | 4 
Connecticut Supplement  Time Away From Wor k and Benefits  
FAMILY AND MEDICAL LEAVE 
We are committed to providing time off to associates for family and medical reasons. Please refer to the Family and 
Medical Leave Policy in the HR Corkboard in PeopleSoft HR ( https://my.anfcorp.com )for more information about the 
Company’s leave -related benefits. The Company also provides leave to eligible associates consistent with the Connecticut 
Family and Medical Leave Act (“CFMLA”). This Policy summarizes the benefits available through the CFMLA.   
Eligibility.  You may be eligible for leave under CFMLA if:  
(1) You have worked at the Company for at least 12 months (which need not be consecutive);  
(2) You have worked at the Company for at least 1,000 hours during the 12 -month period immediately preceding the 
commencement of the leave; and  
(3) The company has 75 associate s in Connecticut.  
Basic Entitlement.  You may take up to 12 weeks of unpaid leave within a twelve -month period. The one -year or two -year 
period is measured by a rolling 12 or 24 -month period dating back from the time you request leave.  
Qualifying Reasons. I n addition to the time off entitlements provided in the Family and Medical Leave Policy in the 
Handbook , you may also take CFMLA for the following reasons:  
• To care for your parent of a spouse;  
• For your own serious health condition (without requiring that you be “unable to perform” an essential function 
of the job); and  
• To serve as an organ or bone marrow donor.  
Additional Military Family Leave Entitlement (Injured Servicemember Leave).  If you are the spouse, son, daughter, 
parent or next of kin of a covered servicemember, you may take up 26 weeks of leave during a single 12 -month period to 
care for such a servicemember with a serious injury or illness.  You may take up to 26 weeks of lea ve during a single 12 -
month period to care for a covered servicemember with a serious injury or illness if the servicemember is your parent -in-
law with a serious health condition. Leave to care for a servicemember is only available during a single 12 -month  period 
and, when combined with other FMLA - or CFMLA -qualifying leave, such time off under this Policy may not exceed 26 
weeks during the single 12 -month period.  The single 12 -month period begins on the first day you take leave to care for 
the injured serv icemember.  
Use of Leave. Leave under this Policy runs concurrently with leave provided under the Family and Medical Leave Policy in the HR Corkboard in PeopleSoft HR ( https://my.anfcorp.com
). 
Returning to Work/Fitness for Duty Medical Certifications.  Generally, if you return to work from a leave that was taken 
because of your own serious health condition, you must provide the Benefits Department and Sedgwic k CMS (refer to the 
Company Directory for contact information) with medical certification confirming that you are able to return to work. The Company may delay your job restoration until you provide this required medical documentation. At the end of a leav e 
under the CFMLA, the Company will return you to your original job, unless that job is not available, in which case the Company will return you to other an available position.  
No Retaliation. The Company will not retaliate against you
 for requesting a leave under this Policy. If you believe you were 
retaliated against, promptly contact  the One Number . 
Page | 5 
Connecticut Supplement  Contacts . If you have questions about leave under this Policy, please contact the Benefits Hotline or Sedgwick CMS . You 
may also file a claim for compensation under the program and/or to file a complaint with the Labor Commissioner for a 
believed violation of the Connecticut Family Leave Law.  
PAY CONTINUATION DURING FAMILY AND MEDICAL LEAVE 
Eligibility.  You are eligible for Connecticut Paid  Leave (“CTPL”) program benefits if you: earn at least $2,325 in the highest 
quarter in the first four of five most recently completed quarters of work; are currently employed for the Company or have been employed by the Company within the last 12 weeks; and the reason for the leave is due to one of the Qualifying Reasons below.  
Qualifying Reasons. Eligible associates  may receive CTPL pay continuation benefits for the following Qualifying Reasons: 
• To bond with a new child, by birth, adoption, or foster plac ement. (For serious health conditions resulting in 
incapacitation during pregnancy, you may qualify for two additional weeks of paid leave benefits.)  
• To address a serious personal or family health condition. Those serving as an organ or bone marrow donor m ay 
also be eligible to receive CTPL benefits.  
• Associates  impacted by family violence may be eligible to receive CTPL benefits to seek medical or psychological 
care, to seek care from a victim services organization, to relocate, or to participate in any civ il or criminal 
proceeding relating to family violence. (Benefits for these reasons are limited to 12 days.)  
• To care for a family member who is injured while on active duty or to address specific issues relating to a family member’s call to active duty or active duty in the armed forces.  
Wage Replacement Benefit.  Eligible associates  may receive up to 12 weeks of paid leave benefits in a 12 -month period, 
with certain exceptions. Benefit rates are equal to 95% of your average weekly wages if the wages are less than or equal to the Connecticut minimum wage multiplied by 40. If wages exc eed the Connecticut minimum wage multiplied by 40, 
your benefit rate will be 95% of your average weekly wage up to the Connecticut minimum wage multiplied by 40 plus 60% of the amount the average weekly wage exceeds the Connecticut minimum wage multiplied by 40. The benefit rate is capped at 60 times the Connecticut minimum wage. In the event you approved for a leave of absence for a Qualifying Reason, you may file a claim with the CTPL to obtain pay continuation benefits.  
Automatic Payroll Deduction. The C ompany automatically contributes a portion of your paycheck to the Connecticut Paid 
Leave (“CTPL”) Authority trust fund. CTPL is funded through associate  payroll contributions. The payroll contributions are 
capped at 0.5% and the amount that is deducted from your paycheck is based on earnings up to the Social Security cap.  
Overlap With Other Policies . To the extent legally permitted: you must follow the leave of absence procedures outlined 
in the applicable leave policy in the Handbook  or in the HR Corkboard in PeopleSoft HR ( https://my.anfcorp.com
); and 
benefits/a leave of absence provided through this Policy will run concurrently with other benefits and/or leaves of absence provided by the Company.  
Additional Information.  For additional information, please visit the website below:  
https://ctpaidleave.my.salesforce.com/sfc/p/#t00000004XRe/a/t00000002aHp/0TTylJsWrYjJlNM8ADO2GGyk.aKbsxs1SX
Tyqb6CVpM   
https://ctpaidleave.my.salesforce.com/sfc/p/#t00000004XRe/a/t00000017vPH/IYK_GaizuYSGI4PeNMl128HN2hn8O1vZ9
diq3q7VKX8    
Page | 6 
Connecticut Supplement  Handbook Supplement Acknowledgment– Connecticut  
By signing below, I acknowledge receipt of this Handbook  Supplement  (“Supplement”) . I understand the practices, 
policies, and procedures described in this Supplement and the Han dbook together are designed to provide a summary of 
what I can expect from my employer, Abercrombie & Fitch, abercrombie kids, HOLLISTER, GILLY HICKS, and Social tourist 
(referred to as the “Company”) and what the Company expects from me. I also understand  and acknowledge:  
• It is my responsibility to familiarize myself with and understand all information in this Supplement;  
• I agree to comply with the standards of conduct in this Supplement; 
• The Company may discipline me, including termination of my employment, if I violate any Company policy;  
• I have a duty to report certain conduct as specified in the policies within this Supplement; 
• This Supplement supersedes all previously issued supplements and any inconsistent written or verbal policy 
statements made or issued before this Supplement;  
• The Company reserves the right to amend, supplement, or rescind the policies described in this Supplement or to 
modify or deviate from such policies at any time without notice. Delay or failure by the Company to enforce a policy or rule will not constitute a waiver of the Company’s right to do so in the future;  
• Neither this Supplement nor any other Company guidelines, policies, or practices create, or are intended to create a promise or representation of continued employment o r an employment agreement. I understand and agree that 
I am employed at -will. The Company or I may terminate my employment with or without cause and with or 
without notice, at any time;  
• At this time, I have no employment -related claims of unlawful conduct  pending with the Company or concerns 
that I have not yet raised with a member of management, Human Resources, or the One Number; and  
• I will contact Human Resources with any questions about this Supplement . 
Signature _________________________________   Date _____________________  
Name ____________________________________ 
  
  
 
 
 
  
Associate Handbook 
Delaware Supplement  
  

Page | 2 
Delaware Supplement  Delaware Supplement  
This document supplements the Handbook for  Abercrombie & Fitch Co.  referred to as “the Company.”  Abercrombie & 
Fitch Co. is a leading specialty retailer comprised of our brands including Abercrombie & Fitch, abercrombie kids, 
HOLLISTER,  GILLY HI CKS, and Social Tourist. In this Handbook  Supplement , “Abercrombie” and “the Company” refers 
generally to all our brands, and particularly to the brand for which you will be working.  
Throughout this Supplement, you are directed to various team members. Th eir contact information is in the Company -
wide Handbook for ease of reference. If you have concerns, suggestions, or complaints relating to your employment, 
please utilize the reporting procedures  in the Handbook and this Supplement.  
Inclusive Workplace Po licies  
PREGNANCY ACCOMMODATIONS AND PREGNANCY DISCRIMINATION , HARASSMENT , AND RETALIATION 
PREVENTION  
This Policy supplements the Reasonable Accommodations  for Disabilities and the Discrimination, Harassment, and 
Retaliation Prevention Policies in the Handbook . 
The Company is committed to providing reasonable accommodations for known limitations related to pregnancy. In 
addition, consistent with the Company’s  values, you have a right to be free from discrimination in relation to pregnancy, 
childbirth, and related conditions. If you need a reasonable accommodation or if you have concerns about unfair treatment, please refer to the Reasonable Accommodations for Disabilities and the Discrimination, Harassment, and Retaliation Prevention Policies in the Handbook  and contact the One Number . 
DISCRIMINATION , HARASSMENT , AND RETALIATION PREVENTION POLICY  
The following section supplements the Discrimination, Harassment, and Retaliation Prevention Policy in the Handbook.  
The Company is committed to a work environment that respects and includes all associates. In addition, consistent with the Company’s values, you have a right to be free from discrimination, harassment, and retaliation. For more information about your rights related to sexual harassment, please review the State’s fact sheet, available here:  
https://dhr.delaware.gov/personnel/neo/documents/sexual -harassment -notice.pdf
  
The Workday and Compensation  
MEAL BREAKS  
This Policy replaces the Meal and Rest Break Policy in the Handbook.  
Meal Breaks . If you work at least 7.5 consecutive hours, you are provided and may take an uninterrupted  and work -free 
30-minute  meal break . The meal break is unpaid if you are a non -exempt associate . The meal break should occur after the 
first two hours of work and before your last t wo hours of work.  
Meal Break Waiver . With written approval from Human Resources, you may voluntarily waive your meal break. If you 
wish to waive a meal break, you must contact Human Resources to obtain and complete a waiver form.  
Page | 3 
Delaware Supplement  Logistics of Meal Breaks . Within the required window, the Company may schedule your meal break to best accommodate 
operating requirements . If, however, a meal break is not scheduled in advance, please use your best judgment to decide 
when – within the required window – it is best to take your meal break, based on your workload and operational demands . 
Please then attempt to contact your manager before you start your break to help the Company ensure proper staffing . If 
you cannot connect with your manager, please still procee d with your meal break . Meal breaks should occur away from 
your work area to the extent possible.  
Recording Meal Breaks . You must follow the timekeeping procedures set forth in the Timekeeping Policy in the Handbook . 
No Off -the-Clock Work . During meal brea ks, you are relieved of all work duties and may not perform any work . Working 
off the clock is strictly prohibited  if you are a non -exempt associate . This also means that during breaks, you are not 
expected to be available to take assignments or respond to work messages such as text messages, telephone calls, or 
emails.  
Duty to Report . No one (manager or non -manager) is permitted to prevent or discourag e you from taking a break as 
described above. If you believe you were prevented, interrupted, or discouraged from taking all or part of any break as 
provided in this Policy, or if you experience other circumstances inconsistent with this Policy, you have a duty to report 
the circumstances to the One Number  immediately . You must provide: (1) your name and work location; (2) the date(s) 
and time(s) at issue; and (3) a brief description of the conduct or circumstance(s).  
The Company will promptly investigate all such reports and will take corrective action when necessary to ensure that all associates are provided meal breaks in compliance with this Policy . You will not be retaliated against for making a good -
faith report under this Policy.  
 
  
 
  
 
 
   
Page | 4 
Delaware Supplement  Handbook Supplement Acknowledgment– Delaware  
By signing below, I acknowledge receipt of this Handbook  Supplement  (“Supplement”) . I understand the practices, 
policies, and procedures described in this Supplement and the Handbook together are designed to prov ide a summary of 
what I can expect from my employer, Abercrombie & Fitch, abercrombie kids, HOLLISTER, GILLY HICKS, and Social tourist 
(referred to as the “Company”) and what the Company expects from me. I also understand and acknowledge:  
• It is my responsibility to familiarize myself with and understand all information in this Supplement;  
• I agree to comply with the standards of conduct in this Supplement; 
• The Company may discipline me, including termination of my employment, if I violate any Company policy;  
• I have a duty to report certain conduct as specified in the policies within this Supplement; 
• This Supplement supersedes all previously issued supplements and any inconsistent written or verbal policy 
statements made or issued before this Supplement;  
• The C ompany reserves the right to amend, supplement, or rescind the policies described in this Supplement or to 
modify or deviate from such policies at any time without notice. Delay or failure by the Company to enforce a 
policy or rule will not constitute a waiver of the Company’s right to do so in the future;  
• Neither this Supplement nor any other Company guidelines, policies, or practices create, or are intended to create a promise or representation of continued employment or an employment agreement. I understand and agree that I am employed at -will. The Company or I may terminate my employment with or without cause and with or 
without notice, at any time;  
• At this time, I have no employment -related claims of unlawful conduct pending with the Company or concern s 
that I have not yet raised with a member of management, Human Resources, or the One Number; and  
• I will contact Human Resources with any questions about this Supplement . 
Signature _________________________________   Date _____________________  
Name ____________________________________ 
  
  
 
 
 
  
Associate Handbook 
District of Columbia Supplement  
  

Page | 2 
DC Supplement  District of Columbia Supplement  
This document supplements the Handbook for  Abercrombie & Fitch Co.  referred to as “the Company.”  Abercrombie & 
Fitch Co. is a leading specialty retailer comprised of our brands including Abercrombie & Fitch, abercrombie kids, 
HOLLISTER,  GILLY HICKS, and Social Tourist. In this Handbook  Supplement , “Abercrombie” and “the Company” refers 
generally to all our brands, and particularly to the brand for which you will be working.  
Throughout this Supplement, you are directed to various team members. Their contact information is in the Company -
wide Handbook for ease of reference. If you have concerns, suggestions, or complaints relating to your employment, 
please utilize the reporting procedures  in the Handbook and this Supplement.  
Inclusive Workplace Polici es 
PREGNANCY ACCOMMODATIONS AND PREGNANCY DISCRIMINATION , HARASSMENT , AND RETALIATION 
PREVENTION  
This Policy supplements the Reasonable Accommodations  for Disabilities and the Discrimination, Harassment, and 
Retaliation Prevention Policies in the Handbook . 
The Company is committed to providing reasonable accommodations for known limitations related to pregnancy or 
breastfeeding. In addition, consistent with the Company’s values and the Protecting Pregnant Workers Fairness Act, you 
have a right to be free from discrimination in relation to pregnancy, childbirth, and related conditions. If you need a 
reasonable accommodation or if you have concerns about unfair treatment, please refer to the Reasonable Accommodations for Disabilities and the Discrimination, Harassment, and Retaliation Prevention Policies in the Handbook  
and contact the One Number . 
Employment Standards  
NOTICE REGARDING NON-COMPETE AGREEMENTS  
No employer operating in the District of Columbia may request or require an associate working in the District of Columbia 
to agree to a non -compete policy or agreement, in accordance with the Ban on Non -Compete Agreements Amendment 
Act of 2020.  The Company  complies with such restrictions.  
Time Away From Work and Benefits  
PAID SICK AND SAFE LEAVE  
For additional information about Paid Sick and Safe Leave (“PSSL”), please view the applicable poster below or contact Human Resources:  
English and Spanish Posters,  
https://does.dc.gov/sites/default/files/dc/sites/does/page_content/attachments/OWH%20 -%20ASSLA%20POSTER -
%20Bilingual.pdf  
Page | 3 
DC Supplement  FAMILY AND MEDICAL LEAVE 
We are committed to providing time off to associates for family and medical reasons. Please refer to the Family and 
Medical Leave Policy in the HR Corkboard in PeopleSoft HR ( https://my.anfcorp.com )for more information about the 
Compa ny’s leave -related benefits. The Company also provides leave to eligible associates consistent with the DC Family 
and Medical Leave Act (“DCFMLA”). This Policy summarizes the benefits available through the DCFMLA.  
Eligibility.  You are eligible for DCFMLA leave if:  
(1) You have worked for the Company in DC continuously for at least 12 months;  
(2) You have worked in DC for at least 1,000 hours during the 12 -month period immediately preceding the leave; and  
(3) At the time of your leave, the Company has at least 20 associates in DC.  
Leave Length.  Eligible associates may take up to 32 workweeks of unpaid leave during any 24 -month period.  
The leave is calculated on a rolling 24 -month period measured backward from the date you use any DCFMLA leave . 
Qualifying Reasons. In addition to the entitlements summarized in the Family and Medical Leave Policy in the HR 
Corkboard in PeopleSoft HR ( https://my.anfcorp.com ), you may also take DCFMLA for the following reasons:  
(1) The placement of a child for whom you have permanent parental responsibility; and/or  
(2) To care for a person to whom you are related by blood, legal custody, or marriage; a child who resides with you and for whom you have permanent parental responsibility; or a person with whom you share or have shared within last year a mutual residence and maintain a committed relationship, when that person has a “serious health condition.”  
However, unlike the FMLA, you may not use DCFMLA leave for certain qualifying exigencies.  
Use of Leave.  If you are taking leave that is covered by the DCFMLA, but not the FMLA, you may elect to substitute accrued 
PTO benefits for unpaid leave, but you are not required to do so. Your decision to decline substitution of paid leave for 
unpaid DCFMLA leave time does not extend the length of the FMLA and/or DCFMLA leave. In addition, your substitution of PTO benefits does not extend the length of DCFMLA leave. Leave under this Policy runs concurrently with leave provided 
under the Family and Medical Leave Policy in the Handbook . Likewise, leaves of absence taken in connection with a 
disability leave plan or workers’ compensation injury/illness will run concurrently with FMLA and/or DCFMLA leave entitlement.  
No Retaliation. The Company will not retaliate against you for requesting a leave under this Policy. If you believe you were 
retaliated against, promptly contact the One Number . 
PAY CONTINUATION DURING FAMILY LEAVE 
Qual ifying Reasons.  Eligible employees receive Paid Family Leave  (PFL) pay continuation benefits for the following 
Qualifying Reasons:  
• Parental leave: to bond with a new child for up to 8 weeks in a year; 
• Family leave: to care for a family member for up to 6 weeks in a year;  
• Medical leave: for your own serious health condition for up to 6 weeks in a year; and  
Page | 4 
DC Supplement  • Prenatal leave - for prenatal medical care for up to 2 weeks in a year.  
Each kind of leave has its own eligibility rules and its own limit on the length of time you can receive benefits in a year. 
The maximum amount of leave for any combination of parental, family, and medical leave is 8 weeks. However, there is 
an exception for pregnant women who take prenatal leave. Pregnant women are eligible for 2 weeks of prenatal leave 
while pregnant and 8 weeks of parental leave after giving birth, for a maximum of 10 weeks.  
Wage Replacement Benefits. PFL benefits are based on the wages you received and what was reported by the Company 
to the DES. The current maximu m weekly benefit amount is $1,009.  In the event you approved for a leave of absence for 
a Qualifying Reason, you may file a apply for benefit continuation through the Office of PFL at dcpaidfamilyleave.dc.gov.  
Automatic Payroll Deduction. The Company autom atically contributes a portion of your paycheck to the Department of 
Employment Services (“DES”).  
Overlap With Other Policies . To the extent legally permitted: you must follow the leave of absence procedures outlined 
in the applicable leave policy in the H andbook  or in the HR Corkboard in PeopleSoft HR ( https://my.anfcorp.com ); and 
benefits/a leave of absence provided through this Policy will run concurrently with other benefits and/or leaves of absence provided by the Company.  
Additional Information.  For additional information, please visit the website below:  
https://does.dc.gov/sites/default/files/dc/sites/does/publication/attachments/2021%20OPFL%20Employee%20Worksit
e%20No tice_2.pdf  
COMMUTER /TRANSIT BENEFITS  
Starting on the first day of employment, full- time and part -time associates who work in DC are eligible for either a pre -tax 
election fringe benefit, a program where the Company pr ovides a subsidy to offset commuting costs, or a Company -
provided transit service . The Company will inform you which of these benefits it offers at the time of your hire . Contact 
the Benefits Department with questions or for further information. While the Company hopes that you will raise concerns 
regarding this policy with management or by contacting the One Number, so such concerns can be promptly addressed, the Company is required to notify associates of the right to submit a complaint to the Department of Employment Services 
Office of Wage -Hour via email ( owh.ask@dc.gov
) or phone (202 -671-1880).  
  
Page | 5 
DC Supplement  Handbook Supplement Acknowledgment– Washington, D.C.  
By signing below, I acknowledge receipt of this Handbook  Supplement  (“Supplement”) . I understand the practices, 
policies, and procedures described in this Supplement and the Handbook together are designed to provide a summary of 
what I ca n expect from my employer, Abercrombie & Fitch, abercrombie kids, HOLLISTER, GILLY HICKS, and Social tourist 
(referred to as the “Company”) and what the Company expects from me. I also understand and acknowledge:  
• It is my responsibility to familiarize myself with and understand all information in this Supplement;  
• I agree to comply with the standards of conduct in this Supplement; 
• The Company may discipline me, including termination of my employment, if I violate any Company policy;  
• I have a duty to report certain conduct as specified in the policies within this Supplement; 
• This Supplement supersedes all previously issued supplements and any inconsistent written or verbal policy 
statements made or issued before this Supplement;  
• The Company reserves the right to amend, supplement, or rescind the policies described in this Supplement or to 
modify or deviate from such policies at any time without notice. Delay or failure by the Company to enforce a policy or rule will not constitute a waiver of th e Company’s right to do so in the future;  
• Neither this Supplement nor any other Company guidelines, policies, or practices create, or are intended to create a promise or representation of continued employment or an employment agreement. I understand and agree that I am employed at -will. The Compan y or I may terminate my employment with or without cause and with or 
without notice, at any time;  
• At this time, I have no employment -related claims of unlawful conduct pending with the Company or concerns 
that I have not yet raised with a member of manage ment, Human Resources, or the One Number; and  
• I will contact Human Resources with any questions about this Supplement . 
Signature _________________________________   Date _____________________  
Name ____________________________________ 
  
 
 
 
 
 
Associate Handbook 
Hawaii Supplement  
  

Page | 2 
Hawaii Supplement  Hawaii Supplement  
This document supplements the Handbook for  Abercrombie & Fitch Co.  referred to as “the Company.”  Abercrombie & 
Fitch Co. is a leading specialty retailer comprised of our brands including Abercrombie & Fitch, abercrombie kids, 
HOLLISTER,  GILLY HICKS, and Social Tourist. In this Handbook  Supplement , “Abercrombie” and “the Company” refers 
generally to all our brands, and particularly to the brand for which you will be working.  
Throughout this Supplement, you are directed to various team members. Their contact information is in the Company -
wide Handbook for ease of reference. If you have concerns, suggestions, or complaints relating to your employment, 
please utilize the reporting procedures  in the Handbook and this Supplement.  
Time Away From Work  
FAMILY AND MEDICAL LEAVE 
We are committed to providing time off to associates for family and medical reasons. Please refer to the Family and 
Medical Leave Policy in the HR Corkboard in PeopleSoft HR ( https://my.anfcorp.com )for more information about the 
Company’s leave -related benefits. The Company also provides leave to eligible associates consistent with the Hawaii 
Family Leave Law (“HFLL”) . this Policy summarizes leave available through  the HFLL.  
Eligibility. You are eligible for HFLL leave if:  
(1) You have been employed for at least six consecutive months; and  
(2) Our company has 100 or more associates in Hawaii (for each working day of 20 or more calendar weeks in the 
current or preceding calendar year).  
Basic Entitlement. Eligible associates may take up to four workweeks of unpaid leave per calendar year Qualifying 
Reasons. Leave under the HFLL is determined on a calendar year basis.  
Qualifying Reasons. HFLL leave may be taken:  
(1) Following the birth or adoption of your child; or  
(2) To care for your spouse (or reciprocal beneficiary), child, parent (including parent -in-law or stepparent) or 
grandparent (including grandparent -in-law) who has a serious health condition.  
For purpos es of HFLL, a “serious health condition” is a physical or mental condition that warrants your participation to 
provide care during the period of treatment or supervision by a healthcare provider and either involves inpatient care in 
a hospital, hospice, or residential health care facility; or requires continuing treatment or continuing supervision by a 
healthcare provider.  
Use of Leave. Leave under this Policy runs concurrently with leave provided under the Family and Medical Leave Policy in the Handbook.  
Substitution of Paid Leave.  You may, but are not required, to use PTO  benefits during HFLL leave.  
Returning to Work.  As with FMLA leave, at the end of HFLL, you typically will be returned to the same or an equivalent 
position with equivalent pay, benefits, and other terms.  
Page | 3 
Hawaii Supplement  No Retaliation. The Company will not retaliate against you for requesting a leave under this Policy. If you believe you were 
retaliated against, promptly contact the One Number . 
  
Page | 4 
Hawaii Supplement  Handbook Supplement Acknowledgment–Hawaii 
By signing below, I acknowledge receipt of this Handbook  Supplement  (“Supplement”) . I understand the practices, 
policies, and procedures described in this Supplement and the Handbook together are designed to provide a summary of 
what I can expect from my employer, Abercrombie & Fitch, abercrombie kids, HOLLISTER, GILLY HICKS, and Social tourist 
(referred to as the “Company”) and what the Company expects from me. I also understand and acknowledge:  
• It is my responsibility to familiarize myself with and understand all information in this Supplement;  
• I agree to comply with the standards of conduct in this Supplement; 
• The Company may discipline me, including termination of my employment, if I violate any Company policy;  
• I have a duty to repo rt certain conduct as specified in the policies within this Supplement;  
• This Supplement supersedes all previously issued supplements and any inconsistent written or verbal policy 
statements made or issued before this Supplement;  
• The Company reserves the ri ght to amend, supplement, or rescind the policies described in this Supplement or to 
modify or deviate from such policies at any time without notice. Delay or failure by the Company to enforce a 
policy or rule will not constitute a waiver of the Company’s right to do so in the future;  
• Neither this Supplement nor any other Company guidelines, policies, or practices create, or are intended to create a promise or representation of continued employment or an employment agreement. I understand and agree that I am employed at -will. The Company or I may terminate my employment with or without cause and with or 
without notice, at any time;  
• At this time, I have no employment -related claims of unlawful conduct pending with the Company or concerns 
that I have not yet raised with a member of management, Human Resources, or the One Number; and  
• I will contact Human Resources with any questions about this Supplement . 
Signature _________________________________   Date _____________________  
Name ____________________________________ 
 
  
 
 
 
  
Associate Handbook 
Illinois Supplement  
  

Page | 2 
Illinois Supplement  Illinois Supplement  
This document supplements the Handbook for  Abercrombie & Fitch Co.  referred to as “the Company.”  Abercrombie & 
Fitch Co. is a leading specialty retailer comprised of our brands including Abercrombie & Fitch, abercrombie kids, 
HOLLISTER,  GILLY HICKS, and Social Tourist. In this Handbook  Supplement , “Abercrombie” and “the Company” refers 
generally to all our brands, and particularly to the brand for which you will be working.  
Throughout this Supplement, you are directed to various team members. Their contact information is in the Company -
wide Handbook for ease of reference. If you have concerns, suggestions, or complaints relating to your employment, 
please utilize the reporting procedures  in the Handbook and this Supplement.  
Inclusive Workplace Policies  
ACCOMMODATIONS AND  DISCRIMINATION , HARASSMENT , AND RETALIATION PREVENTION  
This Policy supplements the Reasonable Accommodations  for Disabilities and the Discrimination, Harassment, and 
Retaliation Prevention Policies in the Handbook . 
The Company is committed to providing reasonable accommodations to qualified individuals with disabilities, including limitations related to pregnancy. You also have a right to certain reasonable accommodations.  If you need a reasonable 
accommodation or if you have concerns about unfair treatment, please refer to the Reasonable Accommodations for Disabilities and the Discrimination, Harassment,  and Retaliation Prevention Policies in the Handbook  and contact the One 
Number.   
As reinforced in the Company -wide Handbook, the Company fosters a work environment free of all forms of 
discrimination, harassment, and retaliation based on any protected category. Not only is sexual harassment inconsistent with the Company’s commitment to a workplace that respects associates, but sexual harassment is also illegal, and you 
have a right to be free from sexual harassment and retaliation. While the Discrimination, Harassment, and Retaliation 
Prevention Policy in the Handbook provides detailed information about the Company’s definitions of unacceptable conduct, in Chicago, sexual harassment also includes unwelcome sexual advances, unwelcome conduct of a sexual nat ure, 
and sexual misconduct – meaning any behavior of a sexual nature which involves coercion, abuse of authority, or misuse 
of an individual’s employment position. Associates working in the City of Chicago are required to complete sexual 
harassment prevent ion training annually, which is provided by the Company.  
If you have concerns about unfair treatment, please refer to the Discrimination, Harassment, and Retaliation Prevention Policy in the Handbook for detailed reporting instructions and notify Human Resources. While we hope that you will raise concerns with the Company following the reporting procedures in the above policies so we can promptly investigate and resolve the matter, you also have a right to file a charge of discrimination or sexual harassme nt under the Illinois Human 
Rights Act with the Illinois Department of Human Rights (“IDHR”). The charge process may be initiated by completing the form available at by contacting the IDHR at IDHR.Intake@illinois.gov
, or by contacting the IDHR’s offices at the locations 
below. You may also contact the Illinois Sexual Harassment and Discrimination Helpline at 1-877-236-7703.  
Page | 3 
Illinois Supplement  IDRH, Chicago Office  
555 W. Monroe Street, Suite  
700 Chicago, IL 60601  
312-814-6200 / 866 -740-3953 (TTY)  
312-814-6251 (Fax)  IDHR, Springfield Office  
535 W. Jefferson Street, 1st Floor  
Springfield, IL 62702  
217-785-5100 / 866 -740-3953 (TTY)  
217-785-5106 (Fax)  
 
 
Additional avenues for pursuing a charge of discrimination or sexual harassment are provided below:  
Chicago Commission on Human Relations  
740 N. Sedgwick, 4th Floor  
Chicago, IL 60654  
(312) 744 -4111 (TTY)  
cchr@cityofchicago.org  U.S. Equal Employment Opportunity Commission  
Chicago District Office  
230 South Dearborn St., Suite 1866 Chicago, Illinois 
60604  
(312) 872 -9744 / (866) 740 -3953 (TTY)  
https://publicportal.eeoc.gov/Portal/Login.aspx  
The Workday and Compensation 
MEAL BREAKS  
This Policy replaces the Meal and Rest Break Policy in the Handbook.  
Meal Breaks . If you  are a non -exempt associate  and work  at least  7.5 continuous hours, you are provided and may take 
an uninterrupted, work -free, and unpaid 30 -minute meal break . If you are an exempt associate  and work 7.5 continuous 
hours or longer, you are provided and may take an uninterrupted, work -free, and paid 2 0-minute meal break. This meal 
break should occur no later than five hours after starting work. If you work more than 7.5 continuous hours, you are  
provided and may take a second meal break. The second meal break must occur no later than 12 hours after you  start 
work ( i.e., no later than five hours after the start of the second “shift ,” if applicable) . 
Logistics of Meal Breaks.  Within the required window, the Company may schedule meal breaks(s) to best accommodate 
operating requirements. If, however, a meal break(s) is not scheduled in advance, please use your best judgment to decide 
when – within the required window – it is best to take your meal break(s), based on your workload and operational 
demands. Please then attempt to contact your manager before you  start your meal break(s) to help the Company ensure 
proper staffing.  If you cannot connect with your manager, please still proceed with your meal break. Meal breaks should 
be taken away from your work area to the extent possible.  
Recording Meal Breaks . You must follow the timekeeping procedures set forth in the Timekeeping Policy in the Handbook . 
No Off -the-Clock Work.  During meal breaks, you are relieved of all work duties and may not perform work. Working off 
the clock is strictly prohibited  if you are a non -exempt associate . This also means that during breaks, you are not expected 
to be available to take assignments or respond to work messages such as text messages, telephone calls, or emails.  
Duty to Report . No one (manager or non -manager) is permitted to prevent or discourage you from taking a break as 
described above. If you believe you were prevented, interrupted, or discouraged from taking all or part of any break, or if 
you experience other circumstances inconsistent with this Policy, you have a duty to report the circumstances to your 
General Manager immediately. You must provide: (1) your name and work location; (2) the date(s) and time(s) at issue; 
and (3) a brief description of the conduct or circumstance(s).  
Page | 4 
Illinois Supplement  The Company will promptly investigate all such reports and will take corrective action when necessary to ensure that all 
associates are provided meal breaks in compliance with this Policy. You will not be retaliated against for making a good -
faith report under this Policy.  
NOTICE  OF THE EARNED INCOME TAX CREDIT  
IF YOU EARNED LESS THAN $41,756 LAST YEAR AND HAVE AT LEAST ONE CHILD, YOU MAY BE ELIGIBLE TO RECEIVE A TAX CREDIT FROM THE FEDERAL GOVERNMENT. THE TAX CREDIT MAY BE A REFUND FROM THE FEDERAL GOVERNMENT FOR AS MUCH AS $6,66 0 EVEN IF YOU DO NOT OWE FEDERAL TAXES, YOU MUST FILE A TAX RETURN TO RECEIVE THE EARNED 
INCOME TAX CREDIT. BE SURE TO FILL OUT THE EARNED INCOME TAX CREDIT FORM IN THE TAX RETURN BOOKLET.  
WAGE INFORMATION ACKNOWLEDGEMENT  
By signing the enclosed Acknowledgement page, you  acknowledge and agree that the Company provided you with notice 
of you rate of pay and the time/place of wage payments.  
Time Away From Work  
PAID SICK AND SAFE LEAVE POLICY FOR ASSOCIATES  IN CHICAGO AND COOK COUNTY  
For additional information about Paid Sick and Safe Leave (“PSSL”), please view the applicable poster below or contact Human Resources:  
Cook County English Poster,  
https://www.cookcountyil.gov/sites/g/files/ywwepo161/files/service/model -earned -sick-leave -notice -employees -
workplace -poster.pdf  
Cook County Spanish Poster,  
https://www.cookcountyil.gov/sites/g/files/ywwepo161/files/service/spanish -language -model -earned -sick-leave -notice -
employe es-workplace -poster -4.pdf  
City of Chicago English Poster, https://www.chicago.gov/content/dam/city/depts/bacp/OSL/20220701mwandpslenglishletterfv.pdf
 
City of Chicago Spanish Poster, https://www.chicago.gov/content/dam/city/depts/bacp/OSL/20220701mwandpslspanish.pdf
.  
Page | 5 
Illinois Supplement  Handbook Supplement Acknowledgment–Illinois 
By signing below, I acknowledge receipt of this Handbook  Supplement  (“Supplement”) . I understand the practices, 
policies, and procedures described in this Supplement and the Handbook together are designed to provide a summary of 
what I can expect from my employer, Abercrombie & Fitch, abercrombie kids, HOLLISTER, GILLY HICKS, and Social  tourist 
(referred to as the “Company”) and what the Company expects from me. I also understand and acknowledge:  
• It is my responsibility to familiarize myself with and understand all information in this Supplement;  
• I agree to comply with the standards of conduct in this Supplement;  
• The Company may discipline me, including termination of my employment, if I violate any Company policy;  
• I have a duty to report certain conduct as specified in the policies within this Supplement; 
• This Supplement su persedes all previously issued supplements and inconsistent written or verbal policy 
statements made or issued before this Supplement;  
• The Company reserves the right to amend, supplement, or rescind the policies described in this Supplement or to 
modify or  deviate from such policies at any time without notice. Delay or failure by the Company to enforce a 
policy or rule will not constitute a waiver of the Company’s right to do so in the future; 
• Neither this Supplement nor any other Company guidelines, polici es, or practices create, or are intended to create 
a promise or representation of continued employment or an employment agreement. I understand and agree that I am employed at -will. The Company or I may terminate my employment with or without cause and wit h or 
without notice, at any time;  
• At this time, I have no employment -related claims of unlawful conduct pending with the Company or concerns 
that I have not yet raised with a member of management, Human Resources, or the One Number; and  
• I will contact Hum an Resources with questions about this Handbook.  
Signature _________________________________   Date _____________________  
Name ____________________________________ 
  
 
 
 
  
Associate Handbook 
Iowa Supplement  
  

Page | 2 
Iowa Supplement  Iowa Supplement  
This document supplements the Handbook for  Abercrombie & Fitch Co.  referred to as “the Company.”  Abercrombie & 
Fitch Co. is a leading specialty retailer comprised of our brands including Abercrombie & Fitch, abercrombie kids, 
HOLLISTER,  GILLY HICKS, and Social Tourist. In this Handbook  Supplement , “Abercrombie” and “the Company” refers 
generally to all our brands, and particularly to the brand for which you will be working.  
Throughout this Supplement, you are directed to various team members. Their contact information is in the Company -
wide Handbook for ease of reference. If you have concerns, suggestions, or complaints relating to your employment, 
please utilize the reporting procedures  in the Handbook and this Supplement.  
Inclusive Workplace Policies  
PREGNANCY ACCOMMODATIONS  
This Policy  supplements the Reasonable Accommodations for Disabilities and Discrimination, Harassment, and 
Retaliation Policies in the Handbook . 
The Company is committed to providing reasonable accommodations for known limitations related to pregnancy. If you 
need a reasonable accommodation or if you have concerns about unfair treatment, please refer to the Reasonable 
Accommodations for Disabilities and the Discrimination, Harassment, and Retaliation Prevention Policies in the Handbook  
and notify your manager, who will escalate the request to Human Res ources. In addition, ple ase note that if a reasonable 
accommodation is not available to allow you to perform the essential  functions of your position, you may be eligible for 
an unpaid leave of absence for up to eight weeks.  
  
Page | 3 
Iowa Supplement  Handbook Supplement Acknowledgment– Iowa  
By signing below, I acknowledge receipt of this Handbook  Supplement  (“Supplement”) . I understand the practices, 
policies, and procedures described in this Supplement and the Handbook together are designed to provide a summary of 
what I can expect from my employer, Abercrombie & Fitch, abercrombie kids, HOLLISTER, GILLY HICKS, and Social tourist (referred to as the “Company”) and what the Company expects from me. I also understand and acknowledge:  
• It is my responsibility to familiarize myself with and understand all information in this Supplement;  
• I agree to comply with the standards of conduct in this Supplement; 
• The Company may discipline me, including termination of my employment, if I violate  any Company policy;  
• I have a duty to report certain conduct as specified in the policies within this Supplement; 
• This Supplement supersedes all previously issued supplements and any inconsistent written or verbal policy 
statements made or issued before th is Supplement;  
• The Company reserves the right to amend, supplement, or rescind the policies described in this Supplement or to 
modify or deviate from such policies at any time without notice. Delay or failure by the Company to enforce a policy or rule will  not constitute a waiver of the Company’s right to do so in the future;  
• Neither this Supplement nor any other Company guidelines, policies, or practices create, or are intended to create a promise or representation of continued employment or an employment agreement. I understand and agree that I am employed at -will. The Company or I may terminate my employment with or without cause and with or 
without notice, at any time;  
• At this time, I have no employment -related claims of unlawful conduct pending with th e Company or concerns 
that I have not yet raised with a member of management, Human Resources, or the One Number; and  
• I will contact Human Resources with any questions about this Supplement . 
Signature _________________________________   Date _____________________ 
Name ____________________________________ 
  
 
 
 
  
Associate Handbook 
Kentucky Supplement  
  

Page | 2 
Kentucky Supplement  Kentucky Supplement  
This document supplements the Handbook for  Abercrombie & Fitch Co.  referred to as “the Company.”  Abercrombie & 
Fitch Co. is a leading specialty retailer comprised of our brands including Abercrombie & Fitch, abercrombie kids, 
HOLLISTER,  GILLY HICKS, and Social Tourist. In this Handbook  Supplement , “Abercrombie” and “the Company” refers 
generally to all our brands, and particularly to the brand for which you will be working.  
Throughout this Supplement, you are directed to various team members. Their contact information is in the Company -
wide Handbook for ease of reference. If you have concerns, suggestions, or complaints relating to your employment, 
please utilize the reporting procedures  in the Handbook and this Supplement.  
Inclusive Workplace Policies  
PREGNANCY ACCOMMODATIONS AND PREGNANCY DISCRIMINATION , HARASSMENT , AND RETALIATION 
PREVENTION  
This Policy supplements the Reasonable Accommodations  for Disabilities and the Discrimination, Harassment, and 
Retaliation Prevention Policies in the Handbook . 
The Company is committed to providing reasonable accommodations for known limitations related to pregnancy. In 
addition, consistent with the Company’s values, you have a right to be free from discrimination in relation to pregnancy, 
childbirth, and related conditions.  If you need a reasonable accommodation or if you have concerns about unfair 
treatment, please refer to the Reasonable Accommodations for Disabilities and the Discrimination, Harassment, and 
Retaliation Prevention Policies in the Handbook  and notify your m anager, who will escalate the request to Human 
Resources . 
The Workday and Compensation  
MEAL AND REST BREAKS  
This Policy replaces the Meal and Rest Break Policy in the Handbook.  
Rest Breaks . If you work more than four consecutive hours, you are provided and may take a 10 -minute uninterrupted, 
work -free, and paid rest break during every four hours worked . Rest breaks should occur as close to the middle of each 
four -hour work period as is practicable.  
Meal Breaks . You are provided and may take a 30 -minute uninterrupted  and work -free meal break between the third and 
fifth hour of each shift worked.  This meal break is unpaid if you are a non -exempt associate . 
Meal Break Waiver . With written approval from Human Resources, you may voluntarily waive meal breaks. If you wish to 
waive a meal break, you must contact Human Resources to obtain and complete a waiver form.  
Logistics of Meal and Rest Breaks . Within the required window, the Company may schedule meal and rest breaks(s) to 
best accommodate operating  requirements . If, however, a rest or meal break is not scheduled in advance, please use your 
best judgment to decide when – within the required window – it is best to take your breaks, based on your workload and 
operational demands. Please then attempt to  contact your manager before you start your break, to help the Company 
Page | 3 
Kentucky Supplement  ensure proper staffing . If you cannot connect with your manager, please still proceed with your break . Breaks should occur 
away from your work area to the extent possible.  
Recording Mea l and Rest Breaks . You must follow the timekeeping procedures set forth in the Timekeeping Policy in the 
Handbook . 
No Off -the-Clock Work . During breaks, you are relieved of all work duties and may not perform work . Working off the 
clock is strictly prohibited  if you are a non -exempt associate . This also means that during breaks, you are not expected to 
be available to take assignments or respond to work messages such as text messages, telephone calls, or emails.  
Duty to Report . No one (manager or non -manager) is permitted to prevent or discourage you from taking a break as 
described above. If you believe you were prevented, interrupted, or discouraged from taking all or part of a break as 
provided in this Policy, or if you experience other circumstances inconsistent with this Policy, you have a duty to report 
the circumstances to the One Number  immediately . You must provide: (1) your name and work location; (2) the date(s) 
and time(s) at issue; and (3) a brief description of the conduct or circumstance(s).  
The Company will promptly investigate all such reports and will take corrective action when necessary to ensure that all associates are provided breaks in compliance with this Po licy. You will not be retaliated against for making a good -faith 
report under this Policy.  
Time Away From Work  
ADOPTION LEAVE  
The Company has profound respect for associates who make the decision to adopt a child or children. If you adopt a child 
under the  age of seven, you may take an unpaid leave of absence of up to six weeks.  
To the extent practicable, you must provide your manager and the Benefits Department with reasonable advance notice 
prior to taking leave; otherwise, provide notice as soon as possible under the circumstances. We may require that you provide reasonable documentation to verify your need for leave for this purpose.  
Leave under this Policy will run concurrently with other leave provided by the Company and/or applicable law, to the exten t permitted by applicable law.  
 
 
Page | 4 
Kentucky Supplement  Handbook Supplement Acknowledgment– Kentucky  
By signing below, I acknowledge receipt of this Handbook  Supplement  (“Supplement”) . I understand the practices, 
policies, and procedures described in this Supplement and the Handbook together are designed to provide a summary of 
what I can expect from my employer, Abercrombie & Fitch, abercrombie kids, HOLLISTER, GILLY HICKS, and Social  tourist 
(referred to as the “Company”) and what the Company expects from me. I also understand and acknowledge:  
• It is my responsibility to familiarize myself with and understand all information in this Supplement;  
• I agree to comply with the standards of conduct in this Supplement;  
• The Company may discipline me, including termination of my employment, if I violate any Company policy;  
• I have a duty to report certain conduct as specified in the policies within this Supplement; 
• This Supplement supersedes all previously issued supplements and any inconsistent written or verbal policy 
statements made or issued before this Supplement;  
• The Company reserves the right to amend, supplement, or rescind the policies described in this Supplement or to 
modif y or deviate from such policies at any time without notice. Delay or failure by the Company to enforce a 
policy or rule will not constitute a waiver of the Company’s right to do so in the future; 
• Neither this Supplement nor any other Company guidelines, po licies, or practices create, or are intended to create 
a promise or representation of continued employment or an employment agreement. I understand and agree that I am employed at -will. The Company or I may terminate my employment with or without cause and  with or 
without notice, at any time;  
• At this time, I have no employment -related claims of unlawful conduct pending with the Company or concerns 
that I have not yet raised with a member of management, Human Resources, or the One Number; and  
• I will contact  Human Resources with any questions about this Supplement . 
Signature _________________________________   Date _____________________  
Name ____________________________________ 
  
 
 
 
  
Associate Handbook 
Louisiana Supplement  
  

Page | 2 
Louisiana Supplement  Louisiana Supplement  
This document supplements the Handbook for  Abercrombie & Fitch Co.  referred to as “the Company.”  Abercrombie & 
Fitch Co. is a leading specialty retailer comprised of our brands including Abercrombie & Fitch, abercrombie kids, 
HOLLISTER,  GILLY HICKS, and Social Tourist. In this Handbook  Supplement , “Abercrombie” and “the Company” refers 
generally to all our brands, and particularly to the brand for which you will be working.  
Throughout this Supplement, you are directed to various team members. Their contact information is in the Company -
wide Handbook for ease of reference. If you have concerns, suggestions, or complaints relating to your employment, 
please utilize the reporting procedures  in the Handbook and this Supplement.  
Inclusive Workplace Policies  
PREGNANCY ACCOMMODATIONS AND PREGNANCY DISCRI MINATION , HARASSMENT , AND RETALIATION 
PREVENTION  
This Policy supplements the Reasonable Accommodations  for Disabilities and the Discrimination, Harassment, and 
Retaliation Prevention Policies in the Handbook . 
Consistent with the Company’s values and in com pliance with Louisiana law, you have a right to be free from 
discrimination and unfair employment practices because of pregnancy, childbirth, or related conditions. The Company is 
committed to providing reasonable accommodations for known limitations relat ed to pregnancy. If you need a reasonable 
accommodation or if you have concerns about unfair treatment, please refer to the Reasonable Accommodations for 
Disabilities and the Discrimination, Harassment, and Retaliation Prevention Policies in the Handbook  and notify your 
manager, who will escalate the request to Human Resources . In addition, please note that if a reasonable accommodation 
is not available to allow you to perform the essential  functions of your position, you may be eligible for an unpaid leave of 
absence for up to four months, depending on the underlying circumstances.  
  
Page | 3 
Louisiana Supplement  Handbook Supplement Acknowledgment– 
Louisiana 
By signing below, I acknowledge receipt of this Handbook  Supplement  (“Supplement”) . I understand the practices, 
policies, and procedures described in this Supplement and the Handbook together are designed to provide a summary of 
what I can expect from my employer, Abercrombie & Fitch, abercrombie kids, HOLLISTER, GILLY HICKS, and Social  tourist 
(referred to as the “Company”) and what the Company expects from me. I also understand and acknowledge:  
• It is my responsibility to familiarize myself with and understand all information in this Supplement;  
• I agree to comply with the standards of c onduct in this Supplement;  
• The Company may discipline me, including termination of my employment, if I violate any Company policy;  
• I have a duty to report certain conduct as specified in the policies within this Supplement; 
• This Supplement supersedes all previously issued supplements and any inconsistent written or verbal policy 
statements made or issued before this Supplement;  
• The Company reserves the right to amend, supplement, or rescind the policies described in this Supplement or to 
modify or deviate from such policies at any time without notice. Delay or failure by the Company to enforce a 
policy or rule will not constitute a waiver of the Company’s right to do so in the future; 
• Neither this Supplement nor any other Company guidelines, policies, or practices create, or are intended to create 
a promise or representation of continued employment or an employment agreement. I understand and agree that I am employed at -will. The Company or I may terminate my employment with or without cause and with or 
witho ut notice, at any time;  
• At this time, I have no employment -related claims of unlawful conduct pending with the Company or concerns 
that I have not yet raised with a member of management, Human Resources, or the One Number; and  
• I will contact Human Resourc es with  any questions about this Supplement . 
Signature _________________________________   Date _____________________  
Name ____________________________________ 
 
  
 
 
 
  
Associate Handbook 
Maine Supplement  
  

Page | 2 
Maine Supplement  Maine Supplement  
This document supplements the Handbook for  Abercrombie & Fitch Co.  referred to as “the Company.”  Abercrombie & 
Fitch Co. is a leading specialty retailer comprised of our brands including Abercrombie & Fitch, abercrombie kids, 
HOLLISTER,  GILLY HICKS, and Social Tourist. In this Handbook  Supplement , “Abercrombie” and “the Company” refers 
generally to all our brands, and particularly to the brand for which you will be working.  
Throughout this Supplement, you are directed to various team members. Their contact information is in the Company -
wide Handbook for ease of reference. If you have concerns, suggestions, or complaints relating to your employment, 
please utilize the reporting procedures  in the Handbook and this Supplement.  
Inclusive Workplace Policies  
DISCRIMINATION , HARASSMENT , AND RETALIATION PREVENTION  
This Policy  supplements the Discrimination, Harassment, and Retaliation Prevention Policy in the Handbook . 
The Company is committed to a work environment that respects and includes all associates. In addition, consistent with 
the Company’s values, you have a right to be free from discrimination, harassment, and retaliation. In Maine, it is unlawful to engage in sexual harassment and harassment based on race, color, sex (including pregnancy and related medical conditions), sexual orientation (including gender identity or expression), disability, religion, ancestry, national origin, age, HIV/AIDS status, genetic information, membership in the National Guard or United States reserves, or because the 
associate filed a claim or asserted a right under Maine's Workers' Compensation Act or Whistleblowers' Protection Act  
If you have concerns about unfair treatment, please refer to the Discrimination, Harassment, and Retaliation Prevention 
Policy in the Handb ook and contact the One Number . While we hope that you will raise concerns with us directly so we 
can promptly investigate and resolve the matter, you may also report potential sexual harassment to the Maine Human Rights Commission:  
Maine Human Rights Comm ission  
51 State House Station  
Augusta, ME 04333- 0051  
PHONE: 207 -624-6050 
TTY/TTD: 207 -624-6064 
FAX: 207 -624-6063  
The Workday and Compensation  
MEAL BREAKS  
This Policy supplements the Meal and Rest Break Policy in the Handbook.   
This Policy  applies to non- exempt associate s only. This Policy  does not apply to exempt associates . 
Meal Breaks . If you are a non -exempt associate  and work six continuous hours or longer, you are provided and may take 
an uninterrupted, work -free, unpaid 30 -minute mea l break . 
Page | 3 
Maine Supplement  Meal and Break Waiver . With written approval from Human Resources, you may voluntarily waive your meal breaks. If 
you wish to waive a meal break, you must contact Human Resources to obtain and complete a waiver form.  
Logistics of Meal Breaks . Within the required window, the Company may schedule breaks to best accommodate operating 
requirements. If, however, your break is not scheduled in advance, please use your best judgment to decide when – within 
the required window – it is best to take your  break, based on your workload and operational demands. Please then 
attempt to contact your manager before you start your break to help the Company ensure proper staffing. If you cannot 
connect with your manager, please still proceed with your break. Breaks should occur away from your work area to the extent possible.  
Recording Meal Breaks . You must follow the timekeeping procedures set forth in the Timekeeping Policy in the Handbook . 
No Off -the-Clock Work.  During breaks, you are relieved of all work duties  and may not perform work. Working off the 
clock is strictly prohibited if you are a non -exempt associate . This also means that during breaks, you are not expected to 
be available to take assignments or respond to work messages such as text messages, telep hone calls, or emails.  
Duty to Report . No one (manager or non -manager) is permitted to prevent or discourage you from a break as described 
above. If you believe you were prevented, interrupted, or discouraged from taking all or part of a break as provided in this 
Policy, or if you experience other circumstances inconsistent w ith this Policy, you have a duty to report the circumstances 
to the One Number  immediately. You must provide: (1) your name and work location; (2) the date(s) and time(s) at issue; 
and (3) a brief description of the conduct or circumstance(s).  
The Company will promptly investigate all such reports and will take corrective action when necessary to ensure that you are provided breaks in compliance with this Policy.  You will not be retaliated against for making a good -faith report under 
this Policy.  
Time Away From Work  
FAMILY AND MEDICAL LEAVE 
We are committed to providing time off to associates  for family and medical reasons. Please refer to the Family and 
Medical Leave Policy in the HR Corkboard in PeopleSoft HR ( https://my.anfcorp.com )for more information about the 
Company’s leave -related benefits. The Company also provides leave to eligible associates  consistent with the Maine 
Family and Medical Leave Act (“MFMLA”). This Policy summarizes leave available through the MFMLA.  
Eligibility. You may take MFMLA for a Qualifying Reason if:  
(1) You have been employed for at least 12 consecutive months; and  
(2) The Company employs 15 or more associates  at a single site in Maine.  
Basic Entit lement.  Eligible associates may take up to ten workweeks of unpaid leave for Qualifying Reasons during a 24 -
month period. The 24 -month MFMLA period and/or 12 -month FMLA period is determined based on a rolling period 
measured backwards from the date the associate’s leave will be taken. The total leave will not exceed 12 weeks in a 12-
month period (FMLA) or ten weeks in a 24-month period (MFMLA), except for leave to care for an injured Servicemember, 
which will not exceed 26 weeks of leave during a single 12 -month period.  
Qualifying Reasons. In addition to the entitlements outlined in the Family and Medical Leave Policy , you may take leave 
under the MFMLA for the following reasons:  
Page | 4 
Maine Supplement  (1) To care for the associate’s domestic partner’s child after birth or placement for adoption ; 
(2) To care for the associate’s  domestic partner, sibling, grandchild,  domestic partner’s grandchild with a serious 
health condition;  
(3) To donate an organ for human organ transplant; and/or  
(4) If the associate’s  spouse, domestic partner, pa rent, sibling, or child, who is a member of state military forces or 
the United States Armed Forces (including the National Guard and Reserves), dies or incurs a serious health 
condition while on active duty.  
Unlike the FMLA, MFMLA does not cover leave for  certain qualifying exigencies or to care for the associate’s  child after 
placement for foster care.  
Leave Because of the Birth or Placement of a Child.  There is no requirement that leave because of the birth of a child or 
placement of a child with the associate  for adoption must be concluded within the 12 -month period beginning on the date 
of birth or placement.  
Protection of Group Health Insurance and O ther Benefits. If you are taking MFMLA leave, the continuation requirements 
for group health plans under the FMLA are not applicable to group health plans covered under ERISA. Therefore, if you 
are on MFMLA only leave, you likely will trigger COBRA require ments due to a reduction in hours worked.  
Use of Leave. Leave under this Policy runs concurrently with leave provided under the Family and Medical Leave Policy in the Handbook.  
Restoration of Employment and Benefits. At the end of MFMLA leave, subject to some exceptions, the Company will generally return to your same or an equivalent position with equivalent pay, benefits,  and other terms.  
No Retaliation. The Company will not tolerate against you  for requesting a leave under this Policy. If you believe you were 
retaliated against, promptly contact the One Number
.  
Page | 5 
Maine Supplement  Handbook Supplement Acknowledgment– Maine  
By signing below, I acknowledge receipt of this Handbook  Supplement  (“Supplem ent”) . I understand the practices, 
policies, and procedures described in this Supplement and the Handbook together are designed to provide a summary of 
what I can expect from my employer, Abercrombie & Fitch, abercrombie kids, HOLLISTER, GILLY HICKS, and Social tourist (referred to as the “Company”) and what the Company expects from me. I also understand and acknowledge:  
• It is my responsibility to familiarize myself with and understand all information in this Supplement;  
• I agree to comply with the standards of conduct in this Supplement;  
• The Company may discipline me, including termination of my employment, if I violate any Company policy;  
• I have a duty to report certain conduct as specified in the policies within this Supplement; 
• This Supplement supersedes all previously issued supplements and  any inconsistent written or verbal policy 
statements made or issued before this Supplement;  
• The Company reserves the right to amend, supplement, or rescind the policies described in this Supplement or to 
modif y or deviate from such policies at any time without notice. Delay or failure by the Company to enforce a 
policy or rule will not constitute a waiver of the Company’s right to do so in the future; 
• Neither this Supplement nor any other Company guidelines, po licies, or practices create, or are intended to create 
a promise or representation of continued employment or an employment agreement. I understand and agree that I am employed at -will. The Company or I may terminate my employment with or without cause and  with or 
without notice, at any time;  
• At this time, I have no employment -related claims of unlawful conduct pending with the Company or concerns 
that I have not yet raised with a member of management, Human Resources, or the One Number; and  
• I will contact  Human Resources with any questions about this Supplement . 
Signature _________________________________   Date _____________________  
Name ____________________________________ 
 
  
 
 
 
  
Associate Handbook 
Maryland Supplement  
  

Page | 2 
Maryland Supplement  Maryland Supplement  
This document supplements the Handbook for  Abercrombie & Fitch Co.  referred to as “the Company.”  Abercrombie & 
Fitch Co. is a leading specialty retailer comprised of our brands including Abercrombie & Fitch, abercrombie kids, 
HOLLISTER,  GILLY HICKS, and Social Tourist. In this Handbook  Supplement , “Abercrombie” and “the Company” refers 
generally to all our brands, and particularly to the brand for which you will be working.  
Throughout this Supplement, you are directed to various team members. Their contact information is in the Company -
wide Handbook for ease of reference. If you have concerns, suggestions, or complaints relating to your employment, 
please utilize the reporting procedures  in the Handbook and this Supplement.  
Inclusive Workplace Policies  
PREGNANCY ACCOMMODATIONS AND PREGNANCY DISCRIMINATION , HARASSMENT , AND RETALIATION 
PREVENTION  
This Policy supplements the Reasonable Accommodations  for Disabilities and the Discrimination, Harassment, and 
Retaliation Prevention Policies in the Handbook . 
The Company is committed to providing reasonable accommodations for known limitations related to pregnancy. In 
addition, consistent with the Company’s values , you have a right to be free from discrimination in relation to pregnancy, 
childbirth, and related conditions. You also have a right to reasonable accommodations and leave for a disability caused or contrib uted to by pregnancy. If you need a reasonable accommodation or if you have concerns about unfair treatment, 
please refer to the Reasonable Accommodations for Disabilities and the Discrimination, Harassment, and Retaliation Prevention Policies in the Handb ook and notify your manager, who will escalate  the request to Human Resources .  
The Workday and Compensation  
MEAL BREAKS  
This Policy supplements the Meal and Rest Break Policy in the Handbook.   
This Policy applies  to non- exempt associates  only . 
Meal Breaks . If you are a non -exempt associate , you are provided and may take uninterrupted and work -free meal breaks 
as described in the chart below.  
Length of Workday:  Number of Meal Breaks:  
Less than 4 hours  None  
More than 4 hours, up to 6 hours  One 15-minute paid meal break  or 30 -minute unpaid break  
More than 6 hours, up to 8 hours  One 30 -minute unpaid meal break  
More than 8 hours  One 30 -minute unpaid meal break plus a 15 -minute  paid  break  or 30 -minute 
unpaid break  for every additional 4 consecutive hours worked  
Meal Break Waiver . With written approval from Human Resources, you may voluntarily waive your meal break if you work 
Page | 3 
Maryland Supplement  less than six hours. If you wish to waive a meal break, you must contact Human Resources to obtain and complete a waiver 
form.  
Logistics of Meal Breaks . Withi n the required window, the Company may schedule meal and rest breaks(s) to best 
accommodate operating requirements . If, however, a break is not scheduled in advance, please use your best judgment 
to decide when – within the required window – it is best to take your breaks, based on your workload and operational 
demands. Please then attempt to contact your manager before you start your break, to help the Company ensure proper 
staffing . If you cannot connect with your manager, please still proceed with your b reak . Breaks should occur away from 
your work area to the extent possible.  
Recording Meal and Rest Breaks . You must follow the timekeeping procedures set forth in the Timekeeping Policy in the 
Handbook . 
No Off -the-Clock Work . During breaks, you are relieved of all work duties and may not perform work . Working off the 
clock is strictly prohibited . This also mean s that during breaks, you are not expected to be available to take assignments 
or respond to work messages such as text messages, telephone calls, or emails.  
Duty to Report . No one (manager or non -manager) is permitted to prevent or discourage you from tak ing a break as 
described above. If you believe you were prevented, interrupted, or discouraged from taking all or part of a  break as 
provided in this Policy, or if you experience other circumstances inconsistent with this Policy, you have a duty to report 
the circumstances to the One Number  immediately . You must provide: (1) your name and work location; (2) the date(s) 
and time(s) at issue; and (3) a brief description of the conduct or circumstance(s).  
The Company will promptly investigate all such reports and will take corrective action when necessary to ensure that all associates  are provided breaks in compliance with this Policy . You will not be retaliated against for making a report good -
faith report  under this Policy.  
BREAKS FOR NURSING /PUMPING MOTHERS IN THE CITY OF BALTIMORE  
This Policy applies to employees in the City of Baltimore.  
The Company supports associates  who chooses to breastfeed and/or express breast milk. In accordance with the Baltimor e 
City Lactation Accommodation Ordinance, we will provide a reasonable amount of break time to accommodate you if you want to express breast milk for your child.  
If you otherwise receive paid rest or break time, your lactation break time should, to the ext ent possible, run concurrently 
with that paid break time; if it cannot, break time of more than 30 minutes  will be unpaid if you are a non -exempt 
associate . 
Lactation Location . Upon request, we will provide a lactation location (other than a bathroom or closet) that is as close to 
your work area as possible. This may be the place where you normally work. The designated lactation location may also be used for other purposes (exc ept during the period when you need to express milk, in which case the primary function 
of the space will be its use as a lactation location). We will make associates who might otherwise wish to use the 
designated space aware that the room’s primary function is to serve as a lactation location (when applicable), which takes precedence over all other uses.  
Requesting a Lactation Accommodation. You have a legal right to request a lactation accommodation and can do so by 
contacting your District Manager or calling the One Number . We will respond to your request within five business days, 
and as appropriate and necessary, we will engage in an interactive process to determine lactation break schedules and an 
Page | 4 
Maryland Supplement  appropriate location. If we are not able to provide lactation breaks or a lactation location, or if we provide a lactation 
location that does not fully comply with the Ordinance or assert a waiver or variance for undue hardship, we will provide you with this information, in a written response.  
Protection Again st Retaliation. The Company will not retaliate  against you for requesting a break or accommodation 
under this Policy or if you otherwise exercise rights conferred by Baltimore’s Ordinance. If you believe you have experienced a violation of the Ordinance or this Policy, promptly contact the One Number . You may also  file a complaint 
with the Baltimore Community Relations Commission.  
Time Away From Work  
PAID SICK AND SAFE LEAVE  
For additional information about Paid Sick and Safe Leave (“PSSL”), please view the applicable poster below or contact Human Reso urces:  
English and Spanish Posters,  
https://www.dllr.state.md.us/paidleave/paidleaveposter.pdf
 
Montgomery County:  
English Poster,  
www.montgomerycountymd.gov/humanrights/Resources/ Files/EarnedSick_SavedLeave_Poster2.pdf   
Spanish Poster,  
www.montgomerycountymd.gov/humanrights/Resources/Files/EarnedSickSavedLeave_Spanish.pdf  
PARENTAL LEAVE 
We are committed to providing time off to parents following the birth or adoption of a child. To the extent the benefits 
below provide greater benefits than provided in the Handbook , the provisions below replace the corresponding provisions 
in the Handbook . If you qualify for leave under this Policy and the Parental Leave Polic y, please refer to the HR Corkboard 
in PeopleSoft HR ( https://my.anfcorp.com ), both leaves run concurrently.  
Eligibility. You are eligible for parental leave under this Policy if:  
(1) You have been  employed by the Company for at least a 12 -month period;  
(2) You have worked at least 1,250 hours during the  previous 12 months; and  
(3) The Company has between 15 and 49 associates  in Maryland. 
Leave Length . If you are eligible, you may take up to six workweeks of unpaid leave in a 12-month period.  
Usage and Notice. While parental leave is unpaid, you must use PTO benefits concurrently with a leave under this Policy. 
To the extent possible, we ask that you provide 30 days written notice of your intention to take parental leave.  
Benefit Continuation. While on parental leave, the Company will maintain coverage of a group health plan for the duration of the parental leave in the same manner that coverage would have provided if you were working. If you do not return to work after the parental leave has expired, the Company may recover premiums that we paid for maintain ing your coverage 
while on parental leave by deducting the amount of premiums paid from your final wages.  
Page | 5 
Maryland Supplement  Return from Leave . When you return to work after taking parental leave, you generally will be restored to the position 
you held when the leave began or to an equivalent position with equivalent benefits, pay, and other terms and conditions 
of employment.  
No Retaliation. The Company will not retaliate against you for requesting a leave under this Policy. If you believe you were 
retaliated against,  promptly contact the One Number .  
Page | 6 
Maryland Supplement  Handbook Supplement Acknowledgment– Maryland  
By signing below, I acknowledge receipt of this Handbook  Supplement  (“Supplement”) . I understand the practices, 
policies, and procedures described in this Supplement and the Han dbook together are designed to provide a summary of 
what I can expect from my employer, Abercrombie & Fitch, abercrombie kids, HOLLISTER, GILLY HICKS, and Social tourist 
(referred to as the “Company”) and what the Company expects from me. I also understand  and acknowledge:  
• It is my responsibility to familiarize myself with and understand all information in this Supplement;  
• I agree to comply with the standards of conduct in this Supplement; 
• The Company may discipline me, including termination of my employment, if I violate any Company policy;  
• I have a duty to report certain conduct as specified in the policies within this Supplement; 
• This Supplement supersedes all previously issued supplements and any inconsistent written or verbal policy 
statements made or issued before this Supplement;  
• The Company reserves the right to amend, supplement, or rescind the policies described in this Supplement or to 
modify or deviate from such policies at any time without notice. Delay or failure by the Company to enforce a policy or rule will not constitute a waiver of the Company’s right to do so in the future;  
• Neither this Supplement nor any other Company guidelines, policies, or practices create, or are intended to create a promise or representation of continued employment o r an employment agreement. I understand and agree that 
I am employed at -will. The Company or I may terminate my employment with or without cause and with or 
without notice, at any time;  
• At this time, I have no employment -related claims of unlawful conduct  pending with the Company or concerns 
that I have not yet raised with a member of management, Human Resources, or the One Number; and  
• I will contact Human Resources with any questions about this Supplement . 
Signature _________________________________   Date _____________________  
Name ____________________________________ 
 
  
 
 
 
  
Associate Handbook 
Massachusetts Supplement  
  

Page | 2 
Massachusetts Supplement  Massachusetts Supplement  
This document supplements the Handbook for  Abercrombie & Fitch Co.  referred to as “the Company.”  Abercrombie & 
Fitch Co. is a leading specialty retailer comprised of our brands including Abercrombie & Fitch, abercrombie kids, 
HOLLI STER,  GILLY HICKS, and Social Tourist. In this Handbook  Supplement , “Abercrombie” and “the Company” refers 
generally to all our brands, and particularly to the brand for which you will be working.  
Throughout this Supplement, you are directed to various te am members. Their contact information is in the Company -
wide Handbook for ease of reference. If you have concerns, suggestions, or complaints relating to your employment, 
please utilize the reporting procedures  in the Handbook and this Supplement.  
Inclusive Workplace Policies  
ACCOMMODATIONS AND DISCRIMINATION , HARASSMENT , AND RETALIATION PREVENTION  
This Policy supplements the Reasonable Accommodations  for Disabilities and the Discrimination, Harassment, and 
Retaliation Prevention Policies in the Handbook . 
The Company is committed to a work environment that respects and includes all associates . The Company is also 
committed to providing reasonable accomm odations for known limitations related to pregnancy and enforcing your right 
to be free from discrimination and unfair employment practices, including such conduct because of pregnancy, childbirth, or related conditions , including but not limited to lactation or the need to express breast milk for a nursing child . If you 
have concerns about unfair treatment, please refer to the Discrimination, Harassment, and Retaliation Prevention Policy in the Handbook  and contact the One Number. If you need a reasonable accommodation, please refer to the Reasonable 
Accommodations for Disabilities Policy and notify your manager, who will escalate the request to Human Resources. While we hope that you will raise concerns with us directly so we can promptly investigate and resolve the matter, you may also report potential claims to the EEOC or MCAD:  
Equal Employment Opportunity Commission 
(“EEOC”)  
J.F.K. Federal Building  
475 Government Center  
Boston, MA 02203- 0506 
800-669-4000 / 617 -565-3200  Massachusetts Commission Against D iscrimination 
(“MCAD”)  
One Ashburton Place  
RM 601  
Boston, MA 02108  
617-994-6000  
The Workday and Compensation  
MEAL BREAKS  
This Policy replaces the Meal and Rest Break Policy in the Handbook.  
Meal Breaks . If you work six or more continuous hours, you are provided and may take an uninterrupted  and work -free 
30-minute meal break . This meal break is unpaid if you are a non -exempt associate . 
Working Through a Meal Break . If the nature of business activity or other circumstances make a meal break impractical, 
you may consume an on -duty meal while performing work duties. If this occurs, please contact Human Resources to 
ensure the break is properly documented.  
Page | 3 
Massachusetts Supplement  Logistics of Meal Breaks . Within the required window, the Company may schedule breaks to best accommodat e operating 
requirements. If, however, your break is not scheduled in advance, please use your best judgment to decide when – within 
the required window – it is best to take your break, based on your workload and operational demands. Please then 
attempt to  contact your manager before you start your break to help the Company ensure proper staffing. If you cannot 
connect with your manager, please still proceed with your break. Meal breaks should occur away from your work area to 
the extent possible.  
Recording  Meal Breaks . You must follow the timekeeping procedures set forth in the Timekeeping Policy in the Handbook . 
No Off -the-Clock Work . During meal breaks, you are relieved of all work duties and may not perform work. Working off 
the clock is strictly prohibited  if you are a non -exempt associate . This also means that during breaks, you are not expected 
to be available to take assignments or respond to work messages such as text messages, telephone calls, or emails.  
Duty to Report . No one (manager or non -manage r)  is permitted to prevent or discourage you from taking a break as 
described above. If you believe you were prevented, interrupted, or discouraged from taking all or part of a break as 
provided in this Policy, or if you experience other circumstances inc onsistent with this Policy, you have a duty to report 
the circumstances to the One Number  immediately. You must provide: (1) your name and work location; (2) the date(s) 
and time(s) at issue; and (3) a brief description of the conduct or circumstance(s).  
The Company will promptly investigate all such reports and will take corrective action when necessary to ensure that you are provided breaks in compliance with this Policy.  You will not be retaliated against for making a good -faith report under 
this Policy . 
EXPENSE REIMBURSEMENT POLICY  
The Company will reimburse you for all necessary expenses and losses incurred that are directly related to your job duties. To receive reimbursement, prior to incurring the expense, you must request and receive written approv al from your 
manager or other Company representative who is authorized to approve such expenses. You must then submit a request 
for reimbursement, together with supporting receipts or other documentation, within 30 days of the date on which the expense is incurred; any expense submitted after this (30) day deadline will be presumed to be unreasonable and 
unnecessary.  
Time Away From Work and Benefits  
PAID SICK AND SAFE LEAVE  
For additional information about Paid Sick and Safe Leave (“PSSL”), please view the applicable poster below or contact 
Human Resources:  
English Poster,  
https://www.mass.gov/doc/earned -sick-time -notice -of-employee -rights -english/download  
Spanish Poster,  
https://www.mass.gov/doc/earned -sick-time -notice -of-employee -rights -spanish/download  
Page | 4 
Massachusetts Supplement  PAY CONTINUATION DURING FAMILY AND MEDICAL LEAVE 
Eligibility. You are eligible for PFML program benefits  if: you have earned at least $5 ,100 during the last four completed 
calendar quarters; you have earned at least 30 times more than how much you would be eligible to receive each week 
from your PFML benefits; and the reason for the leave is due to one of the Qualifying Reasons below. This  policy applies 
to employees working in Massachusetts and those who are former employees that have been unemployed for 26 weeks or fewer.  
Qualifying Reasons : Eligible employees may receive PFML pay continuation benefits for the following Qualifying Reasons :  
• Up to 12 weeks of pay continuation in a benefit year for the birth, adoption, or foster care placement of a child, or because of a qualifying exigency arising out of the fact that a family member is on active duty or has been notified of an impending ca ll to active duty in the Armed Forces;  
• Up to 20 weeks of pay continuation in a benefit year if you have a serious health condition that incapacitates you from work;  
• Up to 26 weeks of pay continuation in a benefit year to care for a family member who is a c overed service member 
undergoing medical treatment or otherwise addressing consequences of a serious health condition relating to their military service;  
• Up to 12 weeks of pay continuation in a benefit year to care for a family member with a serious health  condition 
and/or to manage family affairs for a family member if that family member is on active military duty in a foreign country; or  
• 26 total weeks, aggregate, of paid continuation in a single benefit year.  
Wage Replacement Benefit.  While on a qualifying leave of absence, the amount of paid leave will be based on your 
earnings, with a maximum benefit of $850 per week. In the event you are approved for a leave of absence for a Qualifying Reason, you may file a claim with the DFML to obtain paid leave benefits. The benefits described in this Policy are administered solely by DFML. You must file claims for compensation replacement with the DFML using the Department’s forms. Forms and claim instructions are available on the Department’s website: www.mass.gov/DFML
. The DFML requires 
that notice be provided to the Company prior to the filing of the application with the Department. The Department will 
not accept an application for benefits unless notice to the Company has been made. You may file an application with the 
Department no more than 60 calendar days befo re the anticipated start date of family or medical leave.  
Automatic Payroll Deduction. The Company automatically contribu tes a portion of your paycheck to the Department of 
Family Leave (“DFML”). Currently, employers with more than 25 covered individuals must remit to the DFML an effective contribution rate of 0.68% of associates’ eligible wages. Of the 0.68% total contribution amount, 0.12% of associates’ eligible wages are remitted to the family leave contribution, 0.224% of associates’ eligible wages are remitted for the medical leave contribution, and the Company also contributes 0.336% of associates’ eligible wages to th e medical leave 
contribution). The Company is responsible for remitting the funds withheld from your paycheck.   
Overlap With Other Policies . To the extent legally permitted: you must follow the leave of absence procedures outlined 
in the applicable leave p olicy in the Handbook  or the HR Corkboard in PeopleSoft HR ( https://my.anfcorp.com
); and 
benefits/a leave of absence provided through this Policy will run concurrently with other be nefits and/or leaves of absence 
provided by the Company.  
Benefits Continuation. The Company  will maintain your group health insurance coverage while you are receiving PFML 
benefits, applying the same terms and conditions as if you continued to work. This means that if you are responsible for a 
Page | 5 
Massachusetts Supplement  portion of the premiums for such coverage while working, you will continue to be responsible for the same portion of 
those premiums and for other Company benefit plan coverage while receiving PFML benefits.  
Employer Information: Below please find information about the Company which you may need when request ing paid 
leave benefits from the DFML.  
Employer Name:  Abercrombie & Fitch  
Employer Mailing Address:  Abercrombie & Fitch, P.O. Box 182168, Columbus, OH 43218 -2168 
Employer’s ID Number (“FEIN”):  31-1228829 
You may contact the DFML at: 
Charles F. Hurley Building 
19 Stanford Street, 1st Floor  
Boston, MA 02114  
617-626-6565 | www.mass.gov/DFML  
Private Plan Exemption. If the Company , now or in the future, offers paid leave with benefits that are at least as generous 
as those provided under the law, the Company may apply for an exemption from paying the DFML Family and Employment 
Security Trust Fund contribution and the Company will provide you with related plan details. The job protections described 
in this Policy apply even if the Company is approved to provide leave benefits through a private plan.  
Job Protection . Generally, if you take family or medical leave as described in this Policy, you must be restored to your 
previous position or to an equivalent position, with the same status, pay, employment benefits, length -of-service credit, 
and seniority as of the date of leave. However, if similarly situated associates  were laid off because of economic conditions 
or other operating changes  affecting employment during your leave, you may not be eligible for reinstatement to your 
prior position.  
No Retaliation . The Company will not retaliate against you for requesting a leave  under this policy. If you believe you were 
retaliated against, prom ptly contact the One Number . You may also file a civil action in the superior court within three 
years after the violation occurs.  
SMALL NECESSITIES LEAVE 
The Company provides leave to eligible associates in Massachusetts under the Massachusetts Small Nece ssities Leave Act 
(“SNLA”). The SNLA is like  the leave provided under the Family and Medical Leave Policy in the Handbook . 
Eligibility.  Eligibility for SNLA leave is the same as eligibility for FMLA leave. In other words, you must:  
(1) Have worked for the Company for at least 12 months;  
(2) Have worked 1,250 hours during the last 12 months; and  
(3) Work for a location with at least 50 associates  who work within 75 miles of the work site.  
The 12 -month period during which you can take a leave under this Policy is a r olling period, measured backward from the 
date you use SNLA leave.  
Qualifying Uses for SNLA. If you are an eligible associate , you may take up to 24 hours of unpaid leave during a 12-month 
period for Qualifying Use, such as to:  
Page | 6 
Massachusetts Supplement  (1) Participate in school activi ties directly related to educational advancement of your son or daughter, such as 
parent -teacher conferences or interviewing for a school;  
(2) Accompany your son or daughter to routine medical or dental appointments, such as checkups or vaccinations; 
and/or  
(3) Accompany an elderly relative to routine medical or dental appointments or appointments for other professional services relating to the elder’s care, such as interviewing at nursing or group homes. For purposes of this policy, an elder ly relative is an individual who is at least 60 years of age and who is related to you by blood or marriage.  
Use of SNLA Leave . To the extent you qualify for both SNLA and FMLA leave, the leaves will run concurrently. SNLA leave 
does not have to be taken consecutively. In other words, SNLA leave may be taken intermittently or on a reduced leave schedule. However, if you have PTO available, you must take such time off concurrently with SNLA leave.  
Notice and Documentation Requirements.  Whenever the need for the leave is foreseeable, you are required to provide 
your manager and the Benefits Department  with at least seven days’ notice before the date the leave is to begin. In all 
other instances, you must provide notice as soon as is practicable under the circu mstances. The Company may request 
written certification confirming the necessity for SNLA leave.  
Please contact the Benefits Hotline  for more information about SNLA leave.  
LEAVE FOR VICTIMS OF VIOLENCE  
The Company is committed to your health and safety. Sh ould you or your family member be a victim of domestic violence 
or other similarly abusive behavior, promptly contact the Benefits Department  if you need to take a leave of absence, seek  
other support , or if you need more time off than is provided in this Policy.  
Eligible Associates . You are eligible for up to 15 days of unpaid leave in a 12-month period if you or a family member is a 
victim of abusive behavior to use the leave from work to seek or obtain medical attention, counseling, victim services or 
legal assistance; secure housing; obtain a protective order from a court; appear in court or before a grand jury; meet with 
a district attorney or other law enforcement official; or attend child custody proceedings or address other issues directly 
relat ed to the abusive behavior against you or family member.  
Notice and Documentation Requirements. If you need to take time off under this Policy, you must notify your manager and the Benefits Department as soon as possible. Whenever possible, you should also  include the expected duration of 
the absence. If the need for leave is foreseeable, we ask that you make a reasonable effort to take time off in a manner that does not unduly disrupt our operations. You are not required to look for or secure a replacement to cover work hours. 
The Company may require you to provide reasonable documentation supporting the reason for the leave. Documentation 
may include, for example, a court appearance ticket or subpoena, a police report, an affidavit/letter from an attorney 
involved in the court proceeding, or an affidavit/letter from a social worker or other organization providing you with related assistance.  
No Retaliation. The Company will not retaliate against you for requesting a leave under this Policy. If you believe y ou were 
retaliated against, promptly contact the One Number . 
PARENTAL LEAVE 
We are committed to providing time off to parents following the birth or adoption of a child. To the extent the benefits 
below provide greater benefits than provided in the Handbook , the provisions below replace the corresponding provisions 
Page | 7 
Massachusetts Supplement  in the Handbook . If you qualify for leave under this Policy and the Parental Leave Policy in  HR Corkboard in PeopleSoft HR 
(https://my.anfcorp.com ), both leaves run concurrently.  
Eligibility. You a re eligible for parental leave under this Policy if you have worked full- time for the Company for three 
consecutive months.  
Parental Leave Benefit . You may take up to eight weeks of unpaid parental leave related to: giving birth; the placement 
of a child under the age of 18, or under the age of 23 if the child is mentally or physically disabled; adoption of a child; or 
the placement of a child with you pursuant to a court  order.  You may take up to eight weeks of leave for each child. If you 
and another associate  seek to take parental leave in connection with the same child, you may take a total of eight weeks 
of parental leave in the aggregate.  
Notice Requirements . You must notify your manager and the Benefits Department of the anticipated date of your leave 
at least two weeks in advance of the leave, or as soon as practicable if the delay is for reasons beyond your control. You must intend to return to work following the leave.  
Substitution of Paid Leave . While leave under this Policy is unpaid, if you have available PTO benefits, you may use such 
time concurrently with all or part of the leave.  
Coordination with Other Leaves/Benefits . Parental leave runs concurrently with leave provided under other applicable 
policy and/or law. The receipt of monetary benefits or use of PTO  during a period of parental leave does not extend the 
length of parental leave.  
Returning to Work . At the end of the parental leave period, you typically will be reinstated to your previous position or a 
similar position, with the sam e rate of pay as before you went on leave. There are, however, some circumstances under 
which the Company may not be able to provide reinstatement. While parental leave may be extended, unless otherwise provided by applicable law, reinstatement may not be guaranteed at the conclusion of a parental leave that lasts more than eight weeks.  
No Retaliation. The Company will not retaliate against you for requesting a leave under this Policy. If you believe you were 
retaliated against, promptly contact the One Number.  
MILITARY LEAVE 
This Policy supplements the Military Leave Policy in the Handbook. 
The Company recognizes that you may need to be absent from work to serve in the military. If you need a related unpaid leave of absence, please refer to the Military Leave in the Handbook . In addition, you may be eligible for reemployment 
after military le ave if the following notice provisions are followed:  
• If military service was for less than 31 days, you must report to work on the first regularly scheduled workday that is at least eight hours after you return home from service;  
• If the military service wa s for 31 -180 days, you must apply for reemployment within 14 days following completion 
of service;  
• If the military service was for more than 180 days, you must apply for reemployment within 90 days following completion of military service;  
Page | 8 
Massachusetts Supplement  • If you suffered a service -connected injury or illness and you are hospitalized or convalescing, you have up to two 
years following completion of military service to return to your position or apply for reemployment, depending 
on the length of recovery time required; or  
• If you are unable to comply with the reporting schedule above or if you are injured or recovering from an injury 
and need an accommodation for specific circumstances beyond your control, contact the Benefits Department  as 
soon as possible to determine if you are eligible for a reasonable accommodation or additional time to apply for 
reemployment.  
You will typically be reinstated to your previous position or a similar position, with the same seniority and benefits as before you went on leave. However, please n ote that this Policy does not require the Company to reemploy individuals 
who are not eligible for reemployment under applicable law.  
The Company will not retaliate against you for requesting a leave under this Policy. If you believe you were retaliated 
against, promptly contact the One Number . 
Health and Safety  
WORKERS ’ COMPENSATION  
The Company provides workers’ compensation benefits for the protection of associates with work -related injuries or 
illness. If you experience a work -related injury or illness,  immediately contact the Risk Management Department following 
the reporting procedures in the Handbook.    
Page | 9 
Massachusetts Supplement  Handbook Supplement Acknowledgment– Massachusetts 
By signing below, I acknowledge receipt of this Handbook  Supplement  (“Supplement”) . I understand the practices, 
policies, and procedures described in this Supplement and the Handbook together are designed to provide a summary of 
what I can expect from my employer, Abercrombie & Fitch, abercrombie kids, HOLLISTER, GILLY HICKS, and Social tourist (referred to as the “Company”) and what the Company expects from me. I also understand and acknowledge:  
• It is my responsibility to familiarize myself with and understand all information in this Supplement;  
• I agree to comply with the  standards of conduct in this Supplement;  
• The Company may discipline me, including termination of my employment, if I violate any Company policy;  
• I have a duty to report certain conduct as specified in the policies within this Supplement; 
• This Supplement supersedes all previously issued supplements and any inconsistent written or verbal policy 
statements made or issued before this Supplement;  
• The Company reserves the right to amend, supplement, or rescind the policies described in this Supplement or to 
modi fy or deviate from such policies at any time without notice. Delay or failure by the Company to enforce a 
policy or rule will not constitute a waiver of the Company’s right to do so in the future; 
• Neither this Supplement nor any other Company guidelines, policies, or practices create, or are intended to create a promise or representation of continued employment or an employment agreement. I understand and agree that I am employed at -will. The Compan y or I may terminate my employment with or without cause and with or 
without notice, at any time;  
• At this time, I have no employment -related claims of unlawful conduct pending with the Company or concerns 
that I have not yet raised with a member of manage ment, Human Resources, or the One Number; and  
• I will contact Human Resources with any questions about this Supplement . 
Signature _________________________________   Date _____________________  
Name ____________________________________ 
 
  
 
 
 
 
 
Associate Handbook 
Michigan Supplement  
  

Page | 2 
Michigan Supplement  Michigan Supplement  
This document supplements the Handbook for  Abercrombie & Fitch Co.  referred to as “the Company.”  Abercrombie & 
Fitch Co. is a leading specialty retailer comprised of our brands including Abercrombie & Fitch, abercrombie kids, 
HOLLISTER,  GILLY HICKS, and Social Tourist. In this Handbook  Supplement , “Abercrombie” and “the Company” refers 
generally to all our brands, and particularly to the brand for which you will be working.  
Throughout this Supplement, you are directed to various team members. Their contact information is in the Company -
wide Handbook for ease of reference. If you have concerns, suggestions, or complaints relating to your employment, 
please utilize the reporting procedures  in the Handbook and this Supplement.  
Inclusive Workplace Policies  
REASONABLE ACCOMMODATIONS  
This Policy supplements the Reasonable Accommodations for Disabilities Policy in the Handbook . 
If you need a reasonable accommodation, please refer to the Reasonable Accommodations for Disabilities Policy in the Handbook  and notify your manager, who will escalate the request to Human Resources. In addition, please note that 
under Michigan’s Persons with Disabilities Civil Rights Act, a person with a disability may allege a violation against the Company regarding a failure to accommodate under the Persons with Disabilities Civil Rights Act only if the person with a disability notifies the Company in writing of the need for accommodation within 182 days after the date the person with a disability knew or reasonably should have known that an accommodation was needed.  
Employment Expectations  
SOCIAL SECURITY NUMBER PRIVACY  
The Company is dedicated to protecting the confidentiality of our associates ’ social security numbers (“SSN”). 
Limited Access Protocol . The Company does the following to prevent unauthorized disclosure  of SSNs and to maintain 
confidentiality of documents with SSNs:  
• Prohibits unlawful or unauthorized disclosure of associates ’ SSNs;  
• Limits the number of people with access to associates ’ SSNs, and the circumstances under which associate  SSNs 
may be accesse d; 
• Ensures proper disposal of documents (hard copy or digital) containing associate  SSNs; and  
• Disciplines associates  who violate  this Policy.  
Files with associate  SSNs are maintained under lock, and access to digital files are password protected. Only individuals 
with a legitimate business need to access documents with your SSN may view the documents. Access to documents with your SSN by anyone other than Human Resources must be specifically authorized, in writing, by either Human Resources or you.  
Document retention and destruction protocols . Documents containing your SSN will be disposed of in accordance with 
the Company’s document retention policies and procedure s. 
Page | 3 
Michigan Supplement  Policy violations . Violations of this Policy will result in disciplinary action up to and including termination of employment.  
Time Away From Work  
PAID SICK AND SAFE LEAVE  
For additional information about Paid Sick and Safe Leave (“PSSL”), please view t he applicable poster below or contact 
Human Resources:  
English Poster,  
https://www.michigan.gov/ -/media/Project/Websites/leo/Documents/WAGE -HOUR/WHD -99xx -Information -
Sheets/WHD -9911 -PMLA -
Poster/Paid_Medical_Leave_Act_Poster_9911_English.pdf?rev=764ee47c1ed442bd9ac1d904eb042ea7  
Spanish Poster,  
https://www.michigan.gov/leo/ -/media/Project/Websites/leo/Documents/WAGE -HOUR/WHD -99xx -Information -
Sheets/WHD -9911 -PMLA -
Poster/Paid_Medical_Leave_Act_Poster_9911_Spanish.pdf?rev=80d097742ea2424ab110be5ed6678bb8&hash=E5787E
BF6EA8BC5423E513D3CB4E1308  
  
Page | 4 
Michigan Supplement  Handbook Supplement Acknowledgment– Michigan  
By signing below, I acknowledge receipt of this Handbook  Supplement  (“Supplement”) . I understand the practices, 
policies, and procedures described in this Supplement and the Handbook together are designed to provide a summary of 
what I can expect from my employer, Abercrombie & Fitch, abercrombie kids, HOLLISTER, GILLY HICKS, and Social  tourist 
(referred to as the “Company”) and what the Company expects from me. I also understand and acknowledge:  
• It is my responsibility to familiarize myself with and understand all information in this Supplement;  
• I agree to comply with the standards of c onduct in this Supplement;  
• The Company may discipline me, including termination of my employment, if I violate any Company policy;  
• I have a duty to report certain conduct as specified in the policies within this Supplement; 
• This Supplement supersedes all previously issued supplements and any inconsistent written or verbal policy 
statements made or issued before this Supplement;  
• The Company reserves the right to amend, supplement, or rescind the policies described in this Supplement or to 
modify or deviate from such policies at any time without notice. Delay or failure by the Company to enforce a policy or rule will not constitute a waiver of the Company’s right to do so in the future; 
• Neither this Supplement nor any other Company guidelines, policies, or practices create, or are intended to create a promise or representation of continued employment or an employment agreement. I understand and agree that I am employed at -will. The Company or I may terminate my employment with or without cause and with or 
witho ut notice, at any time;  
• At this time, I have no employment -related claims of unlawful conduct pending with the Company or concerns 
that I have not yet raised with a member of management, Human Resources, or the One Number; and  
• I will contact Human Resourc es with any questions about this Supplement . 
Signature _________________________________   Date _____________________  
Name ____________________________________ 
 
  
 
 
 
 
 
Associate Handbook 
Minnesota Supplement  
  

Page | 2 
Minnesota Supplement  Minnesota Supplement  
This document supplements the Handbook for  Abercrombie & Fitch Co.  referred to as “the Company.”  Abercrombie & 
Fitch Co. is a leading specialty retailer comprised of our brands including Abercrombie & Fitch, abercrombie kids, 
HOLLISTER,  GILLY HICKS, and Social Tourist. In this Handbook  Supplement , “Abercrombie” and “the Company” refers 
generally to all our brands, and particularly to the brand for which you will be working.  
Throughout this Supplement, you are directed to various team members. Their contact information is in the Company -
wide Handbook for ease of reference. If you have concerns, suggestions, or complaints relating to your employment, 
please utilize the reporting procedures  in the Handbook and this Supplement.  
The Workday and Compensation  
BREAKS FOR NURSING /PUMPING MOTHERS  
The Company supports associates  who choose to breastfeed and will pay you for all such reasonable break time. As a nursing 
mother, you should attempt to schedule lactation breaks around your work and break schedule; such breaks may be scheduled 
as frequently as necessary and may last un til you have completed the expression of requisite milk. The Company recognizes 
that your break schedule may need to vary over time, and we will do our best to accommodate such needs.  
If you believe that you have not been provided reasonable break time and /or adequate space, you must contact the One 
Number . The Company will not retaliate against you for requesting an accommodation under this Policy. If you believe you 
were retaliated against, you should promptly contact the One Number . 
MEAL BREAKS  
This Policy replaces the Meal and Rest Break Policy in the Handbook.  
Meal Breaks . If you work eight or more consecutive hours, you are  provided and may take an uninterrupted and work -
free 30 -minute meal break . This meal break is unpaid if you are a non -exempt associate . 
Logistics of Meal Breaks . Within the required window, the Company may schedule breaks to best accommodate operating 
requirements. If, however, your break is not scheduled in advance, please use your best judgment to decide when – within 
the required window – it is best to take your break, based on your workload and operational demands. Please then 
attempt to contact your manager before you start your break to help the Company ensure proper staffing. If you cannot 
connect with your manager, pl ease still proceed with your break. Meal breaks should occur away from your work area to 
the extent possible.  
Recording Meal Breaks . You must follow the timekeeping procedures set forth in the Timekeeping Policy in the Handbook . 
No Off-the-Clock Work . During meal breaks, you are relieved of all work duties and may not perform work. Working off 
the clock is strictly prohibited  if you are a non -exempt associate . This also means that during breaks, you are not expected 
to be available t o take assignments or respond to work messages such as text messages, telephone calls, or emails.  
Duty to Report . No one (manager or non -manager) is permitted to prevent or discourage you from taking a break as 
described above. If you believe you were prev ented, interrupted, or discouraged from taking all or part of a break as 
provided in this Policy, or if you experience other circumstances inconsistent with this Policy, you have a duty to report 
Page | 3 
Minnesota Supplement  the circumstances to the One Number  immediately. You must provide: (1) your name and work location; (2) the date(s) 
and time(s) at issue; and (3) a brief description of the conduct or circumstance(s).  
The Company will promptly investigate all such reports and will take corrective action when necessary to ensure tha t you 
are provided breaks in compliance with this Policy.  You will not be retaliated against for making a good -faith report under 
this Policy.  
Employment Expectations  
WAGE DISCLOSURE PROTECTIONS  
Under the Minnesota Wage Disclosure Protection law, you have the right to tell anyone  the amount of your own wages. 
The Company will not and cannot retaliate against you for disclosing your own wages. Your remedies under the Wage 
Disclosure Protection law are to bring a civil action against your employer and/or file a complaint with the Minnesota 
Department of Labor and Industry at 651 -284-5070 or 800 -342-5354.  
MINIMUM WAGE NOTICE FOR ST. PAUL ASSOCIATES  
Paying associates properly is important to the Company. If you believe you were improperly paid, please  contact the 
Payroll Department  immediately to resolve the issue. Please refer to the Payroll Policy in the Handbook  for additional 
information about reporting concerns regarding inaccurate pay statements. Pursuant to Chapter 224 of the St. Paul Code 
of Ordinances, you are entitled to the payment of the applicable minimum wage, and you have the right to report a violation or suspected violation of the Ordinance or the denial of minimum wage payment.  You may also contact or file a 
complaint with the City of St. Paul’s Department of Human Rights and Equal Economic Opportunity (15 Kellogg Blvd. West 
| Saint Paul, MN 55102 | 651 -266-8989 | laborstandards@ci.stpaul.mn.us
) or in  court.  
The Company will not retaliate against you if you bring forward a good -faith question or concern regarding hours worked , 
pay, or otherwise report an alleged policy violation.  
PERSONNEL RECORDS  
This Policy supplements the Personnel Records Policy  in the Handbook.  
If you wish to review or receive copies of your personnel file , contact your District Manager. You may review your 
personnel record once every six months.  The Company will typically provide an opportunity for review of personnel 
records within seven working days of the written request, or if the personnel record is physically located outside of 
Minnesota, within 14 working days of the written request.  
What is contained in the personnel record is carefully defined under Minnesota law. The law does not require that we allow you to review and copy information that is not contained in your personnel record. If you wish to dispute information contained in your personnel record, you may submit a request to have it removed from  the record. If we do not agree that 
the information should be removed, a written response to the information of up to five pages may be submitted.  
The Company will not retaliate against you for appropriately asserting your rights to review your personnel record. If your 
rights to review your personnel file are improperly denied, the law provides certain remedies.  
For more information, the Minnesota statutes further detailing these rights can be found at Minnesota Statutes § 181.960 
through Minnesota Statut es § 181.965. These laws can be found on the internet at 
Page | 4 
Minnesota Supplement  http://www.leg.state.mn.us/leg/statutes.asp  or in public libraries throughout the state. By signing the en closed 
Acknowledgement, you acknowledge and agree that you were provided with the information in this Policy.  
Time Away From Work  
PAID SICK AND SAFE LEAVE FOR ASSOCIATES  IN DULUTH , MINNESOTA  
For additional information about Paid Sick and Safe Leave (“PSSL” ), please view the applicable poster below or contact 
Human Resources:  
Duluth: 
English Poster,  
duluthmn.gov/media/12046/esst -poster.pdf  
Spanish Poster,  
https://duluthmn.gov/media/12045/esst -poster -spanish- version.pdf  
Minneapolis: English Poster,  
http://sicktimeinfo.minneapolismn.gov/uploads/9/6/3/1/96313024/wage_theft_notice_poster_final_11_19_19.pdf
 
Spanish Poster, 
http://sicktimeinfo.minneapolismn.gov/uploads/9/6/3/1/96313024/wage_theft_notice_poster_spanish_final_11_19_1
9.pdf  
St. Paul:  
English Poster, 
www.stpaul.gov/sites/default/files/Media%20Root/Human%20Rights%20%26%20Equal%20Economic%20Opportunity/E
SST-Worplace%20Notice_English_Final.pdf  
Spanish Poster, 
www.stpaul.gov/sites/default/files/Media%20Root/Human%20Rights%20%26%20Equal%20Economic%20Opportunity/E
SST-Worplace%20Notice_Spanish_Final.pdf  
PARENTAL LEAVE 
We are committed to providing time off to parents following the birth or adoption of a child as well as to associates for 
medical conditions related to pregnancy. Please refer to the Parental Leave  and Family and Medical Leave  policies  in the 
HR Corkboard in PeopleSoft HR ( https://my.anfcorp.com ) and the Reasonable Accommodations for Disabilities polic y in 
the Handbook for information regarding related leaves. In addition to these policies, the Company provides leave to 
associates  who are eligible for leave under the Minnesota Parental Leave Act (“MPLA”), which is like the leave provided 
under the Family and Medical Leave Act . The Policy below provides an overview of leave available under the MPLA. To the 
extent that you  are eligible for a lea ve under both the MPLA and FMLA, both leaves will run concurrently.  
Eligibility. To be eligible for leave under the MPLA:  
(1) You must have worked for the Company for at least 12 months;  
(2) You must have worked at least half the full -time equivalent position for your job during the 12 -month period 
immediately preceding the request for leave; and  
Page | 5 
Minnesota Supplement  (3) The Company must have 21 or more associates at a single location.  
Qualifying Reasons . You may take up to 12 weeks of unpaid MPLA leave for the following Qualifying Reasons:  
(1) The birth or placement for adoption of a child (but not foster care placement); or  
(2) Prenatal care or incapacity due to pregnancy, childbirth, or related health conditions.  
Leave for the birth or adoption of a child must occur within 12 months  after the birth or adoption, except that where the 
child must remain in the hospital longer than the mother, in which case the leave must be taken no later than 12 months 
after the child leaves the hospital.  
Protection of Group Health Insurance . During a period of leave pursuant to the MPLA, you may continue health insurance 
coverage, but you may be required to pay the full cost of coverage.  
Returning to Work . You will typically be reinstated to your previous position or a similar position, with the same s eniority 
and benefits as before you went on leave.  
No Retaliation. The Company will not retaliate against you for requesting a leave under this Policy. If you believe you were retaliated against, promptly contact the One Number . 
 
Page | 6 
Minnesota Supplement  Handbook Supplement Acknowledgment–Minnesota 
By signing below, I acknowledge receipt of this Handbook  Supplement  (“Supplement”) . I understand the practices, 
policies, and procedures described in this Supplement and the Handbook together are designed to provide a summary of 
what I can expect from my employer, Abercrombie & Fitch, abercrombie kids, HOLLISTER, GILLY HICKS, and Social  tourist 
(referred to as the “Company”) and what the Company expects from me. I also understand and acknowledge:  
• It is my responsibility to familiarize myself with and understand all information in this Supplement;  
• I agree to comply with the standards of c onduct in this Supplement;  
• The Company may discipline me, including termination of my employment, if I violate any Company policy;  
• I have a duty to report certain conduct as specified in the policies within this Supplement; 
• This Supplement supersedes all previously issued supplements and any inconsistent written or verbal policy 
statements made or issued before this Supplement;  
• The Company reserves the right to amend, supplement, or rescind the policies described in this Supplement or to 
modify or deviate from such policies at any time without notice. Delay or failure by the Company to enforce a policy or rule will not constitute a waiver of the Company’s right to do so in the future; 
• Neither this Supplement nor any other Company guidelines, policies, or practices create, or are intended to create a promise or representation of continued employment or an employment agreement. I understand and agree that I am employed at -will. The Company or I may terminate my employment with or without cause and with or 
witho ut notice, at any time;  
• At this time, I have no employment -related claims of unlawful conduct pending with the Company or concerns 
that I have not yet raised with a member of management, Human Resources, or the One Number; and  
• I will contact Human Resourc es with any questions about this Supplement . 
Signature _________________________________   Date _____________________  
Name ____________________________________ 
 
  
 
 
 
 
 
Associate Handbook 
Missouri Supplement  
  

Page | 2 
Missouri Supplement  Missouri Supplement  
This document supplements the Handbook for  Abercrombie & Fitch Co.  referred to as “the Company.”  Abercrombie & 
Fitch Co. is a leading specialty retailer comprised of our brands including Abercrombie & Fitch, abercrombie kids, 
HOLLISTER,  GILLY HICKS, and Social Tourist. In this Handbook  Supplement , “Abercrombie” and “the Company” refers 
generally to all our brands, and particularly to the brand for which you will be working.  
Throughout this Supplement, you are directed to various team members. Their contact information is in the Company -
wide Handbook for ease of reference. If you have concerns, suggestions, or complaints relating to your employment, 
please utilize the reporting procedures  in the Handbook and this Supplement.  
Time Away From Work  
LEAVE FOR VICTIMS OF VIOLENCE  
The Company is committed to your health and safet y. Should you or your family member be a victim of domestic violence 
or other similarly abusive behavior, promptly communicate with the Benefits Department if you need to take a leave of absence, seek other support, or if you need more time off than is pro vided in this Policy.  
Eligible Associate s. If you experience a Qualifying Reason for leave as summarized below, you may take up to two weeks 
of unpaid leave within a 12 -month period.  
Qualifying Reasons for Leave. Eligible associate s may take leave to:  
• Seek medical attention for, or to recover from, physical or psychological injuries caused by domestic or sexual violence;  
• Obtain services from a victim services organization;  
• Obtain psychological or other counseling;  
• Participate in safety planning, temporarily or permanently relocate, or take other actions to increase the safety of yourself, family, or household; or  
• Seek legal assistance or remedies to ensure health and safety.  
Notice and Documentation Requirements. If you need to take time off under this P olicy, you must notify your manager 
and the Benefits Department as soon as possible. Whenever possible, you should also include the expected duration of the absence. If the need for leave is foreseeable, we ask that you make a reasonable effort to take time off in a manner that does not unduly disrupt our operations. You are not required to look for or secure a replacement to cover work hours. The Company may require you to provide reasonable documentation supporting the reason for the leave. Documentation may include, for example, a court appearance ticket or subpoena, a police report, an affidavit/letter from an attorney involved in the court proceeding, or an affidavit/letter from a social worker or other organization providing you with related assistance . 
No Retaliation. The Company will not retaliate against you for requesting a leave under this Policy. If you believe you were retaliated against, promptly contact the One Number.  
Additional Notice. For additional information about related benefits, please  click on the link below:  
Page | 3 
Missouri Supplement  https://labor.mo.gov/sites/labor/files/DLS/LS_112_Poster_f_0.pdf  
  
Page | 4 
Missouri Supplement  Handbook Supplement Acknowledgment– Missouri  
By signing below, I acknowledge receipt of this Handbook  Supplement  (“Supplement”) . I understand the practices, 
policies, and procedures described in this Supplement and the Handbook together are designed to provide a summary of 
what I can expect from my emplo yer, Abercrombie & Fitch, abercrombie kids, HOLLISTER, GILLY HICKS, and Social tourist 
(referred to as the “Company”) and what the Company expects from me. I also understand and acknowledge:  
• It is my responsibility to familiarize myself with and understand  all information in this Supplement;  
• I agree to comply with the standards of conduct in this Supplement; 
• The Company may discipline me, including termination of my employment, if I violate any Company policy;  
• I have a duty to report certain conduct as specified in the policies within this Supplement; 
• This Supplement supersedes all previously issued supplements and inconsistent written or verbal policy 
statements made or issued before this Supplement;  
• The Company reserves the right to amend, supplement, or rescind the policies described in this Supplement or to 
modify or deviate from such policies at any time without notice. Delay or failure by the Company to enforce a policy or rule will not constitute a waiver of the Company’s right to do so in the futu re; 
• Neither this Supplement nor any other Company guidelines, policies, or practices create, or are intended to create a promise or representation of continued employment or an employment agreement. I understand and agree that I am employed at -will. The Compan y or I may terminate my employment with or without cause and with or 
without notice, at any time;  
• At this time, I have no employment -related claims of unlawful conduct pending with the Company or concerns 
that I have not yet raised with a member of manage ment, Human Resources, or the One Number; and  
• I will contact Human Resources with any questions about this Supplement . 
Signature _________________________________   Date _____________________  
Name ____________________________________ 
 
  
 
 
 
  
Associate Handbook 
Nevada Supplement  
  

Page | 2 
Nevada Supplement  Nevada Supplement  
This document supplements the Handbook for  Abercrombie & Fitch Co.  referred to as “the Company.”  Abercrombie & 
Fitch Co. is a leading specialty retailer comprised of our brands including Abercrombie & Fitch, abercrombie kids, 
HOLLISTER,  GILLY HICKS, and Social Tourist. In this Handbook  Supplement , “Abercrombie” and “the Company” refers 
generally to all our brands, and particularly to the brand for which you will be working.  
Throughout this Supplement, you are directed to various team members. Their contact information is in the Company -
wide Handbook for ease of reference. If you have concerns, suggestions, or complaints relating to your employment, 
please utilize the reporting procedures  in the Handbook and this Supplement.  
Inclusive Workplace Policies  
PREGNANCY ACCOMMODATIONS AND PREGNANCY DISCRIMINATION , HARASSMENT , AND RETALIATION 
PREVENTION  
This Policy supplements the Reasonable Accommodations  for Disabilities and the Discrimination, Harassment, and 
Retaliation Prevention Policies in the Handbook . 
Consistent with the Company’s values and in compliance wi th the Nevada Pregnant Workers Fairness Act, you have a right 
to be free from discrimination and unfair employment practices because of pregnancy, childbirth, or related conditions. 
The Company is committed to providing reasonable accommodations for known limitations related to pregnancy. If you 
need a reasonable accommodation or if you have concerns about unfair treatment, please refer to the Reasonable 
Accommodations for Disabilities and the Discrimination, Harassment, and Retaliation Prevention Policies in the Handbook  
and notify your manager, who will escalate the request to Human Resources . 
The Workday and Compensation  
MEAL AND REST BREAKS  
This Policy replaces  the Meal and Rest Break Policy in the Handbook.  
Rest Breaks . If you work at least 3.5 continuous hours, you are provided and may take an uninterrupted, work -free, and 
paid ten -minute rest break during each four -hour (or major fraction thereof) work period as described in the chart below.  
Length of Workday:  Number of Rest Breaks:  
Less than 3.5 hours  None  
At least 3.5 hours, up to 7 hours  One 10 -minute rest break  
More than 7 hours, up to 11 hours  Two 10 -minute rest breaks  
More than 11 hours, up to 15 hours  Three 10 -minute rest breaks  
Meal Breaks . If you work eight or more continuous hours, you are provided and may take an uninterrupted  and work -free 
30-minute meal break . This break is unpaid if you are a non -exempt associate . 
Page | 3 
Nevada Supplement  Meal Break Waiver . With written approval from Human Resources, you may voluntarily waive your meal break. If you 
wish to waive a meal break, you must contact Human Resources to obtain and complete a waiver form. 
Logistics of Meal and Rest Breaks . Within the required window, the Company may schedule breaks to best accommodate 
operating requirements. If, however, your break is not scheduled in advance, please use your best judgment to decide 
when – with in the required window – it is best to take your break, based on your workload and operational demands. 
Please then attempt to contact your manager before you start your break to help the Company ensure proper staffing. If 
you cannot connect with your mana ger, please still proceed with your breaks. Meal and/or rest breaks should occur away 
from your work area to the extent possible.  
Recording Meal and Rest Breaks . You must follow the timekeeping procedures set forth in the Timekeeping Policy in the 
Handbook . 
No Off -the-Clock Work . During these breaks, you are relieved of all work duties and may not perform work. Working off 
the clock is strictly prohibited  if you are a non -exempt associate . This also means that during breaks, you are not expected 
to be available to take assignments or respond to work messages such as text messages, telephone calls, or emails.  
Duty to Report . No one (manager or non -manager) is permitted to prevent or discourage you from taking a break as 
described above. If you believe you wer e prevented, interrupted, or discouraged from taking all or part of a break as 
provided in this Policy, or if you experience other circumstances inconsistent with this Policy, you have a duty to report the circumstances to the One Number  immediately. You m ust provide: (1) your name and work location; (2) the date(s) 
and time(s) at issue; and (3) a brief description of the conduct or circumstance(s).  
The Company will promptly investigate all such reports and will take corrective action when necessary to ensu re that you 
are provided breaks in compliance with this Policy.  You will not be retaliated against for making a good -faith report under 
this Policy.  
Time Away From Work  
PAID TIME OFF 
This Policy supplements the current PTO  Policy  to the extent this Policy provides greater benefits than provided in the 
PTO policy in the Handbook.   
PTO Accruals. If you are not otherwise eligible to accrue PTO  in a given pay -period under the PTO Policy (including during 
the first year of employment),  you will accrue PTO  at the rate of 0.01923 hours per hour worked.  
PTO Use. If you are not otherwise eligible to use PTO until completion of one year of employment, you may begin using 
accrued PTO upon completion of 90 days of employment.  
Compliance with N evada Law.  You must contact the One Number  if you believe that you were : (1) denied the right to use 
paid leave available for use in accordance with Nevada law; (2) required to find a replacement worker as a condition of using paid leave available; or (3) subjected to retaliation for using paid leave.  
  
Page | 4 
Nevada Supplement  Handbook Supplement Acknowledgment– Nevada 
By signing below, I acknowledge receipt of this Handbook  Supplement  (“Supplement”) . I understand the practices, 
policies, and procedures described in this Supplement and the Handbook together are designed to provide a summary of 
what I can expect from my employer, Abercrombie & Fitch, abercrombie kids, HOLLISTER, GILLY HICKS, and Social  tourist 
(referred to as the “Company”) and what the Company expects from me. I also understand and acknowledge:  
• It is my responsibility to familiarize myself with and understand all information in this Supplement;  
• I agree to comply with the standards of c onduct in this Supplement;  
• The Company may discipline me, including termination of my employment, if I violate any Company policy;  
• I have a duty to report certain conduct as specified in the policies within this Supplement; 
• This Supplement supersedes all previously issued supplements and any inconsistent written or verbal policy 
statements made or issued before this Supplement;  
• The Company reserves the right to amend, supplement, or rescind the policies described in this Supplement or to 
modify or deviate from such policies at any time without notice. Delay or failure by the Company to enforce a policy or rule will not constitute a waiver of the Company’s right to do so in the future; 
• Neither this Supplement nor any other Company guidelines, policies, or practices create, or are intended to create a promise or representation of continued employment or an employment agreement. I understand and agree that I am employed at -will. The Company or I may terminate my employment with or without cause and with or 
witho ut notice, at any time;  
• At this time, I have no employment -related claims of unlawful conduct pending with the Company or concerns 
that I have not yet raised with a member of management, Human Resources, or the One Number; and  
• I will contact Human Resourc es with any questions about this Supplement . 
Signature _________________________________   Date _____________________  
Name ____________________________________ 
 
  
 
 
 
 
 
Associate Handbook 
New Hampshire Supplement  
  

Page | 2 
New Hampshire Supplement  New Hampshire Supplement  
This document supplements the Handbook for  Abercrombie & Fitch Co.  referred to as “the Company.”  Abercrombie & 
Fitch Co. is a leading specialty retailer comprised of our brands including Abercrombie & Fitch, abercrombie kids, 
HOLLISTER,  GILLY HICKS, and Social Tourist. In this Handbook  Supplement , “Abercrombie” and “the Company” refers 
generally to all our brands, and particularly to the brand for which you will be working.  
Throughout this Supplement, you are directed to various team members. Their contact information is in the Company -
wide Handbook for ease of reference. If you have concerns, suggestions, or complaints relating to your employment, 
please utilize the reporting procedures  in the Handbook and this Supplement.  
The Workday and Compensation  
MEAL BREAKS  
This replaces the Meal and Rest Break Policy in the Handbook.  
Meal Breaks . If you  are an exempt associate  and work more than five consecutive hours, you are provided and may take 
an uninterrupted and work -free 20-minute meal break. If you are a non -exempt associate  and work more than five 
consecutive hours,  you are provided and may take an uninterrupted, work -free, and unpaid 30-minute meal break . 
Meal Break Waiver . With written approval from Human Resources, you may voluntarily waive meal and rest breaks under 
the circumstances that follow. If you wish to waive a meal break, you must contact Human Resources to obtain and complete a waiver form.  
Logistics of Meal Breaks . Within the required window, the Company may schedule breaks to best accommodate operating 
requirements. If, however, your break is not sche duled in advance, please use your best judgment to decide when – within 
the required window – it is best to take your break, based on your workload and operational demands. Please then 
attempt to contact your manager before you start your break to help the  Company ensure proper staffing. If you cannot 
connect with your manager, please still proceed with your break. Meal breaks should occur away from your work area to the extent possible.  
Recording Meal Breaks . You must follow the timekeeping procedures set forth in the Timekeeping Policy in the Handbook . 
No Off -the-Clock Work . During these breaks, you are relieved of all work duties and may not perform work. Working off 
the clock is strictly prohibited  if you are a non -exempt associate . This also means that during breaks, you are not expected 
to be available to take assignments or respond to work messages such as text messages, telephone calls, or emails.  
Duty to Report . No one (manager or non -manager) is permitted to prevent or discourage you from taking a break as 
described above. If you believe you were prevented, interrupted, or discouraged from taking all or part of a break as 
provided in this Policy, or if you experience other circumstances inconsistent with this Policy, you have a duty to report 
the cir cumstances to the One Number  immediately. You must provide: (1) your name and work location; (2) the date(s) 
and time(s) at issue; and (3) a brief description of the conduct or circumstance(s).  
The Company will promptly investigate all such reports and will take corrective action when necessary to ensure that you 
are provided breaks in compliance with this Policy.  You will not be retaliated against for making a good -faith report under 
this Policy.  
Page | 3 
New Hampshire Supplement  COMPENSATION NOTICE  
By signing the enclosed Acknowledgement, you  agree and acknowledge that you were  provided , during the onboarding 
process,  information regarding you r pay rate , pay calculation , and timing of pay.  
Time Away From Work  
PREGNANCY DISABILITY LEAVE  
Following the birth of a child, you may take an unpaid leave of absence under this Policy for the period of temporary 
physical disability resulting from pregnancy, childbirth, or related medical conditions.  Leave under this Policy begins when 
you are medically determine d to be disabled and ends when you are medically determined to be able to return to work.  
Requests for leave must be submitted in writing and approved in advance by Human Resources.  If you request such leave 
for more than six weeks, you must provide the Co mpany with certification from a physician providing that you are disabled 
from working.  
You must substitute available PTO benefits during unpaid leave taken under this Policy.  Pregnancy disability leave will run 
concurrently with FMLA leave, as applicable,  and other related leave provided/as permitted by applicable law.  
During a pregnancy disability leave, the Company will maintain your health insurance benefits under the same terms and conditions applicable to associates
 not on leave if you continue your r egular associate  contributions to these plans on a 
timely basis.  If you are on a leave and not eligible for FMLA leave, or if you have exhausted your FMLA leave, you will be 
responsible for paying your portion of the insurance coverage premiums in advance each month. Failure to do so may 
result in loss of coverage and possible refusal by the insurance carrier(s) to allow coverage to be reinstated.  
If you return to work following leave of absence provided under this Policy, you will be considered as having had continuous employment for purposes of seniority and other benefits based upon years of service. When you can  return 
to work, the Company will return you to your original job if available or a comparable position if business necessities permit. The Company does not guarantee that your job will remain available or that a comparable position will exist when returning from a pregnancy disability lea ve. 
If you have questions about this Policy, please contact the One Number.  
Page | 4 
New Hampshire Supplement  Handbook Supplement Acknowledgment– New Hampshire  
By signing below, I acknowledge receipt of this Handbook  Supplement  (“Supplement”) . I understand the practices, 
policies, and procedures described in this Supplement and the Handbook together are designed to provide a summary of 
what I can expect from my employer, Abercrombie & Fitch, abercrombie kids, HOLLISTER, GILLY HICKS, and Social  tourist 
(referred to as the “Company”) and what the Company expects from me. I also understand and acknowledge:  
• It is my responsibility to familiarize myself with and understand all information in this Supplement;  
• I agree to comply with the standards of c onduct in this Supplement;  
• The Company may discipline me, including termination of my employment, if I violate any Company policy;  
• I have a duty to report certain conduct as specified in the policies within this Supplement; 
• This Supplement supersedes all previously issued supplements and  any inconsistent written or verbal policy 
statements made or issued before this Supplement;  
• The Company reserves the right to amend, supplement, or rescind the policies described in this Supplement or to 
modify or deviate from such policies at any time without notice. Delay or failure by the Company to enforce a policy or rule will not constitute a waiver of the Company’s right to do so in the future; 
• Neither this Supplement nor any other Company guidelines, policies, or practices create, or are intended to create a promise or representation of continued employment or an employment agreement. I understand and agree that I am employed at -will. The Company or I may terminate my employment with or without cause and with or 
witho ut notice, at any time;  
• At this time, I have no employment -related claims of unlawful conduct pending with the Company or concerns 
that I have not yet raised with a member of management, Human Resources, or the One Number; and  
• I will contact Human Resourc es with  any questions about this Supplement . 
Signature _________________________________   Date _____________________  
Name ____________________________________ 
 
  
 
 
 
 
 
Associate Handbook 
New Jersey Supplement  
  

Page | 2 
New Jersey Supplement  New Jersey Supplement  
This document supplements the Handbook for  Abercrombie & Fitch Co.  referred to as “the Company.”  Abercrombie & 
Fitch Co. is a leading specialty retailer comprised of our brands including Abercrombie & Fitch, abercrombie kids, 
HOLLISTER,  GILLY HICKS, and Social Tourist. In this Handbook  Supplement , “Abercrombie” and “the Company” refers 
generally to all our brands, and particularly to the brand for which you will be working.  
Throughout this Supplement, you are directed to various team members. Their contact information is in the Company -
wide Handbook for ease of reference. If you have concerns, suggestions, or complaints relating to your employment, 
please utilize the reporting procedures  in the Handbook and this Supplement.  
Inclusive Workplace Policies  
EQUAL EMPLOYMENT OPPORTUNITY  
This Policy supplements the Discrimination, Harassment, and Retaliation Prevention Policy in the Handbook . 
The Company has robust policies in the Handbook  about equal employment opportunities and our efforts to prevent 
discrimination, harassment, and retaliation. Not only is discrimination, harassment, and retaliation against the Company’s 
core values, bu t you also have the right to be free of gender inequity or bias in pay, compensation, benefits, or other terms 
or conditions of employment under the Law Against Discrimination. Our procedure for reporting believed violations of this Policy is in the Discrimination, Harassment, and Retaliation Prevention Policy contained in the Handbook . By signing 
the enclosed Acknowledgement, you acknowledge and agree that you received, read, and understood this Policy.  
Employment Standards  
WHISTLEBLOWER POLICY  
You have the right under the Conscientious Employee Protection Act (“CEPA”) to: (1) complain, disclose, threaten to 
disclose, provide information, and/or testify about an activity, policy, and/or practice that you reasonably believe violates 
a law, rule, or regulation; and (2) without fear of retaliation or reprisal, object to or refuse to participate in an  activity, 
policy, or practice incompatible with a clear mandate of public policy concerning public health, safety, or welfare.  
The Company recognizes its obligations under CEPA . Immediately report perceived violations to the Chief Ethics and 
Compliance Officer or to the One Number . You will not be retaliated against  for raising a complaint pursuant to this Policy.  
The Workday and Compensation  
WAGE AND BENEFIT INFORMATION  
It is critical that you comply with the wage and benefit policies in the Handbook  because, among other reasons, the 
Company is obligated to maintain and report records related to wages, benefits, taxes, other contributions pursuant to 
state wage, benefit, and tax laws. For additional information related to the Company’s obligation to maintain and report these records, please review the state’s model notice, available here:  
https://nj.gov/labor/forms_pdfs/EmployerPosterPacket/MW -400.pdf
. 
Page | 3 
New Jersey Supplement  Time Away From Work  
PAID SICK AND SAFE LEAVE  
For additional information about Paid Sick and Safe Leave (“PSSL”), please view the applicable poster below or contact 
Human Resources:  
English Poster,  
www.nj.gov/labor /forms_pdfs/mw565sickleaveposter.pdf  
Spanish Poster,  
www.nj.gov/labor/forms_pdfs/leavetranslate/MW -565.11%20(10 -18)%20Sick%20Leave%20- %20Spanish.pdf   
FAMILY LEAVE 
Like the Family and Medical Leave Policy , the New Jersey Family Leave Act (“NJFLA”) requires employers to provide family 
leaves of absence to eligible associates . Where both  laws apply to your leave, the leave under both laws will run 
concurrently. Questions concerning NJFLA leave should be directed to Human Resources.  
Eligibility . To be eligible for leave under the NJFLA:  
(1) You must have worked for the Company for at least 12 months;  
(2) You must have worked at least 1,000 “base hours” during the 12 -month period prior to leave; and  
(3) The Company must have 30 or more associates . 
Leave Entitlement . The NJFLA provides up to 12 workweeks of unpaid leave for certain family reasons during a 24 -month 
period. NJFLA leave may be taken to care for your family member who has a serious health cond ition. For purposes of the 
NJFLA, “family member” means a spouse, civil union/domestic partner, child, parent or parent -in-law, sibling, 
grandparent, grandchild, other individual related by blood to you, and an other individual that you show to have the 
equivalent of a family relationship with you. Leave because the birth of a child or placement of a child with you for adoption 
may commence within one year of the date of birth or placement.  
Because NJFLA is a family leave law, leave granted due to your own s erious health condition is not covered under this 
Policy. If you need a leave due to your own serious health condition, please refer to the leave of absence -related policies 
in the Handbook  and the HR Corkboard in PeopleSoft HR ( https://my.anfcorp.com ). 
Reduced Schedules . You may elect to take NJFLA leave on a reduced schedule basis. However, a reduced schedule may 
not last longer than 12 months for any period of leave . 
Intermittent Leave. You may elect to take NJFLA leave to care for a family member with a serious health c ondition on a 
reduced schedule or an intermittent basis if:  
• Medically necessary;  
• The total time within which the leave is taken does not exceed 12 months for each serious condition;  
• You provide the Company with a copy of a certification from your family me mber’s healthcare provider;  
• You provide the Company with prior notice of the leave at least 15 days before the first day of the leave, unless 
an emergency or other unforeseen circumstance precludes prior notice;  
Page | 4 
New Jersey Supplement  • You make a reasonable effort to schedule lea ve so it does not unduly disrupt the Company’s operations; and  
• Intermittent leave taken in connection with a single serious health condition does not exceed 12 months.  
With advance notice and if certain conditions are met, you may take leave for the birth, adoption, or placement of a child 
in foster care on an intermittent basis.  
You must make a reasonable effort to schedule intermittent or reduced schedule leave so that it does not unduly disrupt 
the Company’s business operations.  
Position Alterations. If you are on a reduced schedule or intermittent leave, the Company may require you to temporarily 
transfer to an available alternative position for which you are qualified and that better accommodates a recurring period 
of leave. The alternative positi on will have pay and benefits equivalent to your regular position.  
Group Health Insurance.  NJFLA leave that is not used in conjunction with FMLA may not be eligible for the Company’s 
continuation of group health plan benefits. Contact the Benefits Department  to determine the impact on insurance 
benefits.  
Restoration of Employment and Benefits . As with FMLA leave, at the end of NJFLA leave, subject to some exceptions, you 
generally have the right to return to the same or equivalent position with equivalent pay, benefits, and other terms. 
However, unlike key associates under the FMLA who may be denied reinstatement, if you are a key associate under NJFLA, 
you may be denied NJFLA leave if: (1) you are a salaried associate among the highest paid 5% of associates  for one of the 
seven highest paid associates ; and (2) denial of the leave is necessary to prevent substantial and grievous economic injury 
to the Company’s operations. The Company will notify you if you qualify as a key associate  under the NJFLA and if le ave is 
being denied. If the denial of the NJFLA leave occurs while your leave already has begun, you must return to work within 
two weeks.  
PAY CONTINUATION DURING FAMILY LEAVE  
Qualifying Reasons. Eligible employees may receive Division of Temporary Disability Insurance (TDI) pay continuation 
benefits for the following Qualifying Reasons:  
• To care for a child, spouse, civil union or registered domestic partner, or parent with a serious health condition; 
or  
• To bond with a new child or for pre gnancy -related medical conditions.  
Wage Replacement Benefit. These benefits are financed solely through your contributions to the State of New Jersey, which is responsible for determining if you are eligible for such benefits. To obtain compensation replac ement benefits, 
file a claim with the Division of TDI and visit myleavebenefits.nj.gov.  
Automatic Payroll Deduction. The Company automatically contributes a portion of your paycheck to the Division of TDI. The amount of wages that are deducted may change f rom year to year.  
Overlap With Other Policies . To the extent legally permitted: you must follow the leave of absence procedures outlined 
in the applicable leave policy in the Handbook  or the HR Corkboard in PeopleSoft HR ( https://my.anfcorp.com
); and 
benefits/a leave of absence provided through this Policy will run concurrently with other benefits and/or leaves of absence provided by the Company.  
Additional Information.  The Company will not retaliate against you for exercising your rights under this policy. For 
Page | 5 
New Jersey Supplement  additional information, please visit the website below:  
https://nj.gov/labor/myleavebenefits/  
LEAVE FOR VICTIMS VIOLENCE  
The Company is committed to your health and safety. Should you or your family member be a victim of domestic violence 
or other similarly abusive behavior, promptly contact  the Benefits Department  if you need to take a leave of absence , seek 
other support , or .i f you need additional time off than is provided in this Policy.  
Eligibility.  You are eligible for leave as provided in this Policy if you have worked at least 1,000 hours during the 
immediately preceding 12 -month period, and the Company employs 25 or more associates in New Jersey for each working 
day during 20 or more calendar work weeks in the then -current or immediately preceding calendar year.  
Qualifying Reasons. Leave though this Policy is available if you are a victim of domestic violence or a victim of a sexually 
violent  offense. You may also take leave under this Policy if you r child, parent, spouse, domestic partner, or civil union 
partner is a victim of domestic violence or a sexually violent  offense.  
Length of Leave and Notice Requirements. Leave must be used in the 12 -month period immediately following an instance 
of domest ic violence or a sexually violent  offense. If the reason for leave is foreseeable, you must provide the Company 
with written notice as far in advance as possible. The Company may require you to provide documentation of the basis for the leave.  
Intermittent  Leave and Substitution of Paid Leave. Unpaid leave may be taken intermittently in intervals of one day or 
more.  
Leave Runs Concurrently with PTO . You must use available PTO concurrently during any period of unpaid leave taken 
under this Policy. If you req uest leave for a reason covered by both the NJ SAFE Act, NJFLA, and/or the federal FMLA, the 
leave will run concurrently with your entitlement under each respective law.  
No Retaliation. The Company will not retaliate against you for requesting a leave unde r this Policy. If you believe you were 
retaliated against, promptly contact the One Number . 
Additional Notice. For additional information about benefits through the New Jersey SAFE Act, please review the notice 
below:  
https://www.nj.gov/labor/forms_pdfs/lwdhome/AD -289_9- 13.pdf
 
  
Page | 6 
New Jersey Supplement  Handbook Supplement Acknowledgment– New Jersey 
By signing below, I acknowledge receipt of this Handbook  Supplement  (“Supplement”) . I understand the practices, 
policies, and procedures described in this Supplement and the Handbook together are designed to provide a summary of 
what I can expect from my employer, Abercrombie & Fitch, abercrombie kids, HOLLISTER, GILLY HICKS, and Social tourist (referred to as the “Company”) and what the Company expects from me. I also understand and acknowledge:  
• It is my responsibility to familiarize myself with and understand all information in this Supplement;  
• I agree to comply with the standards of conduct in this Supplement; 
• The Company may discipline me, including termination of my employment, if I violate any Company policy;  
• I have a duty to report certain conduct as specified in the policies within this Supplement;  
• This Supplement supersedes all previously issued supplements and any inconsistent written or verbal policy 
statements made or issued before this Supplement;  
• The Company reserves the right to amend, supplement, or rescind the policies described in this Supplement or to 
modify or deviate from such policies at any time without notice. Delay or failure by the Company to enforce a policy or rule will not constitute  a waiver of the Company’s right to do so in the future;  
• Neither this Supplement nor any other Company guidelines, policies, or practices create, or are intended to create a promise or representation of continued employment or an employment agreement. I un derstand and agree that 
I am employed at -will. The Company or I may terminate my employment with or without cause and with or 
without notice, at any time;  
• At this time, I have no employment -related claims of unlawful conduct pending with the Company or co ncerns 
that I have not yet raised with a member of management, Human Resources, or the One Number; and  
• I will contact Human Resources with any questions about this Supplement . 
Signature _________________________________   Date _____________________  
Name ____________________________________ 
 
  
 
 
 
 
 
Associate Handbook 
New Mexico Supplement  
  

Page | 2 
New Mexico Supplement  New Mexico Supplement  
This document supplements the Handbook for  Abercrombie & Fitch Co.  referred to as “the Company.”  Abercrombie & 
Fitch Co. is a leading specialty retailer comprised of our brands including Abercrombie & Fitch, abercrombie kids, 
HOLLISTER,  GILLY HICKS, and Social Tourist. In this Handbook  Supplement , “Abercrombie” and “the Company” refers 
generally to all our brands, and particularly to the brand for which you will be working.  
Throughout this Supplement, you are directed to various team members. Their contact information is in the Company -
wide Handbook for ease of reference. If you have concerns, suggestions, or complaints relating to your employment, 
please utilize the reporting procedures  in the Handbook and this Supplement.  
Time Away From Work  
PAID SICK AND SAFE LEAVE  
For additional information about Paid Sick and Safe Leave (“PSSL”), please view the applicable poster below or contact 
Human Resources:  
English Poster, 
https://www.dws.state.nm.us/Portals/0/DM/LaborRelations/Paid_Sick_Leave_poster_letter_size.pdf?ver=2022 -03-29-
000528- 147 
Spanish Poster, 
https://www.dws.state.nm.us/Portals/0/DM/LaborRelations/Paid_Si ck_Leave_poster_Spanish_letter_size.pdf?ver=2022
-04-06-163201 -883 
Bernalillo County  
English Poster,  
https://www.bernco.gov/planning/wp -content/uploads/sites/58/2021/03/BC -Employee -Wellness -Act-Poster_FINAL.pdf  
Spanish Poster,  
https://www.bernco.gov/planning/wp -content/uploads/sites/58/2022/09/2022 -BC-Employee -Wellness -Act-
Poster.SpanishFINAL.pdf  
  
Page | 3 
New Mexico Supplement  Handbook Supplement Acknowledgment– New Mexico  
By signing below, I acknowledge receipt of this Handbook  Supplement  (“Supplement”) . I understand the practices, 
policies, and procedures described in this Supplement and the Handbook together are designed to provide a summary of 
what I can expect from my employer, Abercrombie & Fitch, abercrombie kids, HOLLISTER, GILLY HICKS, and Social tourist 
(referred to as the “Company”) and what the Company expects from me. I also understand and acknowledge:  
• It is my responsibility to familiarize myself with and understand all information in this Supplement;  
• I agree to comply with the standards of conduct in this Supplement; 
• The Company may discipline me, including termination of my employment, if I violate any Company policy;  
• I have a duty to report certain conduct as specified in the policies within this Supplement; 
• This Supplement supersedes all previously issued supplements and any inconsistent written or verbal policy 
statements made or issued before this Supplement;  
• The Company reserves th e right to amend, supplement, or rescind the policies described in this Supplement or to 
modify or deviate from such policies at any time without notice. Delay or failure by the Company to enforce a 
policy or rule will not constitute a waiver of the Compan y’s right to do so in the future;  
• Neither this Supplement nor any other Company guidelines, policies, or practices create, or are intended to create a promise or representation of continued employment or an employment agreement. I understand and agree that  
I am employed at -will. The Company or I may terminate my employment with or without cause and with or 
without notice, at any time;  
• At this time, I have no employment -related claims of unlawful conduct pending with the Company or concerns 
that I have not yet raised with a member of management, Human Resources, or the One Number; and  
• I will contact Human Resources with any questions about this Supplement . 
Signature _________________________________   Date _____________________  
Name ____________________________________ 
 
  
 
 
 
 
 
Associate Handbook 
New York Supplement  
  

Page | 2 
New York Supplement  New York Supplement  
This document supplements the Handbook for  Abercrombie & Fitch Co.  referred to as “the Company.”  Abercrombie & 
Fitch Co. is a leading specialty retailer comprised of our brands including Abercrombie & Fitch, abercrombie kids, 
HOLLISTER,  GILLY HICKS, and Social Tourist. In this Handbook  Supplement , “Abercrombie” and “the Company” refers 
generally to all our brands, and particularly to the brand for which you will be working.  
Throughout this Supplement, you are directed to various team members. Their contact information is in the Company -
wide Handbook for ease of reference. If you have concerns, suggestions, or complaints relating to your employment, 
please utilize the reporting procedures  in the Handbook and this Supplement.  
Inclusive Workplace Policies  
EQUAL  EMPLOYMENT OPPORTUNITY  
This Policy  supplements the Equal Employment Opportunity Policy in the Handbook . 
The Company has robust policies concerning equal employment opportunities and our efforts to prevent discrimination, 
harassment, and retaliation. The Company does not tolerate discrimination or harassment in the workplace. In accordance 
with New York Labor Law § 203 -e, this specifically includes, for example, a prohibition against discrimination and 
retaliation based on your (or a depen dent’s) reproductive health decision- making, including but not limited to use of or 
access to a particular drug, device, or medical service related to reproductive health. Likewise, the Company will not request or access personal information regarding the same without first receiving your informed affirmative written consent.  
We encourage you to bring concerns regarding potential discrimination or retaliation based on  reproductive health 
decision -making to the One Number . While we hope that you will raise c oncerns with us directly so we can promptly 
investigate and address the matter, you also have the  right to bring a civil action in court against an employer alleged to 
have violated New York law. In civil action alleging a violation of this provision of New York law, the court may award damages, afford injunctive relief, order reinstatement, and/or award liquidated damages.  
NYC  GENDER NON-DISCRIMINATION  
This Policy supplements the Equal Employment Opportunity Policy in the Handbook . 
As explained in the Handbook and throughout this supplemental document, the Company prohibits discrimination in employment based on a classification protected by law, including gender. For purposes of this Policy, “gender” is an 
individual’s actual or perceived sex, including gender identity, self- image, appearance, behavior, or expression, regardless 
of whether the individual’s gender identity, self- image, appearance, behavior, or expression which is different from 
traditional associations with the legal sex assigned to that individual at birth. We are dedicated to ensuring the fulfillmen t 
of this Policy as it applies to all terms and conditions of employment, including recruitment, hiring , placement, promotion, 
transfer, training, compensation, benefits, accommodation requests, access to programs and facilities, associate  activities, 
and general treatment during employment.  
Page | 3 
New York Supplement  In furtherance of this Policy:  
• The Company gives all associates  the option of indicating preferred gender pronouns. Our systems allow you to 
self- identify your name and gender and do not limit such identifications to male and female only.  
• The Company will not require use of a single -occupancy bathroom because an individu al is transgender or gender 
non-conforming.  
• Our expectations regarding dress code and appearance are gender neutral and do not differentiate or impose 
restrictions or requirements based on gender or sex.  
• We evaluate all accommodations requests (including requests for medical leaves) in a fair and non -discriminatory 
manner.  
• We expect and require all associates  to engage with our customers and other members of the public in a 
respectful, non -discriminatory manner, which includes respecting gender diversity an d ensuring that members of 
the public are not discriminated against  (including discrimination with respect to single -sex programs and 
facilities).  
If you have questions or concerns regarding gender discrimination or believe you were subjected to discrimina tion or 
retaliation , promptly contact the One Number .  
DISCRIMINATION , HARASSMENT , AND RETALIATION PREVENTION  
This Policy supplements the Discrimination, Harassment, and Retaliation Prevention Policy in the Handbook . 
Consistent with the Company’s values, you have a right to be free from discrimination, harassment, and retaliation. In New York and in New York City, it is unlaw ful to engage in such conduct under the New York City Human Rights Law (“NYC  
HRL”). If you have concerns about unfair treatment, please refer to the Discrimination, Harassment, and Retaliation 
Prevention 
Policy in the Handbook , contact the One Number , and complete the complaint form that is enclosed in this 
document.  
While we hope that you will raise concerns with us directly so we can promptly investigate and resolve the matter, you 
may also report potential harassment to the EEOC, the New York State Divis ion of Human Rights, the New York City 
Commission on Human Rights, another enforcement agency (where applicable), or certain courts of law. While a private 
attorney is not required to file a complaint with a governmental agency, you may also seek the legal  advice of an attorney. 
In addition, if harassment involves unwanted physical touching, coerced physical confinement, or coerced sex acts, the conduct may constitute a crime, in which case, promptly contact the local police department. Additional informati on 
regarding reporting avenues is available below.  
New York State Human Rights Law. The NYC HRL applies to all New York employers and protects associates , paid or unpaid 
interns, and non -associates , regardless of immigration status. A complaint alleging an HRL violation may be filed either 
with the Division of Human Rights (“DHR”) or in New York State Supreme Court. Complaints with the DHR may be filed within three years of the harassment. If you did not file at the DHR, you can sue directly in state court under the HRL, within three years of the alleged sexual harassment. You may not file with the DHR if you have already filed an HRL complaint in state court. Complaining internally to the Company do es not extend the time to file with the DHR or in court. 
The time limitations  are counted from the date of the most recent incident of harassment. Having an attorney is not 
required to file a complaint with the DHR, and there is no cost to file with the DH R. 
The DHR will investigate the complaint and determine whether there is probable cause to believe that sexual harassment has occurred. If you are found to be subjected to unlawful harassment after a hearing, you may be entitled to certain 
Page | 4 
New York Supplement  remedies, including monetary damages, civil penalties, and injunctive relief (such as an order that certain action be taken, 
or certain behavior stop). The DHR may be con tacted at: NYS Division of Human Rights, One Fordham Plaza, Fourth Floor, 
Bronx, New York 10458 , 718-741-8400 , or visit: www.dhr.ny.gov . You may also report potential harassment or receive 
legal assistance regarding potential harassment by calling the DHR’s confidential, toll- free hotline  at 1-800-HARASS- 3 (1-
800-427-2773), Monday through Friday from 9:00 a.m. to 5:00 p.m.  
Civil Rights Act of 1964. The Equal Employment Opportunity Commission (“ EEOC ”) enforces federal anti- discrimination 
laws, including Title VII of the 1964 federal Civil Rights Act. You may file an EEOC complaint within 300 days from the alleged harassment. If you are alleging discrimination at work, you can file a “Charge of Discrimination.” The EEOC has 
district, area, and field offices where complaints can be filed. EEOC may be contacted by calling 1 -800-669- 4000 (TTY: 1-
800-669-6820), visiting their website at www.eeoc.gov , or via email at info@eeoc.gov
. There is no cost to file a complaint 
with the EEOC. The EEOC will investigate the complaint and determine whether there is reasonable cause to believe that discrimination has occurred, at which point the EEOC will issue a “Right to Sue” letter permitting you to file a complaint in federal court. The EEOC does not hold hearings or award relief but may take other action in cluding pursuing cases in 
federal court on behalf of complaining parties. Federal courts may award remedies if discrimination is found to have 
occurred. In general, private employers must have at least 15 associates to come within the jurisdiction of the E EOC. If 
you filed an administrative complaint with the DHR, the DHR will cross -file the complaint with the EEOC to preserve the 
right to proceed in federal court.  
Local Protections. Many localities also have and enforce laws protecting individuals from sexual harassment and 
discrimination. If you work in New York City, you may file complaints of sexual harassment with the New York City Commission on Human Rights (“CHR”). Their main office may be contacted at Law Enforcement Bureau of the NYC Commission on H uman Rights, 40 Rector Street, 10th Floor, New York, New York. CHR’s borough offices can be contacted 
at the following phone numbers: Manhattan, 212 -306-7450; Brooklyn, 718- 722-3130; Bronx, 718- 579-6900; Queens, 718 -
657-2465; Staten Island, 718- 390-8506. V isit the CHR online at www1.nyc.gov/site/cchr/index.page for more information 
on how to contact the CHR or file a complaint. A Stop Sexual Harassment Act Fact Sheet is also available below and posted at your worksite and/or on our intranet:  
https://www1.nyc.gov/assets/doc/downloads/EEO/Stop_Sexual_Harassment_Fact_Sheet.pdf
 
COMPLAINT FORM FOR REPORTING SEXUAL HARASSMENT  
If you believe you were subjected to sexual harassment, you are encouraged to complete this form and submit it to Human Resources. You will not be retaliated against for filing a complaint.  
If you are more comfortable reporting verbally or in another manner, you should ask Human Resources to complete this form, and Human Resources will provide you with a copy of the completed form and will investigate the claims as outlined at the end of this form.  
For additional resources, visit  ny.gov/programs/combating -sexual -harassment -workplace or in New York City 
www1.nyc.gov/site/cchr/index.page
  
Page | 5 
New York Supplement  COMPLAINANT INFORMATION 
Name: ___________________________Email: ___________________  
Phone: ___________________  
Work Location:  _____________________    Job Title: _______________________________  
Select Preferred Communication Method:  Email   Phone   In person  
SUPERVISOR INFORMATION  
Immediate Supervisor’s Name: _________________________  
Work Location: _____________________   Job Title: _______________________________  
Work Phone: _____________________ __   Work Address: __________________________  
  
Page | 6 
New York Supplement  COMPLAINT INFORMATION  
1. Your complaint of Sexual Harassment is made about:  
Name: _____________________________Job Title: ____________________________  
Work Phone: _____________________  Work Address: __________________________  
Relationship to you: Supervisor   Subordinate   Co-Worker   Other  
2. Please describe what happened and how it is affecting you and your work. Please use additional sheets of paper if 
necessary and attach any relevant documents or evidence.  
3. Date(s) sexual harassment occurred: __________________________________________________  
Is the sexual harassment continuing? Yes No 
4. Please list the name and contact information of any witnesses or individuals who may have information related to your complaint:  
5. This question is optional but may help the investigation. Have you previously complained or provided 
inform ation (verbal or written) about related incidents?  If yes, when and to whom did you complain or 
provide information?  
If you have retained legal counsel and would like us to work with them, please provide their contact information.  
By signing below, you affirm that the information is true and accurate to the best of your knowledge.  
Signature: __________________________   Date: __________________  
 
Page | 7 
New York Supplement  The Workday and Compensation  
PREDICTIVE SCHEDULING FOR EMPLOYEES IN NEW YORK CITY 
You Have a Right to a Predictable Work Schedule Notice  
1. Available in English at: https://www.nyc.gov/assets/dca/downloads/pdf/workers/Retail-FairWorkweek -Notice -
English.pdf  
2. Available in other languages at: https://www.nyc.gov/site/dca/businesses/fair -workweek -retail- employers.page  
WORKPLACE POSTERS  
Posters providing you with additional information about the workplace and employment laws are available at your 
worksite and the posters are electronically available at the below links.  
New York State P osters  
• Minimum Wage : https://dol.ny.gov/system/files/documents/2023/01/ls207.pdf  
• Equal Pay : https://dol.ny.gov/system/files/documents/2021/03/ls603_equity_provision.pdf   
• Blood Donation Leave  
o English at: https://dol.ny.gov/system/files/documents/2021/03/ls703.pdf   
o Spanish at: https://dol.ny.gov /system/files/documents/2021/03/ls703s.pdf   
• Time Off to Vote Notice: https://www.elections.ny.gov/NYSBOE/elections/TimeOffToVoteNotice.pdf   
• New York State Division of Human Rights : https://dhr.ny.gov/system/files/documents/2022/05/poster.pdf  
• New York Correction Law Article 23 -A: https://dol.ny.gov/system/files/documents/2021/02/correctio n-law-
article -23a.pdf   
• Notice of Employee Rights, Protections, and Obligations Under Labor Law Section 740 : 
https://dol.ny.gov/system/files/documents/2022/02/ls740_1.pdf  
• Veterans Benefits and Services : https://dol.ny.gov/system/files/documents/2023/03/p37- vets-benefits -and-
services -3-8- 23.pdf   
• Unemployment Insurance Notice to Employees :  
https://dol.ny.gov/system/files/documents/2023/05/ia133_0.pdf   
• Rights of Nursing Mothers to Express Breast Milk in the Work Place : 
https://dol.ny.gov/system/files/documents/2023/03/ls702.pdf   
• Schedule of Hours of Work for Minors under 18 Years of Age : 
https://dol.ny.gov/system/files/documents/2023/06/p879.pdf   
o Summary of permitted work hours for minors available at: https://dol.ny.gov/system/files/documents/2023/04/ls171.pdf
  
• Sexual Harassment Prevention Notice  
o English : 
https://www.ny.gov/sites/default/files/atoms/files/sexualharassmentpreventionposter_English_handfill.pdf   
Page | 8 
New York Supplement  o Available in other languages at: https://www.ny.gov/combating- sexual -harassment -workplace/combat -
harassment -translations  
New York City Posters  
• Notice of Employee Rights: Safe and Sick Leave  
o English: https://www.nyc.gov/assets/dca/downloads/pdf/about/PaidSafeSickLeave -MandatoryNotice -
English.pdf   
o Spanish: https://www.nyc.gov/assets/dca/downloads/pdf/about/PaidSafeSickLeave -MandatoryNotice -
Spanish.pdf  
o Available in o ther languages at: https://www.nyc.gov/site/dca/about/Paid -Safe -Sick-Leave -Notice -of-
Employee -Rights.page  
• You Have a Rig ht to Temporary Changes to Your Work Schedule Notice : 
https://www.nyc.gov/assets/dca/downloads/pdf/workers/TemporaryScheduleChange -Notice -English.pdf  
• Pregnancy Accommodations at Work Notice  
o English: https://www.nyc.gov/assets/cchr/downloads/pdf/publications/Pregnancy _Poster_2017.pdf   
o Spanish: https://www.nyc.gov/assets/cchr/downloads/pdf/materials/Pregnancy_Notice -Sp.pdf  
Westchester County Posters  
• Safe Time Leave Law Poster  
o English: https://humanrights.westchestergov.com/images/stories/pdfs/2019safeposter.pdf  
o Spanish: https://humanrights.westchestergov.com/images/stories/pdfs/2019stpostersoct.pdf  
TEMPORARY SCHEDULE CHANGE  
This Policy supplements the Work Hours and Schedules Policy in the Handbook  and applies to associates  in New York 
City.  
Eligibility.  Eligible associates  must have worked for the Company for at least 120 calendar days and must work 80 hours 
or more per calendar year in New York City.  
Schedule Changes. If eligible, you m ay request a temporary adjustment to the hours, times, or locations of your usual 
work schedule for the covered reasons described below.  
Covered Reasons.  If eligible, you may request a temporary schedule change to address the following “personal events”: 
• Care for a minor child for whom you provide direct and ongoing care;  
• Care for an individual (“care recipient”) with a disability for whom you provide dire ct and ongoing care to meet 
the needs of daily living and who is a family member or who resides in your household;  
• Attendance at a legal proceeding or hearing for public benefits for yourself, your family member, or your minor 
child or care recipient;  
Page | 9 
New York Supplement  • Time  off for a reason covered under NYC’s Paid Safe and Sick Leave Law, including care and treatment for yourself 
or a family member or assistance or other safety measures if you or a family member are experiencing an  act or 
threat of domestic violence or unwanted sexual contact, stalking, or human trafficking; or  
• Any other reason under applicable law.  
If you, in the process of a temporary schedule change, falsely represent that you have a “personal event” but in truth do 
not, you will be disciplined . 
Duration.  Eligible associates may request one to two temporary schedule changes per year, depending on the duration:  
• Two temporary schedule changes, which are up to one workday in duration; or  
• One temporary schedule change, which is two workdays in duration.  
Requesting a Temporary Schedule Change . As soon as you become aware of the need for a temporary schedule change, 
you should notify a manager by providing the following information in writing:  
• Date of the temporary schedule change;  
• Acknowledgment that the change is due to one or more of the personal events listed above; and  
• The proposed temporary schedule change (for example, using unpaid time off, a schedule swap, or a change in work hours).  
The Company will respond to the request as soon as pract icable. Requests may be denied if you have exhausted your 
requests for the calendar year or if a request is made for a reason that is not a qualifying personal event.  
Schedule Changes are Unpaid. Temporary schedule changes that involve time off will be unpaid unless: (1) pay is required by law; or (2) you have available paid sick leave or PTO that you wish to use for the absence.  
No Retaliation . The Company will not retaliate against you  for requesting a schedule change under this Policy. If you 
believe you  were retaliated against, promptly contact the One Number . 
MEAL BREAKS  
This Policy replaces the Meal and Rest Break Policy in the Handbook.  
Meal Breaks . You are provided and may take uninterrupted  and work -free meal break s as described in the chart below.  If 
you are a non -exempt associate , the break(s) are unpaid.  
Length of Workday:  Number of Meal Breaks:  
Less than 6 hours  None  
More than 6 hours and your shift extends between 11:00 
a.m. and 2:00 p.m.  One 30 -minute meal break between 11:00 a.m. and 
2:00 p.m.  
More than 6 hours and you start your shift before 11:00 
a.m. and continue after 7:00 p.m.  If you are an exempt associate : two paid 20 -minute 
meal breaks between 5:00 p.m. and 7:00 p.m.  
If you are a non -exempt associate : two 30-minute 
unpaid meal breaks  between 5:00 p.m. and 7:00 p.m.  
Page | 10 
New York Supplement  More than 6 hours and you start your shift between 1:00 
p.m. and 6:00 a.m.  One 45-minute meal break in the beginning of the 
shift  
Logistics of Meal Breaks . Within the required window, the Company may schedule breaks to best accommodate operating 
requirements. If, however, your breaks are not scheduled in advance, please use your best judgment to decide when – 
within the required window – it is best to take your breaks, based on your workload and operational demands. Please 
then attempt to contact your manager before you start your breaks to help the Company ensure proper staffing.  If you 
cannot connect with your manager, please still proceed with your breaks. Meal breaks should occur away from your work 
area to the extent possible.  
Recording Meal Breaks . You must follow the timekeeping procedures set forth in the Timekeeping Policy  in the Handbook . 
No Off -the-Clock Work . During these breaks, you are relieved of all work duties and may not perform work. Working off 
the clock is strictly prohibited  if you are a non -exempt associate . This also means that during breaks, you are not expe cted 
to be available to take assignments or respond to work messages such as text messages, telephone calls, or emails.  
Duty to Report . No one (manager or non -manager) is permitted to prevent or discourage you from taking a break as 
described above. If you  believe you were prevented, interrupted, or discouraged from taking all or part of a break as 
provided in this Policy, or if you experience other circumstances inconsistent with this Policy, you have a duty to report the circumstances to the One Number  immediately. You must provide: (1) your name and work location; (2) the date(s) 
and time(s) at issue; and (3) a brief description of the conduct or circumstance(s).  
The Company will promptly investigate all such reports and will take corrective action when necessary to ensure that you are provided breaks in compliance with this Policy.  You will not be retaliated against for making a good -faith report under 
this Policy.  
BREAKS FOR NURSING /PUMPING MOTHERS  
This replaces the Breaks for Nursing/Pumping Mothers Policy in the Handbook . 
The Company supports associates who choose to breastfeed and will provide you with a private space. You should attempt to 
schedule lactation breaks around your work and break schedule; such breaks may be scheduled as frequentl y as necessary 
and may last as long as necessary. The Company recognizes that your break schedule may need to vary over time, and we will do our best to accommodate such needs. If you are a non -exempt associate , breaks of more than 30 minutes that do not r un 
concurrently with paid rest breaks provided by the Company are unpaid, and you must clock out for the break(s).  
Please contact your District Manager or all the One Number to arrange a private lactation room and a break schedule. You 
will receive a respo nse within five business days. If more than one associate needs to use the space to express breast milk, 
we will discuss schedules or other alternative options with all affected associates who use the shared space to determine 
what arrangements can address everyone’s needs. If you need to use the room and find it unavailable, please notify your District M anager or contact the One Number, so we can rectify the situation.  
Our practices and this Policy comply with New York City labor laws, which require employers to provide a reasonable break time for 
associates to express breast milk. The Company prohibits discrimination, harassment, and retaliation for exercising 
the right to express breast m ilk in the workplace . Promptly report discrimination, harassment, retaliation, or other alleged 
violations of this Policy  to the One Number . 
For additional information, please visit the website below:  
Page | 11 
New York Supplement  https://dol.ny.gov/system/files/documents/2021/03/fact -sheet -your -right -as-a-nursing -mother -to-pump -breast -milk-at-
work -p708.pdf  
PRE-TAX INCOME INFORMATION  
This Policy applies to associates  in NYC.  
By signing the enclosed Acknowledgement, you acknowledge and agree that you  received a copy of the City’s model notice 
related to use of pre -tax income for fringe benefits. This notice is also available here:  
https://www 1.nyc.gov/assets/dca/downloads/pdf/about/CommuterBenefits -EmployerComplianceForm.pdf .  
Time Away From Work  and Benefits  
PAID SICK AND SAFE LEAVE  FOR ASSOCIATES  IN NEW YORK 
For additional information about Paid Sick and Safe Leave (“PSSL”), please view the applicable poster below or contact 
Human Resources:  
New York City :  
English Poster,  
https://www1.nyc.gov/assets/dca/downloads/pdf/about/PaidSafeSickLeave -MandatoryNotice -English.pdf  
Spanish Post er,  
https://www1.nyc.gov/assets/dca/downloads/pdf/about/PaidSafeSickLeave -MandatoryNotice -Spanish.pdf  
Westchester County:  
English Poster,  
https://humanrights.westchestergov.com/images/stories/pdfs/2019safeposter.pdf  
Spanish Poster,  
https://humanrights.westchestergov.com/images/stories/pdfs/2019stpostersoct.pdf  
By signing the enclosed acknowledgement, you ackno wledge and agree that you were provided this notice regarding PSSL.  
FAMILY LEAVE  AND PAY CONTINUATION DURING FAMILY LEAVE 
Eligibility.  If you are a full- time associate , you become eligible for up to 12 weeks of paid family leave (“PFL”) /pay 
continuation  after 26 consecutive weeks of work. If you are a part -time associate , you become eligible for PFL /pay 
continuation  on your 175th day of work.  
Qualifying Reasons. Eligible associates  may receive  PFL/pay continuation benefits  for the following Qualifying Reasons:  
• To provide care, including physical or psychological care, to a family member* due to the family member’s serious health condition;  
• To bond with your newborn children during the first year of the child’s life, or in t he case of adoption or foster 
care placement, for the first year after the placement of a child with you; and  
Page | 12 
New York Supplement  • For a qualifying reason as provided for under the federal Family and Medical Leave Act arising from your spouse, 
domestic partner, child, or parent being on active military duty, or alternatively, being notified of an impending 
call or order to active military duty.  
*For purposes of this Policy, family member is defined as your child(ren) or sibling(s) (whether biological, step, “half,” 
adopted, fos ter, in loco parentis, or adult), spouse or domestic partner, other relatives ( e.g., grandparents or 
grandchildren), and those who are related by blood or affinity whose close association is the equivalent of a family relationship.  
Wage Replacement  Benefit . You may receive PFL at 67% of your average weekly wage or 67% of the state average weekly 
wage, whichever is less. You must file a claim with the New York Department of Family Leave to obtain pay continuation 
benefits.  
Automatic Payroll Deduction. The Company automatically contributes a portion of your paycheck to the Department of 
Family Leave (“DFML”). Your contribution amount is set each year.  
Benefits Continuation. The Company  will maintain your group health insurance coverage while you are receivin g PFL 
benefits , applying the same terms and conditions as if you continued to work. This means that if you are responsible for a 
portion of the premiums for such coverage while working, you will continue to be responsible for the same portion of those prem iums and for other Company benefit plan coverage while receiving DFML benefits . 
Returning to Work. When you return from PFL, you will be returned to the same or equivalent position you held when the leave began.  
Overlap With Other Policies . To the extent l egally permitted: you must follow the leave of absence procedures outlined 
in the applicable leave policy in the Handbook; and benefits/a leave of absence provided through this Policy will run concurrently with other benefits and/or leaves of absence provided by the Company.  
Additional Information.  The Company will not retaliate against you for exercising your right to apply for and receive PFL 
benefits. For additional information, please visit the website below:  
https://paidfamilyleave.ny.gov/2023#:~:text=New%20York%20State%20Paid%20Family%20Leave%20provides%20elig ibl
e,member%20is%20deployed%20abroad%20on%20active%20military%20service.  
BLOOD DONATION LEAVE  
We encourage all associates who are able and interested in doing so to donate blood. Whenever possible, we ask that you 
do this before or after work or on days that you are not scheduled to work. However, if you work at least 20 hours per 
week, you may take up to three hours of unpaid leave in a calendar year to donate blood. Before doing so, you must submit a written request for time off to your manager. You must submit the time off request at least three workdays ahead of the requested absence.  
The Company will not retaliate against you  for requesting or taking time off under this Policy. If you believe  you were  
retaliated ag ainst, promptly contact the One Number . 
LEAVE FOR VICTIMS OF VIOLENCE  (WESTCHESTER COUNTY ) 
This Policy applies to associates in Westchester County.  
Page | 13 
New York Supplement  The Company is committed to your health and safety. Should you or your family member be a victim of domestic violence 
or other similarly abusive behavior, promptly contact the Benefits Department  if you need to take a leave of absence, seek  
other support , or if you need more time off than is provided in this Policy.  
Eligible Associates . If you work in Westchester County and have worked for the Company for at least 90 days, you may 
take up to 40 hours of paid leave under this Policy.  
Qualifying Reasons for Leave. Eligible associates may take leave to:  
• Attend or testify in a court proceeding relating to t he domestic violence or human trafficking; and/or  
• Relocate/move to a safe location.  
Notice and Documentation Requirements. If you need to take time off under this Policy, you must notify your manager 
and the Benefits Department  as soon as possible. Whenever possible, you should also include the expected duration of 
the absence. If the need for leave is foreseeable, we ask that you make a reasonable effort to take time off in a manner that does not unduly disrupt our operations, if possible. You are not requ ired to look for or secure a replacement to cover 
work hours. The Company may require you to provide reasonable documentation supporting the reason for the leave. Documentation may include, for example, a court appearance ticket or subpoena, a police report, an affidavit/letter from an attorney involved in the court proceeding, or an affidavit/letter from a social worker or other organization providing you with related assistance.  
No Retaliation. The Company will not retaliate against you  for requesting a l eave under this Policy. If you believe you were 
retaliated against, promptly contact the One Number . 
Additional Notice. For additional information about related benefits to associates in Westchester County, please click on 
the link below:  
https://library.municode.com/ny/westchester_county/ordinances/code_of_ordinances?nodeId=957558
 
NYC  COMMUTER BENEFITS  
Starting four weeks after full- time employment, full -time associates who work an average of at least 30 hours per week 
are eligible to use up to $270/month of pre -tax income to pay for qualified transportation benefits. Qualified 
transportation includes NY C regional mass transit services, eligible ferry and water taxi services, eligible vanpool services, 
eligible commuter bus services, Access -A-Ride and other area paratransit providers. Participation in this commuter benefit 
is voluntary, and if you elect t o join, you may subsequently cancel your participation. If you wish to enroll in the commuter 
benefits program, please contact the Benefits Department  and complete the commuter benefits participation form, which 
is available here:  
https://www1.nyc.gov/assets/dca/downloads/pdf/about/CommuterBenefits -EmployerComplianceForm.pdf   
Page | 14 
New York Supplement  Handbook Supplement Acknowledgment–New York  
By signing below, I acknowledge receipt of this Handbook  Supplement  (“Supplement”) . I understand the practices, 
policies, and procedures described in this Supplement and the Handbook together are designed to provide a summary of 
what I can expect from my employer, Abercrombie & Fitch, abercrombie kids, HOLLISTER, GILLY HICKS, and Social tourist (referred to as the “Company”) and what the Company expects from me. I also understand and acknowledge:  
• It is my responsibility to familiarize myself with and understand all information in this Supplement;  
• I agree to comply with the standards of conduct in this Supplement; 
• The Company may discipline me, including termination of my employment, if I violate any Company policy;  
• I have a duty to report certain conduct as specified in the policies within this Supplement; 
• This Supplement supersedes all previously issued supplements and any inconsistent written or verbal policy 
statements made or issued before this Supplement;  
• The Company reserves the right to amend, supplement, or rescind the policies described in this Supplement or to 
modify or deviate from such policies at any time without notice. Delay or failure by the Company to enforce a policy or ru le will not constitute a waiver of the Company’s right to do so in the future;  
• By accepting and continuing employment with the Company, and signing below, I consent to the Company’s surveillance of my electronic activities;  
• Neither this Supplement nor any  other Company guidelines, policies, or practices create, or are intended to create 
a promise or representation of continued employment or an employment agreement. I understand and agree that I am employed at -will. The Company or I may terminate my employm ent with or without cause and with or 
without notice, at any time;  
• At this time, I have no employment -related claims of unlawful conduct pending with the Company or concerns 
that I have not yet raised with a member of management, Human Resources, or the O ne Number; and  
• I will contact Human Resources with any questions about this Supplement . 
Signature _________________________________   Date _____________________  
Name ____________________________________ 
 
  
 
 
 
 
 
Associate Handbook 
North Dakota Supplement  
  

Page | 2 
North Dakota Supplement  North Dakota Supplement  
This document supplements the Handbook for  Abercrombie & Fitch Co.  referred to as “the Company.”  Abercrombie & 
Fitch Co. is a leading specialty retailer comprised of our brands including Abercrombie & Fitch, abercrombie kids, 
HOLLISTER,  GILLY HICKS, and Social Tourist. In this Handbook  Supplement , “Abercrombie” and “the Company” refers 
generally to all our brands, and particularly to the brand for which you will be working.  
Throughout this Supplement, you are directed to various team members. Their contact information is in the Company -
wide Handbook for ease of reference. If you have concerns, suggestions, or complaints relating to your employment, 
please utilize the reporting procedures  in the Handbook and this Supplement.  
The Workday and Compensation  
MEAL BREAKS  
This Policy replaces the Meal and Rest Break Policy in the Handbook.  
Meal Breaks . If you work at least five consecutive hours, you are provided and may take an uninterrupted  and work -free 
30-minute meal break . This break is unpaid if you are a non -exempt associate . 
Meal Break Waiver . With written approval from Human Resources, you may voluntarily waive meal breaks. If you wish to 
waive a meal break, you must contact Human Resources to obtain and complete a waiver form.  
Logistics of Meal and Rest Breaks . Within the required window, the Company may schedule breaks to best accommodate 
operating requirements. If, however, your meal break is not scheduled in advance, please use your best judgment to decide when – within the required window – it is best to take your break, based on your workl oad and operational 
demands. Please then attempt to contact your manager before you start your break to help the Company ensure proper staffing. If you cannot connect with your manager, please still proceed with break. Meal breaks should occur away from your work area to the extent possible.  
Recording Meal Breaks . You must follow the timekeeping procedures set forth in the Timekeeping Policy in the Handbook . 
No Off -the-Clock Work . During these breaks, you are relieved of all work duties and may not perform work. Working off 
the clock is strictly prohibited  if you are a non -exempt associate . This also means that during breaks, you are not expected 
to be available to take assignments or respond to work messages such as text messages, telephone calls, or emails . 
Duty to Report . No one (manager or non -manager) is permitted to prevent or discourage you from taking a break as 
described above. If you believe you were prevented, interrupted, or discouraged from taking all or part of a break as 
provided in this Policy, or if you experience other circumstances inconsistent with this Policy, you have a duty to report the circumstances to the One Number  immediately. You must provide: (1) your name and work location; (2) the date(s) 
and time(s) at issue; and (3) a brief description of the conduct or circumstance(s).  
The Company will promptly investigate all such reports and will take corrective action when necessary to ensure that you are provided breaks in compliance with this Policy.  You will not be retaliated against for making a good -faith report under 
this Policy . 
 
Page | 3 
North Dakota Supplement  Handbook Supplement Acknowledgment– North Dakota  
By signing below, I acknowledge receipt of this Handbook  Supplement  (“Supplement”) . I understand the practices, 
policies, and procedures described in this Supplement and the Handbook together are designed to provide a summary of 
what I can expect from my employer, Abercrombie & Fitch, abercrombie kids, HOLLISTER, GILLY HICKS, and Social tourist (referred to as the “Company”) and what the Company expects from me. I also understand and acknowledge:  
• It is my responsibility to familiarize myself with and understand all information in this Supplement;  
• I agree to comply with the  standards of conduct in this Supplement;  
• The Company may discipline me, including termination of my employment, if I violate any Company policy;  
• I have a duty to report certain conduct as specified in the policies within this Supplement; 
• This Supplement supersedes all previously issued supplements and any inconsistent written or verbal policy 
statements made or issued before this Supplement;  
• The Company reserves the right to amend, supplement, or rescind the policies described in this Supplement or to 
modi fy or deviate from such policies at any time without notice. Delay or failure by the Company to enforce a 
policy or rule will not constitute a waiver of the Company’s right to do so in the future; 
• Neither this Supplement nor any other Company guidelines, p olicies, or practices create, or are intended to create 
a promise or representation of continued employment or an employment agreement. I understand and agree that I am employed at -will. The Company or I may terminate my employment with or without cause an d with or 
without notice, at any time;  
• At this time, I have no employment -related claims of unlawful conduct pending with the Company or concerns 
that I have not yet raised with a member of management, Human Resources, or the One Number; and  
• I will contact Human Resources with any questions about this Supplement . 
Signature _________________________________   Date _____________________  
Name ____________________________________ 
 
  
 
 
 
 
 
Associate Handbook 
Oregon Supplement  
  

Page | 2 
Oregon Supplement  Oregon Supplement  
This document supplements the Handbook for  Abercrombie & Fitch Co.  referred to as “the Company.”  Abercrombie & 
Fitch Co. is a leading specialty retailer comprised of our brands including Abercrombie & Fitch, abercrombie kids, 
HOLLISTER,  GILLY HICKS, and Social Tourist. In this Handbook  Supplement , “Abercrombie” and “the Company” refers 
generally to all our brands, and particularly to the brand for which you will be working.  
Throughout this Supplement, you are directed to various team members. Their contact information is in the Company -
wide Handbook for ease of reference. If you have concerns, suggestions, or complaints relating to your employment, 
please utilize the reporting procedures  in the Handbook and this Supplement.  
Inclusive Workplace Policies  
ACCOMMODATIONS AND DISCRIMINATION , HARASSMENT , AND RETALIATION PREVENT ION 
This Policy supplements the Reasonable Accommodations  for Disabilities and the Discrimination, Harassment, and 
Retaliation Prevention Policies in the Handbook . 
The Company is committed to a work environment that respects and includes all associates . The Company is also 
committed to providing reasonable accommodations for known limitations related to pregnancy and enforcing your right 
to be free from discrimination and unfair employment practices, including such conduct because of pregnancy, childbir th, 
or related conditions. If you have concerns about unfair treatment, please refer to the Discrimination, Harassment, and Retaliation Prevention Policy in the Handbook  and contact the One Number . If you need a reasonable accommodation, 
please refer to th e Reasonable Accommodations for Disabilities Policy and notify your manager, who will escalate the 
request to Human Resources .  
While we hope that you will raise concerns with us directly so we can promptly investigate and resolve the matter, you 
may also report potential sexual harassment externally; the statute of limitations period applicable to bring a cause of 
action alleging unlawful discrimination or sexual assault is five years.  
Please also note that the Company will not require you to enter into a non -disclosure or non -disparagement agreement 
that has the purpose or effect of preventing you from disclosing or discussing conduct that relates to alleged discrimination  
or harassment based on a Protected Category between you and another 
associate . Howev er, if you claim to be aggrieved 
by unlawful discrimination or sexual assault, you may voluntarily request to enter a settlement, separation, or severance agreement with the Company that includes non -disclosure, non -disparagement, and/or no -rehire provisio ns. If such an 
agreement is provided, the Company will provide you at least seven days to revoke the agreement.  
The Workday and Compensation  
MEAL AND REST BREAKS  
This Policy supplements the Meal and Rest Break Policy in the Handbook.  
This Policy applies  to non- exempt associate s only . 
Meal Breaks . If you are a non -exempt associate  and work six or more continuous hours, you are provided and may take 
an uninterrupted, work -free, and unpaid 30 -minute meal break or a paid 20 -minute meal break . You are provided and 
Page | 3 
Oregon Supplement  may take additional unpaid meal breaks if you work 14 or more hours in a day . If your work period is at least six hours but 
less than seven hours, the meal break should occur after your second hour of work and before the start of your fifth ho ur 
of work . If your work period is more than seven hours, the meal break should occur after your third hour of work and 
before the start of your sixth hour of work.  
Rest Breaks . If you are a non -exempt associate , you are provided and may take uninterrupted, work -free, and paid rest 
breaks as described in the chart below . Rest breaks should occur as close to the middle of each work period as is 
practicable.  
Length of Workday:  Number of Rest Breaks:  
Less than two hours  None  
More than two hours, up to six hours  One ten -minute rest break  
More than six hours, up to ten hours  Two ten -minute rest breaks  
More than ten hours, up to 14 hours  Three ten -minute rest breaks  
14 hours or more  Three ten -minute rest breaks  
Logistics of Meal and Rest Breaks . Within the required window, the Company may schedule breaks to best accommodate 
operating requirements. If, however, your breaks are not scheduled in advance, please use your best judgment to decide 
when – within the required window – it is be st to take your breaks, based on your workload and operational demands. 
Please then attempt to contact your manager before you start your breaks to help the Company ensure proper staffing. If 
you cannot connect with your manager, please still proceed with your breaks. Meal and/or rest breaks should occur away 
from your work area to the extent possible.  
Recording Meal and Rest Breaks . You must follow the timekeeping procedures set forth in the Timekeeping Policy in the 
Handbook . 
No Off -the-Clock Work . During these breaks, you are relieved of all work duties and may not perform work. Working off 
the clock is strictly prohibited. This also means that during breaks, you are not expected to be available to take assignment s 
or respond to work messages such a s text messages, telephone calls, or emails.  
Duty to Report . No one (manager or non -manager) is permitted to prevent or discourage you from taking a break as 
described above. If you believe you were prevented, interrupted, or discouraged from taking all or part of a break as 
provided in this Policy, or if you experience any other circumstances inconsistent with this Policy, you have a duty to report the circumstances to the One Number  immediately. You must provide: (1) your name and work location; (2) the date(s) 
and time(s) at issue; and (3) a brief description of the conduct or circumstance(s).  
The Company will promptly investigate all such reports and will take corrective action when necessary to ensure that you 
are provided breaks in compliance with this  Policy.  You will not be retaliated against for making a good -faith report under 
this Policy.  
Time Away From Work and Benefits  
PAID SICK AND SAFE LEAVE  
For additional information about Paid Sick and Safe Leave (“PSSL”), please view the applicable poster below or contact Human Resources:  
Page | 4 
Oregon Supplement  English Poster,  
https://www.oregon.gov/boli/employers/Documents/BOLI_SickLeave.pdf . 
Spanish Poster,  
http://www.oregon.gov/boli/employers/Documents/BO LI_SickLeave_Spanish.pdf  
PAID FAMILY LEAVE  
We are committed to providing time off to associates  for family and medical reasons. Please refer to the Handbook and  
the HR Corkboard in PeopleSoft HR ( https://my.anfcorp.com ) for more information about the Company’s leave -related 
benefits. Effective September 2023, the Company also provides leave to eligible associates  consistent with Oregon’s  paid 
family  and medical  leave  insurance program, known  as Paid Leave Oregon (“PLO”). PLO is funded through payroll 
contributions made to the PLO program. The contribution rate is set annually by Oregon’s Employment Department and 
will be determined once program costs are estimated. You will contribute 60%, and the Company will contribute 4 0% of 
the required contribution. Your portion is withheld from your pay, like income tax withholding.  
Eligibility. You are eligible for PLO leave if:  
• You work for the Company in Oregon;  
• You earned at least $1,000 the year before you apply for benefits; and  
• You have a Qualifying Reason that is listed below.  
Qualifying Reasons.  You may take PLO leave for the Qualifying Reasons below:  
• The birth of a child;  
• Bonding with a child in the first year:  
o After birth;  
o Through adoption; or  
o When they’re placed in your hom e through foster care;  
• A family member has a serious health condition;  
• You have a serious health condition; or  
• You or your child  are a survivor of sexual assault, domestic violence, harassment, or stalking.  
For purposes of PLO leave, “family member” includes:  
• Your spouse or domestic partner;  
• Your child (biological, adopted, stepchild, or foster child), your spouse or domestic partner’s child, or the child’s spouse or domestic partner;  
• Your parent (biological, adoptive, stepparent, foster parent, or le gal guardian), the parent of your spouse or 
domestic partner, or your parent’s spouse or domestic partner;  
• Your sibling or stepsibling or their spouse or domestic partner;  
• Your grandparent or your grandparent’s spouse or domestic partner;  
• Your grandchild o r your grandchild’s spouse or domestic partner;  
Page | 5 
Oregon Supplement  • Anyone you are related to by blood; or  
• Anyone who is connected to you and has a family relationship.  
Length of Leave.  You may take up to 12 weeks of PLO leave per year, on a weekly or daily basis, depending o n what your 
serious health condition needs, subject to the following exceptions:  
• Women who take PLO leave because they are pregnant, have given birth, or have health needs because of 
childbirth may take up to an additional 2 weeks of leave for a PLO -qualifying purpose (up to 14 total weeks)  
• If you and one of your family members both work for the Company, you both may take up to 12 weeks of parental leave. You may be required to stagger the leave.  
• In the unfortunate case of the death of a family member, you may take a maximum of two weeks of PLO leave 
per death and up to a maximum of 12 weeks each year.  
Scheduling and Leave Documentation. You must give notice to your manager and the Benefits Department  at least 30 
days in advance of the need for PLO if the need is foreseeable based on an expected birth, placement for adoption or foster care, or planned medical treatment for a qualifying serious health condition. If the need for PLO is not foreseeable, please notify your manager and the Benefits Department  as soon as possible under the circumstances. You must complete 
the state’s documentation and work with the Benefits Department to ensure that your completed PLO request package is 
submitted properly. He alth information related to PLO, medical leave, or safe leave provided by the Company is 
confidential and will not be released by the Company without your permission, unless state/federal law, or a court order permits or requires such disclosure.  
Use of Le ave. Leave under this Policy runs concurrently with leave provided under the Family and Medical Leave Policy.  
Paid Leave Benefits.  You may receive a weekly PLO benefit payment. The amount of the benefit payment will depend on 
your average weekly wage rate and can be up to 100% of your wages. Please review the FAQ linked at the bottom of this 
policy for additional information regarding filing a claim for PLO benefits. You have a right to appeal a denial decision wit h 
the Oregon Employment Department.  
Benefi ts Continuation. The Company will maintain your group health insurance coverage while you are on PLO, applying 
the same terms and conditions as if you continued to work. This means that if you are responsible for a portion of the premiums for such coverage  while working, you will continue to be responsible for the same portion of those premiums 
and for other Company benefit plan coverage during the PLO.  
Returning to Work . When you return from PLO, you typically will be returned to the same or equivalent pos ition you held 
when the leave began.  
No Retaliation . If you have worked for the Company for 90 consecutive days prior to claiming benefits under PLO, your 
leave is protected. Retaliation is prohibited, and the Company will not retaliate against you for req uesting leave under this 
Policy, providing notification of leave, taking leave under the program, or for claiming family and medical leave insurance benefits. If you believe you were retaliated against, promptly notify Human Resources. You may also bring a  civil action or 
file a complaint for a violation of the law.  
Additional Information. For additional information regarding PLO, please view the state’s FAQ available here:  
https://d1o0i0v5q5lp8h.cloudfront.net/paidleave/live/assets/resources/Paid -Leave -ModelNotice -Poster -EN.pdf
  
Page | 6 
Oregon Supplement  PAY CONTINUATION DURING FAMILY LEAVE  
Eligibility.  You are eligible for Paid Family and Medical Leave (PFML) insurance benefits if you earned $1,000 or more in 
the year prior to claiming benefits and the reason for the leave is due to one of the Qua lifying Reasons below.  
Qualifying Reasons. Eligible employees may receive pay continuation benefits for the following Qualifying Reasons:  
• Up to 12  weeks of benefits care for yourself or a family member.  
• Up to two  additional weeks for pregnancy, childbirth, or related circumstances.  
Wage Continuation Benefit . In the event  you approved for a leave of absence for a Qualifying Reason, you may file a claim 
to obtain pay continuation benefits. You may receive a weekly pay continuation payment. The amount of the payment 
will depend on your average weekly wage rate and can be up to 100% of your wages. Please review the FAQ linked at the bottom of this policy for additional information regarding filing a claim for PFML benefits.  
Automatic Payroll Deduction. The Company automatically contributes a portion of your paycheck to the PF ML insurance 
program. The contribution rate is set annually by the state’s Employment Department and will be determined once  
program costs are estimated. You will contribute 60% and the Company will contribute 40% of the required contribution. Your portion  is withheld from your pay, like income tax withholding.  
Overlap With Other Policies . To the extent legally permitted: you must follow the leave of absence procedures outlined 
in the applicable leave policy in the Handbook; and benefits/a leave of absence provided through this Policy will run concurrently with other benefits and/or leaves of absence provided by the Company.  
Additional . For additional information, please visit  the website below:  
https://www.oregon.gov/employ/PFMLI/Documents/PFMLI_003_0921.pdf
 
SUPPLEMENTAL BEREAVEMENT LEAVE  
Bereavement leave through this Policy runs concurrently with time off under the Bereavement Leave Policy in t he 
Company -wide Handbook.  
You are eligible for bereavement leave under this Policy if you have worked for the Company for at least 180 days and work at least 25 hours/week. 
When a death of a covered family member occurs, you may take up to ten days of unpaid bereavement leave. The leave 
must be completed within 60 days of receiving notice of the family member’s death. The total bereavement leave taken is counted toward the total of 12 weeks of family leave provided under the Oregon Family Leave Act, which is referenced in the Family Leave Policy above.  
For purposes of this Policy, a “covered family member” includes children, a spouse, parent, parent -in law, grandparent, 
or grandchild. 
If you need to take bereavement leave, you must notify your manager as soon as possible. Bereavement leave is available 
on the days (and at the time) that you would have otherwise been scheduled to work.  
The Company may provide additional bereavement time off, subject to the approval of the department manager and Human Resources. If you require additional bereavement time off, promptly notify Human Resources.
  
Page | 7 
Oregon Supplement  Handbook Supplement Acknowledgment– Oregon  
By signing below, I acknowledge receipt of this Handbook  Supplement  (“Supplement”) . I understand the practices, 
policies,  and procedures described in this Supplement and the Handbook together are designed to provide a summary of 
what I can expect from my employer, Abercrombie & Fitch, abercrombie kids, HOLLISTER, GILLY HICKS, and Social tourist 
(referred to as the “Company”) and what the Company expects from me. I also understand and acknowledge:  
• It is my responsibility to familiarize myself with and understand all information in this Supplement;  
• I agree to comply with the standards of conduct in this Supplement; 
• The Company may discipline me, including termination of my employment, if I violate any Company policy;  
• I have a duty to report certain conduct as specified in the policies within this Supplement; 
• This Supplement supersedes all previously issued supplements and any inconsistent written or verbal policy 
statements made or issued before this Supplement;  
• The Company reserves the right to amend, supplement, or rescind the policies described in this Supplement or to 
modify or deviate from such policies at any time without n otice. Delay or failure by the Company to enforce a 
policy or rule will not constitute a waiver of the Company’s right to do so in the future; 
• Neither this Supplement nor any other Company guidelines, policies, or practices create, or are intended to creat e 
a promise or representation of continued employment or an employment agreement. I understand and agree that I am employed at -will. The Company or I may terminate my employment with or without cause and with or 
without notice, at any time;  
• At this time, I have no employment -related claims of unlawful conduct pending with the Company or concerns 
that I have not yet raised with a member of management, Human Resources, or the One Number; and  
• I will contact Human Resources with any questions about this Supple ment . 
Signature _________________________________   Date _____________________  
Name ____________________________________ 
 
  
 
 
 
 
 
Associate Handbook 
Pennsylvania Supplement  
  

Page | 2 
Pennsylvania Supplement  Pennsylvania Supplement  
This document supplements the Handbook for  Abercrombie & Fitch Co.  referred to as “the Company.”  Abercrombie & 
Fitch Co. is a leading specialty retailer comprised of our brands including Abercrombie & Fitch, abercrombie kids, 
HOLLISTER,  GILLY HICKS, and Social Tourist. In this Handbook  Supplement , “Abercrombie” and “the Company” refers 
generally to all our brands, and particularly to the brand for which you will be working.  
Thro ughout this Supplement, you are directed to various team members. Their contact information is in the Company -
wide Handbook for ease of reference. If you have concerns, suggestions, or complaints relating to your employment, 
please utilize the reporting pr ocedures  in the Handbook and this Supplement.  
The Workday and Compensation  
UNPAID WAGES  
This Policy applies to associates  in Philadelphia.  
Paying associates properly is important to the Company. If you believe you were improperly paid, you must contact the 
Payroll Department  immediately. Please refer to the Payroll Policy in the Handbook  for additional information about how 
to report concerns  internally . You may  also file a wage theft complaint or bring a civil action for unpaid wages pursuant to 
Philadelphia’s Wage Theft Ordinance. A signed wage theft complaint, in which the alleged unpaid wages are equal to or greater than the minimum threshold amount of $100 and equal to or less than the maximum threshold amount of $100,000, must be filed with the wage theft coordinator in the Mayor’s Office of Benefits and Wage Compliance within 
three years from the date the alleged wage theft occurred. The Company prohibits retaliation for exercising rights 
provided under the Ordinance, such as filing a complaint or bringing a civil action.  
FAIR WORKWEEK SCHEDULING FOR EMPLOYEES IN PHILADELPHIA , PENNSYLVANIA  
You Have a Right to a Predictable Work Schedule Notice:  
Multilingual Poster, Fair Workweek resources | Department of Labor | City of Philadelphia :  
https://www.phila.gov/documents/fair -workweek -resources/   
Time Away From Work  
PAID SICK AND SAFE LEAVE FOR ASSOCIATES  IN PHILADELPHIA AND /OR PITTSBURGH  
For additional information about Paid Sick and Safe Leave (“PSSL”), please view the applicable poster below or contact Human Resources:  
Allegheny County: 
English Poster,  
www.alleghenycounty.us/uploadedFiles/Allegheny_Ho me/Dept_-
_Content/Administrative/Docs/Paid%20Sick%20Leave%20Ordinance%20 -%20notice.pdf  
Page | 3 
Pennsylvania Supplement  Spanish Poster,  
https://www.alleghenycounty.us/uploadedFiles/Allegheny_Home/Dept_ -
_Content/Administrative/Docs/Paid%20Sick%20Leave%20Ordinance%20Notice%20 -%20Spanish.pdf  
Philadelphia:  
Multilingual Posters,  
www.phila.gov/media/20191218103833/Paid -Sick-Leave -Poster -Translations.pdf  
Pittsburg:  
English Poster,  
https://apps.pittsburghpa.gov/redtail/images/9692_Notice -Paid -Sick-Days -Act_06 -2020.pdf  
Spanish Poster,  
https://apps.pittsburghpa.gov/redtail/images/9807_Updated_8014 -NOTICE -PAID -SICK -FINAL_06 -2020_Spanish.pdf  
Health and Safety  
WORKERS ’ COMPENSATION  
The Company provides workers’ compensation benefits for the protection of associates with work -related injuries or 
illness. If you are injured or become ill because of  your job, it is your responsibility to immediately notify the Risk 
Management Department of the injury to receive benefits. You have a duty to obtain treatment from one or more of the 
Company’s designated healthcare providers for 90 days from the date of the first visit to the designated provider. If  you 
obtain treatment from a designated prov ider over the 90 -day window, you have a right to have all reasonable medical 
supplies and treatment related to the injury paid for by the Company. During the 90 -day window, you have the right to:  
• Switch from one healthcare provider on the list to another provider on the list; all such treatment will be paid for by the Company;  
• Seek treatment from a referral provider if you are referred to a designated provider; the Company must pay for the treatment rendered by the referral provider;  
• Seek emergency medical treatment from a medical provider, but subsequent non -emergency treatment must be 
by a designated provider for the remainder of the 90 -day window;  
• Seek treatment or medical consultation from a non -designated provider during the 90 -day window; these service s 
will be at your expense during this time ; 
• Seek treatment from a healthcare provider after the 90 -day window ends; such treatment must be paid by the 
Company if it is reasonable and necessary; and  
• Seek an additional opinion from a healthcare provider of y our choice when a designated provider prescribes 
invasive surgery. If the additional opinion differs from the opinion of the designated provider and the additional opinion provides a specific and detailed course of treatment, you may determine which course  of treatment to 
follow. If you opt to follow the course of treatment outlined by the additional opinion, the treatment will be performed by one of the healthcare providers on the Company's designated list for 90 days from the date of the first visit to th e provider of the additional opinion.  
It is your obligation to notify the Company of treatment by a non -designated provider within five days of the first visit to 
that provider. The Company may not be required to pay for treatment rendered by a non -designa ted provider prior to 
Page | 4 
Pennsylvania Supplement  receiving this notification. However, the Company must pay for these services once notified, unless the treatment is found 
to be unreasonable. By signing the enclosed Acknowledgement, you agree and acknowledge that you received this P olicy.  
  
Page | 5 
Pennsylvania Supplement  Handbook Supplement Acknowledgment– Pennsylvania  
By signing below, I acknowledge receipt of this Handbook  Supplement  (“Supplement”) . I understand the practices, 
policies, and procedures described in this Supplement and the Handbook together are designed to provide a summary of 
what I can expect from my employer, Abercrombie & Fitch, abercrombie kids, HOLLISTER, GILLY HICKS, and Social  tourist 
(referred to as the “Company”) and what the Company expects from me. I also understand and acknowledge:  
• It is my responsibility to familiarize myself with and understand all information in this Supplement;  
• I agree to comply with the standards of conduct in this Supplement;  
• The Company may discipline me, including termination of my employment, if I violate any Company policy;  
• I have a duty to report certain conduct as specified in the policies within this Supplement; 
• This Supplement supersedes all previously issued supplements and any inconsistent written or verbal policy 
statements made or issued before this Supplement;  
• The Company reserves the right to amend, supplement, or rescind the policies described in this Supplement or to 
modif y or deviate from such policies at any time without notice. Delay or failure by the Company to enforce a 
policy or rule will not constitute a waiver of the Company’s right to do so in the future; 
• Neither this Supplement nor any other Company guidelines, po licies, or practices create, or are intended to create 
a promise or representation of continued employment or an employment agreement. I understand and agree that I am employed at -will. The Company or I may terminate my employment with or without cause and  with or 
without notice, at any time;  
• At this time, I have no employment -related claims of unlawful conduct pending with the Company or concerns 
that I have not yet raised with a member of management, Human Resources, or the One Number; and  
• I will contact  Human Resources with any questions about this Supplement . 
Signature _________________________________   Date _____________________  
Name ____________________________________ 
 
  
 
 
 
 
 
Associate Handbook 
Rhode Island Supplement  
  

Page | 2 
Rhode Island Supplement  Rhode Island Supplement  
This document supplements the Handbook for  Abercrombie & Fitch Co.  referred to as “the Company.”  Abercrombie & 
Fitch Co. is a leading specialty retailer comprised of our brands including Abercrombie & Fitch, abercrombie kids, 
HOLLISTER,  GILLY HICKS, and Social Tourist. In this Handbook  Supplement , “Abercrombie” and “the Company” refers 
generally to all our brands, and particularly to the brand for which you will be working.  
Throughout this Supplement, you are directed to various team members. Their contact information is in the Company -
wide Handbook for ease of reference. If you have concerns, suggestions, or complaints relating to your employment, 
please utilize the reporting procedures  in the Handbook and this Supplement.  
Inclusive Workplace Policies  
ACCOMMODATIONS AND DISCRIMINATION , HARASSMENT , AND RETALIATIO N PREVENTION  
This Policy supplements the Reasonable Accommodations  for Disabilities and the Discrimination, Harassment, and 
Retaliation Prevention Policies in the Handbook . 
The Company is committed to a work environment that respects and includes all assoc iates . The Company is also 
committed to providing reasonable accommodations for known limitations related to pregnancy and enforcing your right 
to be free from discrimination and unfair employment practices, including such conduct because of pregnancy, chi ldbirth, 
or related conditions. If you have concerns about unfair treatment, please refer to the Discrimination, Harassment, and Retaliation Prevention Policy in the Handbook  and contact the One Number . If you need a reasonable accommodation, 
please refer to the Reasonable Accommodations for Disabilities Policy and notify your manager, who will escalate the request to Human Resources.  
While we hope that you will raise concerns with us directly so we can promptly investigate and resolve the matter, you may also report potential sexual harassment to the EEOC or the Rhode Island Commission for Human Rights:  
https://schac.sc.gov/about -us/brochures -and-posters
 
Equal Employment Opportunity Commission 
(“EEOC”)  
JFK Federal Building, Room 475  
Boston, MA 02203  
617-565-3200  
 Rhode Island Commission for Human Rights  
180 Westminster Street, 3rd Floor  
Providence, RI 02903 401-277-2661  
The Workday and Compensation  
MEAL BREAKS  
This Policy supplements the Meal and Rest Break Policy in the Handbook.  
Meal Breaks. If you are an exempt associate  and work between six and eight hours in a workday, you are provided and 
may take an uninterrupted and work -free 20 -minute meal break and a second 30 -minute meal break when you work more 
than eight continuous hours. If you are a non- exempt and work between  six and eight hours in a workday, you are provided 
Page | 3 
Rhode Island Supplement  and may take an uninterrupted, work -free, and unpaid 30 -minute meal break and a second uninterrupted and work -free 
unpaid 30 -minute meal break If you work more than eight continuous hours.  
Meal Break Waiv er. With written approval from Human Resources, you may voluntarily waive meal breaks. If you wish to 
waive a meal break, you must contact Human Resources to obtain and complete  a waiver form.  
Logistics of Meal Breaks . Within the required window, the Company may schedule breaks to best accommodate operating 
requirements. If, however, your breaks are not scheduled in advance, please use your best judgment to decide when – 
within the required window – it is best to take your breaks, based on your workload and  operational demands. Please 
then attempt to contact your manager before you start your breaks to help the Company ensure proper staffing. If you cannot connect with your manager, please still proceed with your breaks. Meal breaks should occur away fr om your work 
area to the extent possible.  
Recording Meal Breaks . You must follow the timekeeping procedures set forth in the Timekeeping Policy in the Handbook . 
No Off -the-Clock Work . During these breaks, you are relieved of all work duties and may not perform work. Working off 
the clock is strictly prohibited  if you are a non -exempt associate.  This also means that during breaks, you are not expected 
to be available to take assignments or respond to work messages such as text messages, telephone calls, o r emails.  
Duty to Report . No one (manager or non -manager) is permitted to prevent or discourage you from taking a break as 
described above. If you believe you were prevented, interrupted, or discouraged from taking all or part of a break as 
provided in thi s Policy, or if you experience other circumstances inconsistent with this Policy, you have a duty to report 
the circumstances to the One Number  immediately. You must provide: (1) your name and work location; (2) the date(s) 
and time(s) at issue; and (3) a brief description of the conduct or circumstance(s).  
The Company will promptly investigate all such reports and will take corrective action when necessary to ensure that you are provided breaks in compliance with this Policy.  You will not be retaliated against for making a good -faith report under 
this Policy.  
Employment Standards  
WHISTLEBLOWER PROTECTIONS  
Rhode Island law provides you the right to report workplace practices or policies that you believe may be in violation of law, against public policy, and/or fraudulent or unethical. We will not take an  adverse employment action or otherwise 
retaliate against you (or a person acting on behalf of you) who:  
• Reports (or is about to report) to a member of management or a public body, a violation of law, regulation or rule issued under the law, known,  or reasonably believed to have occurred, or that is expected to occur;  
• Is asked by a public body to testify or participate in an investigation, hearing, or inquiry held by the public body or in a court action; or  
• Refuses to violate or assist in violating the law. 
To report a concern relating to the activities listed above, contact the Chief Ethics and Compliance Officer or the One 
Number . 
Page | 4 
Rhode Island Supplement  Time Away From Work  
PAID SICK AND SAFE LEAVE  
For additional information about  Paid Sick and Safe Leave (“PSSL”), please view the applicable poster below or contact 
Human Resources:  
Posters,  
https://dlt.ri.gov/employers/required -workplace -posters  
PAID TEMPORARY CAREGIVER INSURANCE BENEFITS AND LEAVE 
Temporary caregiver benefits are available through the Rhode Island “Temporary Caregiver Insurance” (“TCI”) program, 
which is administered by the Rhode Island Department of Labor and Training (“DLT”).  
Eligibility.  Under the TCI program, if you are out of work for at least seven consecutive days, you may be eligible for up to 
four weeks of caregiver leave and temporary caregiver wage replacement benefits within a 52-week period to care for a 
seriously ill child, spo use, domestic partner, parent, parent- in-law, or grandparent, or to bond with a newborn child, new 
adopted child, or new foster -care child. TCI benefits are only available to you if you are exercising your benefit to take a 
leave while covered by the TCI p rogram.  
Qualifying Events. TCI benefits are available for a week in which you are unable to perform your usual work because you 
are: 
(1) Bonding with a newborn child or a newly adopted child (during the first 12 months of parenting only); or  
(2) Caring for a child, a parent, parent -in-law, grandparent, spouse, or domestic partner, who has a serious health 
condition, subject to a waiting period (during which you may use available PTO ). 
TCI benefits are financed solely through your contributions to the TCI program, w hich is solely responsible for determining 
if you are eligible for such benefits.  
Notice of Time Off. If you are planning to take time off and apply for/receive TCI benefits, please provide us with a minimum of 30 days’ notice prior to the start of your caregiver leave, except in the event the time of the leave is unforeseeable or the time of the leave changes for unforeseeable circumstances, in which case you should provide notice as soon as practicable. Failure to provide us with this notice (for foreseeable absences) may result in delay or reduction in your benefits.  
Required Documentation. If your leave is to bond with a new child, you must provide a birth certificate, a certificate of 
adoption, or other documentation showing that you, your domestic part ner, or persons in loco parentis are the parent of 
the child within 12 months of the child's birth or placement for adoption or foster care. If your leave is to care for a 
seriously ill family member, your family member’s healthcare provider must complete a medical certification (which is 
available online here: http://www.dlt.ri.gov/tdi/).  
In the case of a parent (or persons who are in loco parentis caring for the serious health condition of a foster care child),  
you must submit all required information, with a written request to the Department of Children, Youth, and Families, for the release of medical information by the child’s treating licensed qualified healthcare provider. In the absence of the requested transmitted medical information by the Departmen t of Children, Youth and Families within ten business days, 
Page | 5 
Rhode Island Supplement  you may request the licensed qualified healthcare provider to directly transmit the medical eligibility of the serious health  
condition to the DLT.  
Benefit Continuation. During caregiver leave taken pursuant to this Policy, we will maintain your existing health benefits 
for the duration of the leave as if you had continued in employment continuously from the date you commenced the leave 
until the date the caregiver benefits terminate; provided, how ever, that you must continue to pay your  share of the cost 
of health benefits as required prior to the commencement of the caregiver benefits.  
Interaction with Statutory Leave and Company Benefits. In the case of a leave that qualifies under the TCI program and 
the federal FMLA and/or the RIPFLA, the leave will count against your entitlement under both of those laws and will run concurrently. Upon the expiration of TCI leave, you will be entitled to be restored to the position you held when your leave comme nced, or to a position with equivalent seniority, status, employment benefits, pay, and other terms and conditions 
of employment including fringe benefits and service credits that you were entitled to at the start of leave.  
If you have questions regarding this Policy, please contact the One Number . 
FAMILY AND MEDICAL LEAVE  
We are committed to providing time off to associates  for family and medical reasons. Please refer to the Family and 
Medical Leave Policy in the HR Corkboard in PeopleSoft HR ( https://my.anfcorp.com )for more information about the 
Compa ny’s leave -related benefits. The Company also provides leave to eligible associates  consistent with the Rhode Island 
Parental and Family Leave Act (“RIPFLA”). This Policy summarizes the benefits available through the RIPFLA.  
Eligibility.  You are eligible for RIPFLA leave if:  
(1) you have worked for the Company for at least 12 consecutive months;  
(2) you worked a full -time basis for an average of 30 or more hours per week; and  
(3) the Company have 50 or more associates  in Rhode Island.  
Leave Length . Eligible associates  may  take up to 13 consecutive workweeks of unpaid leave during a 24 -month period. 
The 24 -month RIPFLA period is determined based on a rolling period measured backwards from the date your leave will 
start.  
Qualifying Reasons. In addition to the entitlements outlined in the Family and Medical Leave Policy in the in the HR 
Corkboard in PeopleSoft HR ( https://my.anfcorp.com ), you may also take RIPFLA leave to care for your parent -in-law who 
has a serious health condition. RIPFLA does not cover leave for certain qualifying exigencies or to care for your child after  
placement for foster care. 
If Spouses Are Employed by the Same Company. If leave is taken for the birth and care of a newborn child, for placement 
of a child for adoption or foster care, or to care for a parent who has a serious health condition, to the extent you and a spouse both work for the Company, the RIPFLA leave benefits summarized in this Policy are separate for each of you.  
Intermittent Leave and Reduced Leave Schedules . You may not take intermittent leave under this Policy.  
No Retaliation. The Company will not retaliate against you for requesting a leave under this Policy. If you believe you were 
retaliated against, promptly contact the One Number .
  
Page | 6 
Rhode Island Supplement  Handbook Supplement Acknowledgment– Rhode Island  
By signing below, I acknowledge receipt of this Handbook  Supplement  (“Supplement”) . I understand the practices, 
policies, and procedures described in this Supplement and the Handbook together are designed to provide a summary of 
what I can expect from my employer, Abercrombie & Fitch, abercrombie kids, HOLLISTER, GILLY HICKS, and Social  tourist 
(referred to as the “Company”) and what the Company expects from me. I also understand and acknowledge:  
• It is my responsibility to familiarize myself with and understand all information in this Supplement;  
• I agree to comply with the standards of c onduct in this Supplement;  
• The Company may discipline me, including termination of my employment, if I violate any Company policy;  
• I have a duty to report certain conduct as specified in the policies within this Supplement; 
• This Supplement supersedes all previously issued supplements and any inconsistent written or verbal policy 
statements made or issued before this Supplement;  
• The Company reserves the right to amend, supplement, or rescind the policies described in this Supplement or to 
modify or deviate from such policies at any time without notice. Delay or failure by the Company to enforce a policy or rule will not constitute a waiver of the Company’s right to do so in the future; 
• Neither this Supplement nor any other Company guidelines, policies, or practices create, or are intended to create a promise or representation of continued employment or an employment agreement. I understand and agree that I am employed at -will. The Company or I may terminate my employment with or without cause and with or 
witho ut notice, at any time;  
• At this time, I have no employment -related claims of unlawful conduct pending with the Company or concerns 
that I have not yet raised with a member of management, Human Resources, or the One Number; and  
• I will contact Human Resources with  any questions about this Supplement . 
Signature _________________________________   Date _____________________  
Name ____________________________________ 
 
  
 
 
 
 
 
Associate Handbook 
South Carolina Supplement  
  

Page | 2 
South Carolina Supplement  South Carolina Supplement  
This document supplements the Handbook for  Abercrombie & Fitch Co.  referred to as “the Company.”  Abercrombie & 
Fitch Co. is a leading specialty retailer comprised of our brands including Abercrombie & Fitch, abercrombie kids, 
HOLLISTER,  GILLY HICKS, and Social Tourist. In this Handbook  Supplement , “Abercrombie” and “the Company” refers 
generally to all our brands, and particularly to the brand for which you will be working.  
Throughout this Supplement, you are directed to various team members. Their contact information is in the Company -
wide Handbook for ease of reference. If you have concerns, suggestions, or complaints relating to your employment, 
please utilize the reporting procedures  in the Handbook and this Supplement.  
Employment At -Will Disclaimer  
I AM EMPLOYED “AT-WILL .” AS A RESULT, UNLESS STATE LAW PROVIDES OTHERWISE, BOTH YOU AND/OR THE 
COMPANY MAY TERMINATE THE EMPLOYMENT RELATIONSHIP AT ANY TIME, FOR ANY LAWFUL REASON, OR NO 
REASON AT ALL, WITH OR WITHOUT ANY CAUSE OR PRIOR NOTICE. NO REPRESENTATIVE OF THE COMPANY, OTHER 
THAN AN OFFICER OF THE COMPANY OR THEIR DESIGNEE, HAS THE AUTHORITY TO ENTER INTO ANY AGREEMENT – 
EXPRESSED OR IMPLIED – FOR EMPLOYMENT FOR ANY SPECIFIED PERIOD, OR TO MAKE ANY AGREEMENT CONTRARY 
TO THE FOREGOING. ANY SUCH AGREEMENT PURPORTING TO ALTER THE AT -WILL NATURE OF EMPLOYMENT WITH 
THE COMPANY IN ANY MANNER MUST BE IN WRITING AND SIGNED BY AN OFFICER OF THE COMPANY OR THEIR 
DESIGNEE. THIS POLICY OF AT -WILL EMPLOYMENT CAN BE CHANGED ONLY IN WRITING SIGNED BY ME, THE VICE 
PRESIDENT OF HUMAN RESO URCES, AND THE PRESIDENT OF THE COMPANY. 
THE COMPANY’S POLICIES AND PROCEDURES, INCLUDING THOSE STATED IN THIS HANDBOOK AND THE HANDBOOK 
ITSELF, DO NOT CONTAIN AND ARE NOT TO BE INTERPRETED AS PROMISES OR CONTRACTS OF ANY KIND, REAL OR 
IMPLIED, BETWEEN THE  COMPANY AND ITS ASSOCIATES . THIS HANDBOOK IS NEITHER A CONTRACT OF EMPLOYMENT 
NOR A LEGAL DOCUMENT, AND NOTWITHSTANDING ANYTHING CONTAINED IN THIS HANDBOOK, THE COMPANY 
MAINTAINS THE RIGHT TO CHANGE OR TERMINATE THESE POLICIES OR PROCEDURES, AS WELL AS ANY OTHER 
WORKING CONDITIONS, AT ANY TIME, WITH OR WITHOUT NOTICE. 
Inclusive Workplace Policies  
PREGNANCY ACCOMMODATIONS AND PREGNANCY DISCRIMINATION , HARASSMENT , AND RETALIATION 
PREVENTION  
This Policy supplements the Reasonable Accommodations  for Disabiliti es and the Discrimination, Harassment, and 
Retaliation Prevention Policies in the Handbook . 
The Company is committed to providing reasonable accommodations for known limitations related to pregnancy. In 
addition, consistent with the Company’s values and the South Carolina Pregnancy Accommodations Act, you have a right to be free from discrimination in relation to pregnancy, childbirth, and related conditions. If you need a reasonable accommodation or if you have concerns about unfair treatment, please refer to the Reasonable Accommodations for Disabilities and the Discrimination, Harassment, and Retaliation Prevention Policies in the Handbook  and contact the One 
Number or your manager, who will escalate the request to the  Human Resources.  
 
Page | 3 
South Carolina Supplement  Handbook Supplement Acknowledgment– 
South Carolina  
By signing below, I acknowledge receipt of this Handbook  Supplement  (“Supplement”) . I understand the practices, 
policies, and procedures described in this Supplement and the Handbook together are designed to provide a summary of 
what I can expect from my e mployer, Abercrombie & Fitch, abercrombie kids, HOLLISTER, GILLY HICKS, and Social tourist 
(referred to as the “Company”) and what the Company expects from me. I also understand and acknowledge:  
• I received the employment -at will disclaimer in this Suppleme nt. 
• It is my responsibility to familiarize myself with and understand all information in this Supplement;  
• I agree to comply with the standards of conduct in this Supplement; 
• The Company may discipline me, including termination of my employment, if I violate any Company policy;  
• I have a duty to report certain conduct as specified in the policies within this Supplement; 
• This Supplement supersedes all previously issued supplements and any inconsistent written or verbal policy 
statements made or issued before this Supplement;  
• The Company reserves the right to amend, supplement, or rescind the policies described in this Supplement or to 
modify or deviate from such policies at any time without notice. Delay or failure by the Company to enforce a 
policy or rule will not constitute a waiver of the Company’s right to do so in the future;  
• Neither this Supplement nor any other Company guidelines, policies, or practices create, or are intended to create 
a promise or representation of continued employment or an employment  agreement. I understand and agree that 
I am employed at -will. The Company or I may terminate my employment with or without cause and with or 
without notice, at any time;  
• At this time, I have no employment -related claims of unlawful conduct pending with the Company or concerns 
that I have not yet raised with a member of management, Human Resources, or the One Number; and  
• I will contact Human Resources with any questions about this Supplement . 
Signature _________________________________   Date _____________________  
Name ____________________________________ 
 
  
 
 
 
 
 
Associate Handbook 
Tennessee Supplement  
  

Page | 2 
Tennessee Supplement  Tennessee Supplement  
This document supplements the Handbook for  Abercrombie & Fitch Co.  referred to as “the Company.”  Abercrombie & 
Fitch Co. is a leading specialty retailer comprised of our brands including Abercrombie & Fitch, abercrombie kids, 
HOLLISTER,  GILLY HICKS, and Social Tourist. In this Handbook  Supplement , “Abercrombie” and “the Company” refers 
generally to all our brands, and particularly to the brand for which you will be working.  
Throughout this Supplement, you are directed to various team members. Their contact information is in the Company -
wide Handbook for ease of reference. If you have concerns, suggestions, or complaints relating to your employment, 
please utilize the reporting procedures  in the Handbook and this Supplement.  
Inclusive Workplace Policies  
ABUSIVE CONDUCT PREVENTION  
The Company strives to provide high quality services in an atmosphere of respect, collaboration, openness, safety, and 
equality. All associates  have the right to be treated with dignity and respect. All complaints of negative and inappropriate 
workplace be haviors will be taken seriously, and associates  who file such a complaint or make a report in good faith will 
not suffer negative consequences for reporting others for inappropriate behavior.  
Abusive Conduct . For purposes of this Policy, abusive conduct in cludes acts or omissions that would cause a reasonable 
person, based on the severity, nature, and frequency of the conduct, to believe that you were being subjected to an abusive work environment. Abusive conduct can include but is not limited to:  
• Repeated verbal abuse in the workplace, including derogatory remarks, insults, and epithets; 
• Verbal, nonverbal, or physical conduct of a threatening, intimidating, or humiliating nature in the workplace; or  
• Sabotaging or undermining of an associate’s  work performance in the workplace.  
A single act typically will not be considered abusive conduct unless it is determined to be severe and egregious.  Examples 
of conduct that is not considered abusive conduct includes:  
• Discipline that an associate receives which  is related to violation of the Company’s policies including, but not 
limited to, those in the Handbook  and this Supplement;  
• Routine coaching and counseling ( e.g., feedback about and correction of work performance);  
• Reasonable work assignments ( e.g., a req uirement to work overtime or make modifications to one’s work 
schedule);  
• Individual differences in styles of personal expression;  
• Passionate, loud expression with no intent to harm others;  
• Differences of opinion on work -related concerns; or  
• Non -abusive exercise of managerial prerogative.  
Associate  Responsibilities . You are expected to treat all other associates with dignity and respect. This includes not 
engaging in threatening, violent, intimidating,  or other abusive conduct or behaviors. You are also e xpected to cooperate 
with preventative measures that we implement and to recognize that we will discipline anyone engaging in unacceptable 
Page | 3 
Tennessee Supplement  behavior. You are expected to assume personal responsibility to promote fairness and equity in the workplace and repo rt 
incidents of abusive conduct as set forth below . 
Our Responsibilities. The Company is committed to:  
• Providing a safe working environment;  
• Having preventative measures in place;  
• Immediately dealing with threatening or potentially violent situations;  
• Trea ting associates , customers , and others with whom we do business with courtesy and respect;  
• Ensuring that all e  associates have access to and are aware of this Policy, including the procedures to be followed 
if a complaint of inappropriate behavior at work is made;  
• Being vigilant for signs of inappropriate behaviors at work and acting to resolve the behavior before it escalates; 
and 
• Responding promptly, sensitively, and confidentially to all situations where abusive behavior is observed or alleged to have occurred.  
Reporting Procedure/Complaint Process.  If you believe  you were  subjected to or witnessed abusive conduct, promptly 
report the matter to your manager or the One Number . We ask that you provide as many precise details ( e.g., dates, 
times, locations, and any witnesses) as possible, as this improves our ability to understand, investigate, and appropriately 
address reported issues . Any manager or supervisor who learns of an  associate’s  concern about conduct in violation of 
this Policy, whether informally or through a formal complaint, is expected to immediately report it to the One Number . 
Investigation. Investigations of abusive conduct will be conducted as soon as practicable. Typically, the investigation will 
include  interviewing the complainant, accused, and witnesses. The investigation will be  conducted thoroughly, objectively, 
with sensitivity, and with respect for all people involved. We will strive to maintain confidentiality throughout the investigative process to the extent practicable, but our duty to investigate and take corrective action as appropriate may require the disclosure of certain information, and therefore complete confidentiality cannot be guaranteed. Upon completion of the investigation, we will evaluate the information gathered and will take appropriate remedial, corrective, and/or disciplinary action as necessary.  
Consequences for Violating this Policy.  If you engage  in conduct that violates this Policy or if you  encourage such conduct 
by others , you will be disciplined , up to and including termination. While the Company encourages all associates  to raise 
any concern(s) under this Policy, it is also recognized that intentional or maliciously false allegations can have a serious effect on innocent people. Anyone who falsely accuses another of violations of this Policy, provides false information during an investigation, or otherwise acts in bad faith in connection with the Company’s fulfillment of this Policy, will als o 
be disciplined , up to and including t ermination.  
No Retaliation.  The Company will not retaliate against you  for acting in accordance with Policy. If you believe you were 
retaliated against, promptly contact the One Number . 
The Workday and Compensation  
MEAL BREAKS  
This Policy replaces the Meal and Rest Break Policy in the Handbook.  
Page | 4 
Tennessee Supplement  Meal Breaks . If you work at least six consecutive hours, you are provided and may take an uninterrupted  and work -free 
30-minute meal break . This break is unpaid if you are a non -exempt associate . 
Meal Break Waive r. With written approval from Human Resources, you may voluntarily waive meal breaks. If you wish to 
waive a meal break, you must contact Human Resources to obtain and complete a waiver form.  
Logistics of Meal and Rest Breaks . Within the required window, the Company may schedule breaks to best accommodate 
operating requirements. If, however, your breaks are not scheduled in advance, please use your best judgment to decide 
when – within the required window – it is best to take your breaks, based on your workload and operational demands. 
Please then attempt to contact your manager before you start your breaks to help the Company ensure proper staffing. If you cannot connect with your manager, please still proceed with your breaks. Meal breaks should occur away from your work area to the extent possible.  
Recording Meal Breaks . You must follow the timekeeping procedures set forth in the Timekeeping Policy in the Handbook . 
No Off -the-Clock Work . During these breaks, you are relieved of all work duties and  may not perform work. Working off 
the clock is strictly prohibited  if you are a non -exempt associate . This also means that during breaks, you are not expected 
to be available to take assignments or respond to work messages such as text messages, telephone calls, or emails.  
Duty to Report . No one (manager or non -manager) is permitted to prevent or discourage you from taking a break as 
described above. If you believe you were prevented, interrupted, or discouraged from taking all or part of a break as 
provid ed in this Policy, or if you experience other circumstances inconsistent with this Policy, you have a duty to report 
the circumstances to the One Number  immediately. You must provide: (1) your name and work location; (2) the date(s) 
and time(s) at issue; and (3) a brief description of the conduct or circumstance(s).  
The Company will promptly investigate all such reports and will take corrective action when necessary to ensure that you are provided breaks in compliance with this Policy.  You will not be retaliated against for making a good -faith report under 
this Policy.  
Time Away From Work  
PARENTAL LEAVE 
We are committed to providing time off to parents following the birth or adoption of a child. To the extent the benefits 
below provide greater benefits than provided in the HR Corkboard in PeopleSoft HR ( https://my.anf corp.com ), the 
provisions below replace the corresponding provisions in the Handbook .  
Eligibility. You are eligible to take leave for a Qualifying Reason for up to four calendar months if you have worked for the 
Company for at least 12 consecutive months.  
Qualifying Reasons . You may take parental leave under this Policy for reasons related to pregnancy, childbirth, nursing, 
or for adoption (“parental leave”). With respect to adoptions, the leave period may begin when you receive custody of the child.  
Notice. To qualify for this leave, advance notice to your manager and the Benefits Department is required. Your notice 
must include the anticipated start date of your leave, the length of your leave, and the intended date of y our return to 
work. If you experience a medical emergency, your manager or Human Resources should be notified as soon as practicable.  
Page | 5 
Tennessee Supplement  Use of Leave. Leave under this Policy runs concurrently with leave provided under the Family and Medical Leave Policy in 
the HR Corkboard in PeopleSoft HR ( https://my.anfcorp.com ). 
Reinstatement. If you provide three months’ notice, you will be reinstated to the same or a similar position after ret urning 
from leave. Rest assured that you do not forfeit rights and benefits if you were prevented from giving three months’ notice 
due to a medical emergency or because notice of the adoption was received fewer than three months in advance. The 
Company cannot guarantee that your position will be available if you are unable to return to work after the leave as provided in this Policy.  
No Retaliation. The Company will not retaliate against you for requesting a leave under this Policy. If you believe you were 
retaliated against, promptly report the retaliation by contacting the One Number . 
  
Page | 6 
Tennessee Supplement  Handbook Supplement Acknowledgment–Tennessee 
By signing below, I acknowledge receipt of this Handbook  Supplement  (“Supplement”) . I understand the practices, 
policies, and procedures described in this Supplement and the Handbook together are designed to provide a summary of 
what I can expect from my employer, Abercrombie & Fitch, abercrombie kids, HOLLISTER, GILLY HICKS, and Social  tourist 
(referred to as the “Company”) and what the Company expects from me. I also understand and acknowledge:  
• It is my responsibility to familiarize myself with and understand all information in this Supplement;  
• I agree to comply with the standards of c onduct in this Supplement;  
• The Company may discipline me, including termination of my employment, if I violate any Company policy;  
• I have a duty to report certain conduct as specified in the policies within this Supplement; 
• This Supplement supersedes all previously issued supplements and any inconsistent written or verbal policy 
statements made or issued before this Supplement;  
• The Company reserves the right to amend, supplement, or rescind the policies described in this Supplement or to 
modify or deviate from such policies at any time without notice. Delay or failure by the Company to enforce a policy or rule will not constitute a waiver of the Company’s right to do so in the future; 
• Neither this Supplement nor any other Company guidelines, policies, or practices create, or are intended to create a promise or representation of continued employment or an employment agreement. I understand and agree that I am employed at -will. The Company or I may terminate my employment with or without cause and with or 
witho ut notice, at any time;  
• At this time, I have no employment -related claims of unlawful conduct pending with the Company or concerns 
that I have not yet raised with a member of management, Human Resources, or the One Number; and  
• I will contact Human Resourc es with  any questions about this Supplement . 
Signature _________________________________   Date _____________________  
Name ____________________________________ 
 
  
 
 
 
 
 
Associate Handbook 
Texas  Supplement  
  

Page | 2 
Texas Supplement  Texas Supplement  
This document supplements the Handbook for  Abercrombie & Fitch Co.  referred to as “the Company.”  Abercrombie & 
Fitch Co. is a leading specialty retailer comprised of our brands including Abercrombie & Fitch, abercrombie kids, 
HOLLISTER,  GILLY HICKS, and Social Tourist. In this Handbook  Supplement , “Abercrombie” and “the Company” refers 
generally to all our brands, and particularly to the brand for which you will be working.  
Throughout this Supplement, you are directed to various team members. Their contact information is in the Company -
wide Handbook for ease of reference. If you have concerns, suggestions, or complaints relating to your employment, 
please utilize the reporting procedures  in the Handbook and this Supplement.  
Health and Safety  
WORKERS ’ COMPENSATION  
The Company has workers' compensation insurance coverage in the event of a work -related injury or occupational disease.  
This coverage is currently effective. Any injuries or occupational diseases which occur during your employment will be 
handled by the Company’s workers’ compensation carrier. You, or a person acting on your behalf, must notify the Company of an injury or occupational disease no later than the 30th day after the date on which the injury occurred or 
the date you knew or should have known of an occupational disease, unless the Texas Department of Insurance, Division of Workers’ Compensation (Division) determines that good cause existed for failure to provide timely notice. The Company is required to provide you with coverage information, in writing, when you are hired (which is satisfied through this Policy)  
or whenever the Company becomes, or ceases to be, co vered by workers' compensation insurance.  
You may elect to retain your common law right of action if, no later than five days after you begin employment or within five days after receiving written notice from the Company that the Company has obtained work ers compensation 
insurance coverage, you notify the Company in writing that you wish to retain your common law right to recover damages for personal injury. If you elect to retain your common law right of action, you cannot obtain workers’ compensation income or medical benefits if you are injured.   
Page | 3 
Texas Supplement  Handbook Supplement Acknowledgment– Texas  
By signing below, I acknowledge receipt of this Handbook  Supplement  (“Supplement”) . I understand the practices, 
policies, and procedures described in this Supplement and the Handbook together are designed to provide a summary of 
what I can expect from my employer, Abercrombie & Fitch, abercrombie kids, HOLLISTER, GILLY HICKS, and Social tourist 
(referred to as the “Company”) and what the Company expects from me. I also understand and acknowledge:  
• It is my responsibility to familiarize myself with and understand all information in this Supplement;  
• I agree to comply with the standards of conduct in this Supplement; 
• The Company may discipline me, including termination of my employment, if I violate any Company policy;  
• I have a duty to report certain conduct as specified in the policies within this Supplement; 
• This Supplement supersedes all previously issued supplements and any inconsistent written or verbal policy 
statements made or issued before this Supplement;  
• The Company reserves the right to amend, supplement, or rescind the policies described in this Supplement or to 
modify or deviate from such policies at any time without n otice. Delay or failure by the Company to enforce a 
policy or rule will not constitute a waiver of the Company’s right to do so in the future; 
• Neither this Supplement nor any other Company guidelines, policies, or practices create, or are intended to creat e 
a promise or representation of continued employment or an employment agreement. I understand and agree that I am employed at -will. The Company or I may terminate my employment with or without cause and with or 
without notice, at any time;  
• At this time, I have no employment -related claims of unlawful conduct pending with the Company or concerns 
that I have not yet raised with a member of management, Human Resources, or the One Number; and  
• I will contact Human Resources with any questions about this Supple ment . 
Signature _________________________________   Date _____________________  
Name ____________________________________ 
 
  
 
 
 
 
 
Associate Handbook 
Utah Supplement  
  

Page | 2 
Utah Supplement  Utah Supplement  
This document supplements the Handbook for  Abercrombie & Fitch Co.  referred to as “the Company.”  Abercrombie & 
Fitch Co. is a leading specialty retailer comprised of our brands including Abercrombie & Fitch, abercrombie kids, 
HOLLISTER,  GILLY HICKS, and Social Tourist. In this Handbook  Supplement , “Abercrombie” and “the Company” refers 
generally to all our brands, and particularly to the brand for which you will be working.  
Throughout this Supplement, you are directed to various team members. Their contact information is in the Company -
wide Handbook for ease of reference. If you have concerns, suggestions, or complaints relating to your employment, 
please utilize the reporting procedures  in the Handbook and this Supplement.  
Inclusive Workplace Policies  
PREGNANCY ACCOMMODATIONS AND PREGNANCY DISCRIMINATION , HARASSMENT , AND RETALIATION  
PREVENTION  
This Policy supplements the Reasonable Accommodations  for Disabilities and the Discrimination, Harassment, and 
Retaliation Prevention Policies in the Handbook . 
The Company is committed to providing reasonable accommodations for known limitations related to pregnancy. In 
addition, consistent with the Company’s  values, you have a right to be free from discrimination in relation to pregnancy, 
childbirth, and related conditions. If you need a reasonable accommodation or if you have concerns about unfair treatment, please refer to the Reasonable Accommodations for Disabilities and the Discrimination, Harassment, and Retaliation Prevention Policies in the Handbook  and notify  your manager who will escalate the request to  Human 
Resources. 
 
Page | 3 
Vermont Supplement  Handbook Supplement Acknowledgment– Utah  
By signing below, I acknowledge receipt of this Handbook  Supplement  (“Supplement”) . I understand the practices, 
policies, and procedures described in this Supple ment and the Handbook together are designed to provide a summary of 
what I can expect from my employer, Abercrombie & Fitch, abercrombie kids, HOLLISTER, GILLY HICKS, and Social tourist 
(referred to as the “Company”) and what the Company expects from me. I  also understand and acknowledge:  
• It is my responsibility to familiarize myself with and understand all information in this Supplement;  
• I agree to comply with the standards of conduct in this Supplement; 
• The Company may discipline me, including termination  of my employment, if I violate any Company policy;  
• I have a duty to report certain conduct as specified in the policies within this Supplement; 
• This Supplement supersedes all previously issued supplements and any inconsistent written or verbal policy 
statements made or issued before this Supplement;  
• The Company reserves the right to amend, supplement, or rescind the policies described in this Supp lement or to 
modify or deviate from such policies at any time without notice. Delay or failure by the Company to enforce a 
policy or rule will not constitute a waiver of the Company’s right to do so in the future; 
• Neither this Supplement nor any other Comp any guidelines, policies, or practices create, or are intended to create 
a promise or representation of continued employment or an employment agreement. I understand and agree that I am employed at -will. The Company or I may terminate my employment with or  without cause and with or 
without notice, at any time;  
• At this time, I have no employment -related claims of unlawful conduct pending with the Company or concerns 
that I have not yet raised with a member of management, Human Resources, or the One Number; and  
• I will contact Human Resources with any questions about this Supplement . 
Signature _________________________________   Date _____________________  
Name ____________________________________ 
 
 
  
 
 
 
 
 
Associate Handbook 
Virginia Supplement  
  

Page | 2 
Virginia Supplement  Virginia Supplement  
This document supplements the Handbook for  Abercrombie & Fitch Co.  referred to as “the Company.”  Abercrombie & 
Fitch Co. is a leading specialty retailer comprised of our brands including Abercrombie & Fitch, abercrombie kids, 
HOLLISTER,  GILLY HICKS, and Social Tourist. In this Handbook  Supplement , “Abercrombie” and “the Company” refers 
generally to all our brands, and particularly to the brand for which you will be working .  
Throughout this Supplement, you are directed to various team members. Their contact information is in the Company -
wide Handbook for ease of reference. If you have concerns, suggestions, or complaints relating to your employment, please utilize the repor ting procedures  in the Handbook and this Supplement.  
Inclusive Workplace Policies  
PREGNANCY ACCOMMODATIONS AND PREGNANCY DISCRIMINATION , HARASSMENT , AND RETALIATION 
PREVENTION  
This Policy supplements the Reasonable Accommodations  for Disabilities and the Discrimination, Harassment, and 
Retaliation Prevention Policies in the Handbook . 
The Company is committed to providing reasonable accommodations for known limitations related to pregnancy. In 
addition, consistent with the Company’s  values, you have a right to be free from discrimination in relation to pregnancy, 
childbirth, and related conditions. If you need a reasonable accommodation or if you have concerns about unfair treatment, plea se refer to the Reasonable Accommodations for Disabilities and the Discrimination, Harassment, and 
Retaliation Prevention Policies in the Handbook  and notify  your manager, who will escalate the request to  Human 
Resources. For more information, please view the State’s fact sheet available here:  
https://www.doli.virginia.gov/wp -content/uploads/2020/11/OUTREACH_INFO -SHEET_PREGNANCY -DISCN -
PROVISIONS_2020 -07-17_FINAL.pdf  
 
  
Page | 3 
Virginia Supplement  Handbook Supplement Acknowledgment– Virginia  
By signing below, I acknowledge receipt of the Abercrombie & Fitch, abercrombie kids, HOLLISTER, GILLY HICKS, and Social 
Tourist (“the Company”) Supplement to the Handbook. I understand the practices, policies, and procedures described in this Supplement are designed to provide a summary of what I can expect from the Company and what the Company expects from me. I also understand and acknowledge:  
• It is my responsibi lity to familiarize myself with and understand all information in this Supplement;  
• I agree to comply with the standards of conduct in this Supplement; 
• The Company may discipline me, including termination of my employment, if I violate any Company policy;  
• I have a duty to report certain conduct as specified in the policies within this Supplement; 
• This Supplement supersedes all previously issued supplements and inconsistent written or verbal policy 
statements made or issued before this Supplement;  
• The Company reserves the right to amend, supplement, or rescind the policies described in this Supplement or to 
modify or deviate from such policies at any time without notice. Delay or failure by the Company to enforce a 
policy or rule will not constitute a waiver of the Company’s right to do so in the future;  
• Neither this Supplement nor any other Company guidelines, policies, or practices create, or are intended to create a promise or representation of continued employment or an employment agreement. I understand and agree that I am employed at -will. The Company or I may terminate my employment with or without cause and with or 
without notice, at any time;  
• At this time, I have no employment -related claims of unlawful conduct pending with the Company or conc erns 
that I have not yet raised with a member of management, Human Resources, or the One Number; and  
• I will contact Human Resources with questions about this Handbook.  
Signature _________________________________   Date _____________________  
Name ____________________________________ 
 
  
 
 
 
 
 
Associate Handbook 
Washington Supplement  
  

Page | 2 
Washington Supplement  Washington Supplement  
This document supplements the Handbook for  Abercrombie & Fitch Co.  referred to as “the Company.”  Abercrombie & 
Fitch Co. is a leading specialty retailer comprised of our brands including Abercrombie & Fitch, abercrombie kids, 
HOLLISTER,  GILLY HICKS, and Social Tourist. In this Handbook  Supplement , “Abercrombie” and “the Company” refers 
generally to all our brands, and particularly to the brand for which you will be working.  
Throughout this Supplement, you are directed to various team members. Their contact information is in the Company -
wide Handbook for ease of reference. If you have concerns, suggestions, or complaints relating to your employment, 
please utilize the reporting procedures  in the Handbook and this Supplement.  
The Workday and Compensation  
MEAL AND REST BREAKS  
This Policy supplements the Meal and Rest Break Policy in the Handbook.  
This Policy applies to non- exempt associate s only . 
Rest Breaks . If you are a non -exempt associate , you are provided and may take an uninterrupted, work -free, and paid ten-
minute rest break during every four hours worked . The rest breaks should occur as close as possible to the middle of each 
four -hour period as is practicable.  
Meal Breaks . If you are a non -exempt associate , and you work more than five consecutive hours,  you are provided and 
may take an uninterrupted, work -free, and unpaid 30 -minute meal break . This break should occur between the second 
and fifth hours of work . If you work at least three hours longer than your normal workday or shift, you are provided and  
may take a meal break before or during that three -hour period . For purposes of this Policy, a “normal workday” is the shift 
or workday that you are regularly assigned.  
Meal Break Waiver . With written approval from Human Resources, you may voluntarily waiv e meal breaks. If you wish to 
waive a meal break, you must contact Human Resources to obtain and complete a waiver form.  
Logistics of Meal and Rest Breaks . Within the required window, the Company may schedule breaks to best accommodate 
operating requirements. If, however, your breaks are not scheduled in advance, please use your best judgment to decide 
when – within the required window – it is best to take your breaks, based on your workload and operational demands. 
Please then attempt to contact your manager before you start your breaks to help the Company ensure proper staffing. If 
you cannot connect with your manager, please still proceed with your breaks. Meal and/or rest breaks should occur away from your work area to the extent possible.  
Recording Meal  and Rest  Breaks . You must follow the timekeeping procedures set forth in the Timekeeping Policy in the 
Handbook . 
No Off -the-Clock Work . During these breaks, you are relieved of all work duties and may not perform work. Working off 
the clock is strictly prohibited  if you are a non -exempt associate . This also means that during breaks, you are not expected 
to be available to take assignments or respond to work messages such as text messages, telephone calls, or emails.  
Page | 3 
Washington Supplement  Duty to Report . No one (ma nager or non -manager) is permitted to prevent or discourage you from taking a break as 
described above. If you believe you were prevented, interrupted, or discouraged from taking all or part of a break as 
provided in this Policy, or if you experience other circumstances inconsistent with this Policy, you have a duty to report 
the circumstances to the One Number  immediately. You must provide: (1) your name and work location; (2) the date(s) 
and time(s) at issue; and (3) a brief description of the conduct or circumstance(s).  
The Company will promptly investigate all such reports and will take corrective action when necessary to ensure that you 
are provided breaks in compliance with this Policy.  You will not be retaliated against for making a good -faith report under 
this Policy.  
Time Away From Work  
PAID SICK AND SAFE LEAVE  
For additional information about Paid Sick and Safe Leave (“PSSL”), please view the applicable poster below or contact Human Resources:  
English Poster,  
https://view.officeapps.live.com/op/view.aspx?src=https%3A%2F%2Flni.wa.gov%2Fforms -publications%2Ff700 -191-
000.docx&wdOrigin=BROWSELINK  
Spanish Poster,  
https://view.officeapps.live.com/op/view.aspx?src=https%3A%2F%2Fwww.lni.wa.gov%2Fworkers -
rights%2F_docs%2FEmployeePaidSickLeaveNotificationFormSpanish.docx&wdOrigin=BROWSELINK  
English Poster, https://www.seattle.gov/documents/Departments/LaborStandards/2023_OLS_WorkplacePoster%5B42%5D.pdf
 
Spanish Poster, https://www.seattle.gov/documents/Departments/LaborStandards/2022Workplace%20Poster%20FINAL -Spanish.pdf
 
Tacoma : 
English Poster,  
https://cms.cityoftacoma.org/finance/paid- leave/notices/2018 -Paid -Leave -Workplace -Notice -English.pdf  
Spanish Poster,  
https://cms.cityoftacoma.org/finance/paid- leave/notices/2018 -Paid -Leave -Workplace -Notice -Spanish.pdf  
PREGNANCY DISABILITY LEAVE  
This Policy provides unpaid leave for the period  that you are sick or temporarily  disabled because of pregnancy, childbirth, 
or related medical conditions.  
To the extent practicable, you must provide your manager and the Benefits Department with reasonable advance notice 
prior to taking leave; otherwise, provide notice as soon as possible under the circumstances. We may require that you provide reasonable documentation to support your need for leave and/or upon returning to work.  
Leave under this Policy runs concurrently with leave under the FMLA , applicable state law s, and  applicable C ompany -
provided leaves. Likewise, during this leave, you must use available PTO benefits.  
Page | 4 
Washington Supplement  If you take this leave only for the period of your disability, as certified by a healthcare provider, you ordinarily will be 
allowed to return to the same job you hel d when the leave began, or to a similar job of at least the same pay.  
PAY CONTINUATION DURING FAMILY AND MEDICAL LEAVE 
Eligibility. You may be eligible for Paid Family and Medical Leave (PFML) program benefits if: you have worked for the 
Company for at  least 12 months and 1,250 hours; you are on a leave of absence for one of the Qualifying Reasons below.  
Qualifying Reasons. Eligible employees may receive PFML pay continuation benefits for the following Qualifying Reasons:  
(1) Following the birth or placement of a child (through birth, adoption, or foster placement);  
(2) A serious health condition;  
(3) A child, parent, parent -in-law, spouse, domest ic partner, sibling, grandchild, or grandparent’s (“family member”) 
serious health condition; or  
(4) To prepare for a family member’s pre - and post -deployment activities and/or attend to childcare issues related to 
a family member’s military deployment.  
Wage Replacement Benefits. PFML benefits are funded through payroll contributions you make. In addition, if the 
Company has more than 50 employees in Washington, the Company also contributes to the PFML benefits.  To be eligible 
for PFML benefits, you must file a claim for benefits with the ESD by visiting https://www.paidleave.wa.gov/  or completing 
a paper application. If the ESD determines that you are eligible, a partial wage replacement calculated as a percentage of 
gross wages should be available from the PFML.   
Automatic Payroll Deductions. The Company automatically contributes a portion of your paycheck to the st ate’s as 
described in more detail below.  
Overlap With Other Policies . To the extent legally permitted: you must follow the leave of absence procedures outlined 
in the applicable leave policy in the Handbook  or in the HR Corkboard in PeopleSoft HR ( https://my.anfcorp.com ); and 
benefits/a leave of absence provided through this Policy will run concurrently with other benefits and/or leaves of absence provided by the Company.  
Additional Information. The Company will not retaliate against you for requesting a leave under this Policy. If you believe 
you were retaliated against, promptly notify Human Resources. For additional information regarding paid family and 
medical leave, pl ease refer to the State’s poster, available here:  
https://paidleave.wa.gov/app/uploads/2020/11/2020.11.2.FNL_WPFML -poster_EN.pdf  
SUPPLEMENTAL BEREAVEMENT LEAVE  
Bereavement leave through this Policy runs concurrently with time off under the Bereavement Leave Policy in the Company -wide Handbook.  
When a death of a family or household member occurs, you may take up to three days of pa id bereavement leave. 
Additionally, employees eligible for Paid Family and Medical Leave (PFML) may take up to seven additional days of PFML to bereave the death of a newborn or newly adopted/fostered child; for additional information please refer to the P aid 
Family and Medical Leave Policy  in the HR Corkboard in PeopleSoft HR ( https://my.anfcorp.com
). 
Page | 5 
Washington Supplement  If you need to take bereavement leave, you must notify your manager as soon as possible. Bereavement leave is available 
on the days (and at the time) that you would have otherwise been scheduled to work.  
The Company may provide additional bereavement time off, subject to the approval of the department manager and 
Human Resources. If you require additional bereavement time off, promptly notify Human Resources.  
FAMILY LEAVE 
We are committed to providing time off  to associates  for family and medical reasons. Please refer to the Handbook  and 
the HR Corkboard in PeopleSoft HR ( https://my.anfcorp.com ) for more information about the Company’s leave -related 
benefits. In addition to leave provided through the various Company policies, please note that you may use available  PTO 
to care for a child with a health condition  that requires supervision or treatment, a spouse, registered domestic partner, 
parent, parent -in-law, or grandparent who has an emergency health condition, among any other personal reason.   
Page | 6 
Washington Supplement  Handbook Supplement Acknowledgment– Washington  
By signing below, I  acknowledge receipt of this Handbook  Supplement  (“Supplement”) . I understand the practices, 
policies, and procedures described in this Supplement and the Handbook together are designed to provide a summary of 
what I can expect from my employer, Abercrombie & Fitch, abercrombie kids, HOLLISTER, GILLY HICKS, and Social tourist (referred to as the “Company”) and what the Company expects from me. I also understand and acknowledge:  
• It is my responsibility to familiarize myself with and understand all information in this Supplement;  
• I agree to comply with the standards of conduct in this Supplement; 
• The Company may discipline me, including termination of my employment, if I violate  any Company policy;  
• I have a duty to report certain conduct as specified in the policies within this Supplement; 
• This Supplement supersedes all previously issued supplements and  any inconsistent written or verbal policy 
statements made or issued before th is Supplement;  
• The Company reserves the right to amend, supplement, or rescind the policies described in this Supplement or to 
modify or deviate from such policies at any time without notice. Delay or failure by the Company to enforce a policy or rule will  not constitute a waiver of the Company’s right to do so in the future;  
• Neither this Supplement nor any other Company guidelines, policies, or practices create, or are intended to create a promise or representation of continued employment or an employment agreement. I understand and agree that I am employed at -will. The Company or I may terminate my employment with or without cause and with or 
without notice, at any time;  
• At this time, I have no employment -related claims of unlawful conduct pending with th e Company or concerns 
that I have not yet raised with a member of management, Human Resources, or the One Number; and  
• I will contact Human Resources with any questions about this Supplement . 
Signature _________________________________   Date _____________________ 
Name ____________________________________ 
 
  
 
 
 
 
 
Associate Handbook 
West Virginia Supplement  
  

Page | 2 
West Virginia Supplement  
 West Virginia Supplement  
This document supplements the Handbook for  Abercrombie & Fitch Co.  referred to as “the Company.”  Abercrombie & 
Fitch Co. is a leading specialty retailer comprised of our brands including Abercrombie & Fitch, abercrombie kids, 
HOLLISTER,  GILLY HICKS, and Social Tourist. In this Handbook  Supplement , “Abercrombie” and “the Company” refers 
generally to all our brands, and particularly to the brand for which you will be working.  
Throughout this Supplement, you are directed to various team members. Their conta ct information is in the Company -
wide Handbook for ease of reference. If you have concerns, suggestions, or complaints relating to your employment, 
please utilize the reporting procedures  in the Handbook and this Supplement.  
The Workday and Compensation  
MEAL BREAKS  
This Policy replaces the Meal and Rest Break Policy in the Handbook.  
Meal Breaks . If you are a non -exempt associate  and you work six or more continuous hours, you are provided and may 
take an uninterrupted, work -free, and unpaid 30 -minute meal break . If you are an exempt associate  and you work six or 
more continue hours, you are provided and may take an uninterrupted, work -free, and paid 20 -minute meal break.  
Meal Break Waiver . With written approval from Human Resources, you may voluntarily  waive meal breaks. If you wish to 
waive a meal break, you must contact Human Resources to obtain and complete a waiver form.  
Logistics of Meal Breaks . Within the required window, the Company may schedule breaks to best accommodate operating 
requirements. If, however, your breaks are not scheduled in advance, please use your best judgment to decide when – 
within the required window – it is best to take your breaks, based on your workload and operational demands. Please 
then attempt to contact your manager b efore you start your breaks to help the Company ensure proper staffing. If you 
cannot connect with your manager, please still proceed with your breaks. Meal breaks should occur away from your work area to the extent possible.  
Recording Meal Breaks . You mus t follow the timekeeping procedures set forth in the Timekeeping Policy in the Handbook . 
No Off -the-Clock Work . During these breaks, you are relieved of all work duties and may not perform work. Working off 
the clock is strictly prohibited  if you are a non -exempt associate . This also means that during breaks, you are not expected 
to be available to take assignments or respond to work messages such as text messages, telephone calls, or emails.  
Duty to Report . No one (manager or non -manager) is permitted to prevent or discourage you from taking a break as 
described above. If you believe you were prevented, interrupted, or discouraged from taking all or part of a break as 
provided in this Policy, or if you experience other circumstances inconsistent with this Policy, you have a duty to report the circumstances to the One Number  immediately. You must provide: (1) your name and work location; (2) the date(s) 
and time(s) at issue; and (3) a brief description of the c onduct or circumstance(s).  
The Company will promptly investigate all such reports and will take corrective action when necessary to ensure  that you 
are provided breaks in compliance with this Policy.  You will not be retaliated against for making a good -faith report under 
this Policy.  
Page | 3 
West Virginia Supplement  
 Handbook Supplement Acknowledgment– West Virginia  
By signing below, I acknowledge receipt of this Handbook  Supplement  (“Supplement”) . I understand the practices, 
policies, and procedures described in this Supplement and the Handbook together are designed to provide a summary of 
what I can expect from my e mployer, Abercrombie & Fitch, abercrombie kids, HOLLISTER, GILLY HICKS, and Social tourist 
(referred to as the “Company”) and what the Company expects from me. I also understand and acknowledge:  
• It is my responsibility to familiarize myself with and unders tand all information in this Supplement;  
• I agree to comply with the standards of conduct in this Supplement; 
• The Company may discipline me, including termination of my employment, if I violate any Company policy;  
• I have a duty to report certain conduct as specified in the policies within this Supplement; 
• This Supplement supersedes all previously issued supplements and any inconsistent written or verbal policy 
statements made or issued before this Supplement;  
• The Company reserves the right to amend, supplement, or rescind the policies described in this Supplement or to 
modify or deviate from such policies at any time without notice. Delay or failure by the Company to enforce a policy or rule will not constitute a waiver of the Company’s right to do so in the future;  
• Neither this Supplement nor any other Company guidelines, policies, or practices create, or are intended to create a promise or representation of continued employment or an employment agreement. I understand and agree that I am employed at -will. Th e Company or I may terminate my employment with or without cause and with or 
without notice, at any time;  
• At this time, I have no employment -related claims of unlawful conduct pending with the Company or concerns 
that I have not yet raised with a member o f management, Human Resources, or the One Number; and  
• I will contact Human Resources with any questions about this Supplement . 
Signature _________________________________   Date _____________________  
Name ____________________________________ 
 
  
 
 
 
 
 
Associate Handbook 
Wisconsin Supplement  
  

Page | 2 
Wisconsin Supplement  Wisconsin Supplement  
This document supplements the Handbook for  Abercrombie & Fitch Co.  referred to as “the Company.”  Abercrombie & 
Fitch Co. is a leading specialty retailer comprised of our brands including Abercrombie & Fitch, abercrombie kids, 
HOLLISTER,  GILLY HICKS, and Social Tourist. In this Handbook  Supplement , “Abercrombie” and “the Company” refers 
generally to all our brands, and particularly to the brand for which you will be working.  
Thro ughout this Supplement, you are directed to various team members. Their contact information is in the Company -
wide Handbook for ease of reference. If you have concerns, suggestions, or complaints relating to your employment, 
please utilize the reporting pr ocedures  in the Handbook and this Supplement.  
Time Away From Work  
FAMILY AND MEDICAL LEAVE 
We are committed to providing time off to associates  for family and medical reasons. Please refer to the Family and 
Medical Leave Policy in the HR Corkboard in PeopleSoft HR ( https://my.anfcorp.com )for more information about the 
Compa ny’s leave -related benefits.  The Company also provides leave to eligible associates  consistent with the Wisconsin 
Family and Medical Leave Act (“WFMLA”), which is similar to the leave provided under the Family and Medical Leave Policy. This Policy summarizes the benefits available through the WFMLA.  
Eligibility.  You are eligible for leave under the WFMLA if:  
(1) You have worked for the Company for at least 52 consecutive weeks;  
(2) You have worked at least 1,000 hours in the 52 weeks preceding the start of leave; and  
(3) The Company has 50 or more associates . 
Leave Length and Qualifying Reasons.  Under the WFMLA, you may take an unpaid leave as follows:  
(1) Up to six workweeks for birth or adoption of a child;  
(2) Up to two workweeks for your own serious health condition; and  
(3) Up to two workweeks to care for a covered family member with a serious health condition.  
Leave because of the birth or adoptive placement of a child must begin within 16 weeks before or after the birth or adoption.  
For purposes of this Polic y, the 12 -month period is measured by a calendar year from January 1
st to December 31st. The 
total leave will not exceed ten weeks in a 12-month period except for leave to care for an injured servicemember (which 
may not exceed 26 weeks during a single 12 -month period).  
Additionally, you may also take leave to care for a domestic partner or parent -in-law who has a serious health condition.  
Leave under this Policy does not include leave for certain qualifying exigencies or to care for your child after placem ent 
for foster care. 
Substitution of Paid Leave.  You may elect to use accrued PTO  while taking unpaid WFMLA leave. The substitution of paid 
time for unpaid WFMLA leave time does not extend the length of WFMLA leave. In addition, leave under this Policy run s 
Page | 3 
Wisconsin Supplement  concurrently with leave provided under the Family and Medical Leave Policy in the HR Corkboard in PeopleSoft HR 
(https://my.anfcorp.com ). 
No Retaliation. The Company will not retaliate against you for requesting a leave under this Policy. If you believe you were 
retaliated against, promptly contact the One Number . 
Page | 4 
Wisconsin Supplement  Handbook Supplement Acknowledgment–Wisconsin 
By signing below, I acknowledge receipt of this Handbook  Supplement  (“Supplement”) . I understand the practices, 
policies, and procedures described in this Supplement and the Handbook together are designed to provide a summary of 
what I can expect from my employer, Abercrombie & Fitch, abercrombie kids, HOLLISTER, GILLY HICKS, and Social  tourist 
(referred to as the “Company”) and what the Company expects from me. I also understand and acknowledge:  
• It is my responsibility to familiarize myself with and understand all information in this Supplement;  
• I agree to comply with the standards of c onduct in this Supplement;  
• The Company may discipline me, including termination of my employment, if I violate any Company policy;  
• I have a duty to report certain conduct as specified in the policies within this Supplement; 
• This Supplement supersedes all previously issued supplements and any inconsistent written or verbal policy 
statements made or issued before this Supplement;  
• The Company reserves the right to amend, supplement, or rescind the policies described in this Supplement or to 
modify or deviate from such policies at any time without notice. Delay or failure by the Company to enforce a policy or rule will not constitute a waiver of the Company’s right to do so in the future; 
• Neither this Supplement nor any other Company guidelines, policies, or practices create, or are intended to create a promise or representation of continued employment or an employment agreement. I understand and agree that I am employed at -will. The Company or I may terminate my employment with or without cause and with or 
witho ut notice, at any time;  
• At this time, I have no employment -related claims of unlawful conduct pending with the Company or concerns 
that I have not yet raised with a member of management, Human Resources, or the One Number; and  
• I will contact Human Resourc es with any questions about this Supplement . 
Signature _________________________________   Date _____________________  
Name ____________________________________ 
 

""".strip()

COMPANY_NAME = "Abercrombie & Fitch"

DENY_MESSAGE = (
    "I can only answer questions about the employee handbook and official company policies. "
    "For other topics, please contact HR."
)


def load_handbook_file(path: str) -> str:
    """Load handbook text from a file path and return it as a stripped string.

    Raises FileNotFoundError if path doesn't exist; raises other IO errors as normal.
    """
    if not path:
        raise ValueError("path must be a non-empty string")
    if not os.path.exists(path):
        raise FileNotFoundError(f"Handbook file not found: {path}")
    with open(path, "r", encoding="utf-8") as f:
        return f.read().strip()


# Convenience: allow loading a handbook from an environment variable at import time.
_env_path = os.environ.get("HANDBOOK_PATH")
if _env_path:
    try:
        HANDBOOK_TEXT = load_handbook_file(_env_path)
    except Exception:
        # Don't fail import if env path is invalid; let the application decide how to handle it.
        pass

# Sanitize handbook text: remove non-printable/control characters (except newline/tab)
def _clean_handbook_text(s: str) -> str:
    if not isinstance(s, str):
        return s
    # Normalize unicode to decompose compatibility characters
    s = unicodedata.normalize("NFKC", s)
    cleaned_chars = []
    for ch in s:
        cat = unicodedata.category(ch)
        # Keep newlines and tabs even though they are in control categories
        if ch in ("\n", "\t"):
            cleaned_chars.append(ch)
            continue
        # Skip other control or format characters (Cc, Cf, etc.)
        if cat.startswith("C"):
            continue
        cleaned_chars.append(ch)
    # Trim leading/trailing whitespace while preserving internal formatting
    return "".join(cleaned_chars).strip()

# Apply cleaning in place to remove stray control characters introduced during upload.
HANDBOOK_TEXT = _clean_handbook_text(HANDBOOK_TEXT)

