#!/usr/bash 


/home/xray/rosetta/source/bin/spanfile_from_pdb.linuxgccrelease -database /home/xray/rosetta/database/ -in:file:s /home/xray/Downloads/forMarcoMravic/forMarcoMravic/3-HER2_S656C-S656C/inPDB_3-HER2_S656C-S656C.pdb

/home/xray/rosetta/source/bin/rosetta_scripts.linuxgccrelease -parser:protocol /home/xray/Downloads/forMarcoMravic/bin/helix_Relax.xml -in:file:s /home/xray/Downloads/forMarcoMravic/forMarcoMravic/3-HER2_S656C-S656C/inPDB_3-HER2_S656C-S656C.pdb -nstruct 50 -mp:setup:spanfiles /home/xray/Downloads/forMarcoMravic/forMarcoMravic/3-HER2_S656C-S656C/inPDB_3-HER2_S656C-S656C.span -mp:scoring:hbond -relax:jump_move true -out:prefix /home/xray/Downloads/forMarcoMravic/forMarcoMravic/3-HER2_S656C-S656C/outputs/ -out:overwrite -packing:resfile /home/xray/Downloads/forMarcoMravic/forMarcoMravic/3-HER2_S656C-S656C/inPDB_3-HER2_S656C-S656C.resfile -packing:pack_missing_sidechains 0 -pH:pH_mode -pH:value_pH 3



/home/xray/rosetta/source/bin/spanfile_from_pdb.linuxgccrelease -database /home/xray/rosetta/database/ -in:file:s /home/xray/Downloads/forMarcoMravic/forMarcoMravic/3-HER2_S656C-S656C/inChA_3-HER2_S656C-S656C.pdb

/home/xray/rosetta/source/bin/rosetta_scripts.linuxgccrelease -parser:protocol /home/xray/Downloads/forMarcoMravic/bin/helix_Relax.xml -in:file:s /home/xray/Downloads/forMarcoMravic/forMarcoMravic/3-HER2_S656C-S656C/inChA_3-HER2_S656C-S656C.pdb -nstruct 50 -mp:setup:spanfiles /home/xray/Downloads/forMarcoMravic/forMarcoMravic/3-HER2_S656C-S656C/inChA_3-HER2_S656C-S656C.span -mp:scoring:hbond -relax:jump_move true -out:prefix /home/xray/Downloads/forMarcoMravic/forMarcoMravic/3-HER2_S656C-S656C/outputs/ -out:overwrite -packing:resfile /home/xray/Downloads/forMarcoMravic/forMarcoMravic/3-HER2_S656C-S656C/inChA_3-HER2_S656C-S656C.resfile -packing:pack_missing_sidechains 0 -pH:pH_mode -pH:value_pH 3



/home/xray/rosetta/source/bin/spanfile_from_pdb.linuxgccrelease -database /home/xray/rosetta/database/ -in:file:s /home/xray/Downloads/forMarcoMravic/forMarcoMravic/3-HER2_S656C-S656C/inChB_3-HER2_S656C-S656C.pdb

/home/xray/rosetta/source/bin/rosetta_scripts.linuxgccrelease -parser:protocol /home/xray/Downloads/forMarcoMravic/bin/helix_Relax.xml -in:file:s /home/xray/Downloads/forMarcoMravic/forMarcoMravic/3-HER2_S656C-S656C/inChB_3-HER2_S656C-S656C.pdb -nstruct 50 -mp:setup:spanfiles /home/xray/Downloads/forMarcoMravic/forMarcoMravic/3-HER2_S656C-S656C/inChB_3-HER2_S656C-S656C.span -mp:scoring:hbond -relax:jump_move true -out:prefix /home/xray/Downloads/forMarcoMravic/forMarcoMravic/3-HER2_S656C-S656C/outputs/ -out:overwrite -packing:resfile /home/xray/Downloads/forMarcoMravic/forMarcoMravic/3-HER2_S656C-S656C/inChB_3-HER2_S656C-S656C.resfile -packing:pack_missing_sidechains 0 -pH:pH_mode -pH:value_pH 3



