# Copyright 2012-2015 ZTE Corporation. All rights reserved
# Copyright (c) 2012 OpenStack LLC.
# All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
"""
Constants used in ZTE Volume driver.
"""

ZTE_HOST_GROUP_NAME_PREFIX = 'HostGroup_'
ZTE_VOL_AND_SNAP_NAME_PREFIX = 'OpenStack_'
ZTE_VOL__NAME_PREFIX_NEW = 'OpenCos_'
ZTE_CLONE_SUFFIX = 'c'
ZTE_GROUP_MAX_LUN = 255
ZTE_SUCCESS = 0
ZTE_VOLUME_IN_GROUP = 16917029
ZTE_WEB_LOGIN_TYPE = 5
ZTE_ERR_GROUP_NOT_EXIST = 16916997
ZTE_ERR_GROUP_EXIST = 16916994
ZTE_ERR_HOSTNAME_EXIST = 16918785
ZTE_ERR_HOSTNAME_NOT_EXIST = 16918786
ZTE_ERR_PORT_EXIST_OLD = 16918787
ZTE_ERR_PORT_EXIST = 16918798
ZTE_ERR_PORT_EXIST_INOTHER = 16918799
ZTE_ERR_HOST_NOT_EXIST = 16917004
ZTE_ERR_HOST_EXIST_OLD = 16917002
ZTE_ERR_HOST_EXIST = 16917015
ZTE_ERR_HOST_EXIST_INOTHER = 16917016
ZTE_ERR_VOLUME_NOT_EXIST = 17108999
ZTE_ERR_OBJECT_EXIST = 16917159
ZTE_ERR_CLONE_OR_SNAP_NOT_EXIST = 16917040
ZTE_ERR_VOL_EXISTS = 16917000
ZTE_ERR_LUNDEV_NOT_EXIST = 16973826
ZTE_ERR_VAS_OBJECT_NOT_EXIST = 17436681
ZTE_VOLUME_TASK_NOT_FINISHED = 17436959
ZTE_ERR_SNAP_EXIST_CLONE = 16917163
ZTE_SESSION_EXIST = 1495
ZTE_STATUS_OK = 1
ZTE_SIZE = 1024

ZTE_VOLUME = 0
ZTE_SNAPSHOT = 1

ZTE_VOLUME_ALLOCATION_RATIO = 20
ZTE_VOLUME_SNAPSHOT_PERCENT = 50
ZTE_DEFAULT_TIMEOUT = 720
