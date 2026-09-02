---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-fence-h
title: native_fence.h
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > C API > 头文件 > native_fence.h
category: harmonyos-references
scraped_at: 2026-09-02T15:02:45+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:dd6f8a738880505f1fdd54d1bbd41e6d187b5441a76c1fbe5dabbfb7559934ff
---

## 概述

定义获取和使用NativeFence的相关函数。

**引用文件：** <native\_fence/native\_fence.h>

**库：** libnative\_fence.so

**起始版本：** 20

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeWindow

**相关模块：** [NativeFence](capi-nativefence.md)

## 汇总

### 函数

| 名称 | 描述 |
| --- | --- |
| [bool OH\_NativeFence\_IsValid(int fenceFd)](capi-native-fence-h.md#oh_nativefence_isvalid) | 检查fenceFd是否有效。 |
| [bool OH\_NativeFence\_Wait(int fenceFd, uint32\_t timeout)](capi-native-fence-h.md#oh_nativefence_wait) | 阻塞传入的fenceFd。最大阻塞时间由超时参数决定。传入的fenceFd需要用户自己关闭。 |
| [bool OH\_NativeFence\_WaitForever(int fenceFd)](capi-native-fence-h.md#oh_nativefence_waitforever) | 永久阻塞传入的fenceFd。传入的fenceFd需要用户自己关闭。 |
| [void OH\_NativeFence\_Close(int fenceFd)](capi-native-fence-h.md#oh_nativefence_close) | 关闭fenceFd。 |

## 函数说明

### OH\_NativeFence\_IsValid()

```c
bool OH_NativeFence_IsValid(int fenceFd)
```

**描述**

检查fenceFd是否有效。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| int fenceFd | 表示一个文件描述符，用于定时同步。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 返回true表示fenceFd有效，返回false表示该值是一个负整数。 |

### OH\_NativeFence\_Wait()

```c
bool OH_NativeFence_Wait(int fenceFd, uint32_t timeout)
```

**描述**

阻塞传入的fenceFd。最大阻塞时间由超时参数决定。传入的fenceFd需要用户自己关闭。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| int fenceFd | 表示一个文件描述符，用于定时同步。 |
| uint32\_t timeout | 表示等待时间。单位为毫秒，0表示接口立即返回。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 返回true表示对应的fenceFd有信号触发；  在以下情况会返回false：  1.传入的fenceFd为负整数。  2.在指定的超时时间内无信号触发。  3.调用底层poll接口失败。  4.超时时间设置为0。  5.接口中复制文件描述符执行失败。 |

### OH\_NativeFence\_WaitForever()

```c
bool OH_NativeFence_WaitForever(int fenceFd)
```

**描述**

永久阻塞传入的fenceFd。传入的fenceFd需要用户自己关闭。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| int fenceFd | 表示一个文件描述符，用于定时同步。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 返回true表示对应的fenceFd有信号触发；  在以下情况会返回false：  1.传入的fenceFd为负整数。  2.在指定的超时时间内无信号触发，永久等待。  3.接口中复制文件描述符执行失败。 |

### OH\_NativeFence\_Close()

```c
void OH_NativeFence_Close(int fenceFd)
```

**描述**

关闭fenceFd。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| int fenceFd | 表示一个文件描述符，用于定时同步。该值是一个非负整数。 |
