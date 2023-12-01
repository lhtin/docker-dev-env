#!python3 -u

import argparse
import subprocess

parser = argparse.ArgumentParser(description="Build docker image")
parser.add_argument('--image-name', type=str, required=True, help="the real image name will suffix with the use name")
parser.add_argument('--ssh-port', type=str, required=True, help="The ssh port to connect the container")
parser.add_argument('--sudo', action="store_true", default=False, help="Use sudo to run docker?")
args = parser.parse_args()

docker_run_cmd = f"docker run -d -p 127.0.0.1:{args.ssh_port}:22/tcp {args.image_name}"
if args.sudo:
    docker_run_cmd = "sudo " + docker_run_cmd

print(docker_run_cmd)

container_id = subprocess.check_output(docker_run_cmd, shell=True, text=True).strip()
user_name = subprocess.check_output('id -u -n', shell=True, text=True).strip()

print(f"you can view the output by run: docker logs -f {container_id}")
print(f"you can kill the daemon container by run: docker container kill {container_id}")
print(f"now you can use ssh login this container by run: ssh {user_name}@localhost -p {args.ssh_port}")
