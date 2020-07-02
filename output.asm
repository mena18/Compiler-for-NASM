section .bss
	digitSpace resb 100
	digitSpacePos resb 8

	Vvar1 resb 8
	Vvar2 resb 8
	Vvar3 resb 8
	Vvar4 resb 8
section .data
	text db "Hello, World!",10

	S1 db "arithmetic operation",10,0
	S2 db "priority",10,0
section .text
	global _start

_start:

	mov rax,S1
	call _print_string
	mov rax,10
	mov [Vvar1],rax
	mov rax,5
	mov [Vvar2],rax
	mov rax,60
	mov [Vvar3],rax
	mov rax,6
	mov [Vvar4],rax
mov rax,[Vvar1]
	call _print_num
mov rax,[Vvar2]
	call _print_num
mov rax,[Vvar3]
	call _print_num
mov rax,[Vvar4]
	call _print_num
	mov rax,S2
	call _print_string
	mov rax,5
	mov [Vvar1],rax
	mov rax,85
	mov [Vvar2],rax
mov rax,[Vvar1]
	call _print_num
mov rax,[Vvar2]
	call _print_num

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

        
