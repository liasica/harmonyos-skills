---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-105
title: Web页面内容重复加载
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > Web页面内容重复加载
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:32+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:534b81583442802e0696209080b078b54690d1b07d2eb37970ebb6ae3628fd38
---

## 问题现象

第一次进入Web页面之后，再次进入该页面会重新加载，造成闪烁现象。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/_Is1iYANT-iMtH8omL4r9Q/zh-cn_image_0000002628899126.png "点击放大")

## 背景知识

* [Web](../harmonyos-references/arkts-basic-components-web.md)组件提供网页显示的能力。
* [loadUrl](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#loadurl)可加载指定的URL。
* [onLoadIntercept](../harmonyos-references/arkts-basic-components-web-events.md#onloadintercept10)：当Web组件加载URL之前触发该回调，用于判断是否阻止此次访问。

## 问题定位

查看Web组件的设置，Web组件在显示后使用loadUrl加载Web页面，且未使用onLoadIntercept阻拦重复加载页面。

```ts
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebVideo {
  controller: webview.WebviewController = new webview.WebviewController();
  @State showWeb: boolean = false;

  onBackPress(): boolean | void {
    if (this.showWeb) {
      this.showWeb = false;
      return true;
    } else {
      return false;
    }
  }

  build() {
    Stack() {
      Button('显示Web页面')
        .fontSize(20)
        .fontColor(Color.White)
        .type(ButtonType.Capsule)
        .width(200)
        .height(50)
        .backgroundColor('#0A59F7')
        .onClick(() => {
          this.showWeb = true;
        });

      Web({ src: '', controller: this.controller })
        .height('100%')
        .width('100%')
        .fileAccess(true)
        .geolocationAccess(false)
        .initialScale(90)
        .visibility(this.showWeb ? Visibility.Visible : Visibility.Hidden)
        .onVisibleAreaChange([0.0, 1.0], (isExpanding: boolean, currentRatio: number) => {
          if (isExpanding && currentRatio >= 1.0) {
            // 模拟获取数据延迟
            setTimeout(() => {
              this.controller.loadUrl($rawfile('text3.html')); // 加载Web页面
            }, 2000);
          }
        })
        .transition(
          TransitionEffect
            .move(TransitionEdge.END)
            .animation({
              duration: 500
            })
        );
      // 未使用onLoadIntercept阻拦重复加载页面
    }
    .height('100%')
    .width('100%');
  }
}
```

## 分析结论

Web组件未使用onLoadIntercept阻拦重复加载页面，页面一开始显示旧数据，新数据加载完后重新渲染页面，导致内容重复加载。

## 修改建议

Web组件使用onLoadIntercept接口，当即将跳转的页面与当前页面相同时进行阻拦，避免重复加载页面。

```ts
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebVideo {
  controller: webview.WebviewController = new webview.WebviewController();
  @State showWeb: boolean = false;
  lastUrl: string = '';

  onBackPress(): boolean | void {
    if (this.showWeb) {
      this.showWeb = false;
      return true;
    } else {
      return false;
    }
  }

  build() {
    Stack() {
      Button('显示Web页面')
        .fontSize(20)
        .fontColor(Color.White)
        .type(ButtonType.Capsule)
        .width(200)
        .height(50)
        .backgroundColor('#0A59F7')
        .onClick(() => {
          this.showWeb = true;
        });

      Web({ src: '', controller: this.controller })
        .height('100%')
        .width('100%')
        .fileAccess(true)
        .geolocationAccess(false)
        .initialScale(90)
        // 使用onLoadIntercept阻拦重复加载页面
        .onLoadIntercept((event) => {
          let url = event.data.getRequestUrl();
          // 跳转的页面与当前页面相同时进行阻拦
          if (this.lastUrl === url) {
            return true;
          } else {
            this.lastUrl = url;
            return false;
          }
        })
        .visibility(this.showWeb ? Visibility.Visible : Visibility.Hidden)
        .onVisibleAreaChange([0.0, 1.0], (isExpanding: boolean, currentRatio: number) => {
          if (isExpanding && currentRatio >= 1.0) {
            // 模拟获取数据延迟
            setTimeout(() => {
              this.controller.loadUrl($rawfile('text3.html')); // 加载Web页面
            }, 2000);
          }
        })
        .transition(
          TransitionEffect
            .move(TransitionEdge.END)
            .animation({
              duration: 500
            })
        );
    }
    .height('100%')
    .width('100%');
  }
}
```

src/main/resources/rawfile/text3.html：

```html
<!DOCTYPE html>
<html lang="en" style="font-size: 54px" data-dpr="1">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>古文展示</title>
    <style>
        body {
          font-size: 18px;
          height: 100%;
          width: 100%;
          padding: 20px;
        }

        .hidden {
          display: none;
        }
    </style>
</head>

<body>
<div id="contentA" class="hidden">
    六王毕，四海一，蜀山兀，阿房出。覆压三百余里，隔离天日。骊山北构而西折，直走咸阳。二川溶溶，流入宫墙。五步一楼，十步一阁；廊腰缦回，檐牙高啄；各抱地势，钩心斗角。盘盘焉，囷囷焉，蜂房水涡，矗不知其几千万落。长桥卧波，未云何龙？复道行空，不霁何虹？高低冥迷，不知西东。歌台暖响，春光融融；舞殿冷袖，风雨凄凄。一日之内，一宫之间，而气候不齐。(不知其 一作：不知乎；西东 一作：东西)

    　　妃嫔媵嫱，王子皇孙，辞楼下殿，辇来于秦。朝歌夜弦，为秦宫人。明星荧荧，开妆镜也；绿云扰扰，梳晓鬟也；渭流涨腻，弃脂水也；烟斜雾横，焚椒兰也。雷霆乍惊，宫车过也；辘辘远听，杳不知其所之也。一肌一容，尽态极妍，缦立远视，而望幸焉。有不见者，三十六年。燕赵之收藏，韩魏之经营，齐楚之精英，几世几年，剽掠其人，倚叠如山。一旦不能有，输来其间。鼎铛玉石，金块珠砾，弃掷逦迤，秦人视之，亦不甚惜。(有不见者 一作：有不得见者)
</div>
<div id="contentB" class="hidden">

    　　嗟乎！一人之心，千万人之心也。秦爱纷奢，人亦念其家。奈何取之尽锱铢，用之如泥沙？使负栋之柱，多于南亩之农夫；架梁之椽，多于机上之工女；钉头磷磷，多于在庾之粟粒；瓦缝参差，多于周身之帛缕；直栏横槛，多于九土之城郭；管弦呕哑，多于市人之言语。使天下之人，不敢言而敢怒。独夫之心，日益骄固。戍卒叫，函谷举，楚人一炬，可怜焦土！
</div>
<div id="contentC" class="hidden">
    　　呜呼！灭六国者六国也，非秦也；族秦者秦也，非天下也。嗟乎！使六国各爱其人，则足以拒秦；使秦复爱六国之人，则递三世可至万世而为君，谁得而族灭也？秦人不暇自哀，而后人哀之；后人哀之而不鉴之，亦使后人而复哀后人也。
</div>

<script>
    // 模拟逐渐显示页面
    setTimeout(() => {
      document.getElementById("contentA").classList.remove("hidden");
    }, 500);

    setTimeout(() => {
      document.getElementById("contentB").classList.remove("hidden");
    }, 1000);

    setTimeout(() => {
      document.getElementById("contentC").classList.remove("hidden");
    }, 1500);
</script>

</body>

</html>
```

效果图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/Cj5q3wIyQcqVyXwhUomyAw/zh-cn_image_0000002659138395.png "点击放大")
