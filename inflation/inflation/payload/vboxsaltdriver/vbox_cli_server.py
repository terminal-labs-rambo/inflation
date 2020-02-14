from flask import Flask, make_response, request

import logging
import subprocess
import re

app = Flask(__name__)

log = logging.getLogger("werkzeug")
log.setLevel(logging.ERROR)


@app.errorhandler(404)
def not_found(error):
    return make_response("Not found", 404)


def sanitation(s, max_length=16):
    good_char_set = set("-1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_ ")
    is_good = False

    if isinstance(s, str):
        is_good = True
    else:
        return False

    if len(s) < max_length:
        is_good = True
    else:
        return False

    if set(s) <= good_char_set:
        is_good = True
    else:
        return False

    return is_good


def tighten_up(cmd):
    cmd = re.sub(" +", " ", cmd)
    cmd = cmd.rstrip()
    cmd = cmd.lstrip()
    cmd = cmd.lower()
    return cmd


def get_vm_names():
    cli_output = subprocess.check_output(["vboxmanage", "list", "vms"])
    vms = cli_output.split("\n")
    names = []
    for vm in vms:
        if len(vm) > 0:
            names.append(vm.split(" {")[0].replace('"', ""))
    return names


def acceptable_command(cmd):
    cmd_list = cmd.split(" ")
    if len(cmd_list) == 3:
        if cmd_list[0] == "vboxmanage" and cmd_list[1] == "list" and cmd_list[2] == "vms":
            return ["vboxmanage", "list", "vms"]

    if len(cmd_list) == 3:
        if cmd_list[0] == "vboxmanage" and cmd_list[1] == "list" and cmd_list[2] == "hdds":
            return ["vboxmanage", "list", "hdds"]

    if len(cmd_list) == 3:
        if cmd_list[0] == "vboxmanage" and cmd_list[1] == "list" and cmd_list[2] == "runningvms":
            return ["vboxmanage", "list", "runningvms"]

    if len(cmd_list) == 4:
        if (
            cmd_list[0] == "vboxmanage"
            and cmd_list[1] == "controlvm"
            ##and cmd_list[2] == "name"
            and cmd_list[3] == "poweroff"
        ):

            name = cmd_list[2]
            if sanitation(name, 64) and name in get_vm_names():
                return ["vboxmanage", "controlvm", name, "poweroff"]

    if len(cmd_list) == 4:
        if (
            cmd_list[0] == "vboxmanage"
            and cmd_list[1] == "unregistervm"
            ##and cmd_list[2] == "name"
            and cmd_list[3] == "--delete"
        ):

            name = cmd_list[2]
            if sanitation(name, 64) and name in get_vm_names():
                return ["vboxmanage", "unregistervm", name, "--delete"]

    if len(cmd_list) == 4:
        if cmd_list[0] == "vboxmanage" and cmd_list[1] == "guestproperty" and cmd_list[2] == "enumerate":
            # and cmd_list[3] == "name"):

            name = cmd_list[3]
            if sanitation(name, 64) and name in get_vm_names():
                return ["vboxmanage", "guestproperty", "enumerate", name]

    if len(cmd_list) == 5:
        if (
            cmd_list[0] == "vboxmanage"
            and cmd_list[1] == "startvm"
            ##and cmd_list[2] == "name"
            and cmd_list[3] == "--type"
            and cmd_list[4] == "headless"
        ):

            name = cmd_list[2]
            if sanitation(name, 64) and name in get_vm_names():
                return ["vboxmanage", "startvm", name, "--type", "headless"]

    if len(cmd_list) == 6:
        if (
            cmd_list[0] == "vboxmanage"
            and cmd_list[1] == "clonevm"
            ##and cmd_list[2] == "clonefrom"
            and cmd_list[3] == "--name"
            # and cmd_list[4] == "name"
            and cmd_list[5] == "--register"
        ):

            name_1 = cmd_list[2]
            name_2 = cmd_list[4]
            if name_1 in get_vm_names():
                if sanitation(name_1, 64) and sanitation(name_2, 64):
                    return ["vboxmanage", "clonevm", name_1, "--name", tighten_up(name_2), "--register"]

    return False


@app.route("/", methods=["POST"])
def vbox_web_cli():
    if request.json:
        pass
    else:
        return "bad command"

    data = request.json
    if len(data.get(u"cmd")) > 8:
        cmd = str(data.get(u"cmd"))
    else:
        return "bad command"

    if sanitation(cmd, max_length=256):
        pass
    else:
        return "bad command"

    cmd = tighten_up(cmd)

    cleaned_cmd = acceptable_command(cmd)

    if cleaned_cmd:
        cli_output = subprocess.check_output(cleaned_cmd)
    else:
        return "bad command"

    return cli_output


if __name__ == "__main__":
    app.run()
