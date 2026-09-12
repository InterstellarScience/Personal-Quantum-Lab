from netqasm.sdk import EPRSocket
from netqasm.sdk.external import NetQASMConnection



def main(app_config=None, x=0, y=0):
    epr_socket = EPRSocket("Alice")
    Bob = NetQASMConnection(
        app_name=app_config.app_name,
        epr_sockets=[epr_socket]
        )    

    with Bob:
            epr = epr_socket.recv_keep()[0]
            Bob.flush()
            m = epr.measure()
    
    m = int(m)
    return {"Bob": m}

if __name__ == "__main__":
    main()