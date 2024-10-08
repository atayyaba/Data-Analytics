/****** Script for SelectTopNRows command from SSMS  ******/
/*SELECT TOP (1000) [ID]
      ,[BibliographyID]
      ,[PersonID]
  FROM [DblpXml].[dbo].[PersonDetails]*/


  /*Select [DblpXml].[dbo].[PersonDetails].[BibliographyID], COUNT([DblpXml].[dbo].[PersonDetails].[PersonID]) from [DblpXml].[dbo].[PersonDetails]
  group by [DblpXml].[dbo].[PersonDetails].[BibliographyID];*/
 
  /*Select * from [DblpXml].[dbo].[PersonDetails];*/

 /*Select [DblpXml].[dbo].[JournalYearID].[ID],[DblpXml].[dbo].[JournalYearID].[year],
[DblpXml].[dbo].[Countyear].[count]
from [DblpXml].[dbo].[JournalYearID]
INNER JOIN [DblpXml].[dbo].[Countyear] ON [DblpXml].[dbo].[JournalYearID].[year]=[DblpXml].[dbo].[Countyear].[year]*/

/*INSERT INTO [DblpXml].[dbo].[Bibyear]
Select top(1000) [DblpXml].[dbo].[Bibliography].[ID],[DblpXml].[dbo].[Bibliography].[Year] from 
[DblpXml].[dbo].[Bibliography] 
INNER JOIN [DblpXml].[dbo].[PersonDetails] on [DblpXml].[dbo].[Bibliography].[ID]=[DblpXml].[dbo].[PersonDetails].[BibliographyID];
*/
/*Insert into [DblpXml].[dbo].[bibcount] 
Select ID,count(*) from [DblpXml].[dbo].[Bibyear] group by ID;*/

/*Insert into [DblpXml].[dbo].[Bibfinal] 
Select DISTINCT [DblpXml].[dbo].[bibyear].[ID],[DblpXml].[dbo].[bibyear].[year],
[DblpXml].[dbo].[bibcount].[count]
from [DblpXml].[dbo].[bibyear]
INNER JOIN [DblpXml].[dbo].[bibcount] ON [DblpXml].[dbo].[bibyear].[ID]=[DblpXml].[dbo].[bibcount].[ID];*/
SELECT TOP (1000) [ID] ,[year],[count] FROM [DblpXml].[dbo].[JournalFinal];