---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1075
title: Select如何自定义按钮样式和内容
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > Select如何自定义按钮样式和内容
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:06+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:fbaa40a8ff9c4baf52c420d21aeccaebbbbabb43c157a206fe3517926fe29629
---

## 问题现象

Select按钮如何实现以下场景：

* **场景一**：如何修改Select按钮内容区的文本样式和三角箭头颜色。
* **场景二**：Select组件按钮内容居中展示（文本和下拉三角箭头居中显示）。
* **场景三**：如何自定义Select按钮内容区，可以自己输入内容，也能在下拉菜单中选择，以及三角箭头换成其他图标。

## 背景知识

* [Select](../harmonyos-references/ts-basic-components-select.md)下拉按钮组件，提供下拉选择菜单，让用户在多个选项间选择。[selected](../harmonyos-references/ts-basic-components-select.md#selected18)属性可以设置下拉菜单初始选项的索引。[value](../harmonyos-references/ts-basic-components-select.md#value18)设置下拉按钮的文本内容。选中菜单项后，按钮文本将自动更新为选中的菜单项文本。selected和value设置的属性均支持[$$](../harmonyos-guides/arkts-two-way-sync.md)、[!!](../harmonyos-guides/arkts-new-binding.md)双向绑定。
* 从API20开始可以通过[textModifier](../harmonyos-references/ts-basic-components-select.md#textmodifier20)定制Select按钮文本样式，以及通过[arrowModifier](../harmonyos-references/ts-basic-components-select.md#arrowmodifier20)定制Select按钮下拉箭头图标样式。
* [TextArea](../harmonyos-references/ts-basic-components-textarea.md)多行文本输入框组件，当输入的文本内容超过组件宽度时会自动换行显示。当输入内容发生变化时会触发[onChange](../harmonyos-references/ts-basic-components-textinput.md#onchange)。
* [hitTestBehavior](../harmonyos-references/ts-universal-attributes-hit-test-behavior.md#hittestbehavior)设置组件的触摸测试类型。默认触摸测试效果为[HitTestMode](../harmonyos-references/ts-appendix-enums.md#hittestmode9).Default。自身及子节点响应触摸测试，但阻塞兄弟节点的触摸测试，不影响祖先节点的触摸测试。
* [backgroundColor](../harmonyos-references/ts-universal-attributes-background.md#backgroundcolor20)通用属性，通过color值设置组件背景色。color的值为undefined时，恢复为默认透明的背景色。

## 解决方案

* **场景一**：API20以后可以参考官方API示例中[设置Select中文本和箭头样式](../harmonyos-references/ts-basic-components-select.md#示例6设置select中文本和箭头样式)。如果是API20以前可参考场景二中第二种方式。
* **场景二**：由于API20版本Select组件按钮部分只能设置文本和下拉箭头样式，无法直接修改Select按钮内容，但是可以设置[menuAlign](../harmonyos-references/ts-basic-components-select.md#menualign18)让下拉框相对Select按钮居中。如果需要Select按钮内容居中，有以下两种方式可以实现类似的效果。
  1. 通过给Select组件添加Padding属性，设置相同的左右内边距，让文本和图标显示在Select中间，但是在文本较长时使用容易让文本显示不全。

     ```ts
     @Entry
     @Component
     struct Center1 {
       build() {
         Column() {
           Select([
             { value: 'aaa', icon: $r('app.media.startIcon') },
             { value: 'bbb', icon: $r('app.media.startIcon') },
             { value: 'ccc', icon: $r('app.media.startIcon') },
             { value: 'ddd', icon: $r('app.media.startIcon') }
           ])
             .width('70%')
             .selected(0)
             .value('aaa')
             .padding({ left: 90, right: 90 }) // 设置左右边距，按钮内容实现居中
             .space(0)
             .menuAlign(MenuAlignType.CENTER);
         }
         .height('100%')
         .width('100%');
       }
     }
     ```

     效果预览：

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/CPIRjD56RH6mxGCdppR4-w/zh-cn_image_0000002658926449.png "点击放大")
  2. 自定义Select内容区。通过将原本的Select按钮设置为纯透明，在Select组件之上添加Row组件设置相同的宽高（[onSizeChange](../harmonyos-references/ts-universal-component-size-change-event.md#onsizechange)事件获取原Select宽高），对Row设置hitTestBehavior(HitTestMode.None)让事件可透传到Select（子组件也需添加）。自定义Row组件中的内容，实现Select组件按钮内容居中的效果。

     ```ts
     @Entry
     @Component
     struct Center2 {
       @State selectValue: string = '未选择'; // Select的值
       @State selectWidth: number = 0;
       @State selectHeight: number = 0;
       selectItems: SelectOption[] = [
         { value: 'aaa', icon: $r('app.media.startIcon') },
         { value: 'bbb', icon: $r('app.media.startIcon') },
         { value: 'ccc', icon: $r('app.media.startIcon') },
         { value: 'ddd', icon: $r('app.media.startIcon') }
       ];

       build() {
         Column() {
           Stack() {
             Select(this.selectItems)
               .width('70%')
               .value($$this.selectValue)
               .opacity(0)
               .menuAlign(MenuAlignType.CENTER)
               .onSizeChange((oldSize, newSize) => {
                 // 获取Select组件宽高
                 this.selectWidth = newSize.width as number;
                 this.selectHeight = newSize.height as number;
                 console.info('W：', this.selectWidth);
                 console.info('H：', this.selectHeight);
               });
             Row({ space: 10 }) {
               Text(this.selectValue)
                 .maxLines(1)
                 .textOverflow({ overflow: TextOverflow.Ellipsis })
                 .hitTestBehavior(HitTestMode.None)
                 .constraintSize({ maxWidth: this.selectWidth - 40, maxHeight: '100%' }); // 选择的文本
               SymbolGlyph($r('sys.symbol.arrowtriangle_down_fill')).hitTestBehavior(HitTestMode.None).width(20); // 下拉箭头
             }
             .padding(10)
             .width(this.selectWidth) // 根据Select组件设置宽
             .height(this.selectHeight) // 根据Select组件设置高
             .borderRadius(20) // 设置圆角
             .justifyContent(FlexAlign.Center) // 内容居中
             .hitTestBehavior(HitTestMode.None) // 设置事件透传
             .stateStyles({
               // 设置正常状态和按压状态颜色
               normal: {
                 .backgroundColor('#f1f3f5');
               },
               pressed: {
                 .backgroundColor('#D9D9DB');
               }
             });
           };
         }
         .height('100%')
         .width('100%');
       }
     }
     ```

     效果预览：

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/mRHYCQc-Rjy4JgFa2OW_SA/zh-cn_image_0000002628407238.png "点击放大")
* **场景三**：API20以后也可以通过textModifier和arrowModifier自定义内容样式，把文本和下拉箭头改为透明。再通过Row自定义内容在原Select组件上层，参考场景二的第二种方式将Text改为TextArea。在输入框onChange事件中匹配内容对应的索引，并修改Select中的索引，让输入内容可以修改下拉框中的选项。实现既可输入内容也能在下拉菜单中选择。

  ```ts
  import { SymbolGlyphModifier, TextModifier } from '@kit.ArkUI';

  @Entry
  @Component
  struct TextInputSelect {
    @State selectValue: string = ''; // 文本输入框内容
    @State selectIndex: number = -1; // 当前Select索引
    @State selectWidth: number = 0;
    @State selectHeight: number = 0;
    selectItems: SelectOption[] = [
      { value: 'aaa', icon: $r('app.media.startIcon') },
      { value: 'bbb', icon: $r('app.media.startIcon') },
      { value: 'ccc', icon: $r('app.media.startIcon') },
      { value: 'ddd', icon: $r('app.media.startIcon') }
    ];
    textModifier: TextModifier = new TextModifier(); // 自定义Select文本样式
    symbolGlyphModifier: SymbolGlyphModifier = new SymbolGlyphModifier(); // 自定义Select下拉箭头样式

    aboutToAppear(): void {
      // 文本和下拉箭头设置为纯透明
      this.textModifier.fontColor('#00000000');
      this.symbolGlyphModifier.fontColor(['#00000000']);
    }

    build() {
      Column() {
        Stack() {
          Select(this.selectItems)
            .width(300)
            .height(80)
            .backgroundColor('#f1f3f5')
            .value($$this.selectValue)
            .selected(this.selectIndex)
            .textModifier(this.textModifier)
            .arrowModifier(this.symbolGlyphModifier)
            .onSizeChange((oldSize, newSize) => {
              this.selectWidth = newSize.width as number;
              this.selectHeight = newSize.height as number;
              console.info('W：', this.selectWidth);
              console.info('H：', this.selectHeight);
            });
          // 自定义Select内容
          Row() {
            // 文本输入框
            TextArea({ placeholder: '请选择', text: $$this.selectValue })
              .backgroundColor('#00000000')
              .selectionMenuHidden(true)
              .hitTestBehavior(HitTestMode.Transparent)
              .layoutWeight(1)
              .onChange(() => {
                // 匹配当前输入框内容对应的索引
                this.selectIndex = this.selectItems.findIndex((item) => {
                  return item.value === this.selectValue;
                });
                console.info(`当前索引值：${this.selectIndex}`);
              });
            // 自定义下拉按钮
            Row() {
              Text('显示菜单');
              SymbolGlyph($r('sys.symbol.chevron_down'));
            }.margin({ right: 10 })
            .hitTestBehavior(HitTestMode.None); // 设置透传
          }
          .width(this.selectWidth)
          .height(this.selectHeight)
          .borderRadius(20)
          .hitTestBehavior(HitTestMode.None); // 设置透传
        };
      }
      .height('100%')
      .width('100%');
    }
  }
  ```

  效果预览：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/CV-5O8VxScusqf2Mz3RnCQ/zh-cn_image_0000002658806501.png "点击放大")

## 常见FAQ

Q：在字体大小一致的前提下，Select组件中显示的文本相较Text组件中的文本，视觉上更为粗重。

A：根据Select组件中的[font](../harmonyos-references/ts-basic-components-select.md#font)方法得知，下拉按钮本身的文本样式中weight的默认值为FontWeight.Medium，且后续版本没有相关变动。而Text组件字体默认粗细为FontWeight.Normal，所以Select按钮中文本字体默认比Text文本更粗。

Q：Select组件的backgroundColor属性设置为undefined时得到的背景色为透明，是否符合预期？

A：backgroundColor通用属性color值为undefined时，恢复为默认透明的背景色，所以是符合预期的。
