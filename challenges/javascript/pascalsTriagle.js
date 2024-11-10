//--------------------------------------------------------//
// Given an integer numRows, return the first numRows of Pascal's triangle.
// In Pascal's triangle, each number is the sum of the two numbers directly above it: as shown:
//
//             1
//           1   1
//         1   2   1
//       1   3   3   1
//     1   4   6   4   1
//
// Example 1:
// Input: numRows = 5
// Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
//
// Example 2:
// Input: numRows = 1
// Output: [[1]]
//--------------------------------------------------------//

//-----------------------Using Recursion ----------------------------//
//--------------------------------------------------------------------//
function generate1Function(rows) {
  // if numRows == 0, return empty list b/c we are either done or dont want to add another row.
  if (rows == 0) {
    return [];
  }

  // if rows == 1, just return that first row.
  if (rows == 1) {
    return [[1]];
  }

  // recursively call generate1Function, with num rows - 1,
  // to get the number of previous rows,
  // and save off in variable.
  let prevRows = generate1Function(rows - 1);

  // Using the fill() array function (used to fill all or a portion of an array with a static value)
  // create a new Array (using the Array Constructor)
  // and fill in the number of rows we have with 1.
  let newRow = new Array(rows).fill(1);
  /*
  Loop through passed in arg rows (i ==1, as long as i less than rows(which calls generate rows - 1) MINUS 1).
     Set the same index as we are on in the loop of arg rows, of new Array "newRow", to:
      - Value of index of prevRows[rows - 2](A below), and then the value of the index of that of i -1 (B below).
      - plus (+) the value of the index of prevRows[rows - 2], and then the index of that (C below).
     - prevRows
       - Example:
         - []
         - [ [ [ 1 ], [ 1, 1 ], [ 1, 2, 1 ] ] ]
         - [ [ [ 1 ], [ 1, 1 ], [ 1, 2, 1 ], [ 1, 3, 3, 1 ] ], [ [ 1 ], [ 1, 1 ], [ 1, 2, 1 ], [ 1, 3, 3, 1 ] ] ]
      - A) prevRows[rows - 2]
        - Example:
          - []
          - [ [ 1, 1 ] ]
          - [ [ 1, 2, 1 ], [ 1, 2, 1 ] ]
      - B) prevRows[rows - 2][i - 1]
        - Example:
          - []
          - [ 1 ]
          - [ 1, 2 ]
      - C) prevRows[rows - 2][i]
        - Example:
          - []
          - [ 1 ]
          - [ 2, 1 ]
      - D) prevRows[rows - 2][i - 1] + prevRows[rows - 2][i]
        - Example:
          - []
          - [ 2 ]
          - [ 3, 3 ]
      - E) newRow becomes:
        - Example:
          - [ [ 1 ], [ 1, 1 ] ]
          - [ [ 1 ], [ 1, 1 ], [ 1, 2, 1 ] ]
          - [ [ 1 ], [ 1, 1 ], [ 1, 2, 1 ], [ 1, 3, 3, 1 ] ]
  */

  for (let i = 1; i < rows - 1; i++) {
    newRow[i] = prevRows[rows - 2][i - 1] + prevRows[rows - 2][i];
  }

  prevRows.push(newRow);
  return prevRows;
}

console.log("generate1Function", generate1Function(5));
console.log("generate1Function", generate1Function(2));
console.log("--------------------------");

// Can also call function like this...
var generate_1 = function (numRows) {
  if (numRows === 0) {
    return [];
  }
  if (numRows === 1) {
    return [[1]];
  }

  let prevRows = generate_1(numRows - 1);
  let newRow = new Array(numRows).fill(1);

  for (let i = 1; i < numRows - 1; i++) {
    newRow[i] = prevRows[numRows - 2][i - 1] + prevRows[numRows - 2][i];
  }

  prevRows.push(newRow);
  return prevRows;
};

console.log("generate_1", generate_1(5));
console.log("generate_1", generate_1(1));
console.log("--------------------------");


//---------------- Using Combinatorial Formula -----------------------//
//--------------------------------------------------------------------//
const generate2 = (numRows) => {
  // instantiate new empty array
  let result = [];
  // If zero rows, we are done so return result.
  if (numRows == 0) {
    return result;
  }

  // set first row to 1, will always be 1.
  // and push that to result.
  let firstRow = [1];
  result.push(firstRow);

  // Loop the argument passed in (numRows)
  for (i = 1; i < numRows; i++) {
    // set pointer for previous row.(index in result of iterator val - 1)
    //   - (i - 1) b/c array indexes are zero based. So (i) is 1,2,3,4...so (i - 1) is 0,1,2,3.
    let prevRow = result[i - 1];
    // set initial val of current row.
    let currentRow = [1];

    // Loop through i (which will be values), as long as j is less than i...(1 is less than current iterator value passed in from arg numRows).
    for (let j = 1; j < i; j++) {
      // push the index of j - 1 in prevRow plus the index of j to current row.
      currentRow.push(prevRow[j - 1] + prevRow[j]);
    }

    currentRow.push(1);
    result.push(currentRow);
  }
  return result;
};

console.log("generate2", generate2(5));
console.log("generate2", generate2(1));
console.log("generate2", generate2(3));
console.log("--------------------------");

//---------------- Expanded Generate 2 (extra console logs to see process) -----------------------//
var generate2ExpandedExample = function (numRows) {
  let result = [];
  if (numRows === 0) {
    return result;
  }

  let firstRow = [1];
  result.push(firstRow);

  let temp = [];
  let temp2 = [];
  let temp3 = [];
  let temp4 = [];

  for (let i = 1; i < numRows; i++) {
    let prevRow = result[i - 1];
    let currentRow = [1];

    for (let j = 1; j < i; j++) {
      temp.push(prevRow);
      temp2.push(prevRow[j]);
      temp3.push(prevRow[j - 1]);
      temp4.push(prevRow[j - 1] + prevRow[j]);
      console.log("temp", temp)
      console.log("temp2", temp2)
      console.log("temp3", temp3)
      console.log("temp4", temp4)

      currentRow.push(prevRow[j - 1] + prevRow[j]);
    }

    currentRow.push(1);
    console.log("currentRow", currentRow)
    result.push(currentRow);
  }

  return result;
};

console.log("--------------------------------------------------");
console.log("generate2ExpandedExample", generate2ExpandedExample(4));
console.log("generate2ExpandedExample", generate2ExpandedExample(3));
console.log("generate2ExpandedExample", generate2ExpandedExample(1));
console.log("--------------------------------------------------");

//----------------- Using Dynamic Programming with 1D Array ---------//
//--------------------------------------------------------------------//

var generate3Dynamic = function (numRows) {
  if (numRows === 0) {
    return [];
  }
  if (numRows === 1) {
    return [[1]];
  }

  let prevRows = generate3Dynamic(numRows - 1);
  let prevRow = prevRows[prevRows.length - 1];
  let currentRow = [1];

  for (let i = 1; i < numRows - 1; i++) {
    currentRow.push(prevRow[i - 1] + prevRow[i]);
  }

  currentRow.push(1);
  prevRows.push(currentRow);

  return prevRows;
};

console.log("generate3Dynamic", generate3Dynamic(5));
console.log("generate3Dynamic", generate3Dynamic(1));
console.log("--------------------------");
