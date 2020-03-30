from library import car, decorate
import threading
import concurrent.futures
import sys
###############################################################################
####This function will call two cars run in sequence
###############################################################################
@decorate.decorate_answer
def question_1(t_car, b_car):
    t_car.run()
    b_car.run()

###############################################################################
####This function will call two cars run in differernt threads
###############################################################################
@decorate.decorate_answer
def question_2(t_car, b_car):
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(t_car.run)
        executor.submit(b_car.run)

###############################################################################
#### This function will call two cars run in differernt threads
#### and use a lock to prevent race condition
#### 2nd car will wait until 1st car finish
###############################################################################
@decorate.decorate_answer
def question_3(t_car, b_car):
    in_lock = threading.Lock()
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(t_car.run, lock=in_lock)
        executor.submit(b_car.run, lock=in_lock)

###############################################################################
#### This function will call two cars run in differernt threads
#### two cars will run in parallel
###############################################################################
@decorate.decorate_answer
def question_4(t_car, b_car):
    in_event = [threading.Event(), threading.Event()]
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(t_car.run, event=in_event)
        executor.submit(b_car.run, event=in_event[::-1])


if __name__ == "__main__":
    question = [None, question_1, question_2, question_3, question_4]
    cmd = sys.argv[1:]
    bmw_inst = car.BMWCar()
    toyoya_inst = car.ToyotaCar()
    for i in range(len(cmd)):
        try:
            ques_id = int(cmd[i])
            question[ques_id](toyoya_inst, bmw_inst)
        except:
            print("\nYou input %s and it's not right format." %cmd[i])
            print("Please follow the rule in README file.\n")
