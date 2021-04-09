main:
add $sp, $sp, -400
li $t1, 0
sw $t1,396 ($sp)
li $t1, 2
sw $t1,392 ($sp)
li $v0, 5
syscall
sw $v0,396 ($sp)
li $t1, 366
sw $t1,388 ($sp)
lw $t1,396 ($sp)
li $t2, 4
div $t1, $t2
mflo $t3
sw $t3,384 ($sp)
lw $t1,384 ($sp)
li $t2, 4
mult $t1, $t2
mflo $t3
sw $t3,380 ($sp)
lw $t1,380 ($sp)
lw $t2,396 ($sp)
li $t3, 0
bne $t1, $t2 ,yareyare1
li $t3, 1
yareyare1:
sw $t3,376 ($sp)
lw $t1,396 ($sp)
li $t2, 100
div $t1, $t2
mflo $t3
sw $t3,372 ($sp)
lw $t1,372 ($sp)
li $t2, 100
mult $t1, $t2
mflo $t3
sw $t3,368 ($sp)
lw $t1,368 ($sp)
lw $t2,396 ($sp)
li $t3, 0
beq $t1, $t2 ,yareyare2
li $t3, 1
yareyare2:
sw $t3,364 ($sp)
lw $t1,376 ($sp)
lw $t2,364 ($sp)
mult $t1, $t2
mflo $t3
sw $t3,360 ($sp)
lw $t1,360 ($sp)
move $t4, $t1
li $t1, 1
bne $t4, 0, yareyare3
li $t1, 0
yareyare3:
beq $t1, 1, ifstatement11
lw $t1,396 ($sp)
li $t2, 4
div $t1, $t2
mflo $t3
sw $t3,356 ($sp)
lw $t1,356 ($sp)
li $t2, 4
mult $t1, $t2
mflo $t3
sw $t3,352 ($sp)
lw $t1,352 ($sp)
lw $t2,396 ($sp)
li $t3, 0
bne $t1, $t2 ,yareyare4
li $t3, 1
yareyare4:
sw $t3,348 ($sp)
lw $t1,396 ($sp)
li $t2, 400
div $t1, $t2
mflo $t3
sw $t3,344 ($sp)
lw $t1,344 ($sp)
li $t2, 400
mult $t1, $t2
mflo $t3
sw $t3,340 ($sp)
lw $t1,340 ($sp)
lw $t2,396 ($sp)
li $t3, 0
bne $t1, $t2 ,yareyare5
li $t3, 1
yareyare5:
sw $t3,336 ($sp)
lw $t1,348 ($sp)
lw $t2,336 ($sp)
mult $t1, $t2
mflo $t3
sw $t3,332 ($sp)
lw $t1,332 ($sp)
move $t4, $t1
li $t1, 1
bne $t4, 0, yareyare6
li $t1, 0
yareyare6:
beq $t1, 1, ifstatement19
li $t1, 1
move $t4, $t1
li $t1, 1
bne $t4, 0, yareyare7
li $t1, 0
yareyare7:
beq $t1, 1, ifstatement20
 b ifstatement21
ifstatement11:
li $v0, 1
lw $a0,388 ($sp)
syscall
 b ifstatement21
ifstatement19:
li $v0, 1
lw $a0,388 ($sp)
syscall
 b ifstatement21
ifstatement20:
lw $t1,388 ($sp)
li $t2, 1
sub $t3, $t1, $t2
sw $t3,328 ($sp)
lw $t1,328 ($sp)
move $t2, $t1
sw $t2,388 ($sp)
li $v0, 1
lw $a0,388 ($sp)
syscall
 b ifstatement21
ifstatement21:
li $v0, 10
syscall
