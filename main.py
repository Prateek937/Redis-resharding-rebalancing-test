import json
from time import sleep, time
import create_cluster
import count_slot_key
import write_keys
import add_master
import rebalance
import reshard
import remove_master

KEY_COUNT = 100

def count(step):
    print(f"{str(step)} > COUNT NODES\n\n")
    result= count_slot_key.count_slot_key(nodes["node1"]["ip"], nodes["node1"]["port"])
    print(f"{result}\n" )

def wait(seconds):
    print(f"Waiting for {seconds} seconds...")
    sleep(seconds)

def print_time(time_taken):
    print("Time Taken:", time_taken)

def main(nodes):
    global KEY_COUNT
    #console log time stamp and numner of keys tested with
    t1 = time()
    print(t1)
    # operate with 3+1 node and n+1 nodes as well
    print("1 > CREATE CLUSTER OF THREE EMPTY NODES\n\n")
    result = create_cluster.create_cluster(nodes)
    print(f"{result}\n")
    print_time(time()-t1)

    wait(10)
    count(2)

    st1 = time()
    #we need to wait for some time before writing keys otherwise cluster down error occurs
    print(f"3 > WRITE KEYS METHOD 1\n\n")
    result = write_keys.write_keys(nodes, KEY_COUNT)
    print(f"{result}\n")
    print_time(time() - st1)

    count(4)

    st1 = time()
    print(f"3 > WRITE KEYS METHOD 2\n\n")
    result = write_keys.write_keys_to_single_master(nodes, KEY_COUNT)
    print(f"{result}\n")
    print_time(time() - st1)
    
    count(4)

    # st1 = time()
    # print("7 > REBALANCE\n\n")
    # result= rebalance.rebalance_cluster(nodes["node2"]["ip"], nodes["node2"]["port"])
    # print(f"{result}\n" )
    # print_time(time() - st1)
    
    # count(8)
    
    # st1 = time()
    # print("5 > ADD MASTER\n\n")
    # result = add_master.add_master(nodes["node1"]["ip"],6379,nodes["node4"]["ip"],6379)
    # print(f"{result}\n" )
    # print_time(time() - st1)

    # wait(10) #this wait is necessary. it doesn't show up in count otherwise.
    # count(6)

    # st1 = time()
    # print("7 > REBALANCE\n\n")
    # result= rebalance.rebalance_cluster(nodes["node4"]["ip"], nodes["node4"]["port"])
    # print(f"{result}\n" )
    # print_time(time() - st1)
    
    # count(8)

    # wait(15)
    # st1 = time()
    # print("9> RESHARD\n\n")
    # result= reshard.reshard(nodes["node1"]["ip"], nodes["node1"]["port"], nodes["node4"]["ip"], nodes["node4"]["port"])
    # print(f"{result}\n" )
    # print_time(time() - st1)
    
    # wait(15)
    # count(10)
    
    # st1 = time()
    # print("11 > REBALANCE\n\n")
    # result= rebalance.rebalance_cluster(nodes["node4"]["ip"], nodes["node4"]["port"])
    # print(f"{result}\n" )
    # print_time(time() - st1)

    # count(12)

    # st1 = time()
    # print("13 > REMOVE 4TH NDOE\n\n")
    # result= remove_master.remove_master(nodes["node4"]["ip"], nodes["node4"]["port"])
    # print(f"{result}\n" )
    # print_time(time() - st1)

    # count(14)
    
    print_time(time() - t1)


file = open("./inventory.json")
nodes = json.load(file)
main(nodes)

# 7,656,482 written out of 10M  7,656,482  7,656,482 7,656,482
# 672,378  written out of 1M 972,357 972,357 972,307
# increases after rebalance

# sum the total number of keys