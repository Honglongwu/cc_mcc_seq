cd /netshare1/home1/szzhongxin/proj1/hansun/CNV/cnv-seq 

samtools view -F 4  /netshare1/home1/szzhongxin/proj1/hansun/aftmapping2/5A/5A.realigned.bam | perl -lane 'print "$F[2]\t$F[3]"' > CHC_5A.hits
