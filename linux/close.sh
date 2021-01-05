#!/bin/bash
pactl list short modules | grep "sink_name=dynopii" | cut -f1 | xargs -L1 pactl unload-module
pkill arecord