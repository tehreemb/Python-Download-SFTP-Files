import pysftp as sftp

def sftpExample():
	try:
		s = sftp.Connection('ftp.company.com', username='enterusername', password='enterpassword')

		remotepath1='/home/filepath/sample.xlsx'
		localpath1="\\\\corporatenetwork\\datapath\\sample.xlsx"

		s.get(remotepath1,localpath1, preserve_mtime=True)


		s.close()

	except Exception, e:
		print str(e)

sftpExample()
