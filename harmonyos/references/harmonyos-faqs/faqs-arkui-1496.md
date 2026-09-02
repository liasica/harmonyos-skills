---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1496
title: Refresh下拉刷新偏移量控制问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > Refresh下拉刷新偏移量控制问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:11+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:6c747a91e87808775fe2202008abdbad0f72f51bd2dc4a5bd36c883c61be7b2f
---

## 问题现象

在实现下拉刷新功能时，Refresh如何根据下拉操作的实时偏移量来动态执行不同的逻辑？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/LczO3b1RSGe-1QeLsn2x9w/zh-cn_image_0000002628765712.png "点击放大")

## 背景知识

* [onStateChange](../harmonyos-references/ts-container-refresh.md#onstatechange)：当前刷新状态变更时，触发回调。
* [onOffsetChange](../harmonyos-references/ts-container-refresh.md#onoffsetchange12)：下拉距离发生变化时触发回调。
* [onRefreshing](../harmonyos-references/ts-container-refresh.md#onrefreshing)：进入刷新状态时触发回调。
* [cryptoFramework](../harmonyos-references/js-apis-cryptoframework.md)：对于安全要求比较高的场景，推荐使用加解密算法库框架[@ohos.security.cryptoFramework](../harmonyos-references/js-apis-cryptoframework.md)包生成安全随机数。

## 解决方案

根据[onOffsetChange](../harmonyos-references/ts-container-refresh.md#onoffsetchange12)方法判断下拉距离来实现不同的刷新效果。通过[onStateChange](../harmonyos-references/ts-container-refresh.md#onstatechange)方法中刷新的状态以及refreshOffset属性执行不同的刷新逻辑。

完整示例参考如下：

```screen
import cryptoFramework from '@ohos.security.cryptoFramework';

@Entry
@Component
struct RefreshExample {
  @State isRefreshing: boolean = false;
  // 数据源
  @State arr: String[] =
    ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20'];
  // Refresh刷新状态
  @State refreshStatus: RefreshStatus = RefreshStatus.Inactive;
  // 设置触发刷新的下拉偏移量，当下拉距离小于该属性设置值时离手不会触发刷新。
  @State refreshOffset: number = 60;
  // 设置当下拉距离超过refreshOffset时是否能触发刷新。
  @State isGettingData: boolean = false;

  // 下拉大距离的动画刷新效果
  getData() {
    setTimeout(() => {
      this.arr = Array(20)
        .fill(null)
        .map(() => Math.floor(Math.round(cryptoFramework.createRandom().generateRandomSync(1).data[0] * 40 / 255))
          .toString());
      this.isGettingData = false;
      this.isRefreshing = false;
    }, 1000);
  }

  build() {
    Column() {
      Refresh({
        refreshing: $$this.isRefreshing,
      }) {
        List() {
          ForEach(this.arr, (item: string) => {
            ListItem() {
              Text('' + item)
                .width('70%')
                .height(80)
                .fontSize(16)
                .margin(10)
                .textAlign(TextAlign.Center)
                .borderRadius(10)
                .backgroundColor(0xFFFFFF);
            };
          }, (item: string) => item);
        }
        .onScrollIndex((first: number) => {
          console.info(first.toString());
        })
        .width('100%')
        .height('100%')
        .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.BOTTOM])
        .alignListItem(ListItemAlign.Center)
        .scrollBar(BarState.Off);
      }
      .width('100%')
      .height('100%')
      .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM])
      .backgroundColor(0x89CFF0)
      .pullToRefresh(true)
      .refreshOffset(this.refreshOffset)
      // 当前刷新状态变更时，触发回调。
      .onStateChange((refreshStatus: RefreshStatus) => {
        this.refreshStatus = refreshStatus;
        // 通过判断刷新距离执行不同的方法
        if (refreshStatus === 4 && this.refreshOffset === 60) {
          console.info('执行方法a');
        } else if (refreshStatus === 4 && this.refreshOffset === 150) {
          console.info('执行方法b');
        }
      })
      // 下拉距离发生变化时触发回调
      .onOffsetChange((value: number) => {
        // 根据下拉距离不同，设置不同的触发刷新的下拉偏移量
        if (value > 150) {
          this.refreshOffset = 150;
        } else if (value < 150 && value > 0) {
          this.refreshOffset = 60;
        }
      })
      .onRefreshing(() => {
        if (this.refreshOffset === 60) {
          setTimeout(() => {
            this.isRefreshing = false;
          }, 2000);
          return;
        }
        if (this.refreshOffset === 150 && this.isGettingData === false) {
          this.isGettingData = true;
          this.getData();
        }
      });
    };
  }
}
```
