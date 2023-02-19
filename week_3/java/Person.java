public class Person {
    private int age;
    public String first_name;
    public String last_name;

    public Person(String first_name, String last_name, int age) {
        this.first_name = first_name;
        this.last_name = last_name;
        this.age = age;
    }

    public int getAge() {
        return this.age;
    }

    public void ageUp() {
        this.age += 1;
    }

    public String getFullname() {
        return this.first_name + " " + this.last_name;
    }

    public void printFullname() {
        System.out.println(this.getFullname());
    }
}
