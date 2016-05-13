from system.core.controller import *

class Leads(Controller):
	def __init__(self, action):
		super(Leads, self).__init__(action)
		self.load_model('Lead')

	def index(self):
		return self.load_view('index.html')

	def init(self):
		info = {
			'name': '%',
			'from': '%',
			'up_to': 'null',
			'current': 0
		}
		leads_found = self.models['Lead'].get_leads(info)
		pages = leads_found[0]['lead_count']/8
		sub_leads = self.models['Lead'].get_sub_leads(info)
		sub_leads = {'leads': sub_leads, 'page_count': pages}
		return self.load_view('partials/leads.html', leads=sub_leads)

	def leads(self, page_id):
		print "partial"
		info = {
			'name': request.form['name']+'%',
			'from': request.form['from']+'%',
			'up_to': request.form['up_to']+'null'
		}
		leads_found = self.models['Lead'].get_leads(info)
		if leads_found:
			pages = leads_found[0]['lead_count']/8
		else:
			pages = 0
		current_page = 8*(page_id-1)
		info['current'] = current_page
		sub_leads = self.models['Lead'].get_sub_leads(info)
		sub_leads = {'leads': sub_leads, 'page_count': pages}
		return self.load_view('partials/leads.html', leads=sub_leads)