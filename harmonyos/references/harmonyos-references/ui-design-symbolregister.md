---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ui-design-symbolregister
title: symbolRegister (symbol注册)
breadcrumb: API参考 > 应用框架 > UI Design Kit（UI设计套件） > ArkTS API > symbolRegister (symbol注册)
category: harmonyos-references
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:817af0b9b9deb7eda43dffde5d21dd8cee68885b1c84b5ab2140c67e29fd5a5c
---

本模块提供自定义Symbol图标资源与动效参数资源注册加载能力。

**起始版本：** 5.1.1(19)

## 导入模块

```typescript
import { symbolRegister } from '@kit.UIDesignKit';
```

## symbolRegister.registerSymbol

registerSymbol(ttfSrc: resourceManager.Resource, jsonSrc: resourceManager.Resource): boolean

注册自定义Symbol资源。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.Core

**起始版本：** 5.1.1(19)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| ttfSrc | [resourceManager.Resource](ts-types.md#resource) | 是 | 自定义Symbol图标资源。 |
| jsonSrc | [resourceManager.Resource](ts-types.md#resource) | 是 | 自定义Symbol动效参数资源。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回注册结果，true：注册成功，false：注册失败。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](errorcode-ui-design.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 801 | Device Type error. |
| 1012600002 | TTF or JSON resource out of size. |
| 1012600003 | TTF or JSON resource content error. |

**示例：**

```typescript
import { symbolRegister } from '@kit.UIDesignKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct test {
  aboutToAppear(): void {
    try {
      // 注册自定义的Symbol资源，在resource/rawfile目录下配置图标资源
      let result =
        symbolRegister.registerSymbol($rawfile("symbol/symbol_register.ttf"), $rawfile("symbol/symbol_register.json"));
    } catch (error) {
      let err = error as BusinessError;
      console.error("errCode:" + err.code)
      console.error("error " + err.message);
    }
  }

  build() {
    Column() {
      SymbolGlyph($r('app.string.symbol_custom_phone_fill_1'))
    }
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/IG3RlcTES5a5jgBQce8XLQ/zh-cn_image_0000002786362078.png?HW-CC-KV=V1&HW-CC-Date=20261112T233241Z&HW-CC-Expire=31536000000&HW-CC-Sign=687CB08B54D4ACF07F12E9DD229A0011091537C2EF1EAB8DFDA7635A16951F77)
