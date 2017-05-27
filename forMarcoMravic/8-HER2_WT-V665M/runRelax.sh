#!/usr/bash 


/home/xray/rosetta/source/bin/spanfile_from_pdb.linuxgccrelease -database /home/xray/rosetta/database/ -in:file:s /home/xray/Downloads/forMarcoMravic/forMarcoMravic/8-HER2_WT-V665M/inPDB_8-HER2_WT-V665M.pdb

/home/xray/rosetta/source/bin/rosetta_scripts.linuxgccrelease -parser:protocol /home/xray/Downloads/forMarcoMravic/bin/helix_Relax.xml -in:file:s /home/xray/Downloads/forMarcoMravic/forMarcoMravic/8-HER2_WT-V665M/inPDB_8-HER2_WT-V665M.pdb -nstruct 50 -mp:setup:spanfiles /home/xray/Downloads/forMarcoMravic/forMarcoMravic/8-HER2_WT-V665M/inPDB_8-HER2_WT-V665M.span -mp:scoring:hbond -relax:jump_move true -out:prefix /home/xray/Downloads/forMarcoMravic/forMarcoMravic/8-HER2_WT-V665M/outputs/ -out:overwrite -packing:resfile /home/xray/Downloads/forMarcoMravic/forMarcoMravic/8-HER2_WT-V665M/inPDB_8-HER2_WT-V665M.resfile -packing:pack_missing_sidechains 0 -pH:pH_mode -pH:value_pH 3



/home/xray/rosetta/source/bin/spanfile_from_pdb.linuxgccrelease -database /home/xray/rosetta/database/ -in:file:s /home/xray/Downloads/forMarcoMravic/forMarcoMravic/8-HER2_WT-V665M/inChA_8-HER2_WT-V665M.pdb

/home/xray/rosetta/source/bin/rosetta_scripts.linuxgccrelease -parser:protocol /home/xray/Downloads/forMarcoMravic/bin/helix_Relax.xml -in:file:s /home/xray/Downloads/forMarcoMravic/forMarcoMravic/8-HER2_WT-V665M/inChA_8-HER2_WT-V665M.pdb -nstruct 50 -mp:setup:spanfiles /home/xray/Downloads/forMarcoMravic/forMarcoMravic/8-HER2_WT-V665M/inChA_8-HER2_WT-V665M.span -mp:scoring:hbond -relax:jump_move true -out:prefix /home/xray/Downloads/forMarcoMravic/forMarcoMravic/8-HER2_WT-V665M/outputs/ -out:overwrite -packing:resfile /home/xray/Downloads/forMarcoMravic/forMarcoMravic/8-HER2_WT-V665M/inChA_8-HER2_WT-V665M.resfile -packing:pack_missing_sidechains 0 -pH:pH_mode -pH:value_pH 3



/home/xray/rosetta/source/bin/spanfile_from_pdb.linuxgccrelease -database /home/xray/rosetta/database/ -in:file:s /home/xray/Downloads/forMarcoMravic/forMarcoMravic/8-HER2_WT-V665M/inChB_8-HER2_WT-V665M.pdb

/home/xray/rosetta/source/bin/rosetta_scripts.linuxgccrelease -parser:protocol /home/xray/Downloads/forMarcoMravic/bin/helix_Relax.xml -in:file:s /home/xray/Downloads/forMarcoMravic/forMarcoMravic/8-HER2_WT-V665M/inChB_8-HER2_WT-V665M.pdb -nstruct 50 -mp:setup:spanfiles /home/xray/Downloads/forMarcoMravic/forMarcoMravic/8-HER2_WT-V665M/inChB_8-HER2_WT-V665M.span -mp:scoring:hbond -relax:jump_move true -out:prefix /home/xray/Downloads/forMarcoMravic/forMarcoMravic/8-HER2_WT-V665M/outputs/ -out:overwrite -packing:resfile /home/xray/Downloads/forMarcoMravic/forMarcoMravic/8-HER2_WT-V665M/inChB_8-HER2_WT-V665M.resfile -packing:pack_missing_sidechains 0 -pH:pH_mode -pH:value_pH 3



