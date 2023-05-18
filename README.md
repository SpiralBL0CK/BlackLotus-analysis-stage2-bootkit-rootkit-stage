# BlackLotus-analysis-stage2-bootkit-rootkit-stage
BlackLotus stage 2 bootkit-rootkit analysis 

Frist things first this is how a healthy system looks like 

![1](https://github.com/SpiralBL0CK/BlackLotus-analysis-stage2-bootkit-rootkit-stage/assets/25670930/763d7c19-79da-4c01-bc64-249bde695ba7)

![2](https://github.com/SpiralBL0CK/BlackLotus-analysis-stage2-bootkit-rootkit-stage/assets/25670930/de67e159-9e15-430c-bfe4-2ab34f6b379c)

```
C:\Windows\system32>BCDEdit

Windows Boot Manager
--------------------
identifier              {bootmgr}
device                  partition=\Device\HarddiskVolume9
path                    \EFI\MICROSOFT\BOOT\BOOTMGFW.EFI
description             Windows Boot Manager
locale                  en-US
inherit                 {globalsettings}
default                 {current}
resumeobject            {3f80ecd0-df10-11ed-bafc-80a84b2564bb}
displayorder            {current}
toolsdisplayorder       {memdiag}
timeout                 30

Windows Boot Loader
-------------------
identifier              {current}
device                  partition=C:
path                    \Windows\system32\winload.efi
description             Windows 10
locale                  en-US
inherit                 {bootloadersettings}
recoverysequence        {3f80ecd2-df10-11ed-bafc-80a84b2564bb}
displaymessageoverride  Recovery
recoveryenabled         Yes
isolatedcontext         Yes
allowedinmemorysettings 0x15000075
osdevice                partition=C:
systemroot              \Windows
resumeobject            {3f80ecd0-df10-11ed-bafc-80a84b2564bb}
nx                      OptIn
bootmenupolicy          Standard

```

But an infected one looks like this 

=============================================================================

Bindiffing the original winload.efi with the one dropped by the blacklotus

![1](https://github.com/SpiralBL0CK/BlackLotus-analysis-stage2-bootkit-rootkit-stage/assets/25670930/a5beeebe-6d7e-47ed-92ce-72767242a3cc)

![2](https://github.com/SpiralBL0CK/BlackLotus-analysis-stage2-bootkit-rootkit-stage/assets/25670930/af1f2da2-cb15-430f-8809-d9c8c10e6e12)

![3](https://github.com/SpiralBL0CK/BlackLotus-analysis-stage2-bootkit-rootkit-stage/assets/25670930/3866f2f6-9a7b-4338-b303-1d1b470b71fe)

![4](https://github.com/SpiralBL0CK/BlackLotus-analysis-stage2-bootkit-rootkit-stage/assets/25670930/76aeb4af-f423-41eb-bbf6-0d08aed2433e)

We see some similarities but also some discepancies, anywayy....


=============================================================================

Cool so let's get this party started.

![1](https://github.com/SpiralBL0CK/BlackLotus-analysis-stage2-bootkit-rootkit-stage/assets/25670930/77afbc0d-1616-4af8-a8bb-4eaa5682a82b)

![1](https://github.com/SpiralBL0CK/BlackLotus-analysis-stage2-bootkit-rootkit-stage/assets/25670930/756ca67e-baf3-4e83-bb9c-77cfd1c62c63)

Cool so let's start dissecating. So first we see that we have a function which gets called. Cool so what about it ? well 

![1](https://github.com/SpiralBL0CK/BlackLotus-analysis-stage2-bootkit-rootkit-stage/assets/25670930/0f71f792-7a68-4e45-981e-2ac803606dc6)

![2](https://github.com/SpiralBL0CK/BlackLotus-analysis-stage2-bootkit-rootkit-stage/assets/25670930/89940f3b-2ac1-44a5-8376-9b5fad73bdb8)

Cool another function . Not quite... Notice something familiary ?

![1](https://github.com/SpiralBL0CK/BlackLotus-analysis-stage2-bootkit-rootkit-stage/assets/25670930/7c5d8662-72b8-4e7c-8a04-04992e4f1d2d)

![2](https://github.com/SpiralBL0CK/BlackLotus-analysis-stage2-bootkit-rootkit-stage/assets/25670930/72419316-2945-4187-8112-3976d210e7ab)

![3](https://github.com/SpiralBL0CK/BlackLotus-analysis-stage2-bootkit-rootkit-stage/assets/25670930/00ceebe5-fe73-4a28-a4c5-235cabe8786e)

![4](https://github.com/SpiralBL0CK/BlackLotus-analysis-stage2-bootkit-rootkit-stage/assets/25670930/b675edcc-b7ec-4737-afb3-5cf327bffd83)

![5](https://github.com/SpiralBL0CK/BlackLotus-analysis-stage2-bootkit-rootkit-stage/assets/25670930/1795ebdd-6e83-49b3-93bf-6b1911c2af89)

Nothing yet???

No problemo maybe now 

![1](https://github.com/SpiralBL0CK/BlackLotus-analysis-stage2-bootkit-rootkit-stage/assets/25670930/2becee86-c848-4505-b522-b9ff9969edf0)

![2](https://github.com/SpiralBL0CK/BlackLotus-analysis-stage2-bootkit-rootkit-stage/assets/25670930/eb196e09-90bf-41a1-9df6-ace8585cb6ab)

Same demangle function! Hi there old friend :)))

Cool but what about ```return (*(a1 + 88))(v2, &unk_62CEABC, 3i64);``` ?? Well honestly idk what to say just soley from a static perspective so let's try to use the debugger to understand it :))

So when we demangle the string we get 

![1](https://github.com/SpiralBL0CK/BlackLotus-analysis-stage2-bootkit-rootkit-stage/assets/25670930/071d7748-85e0-4d69-b466-f77048d9b66e)

So next when we end up to the call instruction

![1](https://github.com/SpiralBL0CK/BlackLotus-analysis-stage2-bootkit-rootkit-stage/assets/25670930/93c01e2a-86b0-4ba6-ae7c-899fb7aba5ac)

and we get no info.... great, but why is that ? bc we don't have a .pdb file so we can get debug symbols.... Cool at least ida is helpfull here. So we know that the "grand" function takes as input SystemTable->RuntimeServices, which is of type EFI_SYSTEM_TABLE. Cool if we inspect it this is a ```A pointer to the EFI Runtime Services Table.``` . if we search around googler we come around a bunch of docs but one crucial doc we come around is https://uefi.org/sites/default/files/resources/UEFI_Spec_2_1_D.pdf . 
there is says 

![1](https://github.com/SpiralBL0CK/BlackLotus-analysis-stage2-bootkit-rootkit-stage/assets/25670930/6802517e-b815-40f5-88cd-3df8899baf0a)

Cool so a struct with bunch of pointers, ye, but let's zoom in more.

So first it demangles VbsPolicyDisable, if we search google we come around eset analysis which states ```that this variable is evaluated by the Windows OS loader
during boot and if defined, the core VBS features, such as HVCI and Credential Guard will not be initialized.``` , so basically this variable is responsible for current "security" at boot level.
Cool next we have the function which takes that variable and 

![1](https://github.com/SpiralBL0CK/BlackLotus-analysis-stage2-bootkit-rootkit-stage/assets/25670930/61d0e73f-8f7c-4eff-8f70-4d259bd5beb6)

and so we can come to the conclusion that this must be a function which changes somehow the state of that variable. 
Cool so what are some possible function that could do this ? there's only one such function in EFI_SYSTEM_TABLE which EFI_SET_VARIABLE SetVariable;

So we conclude that this function simply take VbsPolicyDisable and sets it to 0B9.

=============================================================================

For wayyy later after i learn how to debug this there's a part in the rootkit where it looks for a certain pettern as it can be seen in the images
![1](https://github.com/SpiralBL0CK/BlackLotus-analysis-stage2-bootkit-rootkit-stage/assets/25670930/781617af-a1e0-4041-b7c5-7f9b0dcc7998)

![2](https://github.com/SpiralBL0CK/BlackLotus-analysis-stage2-bootkit-rootkit-stage/assets/25670930/2961a021-7b43-46e2-afcf-5b0148cb163e)

![3](https://github.com/SpiralBL0CK/BlackLotus-analysis-stage2-bootkit-rootkit-stage/assets/25670930/23fb490c-3918-460f-ab8f-f5f540cdc5ba)

![4](https://github.com/SpiralBL0CK/BlackLotus-analysis-stage2-bootkit-rootkit-stage/assets/25670930/984038f9-157f-436f-a7d9-558cf460652a)

![5](https://github.com/SpiralBL0CK/BlackLotus-analysis-stage2-bootkit-rootkit-stage/assets/25670930/e761b892-2218-42f0-a62d-b14ee34210cc)

![6](https://github.com/SpiralBL0CK/BlackLotus-analysis-stage2-bootkit-rootkit-stage/assets/25670930/0b9dae4d-43ae-4415-9c06-b29de3d7a4f8)


