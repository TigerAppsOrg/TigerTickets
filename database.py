#-----------------------------------------------------------------------
# database.py
#-----------------------------------------------------------------------

import sys
from psycopg2 import connect, Error as dbError
import os
import random
import string

class Database:

    def __init__(self):
        self._connection = None


    def connect(self):
            #        DATABASE_NAME = "PTE"
            #        if not path.isfile(DATABASE_NAME):
            #            raise Exception("reg: database PTE not found")
        DATABASE_URL = os.environ['DATABASE_URL']
        self._connection = connect(DATABASE_URL, sslmode='require')
        # self._connection = connect(host = "localhost", database = "PTE", user = "postgres", password = "postgres")


    def disconnect(self):
        self._connection.close()

        # helper function that appends a backslash right before every instance
        # of a special character


    def format(self, s):
        i = 0
        while i < len(s):
            if s[i] == "'":
                s = s[0:i] + "'" + s[i:]
                i = i+1
            i = i + 1
        return s
#-----------------------------------------------------------------------
    def createUser(self, netid):
        try:
            cursor = self._connection.cursor()

            s = "SELECT * FROM users  WHERE netid = '%s';" % (self.format(netid))
            cursor.execute(s)
            result = cursor.fetchall()
            if len(result)== 0:
                s = "INSERT INTO users(netid) VALUES ('%s');" % (self.format(netid))
            cursor.execute(s)
            cursor.close()
            return True
        except dbError as e:
            print("PTE: " + str(e), file = sys.stderr)
            return False
            sys.exit(1)

        except Exception as e:
            print(str(e), file = sys.stderr)
            return False
            sys.exit(1)

#-----------------------------------------------------------------------

    def escapeString(self, s):
        esc = "\\"
        i = 0
        for c in range(len(s)):
            if s[i] == "%" or s[i] == "_":
                s = s[0:i] + esc + s[i:len(s)]
                i = i + 1
            i = i + 1
        return s
#-----------------------------------------------------------------------
# helper method
    def formatEvent(self, event):
        if event == 'bac':
            event = 'BAC'
        elif event == 'bodyhype':
            event = 'BodyHype'
        elif event is None or event =='':
            event = "All"
        elif event == "disiac":
            event = "Disiac"
        elif event == "expressions":
            event = "Expressions"
        elif event == "kokopops":
            event = "KoKo Pops"
        elif event == "naacho":
            event = "Naacho"
        elif event == "raqs":
            event = "Raqs"
        elif event == "six14":
            event = "Six14"
        elif event == "sympoh":
            event = "Sympoh"
        elif event == "triple8":
            event = "Triple 8"
        elif event == "butler":
            event = "Butler Broadway"
        elif event == "forbes":
            event = "Forbes Broadway"
        elif event == "mathey":
            event = "Mathey Broadway"
        elif event == "rocky":
            event = "Rocky Broadway"
        elif event == "whitman":
            event = "Whitman Broadway"
        elif event == "wilson":
            event = "Wilson Broadway"
        elif event == "highsteppers":
            event = "Highsteppers"
        elif event == "masflow":
            event = "Mas Flow"
        elif event == "ppe":
            event = "Princeton Pianists Ensemble"
        elif event == "bhangra":
            event = "Princeton Bhangra"
        elif event == "ballet":
            event = "Princeton University Ballet"
        elif event == "tapcats":
            event = "TapCats"
        elif event == "triangle":
            event = "Triangle"
        elif event == "puo":
            event = "Princeton University Orchestra"
        elif event == "footnotes":
            event = "Footnotes"
        elif event == "katzenjammers":
            event = "Katzenjammers"
        elif event == "kindredspirit":
            event = "Kindred Spirit"
        elif event == "lavie":
            event = "La Vie En Cello"
        elif event == "nassoons":
            event = "Nassoons"
        elif event == "oldnassoul":
            event = "Old NasSoul"
        elif event == "opus21":
            event = "Opus 21"
        elif event == "poco":
            event = "Princeton Opera Company"
        elif event == "r20":
            event = "Roaring 20"
        elif event == "sherekhan":
            event = "Shere Khan"
        elif event == "sinfonia":
            event = "Sinfonia"
        elif event == "tigerlilies":
            event = "Tigerlilies"
        elif event == "tigertones":
            event = "Tigertones"
        elif event == "tigressions":
            event = "Tigressions"
        elif event == "wildcats":
            event = "Wildcats"
        elif event == "fuzzydice":
            event = "Fuzzy Dice"
        elif event == "jugglingclub":
            event = "Juggling Club"
        elif event == "lobsterclub":
            event = "Lobster Club"
        elif event == "quipfire":
            event = "Quipfire!"
        elif event == "other":
            event = "Other"
        else:
            event = event
        return event
        
#-----------------------------------------------------------------------

    def fulleventname(self, event):
        if event == 'bac':
            event = 'Black Arts Company'
        elif event == 'bodyhype':
            event = 'BodyHype'
        elif event == "disiac":
            event = "Disiac"
        elif event == "expressions":
            event = "Expressions"
        elif event == "kokopops":
            event = "KoKo Pops"
        elif event == "naacho":
            event = "Naacho"
        elif event == "raqs":
            event = "Raqs"
        elif event == "six14":
            event = "Six14"
        elif event == "sympoh":
            event = "Sympoh"
        elif event == "triple8":
            event = "Triple 8"
        elif event == "butler":
            event = "Butler Broadway"
        elif event == "forbes":
            event = "Forbes Broadway"
        elif event == "mathey":
            event = "Mathey Broadway"
        elif event == "rocky":
            event = "Rocky Broadway"
        elif event == "whitman":
            event = "Whitman Broadway"
        elif event == "wilson":
            event = "Wilson Broadway"
        elif event == "highsteppers":
            event = "Highsteppers"
        elif event == "masflow":
            event = "Mas Flow"
        elif event == "ppe":
            event = "Princeton Pianists Ensemble"
        elif event == "bhangra":
            event = "Princeton Bhangra"
        elif event == "ballet":
            event = "Princeton University Ballet"
        elif event == "tapcats":
            event = "TapCats"
        elif event == "triangle":
            event = "Triangle"
        elif event == "puo":
            event = "Princeton University Orchestra"
        elif event == "footnotes":
            event = "Footnotes"
        elif event == "katzenjammers":
            event = "Katzenjammers"
        elif event == "kindredspirit":
            event = "Kindred Spirit"
        elif event == "lavie":
            event = "La Vie En Cello"
        elif event == "nassoons":
            event = "Nassoons"
        elif event == "oldnassoul":
            event = "Old NasSoul"
        elif event == "opus21":
            event = "Opus 21"
        elif event == "poco":
            event = "Princeton Opera Company"
        elif event == "r20":
            event = "Roaring 20"
        elif event == "sherekhan":
            event = "Shere Khan"
        elif event == "sinfonia":
            event = "Sinfonia"
        elif event == "tigerlilies":
            event = "Tigerlilies"
        elif event == "tigertones":
            event = "Tigertones"
        elif event == "tigressions":
            event = "Tigressions"
        elif event == "wildcats":
            event = "Wildcats"
        elif event == "fuzzydice":
            event = "Fuzzy Dice"
        elif event == "jugglingclub":
            event = "Juggling Club"
        elif event == "lobsterclub":
            event = "Lobster Club"
        elif event == "quipfire":
            event = "Quipfire!"
        elif event == "other":
            event = "Other"
        else:
            event = event
        return event


#-----------------------------------------------------------------------
    def ampm(self, time):
        hour = int(str(time)[11:13])
        if hour >= 12:
            if hour > 12:
                hour = hour - 12
            return str(str(time)[0:10] + str(hour) + str(time)[13:] + " " + "PM")
        else:
            return str(str(time)[0:10] + str(hour) + str(time)[13:] + " " + "AM")
#-----------------------------------------------------------------------
    def getTicketByID(self, ticketid):
        try:
            cursor = self._connection.cursor()

            s = "SELECT * FROM tickets WHERE tickets.ticketid = %s;" % (ticketid)
            cursor.execute(s)
            ticket = cursor.fetchall()
            if len(ticket) == 0:
                return [False, False]
            else:
                ticket = ticket[0]
                listTicket = list(ticket)
                listTicket[1] = str(listTicket[1])[0:16]
                listTicket[2] = self.formatEvent(listTicket[2])
                return [True, listTicket]

        except dbError as e:
            print("PTE: " + str(e), file = sys.stderr)
            return [False, False]
            sys.exit(1)

        except Exception as e:
            print(str(e), file = sys.stderr)
            return [False, False]
            sys.exit(1)

#-----------------------------------------------------------------------
    # this is the function for recurring events (Dance groups and broadway)
    def getTickets(self, event, sort):
        try:
            cursor = self._connection.cursor()

            # if no argument restriction, match all
            if event is None or event == '':
                s = "SELECT * FROM tickets WHERE tickets.status = 'available' AND tickets.time >= 'now'"
                if sort is None or sort == '':
                    s= s + " ORDER BY tickets.ticketid DESC;"
                elif sort == "priceasc":
                    s= s + " ORDER BY tickets.price ASC, tickets.ticketid DESC;"
                elif sort == "pricedesc":
                    s= s + " ORDER BY tickets.price DESC, tickets.ticketid DESC"
                elif sort == "dateasc":
                    s= s + " ORDER BY tickets.time ASC, tickets.ticketid DESC;"
                elif sort == "datedesc":
                    s= s + " ORDER BY tickets.time DESC, tickets.ticketid DESC;"
                elif sort == "sellerasc":
                    s= s + " ORDER BY tickets.sellerid ASC, tickets.ticketid DESC;"
                elif sort == "sellerdesc":
                    s= s + " ORDER BY tickets.sellerid DESC, tickets.ticketid DESC;"
                elif sort == "eventasc":
                    s= s + " ORDER BY tickets.fullname ASC, tickets.ticketid DESC;"
                elif sort == "eventdesc":
                    s= s + " ORDER BY tickets.fullname DESC, tickets.ticketid DESC;"
                elif sort == "typeasc":
                    s= s + " ORDER BY tickets.type ASC, tickets.ticketid DESC;"
                elif sort == "typedesc":
                    s= s + " ORDER BY tickets.type DESC, tickets.ticketid DESC;"
                cursor.execute(s)
                results = cursor.fetchall()
            else:
                # query all relevant data using arguments
                event = self.escapeString(event.lower())
                s = "SELECT * FROM tickets WHERE tickets.event = '%s' AND tickets.status = 'available' AND tickets.time >= 'now'"  % (self.format(event))
                if sort is None or sort == '':
                    s= s + " ORDER BY tickets.ticketid DESC;"
                elif sort == "priceasc":
                    s= s + " ORDER BY tickets.price ASC, tickets.ticketid DESC;"
                elif sort == "pricedesc":
                    s= s + " ORDER BY tickets.price DESC, tickets.ticketid DESC"
                elif sort == "dateasc":
                    s= s + " ORDER BY tickets.time ASC, tickets.ticketid DESC;"
                elif sort == "datedesc":
                    s= s + " ORDER BY tickets.time DESC, tickets.ticketid DESC;"
                elif sort == "sellerasc":
                    s= s + " ORDER BY tickets.sellerid ASC, tickets.ticketid DESC;"
                elif sort == "sellerdesc":
                    s= s + " ORDER BY tickets.sellerid DESC, tickets.ticketid DESC;"
                elif sort == "eventasc":
                    s= s + " ORDER BY tickets.fullname ASC, tickets.ticketid DESC;"
                elif sort == "eventdesc":
                    s= s + " ORDER BY tickets.fullname DESC, tickets.ticketid DESC;"
                elif sort == "typeasc":
                    s= s + " ORDER BY tickets.type ASC, tickets.ticketid DESC;"
                elif sort == "typedesc":
                    s= s + " ORDER BY tickets.type DESC, tickets.ticketid DESC;"
                cursor.execute(s)
                results = cursor.fetchall()
            cursor.close()
            resultList = []
            for ticket in results:
                listTicket = list(ticket)
                listTicket[1] = self.ampm(str(listTicket[1])[0:16]) if not listTicket[1] is None else ''
                listTicket[2] = self.formatEvent(listTicket[2]) if not listTicket[2] is None else ''
                resultList.append(listTicket)
            return [True, resultList]

        except dbError as e:
            print("PTE: " + str(e), file = sys.stderr)
            return[False, False]
            sys.exit(1)

        except Exception as e:
            print(str(e), file = sys.stderr)
            return[False, False]
            sys.exit(1)
            


#-----------------------------------------------------------------------
# this is the function for recurring events (Dance groups and broadway)
    def getTicketsSearch(self, event, sort):
        try:
            cursor = self._connection.cursor()

            # if no argument restriction, match all
            if event is None or event == '':
                s = "SELECT * FROM tickets WHERE tickets.status = 'available' AND tickets.time >= 'now'"
                if sort is None or sort == '':
                    s= s + " ORDER BY tickets.ticketid DESC;"
                elif sort == "priceasc":
                    s= s + " ORDER BY tickets.price ASC, tickets.ticketid DESC;"
                elif sort == "pricedesc":
                    s= s + " ORDER BY tickets.price DESC, tickets.ticketid DESC"
                elif sort == "dateasc":
                    s= s + " ORDER BY tickets.time ASC, tickets.ticketid DESC;"
                elif sort == "datedesc":
                    s= s + " ORDER BY tickets.time DESC, tickets.ticketid DESC;"
                elif sort == "sellerasc":
                    s= s + " ORDER BY tickets.sellerid ASC, tickets.ticketid DESC;"
                elif sort == "sellerdesc":
                    s= s + " ORDER BY tickets.sellerid DESC, tickets.ticketid DESC;"
                elif sort == "eventasc":
                    s= s + " ORDER BY tickets.fullname ASC, tickets.ticketid DESC;"
                elif sort == "eventdesc":
                    s= s + " ORDER BY tickets.fullname DESC, tickets.ticketid DESC;"
                elif sort == "typeasc":
                    s= s + " ORDER BY tickets.type ASC, tickets.ticketid DESC;"
                elif sort == "typedesc":
                    s= s + " ORDER BY tickets.type DESC, tickets.ticketid DESC;"
                cursor.execute(s)
                results = cursor.fetchall()
            else:
                # query all relevant data using arguments
                event = self.escapeString(event.lower())
                event = "%" + event + "%"
                s = "SELECT * FROM tickets WHERE (tickets.event LIKE '%s' OR tickets.fullname LIKE '%s') AND tickets.status = 'available' AND tickets.time >= 'now'"  % (self.format(event), self.format(event))
                if sort is None or sort == '':
                    s= s + " ORDER BY tickets.ticketid DESC;"
                elif sort == "priceasc":
                    s= s + " ORDER BY tickets.price ASC, tickets.ticketid DESC;"
                elif sort == "pricedesc":
                    s= s + " ORDER BY tickets.price DESC, tickets.ticketid DESC"
                elif sort == "dateasc":
                    s= s + " ORDER BY tickets.time ASC, tickets.ticketid DESC;"
                elif sort == "datedesc":
                    s= s + " ORDER BY tickets.time DESC, tickets.ticketid DESC;"
                elif sort == "sellerasc":
                    s= s + " ORDER BY tickets.sellerid ASC, tickets.ticketid DESC;"
                elif sort == "sellerdesc":
                    s= s + " ORDER BY tickets.sellerid DESC, tickets.ticketid DESC;"
                elif sort == "eventasc":
                    s= s + " ORDER BY tickets.fullname ASC, tickets.ticketid DESC;"
                elif sort == "eventdesc":
                    s= s + " ORDER BY tickets.fullname DESC, tickets.ticketid DESC;"
                elif sort == "typeasc":
                    s= s + " ORDER BY tickets.type ASC, tickets.ticketid DESC;"
                elif sort == "typedesc":
                    s= s + " ORDER BY tickets.type DESC, tickets.ticketid DESC;"
                cursor.execute(s)
                results = cursor.fetchall()
            cursor.close()
            resultList = []
            for ticket in results:
                listTicket = list(ticket)
                listTicket[1] = self.ampm(str(listTicket[1])[0:16]) if not listTicket[1] is None else ''
                listTicket[2] = self.formatEvent(listTicket[2]) if not listTicket[2] is None else ''
                resultList.append(listTicket)
            return [True, resultList]

        except dbError as e:
            print("PTE: " + str(e), file = sys.stderr)
            return[False, False]
            sys.exit(1)

        except Exception as e:
            print(str(e), file = sys.stderr)
            return[False, False]
            sys.exit(1)
            


#-----------------------------------------------------------------------
    # this is the function for other events
    def getTicketsOther(self, sort):
        try:
            cursor = self._connection.cursor()

            # if no argument restriction, match all
            # query all relevant data using arguments
            s = "SELECT * FROM tickets WHERE tickets.other = 'yes' AND tickets.status = 'available' AND tickets.time >= 'now'"
            if sort is None or sort == '':
                s= s + " ORDER BY tickets.ticketid DESC;"
            elif sort == "priceasc":
                s= s + " ORDER BY tickets.price ASC, tickets.ticketid DESC;"
            elif sort == "pricedesc":
                s= s + " ORDER BY tickets.price DESC, tickets.ticketid DESC"
            elif sort == "dateasc":
                s= s + " ORDER BY tickets.time ASC, tickets.ticketid DESC;"
            elif sort == "datedesc":
                s= s + " ORDER BY tickets.time DESC, tickets.ticketid DESC;"
            elif sort == "sellerasc":
                s= s + " ORDER BY tickets.sellerid ASC, tickets.ticketid DESC;"
            elif sort == "sellerdesc":
                s= s + " ORDER BY tickets.sellerid DESC, tickets.ticketid DESC;"
            elif sort == "eventasc":
                s= s + " ORDER BY tickets.fullname ASC, tickets.ticketid DESC;"
            elif sort == "eventdesc":
                s= s + " ORDER BY tickets.fullname DESC, tickets.ticketid DESC;"
            elif sort == "typeasc":
                s= s + " ORDER BY tickets.type ASC, tickets.ticketid DESC;"
            elif sort == "typedesc":
                s= s + " ORDER BY tickets.type DESC, tickets.ticketid DESC;"
            cursor.execute(s)
            results = cursor.fetchall()

            cursor.close()
            resultList = []
            for ticket in results:
                listTicket = list(ticket)
                listTicket[1] = self.ampm(str(listTicket[1])[0:16]) if not listTicket[1] is None else ''
                listTicket[2] = self.formatEvent(listTicket[2]) if not listTicket[2] is None else ''
                resultList.append(listTicket)
            return [True, resultList]

        except dbError as e:
            print("PTE: " + str(e), file = sys.stderr)
            return[False, False]
            sys.exit(1)
        except Exception as e:
            print(str(e), file = sys.stderr)
            return[False, False]
            sys.exit(1)
#-----------------------------------------------------------------------

    def addTicket(self, time, event, sellerid, price, type, description, status, other):
        try:
            cursor = self._connection.cursor()

            # note that time has special format TIMESTAMP '1999-01-08 04:05:06'
            if time is None:
                raise ValueError("user cannot give null time")
            if event is None:
                raise ValueError("user cannot give null event")
            if sellerid is None:
                raise ValueError("user cannot give null sellerid")
            if price is None:
                price = 0
            if type is None:
                raise ValueError("user cannot give null type")
            if description is None:
                description = ""
            if status is None:
                raise ValueError("user cannot give null ticket status")
        except dbError as e:
            print("PTE: " + str(e), file = sys.stderr)
            return False
            sys.exit(1)
        except Exception as e:
            print(str(e), file = sys.stderr)
            return False
            sys.exit(1)

        try:
            # insert new ticket
            fullname = self.fulleventname(event.lower()).lower()
            s = "INSERT INTO tickets(time, event, sellerid, price, type, description, status, other, timeadded, fullname) VALUES(TIMESTAMP '%s', '%s', '%s', %s, '%s', '%s', '%s', '%s', '%s', '%s');" % (time, self.format(event.lower()), self.format(sellerid), price, type, self.format(description), status, other, 'now', self.format(fullname))
            cursor.execute(s)
            self._connection.commit()
            cursor.close()
            return True
        except Exception as e:
            print(str(e))
            self._connection.rollback()
            cursor.close()
            return False

#-----------------------------------------------------------------------
    def removeTicket(self, ticketid):
        try:
            cursor = self._connection.cursor()

            # if no argument restriction, match all
            if ticketid is None:
                raise ValueError("ticket already removed")
            elif not isinstance(ticketid, str):
                raise ValueError("ticketid not a string")

            # query all relevant data using arguments
            s = "UPDATE tickets SET status = 'deleted' WHERE ticketid = %s;" % (self.format(str(ticketid)))
            cursor.execute(s)
            self._connection.commit()

            s = "select * from transactions where ticketid = %s;" % (self.format(str(ticketid)))
            cursor.execute(s)
            info = cursor.fetchall()
            if (len(info) == 1):
                s = "insert into canceledtransactions(sellerid, buyerid, ticketid, status, time) values ('%s', '%s', %s, '%s', 'now');" % (self.format(info[1]), self.format(info[2]),info[3], self.format(info[4]))
                cursor.execute(s)
                s = "delete from transactions where ticketid = %s;" % (str(ticketid))
                cursor.execute(s)

            self._connection.commit()
            cursor.close()
            return True
        except dbError as e:
            print("PTE: " + str(e), file = sys.stderr)
            return False
            sys.exit(1)
        except Exception as e:
            print(str(e), file = sys.stderr)
            return False
            sys.exit(1)
        except:
            self._connection.rollback()
            return False
            cursor.close()
    #-----------------------------------------------------------------------
    def removeNotif(self, notificationid):
        try:
            cursor = self._connection.cursor()

            # if no argument restriction, match all
            if notificationid is None:
                raise ValueError("notification already removed")

            # query all relevant data using arguments
            s = "UPDATE notify SET status = 'deleted' WHERE notificationid = %s;" % (self.format(str(notificationid)))
            cursor.execute(s)
            self._connection.commit()
            cursor.close()
            return True
        except dbError as e:
            print("PTE: " + str(e), file = sys.stderr)
            return False
            sys.exit(1)
        except Exception as e:
            print(str(e), file = sys.stderr)
            return False
            sys.exit(1)
        except:
            self._connection.rollback()
            return False
            cursor.close()
#-----------------------------------------------------------------------
    def removeTransaction(self, ticketid):
        try:
            cursor = self._connection.cursor()

            # if no argument restriction, match all
            if ticketid is None:
                raise ValueError("ticket already removed")
            elif not isinstance(ticketid, str):
                raise ValueError("ticketid not a string")
        except dbError as e:
            print("PTE: " + str(e), file = sys.stderr)
            sys.exit(1)
        except Exception as e:
            print(str(e), file = sys.stderr)
            sys.exit(1)

        try:
            # query all relevant data using arguments
            s = "DELETE FROM transactions  WHERE tickets.ticketid = %s;" % (ticketid)
            cursor.execute(s)
            self._connection.commit()
            cursor.close()
            return None
        except:
            self._connection.rollback()
            cursor.close()

#-----------------------------------------------------------------------
    def makeTransaction(self, sellerid, buyerid, ticketid):
        try:
            cursor = self._connection.cursor()

            # if no argument restriction, match all
            if sellerid is None:
                raise ValueError("user cannot give null sellerid")
            if buyerid is None:
                raise ValueError("user cannot give null buyerid")
            if ticketid is None:
                raise ValueError("user cannot give null ticketid")

            # check that sellerid matches the sellerid for that ticket
            s = "SELECT sellerid, status FROM tickets where ticketid = %s;" % (str(ticketid))
            cursor.execute(s)
            info = cursor.fetchone()
            seller = info[0]
            if not seller == sellerid:
                raise ValueError("sellerid entered does not match sellerid of ticket")

            # check that ticket is available
            stat = info[1]
            if not stat == 'available':
                raise ValueError("ticket not available")

            # query all relevant data using arguments
            s = "INSERT INTO transactions(sellerid, buyerid, ticketid, status, time) VALUES('%s', '%s', %s, '%s', '%s');" % (self.format(sellerid), self.format(buyerid), str(ticketid), 'pending', 'now')
            cursor.execute(s)
            s = "UPDATE tickets SET status = 'pending' WHERE ticketid = %s;" % (str(ticketid))
            cursor.execute(s)
            self._connection.commit()
            cursor.close()
            return True
        except dbError as e:
            print("PTE: " + str(e), file = sys.stderr)
            return False
            sys.exit(1)
        except Exception as e:
            print(str(e), file = sys.stderr)
            return False
            sys.exit(1)
        except:
            self._connection.rollback()
            return False
            cursor.close()
##-----------------------------------------------------------------------
    def completeTransaction(self, sellerid, buyerid, ticketid):
        try:
            cursor = self._connection.cursor()

            # if no argument restriction, match all
            if sellerid is None:
                raise ValueError("user cannot give null sellerid")
            if buyerid is None:
                raise ValueError("user cannot give null buyerid")
            if ticketid is None:
                raise ValueError("user cannot give null ticketid")

            # check that sellerid matches the sellerid for that ticket
            s = "SELECT sellerid, status FROM tickets where ticketid = %s;" % (str(ticketid))
            cursor.execute(s)
            info = cursor.fetchone()
            seller = info[0]
            if not seller == sellerid:
                raise ValueError("sellerid entered does not match sellerid of ticket")

            # check that ticket is pending
            stat = info[1]
            if not stat == 'pending':
                raise ValueError("ticket missing")

            # query all relevant data using arguments
            s = "UPDATE transactions SET status = 'complete' WHERE ticketid = %s AND status = 'pending';" % (str(ticketid))
            cursor.execute(s)

            s = "UPDATE tickets SET status = 'confirmed' WHERE ticketid = %s AND status = 'pending';" % (str(ticketid))
            cursor.execute(s)
            self._connection.commit()
            cursor.close()
            return True
        except dbError as e:
            print("PTE: " + str(e), file = sys.stderr)
            return False
            sys.exit(1)
        except Exception as e:
            print(str(e), file = sys.stderr)
            return False
            sys.exit(1)
        except:
            self._connection.rollback()
            cursor.close()
            return False
#-----------------------------------------------------------------------

    def rejectTransaction(self, sellerid, ticketid):
        try:
            cursor = self._connection.cursor()

            # if no argument restriction, match all
            if sellerid is None:
                raise ValueError("user cannot give null sellerid")
            if ticketid is None:
                raise ValueError("user cannot give null ticketid")

            # check that sellerid matches the sellerid for that ticket
            s = "SELECT sellerid, status FROM tickets where ticketid = %s;" % (str(ticketid))
            cursor.execute(s)
            info = cursor.fetchone()
            seller = info[0]
            if not seller == sellerid:
                raise ValueError("sellerid entered does not match sellerid of ticket")

            # check that ticket is pending
            stat = info[1]
            if not stat == 'pending':
                raise ValueError("ticket missing")

            # query all relevant data using arguments
            s = "select * from transactions where ticketid = %s;" % (str(ticketid))
            cursor.execute(s)
            info = cursor.fetchone()
            if info[4] == 'pending':
                s = "insert into canceledtransactions(transactionid, sellerid, buyerid, ticketid, status, time) values (%s, '%s', '%s', %s, 'canceled', 'now');" % (info[0], self.format(info[1]), self.format(info[2]), info[3])
                cursor.execute(s)
                s = "delete from transactions where ticketid = %s;" % (str(ticketid))
                cursor.execute(s)
                s = "UPDATE tickets SET status = 'available' WHERE ticketid = %s;" % (str(ticketid))
                cursor.execute(s)
            self._connection.commit()
            cursor.close()
            return[True, info[2], info[1]]

        except dbError as e:
            print("PTE: " + str(e), file = sys.stderr)
            return [False, False]
            sys.exit(1)
        except Exception as e:
            print(str(e), file = sys.stderr)
            return [False, False]
            sys.exit(1)
        except:
            self._connection.rollback()
            return [False, False]
            cursor.close()

#        self.removeTransaction(ticketid)


#-----------------------------------------------------------------------
    def getUserTicket(self, user):
        try:
            cursor = self._connection.cursor()

            # if no argument restriction, match all
            if user is None:
                s = "SELECT * FROM tickets;"
                cursor.execute(s)
                results = cursor.fetchall()
            else:
                # query all relevant data using arguments
                s = "SELECT * FROM tickets WHERE tickets.sellerid = '%s' ORDER BY tickets.ticketid DESC;" % (self.format(user))

                cursor.execute(s)
                results = cursor.fetchall()

            cursor.close()
            resultList = []
            for ticket in results:
                listTicket = list(ticket)
                listTicket[1] = self.ampm(str(listTicket[1])[0:16]) if not listTicket[1] is None else ''
                listTicket[2] = self.formatEvent(listTicket[2]) if not listTicket[2] is None else ''
                resultList.append(listTicket)
            return [True, resultList]

        except dbError as e:
            print("PTE: " + str(e), file = sys.stderr)
            return[False, False]
            sys.exit(1)

        except Exception as e:
            print(str(e), file = sys.stderr)
            return[False, False]
            sys.exit(1)
#-----------------------------------------------------------------------

    def getUserTicketsBuy(self, user):
        try:
            cursor = self._connection.cursor()

            # if no argument restriction, match all
            if user is None:
                s = "create table temp as select * from transactions union select * from canceledtransactions order by transactionid DESC;"
                cursor.execute(s)
                s = "select temp.transactionid, temp.sellerid, temp.ticketid, temp.status, tickets.time, tickets.event, tickets.price, tickets.type, tickets.description, tickets.status from temp left join tickets on temp.ticketid = tickets.ticketid;"
                cursor.execute(s)
                results = cursor.fetchall()
                s = "drop table temp;"
                cursor.execute(s)
                self._connection.commit()
                cursor.close()
            else:
                # query all relevant data using arguments
                s = "create table temp as select * from transactions where transactions.buyerid = '%s' union select * from canceledtransactions where canceledtransactions.buyerid = '%s' order by transactionid DESC;" % (self.format(user), self.format(user))
                cursor.execute(s)
                s = "select temp.transactionid, temp.sellerid, temp.ticketid, temp.status, tickets.time, tickets.event, tickets.price, tickets.type, tickets.description, tickets.status from temp left join tickets on temp.ticketid = tickets.ticketid;"
                cursor.execute(s)
                results = cursor.fetchall()
                s = "drop table temp;"
                cursor.execute(s)
                self._connection.commit()
                cursor.close()
                
            resultList = []
            for ticket in results:
                listTicket = list(ticket)
                listTicket[4] = self.ampm(str(listTicket[4])[0:16]) if not listTicket[4] is None else ""
                listTicket[5] = self.formatEvent(listTicket[5]) if not listTicket[5] is None else ""
                resultList.append(listTicket)
            return [True, resultList]

        except dbError as e:
            print("PTE: " + str(e), file = sys.stderr)
            return[False, False]
            sys.exit(1)

        except Exception as e:
            print(str(e), file = sys.stderr)
            return[False, False]
            sys.exit(1)
#-----------------------------------------------------------------------

    def addNotif(self, time, event, buyerid, price, status, other, type):
        try:
            cursor = self._connection.cursor()

            # note that time has special format TIMESTAMP '1999-01-08 04:05:06'
            if event is None:
                raise ValueError("user cannot give null event")
            if buyerid is None:
                raise ValueError("user cannot give null sellerid")
            if status is None:
                raise ValueError("user cannot give null ticket status")
        except dbError as e:
            print("PTE: " + str(e), file = sys.stderr)
            return False
            sys.exit(1)
        except Exception as e:
            print(str(e), file = sys.stderr)
            return False
            sys.exit(1)

        try:
            if time == ' ':
                s = s = "INSERT INTO notify(event, buyerid, price, type, status, other, timeadded) VALUES('%s', '%s', %s, '%s', '%s', '%s', '%s');"% (self.format(event.lower()), self.format(buyerid), price, type, status, other, 'now')
            else:
                s = "INSERT INTO notify(time, event, buyerid, price, type, status, other, timeadded) VALUES(TIMESTAMP '%s', '%s', '%s', %s, '%s', '%s', '%s', '%s');" % (time, self.format(event.lower()), self.format(buyerid), price, type, status, other, 'now')
            cursor.execute(s)
            self._connection.commit()
            cursor.close()
            return True
        except Exception as e:
            print(str(e))
            self._connection.rollback()
            cursor.close()
            return False

#-----------------------------------------------------------------------

    def addReport(self, reportid, report, bug):
        try:
            cursor = self._connection.cursor()
        except dbError as e:
            print("PTE: " + str(e), file = sys.stderr)
            return False
            sys.exit(1)
        except Exception as e:
            print(str(e), file = sys.stderr)
            return False
            sys.exit(1)

        try:
            s = "INSERT INTO report(reportid, report, bug) VALUES('%s', '%s', '%s');"% (self.format(reportid), self.format(report), self.format(bug))
            cursor.execute(s)
            self._connection.commit()
            cursor.close()
            return True
        except Exception as e:
            print(str(e))
            self._connection.rollback()
            cursor.close()
            return False

#-----------------------------------------------------------------------
    def getNotif(self, time, event, price, other, type):
        try:
            cursor = self._connection.cursor()

            # if no argument restriction, match all
            if event is None:
                s = "SELECT * FROM notify;"
                cursor.execute(s)
                results = cursor.fetchall()
            else:
                # query all relevant data using arguments
                event = self.escapeString(event.lower())
                if type == "sell":
                    type = "buy"
                s = "SELECT * FROM notify WHERE notify.event = '%s' AND notify.time = '%s' AND notify.price >= %s AND notify.other ='%s' AND notify.status='active' AND (notify.type = 'buy/exchange' OR notify.type = '%s') UNION DISTINCT SELECT * FROM notify WHERE notify.event = '%s' AND notify.time = '%s 00:00:00' AND notify.price >= %s AND notify.other ='%s' AND notify.status='active' AND (notify.type = 'buy/exchange' OR notify.type = '%s') UNION DISTINCT SELECT * FROM notify WHERE notify.event = '%s' AND notify.time IS NULL AND notify.price >= %s AND notify.other ='%s' AND notify.status='active' AND (notify.type = 'buy/exchange' OR notify.type = '%s');" % (self.format(event), time, price, other, type, self.format(event), time[0:10], price, other, type, self.format(event), price, other, type)
                cursor.execute(s)
                results = cursor.fetchall()

            cursor.close()
            resultList = []
            for ticket in results:
                listTicket = list(ticket)
                resultList.append(listTicket)
            return [True, resultList]

        except dbError as e:
            print("PTE: " + str(e), file = sys.stderr)
            return[False, False]
            sys.exit(1)

        except Exception as e:
            print(str(e), file = sys.stderr)
            return[False, False]
            sys.exit(1)
#-----------------------------------------------------------------------
    def getUserNotifs(self, user):
        try:
            cursor = self._connection.cursor()

            # if no argument restriction, match all
            if user is None:
                s = "SELECT * FROM notify;"
                cursor.execute(s)
                results = cursor.fetchall()
            else:
                # query all relevant data using arguments
                s = "SELECT * FROM notify WHERE notify.buyerid = '%s' ORDER BY notify.notificationid DESC;" % (self.format(user))

                cursor.execute(s)
                results = cursor.fetchall()

            cursor.close()
            resultList = []
            for ticket in results:
                listTicket = list(ticket)
                if not listTicket[1] is None:
                    listTicket[1] = self.ampm(str(listTicket[1])[0:16]) if not listTicket[1] is None else ""
                else:
                    listTicket[1] = ''
                listTicket[2] = self.formatEvent(listTicket[2]) if not listTicket[2] is None else ''
                resultList.append(listTicket)
            return [True, resultList]

        except dbError as e:
            print("PTE: " + str(e), file = sys.stderr)
            return[False, False]
            sys.exit(1)

        except Exception as e:
            print(str(e), file = sys.stderr)
            return[False, False]
            sys.exit(1)

#-----------------------------------------------------------------------
# this is the function for recurring events (Dance groups and broadway)
    def getTicketsNotif(self, time, event, price, other, type):
        try:
            cursor = self._connection.cursor()

    # if no argument restriction, match all
            if time == ' ':
                # query all relevant data using arguments
                event = self.escapeString(event.lower())
                if type == "buy/exchange":
                    s = "SELECT * FROM tickets WHERE tickets.event = '%s' AND tickets.status = 'available' AND tickets.price <= %s AND tickets.time >= 'now' ORDER BY tickets.ticketid DESC;" % (self.format(event), price)
                elif type == "buy":
                    s = "SELECT * FROM tickets WHERE tickets.event = '%s' AND tickets.type = 'sell' AND tickets.status = 'available' AND tickets.price <= %s AND tickets.time >= 'now' ORDER BY tickets.ticketid DESC;" % (self.format(event), price)
                else:
                    s = "SELECT * FROM tickets WHERE tickets.event = '%s' AND tickets.type = 'exchange' AND tickets.status = 'available' AND tickets.price <= %s AND tickets.time >= 'now' ORDER BY tickets.ticketid DESC;" % (self.format(event), price)
                cursor.execute(s)
                results = cursor.fetchall()

            elif len(time) == 11:
                event = self.escapeString(event.lower())
                if type == "buy/exchange":
                    s = "SELECT * FROM tickets WHERE tickets.event = '%s' AND tickets.status = 'available' AND tickets.price <= %s AND (tickets.time >= 'now' AND (tickets.time >= '%s00:00:00' OR tickets.time <= '%s23:59:59')) ORDER BY tickets.ticketid DESC;" % (self.format(event), price, time, time)
                elif type == "buy":
                    s = "SELECT * FROM tickets WHERE tickets.event = '%s' AND tickets.type = 'sell' AND tickets.status = 'available' AND tickets.price <= %s AND (tickets.time >= 'now' AND (tickets.time >= '%s00:00:00' OR tickets.time <= '%s23:59:59'))  ORDER BY tickets.ticketid DESC;" % (self.format(event), price, time, time)
                else:
                    s = "SELECT * FROM tickets WHERE tickets.event = '%s' AND tickets.type = 'exchange' AND tickets.status = 'available' AND tickets.price <= %s AND (tickets.time >= 'now' AND (tickets.time >= '%s00:00:00' OR tickets.time <= '%s23:59:59')) ORDER BY tickets.ticketid DESC;" % (self.format(event), price, time, time)
                cursor.execute(s)
                results = cursor.fetchall()
                cursor.close()
            else:
                event = self.escapeString(event.lower())
                if type == "buy/exchange":
                    s = "SELECT * FROM tickets WHERE tickets.event = '%s' AND tickets.status = 'available' AND tickets.price <= %s AND (tickets.time = '%s' AND tickets.time >= 'now') ORDER BY tickets.ticketid DESC;" % (self.format(event), price, time)
                elif type == "buy":
                    s = "SELECT * FROM tickets WHERE tickets.event = '%s' AND tickets.type = 'sell' AND tickets.status = 'available' AND tickets.price <= %s AND (tickets.time = '%s' AND tickets.time >= 'now') ORDER BY tickets.ticketid DESC;" % (self.format(event), price, time)
                else:
                    s = "SELECT * FROM tickets WHERE tickets.event = '%s' AND tickets.type = 'exchange' AND tickets.status = 'available' AND tickets.price <= %s AND (tickets.time = '%s' AND tickets.time >= 'now') ORDER BY tickets.ticketid DESC;" % (self.format(event), price, time)
                cursor.execute(s)
                results = cursor.fetchall()
                cursor.close()

            if len(results) > 0:
                return [True, list(results[0])]
            else:
                return [True, None]

        except dbError as e:
            print("PTE: " + str(e), file = sys.stderr)
            return[False, False]
            sys.exit(1)

        except Exception as e:
            print(str(e), file = sys.stderr)
            return[False, False]
            sys.exit(1)

#-----------------------------------------------------------------------
    def editTicket(self, ticketid, time, event, sellerid, price, type, description, status, other):
        try:
            cursor = self._connection.cursor()

            # note that time has special format TIMESTAMP '1999-01-08 04:05:06'
            if time is None:
                raise ValueError("user cannot give null time")
            if ticketid is None:
                raise ValueError("user cannot give null ticketid")
            if event is None:
                raise ValueError("user cannot give null event")
            if sellerid is None:
                raise ValueError("user cannot give null sellerid")
            if price is None:
                price = 0
            if type is None:
                raise ValueError("user cannot give null type")
            if description is None:
                description = ""
            if status is None:
                raise ValueError("user cannot give null ticket status")
        except dbError as e:
            print("PTE: " + str(e), file = sys.stderr)
            return False
            sys.exit(1)
        except Exception as e:
            print(str(e), file = sys.stderr)
            return False
            sys.exit(1)

        try:
            # insert new ticket
            fullname = self.fulleventname(event.lower()).lower()
            s = "update tickets set time = '%s', event = '%s', price = %s, type = '%s', description = '%s', other = '%s', fullname = '%s' where ticketid = '%s';" % (time, self.format(event.lower()), price, type, self.format(description), other, self.format(fullname), ticketid)
            cursor.execute(s)
            self._connection.commit()
            cursor.close()
            return True
        except Exception as e:
            print(str(e))
            self._connection.rollback()
            cursor.close()
            return False
#-----------------------------------------------------------------------
# main function that takes commandline arguments and creates a
# dictionary containing the pertinent arguments dept, area, coursenum,
# title, -h, and print the results if possible
def randomString(stringLength=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))
    
    
def main():
    database = Database()
    database.connect()
    # boundary testing
    database.addTicket(None, randomString(10), randomString(5), random.random()*10, 'sell', randomString(30), 'available', 'yes')
    database.addTicket('now', None, randomString(5), random.random()*10, 'exchange', randomString(30), 'available', 'yes')
    database.addTicket('now', randomString(10), None, random.random()*10, 'sell', randomString(30), 'available', 'yes')
    database.addTicket('now', randomString(10), randomString(5), None, 'exchange', randomString(30), 'available', 'yes')
    database.addTicket('now', randomString(10), randomString(5), random.random()*10, None, randomString(30), 'available', 'yes')
    database.addTicket('now', randomString(10), randomString(5), random.random()*10, 'exchange', None, 'available', 'yes')
    database.addTicket('now', randomString(10), randomString(5), random.random()*10, 'sell', randomString(30), None, 'yes')
    database.addTicket('now', randomString(10), randomString(5), random.random()*10, 'exchange', randomString(30), None, 'yes')
    database.addTicket('now', randomString(10), randomString(5), random.random()*10, 'sell', randomString(30), 'available', None)
    
    database.addTicket('now', 'js112', randomString(5), random.random()*10, 'sell', randomString(30), 'available', 'yes')
    database.addTicket('now', 'shyoo', randomString(5), random.random()*10, 'exchange', randomString(30), 'available', 'yes')
    database.addTicket('now', 'jc84', randomString(5), random.random()*10, 'exchange', randomString(30), 'available', 'yes')
    
    print(database.getTickets('', None))
    print(database.getTickets(None, None))
    
    print(database.getTicketsSearch('', None))
    print(database.getTicketsSearch(None, None))
    
    print(database.getTicketsOther(None))
    
    database.makeTransaction(None, 'shyoo', 1)
    
    database.makeTransaction('shyoo', None, 2)
    
    database.makeTransaction('jc84', 'js112', None)
    
    database.completeTransaction(None, 'shyoo', 1)
    
    database.completeTransaction('shyoo', None, 2)
    
    database.completeTransaction('jc84', 'js112', None)
    
    database.completeTransaction('', 'shyoo', 3)
    
    database.completeTransaction('shyoo', '', 4)
        
    database.rejectTransaction(None, 5)
    
    database.rejectTransaction('shyoo', None)
    
    database.editTicket(None, 'now', 'js112', randomString(5), random.random()*10, 'sell', 'edited', 'available', 'yes')
    database.editTicket(1, None, 'js112', randomString(5), random.random()*10, 'sell', 'edited', 'available', 'yes')
    database.editTicket(2, 'now', None, randomString(5), random.random()*10, 'sell', 'edited', 'available', 'yes')
    database.editTicket(3, 'now', 'js112', None, random.random()*10, 'sell', 'edited', 'available', 'yes')
    database.editTicket(4, 'now', 'js112', randomString(5), None, 'sell', 'edited', 'available', 'yes')
    database.editTicket(5, 'now', 'js112', randomString(5), random.random()*10, None, 'edited', 'available', 'yes')
    database.editTicket(6, 'now', 'js112', randomString(5), random.random()*10, 'sell', None, 'available', 'yes')
    database.editTicket(7, 'now', 'js112', randomString(5), random.random()*10, 'sell', 'edited', None, 'yes')
    database.editTicket(8, 'now', 'js112', randomString(5), random.random()*10, 'sell', 'edited', 'available', None)


    print(database.getUserTicketsBuy(None)[1])

    database.addNotif('now', randomString(10), 'js112', None, 'active', 'yes', 'buy')
    database.addNotif('now', randomString(10), 'shyoo', random.random()*10, None, 'yes', 'buy')
    database.addNotif('now', randomString(10), 'jc84', random.random()*10, 'active', None, 'buy')
    database.addNotif('now', randomString(10), 'jc84', random.random()*10, 'active', 'yes', None)
    database.addNotif(None, randomString(10), 'js112', random.random()*10, 'active', 'yes', 'buy')
    database.addNotif('now', None, 'shyoo', random.random()*10, 'active', 'yes', 'buy')
    database.addNotif('now', randomString(10), None, random.random()*10, 'active', 'yes', 'buy')

    print(database.getUserNotifs(None)[1])
    print(database.getUserNotifs('')[1])
    
    # stress testing
    for ii in range(100):
        database.createUser(randomString(10))
        database.addTicket('now', randomString(10), randomString(5), random.random()*10, 'sell', randomString(30), 'available', 'yes')
        database.addTicket('now', randomString(10), randomString(5), random.random()*10, 'exchange', randomString(30), 'available', 'yes')
        database.getTicketByID(ii)
    print(database.getTickets('', 'priceasc')[1])
    print(database.getTickets('', 'dateasc')[1])
    print(database.getTickets('', 'sellerasc')[1])
    print(database.getTickets('', 'eventasc')[1])
    print(database.getTickets('', 'typeasc')[1])
    print(database.getTickets('', 'pricedesc')[1])
    print(database.getTickets('', 'datedesc')[1])
    print(database.getTickets('', 'sellerdesc')[1])
    print(database.getTickets('', 'eventdesc')[1])
    print(database.getTickets('', 'typedesc')[1])
    
    print(database.getTicketsOther('priceasc')[1])
    print(database.getTicketsOther('dateasc')[1])
    print(database.getTicketsOther('sellerasc')[1])
    print(database.getTicketsOther('eventasc')[1])
    print(database.getTicketsOther('typeasc')[1])
    print(database.getTicketsOther('pricedesc')[1])
    print(database.getTicketsOther('datedesc')[1])
    print(database.getTicketsOther('sellerdesc')[1])
    print(database.getTicketsOther('eventdesc')[1])
    print(database.getTicketsOther('typedesc')[1])
    
    for ii in range(200):
        database.removeTicket(ii)
    for ii in range(100):
        database.addTicket('now', 'js112', randomString(5), random.random()*10, 'sell', randomString(30), 'available', 'yes')
        database.addTicket('now', 'shyoo', randomString(5), random.random()*10, 'exchange', randomString(30), 'available', 'yes')
        database.addTicket('now', 'jc84', randomString(5), random.random()*10, 'exchange', randomString(30), 'available', 'yes')
    print(database.getUserTicket('js112')[1])
    print(database.getUserTicket('shyoo')[1])
    print(database.getUserTicket('jc84')[1])
    
    
    for ii in range(100):
        database.makeTransaction('js112', 'shyoo', ii)
    
    for ii in range(100, 200):
        database.makeTransaction('shyoo', 'jc84', ii)
    
    for ii in range(200, 300):
        database.makeTransaction('jc84', 'js112', ii)
    
    for ii in range(20):
        database.completeTransaction('js112', 'shyoo', ii)
    
    for ii in range(100, 120):
        database.completeTransaction('shyoo', 'jc84', ii)
    
    for ii in range(200, 220):
        database.completeTransaction('jc84', 'js112', ii)
        
    for ii in range(20, 40):
        database.rejectTransaction('js112', ii)
    
    for ii in range(120, 140):
        database.rejectTransaction('shyoo', ii)
    
    for ii in range(220, 240):
        database.rejectTransaction('jc84', ii)
        
    for ii in range(40, 60):
        database.editTicket(ii, 'now', 'js112', randomString(5), random.random()*10, 'sell', 'edited', 'available', 'yes')
    
    for ii in range(140, 160):
        database.editTicket(ii, 'now', 'shyoo', randomString(5), random.random()*10, 'sell', 'edited', 'available', 'yes')

    for ii in range(240, 260):
        database.editTicket(ii, 'now', 'jc84', randomString(5), random.random()*10, 'sell', 'edited', 'available', 'yes')

    print(database.getUserTicketsBuy('js112')[1])
    print(database.getUserTicketsBuy('shyoo')[1])
    print(database.getUserTicketsBuy('jc84')[1])
    

    
    for ii in range(100):
        database.addNotif('now', randomString(10), 'js112', random.random()*10, 'active', 'yes', 'buy')
        database.addNotif('now', randomString(10), 'shyoo', random.random()*10, 'active', 'yes', 'buy')
        database.addNotif('now', randomString(10), 'jc84', random.random()*10, 'active', 'yes', 'buy')

    print(database.getUserNotifs('js112')[1])
    print(database.getUserNotifs('shyoo')[1])
    print(database.getUserNotifs('jc84')[1])
    database.disconnect()

if __name__ == '__main__':
    main()
