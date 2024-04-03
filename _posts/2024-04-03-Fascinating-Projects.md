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

![LoLRa](https://www.youtube.com/watch?v=eIdHBDSQHyw)

Have a look at [lolra](https://github.com/cnlohr/lolra). In this project, it shows how using either a shift register (i.e. I2S or SPI port) or an APLL (clock), you can send LoRa packets that can be decoded by commercial off the shelf LoRa gateways and other chips.

### Inject a backdoor in supply chain

A researcher discover a backdoor in well-known compressed package xz-utils, which is used in sshd ( ssh-server ), How it can be done ?

Have a look at [openwall](https://www.openwall.com/lists/oss-security/2024/03/29/4)

You can find how it been done. 
