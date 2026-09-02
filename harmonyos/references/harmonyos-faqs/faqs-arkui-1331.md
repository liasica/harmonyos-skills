---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1331
title: 使用bindPopup实现气泡占用全屏时TextInput可以输入文本的效果
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 使用bindPopup实现气泡占用全屏时TextInput可以输入文本的效果
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:21+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:f36003e79b08f048def6f3fd4d39a43eb4c1e53352a070bd96cad6485f6f5242
---

## 问题现象

使用TextInput和bindPopup如何实现带动态提示的输入框。需要实现以下效果：

* Popup的背景为透明，Popup显示时占用整个窗口。
* 当点击TextInput输入框时可以获取焦点输入文本，并且输入框失去焦点时隐藏Popup。

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/EORzekH6QxWKvTVkpjTVHA/zh-cn_image_0000002658839163.gif "点击放大")

## 背景知识

* [bindPopup](../harmonyos-references/ts-universal-attributes-popup.md#bindpopup)为[TextInput](../harmonyos-references/ts-basic-components-textinput.md)等组件绑定Popup气泡，可以设置[PopupOptions类型说明](../harmonyos-references/ts-universal-attributes-popup.md#popupoptions类型说明)下的backgroundBlurStyle属性为BlurStyle.NONE用来关闭气泡的模糊背景，可以使气泡变为透明。
* TextInput主要用于获取用户输入的信息，并将信息处理成数据进行上传，[添加事件](../harmonyos-guides/arkts-common-components-text-input.md#添加事件)可以获取输入框内改变的文本内容。

## 解决方案

实现气泡占用全屏时TextInput可以输入文本的效果，参考以下步骤：

1. 定义message存储TextInput组件当前的文本内容，并且使用@State装饰。

   ```screen
   @State message: string = '';
   ```
2. 定义customPopup控制弹出框(Popup)的显示和隐藏状态。当customPopup为true时，弹出框显示，为false时，弹出框隐藏。

   ```screen
   @State customPopup: boolean = false;
   ```
3. 将弹出框(Popup)的尺寸设置为其可用空间的100%宽度和100%高度。

   ```screen
   @Builder
   popupBuilder() {
     Row({ space: 2 }) {
       Text(this.tips).fontSize(15);
     }
     .alignItems(VerticalAlign.Center)
     .justifyContent(FlexAlign.Center)
     .width('100%')
     .height('100%') // popup显示时占用整个窗口
     .padding(5);
   }
   ```
4. 创建TextInput输入框，使用onEditChange事件控制弹出框(Popup)的显示和隐藏，设置backgroundBlurStyle: BlurStyle.NONE禁用弹出框(Popup)弹出背景的模糊效果。

   ```screen
   build() {
     Column() {
       TextInput({ text: this.message, placeholder: '请输入姓名' })
         .margin({
           top: 50,
           left: 15,
           right: 15
         })
         .enableAutoFill(false)
         .bindPopup(this.customPopup, {
           builder: this.popupBuilder,
           placement: Placement.Bottom,
           mask: { color: '#33000000' },
           backgroundBlurStyle: BlurStyle.NONE, // 去除模糊背景填充效果
           enableArrow: false, // 隐藏箭头
           autoCancel: true,
           showInSubWindow: false,
           onStateChange: (e) => {
             if (!e.isVisible) {
               this.customPopup = false; // 点击了弹出框外部的区域，及时地将@State变量同步更新为false
             }
           }
         })
         .onChange((value: string) => {
           this.message = value;
           if (value.length == 0) {
             this.tips = '';
             return;
           }

           if (!isChineseCharByRegex(value)) {
             this.tips = '您的输入有误，姓名只能为汉字';
           } else {
             this.tips = '';
           }
         })
         .onEditChange((isEditing: boolean) => {
           // isEditing为true表示输入框获得了焦点
           if (isEditing) { // 只有获得焦点才显示
             this.customPopup = true;
           } else {
             this.customPopup = false; // 输入框失去焦点时隐藏
           }
         });
     }
     .width('100%')
     .height('100%');
   }
   ```

完整示例参考如下：

```screen
@Entry
@Component
struct BindPopUpDemo {
  @State message: string = '';
  @State customPopup: boolean = false;
  @State tips: string = '';

  @Builder
  popupBuilder() {
    Row({ space: 2 }) {
      Text(this.tips).fontSize(15);
    }
    .alignItems(VerticalAlign.Center)
    .justifyContent(FlexAlign.Center)
    .width('100%')
    .height('100%') // popup显示时占用整个窗口
    .padding(5);
  }

  build() {
    Column() {
      TextInput({ text: this.message, placeholder: '请输入姓名' })
        .margin({
          top: 50,
          left: 15,
          right: 15
        })
        .enableAutoFill(false)
        .bindPopup(this.customPopup, {
          builder: this.popupBuilder,
          placement: Placement.Bottom,
          mask: { color: '#33000000' },
          backgroundBlurStyle: BlurStyle.NONE, // 去除模糊背景填充效果
          enableArrow: false, // 隐藏箭头
          autoCancel: true,
          showInSubWindow: false,
          onStateChange: (e) => {
            if (!e.isVisible) {
              this.customPopup = false; // 点击了弹出框外部的区域，及时地将@State变量同步更新为false
            }
          }
        })
        .onChange((value: string) => {
          this.message = value;
          if (value.length == 0) {
            this.tips = '';
            return;
          }

          if (!isChineseCharByRegex(value)) {
            this.tips = '您的输入有误，姓名只能为汉字';
          } else {
            this.tips = '';
          }
        })
        .onEditChange((isEditing: boolean) => {
          // isEditing为true表示输入框获得了焦点
          if (isEditing) { // 只有获得焦点才显示
            this.customPopup = true;
          } else {
            this.customPopup = false; // 输入框失去焦点时隐藏
          }
        });
    }
    .width('100%')
    .height('100%');
  }
}

function isChineseCharByRegex(char: string): boolean {
  return /^[\u4e00-\u9fa5\u3400-\u4dbf\ud840-\ud87f\udc00-\udfff\uF900-\uFAFF]+$/.test(char);
}
```
