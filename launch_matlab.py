import subprocess

def launch_matlab_unix():
    # NOTE: for this to work, the local system shell must have the "matlab" command defined, possibly as an alias in ~/.bashrc
    # cmd = "'source ~/.bashrc && matlab'"
    subprocess.Popen(['/home/mark/applications/matlab/bin/glnxa64/MATLABWindow'], shell=True, executable='/bin/bash')

def launch_matlab_path():
    matlab_path = "matlab"
    subprocess.Popen(matlab_path)
