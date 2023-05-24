#include <stdio.h>
#include <sqlite3.h>
#include <stddef.h>

int main()
{
    sqlInit;
    int i, sum = 0;
    INSERT INTO comments (comment) VALUES ("Hello World");
    SELECT comment FROM comments INTO wlasnyCallback;
    UPDATE comments SET comment = "New comment" WHERE comment = "Hello World";
    SELECT comment FROM comments INTO wlasnyCallback;
    return 0;
}