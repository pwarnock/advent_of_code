// import java.io.IOException;
// import java.net.URISyntaxException;
// import java.nio.file.Files;
// import java.nio.file.Paths;
import java.util.*;

public class Day8 {  
    public static void main(String[] args) {  
        // Define the map as a 2D char array  
        char[][] map = {  
            "............".toCharArray(),  
            "........0...".toCharArray(),  
            ".....0......".toCharArray(),  
            ".......0....".toCharArray(),  
            "....0.......".toCharArray(),  
            "......A.....".toCharArray(),  
            "............".toCharArray(),  
            "............".toCharArray(),  
            "........A...".toCharArray(),  
            ".........A..".toCharArray(),  
            "............".toCharArray(),  
            "............".toCharArray()  
        };  

        // char[][] map;  

        // try {  
        //     // Read all lines from the input file  
        //     List<String> lines = Files.readAllLines(Paths.get(Day8.class.getResource("input.txt").toURI()));
    
        //     // Initialize the map based on the input file  
        //     map = new char[lines.size()][];  
    
        //     for (int i = 0; i < lines.size(); i++) {  
        //         map[i] = lines.get(i).toCharArray();  
        //     }  
    
        // } catch (IOException | URISyntaxException e) {  
        //     e.printStackTrace(); // Handle the exception  
        //     return; // Exit the program if the file cannot be read  
        // }  

        // Identify frequencies  
        Map<Character, List<Position>> frequencyMap = identifyFrequencies(map);  

        // Place antinodes  
        Set<Position> antinodePositions = placeAntinodes(map, frequencyMap);  

        // Print the updated map  
        printMap(map);  

        // Print the count of antinodes  
        System.out.println("Number of unique antinodes: " + antinodePositions.size());  
    }  

    // Helper class to represent positions on the map  
    static class Position {  
        int row;  
        int col;  

        Position(int row, int col) {  
            this.row = row;  
            this.col = col;  
        }  

        @Override  
        public boolean equals(Object obj) {  
            if (obj instanceof Position) {  
                Position other = (Position) obj;  
                return this.row == other.row && this.col == other.col;  
            }  
            return false;  
        }  

        @Override  
        public int hashCode() {  
            return Objects.hash(row, col);  
        }  
    }  

    // Method to identify frequencies and group their positions  
    static Map<Character, List<Position>> identifyFrequencies(char[][] map) {  
        Map<Character, List<Position>> frequencyMap = new HashMap<>();  

        for (int row = 0; row < map.length; row++) {  
            for (int col = 0; col < map[row].length; col++) {  
                char current = map[row][col];  
                if (current != '.') {  
                    frequencyMap.computeIfAbsent(current, k -> new ArrayList<>()).add(new Position(row, col));  
                }  
            }  
        }  

        return frequencyMap;  
    }  

    // Method to place antinodes based on frequency pairs  
    static Set<Position> placeAntinodes(char[][] map, Map<Character, List<Position>> frequencyMap) {  
        Set<Position> antinodesSet = new HashSet<>(); // To collect unique antinode positions  

        for (Map.Entry<Character, List<Position>> entry : frequencyMap.entrySet()) {  
            List<Position> positions = entry.getValue();  

            // Find all unique pairs  
            for (int i = 0; i < positions.size(); i++) {  
                for (int j = i + 1; j < positions.size(); j++) {  
                    Position a = positions.get(i);  
                    Position b = positions.get(j);  

                    // Calculate direction vector  
                    int deltaRow = b.row - a.row;  
                    int deltaCol = b.col - a.col;  

                    // Antinode positions  
                    Position p1 = new Position(  
                        a.row - deltaRow,  
                        a.col - deltaCol  
                    );  
                    Position p2 = new Position(  
                        b.row + deltaRow,  
                        b.col + deltaCol  
                    );  

                    // Place antinodes if valid and collect their positions  
                    Position antinode1 = placeIfValid(map, p1);  
                    if (antinode1 != null) {  
                        antinodesSet.add(antinode1);  
                    }  
                    Position antinode2 = placeIfValid(map, p2);  
                    if (antinode2 != null) {  
                        antinodesSet.add(antinode2);  
                    }  
                }  
            }  
        }  

        return antinodesSet;  
    }  

    // Method to place antinode if the position is valid and return the position or null  
    static Position placeIfValid(char[][] map, Position pos) {  
        if (pos.row >= 0 && pos.row < map.length && pos.col >= 0 && pos.col < map[pos.row].length) {  
            if (map[pos.row][pos.col] == '.') {  
                map[pos.row][pos.col] = '#';  
            }  
            // Return the position regardless of what's on the map (since antinodes can overlap)  
            return new Position(pos.row, pos.col);  
        }  
        return null;  
    }  

    // Method to print the map  
    static void printMap(char[][] map) {  
        for (char[] row : map) {  
            System.out.println(new String(row));  
        }  
    }  
}  