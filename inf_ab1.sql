/*1., 2.:*/
SELECT land.Name, land.Einwohner
From land, kontinent
WHERE land.KNR=kontinent.KNR AND kontinent.Name="Asien"
ORDER BY Einwohner DESC

/*3.:*/
SELECT land.Name, land.Flaeche
From land, kontinent
WHERE land.KNR=kontinent.KNR AND kontinent.Name="Europa" AND land.Flaeche > "300000"
ORDER BY Flaeche

/*4.:*/
SELECT ort.Name, ort.Einwohner, land.Name
FROM ort, land
where ort.LNR = land.LNR AND ort.Einwohner > 10000000
ORDER BY ort.Einwohner DESC

/*5.:*/
SELECT ort.Name, ort.Einwohner, kontinent.Name
FROM ort, land, kontinent
WHERE ort.LNR = land.LNR AND land.KNR = kontinent.KNR AND kontinent.Name = "Europa" AND ort.Einwohner > 1000000

/*6.:*/
SELECT ort.Name, ort.Einwohner, land.Name, land.Einwohner
FROM ort, land
WHERE ort.LNR = land.LNR AND ort.Einwohner > 1000000 AND land.Einwohner < 10
ORDER BY ort.Einwohner DESC