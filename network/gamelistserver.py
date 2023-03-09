import sys
import socket
import selectors
import traceback

from libs import libserver

class GameListServer():
   
    def __init__(self):
        sel = selectors.DefaultSelector()
        
        if len(sys.argv) != 3:
            print(f"Usage: {sys.argv[0]} <host> <port>")
            sys.exit(1)

        host, port = sys.argv[1], int(sys.argv[2])
        lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Avoid bind() exception: OSError: [Errno 48] Address already in use
        lsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        lsock.bind((host, port))
        lsock.listen()
        print(f"Listening on {(host, port)}")
        lsock.setblocking(False)
        sel.register(lsock, selectors.EVENT_READ, data=None)

        try:
            while True:
                events = sel.select(timeout=None)
                for key, mask in events:
                    if key.data is None:
                        conn, addr = key.fileobj.accept()  # Should be ready to read
                        print(f"Accepted connection from {addr}")
                        conn.setblocking(False)
                        message = libserver.Message(sel, conn, addr)
                        sel.register(conn, selectors.EVENT_READ, data=message)
                    else:
                        message = key.data
                        try:
                            request = message.process_events(mask)
                            if request is not None:
                                print(request)
                        except Exception:
                            print(
                                f"Main: Error: Exception for {message.addr}:\n"
                                f"{traceback.format_exc()}"
                            )
                            message.close()
        except KeyboardInterrupt:
            print("Caught keyboard interrupt, exiting")
        finally:
            sel.close()
    pass

if __name__ == '__main__':
    GameListServer()