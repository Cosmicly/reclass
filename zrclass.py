Excellent, that confirms everything lines up exactly as expected. You're ready to execute.

Confirmed Execution Plan: NON_CHEMICAL → CHEMICAL (OSR_ID = 2, LOCS_0026)
Current State:

RS_CURRENT_VALUE = 12 (last CHEMICAL sequence)
Sequence 12 = LOCS_0025 = CHEMICAL
Sequence 13 = LOCS_0026 = NON_CHEMICAL ← This becomes CHEMICAL

Target State:

RS_CURRENT_VALUE = 13
Sequence 12 = LOCS_0025 = CHEMICAL
Sequence 13 = LOCS_0026 = CHEMICAL ← After reclass


Execute in Order:
sql-- ============================================
-- STEP 1: Update main location zone (200 → 201)
-- ============================================
UPDATE location_zones 
SET lz_zone_id = 201
WHERE lz_zone_id = 200
  AND lz_osr_id = 2 
  AND lz_loc_id LIKE '%00026_';

-- ============================================
-- STEP 2: Update Level-Aisle-Block zones (+10000)
-- ============================================
UPDATE location_zones 
SET lz_zone_id = lz_zone_id + 10000 
WHERE lz_osr_id = 2 
  AND lz_loc_id LIKE '%00026_'
  AND lz_zone_id IN (
    SELECT zone_id FROM zones 
    WHERE zone_osr_id = 2
      AND zone_name LIKE 'SBLOC%LEVEL%NON_CHEM%'
  );

COMMIT;

-- ============================================
-- STEP 3: Update storage zone of empty containers
-- ============================================
UPDATE containers 
SET cont_storage_zone_id = 201
WHERE cont_id IN (
  SELECT cont_id
  FROM containers 
  JOIN container_locations ON cl_cont_id = cont_id 
  JOIN location_zones ON lz_loc_id = cl_loc_id 
  JOIN zones ON zone_id = lz_zone_id 
  JOIN locations ON loc_id = cl_loc_id 
  WHERE cont_storage_zone_id <> zone_id 
    AND loc_type_id = 0 
    AND cont_stream_type = 'EMPTY'
    AND zone_osr_id = 2 
    AND zone_id = 201
);

COMMIT;

-- ============================================
-- STEP 4: Update reassignment configuration
-- ============================================
UPDATE reassignment_sequences 
SET rs_current_value = 13 
WHERE rs_zone_a = 'CHEMICAL' 
  AND rs_zone_b = 'NON_CHEMICAL'
  AND rs_osr_id = 2
  AND rs_current_value = 12;

UPDATE reassignment_zones 
SET rz_rs_zone = 'CHEMICAL'
WHERE rz_osr_id = 2
  AND rz_sequence = 13;

COMMIT;


-- Verify reassignment updated correctly
SELECT rs_current_value FROM reassignment_sequences WHERE rs_osr_id = 2;
-- Expected: 13

SELECT rz_zone_id, rz_zone_name, rz_rs_zone, rz_sequence 
FROM reassignment_zones 
WHERE rz_osr_id = 2 AND rz_sequence IN (12, 13, 14)
ORDER BY rz_sequence;
-- Expected:
-- 25, LOCS_0025, CHEMICAL, 12
-- 26, LOCS_0026, CHEMICAL, 13
-- 27, LOCS_0027, NON_CHEMICAL, 14





CALL THESE OUT:
SELECT cont_id, 
       'get_tray --tray ' || cont_id || ' --target NON_CHEMICAL' AS command
FROM containers 
JOIN container_locations ON cl_cont_id = cont_id 
JOIN location_zones ON lz_loc_id = cl_loc_id 
JOIN zones ON zone_id = lz_zone_id 
JOIN locations ON loc_id = cl_loc_id 
WHERE cont_storage_zone_id <> zone_id 
  AND loc_type_id = 0 
  AND cont_stream_type != 'EMPTY'
  AND zone_osr_id = 2 
  AND zone_id = 201
  AND ROWNUM <= 500
ORDER BY cont_id;

-- Confirm reassignment_zones updated
SELECT rz_zone_id, rz_zone_name, rz_rs_zone, rz_sequence 
FROM reassignment_zones 
WHERE rz_osr_id = 2 AND rz_sequence IN (12, 13, 14)
ORDER BY rz_sequence;
-- Expected: seq 12 = CHEMICAL, seq 13 = CHEMICAL, seq 14 = NON_CHEMICAL

-- Confirm no zone mismatches remain for empties
SELECT COUNT(*) 
FROM containers 
JOIN container_locations ON cl_cont_id = cont_id 
JOIN location_zones ON lz_loc_id = cl_loc_id 
JOIN zones ON zone_id = lz_zone_id 
JOIN locations ON loc_id = cl_loc_id 
WHERE cont_storage_zone_id <> zone_id 
  AND loc_type_id = 0 
  AND cont_stream_type = 'EMPTY'
  AND zone_osr_id = 2;
-- Expected: 0


