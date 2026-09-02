---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-878
title: 启动页中的图片宽高比异常
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 启动页中的图片宽高比异常
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:16+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:f2d1fcee9ef534cbe1eea57081f25ed553ad133a2928aeb57d5001c4c55c8e95
---

## 问题现象

应用启动时，启动页显示的图片显示异常，图片中的字体存在明显的拉伸痕迹，文字整体被压扁了。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/1Q_4q5UOTdmr5BOyBZMTDQ/zh-cn_image_0000002658918839.png "点击放大")

## 背景知识

* [setPreferredOrientation](../harmonyos-references/arkts-apis-window-window.md#setpreferredorientation9)：设置主窗口的显示方向属性。
* [objectfit](../harmonyos-references/ts-basic-components-image.md#objectfit)：设置图片的填充效果。
* [ImageFit](../harmonyos-references/ts-appendix-enums.md#imagefit)枚举：ImageFit.Fill不保持宽高比进行放大缩小，使得图片或视频充满显示边界，对齐方式为水平居中。
* [abilities标签](../harmonyos-guides/module-configuration-file.md#abilities标签)中的orientation配置，可以标识当前UIAbility组件启动时的方向，支持配置枚举，或启动方向资源索引。

## 问题定位

1. 观察应用竖屏冷启动过程，启动页短暂竖屏展示（其中的文字显示异常）后切换为横屏展示（文字显示正常）之后再进入应用首页。
2. 使用DevEcoTesting的UIViewer工具检查UI结构，启动页中使用了Image组件展示图片。查找原始图片资源，确认其宽高是1920\*1080，适合横屏展示，但此时是竖屏显示。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/szwrq_P6SUG7F6vWYYrZhA/zh-cn_image_0000002628399624.png "点击放大")
3. 检查Image组件采用的填充效果。是ImageFit.Fill。

   ```screen
   Image($r('app.media.back_font'))
     .objectFit(ImageFit.Fill)
   ```

## 分析结论

应用冷启动时，拉起启动页未提前切换至横屏。启动页竖屏展示，且图片未保持宽高比缩放，导致启动页中的文字字体宽度不足，辨识度低。

## 修改建议

* 建议在拉起启动页前（推荐在EntryAbility的onWindowStageCreate方法中）提前旋转屏幕至横屏。

  ```screen
  import { UIAbility } from '@kit.AbilityKit';
  import { window } from '@kit.ArkUI';

  export default class EntryAbility extends UIAbility {
    onWindowStageCreate(windowStage: window.WindowStage): void {

      windowStage.loadContent('pages/SplashPage', (err) => {
        if (err.code) {
          // 异常处理
          return;
        }
        // 获取主窗口
        windowStage.getMainWindow((err, data) => {
          // 切换窗口方向为横屏
          data.setPreferredOrientation(window.Orientation.AUTO_ROTATION_LANDSCAPE_RESTRICTED);
        });
      });
    }
  }
  ```

  效果如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/xtBYw0RjS--PY3cRHs_jLg/zh-cn_image_0000002658798891.png "点击放大")
* 横屏应用可以配置应用仅支持横屏。在module.json5文件中，该文件的路径是src>main>module.json5，abilities标签下的当前UIAbility（默认是EntryAbility）中，添加orientation配置项，值为auto\_rotation\_landscape\_restricted，可以根据实际需要调整。

  ```screen
  {
    "module": {
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
          // 配置当前UIAbility组件启动时的方向为（反向）横向
          "orientation": "auto_rotation_landscape_restricted",
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
    }
  }
  ```

  效果如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/3VgH3eTnRNCZX12Uu_TiXw/zh-cn_image_0000002628559536.png "点击放大")
* 将Image组件的填充效果改为保持宽高比缩放，但该方案可能会导致竖屏显示时图片中的文字缩小/放大。

  ```screen
  @Entry
  @Component
  struct SplashPage {
    build() {
      Column() {
        Image($r('app.media.back_font'))
        // 配置图片保持宽高比适当缩放，水平居中，填充视图
          .objectFit(ImageFit.Auto)
      }
      .height('100%')
      .width('100%')
    }
  }
  ```

  效果如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/lmi6j7xUQ3S9QhtqP6MpnA/zh-cn_image_0000002658918847.png "点击放大")
