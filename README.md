# ctg-tools

General-purpose scripts for basic NGS data processing.

More description to come..


# TOOLS: 

## ctg-deliver

rsync ctg-delivery data on lsens4 to customer folder on lfs603
The script also changes permissions (-R 770) and ownership of the delivery folder (chown -R customeruser:ctguser)

#### Usage
```
ctg-deliver -u CTG-USER-LFS -d DATA-TO-DELIVER -c CUSTOMER-USER-LFS
```

#### Example
```
ctg-deliver -u per -d 2021_082 -c stone_a
```

#### Outcome
This will sync the 2021_082 folder into lfs603.srv.lu.se:/srv/data/stone_a/ and change permission and ownership.




## ctg-interop-qc

Run interop on runfolder and generate multiqc report

#### Usage

cd to runfolder to process
```
cd 210406_A00681_0339_AH2V2VDRXY
ctg-interop-qc
``` 

#### Outcome
- This will generate a **ctg-interop** folder containing the interop stats + multiqc output.
- This ctg-interop folder will be written to runfolder.
- In addition, the multiqc output will be copied to **/projects/fs1/shared/ctg-qc/interop**



## ctg-sav-save

Save Illumina SAV files from runfolders

Make copies of the following runfolder files/dirs:
- InterOp           
- RunInfo.xml       
- RunParameters.xml 

#### Usage
Execute from within runfolder
```
ctg-sav-save
```

#### Outcome 
Copy files above in **/projects/fs1/shared/ctg-qc/sav-illumina**

#### Log
After copy, the script creates a ctg_SAV_saved_<runfolder-name>.done in runfolder




