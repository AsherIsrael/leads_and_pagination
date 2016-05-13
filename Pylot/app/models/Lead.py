from system.core.model import Model

class Lead(Model):
	def __init__(self):
		super(Lead, self).__init__()

	def get_leads(self, info):
		print "get_leads"
		get_leads_query = "SELECT *, (SELECT COUNT(*) FROM leads WHERE CONCAT(first_name,' ',last_name) like %s AND registered_datetime > %s AND registered_datetime < %s) as lead_count FROM leads WHERE CONCAT(first_name,' ',last_name) like %s AND registered_datetime > %s AND registered_datetime < %s"
		content = [info['name'], info['from'], info['up_to'], info['name'], info['from'], info['up_to']]
		return self.db.query_db(get_leads_query, content)
		
	def get_sub_leads(self, info):
		print "get sub leads"
		get_sub_leads_query = "SELECT * FROM leads WHERE CONCAT(first_name,' ',last_name) like %s AND registered_datetime > %s AND registered_datetime < %s LIMIT %s, 8"
		content = [info['name'], info['from'], info['up_to'], info['current']]
		return self.db.query_db(get_sub_leads_query, content)
		