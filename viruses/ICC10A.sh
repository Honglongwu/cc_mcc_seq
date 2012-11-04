cd /netshare1/home1/szzhongxin/proj1/hansun/viruses
#samtools view /netshare1/home1/szzhongxin/proj1/hansun/mapping/10A/10A.bam |python 1.filter.py >ICC10A.unmapped
#python 2.fq.py ICC10A.unmapped

read1fq=ICC10A.unmapped.fq
read1sai=ICC10A.unmapped.sai
bam=ICC10A.unmapped.bam

cd /netshare1/home1/szzhongxin/proj1/hansun/viruses/mapping

bwa aln -I \
	/netshare1/home1/szzhongxin/proj1/hansun/viruses/bwa/viruses \
	/netshare1/home1/szzhongxin/proj1/hansun/viruses/$read1fq \
	>$read1sai

bwa samse  \
	/netshare1/home1/szzhongxin/proj1/hansun/viruses/bwa/viruses \
	$read1sai \
	/netshare1/home1/szzhongxin/proj1/hansun/viruses/$read1fq \
	-r "@RG\tID:10a\tSM:10a\tLB:10a\tPL:illumina\tPU:barcode" | \
	samtools view -bS -o $bam -

#samtools  sort $bam $bamsorted

#mv $bamsortedbam $BAM
#samtools index $BAM

