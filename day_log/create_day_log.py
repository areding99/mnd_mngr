import sys, os, datetime, uuid, task_integration

sys.path.append('../task_management')

from lib.config_parser import ConfigParser

cp = ConfigParser()
config = cp.get_config()

# constants
parent_dir = "/Desktop/task_management" # probably no need for this
daily_log_relative_path = "/demo_files/logs" # move to config
tasks_relative_path = "/demo_files/tasks" # move to config


# helpers for setting up today's log
def write_header(f_name, date):
  f_io = open(f_name, 'w+')
  
  if (f_io.read() != ""):
    print("file is not empty")
    return

  f_io.write("---\n")
  f_io.write("title: "+today+"\n")
  f_io.write("path: "+daily_log_relative_path[1:]+"/"+str(date.year)+"/"+today_log_name+"\n")
  f_io.write("created: "+str(date.date())+" "+str(date.time())[:5]+"\n")
  f_io.write("id: "+str(uuid.uuid4())+"\n")
  f_io.write("---\n\n")
  f_io.write("# "+get_weekday(date)+", "+str(date.date())+" "+"\n")

  f_io.close()




def append_tasks_section(f_name, sections):
  f_io = open(f_name, 'a')

  f_io.write("\n# Tasks\n\n")

  # eventually sections should set in config with order
  os.chdir(os.path.expanduser('~')+parent_dir+tasks_relative_path)

  sections = os.listdir()

  # for each section
  for section in sections:
    f_io.write("## "+section+"\n\n")

    os.chdir(section)
    tasks = os.listdir()

    for task in tasks:
      f_io.write("- [ ] "+task+"\n")

    f_io.write("\n")

    os.chdir("..")

  f_io.close()





def read_tasks(f_name):
  f_io = open(f_name)



def get_weekday(date):
  today = date.weekday()

  if today == 0:
    return "Monday"
  elif today == 1:
    return "Tuesday"
  elif today == 2:
    return "Wednesday"
  elif today == 3:
    return "Thursday"
  elif today == 4:
    return "Friday"
  elif today == 5:
    return "Saturday"
  else:
    return "Sunday"




def nav_to_year(date):
  os.chdir(os.path.expanduser('~')+parent_dir+daily_log_relative_path)

  year = date.year

  if (not os.path.isdir(str(year))):
    os.mkdir(str(year))

  os.chdir(str(year))

  return year



def get_yesterday(year):
  if (len(os.listdir()) > 0):
    return max(os.listdir())

  # check last year for a note
  os.chdir("..")
  previous_year_dir = str(year-1)

  if (not os.path.isdir(previous_year_dir)):
    os.chdir(str(year))
    return 
  else:
    os.chdir(previous_year_dir)

    if (len(os.listdir()) == 0):
      return

    yesterday = max(os.listdir())
      
    os.chdir("..")
    os.chdir(str(year))

    return yesterday

def get_yesterday_summary(year):
  yesterday = get_yesterday(year)

  if (yesterday == None):
    # no summary for yesterday
    return 
  
  # get yesterday's summary

def get_outstanding_tasks():


  return



# START OF SCRIPT

date = datetime.datetime.now()
year = nav_to_year(date)

yesterday_summary = get_yesterday_summary(year)

today = str(date.date())
today_log_name = today+".md"

write_header(today_log_name, date)



# append_tasks_section()

# get outstanding tasks

# set up new day




# for now, overwrite
# if (os.path.isfile(today_log_name)):
#   print("you've already created a daily log for today")
#   exit(1)



