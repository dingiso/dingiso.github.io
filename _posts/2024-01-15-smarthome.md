---
title: Smart Home with Home Assistant
description: how to establish a home assistant in local network
author: dingisoul
date: 2024-04-03 19:18:27 +0800
categories: [Blogging, iot]
tags: [iot]
image:
  path: /assets/img/ha-preview.jpg
  alt: home assistant
---

# Smart Home 

## Overview

1. 网关管理设备： [Home Assistant](https://www.home-assistant.io/) 非常好的管理系统
2. 开源扫地机器人系统： [Veletudo](https://valetudo.cloud/)

### 推荐的设备

1. **Hub:** 利用 Home Assitant 装一个并通过 USB 扩展不同的协议（例如zigbee）
2. **Smart bulbs:** 
   1. WIFI-Shelly and Athom,
   2. LAN: Xiaomi’s Yeelight,
   3. Zigbee: IKEA’s Tradfri line of Zigbee 
   4. 剩下的 Philips Hue 也很好
3. **Switches and plugs:** Inovelli’s Zigbee switches 在 home assistant 社区里很受欢迎,但是他要 $50. Zooz and Lutron 也很好. 你也可以找到很多替代品,例如 Sonoff, IKEA, Athom, and Shelly.
4. **Sensors**: 找便宜的? Sonoff’s range of sensors works reasonably well. However, 我推荐更可靠的Aqara or Aeotec, 尽管他们需要 Zigbee. 我使用 IKEA’s 运动传感器，他们也相当可靠.
5. **Robot vacuum**: 尝试 Valetudo 中推荐的款式或者也可以使用 Home Assistant 官方支持的 Dreame and Roborock vacuums.
6. **智能窗帘**: IKEA 的智能窗帘在社区中很受欢迎. I’ve also heard good things about Third Reality and Smartwings, which come equipped with Zigbee.
7. **Other appliances**: Want to automate your AC, garage  door, or ceiling fan that has its own remote? Use an inexpensive Wi-Fi  IR or RF blaster. I saved \$100 buying an AC without smart features,  whereas my Broadlink RM Mini IR blaster cost just \$20, and can also  control my ceiling fan and TV in the same room.

Wi-Fi 设备经常使用 Tuya Smart IoT platform, 也可以被结合进 Home Assistant



