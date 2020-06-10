from structural.proxy.subject import Submitter, InsecureSubmitter


class SubmitterProxy(Submitter):
    def preprocess(self, data):
        """
        Depending on this function, the proxy is either
        a virtual, protection or remote proxy.
        """
        data.encryped = True

    def submit(self, data):
        self.preprocess(data)
        real_submitter = InsecureSubmitter()
        return real_submitter.submit(data)
