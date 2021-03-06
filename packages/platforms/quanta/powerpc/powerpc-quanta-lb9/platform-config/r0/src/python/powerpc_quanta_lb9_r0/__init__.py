#!/usr/bin/python

from onl.platform.base import *
from onl.platform.quanta import *

class OnlPlatform_powerpc_quanta_lb9_r0(OnlPlatformQuanta,
                                        OnlPlatformPortConfig_48x1_4x10):
    PLATFORM='powerpc-quanta-lb9-r0'
    MODEL="LB9"
    """ Define Quanta SYS_OBJECT_ID rule.

    SYS_OBJECT_ID = .xxxx.ABCC
    "xxxx" define QCT device mark. For example, LB9->1048, LY2->3048
    "A" define QCT switch series name: LB define 1, LY define 2, IX define 3
    "B" define QCT switch series number 1: For example, LB9->9, LY2->2
    "CC" define QCT switch series number 2: For example, LY2->00, LY4R->18(R is 18th english letter)
    """
    SYS_OBJECT_ID=".1048.1900"

    def baseconfig(self):
        platform_fancontrol="%s/etc/fancontrol" % self.basedir_onl()
        FAN_CONF = '/etc/fancontrol'
        if os.path.exists(FAN_CONF):
            os.unlink(FAN_CONF)
        if os.path.exists(platform_fancontrol):
            os.symlink(platform_fancontrol, FAN_CONF)
        else:
            sys.exit(1)

        return True



