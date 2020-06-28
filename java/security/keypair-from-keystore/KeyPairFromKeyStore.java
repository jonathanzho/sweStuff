import java.io.FileInputStream;
import java.security.Key;
import java.security.KeyPair;
import java.security.KeyStore;
import java.security.PrivateKey;
import java.security.PublicKey;
import java.security.cert.Certificate;
import java.util.Base64;
import java.util.Scanner;

public class KeyPairFromKeyStore {
  public static void main(String[] argv) throws Exception {
    Scanner reader = new Scanner(System.in);
    
    System.out.println("Enter keystore file name: ");
    String keystoreFileName = reader.next();

    FileInputStream is = new FileInputStream(keystoreFileName);

    KeyStore keystore = KeyStore.getInstance(KeyStore.getDefaultType());

    System.out.println("Enter keystore password: ");
    String keystorePassword = reader.next();

    keystore.load(is, keystorePassword.toCharArray());

    System.out.println("Enter alias: ");
    String alias = reader.next();

    System.out.println("Enter alias password: ");
    String aliasPassword = reader.next();

    reader.close();

    Key privateKey = keystore.getKey(alias, aliasPassword.toCharArray());
    System.out.println("private key algorithm=[" + privateKey.getAlgorithm() + "]");
    System.out.println("private key format=[" + privateKey.getFormat() + "]");

    byte[] privateKeyEncoded = privateKey.getEncoded();
    String privateKeyBase64String = Base64.getEncoder().encodeToString(privateKeyEncoded);
    System.out.println("private key base-64 string=[\n" + privateKeyBase64String + "\n]");

    if (privateKey instanceof PrivateKey) {
      // Get certificate of public key
      Certificate cert = keystore.getCertificate(alias);

      // Get public key
      PublicKey publicKey = cert.getPublicKey();
      System.out.println("public key algorithm=[" + publicKey.getAlgorithm() + "]");
      System.out.println("public key format=[" + publicKey.getFormat() + "]");

      byte[] publicKeyEncoded = publicKey.getEncoded();
      String publicKeyBase64String = Base64.getEncoder().encodeToString(publicKeyEncoded);
      System.out.println("public key base-64 string=[\n" + publicKeyBase64String + "\n]");

      // Return a key pair
      new KeyPair(publicKey, (PrivateKey) privateKey);
    }
  }
}
