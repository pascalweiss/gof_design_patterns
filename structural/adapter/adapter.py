from structural.adapter.adaptee import UserTarget
from structural.adapter.target import InvokerTarget


class InvokerTargetAdapter(InvokerTarget):
    def request(self):
        return UserTarget.get_response()