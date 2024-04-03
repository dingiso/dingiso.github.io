---
title: Reverse an BLE Light
description: Reverse engineering an Bluetooth Low Energy light from alipress
author: dingisoul
date: 2024-03-21 21:15:00 +0800
categories: [Blogging, Hack]
tags: [Hack]
pin: true
math: true
mermaid: true
image:
  path: /commons/devices-mockup.png
  lqip: data:image/webp;base64,UklGRpoAAABXRUJQVlA4WAoAAAAQAAAADwAABwAAQUxQSDIAAAARL0AmbZurmr57yyIiqE8oiG0bejIYEQTgqiDA9vqnsUSI6H+oAERp2HZ65qP/VIAWAFZQOCBCAAAA8AEAnQEqEAAIAAVAfCWkAALp8sF8rgRgAP7o9FDvMCkMde9PK7euH5M1m6VWoDXf2FkP3BqV0ZYbO6NA/VFIAAAA
  alt: Responsive rendering of Chirpy theme on multiple devices.
---

# Reverse one BLE LED

I have bought one BLE(Bluetooth Low Energy) LED and want to control it with [Home Assistant](https://www.home-assistant.io/).

There are many blogs about BLE sniffing for these types of lights, for example [BLE_LED_strip](https://github.com/NotACoin/BLE_LED_strip). Although I did not actually use this method, but thanks to this comprehensive guide.

I tried the method mentioned above, but encoutered the following issues:

1. The Bluetooth HCI log was not included in the bug report when my android phone is not rooted
2. After rooting, the btsnoop_hci.log did not contain much information. Sepcifically, there were no Bluetooth records sent to the remote device.

However, there is still one method available: decompiling the Android application. These little brands' Bluetooth LED applications are also small and often without obfuscation. For example, this light uses the [Allbest Home](https://play.google.com/store/apps/details?id=com.th.joylight). 

### APK decompile

[Jadx](https://github.com/skylot/jadx) is an excellent DEX to Java decompiler, well-suited for our purpose.

The decompiled result is absolutely great. I simply opened the APK file without needing any other operations, and the generated code is highly readable.

I searched for classes and functions containing the keywords `light` `Send` `ble` and `bluetooth`

After some searching, I found methods in `CommandUtil` class that fit the requirements. 

```java
// class com.th.qc.command.CommandUtil
// other methods such as sendLightMode sendLightBright sendLightColor... can also been found here
public final void sendLightSwitch(boolean z) {
    BlueConnectionUtil.getInstance().writeCmd(pack((byte) 17, z ? (byte) 1 : (byte) 0));
}
```

Now we just need to figure out how the `writeCmd` method sends BLE commands and how the `pack` method generates the commands been sent.

##### pack

First, let us see the implementation of  `pack` function:

```java
 public final byte[] pack(byte b, byte... data) {
    Intrinsics.checkNotNullParameter(data, "data");
    ArrayList arrayList = new ArrayList();
    arrayList.add((byte) -96);
    arrayList.add(Byte.valueOf(b));
    arrayList.add(Byte.valueOf((byte) (data.length + 3)));
    for (byte b2 : data) {
        arrayList.add(Byte.valueOf(b2));
    }
    ArrayList arrayList2 = arrayList;
    byte[] shortToByte = BleUtils.getShortToByte(BlockUtils.crc16Check(CollectionsKt.toByteArray(arrayList2)));
    Intrinsics.checkNotNullExpressionValue(shortToByte, "getShortToByte(crc16)");
    arrayList.add(Byte.valueOf(shortToByte[1]));
    arrayList.add(Byte.valueOf(shortToByte[0]));
    return CollectionsKt.toByteArray(arrayList2);
}

public static int calculateCRC16(byte[] bArr) {
    int i = 65535;
    for (byte b : bArr) {
        i ^= b & UByte.MAX_VALUE;
        for (int i2 = 0; i2 < 8; i2++) {
            i = (i & 1) != 0 ? (i >> 1) ^ 40961 : i >> 1;
        }
    }
    return i;
}
```

The method is very straightforward and easy to read. Let's convert it to python :happy: 

```python
# python version 
def crc16(in_) -> int:
    i = 65535
    for b in in_:
        i ^= b & 0xff
        for i2 in range(0,8):
            if (i&1) != 0:
                i = (i>>1) ^ 40961
            else:
                i = i >> 1
    return i

def getshortToByte(i) -> list:
    return [i&0xff,(i>>8&0xff)]

def pack(b, data) -> list:
    ret = []
    ret.append(0xA0)
    ret.append(b)
    ret.append(len(data) + 3)
    for i in data:
        ret.append(i)
    ret += getshortToByte(crc16(ret))
    return ret
```

##### writeCmd

Secondly, let's dig into the `writeCmd` method. Keep in mind that we don't need to understand every detail about the implementation. We only need to stop when the method and parameter names seems familiar to us. 

```java
// in order to simplify the code, I delete some unimportant codes
public wirteCmd(byte[] bArr) {
	BleDevice connectDevice = BleManager.getInstance().getConnectDevice(str);
    if (connectDevice != null) {
        writeShakeBle(connectDevice, bArr, this.mWriteCallback);
    }
}

private void writeShakeBle(final BleDevice bleDevice, final byte[] bArr, final BleWriteCallback bleWriteCallback) {
	BleManager bleManager = BleManager.getInstance();
    String serviceUUID = bleDevice.getFilter().getServiceUUID();
    String writeUUID = bleDevice.getFilter().getWriteUUID();
    if (bleWriteCallback == null) {
        bleWriteCallback = this.mWriteCallback;
    }
    bleManager.write(bleDevice, serviceUUID, writeUUID, bArr, bleWriteCallback);
    return null;
}

public void write(BleDevice bleDevice, String serviceUUID, String writeUUID, byte[] bArr, BleWriteCallback bleWriteCallback) {
        bleBluetooth.newBleConnector().withUUIDString(serviceUUID, writeUUID).writeCharacteristic(bArr, bleWriteCallback, writeUUID);
}
```

the `UUID` and `writeCharacteristic` terms seem familiar to me because these words are inside the BLE protocol definition, which you can find in the manual. I will also explain them in the next section too.

## BLE

In Bluetooth Low Energy (BLE), a UUID (Universally Unique Identifier) is a 128-bit number used to identify and distinguish different BLE services, characteristics, and descriptors. UUIDs are used to define the structure and functionality of BLE data.

A characteristic is a basic data entity in BLE that carries the actual data payload. Characteristics are grouped under services, which are collections of related characteristics. Each characteristic has:

1. UUID: A unique 128-bit identifier that defines the type of data the characteristic represents (e.g., heart rate, temperature, etc.).
2. Properties: Bit flags that define how the characteristic can be used and accessed. These include:
  * Read: Allows the characteristic value to be read.
  * Write: Allows the characteristic value to be written.
  * Notify: Allows the server to send updates to the client when the characteristic value changes.
  * Indicate: Similar to Notify, but with an acknowledgment from the client.
3. Value: The actual data payload of the characteristic.
4. Descriptors (optional): Additional metadata or attributes related to the characteristic, such as value ranges, units, or descriptions.

For example, a Heart Rate Service might have a Heart Rate Measurement Characteristic with a UUID of **0x2A37**. This characteristic could have the Read and Notify properties enabled, allowing a client to read the current heart rate value and receive updates when it changes.

In summary, UUIDs are used to identify BLE entities, characteristics contain the actual data, and properties define how the characteristic can be accessed and used within the BLE protocol.

### Bleak 

[bleak](https://github.com/hbldh/bleak) is python library to communicate with BLE protocol. Our implementation of light switch control will depend on it.  

> A Bluetooth peripheral may have several characteristics with the same UUID, so the means of specifying characteristics by UUID or string representation of it might not always work in bleak version > 0.7.0. One can now also use the characteristic’s handle or even the `BleakGATTCharacteristic` object itself in `read_gatt_char`, `write_gatt_char`, `start_notify`, and `stop_notify`.

One can use the `BleakClient` to connect to a Bluetooth device and read all services via the asynchronous context manager like this:

```python
import asyncio
from bleak import BleakClient

address = "xx:xx:xx:xx:xx:xx"
async with BleakClient(address) as client:
    for service in client.services:
        print(f"Service UUID: {service.uuid}")
        characteristics = service.characteristics
        for characteristic in characteristics:
            print(f"  Characteristic UUID: {characteristic.uuid}")
            print(f"  Properties: {characteristic.properties}")
```

> It is recommended to use the asyncio library with BleakClient.

For our test case, the script will output all services and corresponding characteristics like this:

```
Service UUID: 0000ff10-0000-1000-8000-00805f9b34fb
  Characteristic UUID: 0000ff11-0000-1000-8000-00805f9b34fb
    Properties: notify
  Characteristic UUID: 0000ff12-0000-1000-8000-00805f9b34fb
    Properties: read, write
```

The one we need to focus on is the UUID with the `write` property

## Script

Now, with the knowledge we gained from the previous sections, we can write the code:

```python
from bleak import BleakClient

def crc16(in_) -> int:
    i = 65535
    for b in in_:
        i ^= b & 0xff
        for i2 in range(0,8):
            if (i&1) != 0:
                i = (i>>1) ^ 40961
            else:
                i = i >> 1
    return i

def getshortToByte(i) -> list:
    return [i&0xff,(i>>8&0xff)]

def pack(b, data) -> list:
    ret = []
    ret.append(0xA0)
    ret.append(b)
    ret.append(len(data) + 3)
    for i in data:
        ret.append(i)
    ret += getshortToByte(crc16(ret))
    return ret

LIGHT_ON_CMD = bytes(pack(17,[1]))

address = "90:00:00:51:8E:27"
LIGHT_UUID = # test your uuid here 
async with BleakClient(address) as client:
    await client.write_gatt_char(LIGHT_UUID, LIGHT_ON_CMD)
```

1. The python script needs the MAC address first. You can obtain it from your phone using [nRF Connect](https://apps.apple.com/cn/app/nrf-connect-for-mobile/id1054362403?l=en-GB). For instructions on using nRF Connect, refer to this [manual](https://urish.medium.com/reverse-engineering-a-bluetooth-lightbulb-56580fcb7546). Match the name with the MAC address yourself.

2. Choose the characteristic with the write property and configure it as `LIGHT_UUID`

3. Run the script

4. Success! the light is on. 

5. You can explore other services on your own.

![BEL LED Light Strip](https://www.ukledlights.co.uk/wp-content/uploads/2020/03/led-strip-light-12v-blue-ip65-ukledlights.co_.uk_-1024x1024.jpg)

## TODO

Add the device as [HACS](https://hacs.xyz/) integrations to home assistant 

## References

- [bleak usage](https://bleak.readthedocs.io/en/latest/usage.html)
- [BLE_LED_Strip Reverse Engineering](https://github.com/NotACoin/BLE_LED_strip?tab=readme-ov-file)
- [Reverse Engineering a bulb](https://urish.medium.com/reverse-engineering-a-bluetooth-lightbulb-56580fcb7546)
- 
