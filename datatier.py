##################################################################
# Datatier
# This module provides utility functions for interacting with a database.
# It includes functions to select a single row, select multiple rows,
# and perform actions such as insert, update, or delete.
##################################################################


##################################################################
#
# select_one_row:
#
# Given a database connection and a SQL Select query,
# executes this query against the database and returns
# the first row retrieved by the query (or the empty
# tuple () if no data was retrieved). The query can
# be parameterized, in which case pass the values as
# a list via parameters; this parameter is optional.
#
# Returns: first row retrieved by the given query, or
#          () if no data was retrieved. If an error
#          occurs, a msg is output and None is returned.
#

def select_one_row(dbConn, sql, parameters = None):

    if(parameters == None):
        parameters = []
    
    # create cursor to database
    dbCursor = dbConn.cursor()

    try:
        dbCursor.execute(sql,parameters)
        rows = dbCursor.fetchall() # Get all rows

        # If no rows were retrieved, return an empty tuple, else return the first row
        if len(rows) == 0:  
            return ()
        else:
            return rows[0]  
    except Exception as err:
        print("select_one_row should have returned None, but instead returned:", err)
    finally:
        dbCursor.close()

    


##################################################################
#
# select_n_rows:
#
# Given a database connection and a SQL Select query,
# executes this query against the database and returns
# a list of rows retrieved by the query. If the query
# retrieves no data, the empty list [] is returned.
# The query can be parameterized, in which case pass 
# the values as a list via parameters; this parameter 
# is optional.
#
# Returns: a list of 0 or more rows retrieved by the 
#          given query; if an error occurs a msg is 
#          output and None is returned.
#
def select_n_rows(dbConn, sql, parameters = None):
    
    if(parameters == None):
        parameters = []
    
    # create cursor to databse
    dbCursor = dbConn.cursor()

    try:
        dbCursor.execute(sql, parameters)
        rows = dbCursor.fetchall()
        return rows
    except Exception as err:
        print("select_n_rows failed:", err)
        return None
    finally:
        dbCursor.close()


##################################################################
#
# perform_action: 
# 
# Given a database connection and a SQL action query,
# executes this query and returns the # of rows
# modified; a return value of 0 means no rows were
# updated. Action queries are typically "insert", 
# "update", "delete". The query can be parameterized,
# in which case pass the values as a list via 
# parameters; this parameter is optional.
#
# Returns: the # of rows modified by the query; if an 
#          error occurs a msg is output and -1 is 
#          returned. Note that a return value of 0 is
#          not considered an error --- it means the
#          query did not change the database (e.g. 
#          because the where condition was false?).
#
def perform_action(dbConn, sql, parameters = None):

    if(parameters == None):
        parameters = []

    # create cursor to databse
    dbCursor = dbConn.cursor()   

    # set default rows_modified to -1
    rows_modified = -1

    try:
        # start transaction
        dbCursor.execute(sql,parameters) 
        dbConn.commit()                # commit changes
        # get rows modified by query
        rows_modified = dbCursor.rowcount

    except Exception as err:
        print("perform_action failed:", err)

    finally:
        dbCursor.close()
        return rows_modified
    
