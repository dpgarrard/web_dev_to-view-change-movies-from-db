<html>
<head> <title>Login form</title>
</head>
<body>

<p><strong>Please Log in.</strong></p>

<form action="/addmovie" method="post"> 

  <p><input name="title" type="text" size="20"> title</p>
  <p><input name="description" type="text" size="80"> description</p>
  <p>release year is the users default year</p>
  <p><input name="length" type="text" value='0' size="5"> length</p>

  <p><select name="category"> category
      <option value='1'>Action</option>
      <option value='2'>Animation</option>
      <option value='3'>Children</option>
      <option value='4'>Classics</option>
      <option value='5'>Comedy</option>
      <option value='6'>Documentary</option>
      <option value='7'>Drama</option>
      <option value='8'>Family</option>
      <option value='9'>Foreign</option>
      <option value='10'>Horror</option>
      <option value='11'>Musical</option>
      <option value='12'>Sci-Fi</option>
    </select>
  </p>


  <p><input type="submit"></p>

</form>

</body>
</html>