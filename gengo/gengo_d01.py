#!/usr/bin/python
# coding: UTF-8

'''
Copyright 2013 hamburgerkid

Question
Code a working example (simple is fine) that uses the Gengo API /translate/jobs POST endpoint against our Sandbox.
Feel free to use a client library.
If you have a broader vision behind the example, do elaborate how you would build on it.

API Document
http://developers.gengo.com/v2/jobs/#jobs-post
'''

from gengo import Gengo

gengo = Gengo(
	public_key = PUBLIC_KEY,
	private_key = PRIVATE_KEY,
	sandbox = True)

def postJobs():
	data = {
		'jobs': {
			'job_1': {
				'type': 'text',
				'slug': 'Single :: English to Japanese',
				'body_src': 'Hello Gengo.',
				'lc_src': 'en',
				'lc_tgt': 'ja',
				'tier': 'standard',
				'auto_approve': 1,
				'comment': 'Hello. I\'m looking forward to your excellent translation!',
				#'callback_url': 'http://...',
				'custom_data': 'What dose this work for?',
				'force': 0,
				'use_preferred': 0
			}
		},
		'as_group': 1
	}
	try:
		print gengo.postTranslationJobs(jobs=data)
	except Exception,e:
		print 'Error occurred.',e

if __name__ == '__main__':
	print gengo.getAccountBalance()
	postJobs()
