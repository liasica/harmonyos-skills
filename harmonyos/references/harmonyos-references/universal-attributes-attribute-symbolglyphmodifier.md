---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/universal-attributes-attribute-symbolglyphmodifier
title: 动态SymbolGlyphModifier属性设置
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 通用属性 > 动态属性与自定义 > 动态SymbolGlyphModifier属性设置
category: harmonyos-references
scraped_at: 2026-04-29T13:51:32+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:73ab5d82aea33c591f9a8c1d07d620f8ea706e956fd400ae3bdbc4e6d5218dab
---

SymbolGlyphModifier用于动态设置SymbolGlyph组件的属性和样式，支持使用if/else语句进行设置。[SymbolGlyph](ts-basic-components-symbolglyph.md)是一个用于展示图标符号的组件。

说明

从API version 12开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## SymbolGlyphModifier

PhonePC/2in1TabletTVWearable

定义SymbolGlyphModifier。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### constructor

PhonePC/2in1TabletTVWearable

constructor(src?: Resource)

SymbolGlyphModifier的构造函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src | [Resource](ts-types.md#resource) | 否 | 资源信息。 |

### applyNormalAttribute

PhonePC/2in1TabletTVWearable

applyNormalAttribute?(instance: SymbolGlyphAttribute): void

组件普通状态时的样式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| instance | [SymbolGlyphAttribute](ts-basic-components-symbolglyph.md) | 是 | 动态设置SymbolGlyph组件的属性。 |

## 示例

PhonePC/2in1TabletTVWearable

该示例通过[SymbolGlyphModifier](universal-attributes-attribute-symbolglyphmodifier.md#symbolglyphmodifier)和TextInput组件的[cancelButton](ts-basic-components-textinput.md#cancelbutton18)属性展示了自定义右侧symbol类型清除按钮样式的效果。

```
1. import { SymbolGlyphModifier } from '@kit.ArkUI';

3. // xxx.ets
4. @Entry
5. @Component
6. struct Index {
7. @State text: string = '';
8. symbolModifier: SymbolGlyphModifier =
9. new SymbolGlyphModifier($r('sys.symbol.trash')).fontColor([Color.Red]).fontSize(16).fontWeight(FontWeight.Regular);

11. build() {
12. Column() {
13. TextInput({ text: this.text, placeholder: 'input your word...' })
14. .height(50)
15. .cancelButton({
16. style: CancelButtonStyle.CONSTANT,
17. icon: this.symbolModifier // 从API version 18开始支持symbol类型
18. })
19. }.margin(10)
20. }
21. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9/v3/IJBrbymbRVm_386-Y3F7bQ/zh-cn_image_0000002558606442.png?HW-CC-KV=V1&HW-CC-Date=20260429T055131Z&HW-CC-Expire=86400&HW-CC-Sign=F5CCA782DB9E1505C2D5E1F8849F6DF43C3883A31AC829646240D8F834155214)
