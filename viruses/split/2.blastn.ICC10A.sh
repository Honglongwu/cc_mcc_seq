cd /netshare1/home1/szzhongxin/proj1/hansun/viruses/split
db=/netshare1/home1/szzhongxin/proj1/hansun/viruses/split/human.viruses.target.fa

query=ICC10A.unmapped.sam.unmapped.fa.fa
out=${query}.blasted

blastn  -db $db  -query $query -out $out -outfmt 6  
