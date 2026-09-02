---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-537
title: 应用页面亮度与系统组件亮度差别大
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 应用页面亮度与系统组件亮度差别大
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:15+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:43f695cf09429672316699287a1f52ab57c5959c83a4a0dc893d3f02de3c8a86
---

## 问题现象

浏览页面时，页面的显示亮度远低于系统组件的亮度。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/pXLfNIrLTfel2qcQwdVjqA/zh-cn_image_0000002658910831.png "点击放大")

## 背景知识

* [Stack](../harmonyos-references/ts-container-stack.md)为堆叠容器，子组件按照顺序依次入栈，后一个子组件覆盖前一个子组件。
* 通过[backgroundBrightness](../harmonyos-references/ts-universal-attributes-background.md#backgroundbrightness12)方法可设置组件背景提亮效果。

## 问题定位

1. 使用DevEco Testing查看问题组件，问题组件为Stack组件的子组件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/UWLCNiOdTQuNp-6tIzu0Uw/zh-cn_image_0000002658790879.png "点击放大")
2. 查看该页面的设置，该问题组件的上层组件使用backgroundBrightness进行背景亮度设置，降低了问题组件的显示亮度。

   ```ts
   import { common } from '@kit.AbilityKit';
   import { window } from '@kit.ArkUI';

   @Entry
   @Component
   struct Index {
     aboutToAppear(): void {
       let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
       window.getLastWindow(context).then((lastWindow) => {
         lastWindow.setWindowLayoutFullScreen(true);
         let SystemBarProperties: window.SystemBarProperties = {
           statusBarColor: '#000000',
           statusBarContentColor: '#cccccc'
         };
         lastWindow.setWindowSystemBarProperties(SystemBarProperties);
       });
     }

     build() {
       Stack() {
         Column() {
           Text('我们过了江，进了车站。我买票，他忙着照看行李。行李太多了，得向脚夫行些小费，才可过去。他便又忙着和他们讲价钱。我那时真是聪明过分，总觉他说话不大漂亮，非自己插嘴不可。但他终于讲定了价钱;就送我上车。他给我拣定了靠车门的一张椅子;我将他给我做的紫毛大衣铺好座位。他嘱我路上小心，夜里要警醒些，不要受凉。又嘱托茶房好好照应我。我心里暗笑他的迂;他们只认得钱，托他们直是白托!而且我这样大年纪的人，难道还不能料理自己么?唉，我现在想想，那时真是太聪明了!\n' +
             '\n' +
             '我说道，“爸爸，你走吧。”他往车外看了看，说，“我买几个橘子去。你就在此地，不要走动。”我看那边月台的栅栏处有几个卖东西的等着顾客。走到那边月台，须穿过铁道，须跳下去又爬上去。父亲是一个胖子，走过去自然要费事些。我本来要去的，他不肯，只好让他去。我看见他戴着黑布小帽，穿着黑布大马褂，深青布棉袍，蹒跚地走到铁道边，慢慢探身下去，尚不大难。可是他穿过铁道，要爬上那边月台，就不容易了。他用两手攀着上面，两脚再向上缩;他肥胖的身子向左微倾，显出努力的样子。这时我看见他的背影，我的泪很快地流下来了。我赶紧拭干了泪，怕他看见，也怕别人看见。我再向外看时，他已抱了朱红的橘子往回走了。过铁道时，他先将橘子散放在地上，自己慢慢爬下，再抱起橘子走。到这边时，我赶紧去搀他。他和我走到车上，将橘子一股脑儿放在我的皮大衣上。于是扑扑衣上的泥土，心里很轻松似的，过一会说，“我走了;到那边来信!”我望着他走出去。他走了几步，回过头看见我，说，“进去吧，里边没人。”等他的背影混入来来往往的人里，再找不着了，我便进来坐下，我的眼泪又来了。\n' +
             '\n' +
             '近几年来，父亲和我都是东奔西走，家中光景是一日不如一日。他少年出外谋生，独力支持，做了许多大事。哪知老境却如此颓唐!他触目伤怀，自然情不能自已。情郁于中，自然要发之于外;家庭琐屑便往往触他之怒。他待我渐渐不同往日。但最近两年的不见，他终于忘却我的不好，只是惦记着我，惦记着我的儿子。我北来后，他寄了一信给我，信中说道，“我身体平安，惟膀子疼痛厉害，举箸提笔，诸多不便，大约大去之期不远矣。”我读到此处，在晶莹的泪光中，又看见那肥胖的，青布棉袍，黑布马褂的背影。唉!我不知何时再能与他相见!')
             .fontColor('#ffffff')
             .fontSize(20);
         }
         .width('100%')
         .height('100%')
         .padding({ left: 15, right: 15 });

         Stack()
           .width('100%')
           .height('100%')
           .backgroundBrightness({ rate: 0.5, lightUpDegree: -0.05 }); // 设置背景亮度，降低了底层组件的显示亮度
       }
       .height('100%')
       .width('100%')
       .padding({ top: '123px' })
       .backgroundColor(Color.Black)
       .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM]);
     }
   }
   ```

## 分析结论

问题组件的上层组件使用了backgroundBrightness进行背景亮度设置，降低了底层组件的显示亮度，导致与系统组件亮度差别大。

## 修改建议

删除该减弱页面亮度的上层组件，使页面显示亮度与系统一致。

```ts
import { common } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  aboutToAppear(): void {
    let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
    window.getLastWindow(context).then((lastWindow) => {
      lastWindow.setWindowLayoutFullScreen(true);
      let SystemBarProperties: window.SystemBarProperties = {
        statusBarColor: '#000000',
        statusBarContentColor: '#cccccc'
      };
      lastWindow.setWindowSystemBarProperties(SystemBarProperties);
    })
      .catch((err: BusinessError) => {
        console.error('Failed to get last window:', err);
      });
  }

  build() {
    Stack() {
      Column() {
        Text('我们过了江，进了车站。我买票，他忙着照看行李。行李太多了，得向脚夫行些小费，才可过去。他便又忙着和他们讲价钱。我那时真是聪明过分，总觉他说话不大漂亮，非自己插嘴不可。但他终于讲定了价钱;就送我上车。他给我拣定了靠车门的一张椅子;我将他给我做的紫毛大衣铺好座位。他嘱我路上小心，夜里要警醒些，不要受凉。又嘱托茶房好好照应我。我心里暗笑他的迂;他们只认得钱，托他们直是白托!而且我这样大年纪的人，难道还不能料理自己么?唉，我现在想想，那时真是太聪明了!\n' +
          '\n' +
          '我说道，“爸爸，你走吧。”他往车外看了看，说，“我买几个橘子去。你就在此地，不要走动。”我看那边月台的栅栏处有几个卖东西的等着顾客。走到那边月台，须穿过铁道，须跳下去又爬上去。父亲是一个胖子，走过去自然要费事些。我本来要去的，他不肯，只好让他去。我看见他戴着黑布小帽，穿着黑布大马褂，深青布棉袍，蹒跚地走到铁道边，慢慢探身下去，尚不大难。可是他穿过铁道，要爬上那边月台，就不容易了。他用两手攀着上面，两脚再向上缩;他肥胖的身子向左微倾，显出努力的样子。这时我看见他的背影，我的泪很快地流下来了。我赶紧拭干了泪，怕他看见，也怕别人看见。我再向外看时，他已抱了朱红的橘子往回走了。过铁道时，他先将橘子散放在地上，自己慢慢爬下，再抱起橘子走。到这边时，我赶紧去搀他。他和我走到车上，将橘子一股脑儿放在我的皮大衣上。于是扑扑衣上的泥土，心里很轻松似的，过一会说，“我走了;到那边来信!”我望着他走出去。他走了几步，回过头看见我，说，“进去吧，里边没人。”等他的背影混入来来往往的人里，再找不着了，我便进来坐下，我的眼泪又来了。\n' +
          '\n' +
          '近几年来，父亲和我都是东奔西走，家中光景是一日不如一日。他少年出外谋生，独力支持，做了许多大事。哪知老境却如此颓唐!他触目伤怀，自然情不能自已。情郁于中，自然要发之于外;家庭琐屑便往往触他之怒。他待我渐渐不同往日。但最近两年的不见，他终于忘却我的不好，只是惦记着我，惦记着我的儿子。我北来后，他寄了一信给我，信中说道，“我身体平安，惟膀子疼痛厉害，举箸提笔，诸多不便，大约大去之期不远矣。”我读到此处，在晶莹的泪光中，又看见那肥胖的，青布棉袍，黑布马褂的背影。唉!我不知何时再能与他相见!')
          .fontColor('#ffffff')
          .fontSize(20);
      }
      .width('100%')
      .height('100%')
      .padding({ left: 15, right: 15 });

      // 不设置减弱页面亮度的上层组件
    }
    .height('100%')
    .width('100%')
    .padding({ top: '123px' })
    .backgroundColor(Color.Black)
    .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM]);
  }
}
```

效果图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/b6h4ocYAQb2cXjFSJ4Ys8Q/zh-cn_image_0000002628551514.png "点击放大")
