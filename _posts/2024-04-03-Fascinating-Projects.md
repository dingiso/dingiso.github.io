---
title: Fascinating Projects - A Daily Endeavor description: Reverse engineering an Bluetooth Low Energy light from alipress
author: dingisoul
date: 2024-04-04 18:19:00 +0800
categories: [Blogging, Daily]
tags: [Daily]
pin: true
math: true
mermaid: true
image:
  path: /assets/img/project-preview.jpg
  alt: project preview
---


# Fascinating Projects: A Daily Endeavor

This blog is used to broaden my horizon and make some new ideas


### Transmit LoRa Frames Without a Radio

The actual emission of a wave is made of different frequencies and phases, so can we make specific kind of wave and send it to imitate a radio? That's OK.

How we generate specific frequency with SOC (System-on-Chip), we can use the embedded clock !!!

{% include embed/youtube.html id='eIdHBDSQHyw' %}

Have a look at [lolra](https://github.com/cnlohr/lolra). In this project, it shows how using either a shift register (i.e. I2S or SPI port) or an APLL (clock), you can send LoRa packets that can be decoded by commercial off the shelf LoRa gateways and other chips.

### Inject a backdoor in supply chain

A researcher discover a backdoor in well-known compressed package xz-utils, which is used in sshd ( ssh-server ), How it can be done ?

Have a look at [openwall](https://www.openwall.com/lists/oss-security/2024/03/29/4)

You can find how it been done. 

### Linking Shell Companies to their Secret Owners

This can be a Social Engineering tips I learned from [GIJN](https://gijn.org/stories/tracking-shell-companies-secret-owners/) and it's fascinating too.

0. In registrationthey can’t get around the basics on those forms: an official business  address, real names of at least some directors, and documents about the  nature of the business.

1. always seeking the ultimate beneficial owner, rather than the director or owner names you may find early in your search.
2. **Start with a quick company or person name search in** [**OpenCorporates**](https://opencorporates.com/)
3. Consider a subscription to a corporate risk database if you hit a wall with open source tools - [**Sayari**](https://sayari.com/financial-crime/), [**Orbis**](https://login.bvdinfo.com/R0/Orbis) and [**Factiva**](https://www.dowjones.com/professional/factiva/?LS=Search&utm_medium=cpc&utm_source=google&utm_campaign=AMER-US[EN]_GGL-Brand[GEN]-FA-Factiva_MT-Exact&CID=7015Y000004FylCQAS&utm_term=factiva_(e)&utm_content=&gad_source=1&gclid=Cj0KCQjwwYSwBhDcARIsAOyL0fgmrbfqHGsRhTB984bRyKqKWwdwTOH8U7-c0br0U8gHvRNeG311DH4aAsXEEALw_wcB).
4. Put yourself in the shoes of billionaires and oligarchs, because they are very predictable
5. Use vetted investigative data in the [**ICIJ Offshore Leaks Database**](https://offshoreleaks.icij.org/)
6. Flag potential criminal links in OCCRP’s follow-the-money archive - OCCRP’s [**Aleph database**](https://aleph.occrp.org/) 
7. Experiment with different spellings — and check against Google Maps.
8. Cross-search the “nuggets” you find in other free portals -  [**Open Ownership**](https://www.openownership.org/en/), the UK-based [**Register of Overseas Entities**](https://www.gov.uk/government/collections/register-of-overseas-entities#:~:text=Overseas entities who want to,owners or managing officers are.), and [**Tenders Electronic Daily**](https://ted.europa.eu/en/news/welcome-to-the-new-ted) (TED).
9. Try a family connections tool to track oligarch assets - [**RuPEP**](https://rupep.org/en/)
10. Paperwork tends to poke holes in secrecy — so keep digging.

### Change the debug path in the build outputs

[refix](https://github.com/yosefk/refix) use string replacement to change the absolute path in elf debug information so you can let the gdb select correct path of the source files been compiled 

### Fuxnet: Ukraine Against Russian Infrastructure Malware

[Claroty’s analysis](https://claroty.com/team82/research/unpacking-the-blackjack-groups-fuxnet-malware) of Fuxnet showed that the malware was likely deployed remotely. Once on a device, it would start deleting important files and directories, shutting down remote access services to prevent remote restoration, and deleting routing table information to prevent communication with other devices. Fuxnet would then delete the file system and rewrite the device’s flash memory.  

Once it has corrupted the file system and blocked access to the device, the malware attempts to physically destroy the NAND memory chip and then rewrites the UBI volume to prevent rebooting.

For example, config `vol_flags = PERSISTENT` in `/etc/ubi_vol.cfg`

If you want further prevent reboot of device, add this in start script

```shell
echo 1 > /sys/power/pm_freezer/state
echo 1 > /sys/power/state
```

In addition, fuxnet moves on to physically destroy the NAND memory chips on the device. In order to do so, the malware performs a bit-flip operation on entire sections of the SSD NAND chip, constantly writing and rewriting the memory, only stopping when the malware fails to write to the memory due to it being corrupted. Since the gateway uses NAND memory, which can only write and re-write data a certain number of times (known as the NAND write cycles), constantly rewriting the memory causes the chip to malfunction and be inoperable. 

```c
while(!is_stop) {
  if (write_reseek(fd, xbuf, rz) < 0)
    break;
  if (write_reseek(fd, xbuf, rz) < 0)
    break;
  wr_amount += 2;
  rounds +=2;
  if (rounds >= SSD_ROUNDS) {
    break;
    ssd_bad_rounds = 0
  }
}
```

### Self-made Python Asyncio 

I came to find out that Asyncio is basically just a really nice layer on top of Python Generators.

In the [article](https://jacobpadilla.com/articles/recreating-asyncio), the author create a simplified version of asyncio using just Python Generators. Then, I’m going to refactor the example to use the async and await keywords with the help of the `__await__` dunder method before coming full circle and swapping out my version for the real asyncio. By building a simple version of asyncio, hopefully, by the end of this article, you’ll be able to get a better grasp of how it does its magic!

self-learning notes: 

Q: Is function a class (such as C++ class) ? 

A: Yes, function has stack to store it's state (local variables)

Q: Why this is important ? 

A: We need a function to **stop** and save it's state when stop, so other **thread** can run 

Q: Give an example 

A: a iterator through list can be seen to call multiple access and increase. So if every turn in async can be seen as one access and increase.

Coding Details:

1. seen `yield` as a special return, when the function is called by `next()` not directly, the next function will check the return (yield and normal return). if there is a true `return`, it will generate a `StopIteration`. If it's a yield, it will stop at yield and remember the current program pointer and function context

2. asyncio is just: generator + state machine + event loop 

### [SYZYGY](https://syzygyfpga.io/)

An open standard for high-performance peripheral connectivity. 

* Low cost, compact, high-performance
* connectors
* Pin count economizes available FPGA I/O
* Low cost cable options
* FREE to license

> My Words: It seems that this protocol is designed to hit the "sweet spot" for different peripherals, primarily in the field of FPGAs.

### [CCS 16 Reviewing Process](https://www.cs.cornell.edu/andru/ccs16/report.html#/)

Statistics of CCS 16 Reviewing Process 

### Dumping Firmware from SPI flash chip 

[This Blog](https://www.blackhillsinfosec.com/dumping-firmware-with-the-ch341a-programmer/) shows how to use [CH341A](https://github.com/boseji/CH341-Store) and [AsProgrammer](https://github.com/nofeletru/UsbAsp-flash/releases/) to dump the firmware from flash chip. 

