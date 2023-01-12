# GoogleIP
search through every IPv4 10 whole ranges at a time

to feed it a list


echo filename | cat | xargs -P 10000 -n 1 python3 ips.py [options] searchterm
