## LAB1


############################################################
#
#

# global variables

url = "https://cloud.timeedit.net/kth/web/public01/ri.html?h=t&sid=7&p=20201021.x%2C20210117.x&objects=381614.5&ox=0&types=0&fe=0&g=f&ds=f&cch=16-53%2C6-10"

scheduleFile = "DD1321.htm"    # Name of schedule html-file

############################################################
#
# imports and defs
#
import re, getopt, sys, urllib.request


class Schedule:
    def __init__(self):
        self.week = ''
        self.date = ''
        self.day = ''
        self.activity = []
        self.time = ''

    def __str__(self):
        s = "{} => {:3s}, {:>5s}, {:>3s}, {} ;".format( self.__class__.__name__, self.week, self.day, self.date, self.time )
        for h in self.activity:
            s += h + "; "
        return s

    def __contains__(self, x):
        if (x in self.week or x in self.date or x in self.day or x in self.activity or x in self.time):
            return True


###########################################################################
##
## parse_url_file
##
## IN - Vector with strings
##     
## OUT - Vector/Array with objects (strings?) 
##
def parse_url_file(file_content):
    vek = []

    reg_expr_w = re.compile('.*?td.*?class.*?headline.*?> *([MTOFL][a-zåäö]+) *20[12][0-9]-0?([123]?[0-9])-0?([123]?[0-9])<.*weekin.*> *(v.*?)<.', re.I)
    reg_expr_d = re.compile('.*?td.*?class.*?headline.*?>([MTOFL][a-zåäö]+) *20[12][0-9]-0?([123]?[0-9])-0?([123]?[0-9])<.')
    reg_expr_t = re.compile('.*?td +id="time.*?>(.+?)<.td')
    reg_expr_i = re.compile('.*?td.*?class.*?column[0-1].*?>(.*?)<.td', re.I) 

    #lines = file_content.split('\n')
    lines = file_content

    qq = Schedule()
    week_var = 0
    day_var = 0
    date_var = 0
    timevar = 0
    newEntry = False
    for j, line in enumerate(lines):

        #week
        m = reg_expr_w.match(line) 
        if (m != None):
            week_var = m.group(4)  
            qq.week = week_var 
        else:
            qq.week = week_var
            next

        #activity
        m = reg_expr_i.match(line) 
        if (m != None) and len(m.group(1)) > 0:
            qq.activity.append(m.group(1))
            newEntry =True
            next

        #date
        m = reg_expr_d.match(line) 
        if (m != None) : 
            day_var = m.group(1) 
            date_var = m.group(3) + "/" + m.group(2)  
        else:
            qq.day = day_var
            qq.date = date_var
            next

        #time
        m = reg_expr_t.match(line) 
        if (m != None) and newEntry == True:
            qq.time = m.group(1)
            vek.append(qq)
            qq = Schedule()
            next
    return vek


###########################################################################
##
## get file content
##
## IN  - String with the name of the requested file
##     
## OUT - Vector with rows in the file (if it exists)
## 
##
def get_file_content(file_name):
    infil = ''
    try:
        infil = open(file_name, 'r')
    except:
        print ("No such file", file_name, " please run with --update")
        print ("	python", sys.argv[0], "--update")
        sys.exit()
       
    file_content = infil.readlines()
    #file_content = infil.read()
    # print('file_content = ', file_content) 
    return file_content
    
###########################################################################
##
## usage
##
## IN  
##     
## OUT 
##
def usage():
    print ("Usage example:")
    print ("python" , sys.argv[0] ,  "--update ")
    print ("	updates Time Edit schedule")
    print ("python" , sys.argv[0] ,  '--check "v 49"')
    print ("	checks schedule for week 49")
    print ("python" , sys.argv[0])
    print ("	prints previously downloaded schedule")
    
###########################################################################
##
## parse_command_line_args
##
## IN  what vilket är det som söks efter
##     
## OUT valmöjligheter för start up av systemet. command line options
##
def parse_command_line_args():
    try:
        opts, rest = getopt.getopt(sys.argv[1:], "hc:u", ["help", "check=", "update"])
    except getopt.GetoptError:
        # print help information and exit:
        print ("Unknown option")
        usage()
        sys.exit(2)

    todo = {}
    for option, value in opts:
        if option in ("-h", "--help"):
            usage()
            sys.exit()
        elif option in ('--check', '-c'):
            todo["check"]=value
        elif option in ('--update', '-u'):
            todo["update"] = value

    return todo

###########################################################################
##
## print_schedule
##
## IN  
##     
## OUT 
##
def print_schedule(data):
    print ("----------- Schedule -------------")
    for item in data:
        print (item)

###########################################################################
##
## search_data
##
## IN  
##     
## OUT 
##
def search_data(what, dataset):
    found = False
    for item in dataset:
        if (what in item):
            found = True
            print (item)
    if (found == False):
        print ("Nothing happens", what)

###########################################################################
##
## main
##
## IN  
##     
## OUT 
##
def main():

    global url

    # get command line options
    todo = parse_command_line_args()

    # update time edit file
    if 'update' in todo:
        print ("fetching url ...")
        webcontent = urllib.request.urlopen( url )
        with open( scheduleFile, "w") as fil:
            for row in webcontent:
                utf8line = row.decode('utf8')
                fil.write(utf8line)
        print ("         done")
        
    # Get schedule from disc
    filedata  = get_file_content(scheduleFile)
    sched = parse_url_file(filedata)

    # Do something
    if 'check' in todo:
        search_data(todo["check"], sched)
    else:
        print_schedule(sched)

    
###########################################################################

if __name__ == "__main__":
    main()

# td data och tr är rad
#reg_expr_w matchar med rad 3 och 4
#reg_expr_d matchar med rad 3 och 4
#reg_expr_t matchar med rad 8
#reg_expr_i matchar med rad 9 till 12 

#kan bara söka efter hela ord
