#!/bin/bash
#scp -p quser@192.168.1.218:~/exp/Himac_HH015/exp-config/himac_HH015/run_nlabdaq5/data/tdcdata/00/run00${1}.dat /home/h487/data/rawdata/
#streamingv1_to_parquet.py /mnt/data/h445_h487/nestdaq/tdcdata/00/run00${1}.dat /home/h487/data/parquet/run${1}.parquet #--max-blocks 100000
#streamingv1_to_parquet.py /mnt/hdd/HH015/nestdaq/tdcdata/00/run00${1}.dat /home/h487/data/parquet/run${1}.parquet #--max-blocks 100000


#cd /home/h487/notebooks/jan2026/kojima/mwdc_koji
#python mwdc_processor_koji.py /home/h487/data/parquet/run${1}.parquet --output-file /home/h487/data/parquet/run${1}_mwdc_koji.parquet #--output-wire-data #--output-for-samidare <=For Endo-san 
#cd -

cd /home/h487/notebooks/jan2026/kojima/srppac_koji
python srppac_processor_koji.py /home/h487/data/parquet/run${1}.parquet --output-file /home/h487/data/parquet/run${1}_srppac_koji.parquet   --output-strip-data --preamp-type asagi
#python join_mwdc_srppac_koji.py /home/h487/data/parquet/run${1}
cd -
