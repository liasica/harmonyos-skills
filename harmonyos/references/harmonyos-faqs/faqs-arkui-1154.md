---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1154
title: 如何实现基于dialogContent的自定义弹窗的双向数据绑定
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何实现基于dialogContent的自定义弹窗的双向数据绑定
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:06+08:00
doc_updated_at: 2026-08-19
content_hash: sha256:6a9d8d3388852d5dbec86952e7fe353be82a0c0b4e0430e92b1c2305963831f8
---

## 问题现象

场景一：使用openCustomDialog打开的自定义弹窗中，如何实现弹窗和页面间的双向数据绑定？

场景二：使用bindSheet时，如何实现弹窗和页面间的双向数据绑定？

场景三：使用@CustomDialog时，如何实现弹窗和页面间的双向数据绑定？

## 背景知识

* [openCustomDialog](../harmonyos-references/arkts-apis-uicontext-promptaction.md#opencustomdialog12)：创建并弹出dialogContent对应的自定义弹窗，该方法创建弹窗的方式有两种，一种是通过ComponentContent的方式创建弹窗，一种是通过builder的方式创建弹窗。
* [update](../harmonyos-references/js-apis-arkui-componentcontent.md#update)：该接口属于ComponentContent自带的方法，用于更新通过ComponentContent创建的弹窗。
* [bindSheet](../harmonyos-references/ts-universal-attributes-sheet-transition.md#bindsheet)：给组件绑定半模态页面，点击后显示模态页面。
* [@Builder装饰器](../harmonyos-guides/arkts-builder.md)：ArkUI提供轻量的UI元素复用机制@Builder，其内部UI结构固定，仅与使用方进行数据传递。开发者可将重复使用的UI元素抽象成方法，在build方法中调用。@Builder装饰的函数也称为“自定义构建函数”。
* [自定义弹窗 (CustomDialog)](../harmonyos-references/ts-methods-custom-dialog-box.md#customdialogcontroller)：通过CustomDialogController类显示自定义弹窗。

## 解决方案

* 场景一：使用openCustomDialog打开的自定义弹窗中，如何实现弹窗和页面间的双向数据绑定？
  + 方案一：使用[ComponentContent](../harmonyos-references/js-apis-arkui-componentcontent.md)创建弹窗UI。

    实现弹窗和页面间的双向数据绑定的核心思路是通过共享同一个数据对象Params，并配合ComponentContent中的update()来主动刷新UI。

    在以下示例中，页面组件创建了一个Params的实例并传递给弹窗的UI内容childCom。

    1. 使用@ObservedV2观察Params的变化并使用@Trace装饰value使其能刷新UI。

       ```ts
       @ObservedV2
       class SceneOneOptionOneParams {
         @Trace value: string = '1';
         callback: () => void = (): void => {
         };
       }
       ```
    2. 页面数据同步到弹窗：更新dialogContent对应的自定义弹窗内容，需要使用update来进行修改。在Params参数类中可以定义一个空的callback函数，在页面组件的aboutToAppear方法中将update赋值给callback，当弹窗中数据进行更新时执行callback函数来更新WrappedBuilder对象封装的builder函数参数。

       ```ts
       aboutToAppear(): void {
         this.params.callback = () => {
           this.contentNode.update(this.params); // 用于更新WrappedBuilder对象封装的builder函数参数
         };
       }
       ```

       ```ts
       Button('修改value')
         .margin(10)
         .onClick(() => {
           this.params.value = this.params.value + '9';
           this.contentNode.update(this.params);
         });
       ```
    3. 弹窗数据同步到页面：弹窗中的TextInput组件通过onChange方法直接将输入值同步给params.value，而页面中的Text组件也通过params.value的值显示，因此实现了弹窗数据同步到页面。

       ```ts
       // TextInput是弹窗中的组件
       TextInput({
         text: params.value,
         placeholder: '你好'
       })
         .type(InputType.Normal)
         .height(40)
         .margin(10)
         .textAlign(TextAlign.Start)
         .onChange((value: string) => {
           params.value = value;
         });
       ```

       ```ts
       // Text是页面中的组件
       Text(`text:${this.params.value}`)
         .margin(10);
       ```

    完整示例代码如下：

    ```ts
    import { ComponentContent, UIContext } from '@kit.ArkUI';
    import { BusinessError } from '@kit.BasicServicesKit';

    @ObservedV2
    class SceneOneOptionOneParams {
      @Trace value: string = '1';
      callback: () => void = (): void => {
      };
    }

    @Builder
    function childComOne(params: SceneOneOptionOneParams) {
      Column() {
        Text(`${params.value}`);

        // TextInput是弹窗中的组件
        TextInput({
          text: params.value,
          placeholder: '你好'
        })
          .type(InputType.Normal)
          .height(40)
          .margin(10)
          .textAlign(TextAlign.Start)
          .onChange((value: string) => {
            params.value = value;
          });

        Blank()
          .height(10);

        Text('弹窗中修改value')
          .fontColor('#0a59f7')
          .onClick(() => {
            params.value = params.value + '0';
            params.callback();
          });
      }
      .borderRadius(16)
      .width('90%')
      .padding(20)
      .backgroundColor(Color.White);
    }

    export function showDialogOne<T extends object>(args: T, contentNode: ComponentContent<T>) {
      let uiContext = new UIContext();
      let promptActionUI = uiContext.getPromptAction();
      try {
        promptActionUI.openCustomDialog(contentNode, {
          isModal: true
        });
      } catch (error) {
        let message = (error as BusinessError).message;
        let code = (error as BusinessError).code;
        console.error(`OpenCustomDialog args error code is ${code}, message is ${message}`);
      };
    }

    @Entry
    @ComponentV2
    struct SceneOneOptionOne {
      params: SceneOneOptionOneParams = new SceneOneOptionOneParams();
      uiContext = this.getUIContext();
      contentNode = new ComponentContent(this.uiContext, wrapBuilder(childComOne), this.params);

      aboutToAppear(): void {
        this.params.callback = () => {
          this.contentNode.update(this.params); // 用于更新WrappedBuilder对象封装的builder函数参数
        };
      }

      build() {
        Column() {
          Column() {
            // Text是页面中的组件
            Text(`text:${this.params.value}`)
              .margin(10);

            Button('修改value')
              .margin(10)
              .onClick(() => {
                this.params.value = this.params.value + '9';
                this.contentNode.update(this.params);
              });
          }
          .padding(20)
          .margin(10);

          Button('打开弹窗')
            .margin(10)
            .onClick(() => {
              showDialogOne<SceneOneOptionOneParams>(this.params, this.contentNode);
            });
        }
        .width('100%')
        .height('100%')
        .alignItems(HorizontalAlign.Center);
      }
    }
    ```
  + 方案二：直接使用builder创建弹窗UI。

    该方式下由于没有ComponentContent参与无需使用update()强制更新弹窗。完整示例代码如下：

    ```ts
    @ObservedV2
    class Params {
      @Trace value: string = '1';
    }

    @Entry
    @ComponentV2
    struct SceneOneOptionTwo {
      params: Params = new Params();
      uiContext = this.getUIContext();

      @Builder
      childCom(params: Params) {
        Column() {
          Text(`${params.value}`);
          // TextInput是弹窗中的组件
          TextInput({
            text: params.value,
            placeholder: '你好'
          })
            .type(InputType.Normal)
            .height(40)
            .margin(10)
            .textAlign(TextAlign.Start)
            .onChange((value: string) => {
              params.value = value;
            });
          Blank()
            .height(10);
          Text('弹窗中修改value')
            .fontColor('#0a59f7')
            .onClick(() => {
              params.value = params.value + '0';
            });
        }
        .borderRadius(16)
        .width('90%')
        .padding(20)
        .backgroundColor(Color.White);
      }

      build() {
        Column() {
          Column() {
            // Text是页面中的组件
            Text(`text:${this.params.value}`)
              .margin(10);
            Button('修改value')
              .margin(10)
              .onClick(() => {
                this.params.value = this.params.value + '1';
              });
          }
          .padding(20)
          .margin(10);

          Button('打开弹窗')
            .margin(10)
            .onClick(() => {
              this.uiContext.getPromptAction().openCustomDialog({
                builder: () => {
                  this.childCom(this.params);
                }
              });
            });
        }
        .width('100%')
        .height('100%')
        .alignItems(HorizontalAlign.Center);
      }
    }
    ```

  场景一实现效果图如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/oNwg8U7VTJClp9Bx-OVn4A/zh-cn_image_0000002683244604.png "点击放大")
* 场景二：使用bindSheet时，如何实现弹窗和页面间的双向数据绑定？

  该场景与场景一中的方案二基本一致，只需要注意builder的使用传递规则即可，完整示例代码如下：

  ```ts
  @Builder
  export function
  sheetBuilder(items: number[]) {
    Column() {
      // 自定义滚动容器
      List({ space: '10vp' }) {
        ForEach(items, (item: number) => {
          ListItem() {
            Text(String(item)).fontSize(16).fontWeight(FontWeight.Bold);
          }.width('90%').height('80vp').backgroundColor('#ff53ecd9').borderRadius(10);
        });
      }
      .alignListItem(ListItemAlign.Center)
      .margin({ top: '10vp' })
      .width('100%')
      .height('900px')
      // 设置滚动组件的嵌套滚动属性
      .nestedScroll({
        scrollForward: NestedScrollMode.PARENT_FIRST,
        scrollBackward: NestedScrollMode.SELF_FIRST,
      });

      Text('非滚动区域')
        .width('100%')
        .backgroundColor(Color.Gray)
        .layoutWeight(1)
        .textAlign(TextAlign.Center)
        .align(Alignment.Top);
    }.width('100%').height('100%');
  }

  @Entry
  @Component
  struct SceneTwo {
    // 响应式状态变量：控制Sheet是否显示
    @State isShowSheet: boolean = false;
    // 定义菜单项数据参数
    private items: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];

    build() {
      Column() {
        Button('Open Sheet').width('90%').height('80vp')
          .onClick(() => {
            this.isShowSheet = !this.isShowSheet;
          })
          // 绑定Sheet组件：根据isShowSheet状态动态显示，传入参数items组数
          .bindSheet($$this.isShowSheet, sheetBuilder(this.items), {
            // Sheet尺寸配置：允许的展开尺寸
            detents: [SheetSize.MEDIUM, SheetSize.LARGE, 600],
            // 优先显示位置：底部弹出
            preferType: SheetType.BOTTOM,
            // 标题配置：设置Sheet标题
            title: { title: '嵌套滚动场景' },
          });
      }.width('100%').height('100%')
      .justifyContent(FlexAlign.Center);
    }
  }
  ```

  场景二实现效果如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/KN2ilZr3Q3uUd3jQplqkkQ/zh-cn_image_0000002683246076.png "点击放大")
* 场景三：使用@CustomDialog时，如何实现弹窗和页面间的双向数据绑定？

  详情可参考官方文档：[示例6（使用@Link和@Consume监听数据变化）](../harmonyos-references/ts-methods-custom-dialog-box.md#示例6使用link和consume监听数据变化)。

## 总结

一般创建弹窗UI的方式有以下三种，分别对应不同的同步弹窗与页面数据的方式：

| 创建弹窗方式 | 解决方案 |
| --- | --- |
| 使用ComponentContent创建弹窗 | 该方式需要使用自带的update方法对弹窗进行更新。 |
| 使用builder创建弹窗 | 此时弹窗的同步与刷新需要符合builder的引用传递与回调传递。 |
| 使用@CustomDialog创建弹窗 | 可直接使用状态管理的[@Link](../harmonyos-guides/arkts-link.md)、[@Provide/@Consume](../harmonyos-guides/arkts-provide-and-consume.md)同步弹窗与页面数据。 |
