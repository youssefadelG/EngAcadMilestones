import paramiko

class Keywords:
    def ssh_to_server(self,ip_address, username, password, command):
        """
        SSH to a server and execute a command.
        
        :param ip_address: The IP address of the server.
        :param username: The username to use for SSH.
        :param password: The password to use for SSH.
        :param command: The command to execute on the server.
        :return: The output of the command.
        """
        try:
            # Create a new SSH client
            ssh = paramiko.SSHClient()

            # Automatically add the server's public key to the known_hosts file
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

            # Connect to the server
            ssh.connect(ip_address, username=username, password=password)
            # Execute the command
            stdin, stdout, stderr = ssh.exec_command(command)
            # Get the command output and error
            output = stdout.read().decode()
            error = stderr.read().decode()
            
            # Close the SSH connection
            ssh.close()
            
            if error:
                return f"Error: {error}"
            return output
        
        except paramiko.AuthenticationException:
            raise Exception("Authentication failed, please verify your credentials")
        except paramiko.SSHException as sshException:
            raise Exception(f"Unable to establish SSH connection: {sshException}")
        except Exception as e:
            raise Exception(f"Exception in connecting to the server: {e}")

