
class Server():
    """这是一个服务器的类"""

    def __init__(self, cpu, cache, disk, opr):
        self.cpu = cpu
        self.cache = cache
        self.disk = disk
        self.__opr = opr

    def print_info(self):
        print("%s核cpu,%sG内存,%sG磁盘空间,%s" % (str(self.cpu), str(self.cache), str(self.disk), self.__opr))


if __name__ == '__main__':
    linux_server = Server(8, 40, 150, "Linux")
    #print(linux_server.__opr) 不可访问
    linux_server.print_info()
