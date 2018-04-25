
import py4j.GatewayServer;

public class test_java {

    private Stack stack;

    public test_java() {
      stack = new Stack();
      stack.push("Initial Item");
    }

    public Stack getStack() {
        return stack;
    }

    public static void main(String[] args) {
        GatewayServer gatewayServer = new GatewayServer(new test_java());
        gatewayServer.start();
        System.out.println("Gateway Server Started");
    }

}