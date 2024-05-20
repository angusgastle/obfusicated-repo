# T-SQL (Transact-SQL) Script to display "Hello World"

-- Creating a temporary table to hold the message
CREATE TABLE #HelloWorldTable (
    Message NVARCHAR(50)
);

-- Inserting the "Hello World" message into the temporary table
INSERT INTO #HelloWorldTable (Message)
VALUES ('Hello World');

-- Declaring a cursor to read from the temporary table
DECLARE @MessageCursor CURSOR;
DECLARE @Message NVARCHAR(50);

-- Initializing the cursor with the data from our temporary table
SET @MessageCursor = CURSOR FOR
    SELECT Message
    FROM #HelloWorldTable;

-- Opening the cursor
OPEN @MessageCursor;

-- Fetching the first and only row from the cursor
FETCH NEXT FROM @MessageCursor INTO @Message;

-- Checking if the fetch operation got any rows
WHILE @@FETCH_STATUS = 0
BEGIN
    -- Displaying the "Hello World" message
    PRINT @Message;

    -- Fetching the next row (though there won't be one)
    FETCH NEXT FROM @MessageCursor INTO @Message;
END;

-- Closing the cursor
CLOSE @MessageCursor;

-- Deallocating the cursor to free up resources
DEALLOCATE @MessageCursor;

-- Dropping the temporary table to clean up the database
DROP TABLE #HelloWorldTable;