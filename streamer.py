from __future__ import absolute_import, print_function

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import sys

consumer_key = '9Low6rnq3tZM8Vcaslg8CTuON'
consumer_secret = 'MUpLDzEpJUq393NYz7r7V47oIKDHVfCxcPdNyWr8alGDMQc4gC'
access_token = '1295974295735111680-T3USohZ7q9JuUaZHIJAWvAOh10UDzq'
access_secret = 'J2IlQVlKZzhbrn5l1sHgdH7nOLbZUCGsb5trXSOleyHRt'

class StdOutListener(StreamListener):
	""" A listener handles tweets that are received from the stream.
	This is a basic listener that just prints received tweets to stdout.
	"""
	def on_data(self, data):
		fname = sys.argv[1]
		
		try:
			with open(fname, 'a') as f:
				f.write(data)
				return True
		except BaseException as e:
			print("Error in writing to file")
		print(data)
		return True
		
	def on_error(self,status):
		print(status)
		
if __name__ == '__main__':
	l = StdOutListener()
	auth = OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_secret)
	stream = Stream(auth, l)
	
stream.filter(track=['covid19'])
