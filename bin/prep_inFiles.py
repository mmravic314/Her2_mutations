# input a list of directories (arg 1)
# take input PDB, align it to oriented reference. 
# Make a new working directory, write new PDB file aligned to input pdb (arg 2)
# write out each chain separately 
# write a xx.sh file with the command list to run rosetta and print out association energies to a file
#
# give input to rosetta path (arg 3)
# give input to relax protocol XML file (arg4)
#
# python ../bin/prep_inFiles.py ~/Downloads/forMarcoMravic/forMarcoMravic/ ../OPM_her2_wt-wt.pdb ~/rosetta/ ../bin/helix_Relax.xml


import os, sys, numpy as np
from prody import *

reference 		= parsePDB( sys.argv[2], subset='ca' )
rosiBase 		= sys.argv[3]
rosiScrps		= os.path.join( rosiBase, 'source/bin/rosetta_scripts.linuxgccrelease' )
rosiDB 			= os.path.join( rosiBase, 'database/')
rosiSpanGen 	= os.path.join( rosiBase, 'source/bin/spanfile_from_pdb.linuxgccrelease')
protocolPth 	= os.path.abspath( sys.argv[4] )

natAA = {}
natAA["ALA"] = 'A'; natAA["CYS"] = 'C'; natAA["ASP"] = 'D'; natAA["GLU"] = 'E'; natAA["PHE"] = 'F';
natAA["GLY"] = 'G'; natAA["HIS"] = 'H'; natAA["ILE"] = 'I'; natAA["LYS"] = 'K';
natAA["LEU"] = 'L'; natAA["MET"] = 'M'; natAA["ASN"] = 'N'; natAA["PRO"] = 'P'; natAA["GLN"] = 'Q';
natAA["ARG"] = 'R'; natAA["SER"] = 'S'; natAA["THR"] = 'T'; natAA["VAL"] = 'V'; natAA["TRP"] = 'W'; natAA["TYR"] = 'Y';


for f in os.listdir( sys.argv[1] ):
	if f[-3:] != 'pdb': continue

	print '\nWorking on %s...\n' %f
	# set up environment...
	path 		= os.path.join( sys.argv[1], f)
	working_dir = os.path.join( sys.argv[1], f[:-4] )
	newPath = os.path.join( working_dir, 'inPDB_%s' % f  )
	chAPath = os.path.join( working_dir, 'inChA_%s' % f  )
	chBPath = os.path.join( working_dir, 'inChB_%s' % f  )
	resfile = os.path.join( working_dir, 'inPDB_%sresfile' % f[:-3] )
	res_chA = os.path.join( working_dir, 'inChA_%sresfile' % f[:-3] )
	res_chB = os.path.join( working_dir, 'inChB_%sresfile' % f[:-3] )
	runFile = os.path.join( working_dir, 'runRelax.sh')
	outputs = os.path.join( working_dir, 'outputs/')

	# align PDB

	mutated 		= parsePDB( path )
	mobile_backbone = mutated.select( 'ca' ).copy() 

	transform 		= calcTransformation( mobile_backbone, reference )
	applyTransformation( transform, mutated )


	chainA = mutated.select( 'chain A ' )
	chainB = mutated.select( 'chain B ' )

	# print out resfiles for each, and record rosetta commands in bash
	command_file 	= '#!/usr/bash \n\n\n'
	PDB_obj	 		= [mutated, chainA, chainB]
	resfile_pathz 	= [resfile, res_chA, res_chB]
	pdb_pathz 		= [ newPath, chAPath, chBPath ]
	
	if not os.path.exists( working_dir ):
		os.mkdir( working_dir )
		os.mkdir( outputs )

	for pdb, res_path, path  in zip( PDB_obj, resfile_pathz , pdb_pathz ):

		writePDB( path, pdb )

		resfile_txt = 'start\n'
		for resi in pdb.copy().iterResidues():
			resfile_txt += '%d %s PIKAA %s\n' % ( resi.getResnum(), resi.getChid(), natAA[ resi.getResname() ] )


		outFile = open( res_path, 'w' )
		outFile.write( resfile_txt )
		outFile.close()

		spanFile = path[:-3] + 'span'

		## Make span file from input PDB
		cmdSpan = ' '.join( [ rosiSpanGen, 
			'-database', rosiDB, 
			'-in:file:s', path
			] )

		n_jobs = '50'

		cmdRelax = ' '.join( [  rosiScrps, 
		'-parser:protocol', protocolPth, 			# Path to Rosetta script (see above)
		'-in:file:s', path,							# Input PDB structure
		'-nstruct', n_jobs, 							# Generate 1 model
		'-mp:setup:spanfiles', spanFile,				# Input spanfile
		'-mp:scoring:hbond', 						# Turn on membrane hydrogen bonding
		'-relax:jump_move', 'true', 				# Allow jumps to move during relax
		'-out:prefix', outputs,
		'-out:overwrite',
		'-packing:resfile', res_path , 
		'-packing:pack_missing_sidechains', '0', '-pH:pH_mode', '-pH:value_pH', '3'
 		] ) 

		
		command_file += cmdSpan + '\n\n' + cmdRelax + '\n\n\n\n'
		outFile2 = open( runFile, 'w' )
		outFile2.write( command_file )
		outFile2.close()

