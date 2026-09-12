from netqasm.sdk import EPRSocket
from netqasm.sdk.external import NetQASMConnection



def main(app_config=None, x=0, y=0):
    epr_socket = EPRSocket("bob")
    alice = NetQASMConnection(
        app_name=app_config.app_name,
        epr_sockets=[epr_socket]
        )

    with alice:
        epr = epr_socket.create_keep()[0]
        m = epr.measure()

    m = int(m)
    return {"Alice": m}

if __name__ == "__main__":
    main()