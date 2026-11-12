---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataguard-encryptedusbmanager
title: encryptedUsbManager (加密U盘管理)
breadcrumb: API参考 > 系统 > 安全 > Enterprise Data Guard Kit（企业数据保护服务） > ArkTS API > encryptedUsbManager (加密U盘管理)
category: harmonyos-references
scraped_at: 2026-11-12T09:55:23+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:f49f3eb777522100befde95aac74d7eb88f3c29cdd6697340dfb0ba169ec0521
---

通过dm-crypt机制对U盘进行加密管理，支持挂载或卸载加密U盘的加密区与交换区。

仅供企业安全管控类MDM应用申请权限后使用。

**起始版本：** 26.0.1

## 导入模块

```typescript
import { encryptedUsbManager } from '@kit.EnterpriseDataGuardKit';
```

## CryptType

加密类型枚举。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PCService.EnterpriseEncryptBlock

**起始版本：** 26.0.1

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PLAIN | 0 | plain模式。 |

## CipherType

加密算法和模式枚举。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PCService.EnterpriseEncryptBlock

**起始版本：** 26.0.1

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SM4\_XTS\_PLAIN64 | 0x0 | sm4-xts-plain64算法。 |
| SM4\_CBC\_PLAIN64 | 0x1 | sm4-cbc-plain64算法。 |
| SM4\_ECB | 0x2 | sm4-ecb算法。 |
| AES\_XTS\_PLAIN64 | 0x10 | aes-xts-plain64算法。 |
| AES\_ECB | 0x20 | aes-ecb算法。 |

## DiskInfo

表示磁盘设备信息，用于匹配待操作的磁盘对象。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PCService.EnterpriseEncryptBlock

**起始版本：** 26.0.1

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| vendorId | number | 否 | 否 | 厂商标识（Vendor ID）。 |
| productId | number | 否 | 否 | 产品标识（Product ID）。 |
| busNum | number | 否 | 否 | 总线号。 |
| devAddress | number | 否 | 否 | 设备地址。 |

## PartitionInfo

表示块设备分区信息，对应losetup命令的绑定参数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PCService.EnterpriseEncryptBlock

**起始版本：** 26.0.1

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| offset | number | 否 | 否 | loop设备绑定偏移量，单位：Byte，对应losetup的-o参数。 |
| sizeLimit | number | 否 | 否 | loop设备绑定大小限制，单位：Byte，对应losetup的--sizelimit参数。 |

## CryptInfo

表示加密U盘的加密参数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PCService.EnterpriseEncryptBlock

**起始版本：** 26.0.1

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | [CryptType](dataguard-encryptedusbmanager.md#crypttype) | 否 | 否 | 加密类型，如plain模式。 |
| cipher | [CipherType](dataguard-encryptedusbmanager.md#ciphertype) | 否 | 否 | 加密算法与模式，如sm4-xts-plain64。 |
| keySize | number | 否 | 否 | 密钥长度，单位：bit，取值范围：(0, 512]。 |
| keyFile | string | 否 | 否 | 表示dm-crypt密钥文件路径，密钥以原始二进制的格式进行存储。 |

## MountInfo

表示挂载选项。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PCService.EnterpriseEncryptBlock

**起始版本：** 26.0.1

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| readOnly | boolean | 否 | 否 | 是否以只读方式挂载。true表示只读方式挂载，false表示读写方式挂载。 |

## encryptedUsbManager.openEncryptedPartition

openEncryptedPartition(diskInfo: DiskInfo, partitionInfo: PartitionInfo, cryptInfo: CryptInfo, mountInfo: MountInfo): Promise<void>

打开加密U盘加密区并挂载加密区。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.ENTERPRISE\_ENCRYPT\_BLOCK\_DEVICE

**系统能力：** SystemCapability.PCService.EnterpriseEncryptBlock

**起始版本：** 26.0.1

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| diskInfo | [DiskInfo](dataguard-encryptedusbmanager.md#diskinfo) | 是 | 磁盘设备信息，用于匹配目标磁盘。 |
| partitionInfo | [PartitionInfo](dataguard-encryptedusbmanager.md#partitioninfo) | 是 | 块设备分区信息。 |
| cryptInfo | [CryptInfo](dataguard-encryptedusbmanager.md#cryptinfo) | 是 | 加密参数。 |
| mountInfo | [MountInfo](dataguard-encryptedusbmanager.md#mountinfo) | 是 | 挂载选项。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](errorcode-enterprise-dataguard.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 801 | Capability not supported. Possible causes:  1. The hardware does not support the capability;  2. The chip does not support the capability;  3. A dependentservice feature is not supported. |
| 1030300001 | System service error. |
| 1030300002 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 1030300003 | Failed to bind the loop device. |
| 1030300004 | Failed to create the dm-crypt volume. |
| 1030300005 | Failed to mount the volume. |
| 1030300009 | Disk not found. |
| 1030300010 | Failed to get the disk list from the disk manager service. |
| 1030300013 | The volume is already mounted. |

**示例：**

```typescript
import { encryptedUsbManager } from '@kit.EnterpriseDataGuardKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { usbManager } from '@kit.BasicServicesKit';

// USB-IF 国际标准: Mass Storage - U盘、移动硬盘
const USB_CLASS_MASS_STORAGE = 8;

function getDiskInfo(): encryptedUsbManager.DiskInfo | null {
  const devices: Array<usbManager.USBDevice> = usbManager.getDevices();
  const storageDevice = devices.find(device => {
    // 设备类型代码为U盘、移动硬盘
    if (device.clazz === USB_CLASS_MASS_STORAGE) {
      return true;
    }
    for (const config of device.configs) {
      for (const iface of config.interfaces) {
        if (iface.clazz === USB_CLASS_MASS_STORAGE) {
          return true;
        }
      }
    }
    return false;
  });

  let diskInfo: encryptedUsbManager.DiskInfo | null = null;
  if (storageDevice) {
    diskInfo = {
      vendorId: storageDevice.vendorId,
      productId: storageDevice.productId,
      busNum: storageDevice.busNum,
      devAddress: storageDevice.devAddress
    };
  }
  return diskInfo;
}

try {
  let diskInfo: encryptedUsbManager.DiskInfo | null = getDiskInfo();
  if (diskInfo) {
    let partitionInfo: encryptedUsbManager.PartitionInfo = { offset: 210763776, sizeLimit: 2147483648 };
    let cryptInfo: encryptedUsbManager.CryptInfo = {
      type: encryptedUsbManager.CryptType.PLAIN,
      cipher: encryptedUsbManager.CipherType.SM4_XTS_PLAIN64,
      keySize: 256,
      keyFile: '/data/test/sm4_keyfile.bin'
    };
    let mountInfo: encryptedUsbManager.MountInfo = { readOnly: false };

    encryptedUsbManager.openEncryptedPartition(diskInfo, partitionInfo, cryptInfo, mountInfo).then(() => {
      console.info('Succeeded in opening encrypted partition.');
    }).catch((err: BusinessError) => {
      console.error(`Failed to open encrypted partition. Code: ${err.code}, message: ${err.message}.`);
    });
  } else {
    console.error('Failed to get disk info.');
  }
} catch (e) {
  console.error(`Failed to execute the openEncryptedPartition method. Code: ${e.code}, message: ${e.message}.`);
}
```

## encryptedUsbManager.closeEncryptedPartition

closeEncryptedPartition(diskInfo: DiskInfo): Promise<void>

卸载加密U盘的加密区并关闭加密区。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.ENTERPRISE\_ENCRYPT\_BLOCK\_DEVICE

**系统能力：** SystemCapability.PCService.EnterpriseEncryptBlock

**起始版本：** 26.0.1

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| diskInfo | [DiskInfo](dataguard-encryptedusbmanager.md#diskinfo) | 是 | 磁盘设备信息，用于匹配目标磁盘。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](errorcode-enterprise-dataguard.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 801 | Capability not supported. Possible causes:  1. The hardware does not support the capability;  2. The chip does not support the capability;  3. A dependentservice feature is not supported. |
| 1030300001 | System service error. |
| 1030300002 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 1030300006 | Failed to unmount the volume. |
| 1030300007 | Failed to destroy the dm-crypt volume. |
| 1030300008 | Failed to unbind the loop device. |
| 1030300009 | Disk not found. |
| 1030300010 | Failed to get the disk list from the disk manager service. |
| 1030300011 | Failed to get the volume list from the disk manager service. |
| 1030300012 | Volume not found. |

**示例：**

```typescript
import { encryptedUsbManager } from '@kit.EnterpriseDataGuardKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { usbManager } from '@kit.BasicServicesKit';

// USB-IF 国际标准: Mass Storage - U盘、移动硬盘
const USB_CLASS_MASS_STORAGE = 8;

function getDiskInfo(): encryptedUsbManager.DiskInfo | null {
  const devices: Array<usbManager.USBDevice> = usbManager.getDevices();
  const storageDevice = devices.find(device => {
    // 设备类型代码为U盘、移动硬盘
    if (device.clazz === USB_CLASS_MASS_STORAGE) {
      return true;
    }
    for (const config of device.configs) {
      for (const iface of config.interfaces) {
        if (iface.clazz === USB_CLASS_MASS_STORAGE) {
          return true;
        }
      }
    }
    return false;
  });

  let diskInfo: encryptedUsbManager.DiskInfo | null = null;
  if (storageDevice) {
    diskInfo = {
      vendorId: storageDevice.vendorId,
      productId: storageDevice.productId,
      busNum: storageDevice.busNum,
      devAddress: storageDevice.devAddress
    };
  }
  return diskInfo;
}

try {
  let diskInfo: encryptedUsbManager.DiskInfo | null = getDiskInfo();
  if (diskInfo) {
    encryptedUsbManager.closeEncryptedPartition(diskInfo).then(() => {
      console.info('Succeeded in closing encrypted partition.');
    }).catch((err: BusinessError) => {
      console.error(`Failed to close encrypted partition. Code: ${err.code}, message: ${err.message}.`);
    });
  } else {
    console.error('Failed to get disk info.');
  }
} catch (e) {
  console.error(`Failed to execute the closeEncryptedPartition method. Code: ${e.code}, message: ${e.message}.`);
}
```

## encryptedUsbManager.openSwapPartition

openSwapPartition(diskInfo: DiskInfo, partitionInfo: PartitionInfo, mountInfo: MountInfo): Promise<void>

挂载加密U盘的交换区。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.ENTERPRISE\_ENCRYPT\_BLOCK\_DEVICE

**系统能力：** SystemCapability.PCService.EnterpriseEncryptBlock

**起始版本：** 26.0.1

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| diskInfo | [DiskInfo](dataguard-encryptedusbmanager.md#diskinfo) | 是 | 磁盘设备信息，用于匹配目标磁盘。 |
| partitionInfo | [PartitionInfo](dataguard-encryptedusbmanager.md#partitioninfo) | 是 | 块设备分区信息，对应losetup绑定参数。 |
| mountInfo | [MountInfo](dataguard-encryptedusbmanager.md#mountinfo) | 是 | 挂载选项。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](errorcode-enterprise-dataguard.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 801 | Capability not supported. Possible causes:  1. The hardware does not support the capability;  2. The chip does not support the capability;  3. A dependentservice feature is not supported. |
| 1030300001 | System service error. |
| 1030300002 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 1030300003 | Failed to bind the loop device. |
| 1030300005 | Failed to mount the volume. |
| 1030300009 | Disk not found. |
| 1030300010 | Failed to get the disk list from the disk manager service. |
| 1030300013 | The volume is already mounted. |

**示例：**

```typescript
import { encryptedUsbManager } from '@kit.EnterpriseDataGuardKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { usbManager } from '@kit.BasicServicesKit';

// USB-IF 国际标准: Mass Storage - U盘、移动硬盘
const USB_CLASS_MASS_STORAGE = 8;

function getDiskInfo(): encryptedUsbManager.DiskInfo | null {
  const devices: Array<usbManager.USBDevice> = usbManager.getDevices();
  const storageDevice = devices.find(device => {
    // 设备类型代码为U盘、移动硬盘
    if (device.clazz === USB_CLASS_MASS_STORAGE) {
      return true;
    }
    for (const config of device.configs) {
      for (const iface of config.interfaces) {
        if (iface.clazz === USB_CLASS_MASS_STORAGE) {
          return true;
        }
      }
    }
    return false;
  });

  let diskInfo: encryptedUsbManager.DiskInfo | null = null;
  if (storageDevice) {
    diskInfo = {
      vendorId: storageDevice.vendorId,
      productId: storageDevice.productId,
      busNum: storageDevice.busNum,
      devAddress: storageDevice.devAddress
    };
  }
  return diskInfo;
}

try {
  let diskInfo: encryptedUsbManager.DiskInfo | null = getDiskInfo();
  if (diskInfo) {
    let partitionInfo: encryptedUsbManager.PartitionInfo = { offset: 210763776, sizeLimit: 2147483648 };
    let mountInfo: encryptedUsbManager.MountInfo = { readOnly: false };

    encryptedUsbManager.openSwapPartition(diskInfo, partitionInfo, mountInfo).then(() => {
      console.info('Succeeded in opening swap partition.');
    }).catch((err: BusinessError) => {
      console.error(`Failed to open swap partition. Code: ${err.code}, message: ${err.message}.`);
    });
  } else {
    console.error('Failed to get disk info.');
  }
} catch (e) {
  console.error(`Failed to execute the openSwapPartition method. Code: ${e.code}, message: ${e.message}.`);
}
```

## encryptedUsbManager.closeSwapPartition

closeSwapPartition(diskInfo: DiskInfo): Promise<void>

卸载加密U盘的交换区。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.ENTERPRISE\_ENCRYPT\_BLOCK\_DEVICE

**系统能力：** SystemCapability.PCService.EnterpriseEncryptBlock

**起始版本：** 26.0.1

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| diskInfo | [DiskInfo](dataguard-encryptedusbmanager.md#diskinfo) | 是 | 磁盘设备信息，用于匹配目标磁盘。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](errorcode-enterprise-dataguard.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 801 | Capability not supported. Possible causes:  1. The hardware does not support the capability;  2. The chip does not support the capability;  3. A dependentservice feature is not supported. |
| 1030300001 | System service error. |
| 1030300002 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 1030300006 | Failed to unmount the volume. |
| 1030300008 | Failed to unbind the loop device. |
| 1030300009 | Disk not found. |
| 1030300010 | Failed to get the disk list from the disk manager service. |
| 1030300011 | Failed to get the volume list from the disk manager service. |
| 1030300012 | Volume not found. |

**示例：**

```typescript
import { encryptedUsbManager } from '@kit.EnterpriseDataGuardKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { usbManager } from '@kit.BasicServicesKit';

// USB-IF 国际标准: Mass Storage - U盘、移动硬盘
const USB_CLASS_MASS_STORAGE = 8;

function getDiskInfo(): encryptedUsbManager.DiskInfo | null {
  const devices: Array<usbManager.USBDevice> = usbManager.getDevices();
  const storageDevice = devices.find(device => {
    // 设备类型代码为U盘、移动硬盘
    if (device.clazz === USB_CLASS_MASS_STORAGE) {
      return true;
    }
    for (const config of device.configs) {
      for (const iface of config.interfaces) {
        if (iface.clazz === USB_CLASS_MASS_STORAGE) {
          return true;
        }
      }
    }
    return false;
  });

  let diskInfo: encryptedUsbManager.DiskInfo | null = null;
  if (storageDevice) {
    diskInfo = {
      vendorId: storageDevice.vendorId,
      productId: storageDevice.productId,
      busNum: storageDevice.busNum,
      devAddress: storageDevice.devAddress
    };
  }
  return diskInfo;
}

try {
  let diskInfo: encryptedUsbManager.DiskInfo | null = getDiskInfo();
  if (diskInfo) {
    encryptedUsbManager.closeSwapPartition(diskInfo).then(() => {
      console.info('Succeeded in closing swap partition.');
    }).catch((err: BusinessError) => {
      console.error(`Failed to close swap partition. Code: ${err.code}, message: ${err.message}.`);
    });
  } else {
    console.error('Failed to get disk info.');
  }
} catch (e) {
  console.error(`Failed to execute the closeSwapPartition method. Code: ${e.code}, message: ${e.message}.`);
}
```
