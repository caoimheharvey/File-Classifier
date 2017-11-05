import subprocess
image_path = "./images/complete-dataset/"
image_name = "01.jpg"
tag = "red,blue,kardashian"

output = subprocess.check_output(['./tagging.sh',image_path, image_name, tag])
print(output)
