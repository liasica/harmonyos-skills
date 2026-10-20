---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/arkui-uimana-faq-0008
title: Text组件常见问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 常见问题 > Text组件常见问题
category: harmonyos-faqs
scraped_at: 2026-10-21T07:11:10+08:00
doc_updated_at: 2026-10-20
content_hash: sha256:c32c5a36ca252a81a363e92211a52030fe291fb8287f31365e456d446ec0154c
---

**Q：HarmonyOS中的Text控件无法手动设置isSelected参数，导致无法判断文字是否被选中。如何实现文字多选框效果？**

**A**：

* 方案一：动态变量控制样式：

  具体操作步骤如下：

  1. 新建布尔类型状态控制变量isSelect，用true和false控制该Text组件是否被点击；
  2. 给Text组件添加onClick方法，点击后更改Text组件样式并生成具体业务逻辑。

  详细代码示例如下：

  ```ts
  @Entry
  @Component
  struct Selected {
    @State isSelect1: boolean = false; // 选框1选中状态变量
    @State isSelect2: boolean = false; // 选框2选中状态变量

    build() {
      Row({ space: 10 }) {
        Text('选框1')
          .width(80) // 宽度
          .height(50) // 高度
          .textAlign(TextAlign.Center) // 字体居中
          .fontColor(this.isSelect1 ? '#000000' : '#ff0a59f7') // 字体颜色
          .backgroundColor(this.isSelect1 ? '#bbbbbb' : '#ffb2c9f8') // 背景颜色
          .border({ width: 2, color: this.isSelect1 ? Color.Transparent : '#ff0a59f7' }) // 边框
          .borderRadius(5) // 圆角设置
          .fontWeight(FontWeight.Bold) // 字体加粗
          .onClick(() => { // 点击改变选中状态
            this.isSelect1 = !this.isSelect1;
          });

        Text('选框2')
          .width(80) // 宽度
          .height(50) // 高度
          .textAlign(TextAlign.Center) // 字体居中
          .fontColor(this.isSelect2 ? '#000000' : '#ff0a59f7') // 字体颜色
          .backgroundColor(this.isSelect2 ? '#bbbbbb' : '#ffb2c9f8') // 背景颜色
          .border({ width: 2, color: this.isSelect2 ? Color.Transparent : '#ff0a59f7' }) // 边框
          .borderRadius(5) // 圆角设置
          .fontWeight(FontWeight.Bold) // 字体加粗
          .onClick(() => { // 点击改变选中状态
            this.isSelect2 = !this.isSelect2;
          });
      }
      .width('100%')
      .height('100%')
      .justifyContent(FlexAlign.Center)
      .margin({ top: -100 });

    }
  }
  ```

  实现效果如图：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/eUpEhQ4zR0Oe-40ayuKehw/zh-cn_image_0000002795467159.png "点击放大")
* 方案二：attributeModifier动态属性设置多态样式：

  具体操作步骤如下：

  1. 通过创建继承动态属性attributeModifier的类，设置Text组件的多态样式属性。
  2. 以@ObservedV2与@Trace装饰器装饰类和属性，以观测动态属性值的变化并刷新UI。
  3. Text组件通过点击事件，改变动态属性值，以修改Text组件的样式属性。

  详细代码示例如下：

  ```ts
  import { LengthUnit } from '@kit.ArkUI';

  // 创建动态属性类，并以@ObservedV2与@Trace装饰器装饰
  @ObservedV2
  class TextCustomStyle implements AttributeModifier<TextAttribute> {
    // 动态属性值
    @Trace public isSelected: boolean = false;

    // 设置组件样式
    applyNormalAttribute(instance: TextAttribute): void {
      // 根据动态属性值的不同，设置Text组件的不同样式属性
      if (this.isSelected) {
        instance.fontColor(Color.Blue);
        instance.backgroundColor('#00bfff');
        instance.border({
          width: 0.5,
          color: Color.Blue,
          radius: 18
        });
      } else {
        instance.fontColor(Color.Black);
        instance.backgroundColor(Color.Gray);
        instance.border({
          radius: 18
        });
      }
    }
  }

  @Entry
  @Component
  struct TextMultiSelect {
    arr: string[] = ['Sports', 'Games', 'Programming'];
    @State textStyles: TextCustomStyle[] = [];
    @State selectedItem: string[] = [];

    aboutToAppear(): void {
      // 每个Text组件分别绑定属性类
      for (let i = 0; i < this.arr.length; i++) {
        this.textStyles.push(new TextCustomStyle());
      }
    }

    build() {
      Column() {
        Flex({
          direction: FlexDirection.Row,
          justifyContent: FlexAlign.Center,
          space: {
            main: { value: 5, unit: LengthUnit.VP },
            cross: { value: 10, unit: LengthUnit.VP }
          }
        }) {
          ForEach(this.arr, (item: string, index: number) => {
            Text(item)
              .height(50)
              .fontSize('18fp')
              .padding(5)
              // 设置动态属性
              .attributeModifier(this.textStyles[index])
              .onClick(() => {
                // 改变属性类的属性值
                this.textStyles[index].isSelected = !this.textStyles[index].isSelected;
                if (this.textStyles[index].isSelected) {
                  // 保存选项
                  this.selectedItem.push(item);
                } else {
                  // 删除选项
                  let idx = this.selectedItem.indexOf(item);
                  let arrFront = this.selectedItem.slice(0, idx);
                  let arrBack = this.selectedItem.slice(idx + 1);
                  this.selectedItem = arrFront.concat(arrBack);
                }
              });
          });
        }
        .height('auto')
        .width('100%');

        // 选项展示，无选项时显示None
        Text('Selected Item: ' + (this.selectedItem.length === 0 ? 'None' : this.selectedItem.join(', ')));
      }
      .justifyContent(FlexAlign.SpaceEvenly)
      .height('50%')
      .width('100%');
    }
  }
  ```

  实现效果如图：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/XhMywNwnSDO2H31zXash9A/zh-cn_image_0000002766068602.png "点击放大")
* 方案三：其他多选框实现：
  + 若要实现更标准的切换选框，推荐使用[Toggle组件](../harmonyos-guides/arkts-common-components-switch.md)：Toggle组件提供状态按钮样式、勾选框样式和开关样式，一般用于两种状态之间的切换。
  + 若要实现更标准的多选框，推荐使用[Checkbox组件](../harmonyos-references/ts-basic-components-checkbox.md)：Checkbox提供多选框组件，通常用于某选项的打开或关闭。

**Q：html字符串中包含em标签，使用Text组件如何加强对于文本的渲染？**

**A**：具体步骤如下：

1. 创建方法heightLightWord，使用正则表达式对html字符串进行解析，返回包含content和light字段的数组。
2. 使用ForEach遍历数组，根据light字段设置文本的渲染样式。

示例代码如下：

```ts
interface isHeightLight {
  content: string,
  light: boolean
}

@Entry
@Component
struct IndexOfPage {
  value: string = '<em>第</em>二届海南<em>岛</em>国际<em>电</em>影节开幕式';

  heightLightWord(word: string) {
    // 先将需要高亮的字符筛选出来，待会高亮
    let str = word;
    let result: string[] = [];
    let index = 0;
    while ((index = str.indexOf("<em>", index)) !== -1) {
      if (index + 4 < str.length) {
        result.push(str[index + 4]);
      }
      index += 4;
    }
    // 将字符之间的html格式全部去除
    let rt: string = this.value.replace('<p></p><p></p>', '\n').replace('<p>', '\n').replace('\n\n', '\n');
    rt = rt.replace(/<br\s*\/?>/g, '\n');
    rt = rt.replace(/<\/?p/gi, '\n');
    rt = rt.replace(/<[^>]+>/g,
      '');
    // 取'>'反的集合[^>]，+匹配集合元素一次或多次
    rt = rt.replace(/>/g, '');
    if (this.value) {
      rt = rt.trim();
    }
    const wordArr = rt.split('');
    const indexArr: number[] = [];
    // 获取所有符合条件的下标
    result.forEach((item: string) => {
      let index = wordArr.indexOf(item);
      while (index !== -1) {
        indexArr.push(index);
        index = wordArr.indexOf(item, index + 1);
      }
    });
    return wordArr.map((item: string, index: number): isHeightLight => {
      if (indexArr.indexOf(index) !== -1) {
        return { content: item, light: true };
      } else {
        return { content: item, light: false };
      }
    });
  }

  build() {
    Column() {
      Text() {
        ForEach(this.heightLightWord(this.value), (item: isHeightLight) => {
          Span(item.content)
            .fontColor(item.light ? Color.Blue : Color.Black)
            .fontWeight(item.light ? FontWeight.Bolder : FontWeight.Normal)
            .fontSize(item.light ? 20 : 14)
        })
      }
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }
}
```

效果图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/sQlI4cdOTmm7204w1LcLng/zh-cn_image_0000002795307391.png "点击放大")

**Q：父容器的宽高固定，而Text文本内容长度不确定，当文本过长时，会超出父容器的高度。问题代码如下：**

```ts
@Entry
@Component
struct Index {
  build() {
    Column() {
      Text('11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111' +
        '11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111' +
        '11111111111111111111111111111111111111111111111111111111111111111')
        .wordBreak(WordBreak.BREAK_ALL)
    }
    .width('100%')
    .height(80)
    .backgroundColor('#ffb7bdc4')
    .padding({ top: 20, bottom: 20 })
  }
}
```

问题现象下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/q1jrgl7NT-SuBLgx90qoZw/zh-cn_image_0000002765908690.png "点击放大")

**A**：解决方案如下：

* 方案一：通过measureTextSize的height值获取当前文本高度，需要注意获取到的值为px单位，需通过[px2vp](../harmonyos-references/arkts-apis-uicontext-uicontext.md#px2vp12)转换为vp单位后使用，然后通过容器高度/文本高度计算出最多显示几行文本。

  ```ts
  import { MeasureUtils } from '@kit.ArkUI';

  @Entry
  @Component
  struct MeasureTextPage {
    uiContext: UIContext = this.getUIContext();
    measureText: MeasureUtils = this.uiContext.getMeasureUtils();
    @State textHeight: number = 40;
    textPadding: number = 8;
    @State lineHeight: number = 0;

    aboutToAppear(): void {
      let textSize: SizeOptions = this.measureText.measureTextSize({
        textContent: 'Hello World',
        fontSize: 16
      });
      this.lineHeight = this.getUIContext().px2vp(Number(textSize.height));
      console.info(this.lineHeight.toString());
    }

    build() {
      Column({ space: 20 }) {
        Text('这是一段很长的文本这是一段很长的文本这是一段很长的文本这是一段很长的文本这是一段很长的文本这是一段很长的文本这是一段很长的文本这' +
          '是一段很长的文本这是一段很长的文本这是一段很长的文本这是一段很长的文本这是一段很长的文本这是一段很长的文本这是一段很长的文本这是一段' +
          '很长的文本这是一段很长的文本这是一段很长的文本这是一段很长的文本这是一段很长的文本这是一段很长的文本这是一段很长的文本')
          .backgroundColor('#f1f3f5')
          .borderRadius('8vp')
          .width(304)
          .padding(this.textPadding)
          .height(this.textHeight)
          .maxLines(Math.floor((this.textHeight - 2 * this.textPadding) / this.lineHeight))
          .textOverflow({ overflow: TextOverflow.Ellipsis })
        Button('点击').onClick(() => {
          this.textHeight += 2;
        })
      }.width('100%').height('100%')
      .justifyContent(FlexAlign.Center)
    }
  }
  ```

  效果如下图：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/YkabZVQ8SnGlasT8bA1S8g/zh-cn_image_0000002766068618.png "点击放大")
* 方案二：使用TextArea代替Text组件，当TextArea的文本内容超过组件范围时会自动生成滑动条。

**Q：Text文本超长时超过屏幕宽度后会自动换行，如果设置[maxLines](../harmonyos-references/ts-basic-components-text.md#maxlines)属性虽然可以让文本不换行但是会造成显示不全的问题，如何实现Text文本既能无限长展示又能不换行？问题代码如下：**

**A**：可以在Text组件外嵌套一个横向滚动的Scroll组件，并且设置Text文本为从右往左展示，即可让Text组件内容完整展示，最后搭配TextInput的onChange事件，在内容变化时调用Scroll的scrollEdge方法即可实现“输入长度几乎无限长，不换行”。

```ts
@Component
@Entry
struct Problem {
  @State str: string = '';
  build() {
    Column() {
      Text(this.str)
        .margin({ left: 20 })
        .textAlign(TextAlign.End)
        .height(40)
        .fontSize(22)
        .fontColor(Color.Pink)
        .constraintSize({
          minWidth: '80%'
        })
        .maxLines(1)

      Column() {
        TextInput({ placeholder: "请输入内容" })
          .borderRadius(0)
          .onChange((value: string) => {
            this.str = value
          })
      }

    }.justifyContent(FlexAlign.Center)
    .width('100%')
    .margin({ top: 100 })
    .alignItems(HorizontalAlign.End)
  }
}
```

* Scroll横向展示实现：

  ```ts
  .scrollable(ScrollDirection.Horizontal)
  ```
* 设置文本从右往左展示实现：

  ```ts
  Text(this.str)
              .margin({ left: 20 })
              .textAlign(TextAlign.End)
              .height(40)
              .fontSize(22)
              .fontColor(Color.Black)
              .constraintSize({
                minWidth: '80%'
              })
              .maxLines(1)
              .id('textContent');
  ```
* onChange方法触发Scroll滑动到尾部：

  ```ts
  TextInput({ placeholder: '请输入内容' })
            .margin({left:16,right:16})
            .borderRadius(24)
            .onChange((value: string) => {
              this.str = value;
              this.scroller.scrollEdge(Edge.End);
            });
  ```

完整示例代码如下：

```ts
@Entry
@Component
export struct TextInfiniteLength {
  @State str: string = '';
  controller: TextInputController = new TextInputController();
  scroller: Scroller = new Scroller();

  build() {
    Column() {
      Scroll(this.scroller) {
        Row() {
          Text(this.str)
            .margin({ left: 20 })
            .textAlign(TextAlign.End)
            .height(40)
            .fontSize(22)
            .fontColor(Color.Black)
            .constraintSize({
              minWidth: '80%'
            })
            .maxLines(1)
            .id('textContent');
        }
        .layoutWeight(1)
        .justifyContent(FlexAlign.SpaceBetween);
      }
      .padding({ left: 50 })
      .width('100%')
      .scrollBar(BarState.Off)
      .scrollable(ScrollDirection.Horizontal)
      .height(40)
      .width('100%');

      Column() {
        TextInput({ placeholder: '请输入内容' })
          .margin({left:16,right:16})
          .borderRadius(24)
          .onChange((value: string) => {
            this.str = value;
            this.scroller.scrollEdge(Edge.End);
          });

      };

    }
    .justifyContent(FlexAlign.Center)
    .width('100%')
    .margin({ top: 100 })
    .alignItems(HorizontalAlign.End);
  }
}
```

实现效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/VDu-RGyJS5aJvpz4DhmLcw/zh-cn_image_0000002766068622.png "点击放大")

**Q：如何实现点击文字填充“横线”，“横线”可换行。**

**A**：实现方式如下：

1. 使用Span组件作为横线内容容器，结合@State状态管理实现动态内容更新。
2. 通过点击事件触发数据填充，动态修改文本内容。
3. 利用decoration属性设置下划线效果。

```ts
import display from '@ohos.display';
import window from '@ohos.window';

export class DeviceScreen {
  /**
   * Get the device size.
   *
   * @returns promise of window.
   */
  public static getDeviceSize(context: Context): Promise<window.Window> {
    return window.getLastWindow(context);
  }

  /**
   * Get the screen width.
   *
   * @returns screen width.
   */
  public static getDeviceWidth(): number {
    let displayObject = display.getDefaultDisplaySync();
    let screenPixelWidth = displayObject.width;
    let screenDensityDPI = displayObject.densityDPI;
    return screenPixelWidth * (160 / screenDensityDPI);
  }

  /**
   * Get the screen height.
   *
   * @returns screen height.
   */
  public static getDeviceHeight(): number {
    let displayObject = display.getDefaultDisplaySync();
    let screenPixelHeight = displayObject.height;
    let screenDensityDPI = displayObject.densityDPI;
    return screenPixelHeight * (160 / screenDensityDPI);
  }

  public static getStatusHeight(): number {
    let topRectHeight = AppStorage.get<number>('topRectHeight') as number;
    return topRectHeight;
  }

  public static getNavigationHeight(): number {
    let bottomRectHeight = AppStorage.get<number>('bottomRectHeight') as number;
    return bottomRectHeight;
  }
}

@Entry
@Component
struct DynamicTextFill {
  @State options: string[] = ['儿', '往', '出', '林', '雨', '花', '细', '鱼', '东'];
  @State inputText: string = '';

  build() {
    Column() {
      Text() {
        Span('请从以下九个字中点选一句五言诗:')
        if (this.inputText) {
          Span(this.inputText).decoration({
            type: TextDecorationType.Underline, // 设置下划线样式
            color: Color.Black,
          })
        } else {
          Span('__________，')
        }
      }
      .fontSize(17)
      .fontColor('#333333')
      .fontWeight(FontWeight.Normal)
      .lineHeight(26)
      .margin({ left: 15, top: 10, right: 15 })

      Grid() {
        ForEach(this.options, (item: string) => {
          GridItem() {
            Column() {
              Text(item)
                .fontSize(17)
                .fontColor('#333333')
                .fontWeight(FontWeight.Bold)
            }
            .width('100%')
            .height('100%')
            .justifyContent(FlexAlign.Center)
            .backgroundColor(Color.White)
          }
          .aspectRatio(1)
          .onClick(() => {
            this.inputText += `${item}`;
          })
        }, (item: string, index?: number) => JSON.stringify(item) + index)
      }
      .width(DeviceScreen.getDeviceWidth() - 65 * 2)
      .columnsTemplate('1fr 1fr 1fr')
      .rowsGap(0.5)
      .columnsGap(0.5)
      .margin({ top: 60 })
    }
    .height('100%')
    .width('100%')
    .backgroundColor('#F5F5F5')
  }
}
```

**Q：当Text组件与其他组件堆叠出现时，Text的文字内容需获取其他组件的宽高数据，如何进行缩进避让？**

**A**：

* 方案一：问题描述提到组件堆叠，则可用Stack布局，通过设置缩进，为文本标签留下空间，示例代码如下：

  ```ts
  @Entry
  @Component
  struct ExampleOne {
    private dynamicText: string = '标签';

    build() {
      Stack({ alignContent: Alignment.TopStart }) {
        Text('这是详细内容这是详细内容这是详细内容这是详细内容这是详细内容这是详细内容')
          .fontSize(30)
          .textIndent(60)
          .width('100%')

        Text(this.dynamicText)
          .fontSize(20)
          .width(50)
          .border({ width: 1, color: Color.Black, radius: 10 })
          .textAlign(TextAlign.Center)
      }
      .padding(20)
    }
  }
  ```

  效果图如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/V1Z3qzflQxSUy1vhaZsPig/zh-cn_image_0000002765908704.png "点击放大")
* 方案二：获取其他组件宽度并设置Text组件的缩进避让。
  1. 在通过RelativeContainer相对布局，实现标题Row组件和内容Text组件的相同位置显示，但此时两个组件内容会有重叠遮挡。
  2. 通过onAreaChange获取标题Row组件的宽度信息（this.titleWidth），转换为number类型。

     ```ts
     Row() {
             Text('短剧·中国版教父')
           }
           .justifyContent(FlexAlign.Center)
           .backgroundColor('#a3cf62')
           .padding(4)
           .borderRadius(4)
           .id('row1')
           .alignRules({
             top: { anchor: 'text', align: VerticalAlign.Top },
             left: { anchor: 'text', align: HorizontalAlign.Start }
           })
           .onAreaChange((oldValue: Area, newValue: Area) => {
             this.sizeValue = JSON.stringify(newValue);
             this.titleWidth = parseInt(this.sizeValue.split('width":')[1].split(',')[0]); // 获取标题组件的宽度
           })
     ```
  3. 配置Text组件的首行缩进长度为第二步获取的Row组件的宽度（this.titleWidth），实现文字避让。

     ```ts
     Text(this.message)
             .key('text')
             .maxLines(this.lines)
             .lineHeight(26)
             .textIndent(this.titleWidth + 2)
     ```

  完整代码：

  ```ts
  const COLLAPSE_LINES: number = 2;

  @Entry
  @Component
  struct ExampleTwo {
    private lines: number = COLLAPSE_LINES;
    @State sizeValue: string = '';
    @State titleWidth: number = 0;
    private message: string = '这里是详情内容，这里是详情内容，这里是详情内容，这里是详情内容';

    build() {
      RelativeContainer() {
        Text(this.message)
          .key('text')
          .maxLines(this.lines)
          .lineHeight(26)
          .textIndent(this.titleWidth + 2)
        Row() {
          Text('短剧·中国版教父')
        }
        .justifyContent(FlexAlign.Center)
        .backgroundColor('#a3cf62')
        .padding(4)
        .borderRadius(4)
        .id('row1')
        .alignRules({
          top: { anchor: 'text', align: VerticalAlign.Top },
          left: { anchor: 'text', align: HorizontalAlign.Start }
        })
        .onAreaChange((oldValue: Area, newValue: Area) => {
          this.sizeValue = JSON.stringify(newValue);
          this.titleWidth = parseInt(this.sizeValue.split('width":')[1].split(',')[0]); // 获取标题组件的宽度
        })
      }
      .height('auto')
      .borderWidth(1)
      .margin({ top: 100, left: 8, right: 8 })
    }
  }
  ```

  实现效果：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/qZGNSkAXSSCxA8lsEn8Zuw/zh-cn_image_0000002765908710.png "点击放大")
* 方案三：可以使用ContainerSpan组件，作为设置Text组件的缩进避让的替代方案，可参考官方文档[通过attributemodifier设置背景样式](../harmonyos-references/ts-basic-components-containerspan.md#示例2通过attributemodifier设置背景样式)。可在组件内使用Span、ImageSpan组件。但此方法不支持通用属性和通用事件，有一定局限性。
