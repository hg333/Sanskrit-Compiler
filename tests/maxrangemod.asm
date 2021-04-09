main:
add $sp, $sp, -400
li $t1, 0
sw $t1,396 ($sp)
li $v0, 5
syscall
sw $v0,396 ($sp)
li $t1, 0
li $t2, 1
sub $t3, $t1, $t2
sw $t3,392 ($sp)
lw $t1,392 ($sp)
move $t2, $t1
sw $t2,388 ($sp)
li $t1, 0
sw $t1,384 ($sp)
whilestatement5:
lw $t1,396 ($sp)
li $t2, 0
li $t3, 0
ble $t1, $t2 ,yareyare1
li $t3, 1
yareyare1:
sw $t3,380 ($sp)
lw $t1,380 ($sp)
move $t4, $t1
li $t1, 1
bne $t4, 0, yareyare2
li $t1, 0
yareyare2:
bne $t1, 1, endwhile5
li $v0, 5
syscall
sw $v0,384 ($sp)
lw $t1,384 ($sp)
lw $t2,388 ($sp)
li $t3, 0
ble $t1, $t2 ,yareyare3
li $t3, 1
yareyare3:
sw $t3,376 ($sp)
lw $t1,384 ($sp)
li $t2, 27
li $t3, 0
bne $t1, $t2 ,yareyare4
li $t3, 1
yareyare4:
sw $t3,372 ($sp)
lw $t1,376 ($sp)
lw $t2,372 ($sp)
add $t3, $t1, $t2
sw $t3,368 ($sp)
lw $t1,368 ($sp)
move $t4, $t1
li $t1, 1
bne $t4, 0, yareyare5
li $t1, 0
yareyare5:
beq $t1, 1, ifstatement10
 b ifstatement11
ifstatement10:
lw $t1,384 ($sp)
move $t2, $t1
sw $t2,388 ($sp)
 b ifstatement11
ifstatement11:
lw $t1,396 ($sp)
li $t2, 1
sub $t3, $t1, $t2
sw $t3,364 ($sp)
lw $t1,364 ($sp)
move $t2, $t1
sw $t2,396 ($sp)
 b whilestatement5
endwhile5:
li $v0, 1
lw $a0,388 ($sp)
syscall
li $v0, 10
syscall
