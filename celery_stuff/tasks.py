from time import sleep
from celery import Celery

# Creating a celery instance with redis as message broker.
app = Celery('first_app', broker='redis://localhost/2')
# New code below
app.conf.task_routes = {
    'celery_stuff.tasks.serve_a_beer': {'queue': 'beer'},
    'celery_stuff.tasks.serve_a_coffee': {'queue': 'coffee'}
}


@app.task
def serve_a_beer(_type, size):
    """
     This is a celery task. Just a normal function with task decorator.
     Note that we use the decorator from a celery insance.
    """
    print('Serving {} of {} beer!'.format(size, _type))
    sleep(3)
    print("""
          ------------------------------------------------
                   .   *   ..  . *  *
                 *  * @()Ooc()*   o  .
                     (Q@*0CG*O()  ___
                    |\_________/|/ _ \
                    |  |  |  |  | / | |
                    |  |  |  |  | | | |
                    |  |  |  |  | | | |
                    |  |  |  |  | | | |
                    |  |  |  |  | | | |
                    |  |  |  |  | \_| |
                    |  |  |  |  |\___/  
                    |\_|__|__|_/|
                     \_________/
          ------------------------------------------------
          """)


@app.task
def serve_a_coffee(_type, size):
    """
     This is a celery task. Just a normal function with task decorator.
     Note that we use the decorator from a celery insance.
    """
    print('Serving a {} {} coffee!'.format(size, _type))
    sleep(1)
    print("""
          ---------------------------------
                          )  (
                         (   ) )
                          ) ( (
                     mrf_______)_
                     .-'---------|  
                    ( C|/\/\/\/\/|
                     '-./\/\/\/\/|
                       '_________'
                        '-------'
          ---------------------------------
          """)

