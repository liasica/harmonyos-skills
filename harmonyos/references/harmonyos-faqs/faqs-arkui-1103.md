---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1103
title: expandSafeArea常见问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > expandSafeArea常见问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:06+08:00
doc_updated_at: 2026-07-07
content_hash: sha256:533730399c099fbd9d6aa887f7d26224248a50ded1076fe45a681fed716923f7
---

## 问题现象

安全区域是指页面的显示区域，默认情况下开发者开发的界面都布局在安全区域内，不与系统设置的避让区比如状态栏、导航栏区域重叠。如果希望组件内容可以拓展到非安全区域实现沉浸式效果，可以给组件设置expandSafeArea属性扩展其绘制区域至安全区外。expandSafeArea的部分使用场景和常见问题有哪些？

| 场景 | 场景说明 |
| --- | --- |
| 场景一：横屏下组件没有规避挖孔区域 | 竖屏状态下，挖孔区域处于状态栏中，属于非安全区域，无需特意规避；横屏状态下，挖孔区域处于屏幕左侧或右侧，属于安全区域，需要控制边缘组件规避挖孔区域防止内容被遮挡。 |
| 场景二：TabContent设置expandSafeArea属性无法扩展至非安全区域 | 单独给TabContent设置expandSafeArea属性无法扩展至非安全区域。 |
| 场景三：使用expandSafeArea实现沉浸式，原有UI比例发生变化 | 组件内容扩展至非安全区域后，设置百分比高度的组件无法保持原有比例；设置固定高度的组件会在安全区域中产生空白。 |
| 场景四：给Canvas组件设置expandSafeArea属性，Canvas绘制内容无法扩展至底部导航条 | 给Canvas组件设置expandSafeArea属性，Canvas组件自身可以扩展至顶部状态栏和底部导航条，但其中绘制内容无法扩展至底部导航条。 |

场景一：横屏下组件没有规避挖孔区域。

问题现象图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/RhHCQq92TOi48E9IvNUO7A/zh-cn_image_0000002664269053.png "点击放大")

示例代码如下：

```ts
@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Row() {
        Text(`边缘控件`)
          .fontSize(30)
          .fontWeight(FontWeight.Bold)
          .width(30);
      }
      .justifyContent(FlexAlign.End)
      .height('100%')
      .width('100%')
      .backgroundColor('#f1f3f5');
    }
    .height('100%')
    .width('100%');
  }
}
```

场景二：TabContent设置expandSafeArea属性无法扩展至非安全区域。

问题现象图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/ZXeoiQj-Tn-kgkv6uFHvhw/zh-cn_image_0000002633789968.png "点击放大")

灰色为TabContent背景色。

示例代码如下：

```ts
@Entry
@Component
struct TabsExample {
  private controller: TabsController = new TabsController();

  build() {
    Column() {
      Tabs({ controller: this.controller }) {
        TabContent() {
          Column()
            .width('100%').height('100%').backgroundColor('#f1f3f5');
        }
        .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM]);

        TabContent() {
          Column().width('100%').height('100%').backgroundColor('#00CB87');
        };

        TabContent() {
          Column().width('100%').height('100%').backgroundColor('#FFBF00');
        };

        TabContent() {
          Column().width('100%').height('100%').backgroundColor('#E67C92');
        };
      }
      .barHeight(0)
      .width('100%')
      .height('100%');
    }
    .height('100%')
    .width('100%');
  }
}
```

场景三：使用expandSafeArea实现沉浸式，原有UI比例发生变化。

示例一：组件使用百分比高度时，由于状态栏高度与导航栏高度不一，拓展内容后会导致原有的UI比例发生变化。

问题现象图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/xJXmQli_RQuwQbtMLj8Bjg/zh-cn_image_0000002664269201.png "点击放大")

示例代码如下：

```ts
@Entry
@Component
struct Index4 {
  build() {
    Column() {
      Row()
        .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP])
        .width('100%')
        .height('50%')
        .backgroundColor('#E5E5EA');
      Row()
        .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.BOTTOM])
        .width('100%')
        .height('50%')
        .backgroundColor('#F1F3F5');
    }
    .height('100%')
    .width('100%');
  }
}
```

示例二：设置固定高度的组件会在安全区域中产生空白。

问题现象图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/dJ2O9JFvSW2eQ9v2lzIfzQ/zh-cn_image_0000002664269423.png "点击放大")

示例代码如下：

```ts
@Entry
@Component
struct Index6 {
  build() {
    Column() {
      Column()
        .height(300)
        .width('100%')
        .backgroundColor('#E5E5EA')
        .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP]);

      Column()
        .layoutWeight(1)
        .width('100%')
        .backgroundColor('#F1F3F5')
        .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.BOTTOM]);
    }
    .height('100%')
    .width('100%');
  }
}
```

场景四：给Canvas组件设置expandSafeArea属性，Canvas绘制内容无法扩展至底部导航条。

问题效果图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/hLuUsE7NRnGDfwv0cYdbnA/zh-cn_image_0000002633950226.png "点击放大")

其中，灰色为Canvas背景色，已经扩展至底部导航条，但fillRect方法绘制的黑色矩形与底部导航条仍有一定距离。

示例代码如下：

```ts
import { display } from '@kit.ArkUI';

@Entry
@Component
struct CanvasExample {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  @State screenWidth: number = 0;
  @State screenHeight: number = 0;

  aboutToAppear() {
    display.getAllDisplays((err, data) => {
      let screenWidth: number = data[0].width;
      this.screenWidth = this.getUIContext().px2vp(screenWidth);
      let screenHeight: number = data[0].height;
      this.screenHeight = this.getUIContext().px2vp(screenHeight);
    });
  }

  build() {
    NavDestination() {
      Canvas(this.context)
        .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM])
        .width('100%')
        .height('100%')
        .backgroundColor('#f1f3f5')
        .onReady(() => {
          this.context.fillRect(0, 0, this.screenWidth, this.screenHeight);
        });
    }
    .width('100%')
    .height('100%');
  }
}
```

## 背景知识

* [expandSafeArea](../harmonyos-references/ts-universal-attributes-expand-safe-area.md#expandsafearea)控制组件扩展其安全区域。
  + 设置expandSafeArea属性进行组件绘制扩展时，建议组件尺寸不要设置固定宽高（百分比除外），当设置固定宽高（包括设置'auto'）时，扩展安全区域的方向只支持[SafeAreaEdge.TOP, SafeAreaEdge.START]，扩展后的组件尺寸保持不变。
  + 滚动类容器内的组件不建议设置expandSafeArea属性，如果设置，需要按照组件嵌套关系，将当前节点到滚动类祖先容器间所有直接节点设置expandSafeArea属性，否则expandSafeArea属性在滚动后可能会失效。

## 解决方案

* 场景一：横屏下组件没有规避挖孔区域。

  横屏状态下，挖孔区域处于屏幕左侧或右侧，属于安全区域，此时边缘组件默认情况下会被挖孔区域遮挡。

  如果希望边缘组件避让挖孔区域，需要在模块的module.json5文件中配置metadata，完成配置后，边缘组件会避让挖孔区域，效果如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/cnOM00oBQNS53osABxzSvw/zh-cn_image_0000002664149475.png "点击放大")

  module.json5文件如下：

  ```json
  {
    "module": {
      "metadata": [
        {
          "name": "avoid_cutout", // 设置挖空区避让
          "value": "true"
        }
      ],
      "name": "entry",
      "type": "entry",
      "description": "$string:module_desc",
      "mainElement": "EntryAbility",
      "deviceTypes": [
        "phone"
      ],
      "deliveryWithInstall": true,
      "installationFree": false,
      "pages": "$profile:main_pages",
      "abilities": [
        {
          "name": "EntryAbility",
          "srcEntry": "./ets/entryability/EntryAbility.ets",
          "description": "$string:EntryAbility_desc",
          "icon": "$media:layered_image",
          "label": "$string:EntryAbility_label",
          "startWindowIcon": "$media:startIcon",
          "startWindowBackground": "$color:start_window_background",
          "exported": true,
          "skills": [
            {
              "entities": [
                "entity.system.home"
              ],
              "actions": [
                "ohos.want.action.home"
              ]
            }
          ]
        }
      ],
      "extensionAbilities": [
        {
          "name": "EntryBackupAbility",
          "srcEntry": "./ets/entrybackupability/EntryBackupAbility.ets",
          "type": "backup",
          "exported": false,
          "metadata": [
            {
              "name": "ohos.extension.backup",
              "resource": "$profile:backup_config"
            }
          ],
        }
      ]
    }
  }
  ```

  如果希望在避让的基础上，背景内容可以扩展到挖孔区域，需要给组件设置expandSafeArea属性，并向types参数中添加CUTOUT。

  示例代码如下：

  ```ts
  @Entry
  @Component
  struct Index2 {
    build() {
      RelativeContainer() {
        Row() {
          Text(`边缘控件`)
            .fontSize(30)
            .fontWeight(FontWeight.Bold)
            .width(30);
        }
        .justifyContent(FlexAlign.End)
        .height('100%')
        .width('100%')
        .backgroundColor('#f1f3f5')
        .expandSafeArea([SafeAreaType.CUTOUT], [SafeAreaEdge.START, SafeAreaEdge.END]);
      }
      .height('100%')
      .width('100%');
    }
  }
  ```

  实现效果如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/HzEuOKbfRuaxGNknXFPWpw/zh-cn_image_0000002633790496.png "点击放大")
* 场景二：TabContent设置expandSafeArea属性无法扩展至非安全区域。

  Tabs组件本身虽然不是滚动类组件，但其子组件TabContent是通过放置在一个Swiper中实现的，因此如果需要让某个TabContent可以扩展至状态栏，需要按照组件嵌套关系，将当前节点到滚动类祖先容器间所有直接节点设置expandSafeArea属性。如下代码所示，需要同时给Tabs组件，TabContent组件和TabContent内容的根节点设置expandSafeArea属性。

  ```ts
  @Entry
  @Component
  struct TabsExample {
    private controller: TabsController = new TabsController();

    build() {
      Column() {
        Tabs({ controller: this.controller }) {
          TabContent() {
            Column()
              .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM])
              .width('100%').height('100%').backgroundColor('#f1f3f5');
          }
          .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM]);

          TabContent() {
            Column().width('100%').height('100%').backgroundColor('#00CB87');
          };

          TabContent() {
            Column().width('100%').height('100%').backgroundColor('#FFBF00');
          };

          TabContent() {
            Column().width('100%').height('100%').backgroundColor('#E67C92');
          };
        }
        .expandSafeArea([SafeAreaType.SYSTEM, SafeAreaType.CUTOUT], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM])
        .barHeight(0)
        .width('100%')
        .height('100%');
      }
      .height('100%')
      .width('100%');
    }
  }
  ```

  效果图如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/qKzMXqBkRNGve0ppJ6otsQ/zh-cn_image_0000002664149683.png "点击放大")
* 场景三：使用expandSafeArea实现沉浸式，原有UI比例发生变化。
  + 示例一：组件使用百分比高度时，由于状态栏高度与导航栏高度不一，拓展内容后会导致原有的UI比例发生变化。

    解决方案：expandSafeArea的作用是扩展组件绘制区域至安全区外，它只负责延伸绘制内容，不负责保持原有比例，如果希望保持原有UI比例，建议使用setWindowLayoutFullScreen实现沉浸式，将窗口设为全屏后，页面的容器范围也变成了全屏，如果Row组件的高度设为50%，即为整个屏幕高度的50%。

    示例代码如下：

    ```ts
    import { window } from '@kit.ArkUI';

    @Entry
    @Component
    struct Index5 {
      aboutToAppear(): void {
        let windowStage = AppStorage.get('windowStage') as window.WindowStage;
        windowStage.getMainWindow().then((data) => {
          data.setWindowLayoutFullScreen(true);
        });
      }

      aboutToDisappear(): void {
        let windowStage = AppStorage.get('windowStage') as window.WindowStage;
        windowStage.getMainWindow().then((data) => {
          data.setWindowLayoutFullScreen(false);
        });
      }

      build() {
        Column() {
          Row()
            .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP])
            .width('100%')
            .height('50%')
            .backgroundColor('#E5E5EA');
          Row()
            .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.BOTTOM])
            .width('100%')
            .height('50%')
            .backgroundColor('#F1F3F5');
        }
        .height('100%')
        .width('100%');
      }
    }
    ```

    效果图如下：

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/1fjSrS51RZGS0hYcvTWCPw/zh-cn_image_0000002633950612.png "点击放大")
  + 示例二：组件使用固定高度时，使用expandSafeArea拓展到顶部，中间出现空白。

    设置expandSafeArea属性进行组件绘制扩展时，建议组件尺寸不要设置固定宽高（百分比除外），当设置固定宽高（包括设置'auto'）时，扩展安全区域的方向只支持[SafeAreaEdge.TOP, SafeAreaEdge.START]，扩展后的组件尺寸保持不变。设置百分比高度时，组件是延伸至非安全区域，设置固定高度时，组件相当于是移动并填满非安全区域而非扩展内容至非安全区域。

    解决方案：将组件高度设置为百分比高度。

* 场景四：给Canvas组件设置expandSafeArea属性，Canvas绘制内容无法扩展至底部导航条。

  解决方案：将Canvas的高度设置为固定高度，具体值为屏幕高度，即上述示例代码中的this.screenHeight。

  实现效果如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/j3SKuAZ-RQOCCtbhhPZ6ZA/zh-cn_image_0000002633950636.png "点击放大")

  注意：本文中需要用到的横竖屏切换效果和windowStage需要在EntryAbility.ets中的onWindowStageCreate方法中添加如下代码：

  ```ts
  AppStorage.setOrCreate('windowStage', windowStage);
  let windowClass: window.Window | undefined = undefined;
  windowStage.getMainWindow((err: BusinessError, data) => {
    const errCode: number = err.code;
    if (errCode) {
      console.error(`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}`);
      return;
    }
    windowClass = data;
    let orientation = window.Orientation.AUTO_ROTATION;
    try {
      let promise = windowClass.setPreferredOrientation(orientation);
      promise.then(() => {
        console.info('Succeeded in setting the window orientation.');
      }).catch((err: BusinessError) => {
        console.error(`Failed to set the window orientation. Cause code: ${err.code}, message: ${err.message}`);
      });
    } catch (exception) {
      console.error(`Failed to set window orientation. Cause code: ${exception.code}, message: ${exception.message}`);
    }
  });
  ```

## 常见FAQ

Q：expandSafeArea属性的参数中，TOP、BOTTOM、START、END，是相对什么的？会受手机横竖屏的影响吗？

A：TOP是顶部，BOTTOM是底部，START是左侧，END是右侧，这些位置受手机横竖屏影响，例如，竖屏时，挖孔区域属于顶部，右旋转横屏后，挖孔区域位于右侧，如场景一中代码所示，需要组件内容扩展到右侧挖孔区域，需要向types参数中添加CUTOUT，edges参数中添加END。
