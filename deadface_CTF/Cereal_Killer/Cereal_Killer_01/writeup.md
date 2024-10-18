# Clue / Information
This year, America's politicians are weighing in on the IMPORTANT issues... As in, which spooky cereal is best?

Mr. Robert F. Kennedy, Jr. has a favorite spooky cereal. Tear apart this binary and see if you can figure out what it is!

Submit the flag as flag{flag-text}. Example: flag{cocoaricepuffkrispiesbutter}

SHA1 of the .zip: 2d9622f99cc3f4da60b417078f5b24560bf2286f
Password of the .zip: d34df4c3

# Resolution

Opened `/lin/ck-2024-re04` with BinaryNinja

int32_t sub_2935(void* arg1, int32_t arg2, void* arg3, int32_t arg4, void* arg5)
{
    void* gsbase;
    int32_t eax_3 = *(uint32_t*)((char*)gsbase + 0x14);
    uint32_t var_228 = 0;
    int32_t var_214 = 0;
    uint32_t var_224 = 0;
    void var_210;
    void var_110;

    for (int32_t i = 0; i <= 0xff; i += 1)
    {
        *(uint8_t*)(i + &var_110) = i;
        *(uint8_t*)(i + &var_210) = *(uint8_t*)((char*)arg3 + (((int64_t)i) % arg4));
    }

    for (int32_t i_1 = 0; i_1 <= 0xff; i_1 += 1)
    {
        char eax_23;
        int32_t edx_8;
        edx_8 = HIGHD(((int64_t)(((uint32_t)*(uint8_t*)(i_1 + &var_210)) + (((uint32_t)*(uint8_t*)(i_1 + &var_110)) + var_228))));
        eax_23 = LOWD(((int64_t)(((uint32_t)*(uint8_t*)(i_1 + &var_210)) + (((uint32_t)*(uint8_t*)(i_1 + &var_110)) + var_228))));
        uint32_t edx_9 = (edx_8 >> 0x18);
        var_228 = (((uint32_t)(eax_23 + edx_9)) - edx_9);
        char eax_29 = *(uint8_t*)(var_228 + &var_110);
        *(uint8_t*)(var_228 + &var_110) = *(uint8_t*)(i_1 + &var_110);
        *(uint8_t*)(&var_110 + i_1) = eax_29;
    }
    uint32_t var_228_1 = 0;

    for (int32_t i_2 = 0; i_2 < arg2; i_2 += 1)
    {
        char eax_37;
        int32_t edx_13;
        edx_13 = HIGHD(((int64_t)(var_224 + 1)));
        eax_37 = LOWD(((int64_t)(var_224 + 1)));
        uint32_t edx_14 = (edx_13 >> 0x18);
        var_224 = (((uint32_t)(eax_37 + edx_14)) - edx_14);
        char eax_46;
        int32_t edx_16;
        edx_16 = HIGHD(((int64_t)(var_228_1 + ((uint32_t)*(uint8_t*)(var_224 + &var_110)))));
        eax_46 = LOWD(((int64_t)(var_228_1 + ((uint32_t)*(uint8_t*)(var_224 + &var_110)))));
        uint32_t edx_17 = (edx_16 >> 0x18);
        var_228_1 = (((uint32_t)(eax_46 + edx_17)) - edx_17);
        char eax_52 = *(uint8_t*)(var_228_1 + &var_110);
        *(uint8_t*)(var_228_1 + &var_110) = *(uint8_t*)(var_224 + &var_110);
        *(uint8_t*)(&var_110 + var_224) = eax_52;
        *(uint8_t*)((char*)arg5 + i_2) = (*(uint8_t*)(((uint32_t)(*(uint8_t*)(var_228_1 + &var_110) + *(uint8_t*)(var_224 + &var_110))) + &var_110) ^ *(uint8_t*)((char*)arg1 + i_2));
    }

    if (eax_3 == *(uint32_t*)((char*)gsbase + 0x14))
        return (eax_3 - *(uint32_t*)((char*)gsbase + 0x14));

    __stack_chk_fail_local();
    /* no return */
}

