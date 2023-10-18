const { describe } = require("yargs");
const factorial = require("./factorial.js");

test("tests factorial(0) = 1", () => {
    expect(factorial(0)).toBe(1);
});

test("tests factorial(1) = 1", () => {
    expect(factorial(1)).toBe(1);
})

test("tests factorial(2) = 2", () => {
    expect(factorial(2)).toBe(2);
})

test("tests factorial(4) = 24", () => {
    expect(factorial(4)).toBe(24);
})

test("tests factorial(8) = 40320", () => {
    expect(factorial(8)).toBe(40320);
})

test("tests factorial(18) = 6402373705728000", () => {
    expect(factorial(18)).toBe(6402373705728000);
})

console.log(factorial(0) === 1);
console.log(factorial(1) === 1);
console.log(factorial(2) === 2);
console.log(factorial(4) === 24);
console.log(factorial(8) === 40320);
console.log(factorial(18) === 6402373705728000);
// Test how high of a number your program can calculate. Can you push it further?
