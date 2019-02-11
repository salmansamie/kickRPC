
from fabric import Connection
import invoke

__author__ = 'salmansamie'


class F5RPC(object):
    
    """ 
    TODO Prod:  ssh port to default
                getpass.getpass()
                getpass.getuser
    """
    def __init__(self, f5_host, f5_port, userid, passwd, runcmd):
        self.f5_host = f5_host
        self.f5_port = f5_port
        self.passwd = passwd
        self.userid = userid
        self.runcmd = runcmd

    def ssh_connection(self):
        try:
            contained = Connection(host=self.f5_host,
                                   user=self.userid,
                                   connect_kwargs={
                                       'password': self.passwd},
                                   port=self.f5_port)

            contained.run(self.runcmd)
            contained.close()
            return str(contained)
        
        except invoke.exceptions.UnexpectedExit:
            print("\nInvoke exception occurred!\nCommand may not exist on the remote")


if __name__=="__main__":
    bashEOF = open("remote.sh", "r").read()             # TODO Prod: bashscript fd is here

    exec_remote = F5RPC(f5_host="ip_address",
                        f5_port=22,
                        userid="remote_user",
                        passwd="remote_pass",
                        runcmd=bashEOF,
                        ).ssh_connection()
