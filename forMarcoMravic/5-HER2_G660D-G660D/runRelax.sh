#!/usr/bash 


/home/xray/rosetta/source/bin/spanfile_from_pdb.linuxgccrelease -database /home/xray/rosetta/database/ -in:file:s /home/xray/Downloads/forMarcoMravic/forMarcoMravic/5-HER2_G660D-G660D/inPDB_5-HER2_G660D-G660D.pdb

/home/xray/rosetta/source/bin/rosetta_scripts.linuxgccrelease -parser:protocol /home/xray/Downloads/forMarcoMravic/bin/helix_Relax.xml -in:file:s /home/xray/Downloads/forMarcoMravic/forMarcoMravic/5-HER2_G660D-G660D/inPDB_5-HER2_G660D-G660D.pdb -nstruct 50 -mp:setup:spanfiles /home/xray/Downloads/forMarcoMravic/forMarcoMravic/5-HER2_G660D-G660D/inPDB_5-HER2_G660D-G660D.span -mp:scoring:hbond -relax:jump_move true -out:prefix /home/xray/Downloads/forMarcoMravic/forMarcoMravic/5-HER2_G660D-G660D/outputs/ -out:overwrite -packing:resfile /home/xray/Downloads/forMarcoMravic/forMarcoMravic/5-HER2_G660D-G660D/inPDB_5-HER2_G660D-G660D.resfile -packing:pack_missing_sidechains 0 -pH:pH_mode -pH:value_pH 3



/home/xray/rosetta/source/bin/spanfile_from_pdb.linuxgccrelease -database /home/xray/rosetta/database/ -in:file:s /home/xray/Downloads/forMarcoMravic/forMarcoMravic/5-HER2_G660D-G660D/inChA_5-HER2_G660D-G660D.pdb

/home/xray/rosetta/source/bin/rosetta_scripts.linuxgccrelease -parser:protocol /home/xray/Downloads/forMarcoMravic/bin/helix_Relax.xml -in:file:s /home/xray/Downloads/forMarcoMravic/forMarcoMravic/5-HER2_G660D-G660D/inChA_5-HER2_G660D-G660D.pdb -nstruct 50 -mp:setup:spanfiles /home/xray/Downloads/forMarcoMravic/forMarcoMravic/5-HER2_G660D-G660D/inChA_5-HER2_G660D-G660D.span -mp:scoring:hbond -relax:jump_move true -out:prefix /home/xray/Downloads/forMarcoMravic/forMarcoMravic/5-HER2_G660D-G660D/outputs/ -out:overwrite -packing:resfile /home/xray/Downloads/forMarcoMravic/forMarcoMravic/5-HER2_G660D-G660D/inChA_5-HER2_G660D-G660D.resfile -packing:pack_missing_sidechains 0 -pH:pH_mode -pH:value_pH 3



/home/xray/rosetta/source/bin/spanfile_from_pdb.linuxgccrelease -database /home/xray/rosetta/database/ -in:file:s /home/xray/Downloads/forMarcoMravic/forMarcoMravic/5-HER2_G660D-G660D/inChB_5-HER2_G660D-G660D.pdb

/home/xray/rosetta/source/bin/rosetta_scripts.linuxgccrelease -parser:protocol /home/xray/Downloads/forMarcoMravic/bin/helix_Relax.xml -in:file:s /home/xray/Downloads/forMarcoMravic/forMarcoMravic/5-HER2_G660D-G660D/inChB_5-HER2_G660D-G660D.pdb -nstruct 50 -mp:setup:spanfiles /home/xray/Downloads/forMarcoMravic/forMarcoMravic/5-HER2_G660D-G660D/inChB_5-HER2_G660D-G660D.span -mp:scoring:hbond -relax:jump_move true -out:prefix /home/xray/Downloads/forMarcoMravic/forMarcoMravic/5-HER2_G660D-G660D/outputs/ -out:overwrite -packing:resfile /home/xray/Downloads/forMarcoMravic/forMarcoMravic/5-HER2_G660D-G660D/inChB_5-HER2_G660D-G660D.resfile -packing:pack_missing_sidechains 0 -pH:pH_mode -pH:value_pH 3



