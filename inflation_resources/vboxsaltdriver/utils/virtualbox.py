# -*- coding: utf-8 -*-
"""
Utilities to help make requests to virtualbox

The virtualbox SDK reference can be found at http://download.virtualbox.org/virtualbox/SDKRef.pdf

This code assumes vboxapi.py from VirtualBox distribution
being in PYTHONPATH, or installed system-wide
"""
from __future__ import absolute_import
# Import python libs
import logging

from salt.utils.timeout import wait_for

log = logging.getLogger(__name__)

import vboxsaltdriver

# Import virtualbox libs
HAS_LIBS = False

_virtualboxManager = None

def vb_get_vm_list():
    machine_name_list_raw = vboxsaltdriver.list_vms()
    vms = machine_name_list_raw.split("\n")
    
    machine_name_list = []
    for vm in vms:
        machine_name_list.append(vm.split(" ")[0].replace('"',''))

    machines = []
    for machine_name in machine_name_list:
        machines.append({"name":machine_name})    
    
    return machines


def vb_stop_vm(name):
    machine_name_list_raw = vboxsaltdriver.list_running_vms()
    vms = machine_name_list_raw.split("\n")
    
    machine_name_list = []
    for vm in vms:
        machine_name_list.append(vm.split(" ")[0].replace('"',''))

    if name in machine_name_list:
        log.info("Stopping machine %s", name)
        vboxsaltdriver.stop_vm(name)


def vb_start_vm(name):
    log.info("Starting machine %s", name)
    vboxsaltdriver.start_vm(name)


def vb_destroy_vm(name):
    log.info("Destroying machine %s", name)
    vboxsaltdriver.delete_vm(name)


def vb_get_vm_exists(name):    
    machines_list = vb_get_vm_list()
    for machine in machines_list:
        if machine["name"] == name:       
            return True
    return False


def vb_clone_vm(name, clone_from):
    log.info("Clone virtualbox machine %s from %s", name, clone_from)
    vboxsaltdriver.clone_vm(name, clone_from)


def vb_get_vm_address(name=None):
    log.info("getting virtualbox machine %s address", name)
    results = vboxsaltdriver.get_vm_address(name)
    lines = results.split("\n")
    for line in lines:
        if "Name: /VirtualBox/GuestInfo/Net/1/V4/IP" in line:
            address_pair = line.split(",")[1]
            address_pair = address_pair.replace(" ", "")
            address = address_pair.split(":")[1]
            return address
    return False


def vb_util_treat_vm_dict(machine):
    machine.update({
        "id": machine.get("id", ""),
        "image": machine.get("image", ""),
        "size": "{0} MB".format(machine.get("memorySize", 0)),
        "state": "on",
        "private_ips": [],
        "public_ips": [],
    })
    
    return machine
