
/*SELECT 
    ID,YEAR,
FROM
    [DblpXml].[dbo].[Journal]
INNER JOIN
    [DblpXml].[dbo].[JournalDetails] 
INNER JOIN
    [DblpXml].[dbo].[Bibliography] 
ORDER BY 
    [Journal].ID, 
/*    JournalID;*/
CREATE VIEW result AS (
Select top 1000 bib.ID,bib.Year from 
[DblpXml].[dbo].[Journal] as jr 
INNER JOIN [DblpXml].[dbo].[JournalDetails] as jd
on  jr.ID=jd.JournalID
INNER JOIN [DblpXml].[dbo].[Bibliography] as bib on jd.BibliographyID=bib.ID);*/
/*Select COUNT(*) from result WHERE Year='2015';*/
/*SELECT 
    Year, 
    COUNT(*)
FROM
    result
GROUP BY Year;*/

/*SELECT top 1000 bib.ID,bib.Year from 
	[DblpXml].[dbo].[Journal] as jr 
	INNER JOIN [DblpXml].[dbo].[JournalDetails] as jd
	on  jr.ID=jd.JournalID
	INNER JOIN [DblpXml].[dbo].[Bibliography] as bib on jd.BibliographyID=bib.ID);*/


/*SELECT Year, COUNT(*)
FROM
    result
GROUP BY Year*/

/*CREATE VIEW IY AS 
(SELECT TOP 1000 bib.ID,bib.Year FROM 
[DblpXml].[dbo].[Journal] as jr 
INNER JOIN [DblpXml].[dbo].[JournalDetails] as jd
on  jr.ID=jd.JournalID
INNER JOIN [DblpXml].[dbo].[Bibliography] as bib on jd.BibliographyID=bib.ID);*/

/*SELECT Year, COUNT(*)
FROM IY
ORDER BY ID; */
/*Select * from IY; */
/*SELECT year, COUNT(*)
FROM IY
GROUP BY year;*/
/*SELECT * INTO CT
FROM IY;*/

/*INSERT INTO[DblpXml].[dbo].[JournalCount]*/
/*
INSERT INTO [DblpXml].[dbo].[Countyear]
SELECT year, COUNT(*)
FROM [DblpXml].[dbo].[JournalYearID]
GROUP BY year;*/

/*create view new as(SELECT year, COUNT(*)
FROM IY
GROUP BY year);*/

/*SELECT IY.Year, CT.*/

/*INSERT INTO [DblpXml].[dbo].[JournalFinal]
Select [DblpXml].[dbo].[JournalYearID].[ID],[DblpXml].[dbo].[JournalYearID].[year],
[DblpXml].[dbo].[Countyear].[count]
from [DblpXml].[dbo].[JournalYearID]
INNER JOIN [DblpXml].[dbo].[Countyear] ON [DblpXml].[dbo].[JournalYearID].[year]=[DblpXml].[dbo].[Countyear].[year];
*/
/*SELECT year,COUNT(*)
FROM [DblpXml].[dbo].[JournalFinal]
GROUP BY year;*/
/*SELECT top (1000) [DblpXml].[dbo].[JournalFinal].[year],[DblpXml].[dbo].[JournalFinal].[ID],
[DblpXml].[dbo].[JournalFinal].[count] FROM [DblpXml].[dbo].[JournalFinal] Where year>=2000;*/
/*SELECT TOP (1000) [ID] ,[year],[count] FROM [DblpXml].[dbo].[JournalFinal] Where year<=2000;*/

