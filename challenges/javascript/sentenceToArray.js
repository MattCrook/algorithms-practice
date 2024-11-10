// Write a function that takes in a sentence, with optionally more, and output the sentence as an Array separated by its words.

function arrayList(words, more) {
  let sentence = [];
  const wordsToLettersArray = words.split(" ");
  wordsToLettersArray.forEach(l => {
    sentence.push(l);
  });
  if (more) {
    const moreToLettersArray = more.split(" ");
    moreToLettersArray.forEach(l => {
      sentence.push(l);
    });
  }
  return sentence;
}

console.log(arrayList("My new sentence"))
