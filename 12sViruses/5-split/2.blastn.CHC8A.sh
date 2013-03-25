cd /fs01/szzhongxin/proj1/hansun/12sViruses/5-split
db=/fs01/szzhongxin/proj1/hansun/12sViruses/5-split/human.viruses.target.fa

query=CHC8A.unmapped.sam.unmapped.fa.fa
out=${query}.blasted

blastn  -db $db  -query $query -out $out -outfmt 6  
