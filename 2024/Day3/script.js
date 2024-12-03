async function run() {
    const res = await fetch('https://adventofcode.com/2024/day/3/input');
    const text = await res.text();
    
    // Pattern for both mul expressions and do/don't commands
    const pattern = /(?:mul\((\d+),(\d+)\)|do\(\)|don't\(\))/g;
    
    // Variables for state and results
    const numberPairs = [];
    let aggregateResult = 0;
    let isAggregating = true; // Start in "do" state
    
    // Find all matches and process them
    let match;
    while ((match = pattern.exec(text)) !== null) {
        if (match[0] === 'do()') {
            isAggregating = true;
            continue;
        }
    
        if (match[0] === "don't()") {
            isAggregating = false;
            continue;
        }
    
        if (isAggregating && match[1] && match[2]) {
            const num1 = parseInt(match[1]);
            const num2 = parseInt(match[2]);
            numberPairs.push([num1, num2]);
            aggregateResult += num1 * num2;
        }
    }
    
    // Calculate all multiplications that were aggregated
    const results = numberPairs.map(([num1, num2]) => ({
        numbers: [num1, num2],
        result: num1 * num2
    }));
    
    // Print results
    results.forEach(({numbers, result}) => {
        console.log(`${numbers[0]} × ${numbers[1]} = ${result}`);
    });
    
    console.log(`Final aggregate: ${aggregateResult}`);
    return aggregateResult;
}; run();