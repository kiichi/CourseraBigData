////////////////////////////////////////////////////////////////////////////////////////
// Environment:
// 	Cloudera Quickstart VM
//
// How to compile:
//	export CLASSPATH=$CLASSPATH:.:/usr/lib/crunch/lib/hadoop-common.jar:/usr/lib/crunch/lib/hadoop-annotations.jar
// 	javac MyHadoopIOTest.java 
// 	jar cvf MyHadoopIOTest.jar MyHadoopIOTest.cl
//	/usr/bin/hadoop jar MyHadoopIOTest.jar MyHadoopIOTest
//
// Reference:
// 	http://free-hadoop-tutorials.blogspot.com/2011/04/using-hdfs-programmatically.html
//
////////////////////////////////////////////////////////////////////////////////////////
import org.apache.hadoop.conf.*;
import org.apache.hadoop.fs.*;
public class MyHadoopIOTest {
	public static void main(String[] args){
		try {
			System.out.println("Writing a file .... ");
			Path path = new Path("hello.txt");
			// Write a text file
			FileSystem fs = FileSystem.get(new Configuration());
			FSDataOutputStream fso = fs.create(path);
			fso.writeUTF("hello world");
			fso.close();
		
			// Read the text file
			FSDataInputStream fsi = fs.open(path);
			String greeting = fsi.readUTF();
			fsi.close();
			System.out.println(greeting);

		}catch (Exception ex){
			System.out.println("Some error: " + ex.toString());
		}
	}
}
