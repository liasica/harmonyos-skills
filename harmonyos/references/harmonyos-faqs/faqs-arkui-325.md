---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-325
title: 如何控制CustomDialog显示层级
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何控制CustomDialog显示层级
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:59+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:79295db22603cad49c6749ed2db829fb8f068f9aada06222375714f55c1658cb
---

**问题现象**

在A页面弹出一个CustomDialog，若Dialog未关闭时从A页面跳转到B页面，此时会发现在A页面弹出的Dialog会出现在B页面的层级上方。请问有什么方式可以让页面B盖住Dialog？

**解决措施**

原因是CustomDialog的默认层级高于页面。可以使用navigation方式跳转，它主要用于实现页面间以及组件内部的页面跳转，页面层级由导航栈管理，默认后打开的页面层级高于之前的页面，navigation跳转时系统会自动处理页面层级关系，包括关闭前页面的所有弹窗。具体请参考如下示例代码：

```ts
@Component
struct PrivacyDetailPage {
  @State message: string = 'Hello World';

  build() {
    NavDestination() {
      Row() {
        Column() {
          Text(this.message)
            .fontSize(50)
            .fontWeight(FontWeight.Bold)
        }
        .width('100%')
      }
      .height('100%')
    }
    .onBackPressed(() => {
      this.getUIContext().getPromptAction().showToast({ message: '123' });
      return false;
    })
  }
}

@Entry
@Component
struct CustomDialogDisplayLevel {
  // Used for navigation stack management
  @Provide('pageInfos') pageInfos: NavPathStack = new NavPathStack();
  @State textValue: string = 'Input';
  // Visible and hidden control is set to not occupied
  @State visible: Visibility = Visibility.None;

  @Builder
  pageMap(name: string) {
    if (name === 'pageOne') {
      PrivacyDetailPage()
    }
  }

  build() {
    Navigation(this.pageInfos) {
      Column() {
        Stack() {
          Row() {
            Column() {
              Text('I am the first page')
                .fontSize(30)
                .fontWeight(FontWeight.Bold)
              Button('Button')
                .onClick(() => {
                  console.info('hit me!');
                  if (this.visible === Visibility.Visible) {
                    this.visible = Visibility.None;
                  } else {
                    this.visible = Visibility.Visible;
                  }
                })
                .backgroundColor(0x777474)
                .fontColor(0x000000)
            }
            .height('100%')
            .width('100%')
            .justifyContent(FlexAlign.Start)
            .alignItems(HorizontalAlign.Center)
          }
          .height('100%')
          .backgroundColor('#FFF')

          Text('')
            .onClick(() => {
              if (this.visible === Visibility.Visible) {
                this.visible = Visibility.None;
              } else {
                this.visible = Visibility.Visible;
              }
            })
            .width('100%')
            .height('100%')
            // set opacity
            .opacity(0.5)
            .backgroundColor(Color.Black)
            .visibility(this.visible)
          Column() {
            GridRow({
              columns: {
                xs: 1,
                sm: 4,
                md: 8,
                lg: 12
              },
              breakpoints: {
                value: ['400vp', '600vp', '800vp'],
                reference: BreakpointsReference.WindowSize
              },
            }) {
              GridCol({
                span: {
                  xs: 1,
                  sm: 2,
                  md: 4,
                  lg: 8
                },
                offset: {
                  xs: 0,
                  sm: 1,
                  md: 2,
                  lg: 2
                }
              }) {
                Column() {
                  Text('Privacy')
                    .fontSize(20)
                    .margin({
                      top: 10,
                      bottom: 10
                    })
                  Text('Do you want to jump to the privacy details page?')
                    .fontSize(16)
                    .margin({ bottom: 10 })
                  Flex({ justifyContent: FlexAlign.SpaceAround }) {
                    Button('Cancel')
                      .onClick(() => {
                        if (this.visible === Visibility.Visible) {
                          this.visible = Visibility.None;
                        } else {
                          this.visible = Visibility.Visible;
                        }
                      })
                      .backgroundColor(0xffffff)
                      .fontColor(Color.Black)
                    Button('OK')
                      .onClick(() => {
                        try {
                          this.pageInfos.pushPath({ name: 'pageOne' });
                        } catch (error) {
                          let err = error as BusinessError;
                          hilog.error(0x00, 'PrivacyDetailPage', `error code: ${err.code},message:${err.message}`);
                        }
                      })
                      .backgroundColor(0xffffff)
                      .fontColor(Color.Red)
                  }
                  .margin({ bottom: 10 })
                }
                .backgroundColor(0xffffff)
                .visibility(this.visible)
                .clip(true)
                .borderRadius(20)
              }
            }
          }
          // set dialog width
          .width('100%')
        }
      }
      .width('100%')
      .margin({ top: 5 })
    }
    .navDestination(this.pageMap)
  }
}
```
