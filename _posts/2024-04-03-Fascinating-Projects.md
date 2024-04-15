---
title: Fascinating Projects - A Daily Endeavor
description: Reverse engineering an Bluetooth Low Energy light from alipress
author: dingisoul
date: 2024-04-03 18:19:00 +0800
categories: [Blogging, Daily]
tags: [Daily]
pin: true
math: true
mermaid: true
image:
  path: /assets/img/project-preview.webp
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
