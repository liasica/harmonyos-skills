---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-menu
title: Menu
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 菜单 > Menu
category: harmonyos-references
scraped_at: 2026-09-02T15:01:06+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:9f5605f1d9c2e0b8bfba43f4e632ae5d7753b422b82b28df01e692260ba3b066
---

以垂直列表形式显示的菜单。Menu组件支持配置菜单项、子菜单、图标、分隔线等内容，可用于展示操作选项、功能入口等场景。

**说明** 

* 该组件从API version 9开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* Menu组件需和[bindMenu](ts-universal-attributes-menu.md#bindmenu)或[bindContextMenu](ts-universal-attributes-menu.md#bindcontextmenu8)方法配合使用，不支持作为普通组件单独使用。

## 子组件

包含[MenuItem](ts-basic-components-menuitem.md)、[MenuItemGroup](ts-basic-components-menuitemgroup.md)子组件。

## 接口

Menu()

作为菜单的固定容器，无参数。

**说明** 

* 菜单和菜单项宽度计算规则：

  + 布局过程中，期望每个菜单项的宽度一致。若子组件设置了宽度，则以[constraintSize](ts-universal-attributes-size.md#constraintsize)为准。
  + Menu不设置宽度的情况：Menu会对子组件MenuItem、MenuItemGroup设置默认2栅格的宽度，若菜单项内容区比2栅格宽，则会自适应撑开。
  + Menu设置宽度的情况：Menu会对子组件MenuItem、MenuItemGroup设置减去padding后的固定宽度。
  + Menu支持设置的最小宽度为64vp。
* Menu不支持的通用属性：[外描边设置](ts-universal-attributes-outline.md)下的属性、[shadow](ts-universal-attributes-image-effect.md#shadow)。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 属性

除支持[通用属性](ts-component-general-attributes.md)外，还支持以下属性：

### font10+

font(value: Font)

统一设置Menu中所有文本的字体样式。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Font](ts-types.md#font) | 是 | Menu中所有文本的字体样式。  默认值：  {  size: '16.0fp',  family: 'HarmonyOS Sans',  weight: FontWeight.Medium,  style: FontStyle.Normal  } |

### fontColor10+

fontColor(value: ResourceColor)

统一设置Menu中所有文本的颜色。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](ts-types.md#resourcecolor) | 是 | Menu中所有文本的颜色。 |

### radius10+

radius(value: Dimension | BorderRadiuses)

设置Menu边框圆角半径。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Dimension](ts-types.md#dimension10) | [BorderRadiuses](ts-types.md#borderradiuses9) | 是 | Menu边框圆角半径。  默认值：2in1设备上默认值为8vp，其他设备上默认值为20vp。  从API version 12开始，当水平方向两个圆角半径之和的最大值大于菜单宽度，或垂直方向两个圆角半径之和的最大值大于菜单高度时，菜单四个圆角均采用菜单默认圆角半径值。  当设置Dimension类型且传参为异常值时，菜单圆角取默认值。  当设置BorderRadiuses类型且传参为异常值时，菜单默认没有圆角。 |

### menuItemDivider12+

menuItemDivider(options: DividerStyleOptions | undefined)

设置MenuItem分割线样式，不设置该属性则不展示分割线。

startMargin + endMargin超过组件宽度后startMargin和endMargin会被置0。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [DividerStyleOptions](ts-types.md#dividerstyleoptions12) | undefined | 是 | 设置MenuItem分割线样式。  -strokeWidth：分割线的线宽，默认值是1px。  -color：分割线的颜色，默认值是#33000000。  -startMargin：分割线与MenuItem侧边起始端的距离，默认为16vp，单位为vp。  -endMargin：分割线与MenuItem侧边结束端的距离，默认为16vp，单位为vp。  -mode：分割线的模式，默认值为FLOATING\_ABOVE\_MENU。  startMargin + endMargin超过组件宽度后startMargin和endMargin会被置0。 |

### menuItemGroupDivider12+

menuItemGroupDivider(options: DividerStyleOptions | undefined)

设置MenuItemGroup顶部和底部分割线的样式，不设置该属性则默认展示分割线。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [DividerStyleOptions](ts-types.md#dividerstyleoptions12) | undefined | 是 | 设置MenuItemGroup顶部和底部分割线样式。  -strokeWidth：分割线的线宽，默认值是1px。  -color：分割线的颜色，默认值是#33000000。  -startMargin：分割线与MenuItemGroup侧边起始端的距离，默认为16vp，单位为vp。  -endMargin：分割线与MenuItemGroup侧边结束端的距离，默认为16vp，单位为vp。  -mode：分割线的模式，默认值为FLOATING\_ABOVE\_MENU。  startMargin + endMargin超过组件宽度后startMargin和endMargin会被置0。 |

### subMenuExpandingMode12+

subMenuExpandingMode(mode: SubMenuExpandingMode)

设置Menu子菜单展开样式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [SubMenuExpandingMode](ts-basic-components-menu.md#submenuexpandingmode12枚举说明) | 是 | Menu子菜单展开样式。  默认值：SubMenuExpandingMode.SIDE\_EXPAND  设置为SIDE\_EXPAND时，[subMenuExpandSymbol](ts-basic-components-menu.md#submenuexpandsymbol20)属性不会显示；设置为EMBEDDED\_EXPAND或STACK\_EXPAND时，subMenuExpandSymbol属性才会生效。 |

### subMenuExpandSymbol20+

subMenuExpandSymbol(symbol: SymbolGlyphModifier)

设置Menu子菜单展开符号。仅在SubMenuExpandingMode.EMBEDDED\_EXPAND或SubMenuExpandingMode.STACK\_EXPAND模式下显示，SubMenuExpandingMode.SIDE\_EXPAND模式下不显示。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| symbol | [SymbolGlyphModifier](ts-universal-attributes-attribute-symbolglyphmodifier.md) | 是 | Menu子菜单展开符号。  1、子菜单的展开样式为SubMenuExpandingMode.SIDE\_EXPAND时，不显示展开符号。  2、子菜单的展开样式为SubMenuExpandingMode.EMBEDDED\_EXPAND时，展开时展开符号会顺时针旋转180°。展开符号默认使用new SymbolGlyphModifier($r('sys.symbol.chevron\_down')).fontSize('24vp')。  3、子菜单的展开样式为SubMenuExpandingMode.STACK\_EXPAND时，展开时展开符号会顺时针旋转90°。展开符号默认使用new SymbolGlyphModifier($r('sys.symbol.chevron\_forward')).fontSize('20vp').padding('2vp')。 |

### fontSize(deprecated)

fontSize(value: Length)

统一设置Menu中所有文本的尺寸。

**说明** 

从API version 9开始支持，从API version 10开始废弃，建议使用[font](ts-basic-components-menu.md#font10)代替。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Length](ts-types.md#length) | 是 | Menu中所有文本的尺寸，Length为number类型时，使用fp单位。不支持设置百分比。 |

## SubMenuExpandingMode12+枚举说明

Menu子菜单展开样式枚举。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SIDE\_EXPAND | 0 | 默认展开样式，子菜单位于同一平面侧边展开。 |
| EMBEDDED\_EXPAND | 1 | 内嵌展开样式，子菜单嵌于主菜单内展开。 |
| STACK\_EXPAND | 2 | 堆叠样式，子菜单浮于主菜单上方展开。 |

## 示例

### 示例1（设置多级菜单）

该示例通过配置MenuItem中的builder参数实现多级菜单。

```ts
@Entry
@Component
struct Index {
  // $r('app.media.xxx')需要替换为开发者所需的图像资源文件。
  private iconStr: ResourceStr = $r('app.media.view_list_filled');
  private iconStr2: ResourceStr = $r('app.media.arrow_right_filled');

  @Builder
  SubMenu() {
    Menu() {
      MenuItem({ content: '复制', labelInfo: 'Ctrl+C' })
      MenuItem({ content: '粘贴', labelInfo: 'Ctrl+V' })
    }
  }

  @Builder
  MyMenu() {
    Menu() {
      MenuItem({ startIcon: $r('app.media.icon'), content: '菜单选项' })
      MenuItem({ startIcon: $r('app.media.icon'), content: '菜单选项' })
        .enabled(false)
      MenuItem({
        startIcon: this.iconStr,
        content: '菜单选项',
        endIcon: this.iconStr2,
        builder: (): void => this.SubMenu()
      })
      MenuItemGroup({ header: '小标题' }) {
        MenuItem({
          startIcon: this.iconStr,
          content: '菜单选项',
          endIcon: this.iconStr2,
          builder: (): void => this.SubMenu()
        })
        MenuItem({
          startIcon: $r('app.media.app_icon'),
          content: '菜单选项',
          endIcon: this.iconStr2,
          builder: (): void => this.SubMenu()
        })
      }
      MenuItem({
        startIcon: this.iconStr,
        content: '菜单选项',
      })
    }
  }

  build() {
    Row() {
      Column() {
        Text('click to show menu')
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
      }
      .bindMenu(this.MyMenu)
      .width('100%')
    }
    .height('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/7pAWfOckSYqBSw4RvSQgOQ/zh-cn_image_0000002706836182.png)

### 示例2（设置symbol类型图标）

该示例通过配置symbolStartIcon、symbolEndIcon实现symbol类型图标的菜单。

```ts
// xxx.ets
import { SymbolGlyphModifier } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State startIconModifier: SymbolGlyphModifier = new SymbolGlyphModifier($r('sys.symbol.ohos_mic')).fontSize('24vp');
  @State endIconModifier: SymbolGlyphModifier = new SymbolGlyphModifier($r('sys.symbol.ohos_trash')).fontSize('24vp');
  @State selectIconModifier: SymbolGlyphModifier =
    new SymbolGlyphModifier($r('sys.symbol.checkmark')).fontSize('24vp');
  @State select: boolean = true;

  @Builder
  SubMenu() {
    Menu() {
      MenuItem({ content: '复制', labelInfo: 'Ctrl+C' })
      MenuItem({ content: '粘贴', labelInfo: 'Ctrl+V' })
    }
  }

  @Builder
  MyMenu() {
    Menu() {
      MenuItem({ symbolStartIcon: this.startIconModifier, content: '菜单选项' })
      MenuItem({ symbolStartIcon: this.startIconModifier, content: '菜单选项' })
        .enabled(false)
      MenuItem({
        symbolStartIcon: this.startIconModifier,
        content: '菜单选项',
        symbolEndIcon: this.endIconModifier,
        builder: (): void => this.SubMenu()
      })
      MenuItemGroup({ header: '小标题' }) {
        MenuItem({
          symbolStartIcon: this.startIconModifier,
          content: '菜单选项',
          symbolEndIcon: this.endIconModifier,
          builder: (): void => this.SubMenu()
        })
        MenuItem({
          symbolStartIcon: this.startIconModifier,
          content: '菜单选项',
          symbolEndIcon: this.endIconModifier,
          builder: (): void => this.SubMenu()
        })
      }
      MenuItem({
        content: '菜单选项',
      }).selected(this.select).selectIcon(this.selectIconModifier)
    }
  }

  build() {
    Row() {
      Column() {
        Text('click to show menu')
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
      }
      .bindMenu(this.MyMenu)
      .width('100%')
    }
    .height('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/H3VBOfe8RDCnwrh-_N1ylw/zh-cn_image_0000002736315287.png)

### 示例3（设置Menu子菜单展开符号）

该示例通过配置subMenuExpandSymbol实现对Menu子菜单展开符号配置颜色和大小。

```ts
import { SymbolGlyphModifier } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State startIconModifier: SymbolGlyphModifier = new SymbolGlyphModifier($r('sys.symbol.ohos_star'))
  @State endIconModifier: SymbolGlyphModifier = new SymbolGlyphModifier($r('sys.symbol.ohos_mic'))
  @State expandSymbolModifier: SymbolGlyphModifier =
    new SymbolGlyphModifier($r('sys.symbol.chevron_down')).fontColor([Color.Red]).fontSize('24vp')

  @Builder
  SubMenu() {
    Menu() {
      MenuItem({
        symbolStartIcon: this.startIconModifier,
        content: '图标'
      })
      MenuItem({
        symbolStartIcon: this.startIconModifier,
        content: '列表'
      })
    }.backgroundColor(Color.Grey)
  }

  @Builder
  MyMenu() {
    Menu() {
      MenuItem({
        symbolStartIcon: this.startIconModifier,
        symbolEndIcon: this.endIconModifier,
        content: '新建文件夹',
        builder: (): void => this.SubMenu(),
      })
      MenuItem({
        symbolStartIcon: this.startIconModifier,
        content: '排序方式',
        builder: (): void => this.SubMenu(),
      })
      MenuItem({
        symbolStartIcon: this.startIconModifier,
        content: '查看方式',
        builder: (): void => this.SubMenu(),
      })
    }
    // 设置子菜单展开样式为嵌入式展开
    .subMenuExpandingMode(SubMenuExpandingMode.EMBEDDED_EXPAND)
    .backgroundColor(Color.Grey)
    // 设置子菜单展开符号
    .subMenuExpandSymbol(this.expandSymbolModifier)
  }

  build() {
    Button('click to show menu')
      .position({ top: 40, left: 40 })
      .bindMenu(this.MyMenu)
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/fdqkiX-oRp6J50ViiwtNjw/zh-cn_image_0000002706676248.gif)

### 示例4（设置分割线样式）

该示例通过设置menuItemDivider和menuItemGroupDivider属性实现分割线样式。

```ts
import { LengthMetrics } from '@kit.ArkUI'

@Entry
@Component
struct Index {

  @Builder
  MyMenu() {
    Menu() {
      MenuItem({ content: 'Item Content' })
      MenuItem({ content: 'Item Content' })
      MenuItem({ content: 'Item Content' })
      MenuItemGroup() {
        MenuItem({ content: 'Group Child' })
        MenuItem({ content: 'Group Child' })
      }
      MenuItem({ content: 'Item Content' })
    }
    // 设置菜单项分割线样式
    .menuItemDivider({
      strokeWidth: LengthMetrics.vp(5),
      color: '#d5d5d5',
      mode: DividerMode.EMBEDDED_IN_MENU
    })
    // 设置菜单项分组分割线样式
    .menuItemGroupDivider({
      strokeWidth: LengthMetrics.vp(5),
      color: '#707070',
      mode: DividerMode.EMBEDDED_IN_MENU
    })
  }

  build() {
    RelativeContainer() {
      Button('show menu')
        .bindMenu(this.MyMenu)
    }
    .height('100%')
    .width('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/L9St8bxxTDyFrkdje6pcRg/zh-cn_image_0000002736435331.png)

### 示例5（设置自定义菜单项的多级菜单）

该示例通过设置subMenuBuilder属性为自定义菜单项添加多级菜单。

从API版本26.0.0开始，新增[subMenuBuilder](ts-basic-components-menuitem.md#submenubuilder)属性。

```ts
import { LengthMetrics } from '@kit.ArkUI';

@Entry
@Component
struct Index {

  @Builder
  SubMenu() {
    Menu() {
      MenuItem({ content: '复制', labelInfo: 'Ctrl+C' })
      MenuItem({ content: '粘贴', labelInfo: 'Ctrl+V' })
    }
  }

  @Builder
  SubMenuContent() {
    Row() {
      // $r('app.media.startIcon')需要替换为开发者所需的图像资源文件。
      Image($r('app.media.startIcon')).width(20).height(20)
      Text('Custom Menu Item').margin({start: LengthMetrics.vp(5)})
    }.padding(20)
  }

  @Builder
  MyMenu() {
    Menu() {
      MenuItem(this.SubMenuContent)
      MenuItem(this.SubMenuContent)
        .enabled(false)
      MenuItem(this.SubMenuContent).subMenuBuilder(this.SubMenu)
    }
  }

  build() {
    Row() {
      Column() {
        Text('click to show menu')
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
      }
      .bindMenu(this.MyMenu)
      .width('100%')
    }
    .height('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/DnQkP2_9RSS82ki9IbpFdQ/zh-cn_image_0000002706836184.jpg)
