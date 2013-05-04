#!/bin/bash
#
# Run our web service
#

# working direct to set the path to our modules (not 
# the most efficient but it works)
export MOO_HOME="$( cd "$( dirname "${BASH_SOURCE[0]}/"/)" && cd .. && pwd )"

echo -e "\n** starting service from $MOO_HOME **\n"

# configuration
export PYTHONPATH=${MOO_HOME}/m:${PYTHONPATH}

# run
#python ${MOO_HOME}/moo/moo.py ${MOO_HOME} ${MOO_HOME}/conf/moo.conf
python ${MOO_HOME}/mooc-ws/run.py ${MOO_HOME} ${MOO_HOME}/conf/moo.conf
