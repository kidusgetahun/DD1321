<?php
putenv("PYTHONIOENCODING=utf-8");    // Konfigurera webbservern att använda UTF-8 
putenv("LANG=C.UTF-8");

error_reporting(E_ALL);              // Sätt på php-felmeddelanden
ini_set('display_errors', 1);

$first = $_GET["first"];                   // Spara GET-parametrarna
$last  = $_GET["last"];
$first = preg_replace ("/[^a-zåäö]/", "", $first); // Byt, av säkerhetskäl ut icke-bokstäver
$last  = preg_replace ("/[^a-zåäö]/", "", $last);  // i GET-parametrarna
?>
<html>
<body>

första ordet:  <?php echo $first; ?><br>
andra ordet: <?php echo $last; ?>

<h2>python program</h2>

<?php
// Kör pythonprogrammet och skriv ut (echo) i webbläsaren
echo shell_exec("python3 d63.py " . $first . " " . $last . " 2>&1 ");
?>

</body>
</html>
