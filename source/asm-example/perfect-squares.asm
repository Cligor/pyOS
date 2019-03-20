str_end: .asciiz "perfect-squares ended"

_start:
	mov r0, 1   # teste comentario
	mov r2, 8
	mov r1, 1
	mov r4, data
loop:
	mul r5, r1, r1
	store [r4], r5
	add r4, r4, r0
	add r1, r1, r0
	cmp_neq r3, r1, r2
	jump_cond r3, loop
end:
	mov r0, 1
	mov r1, str_end
	syscall
	mov r0, 0
	syscall
data: .data 10