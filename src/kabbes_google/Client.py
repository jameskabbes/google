import kabbes_google
import kabbes_client

class Client( kabbes_google.Service ):

    _BASE_DICT = {}

    def __init__( self, *args, dict={}, root_dict={}, init_service=True, **kwargs ):

        d = {}
        d.update( Client._BASE_DICT )
        d.update( dict )

        root_inst = kabbes_client.Root( root_dict=root_dict )
        self.Package = kabbes_client.Package( kabbes_google._Dir, dict=d, root=root_inst )
        self.cfg = self.Package.cfg

        if init_service:
            self.init_service_func( *args, **kwargs )

    def init_service_func(self, *args, **kwargs):
        kabbes_google.Service.__init__( self, *args, **kwargs )
