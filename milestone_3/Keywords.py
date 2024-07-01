from robot.api import logger
import paramiko
import os
import getpass

class Keywords:
    ROBOT_LIBRARY_SCOPE = "GLOBAL"
    def __init__(self, ip_address) -> None:
        self.username = None
        self.password = None
        self.ssh_to_server(ip_address=ip_address)
    
    def add_credentials(self) -> None:
        """
        Adds credentials to the object by retrieving them from the environment variables or prompting the user for input.

        :return: None
        """
        if self.username is None:
            if os.environ.get("USERNAME"):
                self.username = os.environ.get("USERNAME") 
            else:
                logger.info(f"Please input value for USERNAME:", also_console=True)
                self.username = input()
        if self.password is None:
            self.password = os.environ.get("PASSWORD") if os.environ.get("PASSWORD") else getpass.getpass(f"Please input password:")

    def ssh_to_server(self,ip_address) -> None:
        """
        SSH to a server and execute a command.
        
        :param ip_address: The IP address of the server.
        :param username: The username to use for SSH.
        :param password: The password to use for SSH.
        :param command: The command to execute on the server.
        :return: The output of the command.
        """
        # if self.username is None or self.password is None:
        self.add_credentials()
        try:
            # Create a new SSH client
            self.ssh = paramiko.SSHClient()

            # Automatically add the server's public key to the known_hosts file
            self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

            # Connect to the server
            self.ssh.connect(ip_address, username=self.username, password=self.password)
        
        except paramiko.AuthenticationException:
            raise Exception("Authentication failed, please verify your credentials")
        except paramiko.SSHException as sshException:
            raise Exception(f"Unable to establish SSH connection: {sshException}")
        except Exception as e:
            raise Exception(f"Exception in connecting to the server: {e}")
    
    def send_command(self, command) -> str:
        try:
            # Execute the command
            stdin, stdout, stderr = self.ssh.exec_command(command)
            # Get the command output and error
            output = stdout.read().decode()
            error = stderr.read().decode()
            if output:
                logger.info(output)
                return output
            else:
                raise Exception(f"Failed due to error:{error}")
        except Exception as e:
            raise Exception("Failed to execute command due to error:" + str(e))
        
    def check_images(self, image):
        try:
            image_exists = self.send_command(f"podman images | grep {image} | wc -l")
            return int(image_exists)
        except Exception as e:
            raise Exception(f"Failed to check Image {image}")
    
    def build_image(self, image, path_to_directory) -> None:
        try:
            self.send_command(f"cd {path_to_directory} && podman build -t {image}")
        except Exception as e:
            raise Exception(f"Failed to build image {image} due to error: {e}")
    def close_session(self) -> None:
        self.ssh.close()
