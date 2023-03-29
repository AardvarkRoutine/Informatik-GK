/*1.:*/
SELECT ort.Name, ort.Einwohner FROM ort, land
WHERE ort.Einwohner > 3000 AND ort.LNR = land.LNR AND land.Name = "Deutschland" AND LEFT(ort.Name, 1) = "K" AND RIGHT(ort.Name, 1) = "L"
ORDER BY ort.Name DESC

/*2.:*/
SELECT ort.Name, ort.Einwohner, land.Name
FROM ort
INNER JOIN land ON ort.LNR = land.LNR
WHERE ort.Einwohner >= 100000 AND land.Name IN ('Deutschland', 'Frankreich', 'England')
ORDER BY ort.Einwohner DESC

/*3.:*/
SELECT land.Name
FROM land
INNER JOIN kontinent ON land.KNR = kontinent.KNR
WHERE kontinent.Name IN ('Afrika', 'Europa') AND RIGHT(land.Name, 2) = 'en'

/*4.:*/


/*5.:*/
