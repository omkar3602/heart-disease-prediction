function populateSelect(target, min, max) {
    if (!target) {
        return false;
    }
    else {
        select = document.getElementById(target);

        for (var i = min; i <= max; i++) {
            var opt = document.createElement('option');
            opt.value = i;
            opt.innerHTML = i;
            select.appendChild(opt);
        }
    }
}

populateSelect('physical', 0, 30);
populateSelect('mental', 0, 30);
populateSelect('sleep', 1, 24);


function addCategories(target, categories) {
    if (!target) {
        return false;
    }
    else {
        select = document.getElementById(target);

        // for each element in the array, create an option
        for (var i = 0; i < categories.length; i++) {
            var opt = document.createElement('option');
            opt.value = categories[i];
            opt.innerHTML = categories[i];
            select.appendChild(opt);
        }
    }
}

addCategories("age", ['18-24',
    '25-29',
    '30-34',
    '35-39',
    '40-44',
    '45-49',
    '50-54',
    '55-59',
    '60-64',
    '65-69',
    '70-74',
    '75-79',
    '80 or older']);

addCategories("race", ['American Indian/\nAlaskan Native',
    'Asian',
    'Black',
    'Hispanic',
    'Other',
    'White',]);

addCategories("health", ['Poor', 'Fair', 'Good', 'Very good', 'Excellent']);