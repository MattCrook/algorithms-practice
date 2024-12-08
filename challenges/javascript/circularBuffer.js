class CircularBuffer {
  constructor(bufferLength) {
    this.buffer = [];
    this.pointer = 0;
    this.bufferLength = bufferLength;
  }

  push(element) {
    if (this.buffer.length === this.bufferLength) {
      this.buffer[this.pointer] = element;
    } else {
      this.buffer.push(element);
    }
    this.pointer = (this.pointer + 1) % this.bufferLength;
  }

  get(i) {
    return this.buffer[i];
  }

  //Gets the ith element before last one
  getLast(i) {
    return this.buffer[this.pointer + this.bufferLength - 1 - i];
  }
}


let circularBuffer = new CircularBuffer(3);
circularBuffer.push("a");
circularBuffer.push("b");
circularBuffer.push("c");
// should print a,b,c
console.log(`0 element: ${circularBuffer.get(0)}; 1 element: ${circularBuffer.get(1)}; 2 element: ${circularBuffer.get(2)};`);

console.log("Last element: " + circularBuffer.getLast(0)); // should print 'c'

circularBuffer.push("d");

// should print d,b,c
console.log(`0 element: ${circularBuffer.get(0)}; 1 element: ${circularBuffer.get(1)}; 2 element: ${circularBuffer.get(2)};`);
