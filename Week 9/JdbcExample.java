

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;
import java.sql.PreparedStatement;

public class jdbc{
    public static void main(String[] args) {
        // Database credentials
        String url = "jdbc:mysql://localhost:3306/smart_city";
        String user = "root";
        String password = "Aryan@mysql136";

        Connection connection = null;
        PreparedStatement pstmt = null;
        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
            connection = DriverManager.getConnection(url, user, password);
            System.out.println(" Connected to the MySQL database successfully!");

            Statement stmt = connection.createStatement();

            String s1 = """
            CREATE TABLE citizens (
                username VARCHAR(50) NOT NULL UNIQUE,
                email VARCHAR(255) NOT NULL UNIQUE,
                password VARCHAR(255) NOT NULL
            );
        """;
            String s2 = "CREATE TABLE IF NOT EXISTS complain_log (" +
                    "id INT AUTO_INCREMENT PRIMARY KEY, " +
                    "username VARCHAR(50) NOT NULL, " +
                    "category VARCHAR(100) NOT NULL, " +
                    "description TEXT NOT NULL" +
                    ")";

            stmt.executeUpdate(s1);
            System.out.println(" Table 'citizen' created successfully!");
            stmt.executeUpdate(s2);
            System.out.println(" Table 'complain_log' created successfully!");
            String x = "INSERT INTO citizens (username, email, password) VALUES (?, ?, ?)";

            pstmt = connection.prepareStatement(x);

            pstmt.setString(1, "aryan_raj");
            pstmt.setString(2, "aryanraj@gmail.com");
            pstmt.setString(3, "aryan123");
            pstmt.executeUpdate();

            pstmt.setString(1, "john_doe");
            pstmt.setString(2, "john@gmail.com");
            pstmt.setString(3, "john@321");
            pstmt.executeUpdate();

            System.out.println(" 2 records inserted successfully into 'citizens' table!");
            String y = "INSERT INTO complain_log (username, category, description) VALUES (?, ?, ?)";
            pstmt = connection.prepareStatement(y);

            pstmt.setString(1, "aryan_raj");
            pstmt.setString(2, "Water Supply");
            pstmt.setString(3, "Water supply has been irregular for the past two days in Sector 5.");
            pstmt.executeUpdate();

            pstmt.setString(1, "john_doe");
            pstmt.setString(2, "Electricity");
            pstmt.setString(3, "Frequent power cuts during night hours in Green Park area.");
            pstmt.executeUpdate();

            System.out.println(" 2 complaint records inserted successfully into 'complain_log' table!");


        } catch (ClassNotFoundException e) {
            System.out.println(" MySQL JDBC Driver not found. Add the connector JAR to your classpath.");
            e.printStackTrace();
        } catch (SQLException e) {
            System.out.println(" Database connection error!");
            e.printStackTrace();
        } finally {
            try {
                if (connection != null && !connection.isClosed()) {
                    connection.close();
                    System.out.println(" Database connection closed.");
                }
            } catch (SQLException e) {
                e.printStackTrace();
            }
        }
    }
}