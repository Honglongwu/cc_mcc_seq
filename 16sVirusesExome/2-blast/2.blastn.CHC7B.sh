cd /netshare1/home1/szzhongxin/proj1/hansun/16sVirusesExome/2-blast
db=/netshare1/home1/szzhongxin/proj1/hansun/Viruses/bwa/hg19.viruses.fasta

query=CHC7B.unmapped.sam.mapped.fa.fa
out=${query}.blasted

blastn  -db $db  -query $query -out $out -outfmt 6  
