<!DOCTYPE html>
<html>
	<head>
		<title>set color</title>
	</head>
	<body>
		<?php
			if($_GET) {
				exec('python /home/pi/making-things-smart/web_interface.py '.$_GET['data']);
			}
		?>
		<form action="/sense-hat-set-color.php" name="sense" method="get">
			Data: <input type='text' name='data' />
			<button type='submit'>Send</button> <br /><br />
		</form>
	</body>
</html>
