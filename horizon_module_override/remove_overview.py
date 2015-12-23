from horizon import base as horizon

project = horizon.get_dashboard('project')
project.default_panel = 'instances'
overview = project.get_panel('overview')
project.unregister(overview.__class__)
