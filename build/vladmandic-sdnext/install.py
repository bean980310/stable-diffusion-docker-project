#!/usr/bin/env python

import os
import sys
import time
import shlex
import subprocess
from functools import lru_cache
import installer

debug_install = installer.log.debug if os.environ.get('SD_INSTALL_DEBUG', None) is not None else lambda *args, **kwargs: None
commandline_args = os.environ.get('COMMANDLINE_ARGS', "")
sys.argv += shlex.split(commandline_args)
args = None
parser = None
script_path = None
extensions_dir = None
git = os.environ.get('GIT', "git")
index_url = os.environ.get('INDEX_URL', "")
stored_commit_hash = None
dir_repos = "repositories"
python = sys.executable # used by some extensions to run python
skip_install = False # parsed by some extensions


def init_args():
    global parser, args # pylint: disable=global-statement
    import modules.cmd_args
    parser = modules.cmd_args.parser
    installer.add_args(parser)
    args, _ = parser.parse_known_args()


def init_paths():
    global script_path, extensions_dir # pylint: disable=global-statement
    import modules.paths
    modules.paths.register_paths()
    script_path = modules.paths.script_path
    extensions_dir = modules.paths.extensions_dir


def get_custom_args():
    custom = {}
    for arg in vars(args):
        default = parser.get_default(arg)
        current = getattr(args, arg)
        if current != default:
            custom[arg] = getattr(args, arg)
    installer.log.info(f'Command line args: {sys.argv[1:]} {installer.print_dict(custom)}')
    if os.environ.get('SD_ENV_DEBUG', None) is not None:
        env = os.environ.copy()
        if 'PATH' in env:
            del env['PATH']
        if 'PS1' in env:
            del env['PS1']
        installer.log.trace(f'Environment: {installer.print_dict(env)}')
    else:
        env = [f'{k}={v}' for k, v in os.environ.items() if k.startswith('SD_')]
        installer.log.debug(f'Env flags: {env}')


@lru_cache()
def commit_hash(): # compatbility function
    global stored_commit_hash # pylint: disable=global-statement
    if stored_commit_hash is not None:
        return stored_commit_hash
    try:
        stored_commit_hash = run(f"{git} rev-parse HEAD").strip()
    except Exception:
        stored_commit_hash = "<none>"
    return stored_commit_hash


@lru_cache()
def run(command, desc=None, errdesc=None, custom_env=None, live=False): # compatbility function
    if desc is not None:
        installer.log.info(desc)
    if live:
        result = subprocess.run(command, check=False, shell=True, env=os.environ if custom_env is None else custom_env)
        if result.returncode != 0:
            raise RuntimeError(f"""{errdesc or 'Error running command'} Command: {command} Error code: {result.returncode}""")
        return ''
    result = subprocess.run(command, stdout=subprocess.PIPE, check=False, stderr=subprocess.PIPE, shell=True, env=os.environ if custom_env is None else custom_env)
    if result.returncode != 0:
        raise RuntimeError(f"""{errdesc or 'Error running command'}: {command} code: {result.returncode}
{result.stdout.decode(encoding="utf8", errors="ignore") if len(result.stdout)>0 else ''}
{result.stderr.decode(encoding="utf8", errors="ignore") if len(result.stderr)>0 else ''}
""")
    return result.stdout.decode(encoding="utf8", errors="ignore")


def check_run(command): # compatbility function
    result = subprocess.run(command, check=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    return result.returncode == 0


@lru_cache()
def is_installed(package): # compatbility function
    return installer.installed(package)


@lru_cache()
def repo_dir(name): # compatbility function
    return os.path.join(script_path, dir_repos, name)


@lru_cache()
def run_python(code, desc=None, errdesc=None): # compatbility function
    return run(f'"{sys.executable}" -c "{code}"', desc, errdesc)


@lru_cache()
def run_pip(pkg, desc=None): # compatbility function
    forbidden = ['onnxruntime', 'opencv-python']
    if desc is None:
        desc = pkg
    for f in forbidden:
        if f in pkg:
            debug_install('Blocked package installation: package={f}')
            return True
    index_url_line = f' --index-url {index_url}' if index_url != '' else ''
    return run(f'"{sys.executable}" -m pip {pkg} --prefer-binary{index_url_line}', desc=f"Installing {desc}", errdesc=f"Couldn't install {desc}")


@lru_cache()
def check_run_python(code): # compatbility function
    return check_run(f'"{sys.executable}" -c "{code}"')


def git_clone(url, tgt, _name, commithash=None): # compatbility function
    installer.clone(url, tgt, commithash)


def run_extension_installer(ext_dir): # compatbility function
    installer.run_extension_installer(ext_dir)


def get_memory_stats():
    import psutil
    def gb(val: float):
        return round(val / 1024 / 1024 / 1024, 2)
    process = psutil.Process(os.getpid())
    res = process.memory_info()
    ram_total = 100 * res.rss / process.memory_percent()
    return f'{gb(res.rss)}/{gb(ram_total)}'

def main():
    global args # pylint: disable=global-statement
    installer.ensure_base_requirements()
    init_args() # setup argparser and default folders
    installer.args = args
    installer.setup_logging()
    installer.log.info('Installing SD.Next')
    installer.get_logfile()
    try:
        sys.excepthook = installer.custom_excepthook
    except Exception:
        pass
    installer.read_options()
    installer.check_python()
    installer.check_version()
    installer.log.info(f'Platform: {installer.print_dict(installer.get_platform())}')
    installer.set_environment()
    installer.install('onnxruntime-gpu', 'onnxruntime-gpu')
    installer.install('onnx', 'onnx')
    installer.check_torch()
    installer.check_onnx()
    installer.check_diffusers()
    installer.check_modified_files()
    installer.install_requirements()
    installer.install_packages()
    installer.install_submodules()
    init_paths()
    installer.install_extensions()
    installer.install_requirements() # redo requirements since extensions may change them
    installer.update_wiki()
    
    installer.install("matplotlib-inline")
    installer.install("ipython")
    installer.install("basicsr")
    installer.install("gfpgan")
    installer.install("triton")
    
    if installer.errors == 0:
        installer.log.debug(f'Setup complete without errors: {round(time.time())}')
    else:
        installer.log.warning(f'Setup complete with errors: {installer.errors}')
        installer.log.warning(f'See log file for more details: {installer.log_file}')
        
main()