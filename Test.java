/**
 * Class for testing Class Version this JVM is able to load
 * We test this by compiling class and looking it's version.
 */

import java.io.*;
import java.util.*;

public class Test {
  public static void main(String[] args) {
    Properties p = System.getProperties();
    try {
      FileWriter fstream = new FileWriter("classver");
      BufferedWriter out = new BufferedWriter(fstream);
      out.write((String)p.get("java.class.version"));
      out.close();
    } catch (IOException e) {
      System.err.println(e.getMessage());
    }
  }
}
