
import subprocess

benchmarks = ['lfsr', 'merge', 'mm', 'sieve', 'spmv']
for benchmark in benchmarks:
    bashCommand = "rm -rf m5out/"
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    bashCommand = "build/X86/gem5.opt configs/ass1/se.py"
    bashCommand += " --cpu-type MinorCPU --mem-type DDR3_1600_8x8"
    bashCommand += " -c /root/cs251a-microbench/" + benchmark
    bashCommand += " --sys-clock 1GHz --caches --l2cache"
    bashCommand += " --l1d_size 64kB --l2_size 2MB --issue-width 2"
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    bashCommand = "cp -a m5out/ ../ass1outputs/" + benchmark +"/9/"
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
