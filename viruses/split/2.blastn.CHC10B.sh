cd /netshare1/home1/szzhongxin/proj1/hansun/viruses/blast
db=/netshare1/home1/szzhongxin/proj1/hansun/Viruses/bwa/hg19.viruses.fasta

query=CHC10B.unmapped.sam.unmapped.fa.fa
out=${query}.blasted

blastn  -db $db  -query $query -out $out -outfmt 6  
