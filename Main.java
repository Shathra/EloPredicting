import java.io.IOException;

public class Main {
	public static void main(String[] args) throws IOException {
		CodeGenerator c = new CodeGenerator();
		InterfaceGenerator ig = new InterfaceGenerator();
		c.generate();
		ig.generateList();
		ig.printCombinations();
		
		
		
		
		
	}
}


