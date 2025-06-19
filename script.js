
let person = {
    name : 'Mohammed Hafiz',
    age : 21,
    gender : 'male',
    pronoun : function () {
        if (this.gender == 'male') {
            return 'He';
        } else if (this.gender == 'female') {
            return 'She';
        } else {
            return 'they';
        }
    }
}

address = `${person.pronoun()} is the person of ${person['name']}, aged ${person['age']} years old..`
console.log(address)