from netqasm.sdk import EPRSocket
from netqasm.sdk.external import NetQASMConnection



def main(app_config=None, x=0, y=0):
    epr_socket = EPRSocket("alice")
    bob = NetQASMConnection(
        app_name=app_config.app_name,
        epr_sockets=[epr_socket]
        )    

    with bob:
            epr = epr_socket.recv_keep()[0]
            bob.flush()
            m = epr.measure()
    
    m = int(m)
    return {"Bob": m}

if __name__ == "__main__":
    main()