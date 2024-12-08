// Circular buffer storage. Externally-apparent 'length' increases indefinitely
// while any items with indexes below length-n will be forgotten (undefined
// will be returned if you try to get them, trying to set is an exception).
// n represents the initial length of the array, not a maximum
function CircularBuffer(n) {
  this._array = new Array(n);
  this.length = 0;
}
CircularBuffer.prototype.toString = function () {
  return "[object CircularBuffer(" + this._array.length + ") length " + this.length + "]";
};
CircularBuffer.prototype.get = function (i) {
  if (i < 0 || i < this.length - this._array.length) return undefined;
  return this._array[i % this._array.length];
};
CircularBuffer.prototype.set = function (i, v) {
  if (i < 0 || i < this.length - this._array.length) throw CircularBuffer.IndexError;
  while (i > this.length) {
    this._array[this.length % this._array.length] = undefined;
    this.length++;
  }
  this._array[i % this._array.length] = v;
  if (i == this.length) this.length++;
};
CircularBuffer.IndexError = {};

//------------------------------------------------------//
/*
get supports default argument (returns last item pushed onto buffer)
get supports negative indexing (counts from right)
prev moves buffer back one and returns what's there (like popping without delete)
next undoes prev (moves buffer forward and returns it)
Could use this for example, to store a command history which I could then flip through in an app using its prev and next methods, which nicely return undefined when they have nowhere to go.
*/
//------------------------------------------------------//


var createRingBuffer = function (length) {
  /* https://stackoverflow.com/a/4774081 */
  var pointer = 0,
    buffer = [];

  return {
    get: function (key) {
      if (key < 0) {
        return buffer[pointer + key];
      } else if (key === false) {
        return buffer[pointer - 1];
      } else {
        return buffer[key];
      }
    },
    push: function (item) {
      buffer[pointer] = item;
      pointer = (pointer + 1) % length;
      return item;
    },
    prev: function () {
      var tmp_pointer = (pointer - 1) % length;
      if (buffer[tmp_pointer]) {
        pointer = tmp_pointer;
        return buffer[pointer];
      }
    },
    next: function () {
      if (buffer[pointer]) {
        pointer = (pointer + 1) % length;
        return buffer[pointer];
      }
    },
  };
};
