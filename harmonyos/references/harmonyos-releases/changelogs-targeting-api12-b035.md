---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/changelogs-targeting-api12-b035
title: 针对API 12应用的变更
breadcrumb: 版本说明 > 更多版本 > 历史版本 > 5.0.0(12) > OS平台能力 > 接口行为变更说明 > HarmonyOS NEXT Developer Beta3引入的接口行为变更 > 针对API 12应用的变更
category: harmonyos-releases
scraped_at: 2026-09-02T14:58:53+08:00
doc_updated_at: 2026-06-27
content_hash: sha256:bf9a8dc6cf3c1b67af90cf17a2aec2540627c38ea196c1e99f0cf095af943662
---

## ArkTS

### JSON.parse解析非法字符串行为变更

**变更原因**

JSON.parse解析非法字符串未抛JS异常，表现与预期及ECMA规范不一致

**变更影响**

此变更涉及应用适配。

```screen
const strData = `{"k1": "hello", "k2": 3}`;
const strErr = strData.substring(0, strData.length - 2); // `{"k1": "hello", "k2": `
JSON.parse(strErr);
```

变更前：JSON.parse解析非法字符串strErr能够正常解析，未抛出JS异常。

变更后：JSON.parse解析非法字符串strErr抛出JS异常。

**起始API Level**

12

**变更的接口/组件**

JSON.parse/ASON.parse/util.json.parse

**适配指导**

针对JSON.parse解析非法字符串的异常场景，开发者需要保证传入的字符串为合法字符串，或者使用try-catch捕获异常。

### JSON.parse解析浮点数下溢或-0行为变更

**变更原因**

JSON.parse相关接口解析字符串含有浮点数下溢或-0的情况，表现与规范不一致。

**变更影响**

此变更涉及应用适配。

变更前：

JSON.parse('123.456e-789'); 返回 -Infinity，是错误结果。

1/JSON.parse('-0'); 返回 Infinity，是错误结果。

变更后：

JSON.parse('123.456e-789'); 返回 0，是正确结果。

1/JSON.parse('-0'); 返回 -Infinity，是正确结果。

**起始API Level**

12

**变更的接口/组件**

JSON.parse/ASON.parse/util.json.parse

**适配指导**

对于开发者，排查代码中是否存在对JSON.parse相关接口传入下溢的浮点数字符串与-0的情况，如果存在该现象，则排查代码逻辑是否能适配正确的值。

## Sendable及共享模块语法规则编译检查完善

**变更原因**

Sendable对象需要遵循[使用规则](../harmonyos-guides/sendable-constraints.md)，共享模块需要遵循[使用规则](../harmonyos-guides/arkts-sendable-module.md)，在Sendable&共享模块的部分需要约束的export场景中，编译器缺少检查，导致这些场景会发生运行时异常但是没有编译时错误。在本次版本更新中，修复了这些约束的编译时检查，将运行时异常提前到编译时。旨在通过编译时错误或警告，帮助开发者更早发现Sendable&共享模块使用约束，减少运行时定位成本。

**变更影响**

变更前：

1. 当在共享模块中使用export default someVariable方式导出，并且someVariable是Non-sendable类型时，DevEco编辑界面有错误提示，编译没有错误，程序运行时会崩溃。
2. 当在共享模块中使用export type someType = someNonSendableType方式导出Non-sendable类型的别名时，DevEco编辑界面没有提示，编译没有异常。
3. 当sendable class内部使用当前模块top level中export的sendable class对象时，DevEco编辑界面没有提示，编译没有异常，运行时会触发异常。

变更后：

1. 当在共享模块中使用export default someVariable方式导出，并且someVariable是Non-sendable类型时，DevEco编辑界面有错误提示，编译有错误。
2. 当在共享模块中使用export type someType = someNonSendableType方式导出Non-sendable类型的别名时，DevEco编辑界面有警告提示，编译有警告。
3. 当sendable class内部使用当前模块top level中export的sendable class对象时，DevEco编辑界面有警告提示，编译有警告。

具体场景示例：

共享模块export约束

场景一：在共享模块中使用export default someVariable方式导出，并且someVariable是Non-sendable类型时。影响：运行时崩溃变更为编译报错

变更前

```ts
'use shared';
class NonSendableClass {};
export default NonSendableClass; // 引发 GC 时崩溃
```

变更后

```ts
'use shared';
class NonSendableClass {};
export default NonSendableClass; // 编译错误
```

场景二：在共享模块中使用export type someType = someNonSendableType方式导出Non-sendable的别名时。影响：无提示变更为编辑警告、编译警告

变更前

```ts
'use shared';
class NonSendableClass {};
export type NonSendableAlias = NonSendableClass;
```

变更后

```ts
'use shared';
class NonSendableClass {};
export type NonSendableAlias = NonSendableClass; // DevEco编辑界面警告提示 & 编译警告
```

sendable class内部的变量使用约束

场景一：当sendable class内部使用当前模块top level中export的sendable class对象时。影响：运行时异常变更为编辑、编译警告

变更前

```ts
import { taskpool } from '@kit.ArkTS';

@Sendable
export class SendableData {};

@Sendable
class SendableClass {
    handle():void {
      new SendableData(); // 运行时异常
    }
}

@Concurrent
async function taskHandle(sendable: SendableClass) {
  sendable.handle();
}

taskpool.execute(new taskpool.Task(taskHandle, new SendableClass()));
```

变更后

```ts
import { taskpool } from '@kit.ArkTS';

@Sendable
export class SendableData {};

@Sendable
class SendableClass {
    handle():void {
      new SendableData(); // DevEco编辑界面警告提示 & 编译警告
    }
}

@Concurrent
async function taskHandle(sendable: SendableClass) {
  sendable.handle();
}

taskpool.execute(new taskpool.Task(taskHandle, new SendableClass()));
```

**起始API Level**

ArkTS Sendable语法检查从API 12起启用。

**变更的接口/组件**

不涉及。

**适配指导**

对于开发者，建议按照Sendable&共享模块规格修复新增警告，防止出现运行时异常。

## ArkUI

### 命令式渲染节点RenderNode属性clipToFrame行为变更

**变更原因**

原先命令式渲染节点RenderNode的clipToFrame设为false不生效，现设置为false，超出节点大小范围的子节点内容不会被剪裁。

**变更影响**

此变更涉及应用适配。

API 11：RenderNode的clipToFrame设为false不生效，超出节点大小范围的子节点内容会被剪裁。开发者在未显式设置clipToFrame属性的情况下，clipToFrame默认值为false。

API 12及以上版本：RenderNode的clipToFrame设为false时，超出节点大小范围的子节点内容不会被剪裁。为保证变更前后clipToFrame的默认行为一致，开发者在未显式设置clipToFrame属性的情况下，clipToFrame默认值变更为true。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/tpXvcR70QD2LDXgaQQ5VLg/zh-cn_image_0000001971091670.png)

**起始API Level**

11

**变更的接口/组件**

命令式渲染节点RenderNode的clipToFrame接口

**适配指导**

若开发者在设置clipToFrame为false的情况下，仍想保持之前的“超出节点大小范围的内容会被剪裁”的行为，可通过设置clipToFrame为true来实现。

```ts
import {  RenderNode, FrameNode, NodeController } from '@kit.ArkUI';

const renderNode = new RenderNode();
renderNode.frame = { x: 50, y: 50, width: 200, height: 200 };
renderNode.backgroundColor = 0xffd5d5d5;
renderNode.clipToFrame = true;  // 设置clipToFrame为true，对超出节点大小的内容进行剪裁。

const childNode = new RenderNode();
childNode.frame = { x: 10, y: 10, width: 250, height: 100 };
childNode.backgroundColor = 0xff004aaf;
renderNode.appendChild(childNode);

class MyNodeController extends NodeController {
  private rootNode: FrameNode | null = null;

  makeNode(uiContext: UIContext): FrameNode | null {
    this.rootNode = new FrameNode(uiContext);

    const rootRenderNode = this.rootNode.getRenderNode();
    if (rootRenderNode !== null) {
      rootRenderNode.appendChild(renderNode);
    }

    return this.rootNode;
  }
}

@Entry
@Component
struct Index {
  private myNodeController: MyNodeController = new MyNodeController();

  build() {
    Row() {
      NodeContainer(this.myNodeController)
    }
  }
}
```

### 使用局部@Builder方法引用传参时，使用bind(this)后，状态管理的父子关系和组件的父子关系不一致，比如使用@ohos.arkui.advanced.ChipGroup高级组件崩溃解决方法

**变更原因**

开发者使用局部@Builder方法引用传参时，使用bind(this)后，在使用 @Provide和@Consume时状态管理的父子关系和组件的父子关系不一致。运行时报错：

```txt
@Component 'MyComponent2'[11] missing @Provide property with name value.Fail to resolve @Consume(value).
```

**变更影响**

此变更涉及应用适配。开发者使用局部@Builder方法引用传参时，使用bind(this)后，状态管理的父子关系和组件的父子关系不一致，涉及高级组件@ohos.arkui.advanced.ChipGroup在内的使用局部@Builder且使用@Builder函数处使用bind(this)的一些自定义组件。

**起始API Level**

12

**变更的接口/组件**

@ohos.arkui.advanced.ChipGroup (操作块组组件)

**适配指导**

将原来的局部@Builder变成@LocalBuilder。

变更前：

```ts
@Component
struct MyComponent {
  @Provide("value") value: number = 10;
  @BuilderParam content: () => void;

  build() {
    Column() {
      this.content();
    }
  }
}

@Component
struct MyComponent2 {
  @Consume("value") value: number;

  build() {
    Text(`${this.value}`)
  }
}

@Entry
@Component
struct Index {
  @State stateValue: string = '';

  @Builder
  content() {
    MyComponent2()
  }

  build() {
    Column() {
      MyComponent({
        content: this.content.bind(this)
      })
    }
  }
}
```

变更后：

```ts
@Component
struct MyComponent {
  @Provide("value") value: number = 10;
  @BuilderParam content: () => void;

  build() {
    Column() {
      this.content();
    }
  }
}

@Component
struct MyComponent2 {
  @Consume("value") value: number;

  build() {
    Text(`${this.value}`)
  }
}

@Entry
@Component
struct Index {
  @State stateValue: string = '';
// 将 @Builder 改成@LocalBuilder
  @LocalBuilder
  content() {
    MyComponent2()
  }

  build() {
    Column() {
      // 去掉bind(this)
      MyComponent({
        content: this.content
      })
    }
  }
}
```

### RichEditor设置预设样式的接口传入默认值时，文本样式效果变更

**变更原因**

RichEditor设置用户预设样式的接口setTypingStyle，传入默认值undefined/null后，开发者自定义预置样式依然存在，未恢复成不设置时效果。

不设置时，当用户输入文本，输入后的文本样式跟随前一个文本的文本样式。

**变更影响**

此变更涉及应用适配

API 11：

当setTypingStyle设置为默认值时，调用接口setTypingStyle不生效。

其效果为在任何文本后面持续输入的文本会一直保持之前开发者设置的预置样式，不会跟随前一个文本样式。

API 12及以上版本：

当setTypingStyle设置为默认值时，会恢复为不设置时效果。

其效果为在任何文本后面持续输入的文本时，会根据前一个文本样式去更新当前输入文本样式。

**起始API Level**

11

**变更的接口/组件**

setTypingStyle

**适配指导**

开发者需要清除TypingStyle使用组件默认样式时，请参照如下代码。

```ts
@Entry
@Component
struct Index {
  controller: RichEditorController = new RichEditorController()
  options: RichEditorOptions = { controller: this.controller }
  build() {
      Column() {
        RichEditor(this.options)
          .borderWidth(1)
          .borderColor(Color.Green)
          .width("100%")
          .height("50%")
        Button('ResetTypingStyle')
          .fontSize(10)
          .onClick(() => {
            // 清除TypingStyle
            this.controller.setTypingStyle(undefined)
            // this.controller.setTypingStyle(null)
          })
        Button('SetTypingStyle')
          .fontSize(10)
          .onClick(() => {
            // 设置TypingStyle
            this.controller.setTypingStyle({fontColor:"#ff0000"})
          })
    }
  }
}
```

### RichEditor占位文本接口中文本样式属性传入异常值/默认值时，占位文本样式的效果变更

**变更原因**

1. RichEditor设置占位文本的接口placeholder，其占位文本样式属性PlaceHolderStyle为异常值"{}"时，组件未将占位文本样式属性设置为默认效果。
2. 当占位文本样式属性中各个属性为默认值undefined时，对应默认效果未生效。

占位文本样式属性：

* 文本尺寸（默认值 16vp）
* 文本粗细（默认值 400）
* 文本字体（默认值 当前系统字体/注册自定义字体）
* 文本样式（默认值 FontStyle.Normal）
* 文本颜色（默认值：跟随系统主题，一般为黑色）

**变更影响**

此变更涉及应用适配

变更前：占位文本样式属性为异常值或其内部其他属性设为默认值时，调用接口placeholder未生效。

变更后：占位文本样式属性为异常值或其内部其他属性设为默认值时，按组件默认占位文本样式/对应属性默认样式生效。

**起始API Level**

12

**变更的接口/组件**

PlaceHolderStyle

**适配指导**

开发者需要排查调用设置占位文本placeholder中PlaceHolderStyle为异常值或其各个属性为异常值时，是否按照默认效果生效。

以style为"{}"和fontcolor为默认值为例，见如下代码，请开发者自行排查。

```ts
@Entry
@Component
struct Index {
  controller: RichEditorController = new RichEditorController()
  options: RichEditorOptions = { controller: this.controller }
  @State style: PlaceholderStyle = { fontColor: "#ff0000" };

  build() {
    Column() {
      RichEditor(this.options)
        .borderWidth(1)
        .borderColor(Color.Green)
        .width("100%")
        .height("50%")
        .placeholder("hello world", this.style)
      Button('change style to {}')
        .fontSize(10)
        .onClick(() => {
          this.style = {};
        })
      Button('change style.fontColor to undefined')
        .fontSize(10)
        .onClick(() => {
          this.style = { fontColor: undefined };
        })
      Button('change style.fontColor to normal value')
        .fontSize(10)
        .onClick(() => {
          this.style = { fontColor: "#ff0000" };
        })
    }
  }
}
```

### 自定义MenuItem的onChange触发逻辑变更

**变更原因**

基于CustomBuilder创建的MenuItem，无法触发onChange事件。变更后事件触发符合预期。

**变更影响**

此变更涉及应用适配。

API 11及以下版本：基于CustomBuilder创建的MenuItem，无法触发onChange事件。

API 12及以上版本：基于CustomBuilder创建的MenuItem，正常触发onChange事件。

**起始API Level**

9

**变更的接口/组件**

MenuItem组件。

**适配指导**

由于此前基于CustomBuilder创建的MenuItem，设置onChange不生效，变更后请按应用场景正确使用onChange。

### Repeat设置totalCount属性行为变更

**变更原因**

totalCount表示UI显示的数据个数。当0 < totalCount < arr.length时，界面中只渲染“totalCount”个数据。

**变更影响**

此变更涉及应用适配。

变更前：Repeat设置totalCount属性时，如果totalCount小于数据长度，显示的数据个数为数据的长度。

将arr.length设置为10，totalCount设置为5。显示效果如图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/NHDfH2e1QKOIj_B5Iw9Shg/zh-cn_image_0000002007771985.jpeg)

变更后：Repeat设置totalCount属性时，如果totalCount小于数据长度，显示的数据个数为totalCount值。

将arr.length设置为10，totalCount设置为5。显示效果如图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/OWV2ckXPSxO8GVv1Cglfjw/zh-cn_image_0000002007731453.jpeg)

**起始API Level**

12

**变更的接口/组件**

Repeat组件。

**适配指导**

如果开发者想要显示的数据个数为数据长度时，需要将totalCount值设置为数组长度。示例代码如下：

```ts
@Entry
@ComponentV2
struct TestPage {
  @Local simpleList: Array<string> = [];
  private totalCount: number = 50;

  aboutToAppear(): void {
    for (let i = 0; i < 50; i++) {
      this.simpleList.push('Hello ' + i);
    }
  }

  build() {
    Column({ space: 10 }) {
      List() {
        Repeat<string>(this.simpleList)
          .each((obj: RepeatItem<string>) => {
            ListItem() {
              Text('[each] ' + obj.item)
                .fontSize(30)
                .margin({ top: 10 })
            }
          })
          .key((item: string, index: number) => item)
          .virtualScroll({ totalCount: this.totalCount })
          .templateId((item: string, index: number) => "default")
          .template('default', (ri) => {
            Text('[template] ' + ri.item)
              .fontSize(30)
              .margin({ top: 10 })
          }, { cachedCount: 3 })
      }
      .cachedCount(1)
      .border({ width: 1 })
      .height('50%')
    }
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }
}
```

### Refresh组件promptText参数设置为undefined时清空文本内容

**变更原因**

Refresh组件通过promptText参数可传入文本字符串显示在刷新区域，该参数设置为undefined时未清空文本内容，不符合ArkUI通用规范，变更后开发者可设置该参数为undefined清空文本内容。

**变更影响**

此变更涉及应用适配。

变更前，promptText参数设置为undefined时会保持当前值不变，刷新区域显示对应文本内容。

变更后，promptText参数设置为undefined时会清空当前文本内容，刷新区域不显示文本内容。

| 变更前 | 变更后 |
| --- | --- |
|  |  |

**起始API Level**

12

**变更的接口/组件**

Refresh组件promptText参数

**适配指导**

开发者需要判断变更后promptText参数设置undefined时清空文本内容后的效果是否符合预期，如不符合可通过对[Refresh组件](../harmonyos-references-V5/ts-container-refresh-V5.md#refreshoptions对象说明)promptText参数设置期望值以达到预期。

```ts
@Entry
@Component
struct RefreshExample {
  @State isRefreshing: boolean = false
  @State arr: String[] = ['0', '1', '2', '3', '4','5','6','7','8','9','10']
  @State promptText: string|undefined = "Loading..."

  build() {
    Column() {
      Refresh({ refreshing: $$this.isRefreshing ,
        promptText: this.promptText  // 设置刷新区域显示文本内容，设置为undefined时清空文本内容
      }) {
        List() {
          ForEach(this.arr, (item: string) => {
            ListItem() {
              Text('' + item)
                .width('80%').height(100).fontSize(16).margin(10)
                .textAlign(TextAlign.Center).borderRadius(10).backgroundColor(0xFFFFFF)
            }
          }, (item: string) => item)
        }
        .width('100%')
        .height('100%')
        .alignListItem(ListItemAlign.Center)
        .scrollBar(BarState.Off)
      }
      .backgroundColor(0x89CFF0)
      .refreshOffset(96)
    }
  }
}
```

## ArkWeb

### onBeforeUnload接口行为变更

**变更原因**

API version 11及之前，刷新或关闭场景下，在即将离开当前页面时触发onBeforeUnload回调，默认情况下会触发系统弹窗能力，弹窗提示语(回调内参数OnBeforeUnloadEvent对应的message内容)为固定英文"Is it OK to leave/reload this page?"，中文环境出现英文提示信息，影响体验。

**变更影响**

此变更涉及应用适配。

从API version 12开始，onBeforeUnload回调内参数OnBeforeUnloadEvent对应的message内容发生变化，中文环境为"系统可能不会保存您所做的更改。"，且该字串内容支持国际化。

**起始API Level**

8

**变更的接口/组件**

Web#onBeforeUnload(callback: Callback<OnBeforeUnloadEvent, boolean>)中的参数OnBeforeUnloadEvent对应的弹窗中显示的信息message。

**适配指导**

默认行为变更，应注意变更后的行为是否对整体应用显示产生影响。
