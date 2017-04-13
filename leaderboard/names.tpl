% rebase('./layout.tpl', title='Teilnehmerliste')

<h1>Der heiße Draht - Teilnehmerliste</h1>

<form method="POST">

    <table>
        <thead>
            <tr>
                <th>ID</th>
                <th>Name</th>
            </tr>
        </thead>
        <tbody>
            % for id in range(1, 16):
            <tr>
                <td>{{id}}</td>
                <td><input type="text" name="names.{{id}}" value="{{names[id] if id in names else ''}}"></td>
            </tr>
            % end
        </tbody>
    </table>

    <button class="button-primary" type="submit">Speichern</button>

</form>
