set history filename ~/.gdb_history
set history save on

set print address on
set print object on
set print array on
set print array-indexes on
set print symbol on
set print pretty on

set auto-load safe-path ~

# https://sourceware.org/gdb/wiki/STLSupport
# svn co svn://gcc.gnu.org/svn/gcc/trunk/libstdc++-v3/python
python

import sys, os
home_dir = os.path.expanduser('~')
gdb_python_dir = f'{home_dir}/.gdb-python'
sys.path.insert(0, gdb_python_dir)
from libstdcxx.v6.printers import register_libstdcxx_printers
register_libstdcxx_printers (None)

