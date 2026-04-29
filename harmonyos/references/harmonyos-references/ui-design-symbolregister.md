---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ui-design-symbolregister
title: symbolRegister
breadcrumb: API参考 > 应用框架 > UI Design Kit（UI设计套件） > ArkTS API > symbolRegister
category: harmonyos-references
scraped_at: 2026-04-29T13:57:09+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:549ce47df2ad5c956e0aee1e35d0373bf2ea9dbdd3fe3c2d9240a808a7603414
---

本模块提供自定义Symbol图标资源与动效参数资源注册加载能力。

**起始版本：** 5.1.1(19)

## 导入模块

PhonePC/2in1TabletTV

```
1. import { symbolRegister } from '@kit.UIDesignKit';
```

## symbolRegister.registerSymbol

PhonePC/2in1TabletTV

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

以下错误码的详细介绍请参见[ArkTS API错误码](ui-design-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 801 | Device Type error. |
| 1012600002 | TTF or JSON resource out of size. |
| 1012600003 | TTF or JSON resource content error. |

**示例：**

```
1. import { symbolRegister } from '@kit.UIDesignKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. @Entry
5. @Component
6. struct test {
7. aboutToAppear(): void {
8. try {
9. // 注册自定义的Symbol资源,在resource/rawfile目录下配置图标资源
10. let result =
11. symbolRegister.registerSymbol($rawfile("symbol/symbol_register.ttf"), $rawfile("symbol/symbol_register.json"));
12. } catch (error) {
13. let err = error as BusinessError;
14. console.error("errCode:" + err.code)
15. console.error("error " + err.message);
16. }
17. }

19. build() {
20. Column() {
21. SymbolGlyph($r('app.string.symbol_custom_phone_fill_1'))
22. }
23. }
24. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/mW_dmRwRSXWZ_Q9-02qpwA/zh-cn_image_0000002558607384.png?HW-CC-KV=V1&HW-CC-Date=20260429T055708Z&HW-CC-Expire=86400&HW-CC-Sign=C6311B76D3380693072A656994C8F0B1A7CDF6BB67C97BFEAFBCAB8040300999)
