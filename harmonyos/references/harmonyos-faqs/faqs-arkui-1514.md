---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1514
title: 如何实现顶部自定义下拉菜单及其遮罩效果
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何实现顶部自定义下拉菜单及其遮罩效果
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:26+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:980d740759d409706ae664235bbbcc6c8600b0626e957b7050430adc24993f13
---

## 问题现象

需要在页面顶部展示一个默认选项。用户点击该选项时，弹出自定义下拉菜单，菜单带有遮罩效果（蒙层）。用户从菜单中选择某一选项后，顶部显示的文本内容应更新为当前所选选项。

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/u5S4t4PcQQiJhqvVZPE3LA/zh-cn_image_0000002658965771.png "点击放大")

## 背景知识

* [Stack](../harmonyos-references/ts-container-stack.md)：堆叠容器，子组件按照顺序依次入栈，后一个子组件覆盖前一个子组件。
* [animation](../harmonyos-references/ts-animatorproperty.md)：组件的某些通用属性变化时，可以通过属性动画实现渐变过渡效果，提升用户体验。支持的属性包括[width](../harmonyos-references/ts-universal-attributes-size.md#width)、[height](../harmonyos-references/ts-universal-attributes-size.md#height)、[backgroundColor](../harmonyos-references/ts-universal-attributes-background.md#backgroundcolor)、[opacity](../harmonyos-references/ts-universal-attributes-opacity.md#opacity)、[scale](../harmonyos-references/ts-universal-attributes-transformation.md#scale)、[rotate](../harmonyos-references/ts-universal-attributes-transformation.md#rotate)、[translate](../harmonyos-references/ts-universal-attributes-transformation.md#translate)等。布局类改变宽高的动画，内容都是直接到终点状态，例如文字、[Canvas](../harmonyos-references/ts-components-canvas-canvas.md)的内容等，如果要内容跟随宽高变化，可以使用[renderFit](../harmonyos-references/ts-universal-attributes-renderfit.md#renderfit)属性配置。

## 解决方案

通过Stack来搭建主体框架，通过变量控制菜单显示隐藏，箭头通过属性动画animation进行翻转。

```screen
@Entry
@Component
struct DropDownSelectionMenuPage {
  @State currentCompany: string = '企业 A';
  private readonly companies: string[] = ['企业 A', '企业 B', '企业 C'];
  @State isMenuShow: boolean = false;
  @State rotateAngle: number = 0; // 0 向上，180 向下
  private readonly animationDuration: number = 250;
  private readonly topBarHeight: number = 50; // 顶部按钮高度

  build() {
    Stack({ alignContent: Alignment.TopStart }) {
      // 主内容区域
      Column() {
        // 顶部按钮
        Row() {
          Row() {
            Text(this.currentCompany)
              .fontSize(16)
              .fontColor('#007DFF');
            // 箭头图标
            Image($r('sys.media.ohos_ic_public_arrow_up'))
              .width(16)
              .height(16)
              .fillColor('#007DFF')
              .margin({ left: 4 })
              .rotate({ angle: this.rotateAngle })
              .animation({
                duration: this.animationDuration,
                curve: Curve.EaseInOut
              });
          }
          .layoutWeight(1)
          .justifyContent(FlexAlign.Center);
        }
        .width('100%')
        .height(this.topBarHeight)
        .backgroundColor('#FFFFFF')
        .border({ width: { bottom: 1 }, color: '#E5E5E5' })
        .onClick(() => this.toggleMenu())
        .zIndex(10); // 高于蒙层

        // 居中文字
        Text(this.currentCompany)
          .fontSize(32)
          .fontWeight(FontWeight.Bold)
          .margin({ top: 200 })
          .alignSelf(ItemAlign.Center)
          .animation({ duration: 200 });

        // 下方占位区域，被蒙层覆盖
        Blank();
      };

      // 蒙层 + 菜单（仅当展开时）
      if (this.isMenuShow) {
        Column() {
          // 菜单
          Column() {
            ForEach(this.companies, (item: string) => {
              Row() {
                Text(item)
                  .fontSize(16)
                  .fontColor(item === this.currentCompany ? '#007DFF' : '#333333');
                if (item === this.currentCompany) {
                  Image($r('sys.media.ohos_ic_public_ok'))
                    .width(20)
                    .height(20)
                    .fillColor('#007DFF');
                }
              }
              .width('100%')
              .height(48)
              .padding({ left: 16, right: 16 })
              .justifyContent(FlexAlign.SpaceBetween)
              .onClick(() => {
                this.currentCompany = item;
                this.toggleMenu();
              });
            }, (item: string) => item);
          }
          .width('100%')
          .backgroundColor('#FFFFFF');

          // 蒙层（剩余区域）
          Column()
            .width('100%')
            .layoutWeight(1) // 撑满剩余高度
            .backgroundColor('rgba(0,0,0,0.5)')
            .onClick(() => this.toggleMenu());
        }
        .width('100%')
        .position({ x: 0, y: this.topBarHeight }) // 顶部 Y 与按钮下沿对齐
        .zIndex(9);
      }
    }
    .width('100%')
    .height('100%')
    .backgroundColor('#F5F5F5')
    .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.BOTTOM]);
  }

  private toggleMenu() {
    this.isMenuShow = !this.isMenuShow;
    this.rotateAngle = this.isMenuShow ? 180 : 0;
  }
}
```
