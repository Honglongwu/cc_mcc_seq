cd /netshare1/home1/szzhongxin/proj1/hansun/Viruses/jumpy/1_jumpy_results
db=/netshare1/home1/people/hansun/GATK/bundle/ucsc.hg19.fasta

query=CHC6B.jmp.br.fasta
out=${query}.blasted

blastn  -db $db  -query $query -out $out -outfmt 6  