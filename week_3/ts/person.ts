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

export default Person;
