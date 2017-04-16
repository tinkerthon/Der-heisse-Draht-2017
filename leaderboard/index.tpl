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
            <th>&nbsp;</th>
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

function draw() {
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
              round2(score.punkte / score.anzahl) + '</td><td>' +
              '<a class="del" data-name="' + encodeURI(data.names[score.id]) +
              '" href="/del/' + score.id + '">löschen</a></td></tr>';
      });

      // ... und füge sie in die Tabelle ein
      $('tbody').html(lines);
  });
}

// Alle 5s
setInterval(draw, 5000);

$('body').on('click', 'a.del', function (e) {
    e.preventDefault();
    if (confirm('Wirklich ' + $(e.target).data('name') + ' löschen?')) {
        $.post($(e.target).attr('href'), draw);
    }
});

</script>
