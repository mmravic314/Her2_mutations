# Marco Mravic DeGrado Lab 2016

## Input 1: pdb of model, e.g. Her2 monomer or dimer
## Input 2: path to rosetta main
## input 3: path to Rosetta scripts XML with protocol 
## input 4: path to resfile

# puts all output and intermediate files to the directory in the path of the input helix

## Example command line
# 
#  python bin/rosiMP_repack.py chA_OPM_her2_wt-wt.pdb ~/rosetta/ bin/helix_Relax.xml  chA_OPM_her2_wt-wt.resfile.txt 



import sys, os, subprocess as sp, numpy as np, time
from prody import *

#### I/Oa5`
inPDB		= sys.argv[1]


rosiBase 	= sys.argv[2]
rosiScrps	= os.path.join( rosiBase, 'source/bin/rosetta_scripts.linuxgccrelease' )
rosiDB 		= os.path.join( rosiBase, 'database/')
rosiSpanGen = os.path.join( rosiBase, 'source/bin/spanfile_from_pdb.linuxgccrelease')

protocolPth = sys.argv[3]
resfile_path= sys.argv[4]

oDir 		= os.path.dirname(  os.path.abspath( inPDB )  ) + '/output_%s/' % inPDB[:-4]
if not os.path.exists(oDir):
	os.mkdir(oDir)
####

## Clean DUm atoms away 
#inPDB_clean = inPDB[:-4] + '_clean.pdb'
#pdb2 		= parsePDB( inPDB ).select( 'protein' ).copy()
#writePDB( inPDB_clean, pdb2 )
##


## Make span file from input PDB
cmdSpan = [ rosiSpanGen, 
'-database', rosiDB, 
'-in:file:s', inPDB
]

spanF = inPDB[:-4] + '.span'
if not os.path.exists(spanF):

	sp.call( cmdSpan )



### Relax strucuture and minize helical orientation
n_jobs = '50'

cmd = [  rosiScrps, 
'-parser:protocol', protocolPth, 			# Path to Rosetta script (see above)
'-in:file:s', inPDB,							# Input PDB structure
'-nstruct', n_jobs, 							# Generate 1 model
'-mp:setup:spanfiles', spanF,				# Input spanfile
'-mp:scoring:hbond', 						# Turn on membrane hydrogen bonding
'-relax:jump_move', 'true', 				# Allow jumps to move during relax
'-out:prefix', oDir,
'-out:overwrite',
'-packing:resfile', resfile_path , 
'-packing:pack_missing_sidechains', '0', '-pH:pH_mode', '-pH:value_pH', '3'
 ]

#print 'rosetta running now ...' 
print cmd
print 

FNULL = open(os.devnull, 'w')

#sp.call( cmd )										# unhash for debugging, verbose rosetta
#sp.call( cmd, stdout=FNULL, stderr=sp.STDOUT )		# unhash for silenced rosetta stdout



scores = []
#print output energies found for all pdb's in the outDir
for i in [ x for x in os.listdir(oDir) if x[-3:] == 'pdb' ]:

	oF 		= os.path.join(oDir,i)

	with open(oF) as fin:
		for line in fin:
			if line[:4] == 'pose':
				score = float( line.split()[-1] )

				scores.append( score )

scores = np.array( sorted( scores ) )
print 'mean score (of top 3)', round( np.mean( scores [:3] ), 1), '(%.1f)' % round( np.std( scores [:3] ), 1)  , '   Stdev of all', round( np.std( scores ), 2 ), '\n'

for i in scores:
	print inPDB[:6], '%0.1f' % i

sys.exit()

###



##

'''  OPTIONS FROM 2015 PLOS paper
-parser:protocol membrane_relax.xml # Path to Rosetta script (see above)
-in:file:s 3PXO_tr_native.pdb # Input PDB structure
-nstruct 1000 # Generate 1000 models
-mp:setup:spanfiles 3PX0.span # Input spanfile
-mp:scoring:hbond # Turn on membrane hydrogen bonding
-relax:jump_move true # Allow jumps to move during relax
-packing:pack_missing_sidechains 0 # Wait to pack sidechains 
'''