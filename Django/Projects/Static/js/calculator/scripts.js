function appendCharacter(char) {
    var result = document.getElementById('result');
    var currentValue = result.value;

    // Check if the last character in the current value is an operator
    var lastChar = currentValue[currentValue.length - 1];
    if (/[\+\-\*\/]/.test(lastChar) && /[\+\-\*\/]/.test(char)) {
        return; // Skip appending the consecutive operator
    }

    // Check if the current value already contains a decimal point within the current number
    if (char === '.') {
        var operators = ['+', '-', '*', '/'];
        var operatorIndex = operators.findIndex(function(op) {
            return currentValue.lastIndexOf(op) > currentValue.lastIndexOf('.');
        });

        if (operatorIndex > -1) {
            var lastOperatorIndex = currentValue.lastIndexOf(operators[operatorIndex]);
            var currentNumber = currentValue.substring(lastOperatorIndex + 1);
            if (currentNumber.includes('.')) {
                return; // Ignore additional dots within the current number
            }
        } else if (currentValue.includes('.')) {
            return; // Ignore additional dots in the overall value
        }
    }

    result.value += char;
}


function deleteCharacter() {
    var result = document.getElementById('result');
    result.value = result.value.slice(0, -1);
}

function clearResult() {
    document.getElementById('result').value = '';
}

function calculate() {
    var result = document.getElementById('result');
    try {
        result.value = eval(result.value);
    } catch (error) {
        result.value = 'Error';
    }
}

function root() {
    var result = document.getElementById('result');
    try {
        result.value = Math.sqrt(eval(result.value));
    } catch (error) {
        result.value = 'Error';
    }
}

function percent() {
    var result = document.getElementById('result');
    try {
        result.value = eval(result.value) / 100;
    } catch (error) {
        result.value = 'Error';
    }
}
