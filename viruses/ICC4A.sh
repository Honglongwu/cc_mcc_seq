cd /netshare1/home1/szzhongxin/proj1/hansun/viruses
#samtools view /netshare1/home1/szzhongxin/proj1/hansun/mapping/4A/4A.bam |python 1.filter.py >ICC4A.unmapped
#python 2.fq.py ICC4A.unmapped

read1fq=ICC4A.unmapped.fq
read1sai=ICC4A.unmapped.sai
bam=ICC4A.unmapped.bam
sam=ICC4A.unmapped.sam

cd /netshare1/home1/szzhongxin/proj1/hansun/viruses/mapping

bwa aln -I \
        /netshare1/home1/szzhongxin/proj1/hansun/viruses/bwa/viruses \
        /netshare1/home1/szzhongxin/proj1/hansun/viruses/$read1fq \
        >$read1sai

bwa samse  \
/netshare1/home1/szzhongxin/proj1/hansun/viruses/bwa/viruses \
$read1sai \
/netshare1/home1/szzhongxin/proj1/hansun/viruses/$read1fq \
-r "@RG\tID:4a\tSM:4a\tLB:4a\tPL:illumina\tPU:barcode" >$sam
#samtools view -bS -o $bam -

#samtools  sort $bam $bamsorted

#mv $bamsortedbam $BAM
#samtools index $BAM


