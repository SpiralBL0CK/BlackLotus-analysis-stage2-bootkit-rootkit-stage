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


=============================================================================

For wayyy later after i learn how to debug this there's a part in the rootkit where it looks for a certain pettern as it can be seen in the images
![1](https://github.com/SpiralBL0CK/BlackLotus-analysis-stage2-bootkit-rootkit-stage/assets/25670930/781617af-a1e0-4041-b7c5-7f9b0dcc7998)

![2](https://github.com/SpiralBL0CK/BlackLotus-analysis-stage2-bootkit-rootkit-stage/assets/25670930/2961a021-7b43-46e2-afcf-5b0148cb163e)

![3](https://github.com/SpiralBL0CK/BlackLotus-analysis-stage2-bootkit-rootkit-stage/assets/25670930/23fb490c-3918-460f-ab8f-f5f540cdc5ba)

![4](https://github.com/SpiralBL0CK/BlackLotus-analysis-stage2-bootkit-rootkit-stage/assets/25670930/984038f9-157f-436f-a7d9-558cf460652a)

![5](https://github.com/SpiralBL0CK/BlackLotus-analysis-stage2-bootkit-rootkit-stage/assets/25670930/e761b892-2218-42f0-a62d-b14ee34210cc)

![6](https://github.com/SpiralBL0CK/BlackLotus-analysis-stage2-bootkit-rootkit-stage/assets/25670930/0b9dae4d-43ae-4415-9c06-b29de3d7a4f8)


