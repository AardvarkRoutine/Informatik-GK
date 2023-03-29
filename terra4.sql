/* Aufg. a)*/
SELECT ort.Name
FROM ort 
INNER JOIN stadtfluss ON ort.ONR = stadtfluss.ONR 
INNER JOIN fluss ON stadtfluss.FNR = fluss.FNR
WHERE
fluss.Name = "Lauter"

/* Aufg. b)*/
SELECT DISTINCT land.Name FROM land
INNER JOIN ort ON land.LNR = ort.LNR
INNER JOIN stadtfluss ON ort.ONR = stadtfluss.ONR 
INNER JOIN fluss ON stadtfluss.FNR = fluss.FNR
WHERE fluss.Name = "Donau"

/* Aufg. c)*/
SELECT count(DISTINCT fluss.Name) AS Anzahl_Flüsse
FROM fluss
INNER JOIN stadtfluss ON stadtfluss.FNR = fluss.FNR
INNER JOIN ort ON ort.ONR = stadtfluss.ONR
INNER JOIN land ON ort.LNR = land.LNR
WHERE land.Name = "Deutschland"

/* Aufg. d)*/
SELECT DISTINCT fluss.Name 
FROM fluss
INNER JOIN stadtfluss ON stadtfluss.FNR = fluss.FNR
INNER JOIN ort ON ort.ONR = stadtfluss.ONR 
WHERE ort.Breite BETWEEN ((SELECT ort.Breite FROM ort WHERE ort.Name = 'Kusel') - 0.5) AND ((SELECT ort.Breite FROM ort WHERE ort.Name = 'Kusel') + 0.5)
AND ort.Laenge BETWEEN ((SELECT ort.Laenge FROM ort WHERE ort.Name = 'Kusel') - 0.5) AND ((SELECT ort.Laenge FROM ort WHERE ort.Name = 'Kusel') + 0.5);

/* Deutscher Ort mit höchster Einwohnerzahl*/
SELECT ort.Name, ort.Einwohner
FROM ort
INNER JOIN land ON ort.LNR = land.LNR
WHERE land.Name = "Deutschland"
ORDER BY ort.Einwohner DESC
LIMIT 1
