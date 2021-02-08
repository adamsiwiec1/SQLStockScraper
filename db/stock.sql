create database stock_db

use stock_db

select @@SERVERNAME


-- Stock table creation script
USE [stock_db]
GO
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[Stock](
	[SID] [int] IDENTITY(100,1) NOT NULL,
	[Ticker] [nvarchar](5) NOT NULL,
	[Exchange] [nvarchar](15) NULL,
	[Name] [nvarchar](100) NOT NULL,
	[DateTimePulled_EST] [nvarchar](100) NOT NULL,
	[Price] [decimal](18, 3) NOT NULL,
	[Ask] [decimal](18, 3) NULL,
	[Bid] [decimal](18, 3) NULL,
	[DayLow] [decimal](18, 3) NULL,
	[DayHigh] [decimal](18, 3) NULL,
	[Volume] [decimal](38, 0) NULL,
	[MarketOpen] [decimal](18, 3) NULL,
	[MarketClose] [decimal](18, 3) NULL,
	[FiftyTwoWeekLow] [decimal](18, 3) NULL,
	[FiftyTwoWeekHigh] [decimal](18, 3) NULL,
	[FiftyDayAverage] [decimal](18, 3) NULL,
	[FiftyTwoWeekChange] [decimal](18, 2) NULL,
	[TwoHundredDayAverage] [decimal](18, 3) NULL,
	[AverageVolume] [decimal](38, 0) NULL,
	[TenDayAverageVolume] [decimal](38, 0) NULL,
	[Country] [nvarchar](4000) NULL,
	[Sector] [nvarchar](4000) NULL,
	[Industry] [nvarchar](4000) NULL,
	[LastDividendValue] [decimal](18, 2) NULL,
	[PayoutRatio] [decimal](38, 3) NULL,
	[ProfitMargins] [decimal](18, 3) NULL,
	[FloatShares] [decimal](38, 0) NULL,
	[ShortShares] [decimal](38, 0) NULL,
	[ShortSharesMonthAgo] [decimal](38, 0) NULL,
	[Employees] [decimal](38, 0) NULL,
	[BookValue] [decimal](18, 4) NULL,
	[EarningsQuarterlyGrowth] [decimal](18, 2) NULL,
	[NetIncomeToCommon] [decimal](18, 2) NULL,
	[SharesOutstanding] [decimal](38, 0) NULL,
	[ShortRatio] [decimal](18, 3) NULL,
	[Market] [nvarchar](4000) NULL,
	[LongBusinessSummary] [nvarchar](4000) NULL,
PRIMARY KEY CLUSTERED 
(
	[SID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO

-- Creation script for each exchage table
USE [stock_db]
GO
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[ASE](
	[ASE_ID] [int] NULL,
	[DateTimePulled_EST] [datetime] NULL,
	[Ticker] [nvarchar](5) NULL,
	[Price] [decimal](18, 3) NULL,
	[Ask] [decimal](18, 3) NULL,
	[Bid] [decimal](18, 3) NULL,
	[DayLow] [decimal](18, 3) NULL,
	[DayHigh] [decimal](18, 3) NULL,
	[MarketOpen] [decimal](18, 3) NULL,
	[MarketClose] [decimal](18, 3) NULL,
	[Volume] [decimal](18, 3) NULL
) ON [PRIMARY]
GO

-- User Defined Functions (UDFs)
create function CalculateShorts()
returns @ShortTable table (Ticker nvarchar(5), Name nvarchar(1000), ShortPercent decimal(7,4))
as
BEGIN
	insert into @ShortTable
	select Ticker, Name, (ShortShares/FloatShares)
	from Stock
	return
END

alter function CalculateShortsDetailed()
returns @TempTable table (Ticker nvarchar(5), Name nvarchar(1000), ShortPercent decimal(7,4), ShortPercentMonthAgo decimal(18,4), ShortShares decimal(38,0), FloatShares numeric(38,0), Exchange nvarchar(30), FiftyDayAvg numeric(38,4), TwoHunnaDayAvg numeric(38,4))
as
BEGIN
	insert into @TempTable
	select Ticker, Name, (ShortShares/FloatShares), (ShortSharesMonthAgo/FloatShares), ShortShares, FloatShares, Exchange , FiftyDayAverage, TwoHundredDayAverage 
	from Stock
	return
END


-- Useful/common queries for this database

-- Select all from Stock table
select * from Stock

-- Count the amount of stocks in the table
select count(SID) from Stock

-- Get a business summary of each company.
select Name, Ticker, LongBusinessSummary from Stock

-- Get a list of stocks ordered by highest income to common individuals 
select Ticker, NetIncomeToCommon from Stock order by NetIncomeToCommon desc

-- Use calculate shorts UDF and order from highest to lowest
select * from CalculateShorts() order by ShortPercent desc

-- Use DETAILED calculate shorts UDF and order from highest to lowest
select * from CalculateShortsDetailed() order by ShortPercentMonthAgo desc

-- List all stock exchanges that appear in our data
select Exchange from Stock group by Exchange

-- Count of all stocks in each exchange
select Exchange, count(Exchange) as NumberOfStocks from Stock group by Exchange

-- Count of stocks in an exchange
select count(Ticker) as Result from Stock where Exchange='nms'

-- List all stocks in a particular exchange
select Ticker from Stock where Exchange='nms'

select * from Stock
