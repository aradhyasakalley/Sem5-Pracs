data segment 
    msg db "enter a character:$ "
data ends

code segment
    assume cs:code,ds:data
    start:
        mov ax,data
        mov ds,ax
        lea dx,msg
        
        ; interrupt to print message
        mov ah,09h
        int 21h
        
        ; interrupt to display rhe char
        mov ah,01
        int 21h
        
        ; interrupt to read a single char
        mov dl,al
        mov ah,02
        int 21h
        
        ; interrupt to terminate program
        mov ah,4ch
        int 21h 
code ends
end start