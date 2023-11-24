from pyngrok import ngrok
import subprocess

# Start your Django server (replace this with your Django server start command)
subprocess.Popen(['python3', 'manage.py', 'runserver', '0.0.0.0:8005'])

# Open a Ngrok tunnel to your Django server
public_url = ngrok.connect(8005)  # Replace '8000' with your Django server port
print("Public URL:", public_url)

# Keep the tunnel open until interrupted
input("Press Enter to exit...\n")

# Clean up: disconnect Ngrok and stop it
ngrok.disconnect(public_url)
ngrok.kill()


## TO RUN NGROK > python3 ngrok_setup.py
