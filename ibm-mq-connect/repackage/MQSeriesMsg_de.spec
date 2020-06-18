Summary: IBM MQ Messages (German) FileSet
Name: MQSeriesMsg_de
Version: 9.1.2
Release: 0
License: Commercial
ExclusiveArch: x86_64
Group: Applications/Networking
AutoReqProv: no
Vendor: IBM
Prefix: /opt/mqm
Requires: MQSeriesRuntime = 9.1.2-0
%define _source_filedigest_algorithm md5
%define _binary_filedigest_algorithm md5
%define _source_payload w7.lzdio
%define _binary_payload w7.lzdio
%global __strip /bin/true
%global _rpmdir /build/slot1/p910_P/inst.images/amd64_linux_2/images/
%global _tmppath /build/slot1/p910_P/obj/amd64_linux_2/install/unix/linux_2
BuildRoot: /build/slot1/p910_P/obj/amd64_linux_2/ship

%description
IBM MQ  for Linux for x86_64 
5724-H72 
This package provides the IBM MQ message catalog for the German language.
%clean
rm -rf $RPM_BUILD_ROOT

%install
install -d $RPM_BUILD_ROOT/opt/mqm
install -d $RPM_BUILD_ROOT/opt/mqm/swidtag
install -d $RPM_BUILD_ROOT/opt/mqm/msg
install -d $RPM_BUILD_ROOT/opt/mqm/msg/de_DE
install /build/slot1/p910_P/obj/amd64_linux_2/ship/opt/mqm/swidtag/IBM_MQ_Messages_German-9.1.2.mqtag $RPM_BUILD_ROOT/opt/mqm/swidtag/IBM_MQ_Messages_German-9.1.2.mqtag
install /build/slot1/p910_P/obj/amd64_linux_2/ship/opt/mqm/msg/de_DE/amq.cat $RPM_BUILD_ROOT/opt/mqm/msg/de_DE/amq.cat

%files
%dir %attr(555,mqm,mqm) "/opt/mqm"
%dir %attr(555,mqm,mqm) "/opt/mqm/swidtag"
%dir %attr(555,mqm,mqm) "/opt/mqm/msg"
%dir %attr(555,mqm,mqm) "/opt/mqm/msg/de_DE"
%attr(444,mqm,mqm) "/opt/mqm/swidtag/IBM_MQ_Messages_German-9.1.2.mqtag"
%attr(444,mqm,mqm) "/opt/mqm/msg/de_DE/amq.cat"

%pre
RPM_PACKAGE_SUMMARY="IBM MQ Messages (German) FileSet"
RPM_PACKAGE_NAME="MQSeriesMsg_de"
RPM_PACKAGE_VERSION="9.1.2"
RPM_PACKAGE_RELEASE="0"
PACKAGEPLATFORMS="x86_64"
PACKAGE_SUFFIX=
ADVANCEDPACKAGELIST="MQSeriesFTService 	MQSeriesAMS 	MQSeriesRDQM 	MQSeriesXRService"
MQ_DEFAULT_INSTALLATION_PATH=/opt/mqm
if [ -z "${RPM_INSTALL_PREFIX}" ] ; then 
  MQ_INSTALLATION_PATH=${MQ_DEFAULT_INSTALLATION_PATH}
else
  MQ_INSTALLATION_PATH=`echo "${RPM_INSTALL_PREFIX}" | sed s#//#/#g`
fi
MQ_RUNSCRIPT=
xtrace_switch=`set -o | grep xtrace | awk '{print $NF}'`
if [ ${xtrace_switch} = "on" ] ; then 
  env | sort
  uname -a
  id
  MQ_RUNSCRIPT="sh -x"
fi

# @(#) MQMBID sn=p912-L190308 su=_o4gl9UGHEemzP9qe_wddSA pn=install/unix/linux_2/preinstall.sh
#   <copyright
#   notice="lm-source-program"
#   pids="5724-H72"
#   years="2005,2018"
#   crc="3530070126" >
#   Licensed Materials - Property of IBM
#
#   5724-H72
#
#   (C) Copyright IBM Corp. 2005, 2018 All Rights Reserved.
#
#   US Government Users Restricted Rights - Use, duplication or
#   disclosure restricted by GSA ADP Schedule Contract with
#   IBM Corp.
#   </copyright>
#
# Common Preinstallation script for all packages
#
# Check that this package is not being installed to a location where
# a different VR exists
#
#######################################################################################################
# Check the install path does not exceed the MQ maximum length of 256
#######################################################################################################
if [ ${#MQ_INSTALLATION_PATH} -gt 256 ]; then
  echo ""
  echo "ERROR:   Specified installation path (${MQ_INSTALLATION_PATH}) exceeds MQ maximum length of 256"
  echo ""
  exit 1
fi

#######################################################################################################
# Check the install path does not contain unsupported charaters
#######################################################################################################
echo "${MQ_INSTALLATION_PATH}" | grep "[:%# ]" > /dev/null
if [ $? -eq 0 ] ; then
  echo ""
  echo "ERROR:   Specified installation path (${MQ_INSTALLATION_PATH}) contains an unsupported character"
  echo ""
  exit 1
fi
# Trailing blanks
echo "${MQ_INSTALLATION_PATH}" | grep "\ $" > /dev/null
if [ $? -eq 0 ] ; then
  echo ""
  echo "ERROR:   Specified installation path (${MQ_INSTALLATION_PATH}) contains an unsupported character"
  echo ""
  exit 1
fi

#######################################################################################################
# Starting with 9.1 fail the install if doing rpm install on Ubuntu
#######################################################################################################
Ubuntu=no
command=`basename $(ls -l /proc/${PPID}/exe | awk '{print $NF}')`
if [ ${command} = 'rpm' ] ; then 
  if [ -x /usr/bin/lsb_release ] 
  then
    lsb_release_out=`/usr/bin/lsb_release -s -i | grep -i ubuntu` 
    if [ ${?} -eq 0 ] ; then 
      Ubuntu=yes
    fi
  else if [ -e /etc/os-release ] 
    then 
      .  /etc/os-release
      if [ ${ID} = 'ubuntu' ] 
      then 
        Ubuntu=yes
      fi
    else
      uname_out=`uname -a | grep -i ubuntu`
        if [ ${?} -eq 0 ]  ; then 
          Ubuntu=yes
        fi
    fi
  fi
  
  if [ ${Ubuntu} = 'yes' ]
  then  
     echo ""
     echo "ERROR:   Use of rpm to install ${RPM_PACKAGE_NAME} on the Ubuntu distribution is no longer supported"
     echo "         Installation terminated"
     echo ""
     exit 255
  fi
fi

#######################################################################################################
# Runtime checks
#######################################################################################################
echo ${RPM_PACKAGE_NAME} | grep  "MQSeriesRuntime" > /dev/null
if [ $? -eq 0 ] ; then
  #####################################################################################################
  # Check that the install path is empty
  # ignore lost+found and .snapshots(GPFS) directories
  # The .snapshots directory can also be renamed within GPFS, so we allow an alternate name to be specified with
  # AMQ_IGNORE_SNAPDIRNAME
  #####################################################################################################
  if [ x${AMQ_OVERRIDE_EMPTY_INSTALL_PATH} = x ] ;then
    if [ -d ${MQ_INSTALLATION_PATH} ] && [ ${MQ_INSTALLATION_PATH} != ${MQ_DEFAULT_INSTALLATION_PATH} ] ; then
      if [ "${AMQ_IGNORE_SNAPDIRNAME}" = "" ] ; then
        SNAPDIR_NAME=".snapshots"
      else
        SNAPDIR_NAME="${AMQ_IGNORE_SNAPDIRNAME}"
      fi
      LS_ALL=`ls -A ${MQ_INSTALLATION_PATH} 2>/dev/null | grep -F -v "lost+found" | grep -F -v "${SNAPDIR_NAME}"`
      if [ "${LS_ALL}" ] ; then
        echo ""
        echo "ERROR:   Specified installation path '${MQ_INSTALLATION_PATH}' is not empty"
        echo ""
        exit 1
     fi
    fi
  fi
#######################################################################################################
# Non Runtime checks
#######################################################################################################
else
  #####################################################################################################
  # Check the version/release of the product already at MQ_INSTALLATION_PATH is the same as this one
  #####################################################################################################
  if [ -x ${MQ_INSTALLATION_PATH}/bin/dspmqver ] ; then
    INSTALLED_VR=$(${MQ_INSTALLATION_PATH}/bin/dspmqver -f2 -b | awk -F. '{print $1 "." $2}')
    PACKAGE_VR=`echo ${RPM_PACKAGE_VERSION} | awk -F. '{print $1 "." $2}'`
    if [ ${INSTALLED_VR} != ${PACKAGE_VR} ] ; then
      echo ""
      echo "ERROR:   This package is not applicable to the MQ installation at ${MQ_INSTALLATION_PATH}"
      echo ""
      exit 1
    fi
  else
    echo ""
    echo "ERROR:   There is no MQSeriesRuntime installed at ${MQ_INSTALLATION_PATH}"
    echo ""
    exit 1
  fi
fi
#######################################################################################################
# Preventing an installation over an existing installation
# Each component has a unique '.mqtag' file.  If this is already present on the filesystem at the
# installation location, then the component must already be installed to this location, so we should
# abort.
#######################################################################################################
case "${RPM_PACKAGE_NAME}" in
  MQSeriesAMS)
      compfile="IBM_MQ_Advanced_Message_Security_Component"
      ;;
  MQSeriesAMQP)
      compfile="IBM_MQ_AMQP_Service"
      ;;
  MQSeriesClient)
      compfile="IBM_MQ_Client"
      ;;
  MQSeriesExplorer)
      compfile="IBM_MQ_Explorer"
      ;;
  MQSeriesFTAgent)
      compfile="IBM_MQ_Managed_File_Transfer_Agent"
      ;;
  MQSeriesFTBase)
      compfile="IBM_MQ_Managed_File_Transfer_Base"
      ;;
  MQSeriesFTLogger)
      compfile="IBM_MQ_Managed_File_Transfer_Logger"
      ;;
  MQSeriesFTService)
      compfile="IBM_MQ_Managed_File_Transfer_Service"
      ;;
  MQSeriesFTTools)
      compfile="IBM_MQ_Managed_File_Transfer_Tools"
      ;;
  MQSeriesGSKit)
      compfile="IBM_MQ_GSKit"
      ;;
  MQSeriesJava)
      compfile="IBM_MQ_Java_Messaging"
      ;;
  MQSeriesJRE)
      compfile="IBM_MQ_JRE"
      ;;
  MQSeriesRDQM)
      compfile="IBM_MQ_RDQM"
      ;;
  MQSeriesMan)
      compfile="IBM_MQ_Man_Pages"
      ;;
  MQSeriesMsg_cs)
      compfile="IBM_MQ_Messages_Czech"
      ;;
  MQSeriesMsg_de)
      compfile="IBM_MQ_Messages_German"
      ;;
  MQSeriesMsg_es)
      compfile="IBM_MQ_Messages_Spanish"
      ;;
  MQSeriesMsg_fr)
      compfile="IBM_MQ_Messages_French"
      ;;
  MQSeriesMsg_hu)
      compfile="IBM_MQ_Messages_Hungarian"
      ;;
  MQSeriesMsg_it)
      compfile="IBM_MQ_Messages_Italian"
      ;;
  MQSeriesMsg_ja)
      compfile="IBM_MQ_Messages_Japanese"
      ;;
  MQSeriesMsg_ko)
      compfile="IBM_MQ_Messages_Korean"
      ;;
  MQSeriesMsg_pl)
      compfile="IBM_MQ_Messages_Polish"
      ;;
  MQSeriesMsg_pt)
      compfile="IBM_MQ_Messages_Brazilian_Portuguese"
      ;;
  MQSeriesMsg_ru)
      compfile="IBM_MQ_Messages_Russian"
      ;;
  MQSeriesMsg_Zh_CN)
      compfile="IBM_MQ_Messages_Chinese_Simplified"
      ;;
  MQSeriesMsg_Zh_TW)
      compfile="IBM_MQ_Messages_Chinese_Traditional"
      ;;
  MQSeriesRuntime)
      compfile="IBM_MQ_Runtime"
      ;;
  MQSeriesSamples)
      compfile="IBM_MQ_Samples"
      ;;
  MQSeriesSDK)
      compfile="IBM_MQ_SDK"
      ;;
  MQSeriesServer)
      compfile="IBM_MQ_Server"
      ;;
  MQSeriesXRService)
      compfile="IBM_MQ_Telemetry_Service"
      ;;
  MQSeriesWeb)
      compfile="IBM_MQ_WebUI"
      ;;
  MQSeriesSFBridge)
      compfile="IBM_MQ_SFBridge."
      ;;
  MQSeriesBCBridge)
      compfile="IBM_MQ_BCBridge."
      ;;
  *)
      echo "ERROR: Package name ${RPM_PACKAGE_NAME} not recognised, aborting installation."
      exit 1
      ;;
esac

#
# If the 'compfile' file is present, then the package is already installed on
# the system, and we abort the installation of this package.
#
if [ -d ${MQ_INSTALLATION_PATH}/swidtag ] ; then  
  ls ${MQ_INSTALLATION_PATH}/swidtag | grep ${compfile}
  if [ $? -eq 0  ]; then
    echo "ERROR:  The specified installation path (${MQ_INSTALLATION_PATH}) already"
    echo "        has this package installed."
    echo "        Aborting installation."
    exit 1
  fi
fi
if [ -d ${MQ_INSTALLATION_PATH}/properties/version ] ; then  
  ls ${MQ_INSTALLATION_PATH}/properties/version | grep ${compfile} 
  if [ $? -eq 0  ]; then
    echo "ERROR:  The specified installation path (${MQ_INSTALLATION_PATH}) already"
    echo "        has this package installed."
    echo "        Aborting installation."
    exit 1
  fi
fi

#   <copyright 
#   notice="lm-source-program" 
#   pids="5724-H72," 
#   years="2005,2017" 
#   crc="1114153681" > 
#   Licensed Materials - Property of IBM  
#    
#   5724-H72, 
#    
#   (C) Copyright IBM Corp. 2005, 2017 All Rights Reserved.  
#    
#   US Government Users Restricted Rights - Use, duplication or  
#   disclosure restricted by GSA ADP Schedule Contract with  
#   IBM Corp.  
#   </copyright> 
# Preinstallation script
# Check's to see if the license agreement has been accepted

if [ ! -r /tmp/mq_license_${RPM_PACKAGE_VERSION}/license/status.dat ] && [ ! -r "${MQ_INSTALLATION_PATH}/licenses/status.dat" ] ; then

    cat << +++EOM+++
ERROR:  Product cannot be installed until the license
        agreement has been accepted.
        Run the 'mqlicense' script, which is in the root
        directory of the install media, or see the
        installation instructions in the IBM 
        Knowledge Center for more information.
+++EOM+++

   exit 1
fi

echo > /dev/null 2>/dev/null

%post
RPM_PACKAGE_SUMMARY="IBM MQ Messages (German) FileSet"
RPM_PACKAGE_NAME="MQSeriesMsg_de"
RPM_PACKAGE_VERSION="9.1.2"
RPM_PACKAGE_RELEASE="0"
PACKAGEPLATFORMS="x86_64"
PACKAGE_SUFFIX=
ADVANCEDPACKAGELIST="MQSeriesFTService 	MQSeriesAMS 	MQSeriesRDQM 	MQSeriesXRService"
MQ_DEFAULT_INSTALLATION_PATH=/opt/mqm
if [ -z "${RPM_INSTALL_PREFIX}" ] ; then 
  MQ_INSTALLATION_PATH=${MQ_DEFAULT_INSTALLATION_PATH}
else
  MQ_INSTALLATION_PATH=`echo "${RPM_INSTALL_PREFIX}" | sed s#//#/#g`
fi
MQ_RUNSCRIPT=
xtrace_switch=`set -o | grep xtrace | awk '{print $NF}'`
if [ ${xtrace_switch} = "on" ] ; then 
  env | sort
  uname -a
  id
  MQ_RUNSCRIPT="sh -x"
fi
if [ ${MQ_INSTALLATION_PATH} !=  ${MQ_DEFAULT_INSTALLATION_PATH} ] ; then 
  if [ -x ${MQ_INSTALLATION_PATH}/bin/amqicrel ] ; then 
     ${MQ_RUNSCRIPT} ${MQ_INSTALLATION_PATH}/bin/amqicrel ${MQ_INSTALLATION_PATH} ${RPM_PACKAGE_NAME}${PACKAGE_SUFFIX}-${RPM_PACKAGE_VERSION}-${RPM_PACKAGE_RELEASE}
  fi
fi
# Insert code to copy the MQ Advanced swidtag if this package is part of MQ Advanced 
echo ${ADVANCEDPACKAGELIST} | grep ${RPM_PACKAGE_NAME} >/dev/null 2>&1 
if [ ${?} -eq 0 ] ; then 
  if [ -f ${MQ_INSTALLATION_PATH}/samp/ibm.com_IBM_MQ_Advanced-${RPM_PACKAGE_VERSION}.tag ] ; then 
    cp -fp ${MQ_INSTALLATION_PATH}/samp/ibm.com_IBM_MQ_Advanced-${RPM_PACKAGE_VERSION}.tag ${MQ_INSTALLATION_PATH}/swidtag/ibm.com_IBM_MQ_Advanced-${RPM_PACKAGE_VERSION}.swidtag 
  fi
fi

%preun
RPM_PACKAGE_SUMMARY="IBM MQ Messages (German) FileSet"
RPM_PACKAGE_NAME="MQSeriesMsg_de"
RPM_PACKAGE_VERSION="9.1.2"
RPM_PACKAGE_RELEASE="0"
PACKAGEPLATFORMS="x86_64"
PACKAGE_SUFFIX=
ADVANCEDPACKAGELIST="MQSeriesFTService 	MQSeriesAMS 	MQSeriesRDQM 	MQSeriesXRService"
MQ_DEFAULT_INSTALLATION_PATH=/opt/mqm
if [ -z "${RPM_INSTALL_PREFIX}" ] ; then 
  MQ_INSTALLATION_PATH=${MQ_DEFAULT_INSTALLATION_PATH}
else
  MQ_INSTALLATION_PATH=`echo "${RPM_INSTALL_PREFIX}" | sed s#//#/#g`
fi
MQ_RUNSCRIPT=
xtrace_switch=`set -o | grep xtrace | awk '{print $NF}'`
if [ ${xtrace_switch} = "on" ] ; then 
  env | sort
  uname -a
  id
  MQ_RUNSCRIPT="sh -x"
fi

#   <copyright 
#   notice="lm-source-program" 
#   pids="5724-H72" 
#   years="2005,2019" 
#   crc="122768040" > 
#   Licensed Materials - Property of IBM  
#    
#   5724-H72 
#    
#   (C) Copyright IBM Corp. 2005, 2019 All Rights Reserved.  
#    
#   US Government Users Restricted Rights - Use, duplication or  
#   disclosure restricted by GSA ADP Schedule Contract with  
#   IBM Corp.  
#   </copyright> 
#
# Pre-uninstallation script
# Checks for already running Q Managers, and if it finds one, stops the
# uninstall.

# If amqiclen exists (should do during uninstall) then run it to clean up
# IPCC resources. If amqiclen returns an error then a queue manager is still
# running so stop the uninstall.
export LANG=C
export LC_ALL=C

# There is a defect in some levels of rpm which causes the return code from the preun
# scriptlet to be ignored. For those levels of rpm we will attempt to shut down 
# running queue managers before proceeding 
Stop_QM='False' 
if [ -x /usr/bin/lsb_release ] ; then 
   Distribution=`/usr/bin/lsb_release -is` 
   Dist_Rel=`/usr/bin/lsb_release -rs`
   command=`basename $(ls -l /proc/${PPID}/exe | awk '{print $NF}')`
   if [ "${Distribution}" = 'Ubuntu' -a  "${Dist_Rel}" = '16.04' -a ${command} = 'rpm' ] ; then
      Stop_QM='True' 
   fi
fi

# We need the sg command to put root into the mqm  group if Q Managers are to be stopped
if [ ! -x /usr/bin/sg ] ; then 
  Stop_QM='False' 
fi

if [ -x ${MQ_INSTALLATION_PATH}/bin/amqiclen ] && [ -f /var/mqm/mqs.ini ]
then
    ${MQ_INSTALLATION_PATH}/bin/amqiclen -v -x > /tmp/amqiclen.$$.out 2>&1
    amqiclen_rc=$?
    if [ $amqiclen_rc -ne 0 ] 
    then
      if [ ${Stop_QM} = 'True' ] 
        then 
          echo " " >&2
          echo "WARNING: MQ shared resources associated with the installation at" >&2
          echo "         '${MQ_INSTALLATION_PATH}' are still in use." >&2
          echo "         Attempting to end queue managers" >&2
          ${MQ_INSTALLATION_PATH}/bin/amqiclen -v -x | grep QMGR | grep -w active | awk '{print $5}' | sed s#\'##g | while read QM 
	    do 
	      echo "         Stopping '${QM}'" >&2
              # Use 'sg' to force root into the mqm group for this command
              /usr/bin/sg mqm -c "${MQ_INSTALLATION_PATH}/bin/endmqm -i ${QM}" | while read line 
	      do 
	        echo "         " $line
	      done 
	    done 
          echo "         Uninstallation will continue" >&2
          echo " " >&2
        else 
          echo " " >&2
          echo "ERROR: MQ shared resources associated with the installation at" >&2
          echo "      '${MQ_INSTALLATION_PATH}' are still in use." >&2
          echo "       You must stop all MQ processing, including applications, Queue Managers" >&2 
          echo "       and Listeners before attempting to install, update or delete" >&2
          echo "       the MQ product." >&2
          echo " " >&2
          echo "       'amqiclen -v -x' return code was: '$amqiclen_rc', output was:" >&2
          cat /tmp/amqiclen.$$.out >&2
          echo " " >&2
          rm -f /tmp/amqiclen.$$.out
          exit 1
        fi
    fi
    rm -f /tmp/amqiclen.$$.out
fi 
#   <copyright 
#   notice="lm-source-program" 
#   pids="5724-H72," 
#   years="2005,2012" 
#   crc="1595222582" > 
#   Licensed Materials - Property of IBM  
#    
#   5724-H72, 
#    
#   (C) Copyright IBM Corp. 2005, 2012 All Rights Reserved.  
#    
#   US Government Users Restricted Rights - Use, duplication or  
#   disclosure restricted by GSA ADP Schedule Contract with  
#   IBM Corp.  
#   </copyright> 
#
# Pre-uninstallation check script for all components
# A check is performed to see if there are any fixpack filesets applied to
# the base component which is currently being uninstalled.  If the fixpack
# has been applied, the uninstallation of this component is aborted to prevent
# the situation where the base fileset has been uninstalled leaving an
# uninstallable fixpack.

FIXPACK_BACKUPDIR="${MQ_INSTALLATION_PATH}/maintenance"

unset fix_exists

fix_exists=$(find $FIXPACK_BACKUPDIR -type d -maxdepth 2 -print 2>/dev/null | \
while read directory ; do
  component=`basename $directory`
  if [ "$RPM_PACKAGE_NAME" = "$component" ]; then
    # safety check - are there actually files under this directory?
    num_files=`find "$directory" -type f -print 2>/dev/null | wc -l`
    if [ $num_files -gt 0 ]; then
      echo  $num_files
      exit
    fi
  fi
done
)
if [ ! -z $fix_exists ] ; then 
  echo "ERROR:  There appears to be a fixpack installed on this machine for this" >&2
  echo "        component." >&2
  echo "" >&2
  echo "        Please ensure you have removed all fixpacks for the ${RPM_PACKAGE_NAME}" >&2
  echo "        component before trying to remove this package." >&2
  echo "" >&2
  exit 1 
fi

# Removing product links

%postun
RPM_PACKAGE_SUMMARY="IBM MQ Messages (German) FileSet"
RPM_PACKAGE_NAME="MQSeriesMsg_de"
RPM_PACKAGE_VERSION="9.1.2"
RPM_PACKAGE_RELEASE="0"
PACKAGEPLATFORMS="x86_64"
PACKAGE_SUFFIX=
ADVANCEDPACKAGELIST="MQSeriesFTService 	MQSeriesAMS 	MQSeriesRDQM 	MQSeriesXRService"
MQ_DEFAULT_INSTALLATION_PATH=/opt/mqm
if [ -z "${RPM_INSTALL_PREFIX}" ] ; then 
  MQ_INSTALLATION_PATH=${MQ_DEFAULT_INSTALLATION_PATH}
else
  MQ_INSTALLATION_PATH=`echo "${RPM_INSTALL_PREFIX}" | sed s#//#/#g`
fi
MQ_RUNSCRIPT=
xtrace_switch=`set -o | grep xtrace | awk '{print $NF}'`
if [ ${xtrace_switch} = "on" ] ; then 
  env | sort
  uname -a
  id
  MQ_RUNSCRIPT="sh -x"
fi
# Remove the MQ Advanced swidtag if no Advanced packages are now installed 
for packagename in ${ADVANCEDPACKAGELIST} 
  do  
    if [ ${packagename}${PACKAGE_SUFFIX} != ${RPM_PACKAGE_NAME} ] ; then
      rpmout=`rpm -q ${packagename}${PACKAGE_SUFFIX} 2>&1`
      rpm -q ${packagename}${PACKAGE_SUFFIX} --qf '%{INSTPREFIXES}
' 2>&1 | grep -w ${MQ_INSTALLATION_PATH} > /dev/null 2>&1 
      if [ $? -eq 0 ] ; then  
         touch /tmp/$$.advanced_yes
      fi
    fi
  done
if [ ! -f /tmp/$$.advanced_yes  ]
  then 
    rm -f ${MQ_INSTALLATION_PATH}/swidtag/ibm.com_IBM_MQ_Advanced-${RPM_PACKAGE_VERSION}.swidtag 
  else 
    rm -f /tmp/$$.advanced_yes 
fi

