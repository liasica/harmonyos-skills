---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1391
title: 页面底部弹窗显示不全
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 页面底部弹窗显示不全
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:15+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:6047250af95d1c8670bd100337a6cb728a90e7fe931a6c7632d73446d61b4886
---

## 问题现象

页面底部的弹窗内容显示不全。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f/v3/IPcIJLU6TGOpXfD1_BWjMg/zh-cn_image_0000002628762566.png "点击放大")

## 背景知识

* [bindSheet](../harmonyos-references/ts-universal-attributes-sheet-transition.md#bindsheet)：给组件绑定半模态页面，点击后显示模态页面。
* [Scroll](../harmonyos-references/ts-container-scroll.md)：可滚动的容器组件，当子组件的布局尺寸超过父组件的尺寸时，内容可以滚动。

## 问题定位

排查应用半模态面板高度设置是否合理。检查bindSheet属性中height的值。如果高度设置不合理，就会导致页面底部弹窗显示不全。

```ts
  build() {
    Column() {
      Button('bindSheet测试')
        .onClick(()=>{
          this.isShow = true
        })
        .bindSheet($$this.isShow, this.settingBuilder, {
          height: 65,  // 高度设置不合理导致显示不全
          backgroundColor: Color.White,
        })
    }
    .height('100%')
    .width('100%')
    .backgroundColor(Color.Gray)
    .padding({top: 50, bottom: 50})
  }
```

## 分析结论

半模态面板高度不足以容纳全部内容，导致底部内容被截断，显示不全。

## 修改建议

建议调整半模态面板高度，尽量使用百分比高度，将半模态页面完整展示出来。同时给半模态页面添加Scroll组件，可以上下滑动查看页面内容。

```ts
@Entry
@Component
struct TestDemo {
  @Builder
  settingBuilder() {
    Setting();
  }

  @State isShow: boolean = false; // 控制模态窗显隐状态

  build() {
    Column() {
      Button('bindSheet测试')
        .margin({ top: 60 })
        .onClick(() => {
          this.isShow = true;
        })
        .bindSheet($$this.isShow, this.settingBuilder, {
          height: '55%',
          backgroundColor: Color.White,
        });
    }
    .height('100%')
    .width('100%')
    .backgroundColor(Color.White);
  }
}

@Component
struct Setting {
  private item: string[] = [];

  aboutToAppear(): void {
    for (let index = 1; index <= 30; index++) {
      this.item.push(`设置${index}`);
    }
  }

  build() {
    Column() {
      Row() {
        Text('标题')
          .fontWeight(FontWeight.Bold)
          .fontSize(25)
          .margin({ left: 16, top: 30 });
      }
      .justifyContent(FlexAlign.Start)
      .width('100%');

      Scroll() {
        Column() {
          ForEach(this.item, (item: string) => {
            Row() {
              Text(item);
              Checkbox();
            }
            .justifyContent(FlexAlign.SpaceBetween)
            .width('100%')
            .height(60);

            Divider()
              .width('100%');
          });
        }
        .justifyContent(FlexAlign.Start)
        .constraintSize({ minHeight: '100%' })
        .width('100%')
        .padding({ left: 16, right: 16, top: 10 });
      }
      .width('100%')
      .scrollBar(BarState.Off)
      .layoutWeight(1);
    }
    .width('100%');
  }
}
```
