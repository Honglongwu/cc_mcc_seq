cd  /netshare1/home1/szzhongxin/proj1/hansun/Viruses/code.jumpy
#qsub jumpy.CHC10A.sh -l nodes=n5  
qsub jumpy.CHC10B.sh -l nodes=cu11  
#qsub jumpy.CHC5A.sh -l nodes=n7  
qsub jumpy.CHC5B.sh -l nodes=cu12  
#qsub jumpy.CHC6A.sh -l nodes=n9  
qsub jumpy.CHC6B.sh -l nodes=cu13
#qsub jumpy.CHC7A.sh -l nodes=n11  
qsub jumpy.CHC7B.sh -l nodes=cu14
#qsub jumpy.ICC10A.sh -l nodes=n13  
qsub jumpy.ICC10B.sh -l nodes=cu15
#qsub jumpy.ICC4A.sh -l nodes=n15  
qsub jumpy.ICC4B.sh -l nodes=cu16
#qsub jumpy.ICC5A.sh -l nodes=n17  
qsub jumpy.ICC5B.sh -l nodes=cu17
#qsub jumpy.ICC9A.sh -l nodes=n24  
qsub jumpy.ICC9B.sh -l nodes=cu18
