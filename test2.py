from test1 import  Server


class SUB_Server(Server):

    def __init__(self, cpu, cache, disk, opr):
        Server.__init__(self, cpu, cache, disk, opr)

    def test_cost(self):
        cost = int(self.cpu) * 1527.679 + int(self.cache) * 100.21 + int(self.disk) * 50.789
        print("需要花费%0.2f" % cost)


if __name__ == '__main__':
    linux_server = SUB_Server(8, 40, 150, "Linux")
    linux_server.test_cost()
