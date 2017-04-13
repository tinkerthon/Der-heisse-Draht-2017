% rebase('./layout.tpl', title='Rangliste')

<h1>Der heiße Draht - Rangliste</h1>
<h2>Stand: <span class="now"><!-- hier kommt Datum / Uhrzeit rein --></span></h2>

<table>
    <thead>
        <tr>
            <th>Position</th>
            <th>Spieler</th>
            <th>Anzahl</th>
            <th>Zeit</th>
            <th>Berührungen</th>
        </tr>
    </thead>
    <tbody>
        <!-- hier kommen die Ergebnisse rein -->
    </tbody>
</table>

<script src="/static/jquery-3.2.1.min.js"></script>
<script>
// Alle 5s
setInterval(function () {
    // Hole die Ergebnisse
    $.get('/scores', function (data) {
        var lines = '';

        // Aktualisiere Uhrzeit
        $('.now').text(data.now);

        // Sammle Zeilen mit Ergebnissen
        data.scores.forEach(function (score) {
            lines += '<tr><td>' +
                score.rang + '</td><td>' +
                data.names[score.id] + '</td><td>' +
                score.anzahl + '</td><td>' +
                score.zeit + '</td><td>' +
                score.beruehrt + '</td></tr>';
        });

        // ... und füge sie in die Tabelle ein
        $('tbody').html(lines);
    });
}, 5000);
</script>
