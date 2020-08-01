
// Write a function that takes a number as parameter,// and shall return the binary IEEE 754 encoding of this number as a string,
// with fields separated by spaces for readability.
// ArrayBuffer https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer
// DataView https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DataView

function numToIEEE_754(num) {
  const view = new DataView(new ArrayBuffer(8));
  view.setFloat64(0, num);
  const s =
    view.getUint32(0).toString(2).padStart(32, "0") +
    view.getUint32(4).toString(2).padStart(32, "0");
  return s.replace(/(.{1})(.{11})(.*)/, "$1 $2 $3");
}


// OR a little more concise...

function numToIEEE_754(num) {
  const view = new DataView(new ArrayBuffer(8));
  view.setFloat64(0, num);
  const binary = view.getBigUint64().toString(2).padStart(64, "0");
  return binary[0] + " " + binary.slice(1, 12) + " " + binary.slice(12);
}
console.log(numToIEEE_754(15.875));
