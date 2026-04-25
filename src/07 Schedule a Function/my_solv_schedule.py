# import time,sched
 
# def schedule_function(etime,func,*args):
#   s = sched.scheduler(time.time,time.sleep)
#   s.enterabs(etime,1,func,argument=args)
#   print(f"{func.__name__} scheduled for{time.asctime(time.localtime(etime))} ")
#   s.run()
# Create one global scheduler
import sched,time,threading
scheduler = sched.scheduler(time.time, time.sleep)

def run_scheduler():
    while True:
        scheduler.run(blocking=False)  # process due events only
        time.sleep(0.5)  # avoid busy loop

# Start scheduler in a background thread
threading.Thread(target=run_scheduler, daemon=True).start()

def schedule_function(event_time, function, *args):
    print(f"{function.__name__}() scheduled for {time.asctime(time.localtime(event_time))}")
    scheduler.enterabs(event_time, 1, function, argument=args)

if __name__ == '__main__':
    schedule_function(time.time() + 5, print, 'Howdy!')
    schedule_function(time.time() + 8, print, 'Hello again!')
    
    # Keep main thread alive long enough to see output
    time.sleep(10)