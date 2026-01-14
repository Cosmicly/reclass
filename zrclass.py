I have to do a reclass to get more chemical storage locations. Here are the steps:

Check if there's 1X free position (1X is one sequence, 2X is two sequence.)
    Sequence represent for the same position in all aisles and levels.
    
    X = sides * depth * Aisles * Levels
    5760 is the minimum free position that is needed for the zone reclass. (Not including the reserved position)

Step 2:
Then you will need to select the proper position depending on the sequencing for the manual zone reclass config

Step 2-A:
SELECT * FROM REASSIGNMENT_SEQUENCES
WHERE RS_OSR_ID = 2
Output:
RS_ID,RS_ZONE_A,RS_ZONE_B,RS_CURRENT_VALUE,RS_PARENT_RS_ID,RS_DESCRIPTION,RS_VISIBLE,RS_ZONE_REFERENCE,RS_OSR_ID
1,CHEMICAL,NON_CHEMICAL,12,,Chemical to non-chemical,1,,2 

Step 2-b:
Query:
select * from reassignment_zones 
WHERE rz_osr_id = 2
order by rz_sequence
Output:
RZ_ZONE_ID,RZ_ZONE_NAME,RZ_RS_ZONE,RZ_RS_ID,RZ_SEQUENCE,RZ_DIRTY,RZ_OSR_ID
14,LOCS_0014,CHEMICAL,1,1,0,2
15,LOCS_0015,CHEMICAL,1,2,0,2
16,LOCS_0016,CHEMICAL,1,3,0,2
17,LOCS_0017,CHEMICAL,1,4,0,2
18,LOCS_0018,CHEMICAL,1,5,0,2
19,LOCS_0019,CHEMICAL,1,6,0,2
20,LOCS_0020,CHEMICAL,1,7,0,2
21,LOCS_0021,CHEMICAL,1,8,0,2
22,LOCS_0022,CHEMICAL,1,9,0,2
23,LOCS_0023,CHEMICAL,1,10,0,2
24,LOCS_0024,CHEMICAL,1,11,0,2
25,LOCS_0025,CHEMICAL,1,12,0,2
26,LOCS_0026,NON_CHEMICAL,1,13,0,2
27,LOCS_0027,NON_CHEMICAL,1,14,0,2
28,LOCS_0028,NON_CHEMICAL,1,15,0,2
29,LOCS_0029,NON_CHEMICAL,1,16,0,2
30,LOCS_0030,NON_CHEMICAL,1,17,0,2
31,LOCS_0031,NON_CHEMICAL,1,18,0,2
32,LOCS_0032,NON_CHEMICAL,1,19,0,2
33,LOCS_0033,NON_CHEMICAL,1,20,0,2
34,LOCS_0034,NON_CHEMICAL,1,21,0,2
35,LOCS_0035,NON_CHEMICAL,1,22,0,2
36,LOCS_0036,NON_CHEMICAL,1,23,0,2
37,LOCS_0037,NON_CHEMICAL,1,24,0,2
38,LOCS_0038,NON_CHEMICAL,1,25,0,2
39,LOCS_0039,NON_CHEMICAL,1,26,0,2
40,LOCS_0040,NON_CHEMICAL,1,27,0,2
41,LOCS_0041,NON_CHEMICAL,1,28,0,2
42,LOCS_0042,NON_CHEMICAL,1,29,0,2
43,LOCS_0043,NON_CHEMICAL,1,30,0,2
44,LOCS_0044,NON_CHEMICAL,1,31,0,2
45,LOCS_0045,NON_CHEMICAL,1,32,0,2
46,LOCS_0046,NON_CHEMICAL,1,33,0,2
47,LOCS_0047,NON_CHEMICAL,1,34,0,2
48,LOCS_0048,NON_CHEMICAL,1,35,0,2
49,LOCS_0049,NON_CHEMICAL,1,36,0,2
50,LOCS_0050,NON_CHEMICAL,1,37,0,2
51,LOCS_0051,NON_CHEMICAL,1,38,0,2
52,LOCS_0052,NON_CHEMICAL,1,39,0,2
53,LOCS_0053,NON_CHEMICAL,1,40,0,2
54,LOCS_0054,NON_CHEMICAL,1,41,0,2
55,LOCS_0055,NON_CHEMICAL,1,42,0,2
56,LOCS_0056,NON_CHEMICAL,1,43,0,2
57,LOCS_0057,NON_CHEMICAL,1,44,0,2
58,LOCS_0058,NON_CHEMICAL,1,45,0,2
59,LOCS_0059,NON_CHEMICAL,1,46,0,2
60,LOCS_0060,NON_CHEMICAL,1,47,0,2
61,LOCS_0061,NON_CHEMICAL,1,48,0,2
62,LOCS_0062,NON_CHEMICAL,1,49,0,2
63,LOCS_0063,NON_CHEMICAL,1,50,0,2
64,LOCS_0064,NON_CHEMICAL,1,51,0,2
65,LOCS_0065,NON_CHEMICAL,1,52,0,2
66,LOCS_0066,NON_CHEMICAL,1,53,0,2
67,LOCS_0067,NON_CHEMICAL,1,54,0,2
68,LOCS_0068,NON_CHEMICAL,1,55,0,2
69,LOCS_0069,NON_CHEMICAL,1,56,0,2
70,LOCS_0070,NON_CHEMICAL,1,57,0,2
71,LOCS_0071,NON_CHEMICAL,1,58,0,2
72,LOCS_0072,NON_CHEMICAL,1,59,0,2
73,LOCS_0073,NON_CHEMICAL,1,60,0,2
74,LOCS_0074,NON_CHEMICAL,1,61,0,2
75,LOCS_0075,NON_CHEMICAL,1,62,0,2
76,LOCS_0076,NON_CHEMICAL,1,63,0,2
77,LOCS_0077,NON_CHEMICAL,1,64,0,2
78,LOCS_0078,NON_CHEMICAL,1,65,0,2
80,LOCS_0080,NON_CHEMICAL,1,67,0,2
81,LOCS_0081,NON_CHEMICAL,1,68,0,2
82,LOCS_0082,NON_CHEMICAL,1,69,0,2
83,LOCS_0083,NON_CHEMICAL,1,70,0,2
84,LOCS_0084,NON_CHEMICAL,1,71,0,2
85,LOCS_0085,NON_CHEMICAL,1,72,0,2
86,LOCS_0086,NON_CHEMICAL,1,73,0,2
87,LOCS_0087,NON_CHEMICAL,1,74,0,2
88,LOCS_0088,NON_CHEMICAL,1,75,0,2
89,LOCS_0089,NON_CHEMICAL,1,76,0,2
90,LOCS_0090,NON_CHEMICAL,1,77,0,2
91,LOCS_0091,NON_CHEMICAL,1,78,0,2
92,LOCS_0092,NON_CHEMICAL,1,79,0,2
93,LOCS_0093,NON_CHEMICAL,1,80,0,2
94,LOCS_0094,NON_CHEMICAL,1,81,0,2
95,LOCS_0095,NON_CHEMICAL,1,82,0,2
96,LOCS_0096,NON_CHEMICAL,1,83,0,2
97,LOCS_0097,NON_CHEMICAL,1,84,0,2
98,LOCS_0098,NON_CHEMICAL,1,85,0,2
99,LOCS_0099,NON_CHEMICAL,1,86,0,2
100,LOCS_0100,NON_CHEMICAL,1,87,0,2
101,LOCS_0101,NON_CHEMICAL,1,88,0,2
102,LOCS_0102,NON_CHEMICAL,1,89,0,2
103,LOCS_0103,NON_CHEMICAL,1,90,0,2
104,LOCS_0104,NON_CHEMICAL,1,91,0,2
105,LOCS_0105,NON_CHEMICAL,1,92,0,2
106,LOCS_0106,NON_CHEMICAL,1,93,0,2
107,LOCS_0107,NON_CHEMICAL,1,94,0,2
108,LOCS_0108,NON_CHEMICAL,1,95,0,2
109,LOCS_0109,NON_CHEMICAL,1,96,0,2
110,LOCS_0110,NON_CHEMICAL,1,97,0,2
111,LOCS_0111,NON_CHEMICAL,1,98,0,2
112,LOCS_0112,NON_CHEMICAL,1,99,0,2
113,LOCS_0113,NON_CHEMICAL,1,100,0,2
114,LOCS_0114,NON_CHEMICAL,1,101,0,2
115,LOCS_0115,NON_CHEMICAL,1,102,0,2
116,LOCS_0116,NON_CHEMICAL,1,103,0,2
117,LOCS_0117,NON_CHEMICAL,1,104,0,2
118,LOCS_0118,NON_CHEMICAL,1,105,0,2
119,LOCS_0119,NON_CHEMICAL,1,106,0,2
120,LOCS_0120,NON_CHEMICAL,1,107,0,2
121,LOCS_0121,NON_CHEMICAL,1,108,0,2
122,LOCS_0122,NON_CHEMICAL,1,109,0,2
123,LOCS_0123,NON_CHEMICAL,1,110,0,2
124,LOCS_0124,NON_CHEMICAL,1,111,0,2
125,LOCS_0125,NON_CHEMICAL,1,112,0,2
126,LOCS_0126,NON_CHEMICAL,1,113,0,2
127,LOCS_0127,NON_CHEMICAL,1,114,0,2
128,LOCS_0128,NON_CHEMICAL,1,115,0,2
129,LOCS_0129,NON_CHEMICAL,1,116,0,2
130,LOCS_0130,NON_CHEMICAL,1,117,0,2
131,LOCS_0131,NON_CHEMICAL,1,118,0,2

Example:
In one example from a different time we did this, we are going from sequence 16 --> 15, thus we changed location x.0097.x  from CHEM to NON_CHEM.
The RZ_ZONE_ID and the RZ_ZONE_NAME are referring to the position SA01.AISLE.LEVEL.SECTION.0097.R/L.

Step 3:
Change the location_zones for that x on level locations aisle block location and main chem/non_chem

update location_zones 
-- New location zone 100: NON_CHEM, 101: CHEM
set lz_zone_id=100 
where 
-- Current location zone 100: NON_CHEM, 101: CHEM
lz_zone_id=101 
and lz_osr_id=1 
-- specific which location for the reclass, last digit for side(left/right)
and lz_loc_id like '%00097_';

    CHEMICAL ZONE ID is always 10000 greater than the NON_CHEMICAL ZONE ID.
    Level - Block
    101021400	SBLOCK_1_LEVEL_14_NON_CHEMICAL
    101031400	SBLOCK_1_LEVEL_14_CHEMICAL
    Level - Aisle - Block
    101020226	SBLOCK_1_LEVEL_2_AISLE_26_NON_CHEMICAL
    101030226	SBLOCK_1_LEVEL_2_AISLE_26_CHEMICAL

update location_zones 
-- CHEM to NON_CHEM -10000, NON_CHEM TO CHEM +10000
set lz_zone_id=lz_zone_id-10000 
where 
lz_osr_id=1 
-- specific the location needs the reclass,  last digit for side(left/right)
and lz_loc_id like '%00097_'
and lz_zone_id in (select zone_id from zones where zone_osr_id = 1
and zone_name like 'SBLOC%LEVEL%_CHEM%') ;


COMMIT;

Step 4:
Change storage zone of the empties to the new zone

update containers set cont_storage_zone_id = 100 where cont_id in (
select cont_id
from containers join container_locations on cl_cont_id = cont_id join location_zones on lz_loc_id = cl_loc_id join zones on
zone_id = lz_zone_id join locations on loc_id = cl_loc_id where
cont_storage_zone_id <> zone_id and loc_type_id = 0 and cont_empty=1
and zone_osr_id = 1 and zone_id in (100));

COMMIT;

Step 5:
Change the configs for manual zone reclass to match the new distribution
    Update the reassignment_sequences and reassignment_zones order by rz_sequence

update reassignment_sequences set rs_current_value=15 
WHERE RS_ZONE = 'CHEMICAL' AND RS_CURRENT_VALUE = 16

update reassignment_zones set rz_rs_zone='NON_CHEMICAL'
where rz_sequence in (16)

COMMIT;

Step 6:
Relocate all containers remaining in the wrong zone with products from command line in server, can build query to show the get_tray output for the container AB2xxxx% - 
    get_tray for the return result for below query until it return nothing.
     get_tray --tray <AB2xxxxxx> --target POOL_GF1

select cont_id, 'get_tray --tray '|| cont_id || '  --target CHEMICAL'
from containers join container_locations on cl_cont_id = cont_id join location_zones on lz_loc_id = cl_loc_id join zones on
zone_id = lz_zone_id join locations on loc_id = cl_loc_id where
cont_storage_zone_id <> zone_id and loc_type_id = 0 and cont_empty=0
and zone_osr_id = 1 and zone_id in (100) and ROWNUM <= 500
order by cont_id;

So the reclass I am doing, I need to change non-chem -> chem. Can you develop a plan exactly the same way using the queries I provided and output which is expected ?

This is for osr_id 2 only, cannot use "    AND cont_empty = 1" would have to be "    AND cont_stream_type = 'EMPTY' ".

For the sequence, set the sequence to the then last chemical rz_sequence which is 12 currently if i select from reassignment zones where rz_osr_id = 2:
"""
RZ_ZONE_ID,RZ_ZONE_NAME,RZ_RS_ZONE,RZ_RS_ID,RZ_SEQUENCE,RZ_DIRTY,RZ_OSR_ID
14,LOCS_0014,CHEMICAL,1,1,0,2
15,LOCS_0015,CHEMICAL,1,2,0,2
16,LOCS_0016,CHEMICAL,1,3,0,2
17,LOCS_0017,CHEMICAL,1,4,0,2
18,LOCS_0018,CHEMICAL,1,5,0,2
19,LOCS_0019,CHEMICAL,1,6,0,2
20,LOCS_0020,CHEMICAL,1,7,0,2
21,LOCS_0021,CHEMICAL,1,8,0,2
22,LOCS_0022,CHEMICAL,1,9,0,2
23,LOCS_0023,CHEMICAL,1,10,0,2
24,LOCS_0024,CHEMICAL,1,11,0,2
25,LOCS_0025,CHEMICAL,1,12,0,2
26,LOCS_0026,NON_CHEMICAL,1,13,0,2
27,LOCS_0027,NON_CHEMICAL,1,14,0,2
28,LOCS_0028,NON_CHEMICAL,1,15,0,2
29,LOCS_0029,NON_CHEMICAL,1,16,0,2
30,LOCS_0030,NON_CHEMICAL,1,17,0,2
31,LOCS_0031,NON_CHEMICAL,1,18,0,2
32,LOCS_0032,NON_CHEMICAL,1,19,0,2
33,LOCS_0033,NON_CHEMICAL,1,20,0,2
34,LOCS_0034,NON_CHEMICAL,1,21,0,2
35,LOCS_0035,NON_CHEMICAL,1,22,0,2
36,LOCS_0036,NON_CHEMICAL,1,23,0,2
37,LOCS_0037,NON_CHEMICAL,1,24,0,2
38,LOCS_0038,NON_CHEMICAL,1,25,0,2
39,LOCS_0039,NON_CHEMICAL,1,26,0,2
40,LOCS_0040,NON_CHEMICAL,1,27,0,2
"""
So 'LOCS_0026' should just stay rz_sequence = 13, and rz_rs_zone should just change to chemical ?
So please begin building the plan.
