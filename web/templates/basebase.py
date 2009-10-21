#!/usr/bin/env python




##################################################
## DEPENDENCIES
import sys
import os
import os.path
from os.path import getmtime, exists
import time
import types
import __builtin__
from Cheetah.Version import MinCompatibleVersion as RequiredCheetahVersion
from Cheetah.Version import MinCompatibleVersionTuple as RequiredCheetahVersionTuple
from Cheetah.Template import Template
from Cheetah.DummyTransaction import DummyTransaction
from Cheetah.NameMapper import NotFound, valueForName, valueFromSearchList, valueFromFrameOrSearchList
from Cheetah.CacheRegion import CacheRegion
import Cheetah.Filters as Filters
import Cheetah.ErrorCatchers as ErrorCatchers
from templates.pythonbase import pythonbase
from mx.DateTime import gmt
import random

##################################################
## MODULE CONSTANTS
try:
    True, False
except NameError:
    True, False = (1==1), (1==0)
VFFSL=valueFromFrameOrSearchList
VFSL=valueFromSearchList
VFN=valueForName
currentTime=time.time
__CHEETAH_version__ = '2.0.1'
__CHEETAH_versionTuple__ = (2, 0, 1, 'final', 0)
__CHEETAH_genTime__ = 1256146344.800509
__CHEETAH_genTimestamp__ = 'Wed Oct 21 17:32:24 2009'
__CHEETAH_src__ = 'basebase.tmpl'
__CHEETAH_srcLastModified__ = 'Wed Oct 21 17:32:09 2009'
__CHEETAH_docstring__ = 'Autogenerated by CHEETAH: The Python-Powered Template Engine'

if __CHEETAH_versionTuple__ < RequiredCheetahVersionTuple:
    raise AssertionError(
      'This template was compiled with Cheetah version'
      ' %s. Templates compiled before version %s must be recompiled.'%(
         __CHEETAH_version__, RequiredCheetahVersion))

##################################################
## CLASSES

class basebase(pythonbase):

    ##################################################
    ## CHEETAH GENERATED METHODS


    def __init__(self, *args, **KWs):

        pythonbase.__init__(self, *args, **KWs)
        if not self._CHEETAH__instanceInitialized:
            cheetahKWArgs = {}
            allowedKWs = 'searchList namespaces filter filtersLib errorCatcher'.split()
            for k,v in KWs.items():
                if k in allowedKWs: cheetahKWArgs[k] = v
            self._initCheetahInstance(**cheetahKWArgs)
        

    def title(self, **KWS):



        ## CHEETAH: generated from #def title at line 10, col 1.
        trans = KWS.get("trans")
        if (not trans and not self._CHEETAH__isBuffering and not callable(self.transaction)):
            trans = self.transaction # is None unless self.awake() was called
        if not trans:
            trans = DummyTransaction()
            _dummyTrans = True
        else: _dummyTrans = False
        write = trans.response().write
        SL = self._CHEETAH__searchList
        _filter = self._CHEETAH__currentFilter
        
        ########################################
        ## START - generated method body
        
        write('''Untitled
''')
        
        ########################################
        ## END - generated method body
        
        return _dummyTrans and trans.response().getvalue() or ""
        

    def banner(self, **KWS):



        ## CHEETAH: generated from #def banner at line 14, col 1.
        trans = KWS.get("trans")
        if (not trans and not self._CHEETAH__isBuffering and not callable(self.transaction)):
            trans = self.transaction # is None unless self.awake() was called
        if not trans:
            trans = DummyTransaction()
            _dummyTrans = True
        else: _dummyTrans = False
        write = trans.response().write
        SL = self._CHEETAH__searchList
        _filter = self._CHEETAH__currentFilter
        
        ########################################
        ## START - generated method body
        
        _v = VFFSL(SL,"title",True) # '$title' on line 15, col 1
        if _v is not None: write(_filter(_v, rawExpr='$title')) # from line 15, col 1.
        write('''
''')
        
        ########################################
        ## END - generated method body
        
        return _dummyTrans and trans.response().getvalue() or ""
        

    def body(self, **KWS):



        ## CHEETAH: generated from #def body at line 20, col 1.
        trans = KWS.get("trans")
        if (not trans and not self._CHEETAH__isBuffering and not callable(self.transaction)):
            trans = self.transaction # is None unless self.awake() was called
        if not trans:
            trans = DummyTransaction()
            _dummyTrans = True
        else: _dummyTrans = False
        write = trans.response().write
        SL = self._CHEETAH__searchList
        _filter = self._CHEETAH__currentFilter
        
        ########################################
        ## START - generated method body
        
        write('''<div id="bodyText">
No body! :)
</div>
''')
        
        ########################################
        ## END - generated method body
        
        return _dummyTrans and trans.response().getvalue() or ""
        

    def _title(self, **KWS):



        ## CHEETAH: generated from #block _title at line 59, col 1.
        trans = KWS.get("trans")
        if (not trans and not self._CHEETAH__isBuffering and not callable(self.transaction)):
            trans = self.transaction # is None unless self.awake() was called
        if not trans:
            trans = DummyTransaction()
            _dummyTrans = True
        else: _dummyTrans = False
        write = trans.response().write
        SL = self._CHEETAH__searchList
        _filter = self._CHEETAH__currentFilter
        
        ########################################
        ## START - generated method body
        
        write('''
''')
        if VFN(VFFSL(SL,"title",True),"find",False)("EVE-Central") != -1: # generated from line 61, col 1
            pass
        else: # generated from line 63, col 1
            write(''' EVE-Central -
''')
        write(''' ''')
        _v = VFFSL(SL,"title",True) # '$title' on line 66, col 2
        if _v is not None: write(_filter(_v, rawExpr='$title')) # from line 66, col 2.
        write('''
''')
        
        ########################################
        ## END - generated method body
        
        return _dummyTrans and trans.response().getvalue() or ""
        

    def _banner(self, **KWS):



        ## CHEETAH: generated from #block _banner at line 122, col 1.
        trans = KWS.get("trans")
        if (not trans and not self._CHEETAH__isBuffering and not callable(self.transaction)):
            trans = self.transaction # is None unless self.awake() was called
        if not trans:
            trans = DummyTransaction()
            _dummyTrans = True
        else: _dummyTrans = False
        write = trans.response().write
        SL = self._CHEETAH__searchList
        _filter = self._CHEETAH__currentFilter
        
        ########################################
        ## START - generated method body
        
        write('''<h1>''')
        _v = VFFSL(SL,"banner",True) # '$banner' on line 123, col 5
        if _v is not None: write(_filter(_v, rawExpr='$banner')) # from line 123, col 5.
        write('''</h1>
''')
        
        ########################################
        ## END - generated method body
        
        return _dummyTrans and trans.response().getvalue() or ""
        

    def respond(self, trans=None):



        ## CHEETAH: main method generated for this template
        if (not trans and not self._CHEETAH__isBuffering and not callable(self.transaction)):
            trans = self.transaction # is None unless self.awake() was called
        if not trans:
            trans = DummyTransaction()
            _dummyTrans = True
        else: _dummyTrans = False
        write = trans.response().write
        SL = self._CHEETAH__searchList
        _filter = self._CHEETAH__currentFilter
        
        ########################################
        ## START - generated method body
        
        write('''








<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN"
\t"http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">

<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en">


<!--
#    EVE-Central.com Codebase
#    Copyright (C) 2006-2009 StackFoundry LLC and Yann Ramin
''')
        write('''#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
''')
        write('''#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
''')
        write('''#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
-->

<head>

<link href="/style.css" rel="stylesheet" type="text/css" />
<script type="text/javascript" src="/js/jquery.min.js"></script>
<script type="text/javascript" src="/js/evec.js"></script>


  <title>
''')
        self._title(trans=trans)
        write('''</title>

</head>

<body>




<script src="http://www.google-analytics.com/urchin.js" type="text/javascript">
</script>
<script type="text/javascript">
_uacct = "UA-84549-2";
urchinTracker();
</script>

<div id="header">


<a href="/"> <img src="http://cdn.eve-central.com/logo.png" alt="Go Home" /></a>
<a href="/home/market.html"><img src="http://cdn.eve-central.com/market.png" alt="View" /></a>
<img src="http://cdn.eve-central.com/tenspacer.png" />
<a href="/tradetool/"><img src="http://cdn.eve-central.com/trade.png" alt="Trade" /></a>
<img src="http://cdn.eve-central.com/tenspacer.png" />
<a href="/home/software.html"><img src="http://cdn.eve-central.com/contr.png" alt="Contribute" /></a>
<img src="http://cdn.eve-central.com/tenspacer.png" />
<a href="/corps/"><img src="http://cdn.eve-central.com/share.png" alt="Share" /></a>
<img src="http://cdn.eve-central.com/tenspacer.png" />
<a href="/home/develop.html"><img src="http://cdn.eve-central.com/develop.png" alt="Develop" /></a>
</div>

<div id="linkBar">

<table border="0" width="98%" cellpadding="0" cellspacing="0">
<tr>
<td class="alignRight">
''')
        if 'user' in VFFSL(SL,"session",True): # generated from line 104, col 1
            write('''<a href="/users/"><i>''')
            _v = VFN(VFFSL(SL,"session",True)['user'],"username",True) # "$session['user'].username" on line 105, col 22
            if _v is not None: write(_filter(_v, rawExpr="$session['user'].username")) # from line 105, col 22.
            write('''</i></a> <a href="/users/logout.html">Logout</a>
''')
        else: # generated from line 106, col 1
            write('''<a href="/users/">Register and Login</a>
&nbsp;
''')
        write('''|
''')
        timehead = gmt()
        write('''
''')
        _v = VFN(VFFSL(SL,"timehead",True),"Format",False)("%b %e %H:%M") # '$timehead.Format("%b %e %H:%M")' on line 113, col 1
        if _v is not None: write(_filter(_v, rawExpr='$timehead.Format("%b %e %H:%M")')) # from line 113, col 1.
        write('''
</td>
</tr>
</table>

</div>



''')
        self._banner(trans=trans)
        write('''
''')
        if VFFSL(SL,"isigb",True): # generated from line 126, col 1
            write('''
''')
        else: # generated from line 128, col 1
            write('''\t<div id="bodyText">
''')
        _v = VFFSL(SL,"body",True) # '$body' on line 131, col 1
        if _v is not None: write(_filter(_v, rawExpr='$body')) # from line 131, col 1.
        write('''


\t</div>




<div id="footer">

''')
        timefoot = gmt()
        write('''
<!-- All times GMT unless otherwise specified. It is now: <b>''')
        _v = VFN(VFFSL(SL,"timefoot",True),"Format",False)("%b %e %H:%M") # '$timefoot.Format("%b %e %H:%M")' on line 143, col 62
        if _v is not None: write(_filter(_v, rawExpr='$timefoot.Format("%b %e %H:%M")')) # from line 143, col 62.
        write(''' (GMT)</b> -->


<p class="adLink">


<b><a href="http://www.shatteredcrystal.com/code.php/eve_online/~325">EVE Online Game Time Codes</a></b> - Support EVE-Central by purchasing them at ShatteredCrystal.com through this affiliate link.</p>
<p>


<script type="text/javascript"><!--
google_ad_client = "pub-8691225504311148";
google_alternate_color = "FFFFFF";
google_ad_width = 468;
google_ad_height = 60;
google_ad_format = "468x60_as";
google_ad_type = "text_image";
google_ad_channel ="2372685710";
google_color_border = "FDFFCA";
google_color_bg = "FDFFCA";
google_color_link = "0000CC";
google_color_url = "008000";
google_color_text = "000000";
//--></script>
<script type="text/javascript"
  src="http://pagead2.googlesyndication.com/pagead/show_ads.js">
</script>
<br />
EVE-Central.com does not select nor endorse any advertisers which make use of Google AdSense keyword based advertising. <i>Don\'t buy ISK for real cash!</i> It is against the EVE-Online Terms of Service. For more details, please consult the <a href="http://eve-online.com">EVE-Online</a> website.
Material related to EVE-Online is used with limited permission of CCP Games hf. No official affiliation or endorsement by CCP Games hf is stated or implied.

<br />


<br />
&copy 2005-2009 <a href="http://www.stackworks.net/">StackFoundry LLC</a>\t Feedback? Bug reports? Send them to Yann at <a href="mailto:atrus [at] stackworks.net">atrus [at] stackworks.net</a>.  EVE-Central.com uses advertising and affiliate links to help offset the cost of co-location, servers and bandwidth. The EVE-Central.com code base is <a href="http://dev.eve-central.com/eve-central/">made available</a> under the <a href="http://www.fsf.org/licensing/licenses/agpl-3.0.html">Affero GPL (AGPL) version 3.0 or later. </a>
</p>

</div>

</body>
</html>
''')
        
        ########################################
        ## END - generated method body
        
        return _dummyTrans and trans.response().getvalue() or ""
        
    ##################################################
    ## CHEETAH GENERATED ATTRIBUTES


    _CHEETAH__instanceInitialized = False

    _CHEETAH_version = __CHEETAH_version__

    _CHEETAH_versionTuple = __CHEETAH_versionTuple__

    _CHEETAH_genTime = __CHEETAH_genTime__

    _CHEETAH_genTimestamp = __CHEETAH_genTimestamp__

    _CHEETAH_src = __CHEETAH_src__

    _CHEETAH_srcLastModified = __CHEETAH_srcLastModified__

    _mainCheetahMethod_for_basebase= 'respond'

## END CLASS DEFINITION

if not hasattr(basebase, '_initCheetahAttributes'):
    templateAPIClass = getattr(basebase, '_CHEETAH_templateClass', Template)
    templateAPIClass._addCheetahPlumbingCodeToClass(basebase)


# CHEETAH was developed by Tavis Rudd and Mike Orr
# with code, advice and input from many other volunteers.
# For more information visit http://www.CheetahTemplate.org/

##################################################
## if run from command line:
if __name__ == '__main__':
    from Cheetah.TemplateCmdLineIface import CmdLineIface
    CmdLineIface(templateObj=basebase()).run()


