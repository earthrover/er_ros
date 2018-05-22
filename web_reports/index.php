<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <title>EARTH ROBOT</title>

    <meta http-equiv="refresh" content="10" />
    <meta http-equiv="cache-control" content="max-age=3000" />

<style>
#flashMe {
  height:4px;
  width:100%;
  background:black;

  animation: flash 3s forwards linear normal;
}
@keyframes flash {
  0% {
    background:white;
  }
  4% {
    background:yellow;
  }
  100% {
    background:grey;
  }
}
</style>
</head>

<body>
ALIVE!
<p>
<div id='flashMe'></div>
<?php
$cmd = 'uptime';
$output = shell_exec($cmd);

echo "<pre>$output</pre>";
?>
<div id='flashMe'></div>
</body>
