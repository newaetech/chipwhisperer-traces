import chipwhisperer as cw
from pathlib import Path
import subprocess
import shutil
import time

def get_firmware_dir():
    full_path = Path(cw.__file__)
    repo_path = full_path.parents[2]
    fw_path = repo_path / "firmware" / "mcu"
    return fw_path

def get_default_build_commands():
    return ["make", "-j", "PLATFORM=CWHUSKY", "CRYPTO_TARGET=TINYAES128C", "SS_VER=SS_VER_2_1"]

def run_build_command(proj_name, cmd, dir=None):
    if dir is None:
        dir = get_firmware_dir() / proj_name
    rtn = subprocess.run(cmd, capture_output=True, cwd=dir)
    return rtn

def build_and_copy_fw(proj_name, cmd=None, dir=None, out_dir="../binaries"):
    if cmd is None:
        cmd = get_default_build_commands()
    if dir is None:
        dir = get_firmware_dir() / proj_name
    print("Building firmware")
    rtn = run_build_command(proj_name, cmd, dir)
    if rtn.returncode != 0:
        raise OSError("Couldn't run command {} in {}, got rtn {}, stderr={}, stdout={}".format(cmd, dir, rtn.returncode, rtn.stderr, rtn.stdout))
    
    outfile_fmt = "{}-CWHUSKY.hex".format(proj_name)
    outfile = dir/outfile_fmt
    print("Copying {} to {}".format(outfile, out_dir))
    shutil.copy(dir / outfile_fmt, out_dir)
    return Path(out_dir) / outfile_fmt

def build_copy_prog_fw(scope, proj_name, cmd=None, dir=None, out_dir="../binaries"):
    fw_path = build_and_copy_fw(proj_name, cmd, dir, out_dir)
    print("Programming...")
    cw.program_target(scope, cw.programmers.SAM4SProgrammer, str(fw_path))
    print("Done")

def reset_target(scope):
    scope.io.nrst = 'low'
    time.sleep(0.25)
    scope.io.nrst = 'high_z'
    time.sleep(0.25)