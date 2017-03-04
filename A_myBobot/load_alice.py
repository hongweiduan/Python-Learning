#coding:utf-8
import aiml
import sys
import os

def get_module_dir(name):
	path = getattr(sys.modules[name],'__file__',None)
	if not path:
		raiseAttributeError('module %s has not attribute __file__' % name)
	return os.path.dirname(os.path.abspath(path))

alice_path = os.getcwd()+'/alice/Howie'
#cd the workpath to alice dir
os.chdir(alice_path)

alice = aiml.Kernel()
# alice.learn("startup.xml")
# alice.respond('LOAD ALICE')

#save the brn file
if os.path.isfile("alice_brain.brn"):		
	alice.bootstrap(brainFile="alice_brain.brn")
else:
	alice.bootstrap(learnFiles="startup.xml",commands="LOAD ALICE")
	alice.saveBrain("alice_brain.brn")


while 1:
	message = raw_input("Howie:")
	if message == "quit":
		exit()
	elif message == "save":
		alice.saveBrain("alice_brain.brn")
	else:
		print "Alice:"+alice.respond(message)
