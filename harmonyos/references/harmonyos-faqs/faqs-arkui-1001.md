---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1001
title: 如何在AlertDialog中根据数组动态生成多个按钮
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何在AlertDialog中根据数组动态生成多个按钮
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:25+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:5082ccfb2e5b32bbfdcdb329fd1d078daa474370331d57811a7ec9e592f957de
---

## 问题现象

AlertDialog是否支持在弹窗内显示一个已经定义好的数组，例如list=[0,1,2,3]，使每个数组元素单独作为按钮显示在弹窗内。

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0c/v3/WxAz6bGER3qUwVI-3tJ7ew/zh-cn_image_0000002658923989.png "点击放大")

## 背景知识

* [AlertDialog](../harmonyos-references/ohos-arkui-advanced-dialog.md#alertdialog)是操作确认类弹出框，触发一个将产生严重后果的不可逆操作时，如删除、重置、取消编辑、停止等。
* 通过[AlertDialogParamWithOptions](../harmonyos-references/ts-methods-alert-dialog-box.md#alertdialogparamwithoptions10对象说明)中的buttonDirection属性可控制按钮的排布方向，按钮排布方向默认为DialogButtonDirection.AUTO。建议3个以上按钮使用Auto模式（两个以上按钮会切换为纵向模式，通常能显示更多按钮）。非Auto模式下，3个以上按钮可能会显示不全，超出显示范围的按钮会被截断。

## 解决方案

总体思路如下：通过实现AlertDialog的[AlertDialogButtonOptions](../harmonyos-references/ts-methods-alert-dialog-box.md#alertdialogbuttonoptions10对象说明)接口，定义一个CustomAlertDialogButtonOptions类，并通过自定义的函数将普通数组转化为AlertDialog的AlertDialogParamWithOptions需要的类型即可实现需求。

1. 实现AlertDialog的AlertDialogButtonOptions接口，命名为CustomAlertDialogButtonOptions。

   ```ts
   class CustomAlertDialogButtonOptions implements AlertDialogButtonOptions {
     value: string = '保存';
     buttonIndex: number = -1;
     action = () => {
       console.info('Callback when button1 is clicked');
     };
   }
   ```
2. 定义函数，根据初始的数组，把每个元素的类型转为CustomAlertDialogButtonOptions类型，并在action回调中根据元素下标处理逻辑。

   ```ts
   setDialogButtonWithList(list: number[]): CustomAlertDialogButtonOptions[] {
     let tempList: CustomAlertDialogButtonOptions[] = [];
     for (let index = 0; index < list.length; index++) {
       const element = list[index];
       tempList.push({
         value: element.toString(),
         buttonIndex: index,
         action: () => {
           switch (index) {
             // 根据index做对应的逻辑处理
             case 0:
               this.title = '选中了第一项';
               break;
             case 1:
               this.title = '选中了第二项';
               break;
             case 2:
               this.title = '选中了第三项';
               break;
             case 3:
               this.title = '选中了第四项';
               break;
           }
           console.info('Callback when button is clicked index =', index);
         }
       });
     }
     return tempList;
   }
   ```

完整示例参考如下：

```ts
class CustomAlertDialogButtonOptions implements AlertDialogButtonOptions {
  value: string = '保存';
  buttonIndex: number = -1;
  action = () => {
    console.info('Callback when button1 is clicked');
  };
}
@Entry
@Component
struct AlertDialogExample {
  private list: number[] = [];
  @State title: string = '';
// 模拟数据源
  aboutToAppear(): void {
    for (let index = 0; index < 4; index++) {
      this.list.push(index);
    }
  }
  setDialogButtonWithList(list: number[]): CustomAlertDialogButtonOptions[] {
    let tempList: CustomAlertDialogButtonOptions[] = [];
    for (let index = 0; index < list.length; index++) {
      const element = list[index];
      tempList.push({
        value: element.toString(),
        buttonIndex: index,
        action: () => {
          switch (index) {
            // 根据index做对应的逻辑处理
            case 0:
              this.title = '选中了第一项';
              break;
            case 1:
              this.title = '选中了第二项';
              break;
            case 2:
              this.title = '选中了第三项';
              break;
            case 3:
              this.title = '选中了第四项';
              break;
          }
          console.info('Callback when button is clicked index =', index);
        }
      });
    }
    return tempList;
  }
  build() {
    RelativeContainer() {
      Button('多按钮弹窗')
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        })
        .onClick(() => {
          this.getUIContext().showAlertDialog(
            {
              title: 'title',
              subtitle: 'subtitle',
              message: 'text',
              autoCancel: true,
              alignment: DialogAlignment.Bottom,
              gridCount: 4,
              buttonDirection: DialogButtonDirection.HORIZONTAL,
              buttons: this.setDialogButtonWithList(this.list),
              cancel: () => {
                console.info('Closed callbacks');
              },
              onWillDismiss: (dismissDialogAction: DismissDialogAction) => {
                console.info(`reason= ${dismissDialogAction.reason}`);
                console.info('AlertDialog onWillDismiss');
                if (dismissDialogAction.reason === DismissReason.PRESS_BACK) {
                  dismissDialogAction.dismiss();
                }
                if (dismissDialogAction.reason === DismissReason.TOUCH_OUTSIDE) {
                  dismissDialogAction.dismiss();
                }
              }
            }
          );
        }).backgroundColor(0x317aff);
      Text(this.title)
        .alignRules({
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        })
        .margin({ top: 50 });
    }.width('100%').margin({ top: 5 });
  }
}
```
