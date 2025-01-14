import os
import json

def c_to_arabic_no(number):
    western_numbers = '0123456789'
    arabic_numbers = '٠١٢٣٤٥٦٧٨٩'
    translation_table = str.maketrans(western_numbers, arabic_numbers)
    return str(number).translate(translation_table)

def generate_quran_html(json_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    files = [f for f in os.listdir(json_dir) if f.endswith('.json')]

    for file in files:
        with open(os.path.join(json_dir, file), 'r', encoding='utf-8') as f:
            surah = json.load(f)

        file_name = os.path.splitext(file)[0]
        surah_number = int(file_name)
        surah_data = surah[str(surah_number)]

        prev_surah = surah_number - 1 if surah_number > 1 else 114
        next_surah = surah_number + 1 if surah_number < 114 else 1

        html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>quran4universe - {surah_data['name_latin']}</title>
</head>
<body>
<div class="header">
<h1><a style="color:#fff;text-decoration:none;" href="/">quran4universe</a></h1>
<h4>
<a href="{prev_surah}.html">《 </a> {surah_data['name']} ({surah_data['name_latin']}) ({surah_data['translations']['id']['name']})
<a href="{next_surah}.html"> 》</a>
</h4>
<div class="slider-container">
<label for="fontSizeSlider" style="color: white;">ubah ukuran teks:</label>
<input id="fontSizeSlider" type="range" min="12" max="32" value="16" oninput="adjustFontSize(this.value)">
</div>
</div>
<div class="contents">
'''

        for ayah_number, ayah_text in surah_data['text'].items():
            html_content += f'''
<h1>{ayah_text} &#1757{c_to_arabic_no(ayah_number)}</h1><div style="text-align:center">
<p>{ayah_number}. {surah_data['translations']['id']['text'][ayah_number]}</p><hr/></div>'''

        html_content += f'''
</div>
<h4><a href="{prev_surah}.html">《 </a> navigation button <a href="{next_surah}.html"> 》</a></h4>'''+'''
<style type="text/css" media="all">
body {
margin: 0;
padding: 0;
color: #333;
background: linear-gradient(to bottom, #f3f4f6, #e7e9ec);
text-align: center;
font-size: 16px;
}
.header {
background: linear-gradient(135deg, #6c63ff, #4a47a3);
color: white;
padding: 20px 10px;
box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
margin: 0px;
}
.header a {
color: lightblue;
text-decoration: none;
}
a {
color: #6488EA;
text-decoration: none;
}
h1 {
font-family: "LPMQ Isep Misbah", Sans-Serif;
}
.slider-container {
margin-top: 10px;
}
.slider-container input[type="range"] {
width: 80%;
margin: 10px auto;
display: block;
}
.contents {
text-align: right;
margin: 35px;
}
.contents h1 {
  font-weight: normal;
}
@font-face {
font-family: "LPMQ Isep Misbah";
src: url("https://db.onlinewebfonts.com/t/eb289d26afbfd6114ddfdc053113218e.eot");
src: url("https://db.onlinewebfonts.com/t/eb289d26afbfd6114ddfdc053113218e.eot?#iefix") format("embedded-opentype"),
url("https://db.onlinewebfonts.com/t/eb289d26afbfd6114ddfdc053113218e.woff2") format("woff2"),
url("https://db.onlinewebfonts.com/t/eb289d26afbfd6114ddfdc053113218e.woff") format("woff"),
url("https://db.onlinewebfonts.com/t/eb289d26afbfd6114ddfdc053113218e.ttf") format("truetype");
}
</style>
<script>
function adjustFontSize(value) {
document.body.style.fontSize = value + "px";
}
</script>
</body>
</html>
'''

        output_file = os.path.join(output_dir, f'{surah_number}.html')
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html_content)

json_dir = 'quran-json'
output_dir = 'quran-id'
generate_quran_html(json_dir, output_dir)
