from apscheduler.schedulers.blocking import BlockingScheduler
from main import main

# Create a blocking scheduler object.
scheduler = BlockingScheduler()

def scheduled_job():
    """
    This function is for scheduling a job, from the function of main.py
    """
    main()
    print ("Your mail has been sent successfully")

# Add a job that will start the scheduled_job function on the given time. for more information
# please look at https://apscheduler.readthedocs.io/en/3.x/index.html
scheduler.add_job(scheduled_job, 'cron', year='*', month='*', day=11, hour=16, minute=26)

# Start the scheduler object.
scheduler.start()