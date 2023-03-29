/* 1.:*/
SELECT sum(land.Einwohner) AS Einwohner_in_Mio from land, kontinent
WHERE land.KNR = kontinent.KNR AND kontinent.Name = "Europa"

/* 2.:*/
SELECT count(land.Name) AS Länder_in_Europa FROM land, kontinent
WHERE land.KNR = kontinent.KNR AND kontinent.Name = "Europa"

/* 3.:*/
SELECT count(ort.name) AS Orte_größer_10Mio FROM ort
WHERE Einwohner>10000000

/* 4.:*/

SELECT ort.Name, min(ort.Breite) AS Breitengrad FROM ort, land
WHERE ort.LNR = land.LNR AND land.Name = "Deutschland"

/* 5.:*/
SELECT avg(ort.Einwohner) AS durchschn_Einwohner from ort, land
WHERE ort.LNR = land.LNR AND land.Name = "Frankreich"

/* 6.:*/
SELECT count(ort.name) as Einwohner_ind_Megacitiy FROM ort, land
WHERE ort.LNR = land.LNR AND land.Name = "Indien" AND ort.Einwohner > 1000000