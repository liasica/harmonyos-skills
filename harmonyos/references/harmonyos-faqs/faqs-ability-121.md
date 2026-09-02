---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-121
title: 应用启动图标动效异常，图片闪烁
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > 应用启动图标动效异常，图片闪烁
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:55+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:75be8b3ee00c14bcdb90e78bf0be8cf92bff4774edf2cc160e9de8d1cb3309e3
---

## 问题现象

应用启动时先短暂显示启动图标，再显示启动页上的图片，两个图片切换时有闪烁的问题，动效异常。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/cwHZ5EBtTVSJw7qC5N_mSA/zh-cn_image_0000002628789132.png "点击放大")

## 背景知识

module.json5配置文件中的[abilities标签](../harmonyos-guides/module-configuration-file.md#abilities标签)：其中的startWindowIcon配置项是用于配置应用启动时显示的图标。这个图标通常出现在应用启动过程中，从桌面图标过渡到应用的第一个页面（如启动页或闪屏页）时显示。应用启动时会通过startWindowIcon属性设置过渡动画的图标。

## 问题定位

检查应用配置的startWindowIcon启动图标和启动页中显示的图片是否是同一张图片。如果是同一张图片，在切换显示启动图标和启动页图片时，会存在图片闪烁问题。

## 分析结论

startWindowIcon配置和启动页展示的图片存在冲突：启动图标会在应用启动时作为过渡动画出现，然后消失，之后再显示启动页中相同的图片，即两张图片切换时会闪一下，最终导致闪烁问题。

## 修改建议

在module.json5配置中，替换startWindowIcon指向的媒体资源图片为透明图片，通过透明图标可隐藏过渡动画的显示效果，消除与主图标重复闪现问题。

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
        "startWindowIcon": "$media:none",
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
        ]
      }
    ],
    "routerMap": "$profile:router_map"
  }
}
```

"$media:none"需要替换为开发者需要的透明图片。

src/main/ets/pages/Index.ets:

```screen
// 启动页
@Entry
@Component
struct Index {
  pageInfos: NavPathStack = new NavPathStack();

  aboutToAppear(): void {
    setTimeout(() => {
      this.pageInfos.pushPath({ name: 'Main' });
    }, 2000);
  }

  build() {
    Navigation(this.pageInfos) {
      Stack() {
        // 启动图标
        Image($r('app.media.startIcon')) // $r('app.media.startIcon')需要替换为开发者需要的图片资源文件
          .width(42)
          .height(42)
          .objectFit(ImageFit.Contain)
          .margin({ top: 100 });
      }
      .height('100%')
      .width('100%');
    }
    .hideTitleBar(true)
    .height('100%')
    .width('100%')
    .mode(NavigationMode.Stack);
  }
}
```

src/main/ets/pages/Main.ets:

```screen
@Builder
export function MainBuilder() {
  Main();
}

@Entry
@Component
export struct Main {
  pageInfos: NavPathStack = new NavPathStack();

  build() {
    NavDestination() {
      // 首页内容
      RelativeContainer() {
        Text('Hello World')
          .fontSize('50fp')
          .alignRules({
            center: { anchor: '__container__', align: VerticalAlign.Center },
            middle: { anchor: '__container__', align: HorizontalAlign.Center }
          });
      }
      .height('100%')
      .width('100%');
    }
    .onBackPressed(() => {
      this.pageInfos.pop(); // 弹出路由栈栈顶元素
      return true;
    })
    .onReady((navContext: NavDestinationContext) => {
      this.pageInfos = navContext.pathStack;
    })
    .hideTitleBar(true)
    .height('100%')
    .width('100%')
    .backgroundColor(Color.White);
  }
}
```

src/main/resources/base/profile/router\_map.json:

```screen
{
  "routerMap": [
    {
      "name": "Main",
      "pageSourceFile": "src/main/ets/pages/Main.ets",
      "buildFunction": "MainBuilder"
    }
  ]
}
```

效果图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/R_C5sA5GRJql-d40tj3JJg/zh-cn_image_0000002658988443.png "点击放大")
