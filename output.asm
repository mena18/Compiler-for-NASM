section .bss
	digitSpace resb 100
	digitSpacePos resb 8

	Va resb 8
	Vb resb 8
	Vi resb 8
	T1 resb 8
section .data
	text db "Hello, World!",10

	S1 db "hello world",10,0
section .text
	global _start

_start:

	mov rax,11
	mov [Va],rax
	mov rax,13
	mov [Vb],rax
	mov rax,0
	mov [Vi],rax
	L1 : 
	mov rax,[Va]
	mov rbx,[Vb]
	cmp rax,rbx
	jle L2
	jmp L3
	L2 : 
mov rax,[Va]
	call _print_num
	mov rax,[Va]
	add rax,1
	mov [T1],rax
	mov rax,[T1]
	mov [Va],rax
	jmp L1
	L3 : 
	mov rax,S1
	call _print_string

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

        
