<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>TrafficTelligence - Traffic Estimation</title>
    <style>
       body {
  background-image: url("https://www.bentleymotors.com/content/dam/bm/websites/bmcom/bentleymotors-com/homepage/26my-azure/GT%20Azure%20Dynamic%20Desktop.jpg/_jcr_content/renditions/original.image_file.1286.643.file/GT%20Azure%20Dynamic%20Desktop.jpg");
  background-repeat: no-repeat;
}
    </style>
</head>
<body>
    <h1>TrafficTelligence</h1>
    <p>Advanced Traffic Volume Estimation with Machine Learning</p>

    <form action="/predict" method="post">
        <label>Date & Time:</label><br>
        <input type="text" name="date_time" placeholder="YYYY-MM-DD HH:MM:SS" required><br><br>

        <label>Temperature (°C):</label><br>
        <input type="number" step="0.01" name="temp" required><br><br>

        <label>Rain (mm):</label><br>
        <input type="number" step="0.01" name="rain" required><br><br>

        <label>Snow (mm):</label><br>
        <input type="number" step="0.01" name="snow" required><br><br>

        <label>Cloud Coverage (%):</label><br>
        <input type="number" name="clouds" required><br><br>

        <label>Weather Main:</label><br>
        <input type="text" name="weather_main" placeholder="e.g., Clear, Clouds" required><br><br>

        <label>Weather Description:</label><br>
        <input type="text" name="weather_description" placeholder="e.g., scattered clouds" required><br><br>

        <input type="submit" value="Estimate Traffic Volume">
    </form>
</body>
</html>