main:
add $sp, $sp, -400
li $t1, 0
sw $t1,396 ($sp)
li $t1, 2
sw $t1,392 ($sp)
li $v0, 5
syscall
sw $v0,396 ($sp)
lw $t1,396 ($sp)
move $t2, $t1
sw $t2,388 ($sp)
whilestatement4:
lw $t1,392 ($sp)
lw $t2,392 ($sp)
mult $t1, $t2
mflo $t3
sw $t3,384 ($sp)
lw $t1,384 ($sp)
lw $t2,396 ($sp)
li $t3, 0
bgt $t1, $t2 ,yareyare1
li $t3, 1
yareyare1:
sw $t3,380 ($sp)
lw $t1,380 ($sp)
move $t4, $t1
li $t1, 1
bne $t4, 0, yareyare2
li $t1, 0
yareyare2:
bne $t1, 1, endwhile4
lw $t1,396 ($sp)
lw $t2,392 ($sp)
div $t1, $t2
mflo $t3
sw $t3,376 ($sp)
lw $t1,376 ($sp)
lw $t2,392 ($sp)
mult $t1, $t2
mflo $t3
sw $t3,372 ($sp)
lw $t1,372 ($sp)
lw $t2,396 ($sp)
li $t3, 0
bne $t1, $t2 ,yareyare3
li $t3, 1
yareyare3:
sw $t3,368 ($sp)
lw $t1,368 ($sp)
move $t4, $t1
li $t1, 1
bne $t4, 0, yareyare4
li $t1, 0
yareyare4:
beq $t1, 1, ifstatement10
 b ifstatement11
ifstatement10:
lw $t1,388 ($sp)
lw $t2,392 ($sp)
div $t1, $t2
mflo $t3
sw $t3,364 ($sp)
lw $t1,388 ($sp)
lw $t2,364 ($sp)
sub $t3, $t1, $t2
sw $t3,360 ($sp)
lw $t1,360 ($sp)
move $t2, $t1
sw $t2,356 ($sp)
lw $t1,356 ($sp)
move $t2, $t1
sw $t2,388 ($sp)
 b ifstatement11
ifstatement11:
whilestatement16:
lw $t1,396 ($sp)
lw $t2,392 ($sp)
div $t1, $t2
mflo $t3
sw $t3,352 ($sp)
lw $t1,352 ($sp)
lw $t2,392 ($sp)
mult $t1, $t2
mflo $t3
sw $t3,348 ($sp)
lw $t1,348 ($sp)
lw $t2,396 ($sp)
li $t3, 0
bne $t1, $t2 ,yareyare5
li $t3, 1
yareyare5:
sw $t3,344 ($sp)
lw $t1,344 ($sp)
move $t4, $t1
li $t1, 1
bne $t4, 0, yareyare6
li $t1, 0
yareyare6:
bne $t1, 1, endwhile16
lw $t1,396 ($sp)
lw $t2,392 ($sp)
div $t1, $t2
mflo $t3
sw $t3,340 ($sp)
lw $t1,340 ($sp)
move $t2, $t1
sw $t2,396 ($sp)
 b whilestatement16
endwhile16:
lw $t1,392 ($sp)
li $t2, 1
add $t3, $t1, $t2
sw $t3,336 ($sp)
lw $t1,336 ($sp)
move $t2, $t1
sw $t2,392 ($sp)
 b whilestatement4
endwhile4:
lw $t1,396 ($sp)
li $t2, 1
li $t3, 0
ble $t1, $t2 ,yareyare7
li $t3, 1
yareyare7:
sw $t3,332 ($sp)
lw $t1,332 ($sp)
move $t4, $t1
li $t1, 1
bne $t4, 0, yareyare8
li $t1, 0
yareyare8:
beq $t1, 1, ifstatement25
 b ifstatement26
ifstatement25:
lw $t1,388 ($sp)
lw $t2,396 ($sp)
div $t1, $t2
mflo $t3
sw $t3,328 ($sp)
lw $t1,388 ($sp)
lw $t2,328 ($sp)
sub $t3, $t1, $t2
sw $t3,324 ($sp)
lw $t1,324 ($sp)
move $t2, $t1
sw $t2,356 ($sp)
lw $t1,356 ($sp)
move $t2, $t1
sw $t2,388 ($sp)
 b ifstatement26
ifstatement26:
li $v0, 1
lw $a0,388 ($sp)
syscall
li $v0, 10
syscall
