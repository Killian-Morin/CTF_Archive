# Break the battalion

## Clue / Information

You have received a file from the the infamous Bronco Battallion of the military. What is the correct input which gives you access to the military secrets? Format is bronco{input}.

[a.out](./a.out)

## Resolution

The file is an executable, pass it to [dogbolt](https://dogbolt.org/), an online decompiler present in the resource of this CTF.

Taking the decompilation from BinaryNinja (only relevant function):
```c
int64_t encrypt(char* arg1)
{
    for (void* i = nullptr; i < strlen(arg1); i += 1)
    {
        *(i + arg1) ^= 0x50;
        putchar(*(i + arg1));
    }

    return putchar(0xa);
}

int32_t main(int32_t argc, char** argv, char** envp)
{
    void* fsbase;
    int64_t rax = *(fsbase + 0x28);
    friendlyFunction();
    puts("What is ze passcode monsieur?");
    void var_118;
    __isoc99_scanf("%255s", &var_118);
    encrypt(&var_118);

    if (strcmp(&var_118, "brigade"))
        puts("wrong password");
    else
        puts("correct password");

    *(fsbase + 0x28);

    if (rax == *(fsbase + 0x28))
        return 0;

    __stack_chk_fail();
    /* no return */
}
```

The passcode must become *brigade* after passing through the `encrypt()` function.

This function do the operation `^= 0x50` on each character passed. This operation is an XOR with a value of 80 or P in the ascii table.

Using [cyberchef](https://cyberchef.org/), select the XOR recipe, select the key as `0x50` with type HEX, pass `brigade` in the input, the output is `2"97145`. Since the XOR operation is reversible, with the key `0x50`, it will always give `brigade` as output if input is `2"97145` and vice-versa.

flag: `bronco{2"97145}`
