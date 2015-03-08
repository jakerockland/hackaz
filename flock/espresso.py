# define bundles of files to deliver to the browser

from flask.ext.assets import Bundle

js_libraries = [
    'js/bootstrap.js',
    'js/bootstrap.min.js',
    'js/jquery.js',
]

coffee_scripts = [
	'twitter-pull.coffee',
]

coffee_bundle = Bundle(
	*coffee_scripts,
	filters='coffeescript',
	output='gen/leche_coffee.%(version)s.js'
)

leche_js = Bundle(
	*(js_libraries + [coffee_bundle]),
	filters='yui_js', output='gen/leche.%(version)s.js'
)
