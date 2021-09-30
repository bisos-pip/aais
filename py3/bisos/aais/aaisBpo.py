# -*- coding: utf-8 -*-
"""\
* *[Summary]* :: A /library/ Beginning point for development of new ICM oriented libraries.
"""

import typing

icmInfo: typing.Dict[str, typing.Any] = { 'moduleDescription': ["""
*       [[elisp:(org-show-subtree)][|=]]  [[elisp:(org-cycle)][| *Description:* | ]]
**  [[elisp:(org-cycle)][| ]]  [Xref]          :: *[Related/Xrefs:]*  <<Xref-Here->>  -- External Documents  [[elisp:(org-cycle)][| ]]

**  [[elisp:(org-cycle)][| ]]   Model and Terminology                                      :Overview:
*** concept             -- Desctiption of concept
**      [End-Of-Description]
"""], }

icmInfo['moduleUsage'] = """
*       [[elisp:(org-show-subtree)][|=]]  [[elisp:(org-cycle)][| *Usage:* | ]]

**      How-Tos:
**      [End-Of-Usage]
"""

icmInfo['moduleStatus'] = """
*       [[elisp:(org-show-subtree)][|=]]  [[elisp:(org-cycle)][| *Status:* | ]]
**  [[elisp:(org-cycle)][| ]]  [Info]          :: *[Current-Info:]* Status/Maintenance -- General TODO List [[elisp:(org-cycle)][| ]]
** TODO [[elisp:(org-cycle)][| ]]  Current         :: Just getting started [[elisp:(org-cycle)][| ]]
**      [End-Of-Status]
"""

"""
*  [[elisp:(org-cycle)][| *ICM-INFO:* |]] :: Author, Copyleft and Version Information
"""
####+BEGIN: bx:icm:py:name :style "fileName"
icmInfo['moduleName'] = "aaisBpo"
####+END:

####+BEGIN: bx:icm:py:version-timestamp :style "date"
icmInfo['version'] = "202109271806"
####+END:

####+BEGIN: bx:icm:py:status :status "Production"
icmInfo['status']  = "Production"
####+END:

icmInfo['credits'] = ""

####+BEGIN: bx:dblock:global:file-insert-cond :cond "./blee.el" :file "/bisos/apps/defaults/update/sw/icm/py/icmInfo-mbNedaGplByStar.py"
icmInfo['authors'] = "[[http://mohsen.1.banan.byname.net][Mohsen Banan]]"
icmInfo['copyright'] = "Copyright 2017, [[http://www.neda.com][Neda Communications, Inc.]]"
icmInfo['licenses'] = "[[https://www.gnu.org/licenses/agpl-3.0.en.html][Affero GPL]]", "Libre-Halaal Services License", "Neda Commercial License"
icmInfo['maintainers'] = "[[http://mohsen.1.banan.byname.net][Mohsen Banan]]"
icmInfo['contacts'] = "[[http://mohsen.1.banan.byname.net/contact]]"
icmInfo['partOf'] = "[[http://www.by-star.net][Libre-Halaal ByStar Digital Ecosystem]]"
####+END:

icmInfo['panel'] = "{}-Panel.org".format(icmInfo['moduleName'])
icmInfo['groupingType'] = "IcmGroupingType-pkged"
icmInfo['cmndParts'] = "IcmCmndParts[common] IcmCmndParts[param]"


####+BEGIN: bx:icm:python:top-of-file :partof "bystar" :copyleft "halaal+minimal"
"""
*  This file:/bisos/git/auth/bxRepos/bisos-pip/aais/py3/bisos/aais/aaisBpo.py :: [[elisp:(org-cycle)][| ]]
 is part of The Libre-Halaal ByStar Digital Ecosystem. http://www.by-star.net
 *CopyLeft*  This Software is a Libre-Halaal Poly-Existential. See http://www.freeprotocols.org
 A Python Interactively Command Module (PyICM).
 Best Developed With COMEEGA-Emacs And Best Used With Blee-ICM-Players.
 *WARNING*: All edits wityhin Dynamic Blocks may be lost.
"""
####+END:

####+BEGIN: bx:icm:python:topControls :partof "bystar" :copyleft "halaal+minimal"
"""
*  [[elisp:(org-cycle)][|/Controls/| ]] :: [[elisp:(org-show-subtree)][|=]]  [[elisp:(show-all)][Show-All]]  [[elisp:(org-shifttab)][Overview]]  [[elisp:(progn (org-shifttab) (org-content))][Content]] | [[file:Panel.org][Panel]] | [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] | [[elisp:(bx:org:run-me)][Run]] | [[elisp:(bx:org:run-me-eml)][RunEml]] | [[elisp:(delete-other-windows)][(1)]] | [[elisp:(progn (save-buffer) (kill-buffer))][S&Q]]  [[elisp:(save-buffer)][Save]]  [[elisp:(kill-buffer)][Quit]] [[elisp:(org-cycle)][| ]]
** /Version Control/ ::  [[elisp:(call-interactively (quote cvs-update))][cvs-update]]  [[elisp:(vc-update)][vc-update]] | [[elisp:(bx:org:agenda:this-file-otherWin)][Agenda-List]]  [[elisp:(bx:org:todo:this-file-otherWin)][ToDo-List]]
"""
####+END:
####+BEGIN: bx:dblock:global:file-insert-cond :cond "./blee.el" :file "/bisos/apps/defaults/software/plusOrg/dblock/inserts/pyWorkBench.org"
"""
*  /Python Workbench/ ::  [[elisp:(org-cycle)][| ]]  [[elisp:(python-check (format "/bisos/venv/py3/bisos3/bin/python -m pyclbr %s" (bx:buf-fname))))][pyclbr]] || [[elisp:(python-check (format "/bisos/venv/py3/bisos3/bin/python -m pydoc ./%s" (bx:buf-fname))))][pydoc]] || [[elisp:(python-check (format "/bisos/pipx/bin/pyflakes %s" (bx:buf-fname)))][pyflakes]] | [[elisp:(python-check (format "/bisos/pipx/bin/pychecker %s" (bx:buf-fname))))][pychecker (executes)]] | [[elisp:(python-check (format "/bisos/pipx/bin/pycodestyle %s" (bx:buf-fname))))][pycodestyle]] | [[elisp:(python-check (format "/bisos/pipx/bin/flake8 %s" (bx:buf-fname))))][flake8]] | [[elisp:(python-check (format "/bisos/pipx/bin/pylint %s" (bx:buf-fname))))][pylint]]  [[elisp:(org-cycle)][| ]]
"""
####+END:

####+BEGIN: bx:icm:python:icmItem :itemType "=Imports=" :itemTitle "*IMPORTS*"
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  =Imports=  :: *IMPORTS*  [[elisp:(org-cycle)][| ]]
"""
####+END:


import os
# import pwd
# import grp
import collections
# import enum

####+BEGIN: bx:dblock:global:file-insert-cond :cond "./blee.el" :file "/bisos/apps/defaults/update/sw/icm/py/importUcfIcmG.py"
from unisos import ucf
from unisos import icm

icm.unusedSuppressForEval(ucf.__file__)  # in case icm and ucf are not used

G = icm.IcmGlobalContext()
# G.icmLibsAppend = __file__
# G.icmCmndsLibsAppend = __file__
####+END:

from bisos.platform import bxPlatformConfig
# from bisos.platform import bxPlatformThis

from bisos.bpo import bpo
# from bisos.aais import aaisBpo

####+BEGIN: bx:dblock:python:section :title "Start Your Sections Here"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ############## [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *Start Your Sections Here*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]]
"""
####+END:

####+BEGIN: bx:dblock:python:func :funcName "si_svcName" :funcType "Obtain" :retType "str" :deco "" :argsList "si"
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Func-Obtain :: /si_svcName/ retType=str argsList=(si)  [[elisp:(org-cycle)][| ]]
"""
def si_svcName(
    si,
):
####+END:
    """
**
"""
    siList = si.split('/')
    return siList[0]

####+BEGIN: bx:dblock:python:func :funcName "si_instanceName" :funcType "Obtain" :retType "str" :deco "" :argsList "si"
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Func-Obtain :: /si_instanceName/ retType=str argsList=(si)  [[elisp:(org-cycle)][| ]]
"""
def si_instanceName(
    si,
):
####+END:
    """
**
"""
    siList = si.split('/')
    return siList[-1]

####+BEGIN: bx:dblock:python:func :funcName "si_virDomSvcName" :funcType "Obtain" :retType "str" :deco "" :argsList "si"
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Func-Obtain :: /si_virDomSvcName/ retType=str argsList=(si)  [[elisp:(org-cycle)][| ]]
"""
def si_virDomSvcName(
    si,
):
####+END:
    """
**
"""
    siList = si.split('/')
    virDomName = siList[1]
    if virDomName == si_instanceName(si):
        return ""
    else:
        return virDomName

####+BEGIN: bx:dblock:python:func :funcName "si_svcBaseDir" :funcType "Obtain" :retType "str" :deco "" :argsList "bpoId si"
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Func-Obtain :: /si_svcBaseDir/ retType=str argsList=(bpoId si)  [[elisp:(org-cycle)][| ]]
"""
def si_svcBaseDir(
    bpoId,
    si,
):
####+END:
    """
**
"""
    bpoBaseDir = bpo.bpoBaseDir_obtain(bpoId)
    siServiceName = si_svcName(si)
    return (
        os.path.join(
            bpoBaseDir,
            format(f"si_{siServiceName}"),
        )
    )

####+BEGIN: bx:dblock:python:func :funcName "si_virDomSvcBaseDir" :funcType "Obtain" :retType "str" :deco "" :argsList "bpoId si"
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Func-Obtain :: /si_virDomSvcBaseDir/ retType=str argsList=(bpoId si)  [[elisp:(org-cycle)][| ]]
"""
def si_virDomSvcBaseDir(
    bpoId,
    si,
):
####+END:
    """
**
"""
    svcVirDomName = si_virDomSvcName(si)
    svcBaseDir = si_svcBaseDir(bpoId, si)
    return (
        os.path.join(
            svcBaseDir,
            svcVirDomName,
        )
    )



####+BEGIN: bx:dblock:python:func :funcName "si_instanceBaseDir" :funcType "Obtain" :retType "str" :deco "" :argsList "bpoId si"
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Func-Obtain :: /si_instanceBaseDir/ retType=str argsList=(bpoId si)  [[elisp:(org-cycle)][| ]]
"""
def si_instanceBaseDir(
    bpoId,
    si,
):
####+END:
    """
**
"""
    svcInstance = si_instanceName(si)
    svcVirDomName = si_virDomSvcName(si)
    if svcInstance == svcVirDomName:
        # Not a virDom
        svcBaseDir = si_svcBaseDir(bpoId, si)
        return (
            os.path.join(
                svcBaseDir,
                svcInstance,
            )
        )
    else:
        virDomSvcBaseDir = si_virDomSvcBaseDir(bpoId, si)
        return (
            os.path.join(
                virDomSvcBaseDir,
                svcInstance,
            )
        )


####+BEGIN: bx:dblock:python:func :funcName "si_primSvcBaseDir" :funcType "Obtain" :retType "str" :deco "" :argsList "bpoId si"
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Func-Obtain :: /si_primSvcBaseDir/ retType=str argsList=(bpoId si)  [[elisp:(org-cycle)][| ]]
"""
def si_primSvcBaseDir(
    bpoId,
    si,
):
####+END:
    """
**
"""
    bpoBaseDir = bpo.bpoBaseDir_obtain(bpoId)
    svcVirDomName = si_virDomSvcName(si)
    return (
        os.path.join(
            bpoBaseDir,
            format(f"si_{svcVirDomName}"),
        )
    )


####+BEGIN: bx:dblock:python:func :funcName "si_primInstanceBaseDir" :funcType "Obtain" :retType "str" :deco "" :argsList "bpoId si"
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Func-Obtain :: /si_primInstanceBaseDir/ retType=str argsList=(bpoId si)  [[elisp:(org-cycle)][| ]]
"""
def si_primInstanceBaseDir(
    bpoId,
    si,
):
####+END:
    """
**
"""
    svcInstance = si_instanceName(si)
    primSvcBaseDir = si_primSvcBaseDir(bpoId, si)

    return (
        os.path.join(
            primSvcBaseDir,
            svcInstance,
        )
    )

####+BEGIN: bx:dblock:python:func :funcName "siRootDir_obtain" :funcType "Obtain" :retType "str" :deco "" :argsList "bpoBaseDir"
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Func-Obtain :: /siRootDir_obtain/ retType=str argsList=(bpoBaseDir)  [[elisp:(org-cycle)][| ]]
"""
def siRootDir_obtain(
    bpoBaseDir,
):
####+END:
    """
**
"""
    return (
        os.path.join(
            bpoBaseDir,
            "so/r3/sr",
        )
    )


####+BEGIN: bx:dblock:python:func :funcName "siFullPathBaseDir_obtain" :funcType "Obtain" :retType "str" :deco "" :argsList "bpoId srRelPath"
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Func-Obtain :: /siFullPathBaseDir_obtain/ retType=str argsList=(bpoId srRelPath)  [[elisp:(org-cycle)][| ]]
"""
def siFullPathBaseDir_obtain(
    bpoId,
    siRelPath,
):
####+END:
    """
** Join dirs as expected.
"""
    return (
        os.path.join(
            siRootDir_obtain(
                bpo.bpoBaseDir_obtain(
                    bpoId
                )
            ),
            siRelPath,
        )
    )


####+BEGIN: bx:dblock:python:subSection :title "Bpo+Si Roots and InfoBases (Control/Input)"

####+END:



####+BEGIN: bx:dblock:python:func :funcName "bpbBisos_baseObtain_control" :comment "BISOS DATA" :funcType "obtain" :retType "bool" :deco "" :argsList "baseDir"
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Func-obtain :: /bpbBisos_baseObtain_control/ =BISOS DATA= retType=bool argsList=(baseDir)  [[elisp:(org-cycle)][| ]]
"""
def bpbBisos_baseObtain_control(
    baseDir,
):
####+END:
    # bxpRoot = "bxpRoot_baseObtain()"

    return( os.path.join(
        baseDir, "bisos", "input"
    ))


####+BEGIN: bx:dblock:python:subSection :title "Bpo+Sr RunTime  Bases"

####+END:

####+BEGIN: bx:dblock:python:func :funcName "bpoSi_runBaseObtain_root" :funcType "obtain" :retType "bool" :deco "" :argsList "bpoId si"
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Func-obtain :: /bpoSi_runBaseObtain_root/ retType=bool argsList=(bpoId si)  [[elisp:(org-cycle)][| ]]
"""
def bpoSi_runBaseObtain_root(
    bpoId,
    si,
):
####+END:
    icm.unusedSuppress(si)
    return(
        os.path.join(
            str(bxPlatformConfig.rootDir_deRun_fpObtain(configBaseDir=None,)),
            "bisos/r3/bpo",
            str(bpoId),
        )
    )



####+BEGIN: bx:dblock:python:func :funcName "bpoSi_runBaseObtain_var" :funcType "obtain" :retType "bool" :deco "" :argsList "bpoId si"
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Func-obtain :: /bpoSi_runBaseObtain_var/ retType=bool argsList=(bpoId si)  [[elisp:(org-cycle)][| ]]
"""
def bpoSi_runBaseObtain_var(
    bpoId,
    si,
):
####+END:
    return(
        os.path.join(
            bpoSi_runBaseObtain_root(
                bpoId,
                si,
            ),
            "var"
        )
    )

####+BEGIN: bx:dblock:python:func :funcName "bpoSi_runBaseObtain_tmp" :funcType "obtain" :retType "bool" :deco "" :argsList "bpoId si"
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Func-obtain :: /bpoSi_runBaseObtain_tmp/ retType=bool argsList=(bpoId si)  [[elisp:(org-cycle)][| ]]
"""
def bpoSi_runBaseObtain_tmp(
    bpoId,
    si,
):
####+END:
    return(
        os.path.join(
            bpoSi_runBaseObtain_root(
                bpoId,
                si,
            ),
            "tmp"
        )
    )

####+BEGIN: bx:dblock:python:func :funcName "bpoSi_runBaseObtain_log" :funcType "obtain" :retType "bool" :deco "" :argsList "bpoId si"
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Func-obtain :: /bpoSi_runBaseObtain_log/ retType=bool argsList=(bpoId si)  [[elisp:(org-cycle)][| ]]
"""
def bpoSi_runBaseObtain_log(
    bpoId,
    si,
):
####+END:
    return(
        os.path.join(
            bpoSi_runBaseObtain_root(
                bpoId,
                si,
            ),
            "log"
        )
    )

####+BEGIN: bx:dblock:python:section :title "Class Definitions"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ############## [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *Class Definitions*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]]
"""
####+END:


####+BEGIN: bx:icm:python:func :funcName "obtainBpo" :funcType "anyOrNone" :retType "bool" :deco "" :argsList "bpoId"
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Func-anyOrNone :: /obtainBpo/ retType=bool argsList=(bpoId)  [[elisp:(org-cycle)][| ]]
"""
def obtainBpo(
    bpoId,
):
####+END:
    return bpo.EffectiveBpos.givenBpoIdObtainBpo(bpoId, AaisBpo)


####+BEGIN: bx:dblock:python:class :className "AaisBpo" :superClass "bpo.Bpo" :comment "Expected to be subclassed" :classType "basic"
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Class-basic :: /AaisBpo/ bpo.Bpo =Expected to be subclassed=  [[elisp:(org-cycle)][| ]]
"""
class AaisBpo(bpo.Bpo):
####+END:
    """
** Abstraction of the base ByStar Portable Object
"""

    def __init__(
            self,
            bpoId,
    ):
        '''Constructor'''
        if bpo.EffectiveBpos.givenBpoIdGetBpoOrNone(bpoId):
            icm.EH_critical_usageError(f"Duplicate Attempt At Singleton Creation bpoId={bpoId}")
        else:
            bpo.EffectiveBpos.addBpo(bpoId, self)

        super().__init__(bpoId)

        self.effectiveSisList = {}

        self.basesObj = AaisBases(bpoId)
        self.basesObj.aais_bases_update()

        self.repo_live = AaisRepo_Live(bpoId)

        self.sivdApache2Repo = A2SivdRepo(bpoId)


        self.siGeneweb = {}
        self.bpoId = bpoId

    def activate(
            self,
            si,
    ):
        """When si is blank, activate the whole BPO. Otherwise just the specified bpo.

        """
        print(self.baseDir)
        print(si)


####+BEGIN: bx:dblock:python:class :className "AaisBases" :superClass "bpo.BpoBases" :comment "Expected to be subclassed" :classType "basic"
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Class-basic :: /AaisBases/ bpo.BpoBases =Expected to be subclassed=  [[elisp:(org-cycle)][| ]]
"""
class AaisBases(bpo.BpoBases):
####+END:
    """
** Abstraction of the base ByStar Portable Object
"""
    def __init__(
            self,
            bpoId,
    ):
        super().__init__(bpoId)
        if not bpo.EffectiveBpos.givenBpoIdGetBpo(bpoId):
            icm.EH_critical_usageError(f"Missing BPO for {bpoId}")
            return

    def aais_bases_update(self,):
        """Extra aais bases."""
        self.bases_update()
        return

    def logBase_update(self,):
        return "NOTYET"

    def logBase_obtain(self,):
        return os.path.join(self.bpo.baseDir, "log") # type: ignore


####+BEGIN: bx:dblock:python:class :className "AaisRepo_Live" :superClass "bpo.BpoRepo" :comment "Expected to be subclassed" :classType "basic"
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Class-basic :: /AaisRepo_Live/ bpo.BpoRepo =Expected to be subclassed=  [[elisp:(org-cycle)][| ]]
"""
class AaisRepo_Live(bpo.BpoRepo):
####+END:
    """
** Abstraction of the base ByStar Portable Object
"""
    def __init__(
            self,
            bpoId,
    ):
        super().__init__(bpoId)
        if not bpo.EffectiveBpos.givenBpoIdGetBpo(bpoId):
            icm.EH_critical_usageError(f"Missing BPO for {bpoId}")
            return

    def info(self,):
        print(f"AaisRepo_Live {self.bpo.bpoId}")

    def obtainFromFPs(self,):
        pass

    def update(
            self,
            containerBpoId,
            ipAddr
    ):
        self.containerBpoId = containerBpoId
        self.ipAddr = ipAddr


####+BEGIN: bx:dblock:python:class :className "AaSivdRepo" :superClass "bpo.BpoRepo" :comment "Expected to be subclassed" :classType "basic"
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Class-basic :: /AaSivdRepo/ bpo.BpoRepo =Expected to be subclassed=  [[elisp:(org-cycle)][| ]]
"""
class A2SivdRepo(bpo.BpoRepo):
####+END:
    """
** Refers to the entirety of bpo/apache2 repo.
"""
    def __init__(
            self,
            bpoId,
    ):
        super().__init__(bpoId)
        if not bpo.EffectiveBpos.givenBpoIdGetBpo(bpoId):
            icm.EH_critical_usageError(f"Missing BPO for {bpoId}")
            return

    def repoBase(self,):
        return os.path.join(self.bpo.baseDir, "apache2") # type: ignore


####+BEGIN: bx:dblock:python:class :className " A2SivdBase_Plone3" :superClass "object" :comment "Expected to be subclassed" :classType "basic"
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Class-basic :: / A2SivdBase_Plone3/ object =Expected to be subclassed=  [[elisp:(org-cycle)][| ]]
"""
class  A2SivdBase_Plone3(object):
####+END:
    """
** Abstraction of the base ByStar Portable Object
"""
    def __init__(
            self,
            bpoId,
    ):
        super().__init__(bpoId)
        if not bpo.EffectiveBpos.givenBpoIdGetBpo(bpoId):
            icm.EH_critical_usageError(f"Missing BPO for {bpoId}")
            return


####+BEGIN: bx:dblock:python:class :className "EffectiveSis" :superClass "object" :comment "" :classType "basic"
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Class-basic :: /EffectiveSis/ object  [[elisp:(org-cycle)][| ]]
"""
class EffectiveSis(object):
####+END:
    """
** Only one instance is created for a given BpoId and an SiId.
"""

    @staticmethod
    def addSi(
            bpoId,
            siId,
            siObj
    ):
        print(f"Adding bpoId={bpoId} siId={siId} siObj={siObj}")
        thisBpo = obtainBpo(bpoId,)
        if not thisBpo:
            return None
        thisBpo.effectiveSisList.update({siId: siObj})


    @staticmethod
    def givenSiIdObtainSiObj(
            bpoId,
            siId,
            SiClass,
    ):
        """Returns and siObj."""
        thisBpo = obtainBpo(bpoId,)
        if not thisBpo:
            return None

        if siId in thisBpo.effectiveSisList:
            return thisBpo.effectiveSisList[siId]
        else:
            return SiClass(siId, siId)

    @staticmethod
    def givenSiIdFindSiObj(
            bpoId,
            siId,
    ):
        """Should really not fail."""
        thisBpo = obtainBpo(bpoId,)
        if not thisBpo:
            return None

        if siId in thisBpo.effectiveSisList:
            return thisBpo.effectiveSisList[siId]
        else:
            icm.EH_problem_usageError("")
            return None

    @staticmethod
    def givenSiIdGetSiObjOrNone(
            bpoId,
            siId,
    ):
        """Expected to perhaps fail."""
        thisBpo = obtainBpo(bpoId,)
        if not thisBpo:
            return None

        if siId in thisBpo.effectiveSisList:
            return thisBpo.effectiveSisList[siId]
        else:
            return None


####+BEGIN: bx:icm:python:func :funcName "obtainBpo" :funcType "anyOrNone" :retType "bool" :deco "" :argsList "bpoId"
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Func-anyOrNone :: /obtainBpo/ retType=bool argsList=(bpoId)  [[elisp:(org-cycle)][| ]]
"""
def obtainSiObj(
        bpoId,
        siId,
):
####+END:
    return EffectiveBpos.givenSiIdObtainSiObj(bpoId, siId, siObj)


####+BEGIN: bx:dblock:python:class :className "AaSiRepo" :superClass "bpo.BpoRepo" :comment "Expected to be subclassed" :classType "basic"
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Class-basic :: /AaSiRepo/ bpo.BpoRepo =Expected to be subclassed=  [[elisp:(org-cycle)][| ]]
"""
class SiRepo(bpo.BpoRepo):
####+END:
    """
** Abstraction of the base ByStar Portable Object
"""

    def __init__(
        self,
    ):
        pass

    def obtainFromFPs(self,):
        pass




####+BEGIN: bx:dblock:python:section :title "Common Parameters Specification"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ############## [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *Common Parameters Specification*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]]
"""
####+END:


####+BEGIN: bx:dblock:python:func :funcName "commonParamsSpecify" :funcType "ParSpec" :retType "" :deco "" :argsList "icmParams"
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Func-ParSpec :: /commonParamsSpecify/ retType= argsList=(icmParams)  [[elisp:(org-cycle)][| ]]
"""
def commonParamsSpecify(
    icmParams,
):
####+END:
    icmParams.parDictAdd(
        parName='si',
        parDescription="Service Instances Relative Path (plone3/main)",
        parDataType=None,
        parDefault=None,
        parChoices=["any"],
        # parScope=icm.ICM_ParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--si',
    )


####+BEGIN: bx:dblock:python:section :title "Common Examples Sections"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ############## [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *Common Examples Sections*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]]
"""
####+END:


####+BEGIN: bx:dblock:python:func :funcName "examples_aaBpo_basicAccess" :comment "Show/Verify/Update For relevant PBDs" :funcType "examples" :retType "none" :deco "" :argsList ""
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Func-examples :: /examples_aaBpo_basicAccess/ =Show/Verify/Update For relevant PBDs= retType=none argsList=nil  [[elisp:(org-cycle)][| ]]
"""
def examples_aaBpo_basicAccess():
####+END:
    """
** Common examples.
"""
    def cpsInit(): return collections.OrderedDict()
    def menuItem(verbosity): icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity=verbosity) # 'little' or 'none'
    # def execLineEx(cmndStr): icm.ex_gExecMenuItem(execLine=cmndStr)

    oneBpo = "pmi_ByD-100001"
    oneSiRelPath = "plone3/main"

    # def moduleOverviewMenuItem(overviewCmndName):
    #     icm.cmndExampleMenuChapter('* =Module=  Overview (desc, usage, status)')
    #     cmndName = "overview_bxpBaseDir" ; cmndArgs = "moduleDescription moduleUsage moduleStatus" ;
    #     cps = collections.OrderedDict()
    #     icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='none') # 'little' or 'none'

    # moduleOverviewMenuItem(bpo_libOverview)

    icm.cmndExampleMenuChapter(' =Bpo+Sr ZZZ Info Base Roots=  *bpoSi Control Roots*')

    cmndName = "bpoSiFullPathBaseDir" ; cmndArgs = "" ;
    cps=cpsInit() ; cps['bpoId'] = oneBpo ; cps['si'] = oneSiRelPath
    menuItem(verbosity='little')


    icm.cmndExampleMenuChapter(' =Bpo+Sr Info Base Roots=  *bpoSi Control Roots*')

    cmndName = "bpoSiRunRootBaseDir" ; cmndArgs = "" ;
    cps=cpsInit() ; cps['bpoId'] = oneBpo ; cps['si'] = oneSiRelPath
    menuItem(verbosity='little')

    cmndName = "bpoSiRunRootBaseDir" ; cmndArgs = "all" ;
    cps=cpsInit() ; cps['bpoId'] = oneBpo ; cps['si'] = oneSiRelPath
    menuItem(verbosity='little')

    cmndName = "bpoSiRunRootBaseDir" ; cmndArgs = "var" ;
    cps=cpsInit() ; cps['bpoId'] = oneBpo ; cps['si'] = oneSiRelPath
    menuItem(verbosity='little')


####+BEGIN: bx:dblock:python:section :title "ICM Commands"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ############## [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *ICM Commands*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]]
"""
####+END:


####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "bpoSiFullPathBaseDir" :parsMand "bpoId si" :parsOpt "" :argsMin "0" :argsMax "0" :asFunc "" :interactiveP ""
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  ICM-Cmnd   :: /bpoSiFullPathBaseDir/ parsMand=bpoId si parsOpt= argsMin=0 argsMax=0 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class bpoSiFullPathBaseDir(icm.Cmnd):
    cmndParamsMandatory = [ 'bpoId', 'si', ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        bpoId=None,         # or Cmnd-Input
        si=None,         # or Cmnd-Input
    ):
        cmndOutcome = self.getOpOutcome()
        if interactive:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome

        callParamsDict = {'bpoId': bpoId, 'si': si, }
        if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome
        bpoId = callParamsDict['bpoId']
        si = callParamsDict['si']

####+END:
        retVal = siFullPathBaseDir_obtain(
            bpoId=bpoId,
            siRelPath=si,
        )

        if interactive:
            icm.ANN_write("{}".format(retVal))

        return cmndOutcome.set(
            opError=icm.notAsFailure(retVal),
            opResults=retVal,
        )

####+BEGIN: bx:icm:python:method :methodName "cmndDocStr" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList ""
    """
**  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Method-anyOrNone :: /cmndDocStr/ retType=bool argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
"""
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndDocStr(self):
####+END:
        return """
***** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Returns the full path of the Sr baseDir.
"""


####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "bpoSiRunRootBaseDir" :parsMand "bpoId si" :parsOpt "" :argsMin "0" :argsMax "3" :asFunc "" :interactiveP ""
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  ICM-Cmnd   :: /bpoSiRunRootBaseDir/ parsMand=bpoId si parsOpt= argsMin=0 argsMax=3 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class bpoSiRunRootBaseDir(icm.Cmnd):
    cmndParamsMandatory = [ 'bpoId', 'si', ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 3,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        bpoId=None,         # or Cmnd-Input
        si=None,         # or Cmnd-Input
        argsList=[],         # or Args-Input
    ):
        cmndOutcome = self.getOpOutcome()
        if interactive:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome
            effectiveArgsList = G.icmRunArgsGet().cmndArgs  # type: ignore
        else:
            effectiveArgsList = argsList

        callParamsDict = {'bpoId': bpoId, 'si': si, }
        if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome
        bpoId = callParamsDict['bpoId']
        si = callParamsDict['si']

        cmndArgsSpecDict = self.cmndArgsSpec()
        if not self.cmndArgsValidate(effectiveArgsList, cmndArgsSpecDict, outcome=cmndOutcome):
            return cmndOutcome
####+END:

        cmndArgs = list(self.cmndArgsGet("0&2", cmndArgsSpecDict, effectiveArgsList)) # type: ignore

        if len(cmndArgs):
            if cmndArgs[0] == "all":
                cmndArgsSpec = cmndArgsSpecDict.argPositionFind("0&2")
                argChoices = cmndArgsSpec.argChoicesGet()
                argChoices.pop(0)
                cmndArgs= argChoices

        retVal = bpoSi_runBaseObtain_root(
            bpoId=bpoId,
            si=si,
        )

        if interactive:
            icm.ANN_write("{}".format(retVal))
            for each in cmndArgs:
                if each == "var":
                    icm.ANN_write("{each}".format(each=bpoSi_runBaseObtain_var(bpoId, si)))
                elif each == "tmp":
                    icm.ANN_write("{each}".format(each=bpoSi_runBaseObtain_tmp(bpoId, si)))
                elif each == "log":
                    icm.ANN_write("{each}".format(each=bpoSi_runBaseObtain_log(bpoId, si)))
                else:
                    icm.EH_problem_usageError("")

        return cmndOutcome.set(
            opError=icm.notAsFailure(retVal),
            opResults=retVal,
        )

####+BEGIN: bx:icm:python:method :methodName "cmndArgsSpec" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList ""
    """
**  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Method-anyOrNone :: /cmndArgsSpec/ retType=bool argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
"""
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndArgsSpec(self):
####+END:
        """
***** Cmnd Args Specification
"""
        cmndArgsSpecDict = icm.CmndArgsSpecDict()

        cmndArgsSpecDict.argsDictAdd(
            argPosition="0&2",
            argName="cmndArgs",
            argDefault=None,
            argChoices=['all', 'var', 'tmp', 'log',],
            argDescription="Rest of args for use by action"
        )

        return cmndArgsSpecDict

    
####+BEGIN: bx:icm:python:method :methodName "cmndDocStr" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList ""
    """
**  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Method-anyOrNone :: /cmndDocStr/ retType=bool argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
"""
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndDocStr(self):
####+END:
        return """
***** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Returns the full path of the Sr baseDir.
"""



####+BEGIN: bx:icm:python:section :title "End Of Editable Text"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ############## [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *End Of Editable Text*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]]
"""
####+END:

####+BEGIN: bx:dblock:global:file-insert-cond :cond "./blee.el" :file "/bisos/apps/defaults/software/plusOrg/dblock/inserts/endOfFileControls.org"
#+STARTUP: showall
####+END:
