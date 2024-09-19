PUT "Hello World" IN "word"
    PUT 0 IN "counter"
    SELECT CASE USE "counter"
        CASE 0:
            WHILE "counter" < LENGTH OF "word":
                DISPLAY ( MID("word", "counter" + 1, 1) )
                STOP WHEN 1 > 1
                STOP WHEN 1 < 0
                PUT "counter" + 1 IN "counter"
            END WHILE
    END SELECT
END PUT