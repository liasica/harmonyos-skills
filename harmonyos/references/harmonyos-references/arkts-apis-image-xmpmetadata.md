---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-xmpmetadata
title: Class (XMPMetadata)
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > ArkTS API > @ohos.multimedia.image (图片处理) > Class (XMPMetadata)
category: harmonyos-references
scraped_at: 2026-09-02T14:52:54+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:5f5a0865303a3297355325549b2fc8ceab36db3d2c81ffd1c9598472f32bf9e1
---

XMP（Extensible Metadata Platform）元数据。

**起始版本：** 26.0.0

## 导入模块

```ts
import { image } from '@kit.ImageKit';
```

## XMP路径语法

XMP路径用于定位元数据中的具体标签。路径由以下语法构件组合而成：

| 语法类别 | 说明 | 示例 |
| --- | --- | --- |
| 基本属性路径 | 使用:将命名空间前缀和标签名分隔开。 | dc:title表示Dublin Core命名空间中的title字段。 |
| 数组索引 | 使用[]配合从1起始的索引值定位元素，或使用last()访问最后一个元素。 | dc:subject[2]表示第二个元素；dc:subject[last()]表示最后一个元素。 |
| 结构体成员 | 使用/指定结构体成员。 | exif:Flash/exif:Fired表示exif:Flash字段的Fired成员。 |
| 限定符访问 | 使用/?指定限定符。也常用于访问多语言文本数组中元素的语言属性。 | dc:title/?book:lastUpdated表示title的book:lastUpdated限定符；dc:title[1]/?xml:lang表示第一个多语言文本元素的语言限定符。 |
| 命名空间前缀  （仅rootPath支持） | 仅指定命名空间前缀，遍历该命名空间下所有标签。 | dc遍历Dublin Core命名空间下的全部字段。 |

## registerXMPNamespace

registerXMPNamespace(xmpNamespace: XMPNamespace): Promise<void>

注册指定的命名空间。使用Promise异步回调。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| xmpNamespace | [XMPNamespace](arkts-apis-image-i.md#xmpnamespace) | 是 | XMP命名空间。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[Image错误码](errorcode-image.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7600206 | Invalid argument. Possible causes:  1. Invalid namespace format.  2. The uri is already registered.  3. The prefix is already registered. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

async function RegisterNamespacePrefix() {
  try {
    let xmpMetadata = new image.XMPMetadata();
    // 注册自定义命名空间，注册后方可使用该前缀创建标签。
    let xmpNamespace: image.XMPNamespace = {uri: "urn:example:book:1.0", prefix: "book"};
    await xmpMetadata.registerXMPNamespace(xmpNamespace);
    console.info('Succeeded in registering namespace prefix.');
  } catch (error) {
    let err: BusinessError = error as BusinessError;
    console.error(`Failed to register namespace prefix! code is ${err.code}, message is ${err.message}`);
  }
}
```

## setValue

setValue(path: string, type: XMPTagType, value?: string): Promise<void>

为指定路径下的XMP标签设置类型和值。使用Promise异步回调。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 目标XMP标签的路径。路径语法参见[XMP路径语法](arkts-apis-image-xmpmetadata.md#xmp路径语法)。 |
| type | [XMPTagType](arkts-apis-image-e.md#xmptagtype) | 是 | XMP标签类型。 |
| value | string | 否 | XMP标签值。默认为空字符串。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[Image错误码](errorcode-image.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7600206 | Invalid argument. Possible causes:  1. Namespace is not registered.  2. The path syntax is invalid.  3. The path does not match the type.  4. The value is invalid for the type. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

async function SetValue() {
  try {
    let xmpMetadata = new image.XMPMetadata();
    // 设置xmp:title标签的值，类型为字符串，值为'My Title'。
    // xmp为内置命名空间，无需注册即可使用。
    await xmpMetadata.setValue(`${image.XMP_BASIC.prefix}:title`, image.XMPTagType.STRING, 'My Title');
    console.info('Succeeded in setting XMP tag value.');
  } catch (error) {
    let err: BusinessError = error as BusinessError;
    console.error(`Failed to set XMP tag value! code is ${err.code}, message is ${err.message}`);
  }
}
```

## getTag

getTag(path: string): Promise<XMPTag | null>

从指定路径获取单个XMP标签。使用Promise异步回调。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 目标XMP标签的路径。路径语法参见[XMP路径语法](arkts-apis-image-xmpmetadata.md#xmp路径语法)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[XMPTag](arkts-apis-image-i.md#xmptag) | null> | Promise对象，返回指定路径下的XMP标签。若获取失败，返回空值。 |

**错误码：**

以下错误码的详细介绍请参见[Image错误码](errorcode-image.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7600206 | Invalid argument. Possible causes:  1. Namespace is not registered.  2. The path syntax is invalid. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

async function GetTag() {
  try {
    let xmpMetadata = new image.XMPMetadata();
    await xmpMetadata.setValue(`${image.XMP_BASIC.prefix}:title`, image.XMPTagType.STRING, 'My Title');
    // 获取xmp:title路径的标签。
    let tag: image.XMPTag | null = await xmpMetadata.getTag(`${image.XMP_BASIC.prefix}:title`);
    console.info(`Succeeded in getting an XMP tag. ${image.XMP_BASIC.prefix}:title: ${tag?.value}.`);
  } catch (error) {
    let err: BusinessError = error as BusinessError;
    console.error(`Failed to get an XMP tag. Code: ${err.code}, message: ${err.message}.`);
  }
}
```

## removeTag

removeTag(path: string): Promise<void>

删除指定路径下的XMP标签。使用Promise异步回调。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 目标XMP标签的路径。路径语法参见[XMP路径语法](arkts-apis-image-xmpmetadata.md#xmp路径语法)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[Image错误码](errorcode-image.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7600206 | Invalid argument. Possible causes:  1. Namespace is not registered.  2. The path syntax is invalid. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

async function RemoveTag() {
  try {
    let xmpMetadata = new image.XMPMetadata();
    await xmpMetadata.setValue(`${image.XMP_BASIC.prefix}:title`, image.XMPTagType.STRING, 'My Title');
    await xmpMetadata.removeTag(`${image.XMP_BASIC.prefix}:title`);
    // 再次获取验证是否已移除，如果节点不存在则返回null。
    let tag: image.XMPTag | null = await xmpMetadata.getTag(`${image.XMP_BASIC.prefix}:title`);
    console.info(`Succeeded in removing an XMP tag. ${image.XMP_BASIC.prefix}:title exists after remove: ${tag !== null}.`);
  } catch (error) {
    let err: BusinessError = error as BusinessError;
    console.error(`Failed to remove an XMP tag. Code: ${err.code}, message: ${err.message}.`);
  }
}
```

## enumerateTags

enumerateTags(callback: (path: string, tag: XMPTag) => boolean, rootPath?: string, options?: XMPEnumerateOptions): void

枚举指定路径下的所有XMP标签。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | (path: string, tag: [XMPTag](arkts-apis-image-i.md#xmptag)) => boolean | 是 | 同步回调函数。  返回true，表示继续遍历；返回false，表示停止遍历。  path参数是标签的唯一路径标识，遵循[XMP路径语法](arkts-apis-image-xmpmetadata.md#xmp路径语法)；tag参数是对应标签的数据表示形式。 |
| rootPath | string | 否 | 遍历起始节点。默认从根节点开始，路径语法参见[XMP路径语法](arkts-apis-image-xmpmetadata.md#xmp路径语法)。 |
| options | [XMPEnumerateOptions](arkts-apis-image-i.md#xmpenumerateoptions) | 否 | 遍历选项。  默认行为：仅遍历直接子节点，返回普通节点和限定符。 |

**错误码：**

以下错误码的详细介绍请参见[Image错误码](errorcode-image.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7600206 | Invalid argument. Possible causes:  1. Namespace is not registered.  2. The rootPath syntax is invalid. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

async function EnumerateTags(imageSourceObj: image.ImageSource) {
  // 指定读取XMP类型的元数据。
  let types: image.MetadataType[] = [image.MetadataType.XMP_METADATA];
  await imageSourceObj.readImageMetadataByType(types).then((metaData: image.ImageMetadata) => {
    if (metaData != undefined && metaData.xmpMetadata != undefined) {
      try {
        // 获取所有XMP标签（递归模式、包含普通节点和限定符）。
        metaData.xmpMetadata.enumerateTags((path: string, tag: image.XMPTag): boolean => {
          // 打印标签路径、名称和值。
          console.info(`Succeeded in enumerating an XMP tag. Path: ${path}, name: ${tag.name}, value: ${tag.value}.`);
          return true;  // 返回true继续遍历。
        }, undefined, { isRecursive: true, onlyQualifier: false });
      } catch (error) {
        let err: BusinessError = error as BusinessError;
        console.error(`Failed to enumerate XMP tags. Code: ${err.code}, message: ${err.message}.`);
      }
    }
  }).catch((error: BusinessError) => {
    console.error(`Failed to read image metadata by type. Code: ${error.code}, message: ${error.message}.`);
  })
}
```

## getTags

getTags(rootPath?: string, options?: XMPEnumerateOptions): Promise<Record<string, XMPTag>>

获取指定路径下的XMP标签及其子标签。使用Promise异步回调。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| rootPath | string | 否 | 遍历起始节点。默认从根节点开始，路径语法参见[XMP路径语法](arkts-apis-image-xmpmetadata.md#xmp路径语法)。 |
| options | [XMPEnumerateOptions](arkts-apis-image-i.md#xmpenumerateoptions) | 否 | 遍历选项。  默认行为：仅遍历直接子节点，返回普通节点和限定符。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Record<string, [XMPTag](arkts-apis-image-i.md#xmptag)>> | Promise对象，返回XMP标签集合。 |

**错误码：**

以下错误码的详细介绍请参见[Image错误码](errorcode-image.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7600206 | Invalid argument. Possible causes:  1. Namespace is not registered.  2. The rootPath syntax is invalid. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

async function GetTags(imageSourceObj: image.ImageSource) {
  // 指定读取XMP类型的元数据。
  let types: image.MetadataType[] = [image.MetadataType.XMP_METADATA];
  await imageSourceObj.readImageMetadataByType(types).then(async (metaData: image.ImageMetadata) => {
    if (metaData != undefined && metaData.xmpMetadata != undefined) {
      try {
        // 获取所有XMP标签（递归模式、包含普通节点和限定符）。
        let tags: Record<string, image.XMPTag> =
          await metaData.xmpMetadata.getTags(undefined, { isRecursive: true, onlyQualifier: false });
        console.info(`Succeeded in getting XMP tags. Count: ${Object.keys(tags).length}, data: ${JSON.stringify(tags)}.`);
      } catch (error) {
        let err: BusinessError = error as BusinessError;
        console.error(`Failed to get XMP tags. Code: ${err.code}, message: ${err.message}.`);
      }
    }
  }).catch((error: BusinessError) => {
    console.error(`Failed to read image metadata by type. Code: ${error.code}, message: ${error.message}.`);
  })
}
```

## getBlob

getBlob(): Promise<ArrayBuffer>

以二进制数据的形式获取XMP元数据。使用Promise异步回调。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<ArrayBuffer> | Promise对象，返回XMP元数据的二进制数据。 |

**错误码：**

以下错误码的详细介绍请参见[Image错误码](errorcode-image.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7600301 | Memory alloc failed. |
| 7600302 | Memory copy failed. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

async function GetBlob(imageSourceObj: image.ImageSource) {
  // 指定读取XMP类型的元数据。
  let types: image.MetadataType[] = [image.MetadataType.XMP_METADATA];
  await imageSourceObj.readImageMetadataByType(types).then(async (metaData: image.ImageMetadata) => {
    if (metaData != undefined && metaData.xmpMetadata != undefined) {
      try {
        let blob: ArrayBuffer = await metaData.xmpMetadata.getBlob();
        console.info(`Succeeded in getting an XMP blob. Length: ${blob.byteLength}.`);
      } catch (error) {
        let err: BusinessError = error as BusinessError;
        console.error(`Failed to get an XMP blob. Code: ${err.code}, message: ${err.message}.`);
      }
    }
  }).catch((error: BusinessError) => {
    console.error(`Failed to read image metadata by type. Code: ${error.code}, message: ${error.message}.`);
  })
}
```

## setBlob

setBlob(buffer: ArrayBuffer): Promise<void>

使用二进制数据替换当前XMP元数据。使用Promise异步回调。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| buffer | ArrayBuffer | 是 | 要替换的二进制数据。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[Image错误码](errorcode-image.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7600206 | Invalid argument. Possible causes:  1. The buffer is empty or invalid. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

async function SetBlob(imageSourceObj: image.ImageSource) {
  // 指定读取XMP类型的元数据。
  let types: image.MetadataType[] = [image.MetadataType.XMP_METADATA];
  await imageSourceObj.readImageMetadataByType(types).then(async (metaData: image.ImageMetadata) => {
    if (metaData != undefined && metaData.xmpMetadata != undefined) {
      try {
        let blob: ArrayBuffer = await metaData.xmpMetadata.getBlob();
        // 以原始二进制数据回填，验证setBlob接口可用性。
        await metaData.xmpMetadata.setBlob(blob);
        let newBlob: ArrayBuffer = await metaData.xmpMetadata.getBlob();
        console.info(`Succeeded in setting an XMP blob. New length: ${newBlob.byteLength}.`);
      } catch (error) {
        let err: BusinessError = error as BusinessError;
        console.error(`Failed to set an XMP blob. Code: ${err.code}, message: ${err.message}.`);
      }
    }
  }).catch((error: BusinessError) => {
    console.error(`Failed to read image metadata by type. Code: ${error.code}, message: ${error.message}.`);
  })
}
```
