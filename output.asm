section .bss
	digitSpace resb 100
	digitSpacePos resb 8

	VVa resb 8
	VVb resb 8
	VVc resb 8

section .data
	text db "Hello, World!",10
section .text
	global _start

_start:

	mov rax,12
	mov [VVa],rax
	mov rax,[VVa]
	mov rbx,15
	cmp rax,rbx
	jg L1
	jmp L3
	L1 :
	mov rax,12
	mov [VVc],rax
	jmp L2
	L3 :
	mov rax,15
	mov [VVb],rax
    call _print_num
	L2 :




	mov rax, 60
	mov rdi, 0
	syscall


_print_num:
    mov rcx, digitSpace
    mov rbx, 10
    mov [rcx], rbx
    inc rcx
    mov [digitSpacePos], rcx

_printRAXLoop:
    mov rdx, 0
    mov rbx, 10
    div rbx
    push rax
    add rdx, 48

    mov rcx, [digitSpacePos]
    mov [rcx], dl
    inc rcx
    mov [digitSpacePos], rcx

    pop rax
    cmp rax, 0
    jne _printRAXLoop

_printRAXLoop2:
    mov rcx, [digitSpacePos]

    mov rax, 1
    mov rdi, 1
    mov rsi, rcx
    mov rdx, 1
    syscall

    mov rcx, [digitSpacePos]
    dec rcx
    mov [digitSpacePos], rcx

    cmp rcx, digitSpace
    jge _printRAXLoop2

    ret


_print_string:
    push rax
    mov rbx, 0

_printLoop:
    inc rax
    inc rbx
    mov cl, [rax]
    cmp cl, 0
    jne _printLoop

    mov rax, 1
    mov rdi, 1
    pop rsi
    mov rdx, rbx
    syscall

    ret
