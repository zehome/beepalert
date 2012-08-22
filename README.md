Very small script to fire beep alarm if a loadavg is above a threshold.


Example usage: (Fires the alarm when loadavg on 10.31.254.20 is above 5.0)

<pre>
ssh ed@10.31.254.20 'while [ 1 ]; do cat /proc/loadavg; sleep 5; done' | python beepalert.py 5.0
</pre>

Author
======
Laurent Coustet <ed@zehome.com>

Licence
=======

BSD
