import subprocess

benchmarks = ['lfsr', 'merge', 'mm', 'sieve', 'spmv']
for benchmark in benchmarks:
    bashCommand = "rm -rf m5out/"
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    bashCommand = "build/X86/gem5.opt configs/ass1/se.py"
    bashCommand += " --cpu-type DerivO3CPU --mem-type DDR3_1600_8x8"
    bashCommand += " -c /root/cs251a-microbench/" + benchmark
    bashCommand += " --sys-clock 1GHz --caches --l2cache"
    bashCommand += " --l1d_size 64kB --l2_size 2MB --issue-width 8"
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    bashCommand = "cp -a m5out/ ../ass1outputs/" + benchmark +"/1/"
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()


    bashCommand = "rm -rf m5out/"
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    bashCommand = "build/X86/gem5.opt configs/ass1/se.py"
    bashCommand += " --cpu-type MinorCPU --mem-type DDR3_1600_8x8"
    bashCommand += " -c /root/cs251a-microbench/" + benchmark
    bashCommand += " --sys-clock 1GHz --caches --l2cache"
    bashCommand += " --l1d_size 64kB --l2_size 2MB --issue-width 8"
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    bashCommand = "cp -a m5out/ ../ass1outputs/" + benchmark +"/2/"
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()


    bashCommand = "rm -rf m5out/"
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    bashCommand = "build/X86/gem5.opt configs/ass1/se.py"
    bashCommand += " --cpu-type DerivO3CPU --mem-type DDR3_1600_8x8"
    bashCommand += " -c /root/cs251a-microbench/" + benchmark
    bashCommand += " --sys-clock 1GHz --caches --l2cache"
    bashCommand += " --l1d_size 64kB --l2_size 2MB --issue-width 2"
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    bashCommand = "cp -a m5out/ ../ass1outputs/" + benchmark +"/3/"
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()


    bashCommand = "rm -rf m5out/"
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    bashCommand = "build/X86/gem5.opt configs/ass1/se.py"
    bashCommand += " --cpu-type DerivO3CPU --mem-type DDR3_1600_8x8"
    bashCommand += " -c /root/cs251a-microbench/" + benchmark
    bashCommand += " --sys-clock 4GHz --caches --l2cache"
    bashCommand += " --l1d_size 64kB --l2_size 2MB --issue-width 8"
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    bashCommand = "cp -a m5out/ ../ass1outputs/" + benchmark +"/4/"
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()


    bashCommand = "rm -rf m5out/"
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    bashCommand = "build/X86/gem5.opt configs/ass1/se.py"
    bashCommand += " --cpu-type DerivO3CPU --mem-type DDR3_1600_8x8"
    bashCommand += " -c /root/cs251a-microbench/" + benchmark
    bashCommand += " --sys-clock 1GHz --caches "
    bashCommand += " --l1d_size 64kB --issue-width 8"
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    bashCommand = "cp -a m5out/ ../ass1outputs/" + benchmark +"/5/"
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()


    bashCommand = "rm -rf m5out/"
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    bashCommand = "build/X86/gem5.opt configs/ass1/se.py"
    bashCommand += " --cpu-type DerivO3CPU --mem-type DDR3_1600_8x8"
    bashCommand += " -c /root/cs251a-microbench/" + benchmark
    bashCommand += " --sys-clock 1GHz --caches --l2cache"
    bashCommand += " --l1d_size 64kB --l2_size 256kB --issue-width 8"
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    bashCommand = "cp -a m5out/ ../ass1outputs/" + benchmark +"/6/"
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()

    bashCommand = "rm -rf m5out/"
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    bashCommand = "build/X86/gem5.opt configs/ass1/se.py"
    bashCommand += " --cpu-type DerivO3CPU --mem-type DDR3_1600_8x8"
    bashCommand += " -c /root/cs251a-microbench/" + benchmark
    bashCommand += " --sys-clock 1GHz --caches --l2cache"
    bashCommand += " --l1d_size 64kB --l2_size 16MB --issue-width 8"
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    bashCommand = "cp -a m5out/ ../ass1outputs/" + benchmark +"/7/"
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
