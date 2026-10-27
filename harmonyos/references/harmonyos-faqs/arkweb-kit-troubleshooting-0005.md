---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/arkweb-kit-troubleshooting-0005
title: ArkWeb页面跳转问题定位
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > 故障排查 > ArkWeb页面跳转问题定位
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:04+08:00
doc_updated_at: 2026-10-20
content_hash: sha256:b0996b60d1c225b1ae4242c04c1bcba2b32db18273215a1cdc9ce854fe57d682
---

## 在应用内各页面跳转时需要等待加载

### 问题现象

在应用内各页面相互跳转时，需要等待一段加载时间。

### 定位过程

1. 使用DevEco Profiler ArkWeb模板抓取应用内各页面相互跳转的Trace，搜索关键字H:NWebImpl | CreateNWeb无结果，说明应用内各页面跳转时并未创建新的Web。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/4XrC9bcqT3qu6ar_IevCuA/zh-cn_image_0000002768118980.png "点击放大")
2. 使用ArkUI Inspector发现应用从首页开始即为Web页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/vbHytbI7REG07oiSxtTS9A/zh-cn_image_0000002768118982.png "点击放大")

   使用DevEco Profiler Launch模板抓取应用启动过程Trace，搜索关键字H:NWebImpl | CreateNWeb，可以找到应用在加载主页面后创建了Web组件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/O3hL4onwTI-ZBO52FgQ47A/zh-cn_image_0000002797438939.png "点击放大")

   结合步骤1可以得出应用在启动时创建此Web，后续应用内的各页面跳转均在此Web中完成。
3. 使用DevTools分析网页内各页面跳转的性能。在“性能”页签下的“网络”模块可以看到存在下载图片资源耗时1秒以上以及执行脚本耗时1.3s以上的情况。是子资源加载、脚本运行耗时导致的页面加载耗时长。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/yNS_3J_YQRGzPHtpJTKg9Q/zh-cn_image_0000002768118984.png "点击放大")

### 分析结论

应用内各页面跳转加载耗时是网页子资源加载、脚本运行耗时较多导致。

### 修改建议

通过[预下载优化](../best-practices/bpta-web-develop-optimization.md#section11708113212514)提前下载页面所需的资源。

## Web页面内容重复加载

### 问题现象

第一次进入Web页面之后，再次进入该页面会重新加载，造成闪烁现象。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/Uz2yoQ-PSJGeWEvpjHKXvw/zh-cn_image_0000002797438969.png "点击放大")

### 定位过程

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

### 分析结论

Web组件未使用onLoadIntercept阻拦重复加载页面，页面一开始显示旧数据，新数据加载完后重新渲染页面，导致内容重复加载。

### 修改建议

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

```ts
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/uEZ1_9ScTzei44ys97rivg/zh-cn_image_0000002797439231.png "点击放大")

## 进入Web页面后，点击返回出现空白页面，再次返回正常

### 问题现象

在首页点击内容后，页面跳转到Web页面，当用户点击返回按钮想回到首页时，会出现空白页面，无法正常显示内容，但再次点击返回按钮后，页面返回到首页。

### 定位过程

页面在加载Web内容时，进度条到一半后出现重新加载的现象。是页面加载被拦截后再次跳转新的页面，导致加载页面时，初始出现短暂空白，随后页面正常加载。返回上一页时，因页面加载过程被中断或拦截，进入一个处于半加载状态的界面，呈现为空白页。在日志中，OnBeforeBrowse字段为拦截关键字：

```txt
[web_contents_impl.cc:10430] [Adblock] set adblock switch for site, frame tree node id:14 adblock switch from UI: 1
[render_frame_host_impl.cc:15523] [AdBlock] Update adblock site switch:1
[nweb_handler_delegate.cc:1524] NWebHandlerDelegate::OnBeforeBrowse
```

### 分析结论

当点击页面中自定义类型的url链接时，onLoadIntercept回调中执行了跳转到其他HarmonyOS页面，但未终止onLoadIntercept回调中代码的执行，导致执行到了最后一行返回false，表示允许此次访问。

于是Web内跳转到了链接指向的url是不存在的页面，看到Web组件显示空白的现象。

```ts
build() {
  Column() {
    Web({
      controller: this.webController,
      src: this.webUrl
    })
      .onInterceptRequest((event) => {
        if (!event) {
          return;
        }
        return null;
      })
      .onLoadIntercept((event) => {
        let url = event.data.getRequestUrl();
        if (url.includes(`xx.com`)) {
          // 加载最终的url
          this.controller.loadUrl('');
        }
        return false;
      });
  }
  .height('100%');
}
```

### 修改建议

当H5跳转链接为无需访问的链接时，可在Web组件的onLoadIntercept回调中自定义处理逻辑。处理完成后，应立即返回true，以阻止当前url的加载，从而有效拦截跳转。代码示例：

```screen
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct NavToWeb {
  @Provide('NavPathStack') pageStack: NavPathStack = new NavPathStack();

  @Builder
  PagesMap(name: string) {
    if (name === 'Page1') {
      JumpInterceptCase();
    }
  }

  build() {
    Navigation(this.pageStack) {
      Text('首页')
        .fontSize(30)
        .offset({ y: '50%' })
        .onClick(() => {
          this.pageStack.pushPathByName('Page1', '');
        });
    }
    .mode(NavigationMode.Stack)
    .navDestination(this.PagesMap);
  }
}

@Component
export struct JumpInterceptCase {
  @Consume('NavPathStack') pageStack: NavPathStack;
  controller: webview.WebviewController = new webview.WebviewController();

  @Builder
  myBuilder() {
    Column() {
      Button('content1')
        .margin(10)
        .fontSize(20);

      Button('content2')
        .margin(10)
        .fontSize(20);
    }
    .width('100%');
  }

  build() {
    NavDestination() {
      Column() {
        Row() {
          Blank().width(10)
          Text('返回')
            .onClick(() => {
              this.pageStack.pop();
            })
            .fontSize(18)
            .width('100%')
            .alignSelf(ItemAlign.Start)
        }
        Web({ src: '', controller: this.controller })
          .width('100%')
          .height('100%')
          .fileAccess(false)
          .javaScriptAccess(true)
          .domStorageAccess(true)
          .geolocationAccess(false)
          .horizontalScrollBarAccess(false)
          .verticalScrollBarAccess(false)
          .copyOptions(CopyOptions.LocalDevice)
          .onControllerAttached(() => {
            this.controller.loadUrl($rawfile('audio.html')); // 替换成开发者自己的HTML
          })
          .onInterceptRequest((event) => {
            if (!event) {
              return;
            }
            return null;
          })
          .onLoadIntercept((event) => {
            let url = event.data.getRequestUrl();
            if (url.includes(`resource://rawfile/audio.html`)) { // 替换成开发者自己的HTML
              // 加载最终的url
              this.controller.loadUrl($rawfile('webBlock.html')); // 替换成开发者自己的HTML
              return true;
            }
            return false;
          });
      }
      .width('100%')
      .height('100%');
    }
    .hideTitleBar(true)
    .mode(NavDestinationMode.STANDARD);
  }
}
```

audio.html示例代码如下：

```html
<!-- Start solution1 -->
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>播放音频</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        textarea {
            width: 100%;
            height: 100px;
        }
        button {
            margin-top: 10px;
        }
        audio {
            margin-top: 10px;
        }
    </style>
</head>
<body onload='playAudio()'>
<audio id="audioPlayer" muted="" controls></audio>
<script>
    function playAudio(hexInput) {
        // 将16进制字符串转换为二进制字节数组
        const binaryData = Uint8Array.from(hexInput.match(/.{1,2}/g), byte => parseInt(byte, 16));
        // 创建一个Blob对象
        const blob = new Blob([binaryData], { type: 'audio/mpeg' });
        // 创建一个url对应于该Blob
        const url = URL.createObjectURL(blob);
        // 设置音频元素的src属性
        const audioPlayer = document.getElementById('audioPlayer');
        audioPlayer.src = url;
        // 播放音频
        audioPlayer.play().catch(error => {
        });
    }
</script>
</body>
</html>
<!-- End solution1 -->
```

webBlock.html示例代码如下：

```html
<!--start solution7-->
<!DOCTYPE html>
<html lang="zh">
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">
    <title>简单示例</title>
</head>
<body>
<h1>欢迎</h1>
<p>这是一个简单的 HTML 页面。</p>
</body>
</html>
<!--end solution7-->
```

## 网页弹窗点击后，跳转失败停留空白页面

### 问题现象

应用网页弹窗点击“取消”后，会停留在一个空白页面。

### 定位过程

弹窗提示选择“取消”后，弹窗消失，页面保持原有空白页面。同时，侧滑后返回了上一界面。证明网页未进行返回或者跳转新页面来响应“取消”事件。

### 分析结论

应用没有对“取消”事件做返回处理。

### 修改建议

1. 使用backward返回上一页面。

   简易示例代码如下：

   ```ts
   // xxx.ets
   import { webview } from '@kit.ArkWeb';
   import { BusinessError } from '@kit.BasicServicesKit';

   @Entry
   @Component
   struct WebBackward {
     controller: webview.WebviewController = new webview.WebviewController();

     build() {
       Column() {
         Blank()
           .height(20)
         Button('返回')
           .onClick(() => {
             try {
               this.controller.backward();
             } catch (error) {
               console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
             }
           })
         Web({ src: $rawfile('one.html'), controller: this.controller })
           .fileAccess(false)
           .geolocationAccess(false)
       }
     }
   }
   ```
2. 修改网页代码，添加返回上一页面操作。

   ```html
   <!-- one.html -->
   <!DOCTYPE html>

   <html>
   <head>
       <meta charset="utf-8" name="viewport" content="width=device-width, initial-scale=1.0">
       <title>页面1</title>
       <style>
           body {
               font-family: Arial, sans-serif;
               padding: 20px;
           }
           .nav-link {
               display: inline-block;
               padding: 15px 25px;
               background: #4CAF50;
               color: white;
               text-decoration: none;
               border-radius: 5px;
           }
       </style>
   </head>
   <body>
   <h1>这是页面1</h1>
   <p>点击下方按钮跳转到页面2：</p>
   <a href="two.html" class="nav-link">前往页面2</a>
   </body>
   </html>
   ```

   ```html
   <!-- two.html -->
   <!DOCTYPE html>
   <html>
   <head>
       <meta charset="utf-8" name="viewport" content="width=device-width, initial-scale=1.0">
       <title>页面2</title>
       <style>
           body {
               font-family: Arial, sans-serif;
               padding: 20px;
           }
           .back-btn {
               display: inline-block;
               padding: 15px 25px;
               background: #f44336;
               color: white;
               text-decoration: none;
               border-radius: 5px;
               margin-bottom: 20px;
           }
       </style>
       <script>
           // 移动端侧滑返回功能
           let touchStartX = 0;
           let touchStartY = 0;

           document.addEventListener('touchstart', function(e) {
               touchStartX = e.changedTouches[0].screenX;
               touchStartY = e.changedTouches[0].screenY;
           });

           document.addEventListener('touchend', function(e) {
               const touchEndX = e.changedTouches[0].screenX;
               const touchEndY = e.changedTouches[0].screenY;

               // 右滑返回
               if (touchEndX > touchStartX + 30 && Math.abs(touchEndY - touchStartY) < 50) {
                   window.history.back();
               }
           });

           function historyBack() {
               // 返回上一级页面
               history.back();
           }

           function historyGo() {
               // 返回上一级页面
               history.go(-1);
           }

           function windowHistoryGo() {
               // 返回上一级页面
               window.history.go(-1);
           }

           function windowHistoryBack() {
               // 返回上一级页面
               window.history.back();
           }
       </script>
   </head>
   <body>
   <h1>这是页面2</h1>
   <p>点击下方按钮或者右滑跳转到页面2：</p>
   <button onclick="historyBack()" class="back-btn">historyBack返回页面1</button>
   <button onclick="historyGo()" class="back-btn">historyGo返回页面1</button>
   <button onclick="windowHistoryGo()" class="back-btn">windowHistoryGo返回页面1</button>
   <button onclick="windowHistoryBack()" class="back-btn">windowHistoryBack返回页面1</button>
   </body>
   </html>
   ```
