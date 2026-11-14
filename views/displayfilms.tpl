<html>
<head></head>
<body>
<h1>Film Data</h1>
<p><a href="/login"> <button type="button">Main Menu</button></a></p>
<table cellspacing="9">
<tr>
<th>film_id</th><th>title</th><th>description</th>
<th>year</th><th>length</th><th>category</th>
</tr>
    %for row in rows:
    <tr>
        %for col in row:
            <td>{{col}}</td>
        %end
    </tr>    
    %end    

</table>
</body>
</html>