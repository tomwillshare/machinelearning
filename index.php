
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">

  <head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>

      <link rel="stylesheet" href="main.css">
      <script src="https://cdnjs.cloudflare.com/ajax/libs/xlsx/0.7.7/xlsx.core.min.js"></script>
      <script src="https://cdnjs.cloudflare.com/ajax/libs/xls/0.7.4-a/xls.core.min.js"></script>
      <script type="text/javascript" src="ExportToTable.js"></script>
  </head>

  <body>

<p> Super Machine learning sales check thingy 2 </p>

<?php
    // Step 2. Handling the cells on the server
    // This part of the file checks to see if a POST request has been made
    // Here you would transform the data into the correct format
    // and then pass it to the machine learning function
    if (isset($_POST['cells'])) {
        $data1 = json_encode($_POST['cells']);
        $result = shell_exec('/anaconda3/bin/python test.py ' . $data1);
        echo $result;
        die();
    }
?>

<!-- Step 1. POSTing the cells from the client -->
<!-- Here you would transform the data from the spreadsheet into a HTML table form -->
<!-- When you submit the form, the browser will make a POST request to itself -->



<form method="POST">
  <input type="file" id="excelfile"/>
     <input type="button" id="viewfile" value="Existing Data" onclick="ExportToTable()" accept=".xlsx, .xls, .csv"/>
        <br />
        <br />
     <table id="exceltable">
     </table>



  <button type="submit">Submit</button>
</form>

<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.0/jquery.min.js"></script>
<script type="text/javascript" src="ExportToTable.js"></script>

</body>
</html>
