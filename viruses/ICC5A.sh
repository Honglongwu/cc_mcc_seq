cd /netshare1/home1/szzhongxin/proj1/hansun/viruses
#samtools view /netshare1/home1/szzhongxin/proj1/hansun/mapping/5A/5A.bam |python 1.filter.py >ICC5A.unmapped
#python 2.fq.py ICC5A.unmapped

read1fq=ICC5A.unmapped.fq
read1sai=ICC5A.unmapped.sai
bam=ICC5A.unmapped.bam

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

