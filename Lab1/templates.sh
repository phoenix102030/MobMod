#!/bin/bash

export SUMO_HOME=/packages/sumo
export SUMO_TOOLS=$SUMO_HOME/tools

$SUMO_HOME/bin/sumo --save-template sumo.cfg
$SUMO_HOME/bin/netgenerate --save-template netgenerate.cfg
$SUMO_HOME/bin/duarouter --save-template duarouter.cfg
