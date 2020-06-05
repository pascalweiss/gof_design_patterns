from patterns.structural.proxy.test_utils.receiver import test_response

# ------------------- Subject --------------------


class Submitter:

    def submit(self, data):
        raise NotImplementedError


# --------------- Real Subject --------------------

class InsecureSubmitter(Submitter):
    def submit(self, data):
        return test_response(data)
