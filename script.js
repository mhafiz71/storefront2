
let person = {
    name : 'Mohammed Hafiz',
    age : 21,
    gender : 'He/She',
    pronoun : function () {
        if (this.gender.toLowerCase == 'male') {
            return 'He';
        } else if (this.gender.toLowerCase == 'female') {
            return 'She';
        } else {
            return 'they';
        }
    }
}

addressing = `${person.pronoun()}, is the person of ${person['name']}, aged ${person['age']} years old..`;
// console.log(addressing);

let a = 'red';
let b = 'blue';

let c = a
a = b
b = c

console.log(a, b)