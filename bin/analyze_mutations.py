# analyze association energies and ddg vs WT

from prody import *
import sys, os, numpy as np
from collections import defaultdict
# input working directory, then 

working_dir = sys.argv[1]

namingDict = { 'PDB': 'Dimer', 'ChA':'Monomer A', 'ChB':'Monomer B' }

overall_scores = '\n# pdbType(chA,chB,dimer) meanOfTop3 StdevOfTop3 median stdev \n# Her2 50-minimization-repack-memReorient-trajectories_RosettaMP-fastRelax_pHmode-pH4\n\n' 
# look in each mutation-pdb's working directory
for i in [ os.path.abspath( os.path.join( working_dir, x ) ) for x in os.listdir( working_dir) if os.path.isdir(x) ]:
	
	pbdCentric_scores = '%s\n' % os.path.basename( i )
	print 'entering ', os.path.basename( i )
	score_tracker = defaultdict( list )

	outputs_dir =  os.path.join( i, 'outputs' ) 
	bulk_scoring = '\n# actual rosetta scores & file names...\n'
	# peak into all files in output dir
	for oF in sorted( os.listdir( outputs_dir ), reverse=True ):
		if oF[-3:] != 'pdb': continue

		# enter each file and ectract scores... know which is which by filepath suffix
	
		suffix = oF[2:5]
		path = os.path.join( outputs_dir, oF  )
		with open( path ) as fin:
			for n in fin:

				if n[:4] == 'pose':
					score = float(n.split()[-1] )

		score_tracker[suffix].append( score ) 
		bulk_scoring += '%s %0.1f %s\n' % ( suffix, round( score, 1 ), oF )

	# print summaries of scores
	meanScores = []			# [ dimerMeanSC, chA_meanSC, chB_meanSC ]
	score_summary = ''
	for k, pdb_set in enumerate( sorted( set( score_tracker.keys() ), reverse=True), 1 ):

		vector 	= sorted(np.array( score_tracker[ pdb_set ] ) )
		top3mean, stp3std, totalMedian, totalStd  	= np.mean( vector[:3] ), np.std( vector[:3] ), np.median( vector ), np.std( vector )
		score_summary += '%s     \t%0.1f %0.1f %0.1f %0.1f\n' % ( namingDict[pdb_set],  top3mean, stp3std, totalMedian, totalStd  )
		meanScores.append( top3mean )
	dimerMeanSC, chA_meanSC, chB_meanSC  = tuple( meanScores )
	

	score_summary 	+= '%s  |  Association Energy (Rosetta Energy Units) = %0.1f\n\n' % ( os.path.basename( i ) ,  dimerMeanSC - chA_meanSC  - chB_meanSC )
	overall_scores 	+= score_summary

	score_summary 	= '\n# pdbType(chA,chB,dimer) meanOfTop3 StdevOfTop3 median stdev | 50-minimization-repack-memReorient-trajectories_RosettaMP-fastRelax_pHmode-pH4\n\n' + score_summary
	score_summary 	+= bulk_scoring

	localScorefile 	= os.path.join( i , 'byModel_score_summary.txt' )
	sc_file 		= open( localScorefile, 'w')
	sc_file.write( score_summary )
	sc_file.close()


overallScorefile 	= os.path.join( working_dir , 'global_score_summary.txt' )
sc_file 		= open( overallScorefile, 'w')
sc_file.write( overall_scores )
sc_file.close()