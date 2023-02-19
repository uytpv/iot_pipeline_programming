class Person {
    private __age: number;

    constructor(public first_name: string, public last_name: string, age: number) {
        this.__age = age;
    }

    getAge(): number {
        return this.__age;
    }

    ageUp(): void {
        this.__age += 1;
    }

    getFullname(): string {
        return this.first_name + " " + this.last_name;
    }

    printFullname(): void {
        console.log(this.getFullname());
    }
}


console.log("Program starting.");

console.log("Creating person...");
const person = new Person("John", "Doe", 30);
console.log("Person created.");

console.log("Name:", person.getFullname());
console.log("Age:", person.getAge());

console.log("Person has now birthday...");
person.ageUp();
console.log(`New age: ${person.getAge()}`);

console.log("Program ending.");
