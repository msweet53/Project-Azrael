import os
os.system("raspivid -o - -t 0 -n -w 320 -h 200 -fps 24 | cvlc -vvv stream:///dev/stdin --sout '#standard{access=http,mux=ts,dst=:8090}' :demux=h264")
