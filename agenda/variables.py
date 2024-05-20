OUTPUT_PATH = "C:/Users/JuanC/Desktop/Agenda/prototype-iris/output/"
IMG_PATH = OUTPUT_PATH + "img/"
HTML_HEADER = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@100..900&family=Micro+5&display=swap" rel="stylesheet">
    <title>Agenda</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
<h1>Iris dataset Agenda Report</h1>
"""
HTML_CLOSER = """
</body>
</html>               
"""
CSS = """
html {
    scroll-behavior: smooth;
    font-family: 'Inter', sans-serif;
    display: flex;
    justify-content: center;
}

* {
    margin: 0px;
    padding: 0px;
    text-decoration: none;  
    font-size: 14pt;
    font-weight: 500;
    color: #000063d8;
    font-style: normal;
    text-align: justify;
    line-height: 1.5;
}

body {
    padding-left: 16vw;
    padding-right: 16vw;
    padding-top: 8vh;
    padding-bottom: 4vh;
}

h1 {
    font-size: 36pt;
    font-weight: 800;
}

h2 {
    font-size: 24pt;
    font-weight: 700;
}

img {
    max-width: 80vw;
    max-height: 50vh;
    display: block;
    margin-left: auto;
    margin-right: auto;
}
"""
