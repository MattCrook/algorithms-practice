/*
############################################
CIRCULAR BUFFER FULL

(https://github.com/trevnorris/cbuffer)
############################################
*/


(function (global) {
  class CBuffer {
    constructor() {
      // handle cases where "new" keyword wasn't used
      if (!(this instanceof CBuffer)) {
        // multiple conditions need to be checked to properly emulate Array
        if (arguments.length > 1 || typeof arguments[0] !== "number") {
          return CBuffer.apply(new CBuffer(arguments.length), arguments);
        } else {
          return new CBuffer(arguments[0]);
        }
      }
      // if no arguments, then nothing needs to be set
      if (arguments.length === 0) throw new Error("Missing Argument: You must pass a valid buffer size");
      // this is the same in either scenario
      this.length = this.start = 0;
      // set to callback fn if data is about to be overwritten
      this.overflow = null;
      // emulate Array based on passed arguments
      if (arguments.length > 1 || typeof arguments[0] !== "number") {
        this.data = new Array(arguments.length);
        this.end = (this.size = arguments.length) - 1;
        this.push.apply(this, arguments);
      } else {
        this.data = new Array(arguments[0]);
        this.end = (this.size = arguments[0]) - 1;
      }
      // need to `return this` so `return CBuffer.apply` works
      return this;
    }
    /* mutator methods */
    // pop last item
    pop() {
      var item;
      if (this.length === 0) return;
      item = this.data[this.end];
      // remove the reference to the object so it can be garbage collected
      delete this.data[this.end];
      this.end = (this.end - 1 + this.size) % this.size;
      this.length--;
      return item;
    }
    // push item to the end
    push() {
      var i = 0;
      // check if overflow is set, and if data is about to be overwritten
      if (this.overflow && this.length + arguments.length > this.size) {
        // call overflow function and send data that's about to be overwritten
        for (; i < this.length + arguments.length - this.size; i++) {
          this.overflow(this.data[(this.end + i + 1) % this.size], this);
        }
      }
      // push items to the end, wrapping and erasing existing items
      // using arguments variable directly to reduce gc footprint
      for (i = 0; i < arguments.length; i++) {
        this.data[(this.end + i + 1) % this.size] = arguments[i];
      }
      // recalculate length
      if (this.length < this.size) {
        if (this.length + i > this.size) this.length = this.size;
        else this.length += i;
      }
      // recalculate end
      this.end = (this.end + i) % this.size;
      // recalculate start
      this.start = (this.size + this.end - this.length + 1) % this.size;
      // return number current number of items in CBuffer
      return this.length;
    }
    // reverse order of the buffer
    reverse() {
      var i = 0, tmp;
      for (; i < ~~(this.length / 2); i++) {
        tmp = this.data[(this.start + i) % this.size];
        this.data[(this.start + i) % this.size] = this.data[(this.start + (this.length - i - 1)) % this.size];
        this.data[(this.start + (this.length - i - 1)) % this.size] = tmp;
      }
      return this;
    }
    // rotate buffer to the left by cntr, or by 1
    rotateLeft(cntr) {
      if (typeof cntr === "undefined") cntr = 1;
      if (typeof cntr !== "number") throw new Error("Argument must be a number");
      while (--cntr >= 0) {
        this.push(this.shift());
      }
      return this;
    }
    // rotate buffer to the right by cntr, or by 1
    rotateRight(cntr) {
      if (typeof cntr === "undefined") cntr = 1;
      if (typeof cntr !== "number") throw new Error("Argument must be a number");
      while (--cntr >= 0) {
        this.unshift(this.pop());
      }
      return this;
    }
    // remove and return first item
    shift() {
      var item;
      // check if there are any items in CBuff
      if (this.length === 0) return;
      // store first item for return
      item = this.data[this.start];
      // recalculate start of CBuffer
      this.start = (this.start + 1) % this.size;
      // decrement length
      this.length--;
      return item;
    }
    // sort items
    sort(fn) {
      this.data.sort(fn || defaultComparitor);
      this.start = 0;
      this.end = this.length - 1;
      return this;
    }
    // add item to beginning of buffer
    unshift() {
      var i = 0;
      // check if overflow is set, and if data is about to be overwritten
      if (this.overflow && this.length + arguments.length > this.size) {
        // call overflow function and send data that's about to be overwritten
        for (; i < this.length + arguments.length - this.size; i++) {
          this.overflow(this.data[this.end - (i % this.size)], this);
        }
      }
      for (i = 0; i < arguments.length; i++) {
        this.data[(this.size + this.start - (i % this.size) - 1) % this.size] = arguments[i];
      }
      if (this.size - this.length - i < 0) {
        this.end += this.size - this.length - i;
        if (this.end < 0) this.end = this.size + (this.end % this.size);
      }
      if (this.length < this.size) {
        if (this.length + i > this.size) this.length = this.size;
        else this.length += i;
      }
      this.start -= arguments.length;
      if (this.start < 0) this.start = this.size + (this.start % this.size);
      return this.length;
    }
    /* accessor methods */
    // return index of first matched element
    indexOf(arg, idx) {
      if (!idx) idx = 0;
      for (; idx < this.length; idx++) {
        if (this.data[(this.start + idx) % this.size] === arg) return idx;
      }
      return -1;
    }
    // return last index of the first match
    lastIndexOf(arg, idx) {
      if (!idx) idx = this.length - 1;
      for (; idx >= 0; idx--) {
        if (this.data[(this.start + idx) % this.size] === arg) return idx;
      }
      return -1;
    }
    // return the index an item would be inserted to if this
    // is a sorted circular buffer
    sortedIndex(value, comparitor, context) {
      comparitor = comparitor || defaultComparitor;
      var isFull = this.length === this.size, low = this.start, high = isFull ? this.length - 1 : this.length;

      // Tricky part is finding if its before or after the pivot
      // we can get this info by checking if the target is less than
      // the last item. After that it's just a typical binary search.
      if (low && comparitor.call(context, value, this.data[high]) > 0) {
        (low = 0), (high = this.end);
      }

      while (low < high) {
        var mid = (low + high) >>> 1;
        if (comparitor.call(context, value, this.data[mid]) > 0) low = mid + 1;
        else high = mid;
      }
      return !isFull
        ? low
        : // http://stackoverflow.com/a/18618273/1517919
        (((low - this.start) % this.length) + this.length) % this.length;
    }
    /* iteration methods */
    // check every item in the array against a test
    every(callback, context) {
      var i = 0;
      for (; i < this.length; i++) {
        if (!callback.call(context, this.data[(this.start + i) % this.size], i, this)) return false;
      }
      return true;
    }
    // loop through each item in buffer
    // TODO: figure out how to emulate Array use better
    forEach(callback, context) {
      var i = 0;
      for (; i < this.length; i++) {
        callback.call(context, this.data[(this.start + i) % this.size], i, this);
      }
    }
    // construct new CBuffer of same length, apply map function, and return new CBuffer
    map(callback, context) {
      var outCBuffer = new CBuffer(this.size);
      for (var i = 0; i < this.length; i++) {
        var n = (this.start + i) % this.size;
        outCBuffer.push(callback.call(context, this.data[n], i, this));
      }
      return outCBuffer;
    }
    // check items agains test until one returns true
    // TODO: figure out how to emulate Array use better
    some(callback, context) {
      var i = 0;
      for (; i < this.length; i++) {
        if (callback.call(context, this.data[(this.start + i) % this.size], i, this)) return true;
      }
      return false;
    }
    // calculate the average value of a circular buffer
    avg() {
      return this.length == 0 ? 0 : this.sum() / this.length;
    }
    // loop through each item in buffer and calculate sum
    sum() {
      var index = this.length;
      var s = 0;
      while (index--) s += this.data[index];
      return s;
    }
    // loop through each item in buffer and calculate median
    median() {
      if (this.length === 0) return 0;
      var values = this.slice().sort(defaultComparitor);
      var half = Math.floor(values.length / 2);
      if (values.length % 2) return values[half];
      else return (values[half - 1] + values[half]) / 2.0;
    }
    /* utility methods */
    // reset pointers to buffer with zero items
    // note: this will not remove values in cbuffer, so if for security values
    //       need to be overwritten, run `.fill(null).empty()`
    empty() {
      var i = 0;
      this.length = this.start = 0;
      this.end = this.size - 1;
      return this;
    }
    // fill all places with passed value or function
    fill(arg) {
      var i = 0;
      if (typeof arg === "function") {
        while (((this.data[i] = arg()), ++i < this.size));
      } else {
        while (((this.data[i] = arg), ++i < this.size));
      }
      // reposition start/end
      this.start = 0;
      this.end = this.size - 1;
      this.length = this.size;
      return this;
    }
    // return first item in buffer
    first() {
      return this.data[this.start];
    }
    // return last item in buffer
    last() {
      return this.data[this.end];
    }
    // return specific index in buffer
    get(arg) {
      return this.data[mod(this.start + arg, this.size)];
    }
    isFull(arg) {
      return this.size === this.length;
    }
    // set value at specified index
    set(idx, arg) {
      return (this.data[(this.start + idx) % this.size] = arg);
    }
    // return clean array of values
    toArray() {
      return this.slice();
    }
    // return a string based on the array
    join(separator) {
      if (!separator) separator = ",";
      var outString = new String(this.data[0]);
      for (var i = 1; i < this.length; i++) {
        var n = (this.start + i) % this.size;
        outString = outString.concat(separator, this.data[i]);
      }
      return outString;
    }
    // slice the buffer to an arraay
    slice(start, end) {
      var size = this.length;

      start = +start || 0;

      if (start < 0) {
        if (start >= end) return [];
        start = -start > size ? 0 : size + start;
      }

      if (end == null || end > size) end = size;
      else if (end < 0) end += size;
      else end = +end || 0;

      size = start < end ? end - start : 0;

      var result = Array(size);
      for (var index = 0; index < size; index++) {
        result[index] = this.data[(this.start + start + index) % this.size];
      }
      return result;
    }
  }

  function defaultComparitor(a, b) {
    return a == b ? 0 : a > b ? 1 : -1;
  }

  function mod(n, m) {
    return ((n % m) + m) % m;
  }


  if (typeof module === "object" && module.exports) module.exports = CBuffer;
  else global.CBuffer = CBuffer;
})(this);


console.log("-----------------")
var cBuf1 = new CBuffer(10);      // empty buffer with size of 10
var cBuf2 =  new CBuffer(1,2,3,4); // buffer with size 4
var cBuf3 = CBuffer(5);           // For those who are really lazy, new is optional
console.log("1. ", cBuf1);
console.log("2. ", cBuf2);
console.log("3. ", cBuf3);
console.log("-----------------")


// If you want to catch when data is overwritten, 
// just assign a function to the overflow variable and it will be called 
// whenever a value is about to be overwritten and it will pass the value as the first argument:
var myBuff = CBuffer(4);
myBuff.overflow = function(data) {
    console.log(data);
};

myBuff.push(1,2,3,4); // nothing shows up yet
myBuff.push(5);       // log: 1
