main:
add $sp, $sp, -400
li $t1, 0
sw $t1,396 ($sp)
li $v0, 5
syscall
sw $v0,396 ($sp)
li $t1, 1
sw $t1,392 ($sp)
whilestatement3:
lw $t1,396 ($sp)
li $t2, 0
li $t3, 0
ble $t1, $t2 ,yareyare1
li $t3, 1
yareyare1:
sw $t3,388 ($sp)
lw $t1,388 ($sp)
move $t4, $t1
li $t1, 1
bgt $t4, 0, yareyare2
li $t1, 0
yareyare2:
bne $t1, 1, endwhile3
lw $t1,392 ($sp)
lw $t2,396 ($sp)
mult $t1, $t2
mflo $t3
sw $t3,384 ($sp)
lw $t1,384 ($sp)
move $t2, $t1
sw $t2,392 ($sp)
lw $t1,396 ($sp)
li $t2, 1
sub $t3, $t1, $t2
sw $t3,380 ($sp)
lw $t1,380 ($sp)
move $t2, $t1
sw $t2,396 ($sp)
 b whilestatement3
endwhile3:
li $v0, 1
lw $a0,392 ($sp)
syscall
lw $t1,392 ($sp)
li $t2, 120
li $t3, 0
bne $t1, $t2 ,yareyare3
li $t3, 1
yareyare3:
sw $t3,376 ($sp)
lw $t1,376 ($sp)
move $t4, $t1
li $t1, 1
bgt $t4, 0, yareyare4
li $t1, 0
yareyare4:
beq $t1, 1, ifstatement10
lw $t1,392 ($sp)
li $t2, 2
li $t3, 0
bne $t1, $t2 ,yareyare5
li $t3, 1
yareyare5:
sw $t3,372 ($sp)
lw $t1,372 ($sp)
move $t4, $t1
li $t1, 1
bgt $t4, 0, yareyare6
li $t1, 0
yareyare6:
beq $t1, 1, ifstatement12
li $t1, 1
move $t4, $t1
li $t1, 1
bgt $t4, 0, yareyare7
li $t1, 0
yareyare7:
beq $t1, 1, ifstatement13
 b ifstatement14
ifstatement10:
lw $t1,392 ($sp)
li $t2, 5
add $t3, $t1, $t2
sw $t3,368 ($sp)
lw $t1,368 ($sp)
move $t2, $t1
sw $t2,392 ($sp)
li $v0, 1
lw $a0,392 ($sp)
syscall
 b ifstatement14
ifstatement12:
li $t1, 5
sw $t1,392 ($sp)
 b ifstatement14
ifstatement13:
li $t1, 0
lw $t2,392 ($sp)
sub $t3, $t1, $t2
sw $t3,364 ($sp)
lw $t1,364 ($sp)
move $t2, $t1
sw $t2,392 ($sp)
 b ifstatement14
ifstatement14:
li $v0, 1
lw $a0,392 ($sp)
syscall
li $v0, 10
syscall
sub		$t0, $t1, $t2		# $t0 = $t1 - $t2
