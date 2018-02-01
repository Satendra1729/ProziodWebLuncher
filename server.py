import cherrypy; 


class CMSAppApi(object) : 	
	@cherrypy.expose
	def lunher(self, *args, **kwargs):
		return open("D:/satendraData/ExpAndDev/Dev/ProziodWebLuncher/dist/index.html"); 
	 
	
if __name__ == "__main__" : 
	cherrypy.config.update({'tools.sessions.on': True,
                        'tools.sessions.timeout': 10
               }),
	cherrypy.config.update({'server.socket_host': 'localhost', 'server.socket_port': 8080, }) 
	cherrypy.quickstart(CMSAppApi(),'/',config={'/': {
                'tools.staticdir.on': True,
                'tools.staticdir.dir': 'D:/satendraData/ExpAndDev/Dev/ProziodWebLuncher/dist',
                'tools.staticdir.index': 'index.html',
            }}); 
	
	
	
			