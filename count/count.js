// Write a function that counts the capital "B" letters in "BBc"

const countBs = (word) => {
    let capBs = [];
    for (let i = 0; i <= word.length; i++) {
      const letter = word[i];
      if (letter === "B") {
        capBs.push(letter);
      }
    }
    const Bs = capBs.length;
    return Bs;
  };
  console.log("BBc", countBs("BBc"));



// What if the arg passed in isn't a string? Edge case...
  const countBs2 = (word) => {
    if (typeof word !== "string") {
      toString(word);
    }
    let counter = 0;
    for (let i = 0; i <= word.length; i++) {
      if (word[i] === "B") {
        counter++;
      }
    }
    return counter;
  };
  console.log("{countBs2}", countBs2("bBc"));
