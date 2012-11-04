cd /netshare1/home1/szzhongxin/proj1/hansun/viruses
#samtools view /netshare1/home1/szzhongxin/proj1/hansun/mapping3/4B/4B.bam |python 1.filter.py >ICC4B.unmapped
#python 2.fq.py ICC4B.unmapped

read1fq=ICC4B.unmapped.fq
read1sai=ICC4B.unmapped.sai
bam=ICC4B.unmapped.bam

cd /netshare1/home1/szzhongxin/proj1/hansun/viruses/mapping

bwa aln -I \
	        /netshare1/home1/szzhongxin/proj1/hansun/viruses/bwa/viruses \
		        /netshare1/home1/szzhongxin/proj1/hansun/viruses/$read1fq \
			        >$read1sai

bwa samse  \
	        /netshare1/home1/szzhongxin/proj1/hansun/viruses/bwa/viruses \
		        $read1sai \
			        /netshare1/home1/szzhongxin/proj1/hansun/viruses/$read1fq \
				        -r "@RG\tID:4a\tSM:4a\tLB:4a\tPL:illumina\tPU:barcode" | \ 
        samtools view -bS -o $bam -

	#samtools  sort $bam $bamsorted

	#mv $bamsortedbam $BAM
	#samtools index $BAM

