#!python3 -u

import argparse
import subprocess
import os

parser = argparse.ArgumentParser(description="Build docker image")
parser.add_argument('--image-name', type=str, required=True, help="the real image name will suffix with the use name")
parser.add_argument('--build-dir', type=str, required=True, help="The dir where Dockerfile in")
parser.add_argument('--dockerfile', type=str, required=False, default="Dockerfile", help="The Dockerfile path")
parser.add_argument('--sudo', action="store_true", default=False, help="Use sudo to run docker?")
args = parser.parse_args()

user_id = subprocess.check_output('id -u', shell=True, text=True).strip()
user_name = subprocess.check_output('id -u -n', shell=True, text=True).strip()
group_id = subprocess.check_output('id -g', shell=True, text=True).strip()
group_name = subprocess.check_output('id -g -n', shell=True, text=True).strip()
home_dir = os.path.expanduser('~')

print(f"""Create a docker image with:
  image name: {args.image_name}
  user: {user_name}({user_id})
  group: {group_name}({group_id})
""")

docker_build_cmd = f"docker build -f {args.dockerfile} -t {args.image_name} --build-arg DOCKER_USER_ID={user_id} --build-arg DOCKER_USER_NAME={user_name} --build-arg DOCKER_GROUP_ID={group_id} --build-arg DOCKER_GROUP_NAME={group_name} --build-arg DOCKER_HOME_DIR={home_dir} {args.build_dir}"

if args.sudo:
    docker_build_cmd = "sudo " + docker_build_cmd

print(docker_build_cmd)

os.system(docker_build_cmd)
