var msg    = "Sic gloria transit mundi ...";
var fmsg   = "Ars longa, vita brevis";
var speed  = 100;
var cycles = 1;
for (var i = 1; i <= 100; i++) msg = " " + msg;
var char0  = 0;

function statusScroll()
{
    window.status = msg.substring(char0,msg.length);
    if (++char0 <= msg.length) setTimeout('statusScroll()', speed);
    else if (--cycles > 0) {
        char0 = 0;
        setTimeout('statusScroll()', speed);
    }
    else
        setTimeout('window.status = fmsg', 20);
}

function Last_modified () {
document.write('Last modified on ' + document.lastModified);
}