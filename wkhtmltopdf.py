import subprocess

url = "https://www.google.com"

output_pdf = "output.pdf"

command = [
    R"/usr/bin/wkhtmltopdf",
    "--disable-smart-shrinking",
    url,
    output_pdf
]

try:
    subprocess.run(command, check=True)
    print(f"PDF generated and saved as '{output_pdf}'")
except subprocess.CalledProcessError as e:
    print(f"Error: {e}")
