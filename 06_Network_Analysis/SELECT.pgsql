SELECT
  created AS "time",
  state AS metric,
  state_id
FROM states
WHERE
created >= '2020-10-01' AND
  entity_id = sensor.fibaro_system_fgwpef_wall_plug_power