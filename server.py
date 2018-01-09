import cherrypy; 


class CMSAppApi(object) : 	
	@cherrypy.expose
	def lunher(self, *args, **kwargs):
		return open("/media/imp/NeoCyberSpace/proziod/PMS/ProziodPMS/dist/index.html"); 
	 
	
if __name__ == "__main__" : 
	cherrypy.config.update({'tools.sessions.on': True,
                        'tools.sessions.timeout': 10
               }),
	cherrypy.config.update({'server.socket_host': '192.168.2.4', 'server.socket_port': 80, }) 
	cherrypy.quickstart(CMSAppApi(),'/',config={'/': {
                'tools.staticdir.on': True,
                'tools.staticdir.dir': '/media/imp/NeoCyberSpace/ProziodWebLuncher/dist',
                'tools.staticdir.index': 'index.html',
            }}); 
	
	
	
			