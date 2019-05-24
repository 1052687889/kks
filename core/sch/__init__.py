from core.error import RequestListEmptyException
from core.http.request import Request
import queue
class ManageReq(object):
    __request_dict = {}
    @staticmethod
    def get_request():
        keys = ManageReq.__request_dict.keys()
        if keys == {}.keys():
            raise RequestListEmptyException("爬虫请求队列为空")
        min_priority = min(keys)
        req = ManageReq.__request_dict[min_priority].get()
        if ManageReq.__request_dict[min_priority].empty():
            del ManageReq.__request_dict[min_priority]
        return req

    @staticmethod
    def add_request(request):
        if request.priority not in ManageReq.__request_dict.keys():
            ManageReq.__request_dict[request.priority]=queue.Queue()
        ManageReq.__request_dict[request.priority].put(request)

if __name__ == "__main__":
    ManageReq.add_request(Request(url='www.baidu.com'))
    ManageReq.add_request(Request(url='www.baidu.com',priority=10))
    print(ManageReq.get_request().priority)
    print(ManageReq.get_request().priority)






