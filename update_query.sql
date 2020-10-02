SELECT
  *
FROM tests.destinatarios;

UPDATE tests.destinatarios A
INNER JOIN tests.destinatarios B ON A.id_uruguay = B.id_uruguay
SET
  A.tmp_ci = CONCAT("uy-ci-", SUBSTRING_INDEX(B.id_uruguay, '-', -1));