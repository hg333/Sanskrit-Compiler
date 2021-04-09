main:
add $sp, $sp, -400
li $t1, 0
sw $t1,396 ($sp)
li $t1, 0
sw $t1,392 ($sp)
li $v0, 5
syscall
sw $v0,396 ($sp)
li $v0, 5
syscall
sw $v0,392 ($sp)
li $t1, 1
sw $t1,388 ($sp)
whilestatement4:
lw $t1,392 ($sp)
li $t2, 0
li $t3, 0
ble $t1, $t2 ,yareyare1
li $t3, 1
yareyare1:
sw $t3,384 ($sp)
lw $t1,384 ($sp)
move $t4, $t1
li $t1, 1
bne $t4, 0, yareyare2
li $t1, 0
yareyare2:
bne $t1, 1, endwhile4
lw $t1,388 ($sp)
lw $t2,396 ($sp)
mult $t1, $t2
mflo $t3
sw $t3,380 ($sp)
lw $t1,380 ($sp)
move $t2, $t1
sw $t2,388 ($sp)
lw $t1,392 ($sp)
li $t2, 1
sub $t3, $t1, $t2
sw $t3,376 ($sp)
lw $t1,376 ($sp)
move $t2, $t1
sw $t2,392 ($sp)
 b whilestatement4
endwhile4:
li $v0, 1
lw $a0,388 ($sp)
syscall
li $v0, 10
syscall
