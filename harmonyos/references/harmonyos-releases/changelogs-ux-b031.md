---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/changelogs-ux-b031
title: UX样式或效果的变更
breadcrumb: 版本说明 > 更多版本 > 历史版本 > 5.0.0(12) > OS平台能力 > 接口行为变更说明 > HarmonyOS NEXT Developer Beta2引入的接口行为变更 > UX样式或效果的变更
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:27+08:00
doc_updated_at: 2026-06-27
content_hash: sha256:805ee921382a90f6aa06c4e947787345842edd80ad5c50a9096122a5bed92409
---

## TextInput、TextArea 设置TextAlign.Center且显示PlaceHolder文字时，光标位置的变更

**变更原因**

UX规范变更

**变更影响**

变更前：TextAlign.Center，显示PlaceHolder文字时，光标在文字中间，输入文字后光标在末尾

变更后：TextAlign.Center，显示PlaceHolder文字时，光标在文字前面，输入文字后光标在末尾

| 变更前 | 变更后 |
| --- | --- |
|  |  |

**适配指导**

光标显示效果变化，无需适配。

## bindSheet半模态组件横屏支持设置档位与高度

**变更原因**

手机横屏时，bindSheet支持开发者设置档位和高度

**变更影响**

API version 11及以前：bindSheet在手机横屏时不支持设置档位和高度，默认高度距离横屏窗口顶部8vp。

API version 12及以后：bindSheet在手机横屏时支持开发者设置档位和高度，最大高度距离横屏窗口顶部8vp。

**适配指导**

默认效果变更，需应用适配。横竖屏设置档位规则保持一致，参考detents属性的设置请查阅[半模态组件](../harmonyos-references-V5/ts-universal-attributes-sheet-transition-V5.md)文档进行适配。

## bindSheet支持嵌套滚动

**变更原因**

为满足应用诉求，半模态面板嵌套滚动组件，且在滚动组件上设置嵌套模式时，需要实现联动效果。

**变更影响**

此变更涉及应用适配。

单档位模式下半模态仅可设置一档高度。多档位模式下半模态可以设置三档高度，内容位于半模态面板顶部时，通过上下滑动可以自由切换档位。

API version 12之前，半模态面板嵌套滚动组件，且在滚动组件上设置嵌套模式时，无法实现联动。内容位于顶部，多档位时上下滑动无法切换档位，单档位时下滑无法关闭半模态。

API version 12及以后，半模态面板嵌套滚动组件，且在滚动组件上设置嵌套模式时，可以实现联动。内容位于顶部，多档位时上下滑动可以切换档位；单档位时下滑可以关闭半模态。

在滚动组件上设置嵌套的情况下：

| 多档位变更前 | 多档位变更后 |
| --- | --- |
| 无法通过上下滑动切换档位，在最低档下滑无法关闭半模态 | 可以通过上下滑动切换档位，在最低档下滑可以关闭半模态 |

| 单档位变更前 | 单档位变更后 |
| --- | --- |
| 无法通过下滑关闭半模态 | 可以通过下滑关闭半模态 |

**变更的接口/组件**

bindSheet组件

**适配指导**

需要开发者适配。例如，在半模态面板中嵌套List组件场景，@Builder内容可以参考如下示例。

```ts
private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
@Builder
myBuilder() {
  Column() {
    List({ space: 20, initialIndex: 0 }) {
        ForEach(this.arr, (item: number) => {
          ListItem() {
            Text('' + item)
              .width('100%')
              .height(100)
              .fontSize(16)
              .textAlign(TextAlign.Center)
              .borderRadius(10)
              .backgroundColor(0xFFFFFF)
          }
        }, (item: string) => item)
      }
      .listDirection(Axis.Vertical) // 排列方向
      .edgeEffect(EdgeEffect.None)
      .nestedScroll({
        scrollForward: NestedScrollMode.PARENT_FIRST,
        scrollBackward: NestedScrollMode.SELF_FIRST
      }) // 嵌套模式
      .backgroundColor(Color.Gray)
      .width('90%')
      .height('100%')
  }
}
```

## ListItem横滑跟手比变更

**变更原因**

ListItem横滑动态跟手比计算公式，需要与其他场景（例如：List拖动过界）的公式一致。

**变更影响**

此变更涉及应用适配。

ListItem横滑动态跟手比按新实现后，手指滑动相同距离，组件滑动距离会变大。

**适配指导**

默认效果变更，无需适配。

## DrawableDescriptor显示效果

**访问级别**

公开接口

**变更原因**

对原来非标准288x288图标的裁切行为做统一变更，提高用户体验。

**变更影响**

对于非288x288尺寸前景图片，当前生成的分层图标按照缩放后裁剪显示，288x288尺寸前景图片保持原规格。

**适配指导**

默认效果变更，无需适配，但应注意变更后的默认效果是否符合开发者预期，如不符合则应自定义修改效果控制变量以达到预期。

## TimePickerDialog、DatePickerDialog支持设置前导零

**变更原因**

修改时间日期选择器的样式规范，给TimePickerDialog、DatePickerDialog设置是否需要前导零。

**变更影响**

此变更涉及应用适配，只影响TimePickerDialog、DatePickerDialog组件的默认样式。

* 变更前： TimePickerDialog、DatePickerDialog组件12小时制小时默认有前置零。
* 变更后： TimePickerDialog、DatePickerDialog组件12小时制小时默认没有前置零。

  如下图所示为变更前后效果对比：

| 变更前 | 变更后 |
| --- | --- |
|  |  |

| 变更前 | 变更后 |
| --- | --- |
|  |  |

**适配指导**

默认行为变更，应注意时间窗口是否按照设置显示前导零。

## AlphabetIndexer组件popupPosition属性设置为undefined时重置为默认值

**变更原因**

popupPosition属性设置为undefined时应该重置为默认值，但当前实际上会保持现有状态不发生变化，导致开发者不能重置该属性，变更后开发者可通过对该属性设置undefined重置该属性。

**变更影响**

此变更涉及应用适配。

API version 12之前，popupPosition属性设置为undefined时会保持现有状态，提示弹窗位置不发生变化。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/juWoq5u5RLiekdtrlSV7Aw/zh-cn_image_0000001987151785.png)

API version 12及以后，popupPosition属性设置为undefined时会重置为默认值，提示弹窗位置会发生变化。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/Ac5-mFFzQSqmp-R2eM6MmQ/zh-cn_image_0000001953232366.png)

**变更的接口/组件**

AlphabetIndexer组件

**适配指导**

开发者需要判断变更后popupPosition属性设置undefined时重置为默认值的效果是否符合预期，如不符合可通过改变[AlphabetIndexer组件](../harmonyos-references-V5/ts-container-alphabet-indexer-V5.md)popupPosition属性传入参数以达到预期。

## bindContentCover动效参数变更

**变更原因**

为满足应用述求和UX规格，全模态动效参数改为与半模态一致。

**变更影响**

变更前，全模态动效参数为interpolatingSpring(velocity:n, mass:1, stiffness:100, damping:20)，动效时长约为1200ms。

变更后，全模态动效参数为interpolatingSpring(velocity:n, mass:1, stiffness:328, damping:36)，动效时长约为800ms。

**变更的接口/组件**

bindContentCover组件

**适配指导**

默认行为变更，应注意变更后的默认效果是否符合开发者预期，如不符合则自定义修改效果控制变量以达到预期，可通过transition接口自定义动效。

## RichEditor长按交互调整

**变更原因**

为满足应用述求和UX规格，RichEditor组件长按交互效果需要进行调整。

**变更影响**

变更前，长按文本内容，直接触发选词，展示选中背板、手柄以及文本选择菜单。

变更后，长按文本内容不松手，触发选词并展示选中背板，继续拖动变更选中区域，松手后展示手柄及文本选择菜单。如果不继续拖动，则松手时直接展示手柄和文本选择菜单。

| 变更前 | 变更后 |
| --- | --- |
|  |  |

**变更的接口/组件**

RichEditor组件

**适配指导**

默认行为变更，应注意变更后的默认效果是否符合开发者预期，如不符合则自定义修改事件效果以达到预期。

## 滚动类组件（List、Grid、WaterFlow、Scroll）Friction接口默认值变更

**变更原因**

为了优化功耗，将滚动类组件（List、Grid、WaterFlow、Scroll）friction接口默认值改为0.75。

**变更影响**

此变更涉及应用适配。

变更前，滚动类组件（List、Grid、WaterFlow、Scroll）的friction接口默认值为0.7。

变更后，滚动类组件（List、Grid、WaterFlow、Scroll）的friction接口默认值为0.75。相较变更之前，用同样力度抛滑，抛滑时间更短、抛滑距离更近。

**变更的接口/组件**

滚动类组件（List、Grid、WaterFlow、Scroll）的friction接口。

**适配指导**

开发者如果需要使用变更之前的抛滑效果，可以将friction接口的参数设置为0.7。

```ts
@Entry
@Component
struct FrictionExample {
  build() {
    List() {
      ForEach([1, 2, 3, 4, 5], (item: number) => {
        ListItem() {
          Text('' + item)
            .width('100%').height(200).fontSize(16)
            .textAlign(TextAlign.Center).borderRadius(10).backgroundColor(0xFFFFFF)
        }
      }, (item: string) => item)
    }
    .height(500)
    .friction(0.7)
  }
}
```

## ListItem卡片样式行为变更

**变更原因**

原本ListItem在LazyForEach下使用时，ListItem设置卡片样式不生效，需要调整为可以生效。

**变更影响**

此变更涉及应用适配。

变更前：ListItem在LazyForEach下使用时，卡片样式设置不生效。

变更后：ListItem在LazyForEach下使用时，卡片样式设置可以生效。

```ts
// Basic implementation of IDataSource to handle data listener
abstract class BasicDataSource<T> implements IDataSource {
  private listeners: DataChangeListener[] = []

  public totalCount(): number {
    return 0
  }
  abstract getData(index: number): T;

  registerDataChangeListener(listener: DataChangeListener): void {
    if (this.listeners.indexOf(listener) < 0) {
      this.listeners.push(listener)
    }
  }
  unregisterDataChangeListener(listener: DataChangeListener): void {
   const pos = this.listeners.indexOf(listener);
   if (pos >= 0) {
     this.listeners.splice(pos, 1)
   }
  }

  notifyDataReload(): void {
    this.listeners.forEach(listener => {
      listener.onDataReloaded()
    })
  }
  notifyDataAdd(index: number): void {
    this.listeners.forEach(listener => {
      listener.onDataAdd(index)
    })
  }
  notifyDataChange(index: number): void {
    this.listeners.forEach(listener => {
      listener.onDataChange(index)
    })
  }
  notifyDataDelete(index: number): void {
    this.listeners.forEach(listener => {
      listener.onDataDelete(index)
    })
  }
  notifyDataMove(from: number, to: number): void {
    this.listeners.forEach(listener => {
      listener.onDataMove(from, to)
    })
  }
}

class MyDataSource<T> extends BasicDataSource<T> {
  public dataArray: T[] = [];

  public totalCount(): number {
    return this.dataArray.length
  }
  public getData(index: number): T {
    return this.dataArray[index]
  }

  public addData(index: number, data: T): void {
    this.dataArray.splice(index, 0, data)
    this.notifyDataAdd(index)
  }
  public popFirstData(): void {
    this.dataArray.shift()
    this.notifyDataDelete(0)
  }
  public pushData(data: T): void {
    this.dataArray.push(data)
    this.notifyDataAdd(this.dataArray.length - 1)
  }
  public popData(): void {
    this.dataArray.pop()
    this.notifyDataDelete(this.dataArray.length)
  }
}

@Entry
@Component
struct Index {
  arr:MyDataSource<number> = new MyDataSource<number>();
  aboutToAppear(): void {
    for (let i = 0; i < 10; i++) {
      this.arr.pushData(i)
    }
  }

  build() {
    List() {
      ListItemGroup({ style: ListItemGroupStyle.CARD }) {
        LazyForEach(this.arr, (item: number) => {
          ListItem({ style: ListItemStyle.CARD }) {
            Text("item" + item.toString())
          }
        })
      }
    }.backgroundColor("#DCDCDC")
    .height("100%")
  }
}
```

| 变更前效果 | 变更后效果 |
| --- | --- |
|  |  |

**变更的接口/组件**

涉及的组件：ListItem组件ListItemStyle接口。

**适配指导**

如果ListItem在LazyForEach下使用，设置了卡片样式没有生效，变更后生效卡片样式导致显示界面变化，可以删除卡片样式的设置。

如下代码变更前设置卡片样式不生效，变更后生效卡片样式导致显示界面变化。

```ts
build() {
  List() {
    ListItemGroup({ style: ListItemGroupStyle.CARD }) {
      LazyForEach(this.arr, (item: number) => {
        ListItem({ style: ListItemStyle.CARD }) {
          Text("item" + item.toString())
            .height(64)
        }
      })
    }
  }.backgroundColor("#DCDCDC")
  .height("100%")
}
```

删除ListItem卡片样式可以恢复变更前效果。

```ts
build() {
  List() {
    ListItemGroup({ style: ListItemGroupStyle.CARD }) {
      LazyForEach(this.arr, (item: number) => {
        ListItem() {
          Text("item" + item.toString())
            .height(64)
        }
      })
    }
  }.backgroundColor("#DCDCDC")
  .height("100%")
}
```

## List的constraintSize设置生效

**变更原因**

List的布局行为和当前通用的布局约束优先的规格不一致。

**变更影响**

此变更涉及应用适配。

变更前，List不设置Height时，constraintSize的minHeight设置不生效。

变更后，List不设置Height时，constraintSize的minHeight设置会生效。

```ts
@Entry
@Component
struct ListExample {
  build() {
    List({ space: 5 }) {
      ForEach([1, 2, 3, 4, 5], (item: number) => {
        ListItem() {
          Text('' + item)
            .width('100%').height(50)
            .textAlign(TextAlign.Center).backgroundColor(0xFFFFFF)
        }
      }, (item: string) => item)
    }
    .padding(5)
    .constraintSize({ minHeight: 500 })
    .backgroundColor(0xDCDCDC)
  }
}
```

如下是以上示例代码变更前后效果对比：

| 变更前 | 变更后 |
| --- | --- |
|  |  |

**变更的接口/组件**

List组件的constraintSize接口。

**适配指导**

如果List没有设置height属性，且设置了constraintSize的minHeight属性。变更后minHeight属性生效，导致布局界面变化，如果需要保持之前的布局界面，可以删除constraintSize的minHeight属性。

如下代码，变更前constraintSize的minHeight属性不生效，变更后constraintSize的minHeight属性生效导致显示界面变化。

```ts
@Entry
@Component
struct ListExample {
  build() {
    List({ space: 5 }) {
      ForEach([1, 2, 3, 4, 5], (item: number) => {
        ListItem() {
          Text('' + item)
            .width('100%').height(50)
            .textAlign(TextAlign.Center).backgroundColor(0xFFFFFF)
        }
      }, (item: string) => item)
    }
    .padding(5)
    .constraintSize({ minHeight: 500, maxHeight: 1000 })
    .backgroundColor(0xDCDCDC)
  }
}
```

删除constraintSize接口minHeight设置可以恢复之前的效果。

```ts
@Entry
@Component
struct ListExample {
  build() {
    List({ space: 5 }) {
      ForEach([1, 2, 3, 4, 5], (item: number) => {
        ListItem() {
          Text('' + item)
            .width('100%').height(50)
            .textAlign(TextAlign.Center).backgroundColor(0xFFFFFF)
        }
      }, (item: string) => item)
    }
    .padding(5)
    .constraintSize({ maxHeight: 1000 })
    .backgroundColor(0xDCDCDC)
  }
}
```

## AlphabetIndexer组件autoCollapse属性默认值由false改为true

**变更原因**

自适应折叠模式使用场景更广，显示效果更加灵活，默认开启自适应折叠模式更符合开发者期望。

**变更影响**

此变更涉及应用适配。

API version 12之前：autoCollapse属性默认值为false，当AlphabetIndexer组件高度不足时，不会折叠显示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/6Vbv00EVSP28X3MxJxVPNQ/zh-cn_image_0000001987311653.png)

API version 12及之后：autoCollapse属性默认值为true，当AlphabetIndexer组件高度不足时，会折叠显示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/aKmsVfhFSvugDiePNP22sQ/zh-cn_image_0000001987151797.png)

**变更的接口/组件**

AlphabetIndexer组件

**适配指导**

默认行为变更，默认开启自适应折叠模式，若要关闭自适应折叠模式，可通过设置[autoCollapse](../harmonyos-references-V5/ts-container-alphabet-indexer-V5.md#autocollapse11)属性进行适配。

## 光标默认样式变更

**变更原因**

默认UX样式变更。

**变更影响**

此变更涉及应用适配。

变更前：光标小圆圈默认直径为20vp。

变更后：光标小圆圈默认直径为16vp。

变更前后对比效果，如下表所示

| 变更前 | 变更后 |
| --- | --- |
|  |  |

**变更的接口/组件**

涉及光标的组件：TextInput、TextArea、Search、RichEditor。

**适配指导**

默认UX样式变更，无需适配。

## 高级组件SelectionMenu默认样式变更

**变更原因**

默认UX样式变更。

**变更影响**

此变更涉及应用适配。

变更前：自定义文本选择菜单点击“更多”后展开菜单会显示内置的置灰项分享翻译搜索。

变更后：自定义文本选择菜单点击“更多”后展开菜单去除内置的置灰项分享翻译搜索。

变更前后对比效果，如下表所示：

| 变更前 | 变更后 |
| --- | --- |
|  |  |

**变更的接口/组件**

高级组件SelectionMenu。

**适配指导**

默认UX样式变更，无需适配。

## SVG根节点视窗外图片内容裁剪

**访问级别**

公开接口

**变更原因**

修正视觉效果以符合SVG标准。

**变更影响**

此变更涉及应用适配。

```xml
<svg width="100" height="100" viewBox="0 0 300 300" version="1.1">
    <defs>
        <circle id = "circleId" cx="100" cy="50" r="40"  fill="red"/>
    </defs>
    <polygon points="220,100 300,210 170,250 123,234" style="fill:#cccccc;stroke:#000000;stroke-width:1"/>
    <use href="#circleId" x = "300" y= "150" width="50" height="50"/>
</svg>
```

| 变更前 | 变更后 |
| --- | --- |
| 绘制内容超出根节点视窗区域会显示 | 绘制内容超出根节点视窗区域不显示 |
|  |  |

**变更的接口/组件**

涉及的组件：Image、ImageSpan、Canvas。

**适配指导**

默认效果变更，无需适配，但应注意变更后的行为是否对整体应用显示效果产生影响。

## Symbol系统资源变更

**变更原因**

默认UX样式变更。

**变更影响**

此变更涉及应用适配。

```screen
@Extend(SymbolSpan) function style() {
  .fontWeight(FontWeight.Lighter)
  .fontSize(96)
}
@Entry
@Component
struct Index {
  build() {
    Column() {
      Text() {
        SymbolSpan($r('sys.symbol.ohos_wifi')).style()
        SymbolSpan($r('sys.symbol.ohos_trash')).style()
        SymbolSpan($r('sys.symbol.ohos_trash_circle')).style()
        SymbolSpan($r('sys.symbol.ohos_photo')).style()
        SymbolSpan($r('sys.symbol.ohos_folder_badge_plus')).style()
        SymbolSpan($r('sys.symbol.ohos_lungs')).style()
        SymbolSpan($r('sys.symbol.ohos_mic')).style()
        SymbolSpan($r('sys.symbol.ohos_circle')).style()

        SymbolSpan($r('sys.symbol.ohos_lock')).style()
        SymbolSpan($r('sys.symbol.ohos_star')).style()
        SymbolSpan($r('sys.symbol.ohos_arrow_up')).style()
      }
    }.width('100%')
  }
}
```

下表例举资源变更前后对比效果：

| 变更前 | 变更后 |
| --- | --- |
|  |  |

**变更的接口/组件**

涉及Symbol资源的组件：SymbolSpan、SymbolGlyph。

**适配指导**

默认UX样式变更，无需适配。

## 安全控件的背景板变更

**变更原因**

安全控件可设置背景板的属性为不可见或透明，应用可利用此配置将安全控件对用户隐藏，若用户在不知情的情况下触发点击授权，应用就会获取用户的位置、剪切板等敏感信息。

**变更影响**

此变更涉及应用适配。

变更前:

1. 安全控件按钮在构造函数中不设置背景板时，安全控件不展示背景板。
2. 安全控件按钮背景色高八位的α值低于0x1A（例如0x1800ff00）时,安全控件的背景板透明度显示和开发者的设置值一致。

变更后:

1. 安全控件按钮在构造函数中不设置背景板时，安全控件默认展示背景板。
2. 安全控件按钮背景色高八位的α值低于0x1A（例如0x1800ff00）时,安全控件按钮背景色高八位的α值会被系统强制调整为0xff。

**变更的接口/组件**

@internal/component/ets/location\_button.d.ts中 LocationButton接口。

@internal/component/ets/save\_button.d.ts中 SaveButton接口。

@internal/component/ets/paste\_button.d.ts中 PasteButton接口。

**适配指导**

接口使用的示例代码可参考:

[LocationButton接口指导](../harmonyos-references-V5/ts-security-components-locationbutton-V5.md#接口)

[SaveButton接口指导](../harmonyos-references-V5/ts-security-components-savebutton-V5.md#接口)

[PasteButton接口指导](../harmonyos-references-V5/ts-security-components-pastebutton-V5.md#接口)
