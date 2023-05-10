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
bootmenupolicy          Standard```

But an infected one looks like this 
