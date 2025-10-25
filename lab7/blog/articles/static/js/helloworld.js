// Пример данных
var groupmates = [
    {
        "name": "Павел",
        "surname": "Семеновых",
        "group": "БСТ2201",
        "marks": [4, 4, 5, 5, 3, 4, 4]
    },
    {
        "name": "Александр",
        "surname": "Блинов",
        "group": "БСТ2201",
        "marks": [5, 4, 5, 5, 5, 4, 4]
    },
    {
        "name": "Анатолий",
        "surname": "Жабров",
        "group": "БСТ2201",
        "marks": [3, 4, 5, 5, 4, 3, 3]
    },
    {
        "name": "Кирилл",
        "surname": "Гринёв",
        "group": "БСТ2202",
        "marks": [5, 5, 4, 5, 5, 5, 5]
    },
    {
        "name": "Ольга",
        "surname": "Кузнецова",
        "group": "БСТ2202",
        "marks": [4, 4, 5, 4, 5, 4, 4]
    },
    {
        "name": "Мария",
        "surname": "Лебедева",
        "group": "БСТ2203",
        "marks": [5, 5, 5, 5, 5, 5, 5]
    },
    {
        "name": "Иван",
        "surname": "Соловьёв",
        "group": "БСТ2203",
        "marks": [3, 4, 3, 4, 4, 3, 4]
    },
    {
        "name": "Екатерина",
        "surname": "Фомина",
        "group": "БСТ2201",
        "marks": [4, 5, 4, 5, 5, 5, 5]
    },
    {
        "name": "Андрей",
        "surname": "Поляков",
        "group": "БСТ2204",
        "marks": [3, 3, 4, 3, 3, 4, 3]
    },
    {
        "name": "Дарья",
        "surname": "Романова",
        "group": "БСТ2204",
        "marks": [5, 5, 5, 4, 5, 5, 4]
    }
];



// Фильтрация по средней оценке
function filterByAverageMark(students, minAvg) {
    var filtered = [];
    for (var i = 0; i < students.length; i++) {
        var marks = students[i]['marks'];
        var avg = marks.reduce((a, b) => a + b, 0) / marks.length;
        if (avg > minAvg) {
            filtered.push(students[i]);
        }
    }
    return filtered;
}

// Генерация HTML-таблицы для студентов
function renderStudents(students) {
    var resultDiv = document.querySelector('.students-result');
    if (students.length === 0) {
        resultDiv.innerHTML = "<b>Нет студентов с таким средним баллом.</b>";
        return;
    }
    var html = '<table><tr><th>Имя</th><th>Фамилия</th><th>Группа</th><th>Оценки</th></tr>';
    for (var i = 0; i < students.length; i++) {
        html += '<tr>' +
            '<td>' + students[i]['name'] + '</td>' +
            '<td>' + students[i]['surname'] + '</td>' +
            '<td>' + students[i]['group'] + '</td>' +
            '<td>' + students[i]['marks'].join(", ") + '</td>' +
            '</tr>';
    }
    html += '</table>';
    resultDiv.innerHTML = html;
}

// Обработчик кнопки фильтрации
function showFilteredStudents() {
    var minAvg = parseFloat(document.getElementById('minAverage').value);
    var filtered = filterByAverageMark(groupmates, minAvg);
    renderStudents(filtered);
}