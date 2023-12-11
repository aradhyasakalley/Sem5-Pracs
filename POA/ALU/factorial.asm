data segment 
    a db 5
    fact db ?
data ends     

code segment
    assume ds:data,cs:code
    start:
        mov ax,data
        mov ds,ax
        mov ah,00
        mov al,a
    
    l1: dec a
        mul a
        mov cl,a
        cmp cl,01
        jnz l1
        mov fact,al
code ends
end start
    