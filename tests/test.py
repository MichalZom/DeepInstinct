from client.client import Client
from server.server import Server
import multiprocessing

def test_calcutate_numbers():
    client_conn, server_conn = multiprocessing.Pipe()

    server_side = Server(server_conn)
    server_process = multiprocessing.Process(target=server_side.handle_data)
    server_process.start()

    client_side = Client(client_conn)
    client_side.set_parameters_from_user()
    client_side.send_data_to_server()
    result = client_side.recived_data_from_server()
    client_side.print_final_resutl(result)

    client_conn.send("exit")
    server_process.join()


if __name__ == "__main__": test_calcutate_numbers()