// Have a name, and want to find the persons name in a phone book

const name = "Matt";

const phoneBook = [
  { Joe: "615-123-4567" },
  { Steve: "615-345-4567" },
  { Bob: "615-453-4567" },
  { Dan: "615-234-4567" },
  { Shap: "615-678-4567" },
  { Al: "615-876-4567" },
  { John: "615-123-4567" },
  { Jake: "615-890-4567" },
  { BJ: "615-765-4567" },
  { Brandon: "615-657-4567" },
  { Matt: "615-999-4567" },
  { Sean: "615-000-4567" },
];
let names = [];

const simpleSearch = (arr, nameToFind) => {
  for (let i = 0; i < arr.length; i++) {
    const value = arr[i];
    const key = Object.keys(value);
    names.push(key);
  }
  for (let i = 0; i < names.length; i++) {
    const n = names[i];
    const index = i;
    if (n[0] === nameToFind) {
      return index;
    }
  }
};
console.log("[simpleSearch]", simpleSearch(phoneBook, "Matt"));

const simpleSearchForInLoop = (array, nameToFind) => {
  for (item in array) {
    let index = item;
    let value = array[index];
    if (Object.keys(value)[0] === nameToFind) {
      return index;
    }
  }
};
console.log("[simpleSearchForInLoop]", simpleSearchForInLoop(phoneBook, "Matt"));

const simpleSearchObject = (array) => {
  let map = new Map();
  const keys = phoneBook.map((person) => Object.keys(person)[0]);
  map.set(keys, []);
};
console.log("simpleSearchObject", simpleSearchObject(phoneBook));
