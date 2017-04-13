% rebase('./layout.tpl', title='Rangliste')

<h1>Der heiße Draht - Rangliste</h1>
<h2>Stand: <span class="now"><!-- hier kommt Datum / Uhrzeit rein --></span></h2>

<table>
    <thead>
        <tr>
            <th>Position</th>
            <th>Spieler</th>
            <th>Anzahl</th>
            <th>∅ Zeit</th>
            <th>∅ Berührungen</th>
            <th>∅ Punkte</th>
        </tr>
    </thead>
    <tbody>
        <!-- hier kommen die Ergebnisse rein -->
    </tbody>
</table>

<script src="/static/jquery-3.2.1.min.js"></script>
<script>
function round2(number) {
    var factor = 100,
        n100 = number * factor,
        rounded = Math.round(n100);
    return rounded / factor;
};

// Alle 5s
setInterval(function () {
    // Hole die Ergebnisse
    $.get('/scores', function (data) {
        var lines = '';

        // Aktualisiere Uhrzeit
        $('.now').text(data.now);

        // Sammle Zeilen mit Ergebnissen
        data.scores.forEach(function (score, i) {
            lines += '<tr><td>' +
                (i+1) + '</td><td>' +
                data.names[score.id] + '</td><td>' +
                score.anzahl + '</td><td>' +
                Math.round(score.zeit / score.anzahl) + '</td><td>' +
                Math.round(score.beruehrt / score.anzahl) + '</td><td>' +
                round2(score.punkte / score.anzahl) + '</td></tr>';
        });

        // ... und füge sie in die Tabelle ein
        $('tbody').html(lines);
    });
}, 5000);
</script>
