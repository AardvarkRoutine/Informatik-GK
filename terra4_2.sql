/* inf-schule 3.1.5.4 Aufg. 7*/
SELECT 
  MIN(ort.Breite) AS Most_Southern_Ort, 
  MAX(ort.Breite) AS Most_Northern_Ort, 
  MIN(ort.Laenge) AS Most_Western_Ort, 
  MAX(ort.Laenge) AS Most_Eastern_Ort 
FROM ort 
INNER JOIN land ON ort.LNR = land.LNR 
WHERE land.Name = 'Frankreich';

/* inf-schule 3.1.5.4 Aufg. 7 mit Ortsnamen*/
SELECT 
  (SELECT ort.Name FROM ort INNER JOIN land ON ort.LNR = land.LNR WHERE land.Name = 'Frankreich' AND ort.Laenge = (SELECT MIN(Laenge) FROM ort INNER JOIN land ON ort.LNR = land.LNR WHERE land.Name = 'Frankreich')) AS Most_Western_Ort_Name,
  (SELECT ort.Name FROM ort INNER JOIN land ON ort.LNR = land.LNR WHERE land.Name = 'Frankreich' AND ort.Laenge = (SELECT MAX(Laenge) FROM ort INNER JOIN land ON ort.LNR = land.LNR WHERE land.Name = 'Frankreich')) AS Most_Eastern_Ort_Name,
  (SELECT ort.Name FROM ort INNER JOIN land ON ort.LNR = land.LNR WHERE land.Name = 'Frankreich' AND ort.Breite = (SELECT MIN(Breite) FROM ort INNER JOIN land ON ort.LNR = land.LNR WHERE land.Name = 'Frankreich')) AS Most_Southern_Ort_Name,
  (SELECT ort.Name FROM ort INNER JOIN land ON ort.LNR = land.LNR WHERE land.Name = 'Frankreich' AND ort.Breite = (SELECT MAX(Breite) FROM ort INNER JOIN land ON ort.LNR = land.LNR WHERE land.Name = 'Frankreich')) AS Most_Northern_Ort_Name,
  MIN(ort.Breite) AS Most_Southern_Ort_Latitude, 
  MAX(ort.Breite) AS Most_Northern_Ort_Latitude, 
  MIN(ort.Laenge) AS Most_Western_Ort_Longitude, 
  MAX(ort.Laenge) AS Most_Eastern_Ort_Longitude 
FROM ort 
INNER JOIN land ON ort.LNR = land.LNR 
WHERE land.Name = 'Frankreich';