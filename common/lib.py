#!python3 -u

import argparse
import subprocess
import sys, os
import logging

def init_logger(log_path):
  logging.basicConfig(
          level=logging.INFO,
          format="[%(levelname)s][%(asctime)s] %(message)s",
          handlers=[
            logging.FileHandler(log_path, mode='a'),
            logging.StreamHandler()
          ]
  )

def build():
  parser = argparse.ArgumentParser(description="Build docker image")
  parser.add_argument('--image-name', type=str, required=True, help="the real image name will suffix with the use name")
  parser.add_argument('--build-dir', type=str, required=True, help="The dir where Dockerfile in")
  parser.add_argument('--dockerfile', type=str, required=False, default="Dockerfile", help="The Dockerfile path")
  parser.add_argument('--sudo', action="store_true", default=False, help="Use sudo to run docker?")
  args = parser.parse_args()
  init_logger("build.log")

  user_id = subprocess.check_output('id -u', shell=True, text=True).strip()
  user_name = "docker" # subprocess.check_output('id -u -n', shell=True, text=True).strip()
  group_id = subprocess.check_output('id -g', shell=True, text=True).strip()
  group_name = subprocess.check_output('id -g -n', shell=True, text=True).strip()
  home_dir = os.path.expanduser('~')

  logging.info(f"""Create a docker image with:
  image name: {args.image_name}
  user: {user_name}({user_id})
  group: {group_name}({group_id})
""")

  docker_build_cmd = f"docker build --tag {args.image_name} --build-arg DOCKER_USER_ID={user_id} --build-arg DOCKER_USER_NAME={user_name} --build-arg DOCKER_GROUP_ID={group_id} --build-arg DOCKER_GROUP_NAME={group_name} --build-arg DOCKER_HOME_DIR={home_dir} {args.build_dir} --file {args.dockerfile}"

  if args.sudo:
    docker_build_cmd = "sudo " + docker_build_cmd

  logging.info(docker_build_cmd)

  os.system(docker_build_cmd)

def run():
  parser = argparse.ArgumentParser(description="Build docker image")
  parser.add_argument('--image-name', type=str, required=True, help="the real image name will suffix with the use name")
  parser.add_argument('--ssh-port', type=str, required=True, help="The ssh port to connect the container")
  parser.add_argument('--sudo', action="store_true", default=False, help="Use sudo to run docker?")
  parser.add_argument('--volume', nargs="+", help="Volume map when run docker, like --volume path1 path2 to -v path1:path1 -v path2:paht2")
  args = parser.parse_args()
  init_logger("run.log")

  volume_map = ""
  if args.volume:
    paths = map(lambda p: p + ":" + p, map(lambda p: os.path.abspath(p), args.volume))
    volume_map = "--volume " + (" --volume ".join(paths))
  docker_run_cmd = f"docker run --privileged --detach --publish 127.0.0.1:{args.ssh_port}:22/tcp {volume_map} {args.image_name}"

  if args.sudo:
    docker_run_cmd = "sudo " + docker_run_cmd

  logging.info(docker_run_cmd)
  container_id = subprocess.check_output(docker_run_cmd, shell=True, text=True).strip()
  user_name = subprocess.check_output('id -u -n', shell=True, text=True).strip()

  sudo = "sudo " if args.sudo else ""
  logging.info(f"you can view the output by run: `{sudo}docker logs -f {container_id}`")
  logging.info(f"you can kill the daemon container by run: `{sudo}docker container kill {container_id}`")
  logging.info(f"now you can use ssh login this container by run (password is 1): `ssh {user_name}@localhost -p {args.ssh_port}`")
  logging.info("you can these messages in run.log file")
