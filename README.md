Very small script to fire beep alarm if a loadavg is above a threshold.


Example usage:
`̀``
ssh ed@10.31.254.20 'while [ 1 ]; do cat /proc/loadavg; sleep 5; done' | python beepalert.py 5.0
`̀``
