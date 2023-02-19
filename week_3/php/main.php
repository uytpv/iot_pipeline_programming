<?php
echo "Program starting.\n";

echo "Creating person...\n";
$person = new Person("John", "Doe", 30);
echo "Person created.\n";

echo "Name: " . $person->getFullname() . "\n";
echo "Age: " . $person->getAge() . "\n";

echo "Person has now birthday...\n";
$person->ageUp();
echo "New age: " . $person->getAge() . "\n";

echo "Program ending.\n";

class Person {
    private $age;
    public $first_name;
    public $last_name;

    public function __construct($first_name, $last_name, $age) {
        $this->first_name = $first_name;
        $this->last_name = $last_name;
        $this->age = $age;
    }

    public function getAge() {
        return $this->age;
    }

    public function ageUp() {
        $this->age += 1;
    }

    public function getFullname() {
        return $this->first_name . " " . $this->last_name;
    }

    public function printFullname() {
        echo $this->getFullname() . "\n";
    }
}
?>