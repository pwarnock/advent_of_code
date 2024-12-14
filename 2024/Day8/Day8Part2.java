import java.io.IOException;
import java.net.URISyntaxException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.*;

public class Day8Part2 {    
    public static void main(String[] args) {    
        // Define the map as a 2D char array    
        // char[][] map = {    
        //     "............".toCharArray(),    
        //     "........0...".toCharArray(),    
        //     ".....0......".toCharArray(),    
        //     ".......0....".toCharArray(),    
        //     "....0.......".toCharArray(),    
        //     "......A.....".toCharArray(),    
        //     "............".toCharArray(),    
        //     "............".toCharArray(),    
        //     "........A...".toCharArray(),    
        //     ".........A..".toCharArray(),    
        //     "............".toCharArray(),    
        //     "............".toCharArray()    
        // };
        
        char[][] map;  

        try {  
            // Read all lines from the input file  
            List<String> lines = Files.readAllLines(Paths.get(Day8.class.getResource("input.txt").toURI()));
    
            // Initialize the map based on the input file  
            map = new char[lines.size()][];  
    
            for (int i = 0; i < lines.size(); i++) {  
                map[i] = lines.get(i).toCharArray();  
            }  
    
        } catch (IOException | URISyntaxException e) {  
            e.printStackTrace(); // Handle the exception  
            return; // Exit the program if the file cannot be read  
        }  

        // Identify frequencies    
        Map<Character, List<Position>> frequencyMap = identifyFrequencies(map);    

        // Find antinodes    
        Set<Position> antinodePositions = findAntinodes(map, frequencyMap);    

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

    // Method to find antinodes based on frequency pairs    
    static Set<Position> findAntinodes(char[][] map, Map<Character, List<Position>> frequencyMap) {    
        Set<Position> antinodesSet = new HashSet<>(); // To collect unique antinode positions    

        for (Map.Entry<Character, List<Position>> entry : frequencyMap.entrySet()) {    
            List<Position> antennas = entry.getValue();    

            if (antennas.size() < 2) {    
                continue; // Skip frequencies with only one antenna    
            }    

            // For all pairs of antennas of the same frequency    
            for (int i = 0; i < antennas.size(); i++) {    
                Position a1 = antennas.get(i);    
                for (int j = i + 1; j < antennas.size(); j++) {    
                    Position a2 = antennas.get(j);    

                    int deltaRow = a2.row - a1.row;    
                    int deltaCol = a2.col - a1.col;    

                    // For each position in the map    
                    for (int row = 0; row < map.length; row++) {    
                        for (int col = 0; col < map[row].length; col++) {    
                            int cross = deltaRow * (col - a1.col) - deltaCol * (row - a1.row);    
                            if (cross == 0) {    
                                Position pos = new Position(row, col);    
                                antinodesSet.add(pos);    

                                // Mark the antinode on the map if it's not an antenna    
                                if (map[row][col] == '.') {    
                                    map[row][col] = '#';    
                                }    
                            }    
                        }    
                    }    
                }    
            }    
        }    

        return antinodesSet;    
    }    

    // Method to print the map    
    static void printMap(char[][] map) {    
        for (char[] row : map) {    
            System.out.println(new String(row));    
        }    
    }    
}    