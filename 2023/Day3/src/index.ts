import 'module-alias/register';
import { promises as fs } from "fs";
import path from 'path';

interface MatchResult {
    sum: number;
    matchCount: number;
}

interface Position {
    row: number;
    col: number;
}

interface PartNumber {
    value: number;
    startIdx: number;
    endIdx: number;
    row: number;
}

async function fetchText(): Promise<string> {
    try {
        const inputPath = path.resolve(__dirname, '../data/input.txt');
        const text = await fs.readFile(inputPath, 'utf8');
        return text;
    } catch (error) {
        console.error('Error fetching input:', error);
        throw error;
    }
}

class SchematicAnalyzer {
    private schematic: string[];
    private height: number;
    private width: number;

    constructor(input: string) {
        this.schematic = input.split('\n');
        this.height = this.schematic.length;
        this.width = this.schematic[0].length;
    }

    public solvePart1(): MatchResult {
        const numbers: number[] = [];

        for (let i = 0; i < this.height; i++) {
            const line = this.schematic[i];
            const prevLine = i > 0 ? this.schematic[i-1] : '';
            const nextLine = i < this.height - 1 ? this.schematic[i+1] : '';

            const numberMatches = [...line.matchAll(/\d+/g)];

            for (const match of numberMatches) {
                const num = parseInt(match[0]);
                const startIdx = match.index!;
                const endIdx = startIdx + match[0].length - 1;

                if (this.hasAdjacentSymbol(prevLine, line, nextLine, startIdx, endIdx)) {
                    numbers.push(num);
                }
            }
        }

        return {
            sum: numbers.reduce((acc, curr) => acc + curr, 0),
            matchCount: numbers.length
        };
    }

    public solvePart2(): MatchResult {
        const gearRatios: number[] = [];
        const partNumbers = this.findPartNumbers();

        for (let row = 0; row < this.height; row++) {
            for (let col = 0; col < this.width; col++) {
                if (this.schematic[row][col] === '*') {
                    const adjacentNumbers = this.findAdjacentNumbers(
                        { row, col },
                        partNumbers
                    );

                    if (adjacentNumbers.length === 2) {
                        gearRatios.push(adjacentNumbers[0] * adjacentNumbers[1]);
                    }
                }
            }
        }

        return {
            sum: gearRatios.reduce((acc, curr) => acc + curr, 0),
            matchCount: gearRatios.length
        };
    }

    private hasAdjacentSymbol(prevLine: string, currentLine: string, nextLine: string, startIdx: number, endIdx: number): boolean {
        const checkRange = {
            start: Math.max(0, startIdx - 1),
            end: Math.min(currentLine.length - 1, endIdx + 1)
        };

        const isSymbol = (char: string) => char !== '.' && isNaN(parseInt(char));

        if (prevLine) {
            for (let i = checkRange.start; i <= checkRange.end; i++) {
                if (isSymbol(prevLine[i])) return true;
            }
        }

        if (checkRange.start < startIdx && isSymbol(currentLine[checkRange.start])) return true;
        if (checkRange.end > endIdx && isSymbol(currentLine[checkRange.end])) return true;

        if (nextLine) {
            for (let i = checkRange.start; i <= checkRange.end; i++) {
                if (isSymbol(nextLine[i])) return true;
            }
        }

        return false;
    }

    private findPartNumbers(): PartNumber[] {
        const partNumbers: PartNumber[] = [];

        for (let row = 0; row < this.height; row++) {
            const line = this.schematic[row];
            const numberMatches = [...line.matchAll(/\d+/g)];

            for (const match of numberMatches) {
                partNumbers.push({
                    value: parseInt(match[0]),
                    startIdx: match.index!,
                    endIdx: match.index! + match[0].length - 1,
                    row
                });
            }
        }

        return partNumbers;
    }

    private findAdjacentNumbers(gearPos: Position, partNumbers: PartNumber[]): number[] {
        const adjacentNumbers = new Set<number>();

        for (const partNumber of partNumbers) {
            if (Math.abs(partNumber.row - gearPos.row) <= 1) {
                const numberRange = {
                    start: partNumber.startIdx - 1,
                    end: partNumber.endIdx + 1
                };

                if (gearPos.col >= numberRange.start && gearPos.col <= numberRange.end) {
                    adjacentNumbers.add(partNumber.value);
                }
            }
        }

        return Array.from(adjacentNumbers);
    }
}

async function part1(input: string): Promise<MatchResult> {
    try {
        const analyzer = new SchematicAnalyzer(input);
        return analyzer.solvePart1();
    } catch (error) {
        console.error('Error processing input:', error);
        throw error;
    }
}

async function part2(input: string): Promise<MatchResult> {
    try {
        const analyzer = new SchematicAnalyzer(input);
        return analyzer.solvePart2();
    } catch (error) {
        console.error('Error processing input:', error);
        throw error;
    }
}

async function execute() {
    try {
        const input = await fetchText();
        const part1Result = await part1(input);
        const part2Result = await part2(input);

        console.log('Part 1 Results:', part1Result);
        console.log('Part 2 Results:', part2Result);
    } catch (error) {
        console.error('Failed to execute:', error);
    }
}

// Execute both parts
execute();