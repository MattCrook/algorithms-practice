// The problem calls for moving a set of disks from one tower to another with the restriction that at no time a disk is placed
// on top of a smaller disk. The problem has an associated well-known recursive algorithm.

function Hanoi(n, from, to, via) {
  if (n == 0) return;
  Hanoi(n - 1, from, via, to);
  moveDisk(from, to);

  // callStack.push([from,to]); // save parameters to callStack array
  Hanoi(n - 1, via, to, from);
}

var callcallStack;

function executeHanoi() {
  //  Some initialization code goes here
  callStack = []; // callStack array is global
  Hanoi(diskCount, 0, 2, 1);
  moveDisk(); // moveDisk takes its parameters from callStack
}

function moveDisk() {
  if (callStack.length == 0) return;
  var param = callStack.shift(); // Get call parameters from callStack
  // Note: throughout the code, I use fromBar, toBar to refer to towers
  fromBar = param[0];
  toBar = param[1];
  // find top element in fromBar
  var elem = document.getElementById(barsInfo[fromBar].disks.pop());
  moveInfo = {
    elem: elem,
    fromBar: fromBar,
    toBar: toBar,
    whichPos: "top", // element position property for movement
    dir: -1, // 1 or -1
    state: "up", // move upward
    endPos: 60, // end position (in pixels) for move upward
  };

  myTimer = setInterval(animateMove, speed); // Start animation
}

// n: number of disks; serves as the problem size for recursion
// from: the "from" tower is where the disks are placed
// to: the "to" tower is where the disks must be finally placed
// via: the "via" tower is that used as an intermediate location as disks are moved between the towers from and to.
