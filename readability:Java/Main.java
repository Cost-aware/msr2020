import java.sql.*;


public class Main {

    public static String dbURL = "jdbc:sqlserver://localhost;DatabaseName = sotorrent18_09;";
    public static Connection conn;
    public static Statement stmt;

    public static void main(String[] args) {
        try {
            Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver");
            conn = DriverManager.getConnection(dbURL, "sa", "amir1994");
            if (conn != null) {
                System.out.println("Connected");

                System.out.println("get all the records...");

                stmt = conn.createStatement();

                String sql = "SELECT * FROM FilteredCodeHistory";

                ResultSet rs = stmt.executeQuery(sql);
                int line = 0 ;
                while (rs.next()) {
                    if (line < 404995);
                    else {
                        //Retrieve by column name
                        int rootBlockId = rs.getInt("RootBlockId");
                        int blockId = rs.getInt("BlockId");
                        int lineCount = rs.getInt("LineCount");
                        Timestamp date = rs.getTimestamp("CreationDate");
                        String content = rs.getString("Content");

                        String formattedContent = content.replaceAll("&#xD;&#xA;", "\n\t");

                        float readability = (float) raykernel.apps.readability.eval.Main.getReadability(formattedContent);
                        PreparedStatement stmt = conn.prepareStatement("INSERT INTO ReadabilityResult (RootBlockId, BlockId , CreationDate, LineCount , ReadabilityScore , Content) " +
                                "VALUES(? , ?, ? , ? , ?, ?)");

                        stmt.setInt(1, rootBlockId);
                        stmt.setInt(2, blockId);
                        stmt.setTimestamp(3, date);
                        stmt.setInt(4, lineCount);
                        stmt.setFloat(5, readability);
                        stmt.setString(6, content);

                        stmt.executeUpdate();
                    }
                    System.out.println("reading line " + line);
                    line++;
                }

                System.out.println("DONE!!");
            }
        } catch (SQLException ex) {
            ex.printStackTrace();
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        } finally {
            try {
                if (conn != null && !conn.isClosed()) {
                    conn.close();
                }
            } catch (SQLException ex) {
                ex.printStackTrace();
            }
        }
    }
}
