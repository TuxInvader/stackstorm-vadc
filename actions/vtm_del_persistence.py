#! /usr/bin/python

from st2actions.runners.pythonrunner import Action
from lib.vadc import Vtm


class VtmDelPersistence(Action):

    def run(self, vtm, name):

        vtm = Vtm(self.config, self.logger, vtm)
        vtm.del_session_persistence(name)
        return (True, None)
