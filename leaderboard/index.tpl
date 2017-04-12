<!doctype html>
<html lang="en">
	<head>
		<meta charset="utf-8">
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<meta name="author" content="Dr. Olav Schettler">
		<meta name="description" content="Rangliste.">
		<title>Rangliste | Ostern 2017</title>
		<link rel="icon" href="/icon.png">
		<link rel="stylesheet" href="/static/normalize.css">
		<link rel="stylesheet" href="/static/milligram.min.css">
		<link rel="stylesheet" href="/static/main.css">
	</head>
	<body>

        <main class="container">

    		<h1>Der heiße Draht - Rangliste</h1>
            <h2>Stand: <span class="jetzt"><!-- hier kommt Datum / Uhrzeit rein --></span></h2>

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

        </main>

        <script src="/static/jquery-3.2.1.min.js"></script>
        <script>
        // Alle 5s
        setInterval(function () {
            // Hole die Ergebnisse
            $.get('/scores', function (data) {
                var zeilen = '';

                // Aktualisiere Uhrzeit
                $('.jetzt').text(data.jetzt);

                // Sammle Zeilen mit Ergebnissen
                data.scores.forEach(function (score) {
                    zeilen += '<tr><td>' +
                        score.rang + '</td><td>' +
                        data.namen[score.id] + '</td><td>' +
                        score.anzahl + '</td><td>' +
                        score.zeit + '</td><td>' +
                        score.beruehrt + '</td></tr>';
                });

                // ... und füge sie in die Tabelle ein
                $('tbody').html(zeilen);
            });
        }, 5000);
        </script>

	</body>
</html>
