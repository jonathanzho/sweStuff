public class TestDiamondInheritance {
    public static void main(String[] args) {
	System.out.println("[V] TestDiamondInheritance: ========== animal1");
        Animal animal1 = new Animal("animal1");

        System.out.println("[V] TestDiamondInheritance: ========== bird2");
	Bird bird2 = new Bird("bird2");
	bird2.fly();
	bird2.run();

	System.out.println("[V] TestDiamondInheritance: ========== horse3");
	Horse horse3 = new Horse("horse3");
	horse3.run();

	System.out.println("[V] TestDiamondInheritance: ========== pegasus4");
	Pegasus pegasus4 = new Pegasus("pegasus4");
	pegasus4.fly();
	pegasus4.run();
	pegasus4.setName("pegasus-4-copy");
	pegasus4.getName();
    }
}

